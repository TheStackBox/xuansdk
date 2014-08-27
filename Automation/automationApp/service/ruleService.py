##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
#    Xuan Automation Application is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
import bisect
import copy
import json
import time

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.eventTracker import EventTracker
from automationApp.core.methodTracker import MethodTracker
from automationApp.core.storage import Storage
from automationApp.core.triggerTracker import TriggerTracker
from automationApp.dto.groupDTO import GroupDTO
from automationApp.dto.methodDTO import MethodDTO
from automationApp.dto.ruleDTO import RuleDTO
from automationApp.module.timerModule import TimerModule
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator


class RuleContainer(object):

    def __init__(self):
        self.__rules = {}
        self.__ruleSequence = []

    def rule_count(self):
        return len(self.__ruleSequence)

    def set(self, ruleId, ruleDTO):
        self.__rules[ruleId] = ruleDTO
        if ruleId not in self.__ruleSequence:
            bisect.insort(self.__ruleSequence, ruleId)

    def unset(self, ruleId):
        try:
            del(self.__rules[ruleId])
        except:
            pass

        try:
            self.__ruleSequence.remove(ruleId)
        except:
            pass

    def has_id(self, ruleId):
        return ruleId in self.__rules

    def get_by_id(self, ruleId):
        return self.__rules[ruleId]

    def list(self, offset, limit):
        return self.__ruleSequence[offset:limit]

    
class RuleTriggerController(object):
    
    def __init__(self):
        self.triggerTime = 0 # Keep track of last timestamp when rule triggered.
        self.triggerReset = False # Only set to True when rule is disabled or just set.


class RuleService(object):

    def __init__(self, fireEventFunc=None):
        self.__fireEventFunc = fireEventFunc

        self.__ruleContainer = RuleContainer()

        self.__methodTracker = MethodTracker(self.__method_tracker_update_notify)
        self.__eventTracker = EventTracker(self.__event_tracker_event_callback)
        self.__triggerTracker = TriggerTracker()

        self.__ruleTriggerController = {} # Control rule do not let it execute too many times in a short period of time.

        #=======================================================================
        # Load rules from database
        #=======================================================================
        rules = Storage.list_all_rules()
        for rule in rules:
            AppConstants.get_thread_pool_executor().submit(self.set_rule, **rule)

    def set_rule(self, trigger, condition, execution, ruleId=None, ruleName=None, enabled=True):

        def __validate_max_rule_size():
            if self.__ruleContainer.rule_count() >= AppConstants.MAX_RULE_SIZE:
                raise AutomationException(1708, "Rule size cannot be more than " + str(AppConstants.MAX_RULE_SIZE))

        #=======================================================================
        # Get RuleDTO object, create new id if necessary
        #=======================================================================
        if Util.is_empty(ruleId):
            __validate_max_rule_size()
            while True:
                ruleId = str(time.time())
                if not self.__ruleContainer.has_id(ruleId): # prevent uuid collision
                    ruleDTO = RuleDTO(**{RuleDTO.PROP_RULE_ID:ruleId})
                    break
        elif self.__ruleContainer.has_id(ruleId):
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)

            if ruleDTO.get_status_processed() != RuleDTO.RULE_STATUS_PROCESSED_UPDATED:
                raise AutomationException(1704, "Rule is under processing")

            self.__enable_rule(ruleId, False)
        else:
            __validate_max_rule_size()
            ruleDTO = RuleDTO(**{RuleDTO.PROP_RULE_ID:ruleId})

        #=======================================================================
        # Validates all inputs, make sure inputs are in correct format
        #=======================================================================
        if isinstance(trigger, str):
            try:
                trigger = json.loads(trigger)
            except Exception:
                raise AutomationException(1701, "invalid json string in param: trigger")

        triggerDTO = self.__triggerTracker.parse_to_trigger_dto(trigger)

        def __validate_method_object(methodList):
            if not isinstance(methodList, list):
                raise AutomationException(1097, "List is required for both 'condition' and 'execution'")

            #===================================================================
            # Check allowed size, raise error if exceeded.
            #===================================================================
            if len(methodList) > AppConstants.MAX_METHOD_SIZE:
                raise AutomationException(1706, "Only " + str(AppConstants.MAX_METHOD_SIZE) + " is allowed for each 'condition' and 'execution'")

            #===================================================================
            # Check if all kbxMethodIds are valid and all kbxMethodParams are list
            #===================================================================
            idValidator = NumberValidator(isRequired=True, minVal=1, decimalPoint=0)
            if not all([idValidator.is_valid(eachMethod[MethodDTO.PROP_METHOD_ID])
                        and isinstance(eachMethod[MethodDTO.PROP_METHOD_ARGS], list)
                        for eachMethod in methodList]):
                raise AutomationException(1097, "'condition' and 'execution' have invalid data structure")

            #===================================================================
            # Check if all kbxParamName and kbxParamCurrentValue exists
            #===================================================================
            paramNameValidator = StringValidator(isRequired=True)
            for eachMethod in methodList:
                methodArgs = eachMethod[MethodDTO.PROP_METHOD_ARGS]
                for methodArg in methodArgs:
                    if not paramNameValidator.is_valid(methodArg[AppConstants.ARG_NAME]):
                        raise AutomationException(1097, "'condition' and 'execution' have invalid params structure")

                    if not AppConstants.ARG_CURRENT_VALUE in methodArg:
                        raise AutomationException(1097, "'condition' and 'execution' current value is missing")

        if isinstance(condition, str):
            try:
                condition = json.loads(condition)
            except Exception:
                raise AutomationException(1701, "invalid json string in param: condition")

        __validate_method_object(condition)

        if isinstance(execution, str):
            try:
                execution = json.loads(execution)
            except Exception:
                raise AutomationException(1701, "invalid json string in param: execution")

        __validate_method_object(execution)

        #=======================================================================
        # Set basic information of the rule
        #=======================================================================
        ruleDTO.set_rule_id(ruleId)
        ruleDTO.set_rule_name(ruleName)
        ruleDTO.set_enabled(enabled)

        ruleDTO.set_trigger(triggerDTO)
        ruleDTO.set_status_processed(RuleDTO.RULE_STATUS_PROCESSED_UPDATING)


        #=======================================================================
        # Append if its new rule
        #=======================================================================
        if not self.__ruleContainer.has_id(ruleId):
            self.__ruleContainer.set(ruleId, ruleDTO)

        ruleTriggerController = RuleTriggerController()
        ruleTriggerController.triggerReset = True
        self.__ruleTriggerController[ruleId] = ruleTriggerController

        #=======================================================================
        # Fire rule update start event
        #=======================================================================
        self.__fire_rule_update_started_event(ruleId)

        #=======================================================================
        # Submit to a thread to process other info, and return... performance...
        #=======================================================================
        AppConstants.get_thread_pool_executor().submit(self.__create_rule, ruleDTO, condition, execution)

    def delete_rule(self, ruleId):
        self.__check_rule_process_status(ruleId)

        #=======================================================================
        # Remove trigger and event listener
        #=======================================================================
        try:
            self.__enable_rule(ruleId, False)
        except Exception as e:
            Logger.log_debug("Unable to disable rule upon delete:", e)

        #=======================================================================
        # Remove entries in method trackers
        #=======================================================================
        try:
            self.__methodTracker.update_method(ruleId)
        except Exception as e:
            Logger.log_debug("Unable to update method tracker:", e)

        #=======================================================================
        # Remove entries in ruleService
        #=======================================================================
        try:
            self.__ruleContainer.unset(ruleId)
            del(self.__ruleTriggerController[ruleId])
        except Exception as e:
            Logger.log_debug("Unable to remove rule from rule container:", e)

        #=======================================================================
        # Remove from app storage
        #=======================================================================
        try:
            Storage.delete_rule(ruleId)
            Logger.log_debug(ruleId, "removed from storage.")
        except Exception as e:
            Logger.log_debug("Unable to remove rule from storage:", e)

    def get_rule(self, ruleId, language=AppInfo.DEFAULT_API_LANGUAGE):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
            ruleDTO = copy.deepcopy(ruleDTO)
        except:
            raise AutomationException(1707, "Rule Id not found")

        condDTOs = ruleDTO.get_conditions()
        execDTOs = ruleDTO.get_executions()

        methodDTOs = condDTOs + execDTOs
        methodIds = [methodDTO.get_method_id() for methodDTO in methodDTOs]

        self.__methodTracker.update_language(language, methodIds)

        statusCodeOfRemoved = (AppConstants.METHOD_ERROR_METHOD_REMOVED[0], AppConstants.METHOD_ERROR_GROUP_REMOVED[0])
        
        for condDTO in condDTOs:
            try:
                #===============================================================
                # Update method
                #===============================================================
                args = condDTO.get_method_args()
                mapArgs = {arg[AppConstants.ARG_NAME]:arg[AppConstants.ARG_CURRENT_VALUE] for arg in args}

                #===============================================================
                # Update arguments
                #===============================================================
                condDTO.update(self.__methodTracker.get_method(condDTO.get_method_id()))
                if condDTO.get_status_code() in statusCodeOfRemoved:
                    condDTO.set_method_args(None)
                else:
                    processedArgs = condDTO.get_method_args()
                    for processedArg in processedArgs:
                        processedArg[AppConstants.ARG_CURRENT_VALUE] = mapArgs.get(processedArg[AppConstants.ARG_NAME])
            except:
                continue

        for execDTO in execDTOs:
            try:
                args = execDTO.get_method_args()
                mapArgs = {arg[AppConstants.ARG_NAME]:arg[AppConstants.ARG_CURRENT_VALUE] for arg in args}

                execDTO.update(self.__methodTracker.get_method(execDTO.get_method_id()))
                if execDTO.get_status_code() in statusCodeOfRemoved:
                    execDTO.set_method_args(None)
                else:
                    processedArgs = execDTO.get_method_args()
                    for processedArg in processedArgs:
                        processedArg[AppConstants.ARG_CURRENT_VALUE] = mapArgs.get(processedArg[AppConstants.ARG_NAME])
            except:
                continue

        return ruleDTO

    def list_rules(self, offset=0, limit=200):
        rules = []
        for ruleId in (ruleId for ruleId in self.__ruleContainer.list(offset, limit)):
            try:
                ruleDTO = self.__get_rule_summary(ruleId)
                rules.append(self.__filter_rule_summary(ruleDTO))
            except Exception as e:
                ruleDTO = self.__ruleContainer.get_by_id(ruleId)
                rules.append(self.__filter_rule_summary(ruleDTO))
                Logger.log_debug(e)
        
        return rules, self.__ruleContainer.rule_count()

    def trigger_rule(self, ruleId, checkCondition=False, eventTag=None, eventData=None):
        self.__check_rule_process_status(ruleId)

        AppConstants.get_thread_pool_executor().submit(self.__trigger_rule, ruleId, checkCondition, eventTag, eventData)

    def enable_rule(self, ruleId, enabled):
        self.__check_rule_process_status(ruleId)

        if not isinstance(enabled, bool):
            raise AutomationException(1097, "Invalid parameter 'enabled'")
        
        if enabled is False:
            self.__ruleTriggerController[ruleId].triggerReset = True

        AppConstants.get_thread_pool_executor().submit(self.__enable_rule, ruleId, enabled)

    def __check_rule_process_status(self, ruleId):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
        except:
            raise AutomationException(1707, "Rule Id not found")

        if ruleDTO.get_status_processed() != RuleDTO.RULE_STATUS_PROCESSED_UPDATED:
            raise AutomationException(1704, "Rule is under processing")
        
    def __filter_rule_summary(self, ruleDTO):
        return {RuleDTO.PROP_RULE_ID:ruleDTO.get_rule_id(),
                RuleDTO.PROP_RULE_NAME:ruleDTO.get_rule_name(),
                RuleDTO.PROP_RULE_TYPE:ruleDTO.get_rule_type(),
                RuleDTO.PROP_ENABLED:ruleDTO.get_enabled(),
                RuleDTO.PROP_STATUS_CODE:ruleDTO.get_status_code(),
                RuleDTO.PROP_STATUS_MESSAGE:ruleDTO.get_status_message(),
                RuleDTO.PROP_STATUS_PROCESSED:ruleDTO.get_status_processed(),
                RuleDTO.PROP_CONDITION:[{GroupDTO.PROP_GROUP_ICON:methodDTO.get(GroupDTO.PROP_GROUP_ICON),
                                         MethodDTO.PROP_GROUP_ID:methodDTO.get_group_id(),
                                         MethodDTO.PROP_STATUS_CODE:methodDTO.get_status_code(),
                                         MethodDTO.PROP_STATUS_MESSAGE:methodDTO.get_status_message()} for methodDTO in ruleDTO.get_conditions()],
                RuleDTO.PROP_EXECUTION:[{GroupDTO.PROP_GROUP_ICON:methodDTO.get(GroupDTO.PROP_GROUP_ICON),
                                         MethodDTO.PROP_GROUP_ID:methodDTO.get_group_id(),
                                         MethodDTO.PROP_STATUS_CODE:methodDTO.get_status_code(),
                                         MethodDTO.PROP_STATUS_MESSAGE:methodDTO.get_status_message()} for methodDTO in ruleDTO.get_executions()]}

    def __get_rule_summary(self, ruleId):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
        except:
            raise AutomationException(1707, "Rule Id not found")
        
        if ruleDTO.get_status_processed() != RuleDTO.RULE_STATUS_PROCESSED_UPDATED:
            raise AutomationException(1704, "Rule is updating")
        
        ruleDTO = copy.deepcopy(ruleDTO)

        for condDTO in ruleDTO.get_conditions():
            try:
                condDTO.update(self.__methodTracker.get_method(condDTO.get_method_id()))

                #===============================================================
                # Aggregate group icon
                #===============================================================
                groupDTO = self.__methodTracker.get_group(condDTO.get_group_id())
                condDTO[GroupDTO.PROP_GROUP_ICON] = groupDTO.get_group_icon()
            except:
                continue

        for execDTO in ruleDTO.get_executions():
            try:
                execDTO.update(self.__methodTracker.get_method(execDTO.get_method_id()))

                groupDTO = self.__methodTracker.get_group(execDTO.get_group_id())
                execDTO[GroupDTO.PROP_GROUP_ICON] = groupDTO.get_group_icon()
            except:
                continue

        return ruleDTO

    def __enable_rule(self, ruleId, enabled):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
        except:
            return

        if ruleDTO.get_status_processed() != RuleDTO.RULE_STATUS_PROCESSED_UPDATED:
            return

        if not isinstance(enabled, bool):
            return

        ruleDTO.set_enabled(enabled)

        if enabled is True:
            condDTOs = ruleDTO.get_conditions()

            methodIds = []
            for condDTO in condDTOs:
                methodId = condDTO.get_method_id()
                methodIds.append(methodId)
                #===============================================================
                # Whole Chunks of code here just to integrate with Timer Module!!
                #===============================================================
                if methodId == TimerModule.METHOD_ID_DAILY_TASK:
                    methodParams = condDTO.get_method_args()
                    timeValue = None
                    for methodParam in methodParams:
                        if methodParam.get(AppConstants.ARG_NAME) == "time":
                            timeValue = methodParam.get(AppConstants.ARG_CURRENT_VALUE)
                            break

                    AppConstants.get_thread_pool_executor().submit(TimerModule.add_daily_task_scheduler, ruleId, timeValue)

            tags = self.__methodTracker.get_tags_by_id(methodIds)
            if len(tags) > 0:
                self.__eventTracker.update_listener(ruleId, *tags)

            self.__triggerTracker.register_listener(ruleId, ruleDTO.get_trigger())

            #===================================================================
            # Execute once if its not a scene and no timer callback
            #===================================================================
            if self.__ruleTriggerController[ruleId].triggerReset is True:
                self.__ruleTriggerController[ruleId].triggerReset = False
                if ruleDTO.get_trigger().is_no_callback() and len(tags) > 0:
                    AppConstants.get_thread_pool_executor().submit(self.trigger_rule, ruleId=ruleId, checkCondition=True)
                    

        else:
            #===============================================================
            # Whole Chunks of code here just to integrate with Timer Module!!
            #===============================================================
            condDTOs = ruleDTO.get_conditions()
            for condDTO in condDTOs:
                methodId = condDTO.get_method_id()
                if methodId == TimerModule.METHOD_ID_DAILY_TASK:
                    methodParams = condDTO.get_method_args()
                    timeValue = None
                    for methodParam in methodParams:
                        if methodParam.get(AppConstants.ARG_NAME) == "time":
                            timeValue = methodParam.get(AppConstants.ARG_CURRENT_VALUE)
                            break

                    AppConstants.get_thread_pool_executor().submit(TimerModule.delete_daily_task_scheduler, ruleId, timeValue)
            #===================================================================
            # Timer Module integration ends!!!
            #===================================================================

            self.__eventTracker.update_listener(ruleId)
            self.__triggerTracker.unregister_listener(ruleId)

        #=======================================================================
        # Update app storage..
        # Looks like all changes will execute this function at the end
        #=======================================================================
        Storage.store_rule(ruleDTO)

    def __create_rule(self, ruleDTO, condition, execution):
        ruleId = ruleDTO.get_rule_id()

        try:
            #=======================================================================
            # Add methods to subscribe list
            #=======================================================================
            condDTOs = [MethodDTO(**eachCond) for eachCond in condition]
            execDTOs = [MethodDTO(**eachExec) for eachExec in execution]

            methodIds = [methodDTO.get_method_id() for methodDTO in condDTOs + execDTOs]
            self.__methodTracker.update_method(ruleId, *methodIds)

            #=======================================================================
            # Set Conditions, Executions, and Rule Type
            #=======================================================================
            ruleDTO.set_conditions(condDTOs)
            ruleDTO.set_executions(execDTOs)

            if len(condDTOs) == 0 and ruleDTO.get_trigger().is_no_callback():
                ruleDTO.set_rule_type(RuleDTO.RULE_TYPE_SCENE)
            else:
                ruleDTO.set_rule_type(RuleDTO.RULE_TYPE_RULE)

            #=======================================================================
            # Update rule status code
            #=======================================================================
            self.__update_rule_status(ruleId)

        except Exception as e:
            Logger.log_debug(e)

    def __trigger_rule(self, ruleId, checkCondition=False, eventTag=None, eventData=None):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
        except:
            return

        currentTime = time.time()

        #=======================================================================
        # Block if last execution is less than 500 ms
        #=======================================================================
        try:
            lastTriggerTime = self.__ruleTriggerController[ruleId].triggerTime
            triggerInterval = currentTime - lastTriggerTime
            if triggerInterval < AppConstants.MIN_TRIGGER_INTERVAL:
                Logger.log_debug("Rule Execution Blocked --- Triggered again in ", triggerInterval, " sec")
                return
            else:
                self.__ruleTriggerController[ruleId].triggerTime = currentTime
        except Exception as e:
            Logger.log_debug("Spamming Protection Error: ", e)
            self.__ruleTriggerController[ruleId].triggerTime = currentTime

        try:
            #=======================================================================
            # Execute conditions
            #=======================================================================
            if checkCondition is True:
                condDTOs = ruleDTO.get_conditions()
                for condDTO in condDTOs:
                    methodId = condDTO.get_method_id()
    
                    methodDTOWithInfo = self.__methodTracker.get_method(methodId)
                    methodName = methodDTOWithInfo.get_method_name()
                    methodStatusCode = methodDTOWithInfo.get_status_code()
                    if methodStatusCode != AppConstants.METHOD_ERROR_OK[0]:
                        Logger.log_debug("Rule Exec --- Cond Checking (%s) --- %s --- STOP EXECUTION" % (str(methodName), str(methodDTOWithInfo.get_status_message())))
                        return
                    else:
                        methodArgs = condDTO.get_method_args()
    
                        kwargs = {methodArg[AppConstants.ARG_NAME]:methodArg[AppConstants.ARG_CURRENT_VALUE] for methodArg in methodArgs}
                        kwargs["kbxMethodId"] = methodId
    
                        if eventTag is not None:
                            kwargs[AppConstants.KEY_CONDITION_EVENT_TAG] = eventTag
                            kwargs[AppConstants.KEY_CONDITION_EVENT_DATA] = eventData
    
                        if AppInfo.REQUEST_KEY_LANGUAGE not in kwargs:
                            kwargs[AppInfo.REQUEST_KEY_LANGUAGE] = AppInfo.DEFAULT_API_LANGUAGE
    
                        kwargs[AppConstants.KEY_CONDITION_TIMESTAMP] = currentTime
    
                        result = SharedMethod.call_by_method_id(**kwargs)
    
                        if result[AppConstants.KEY_CONDITION_RESPONSE] is not True:
                            Logger.log_debug("Rule Exec --- Cond Checking (%s) --- Result (%s) --- STOP EXECUTION" % (str(methodName), str(result)))
                            return # Condition checking failed
                        else:
                            Logger.log_debug("Rule Exec --- Cond Checking (%s) --- Result (%s) --- CONTINUE EXECUTION" % (str(methodName), str(result)))
    
            #=======================================================================
            # Execute actions
            #=======================================================================
            execDTOs = ruleDTO.get_executions()
            for execDTO in execDTOs:
                methodId = execDTO.get_method_id()
    
                methodDTOWithInfo = self.__methodTracker.get_method(methodId)
                methodName = methodDTOWithInfo.get_method_name()
                methodStatusCode = methodDTOWithInfo.get_status_code()
    
                if methodStatusCode != AppConstants.METHOD_ERROR_OK[0]:
                    Logger.log_debug("Rule Exec --- Run Action (%s) --- %s --- SKIP ACTION" % (str(methodName), str(methodDTOWithInfo.get_status_message())))
                    continue
                else:
                    methodArgs = execDTO.get_method_args()
    
                    kwargs = {methodArg[AppConstants.ARG_NAME]:methodArg[AppConstants.ARG_CURRENT_VALUE] for methodArg in methodArgs}
                    kwargs["kbxMethodId"] = methodId
    
                    kwargs[AppConstants.KEY_ACTION_TIMESTAMP] = currentTime
                    
                    Logger.log_debug("Rule Exec --- Run Action (Id:%s, Name:%s)" % (str(methodId), str(methodName)))
    
                    if AppInfo.REQUEST_KEY_LANGUAGE not in kwargs:
                        kwargs[AppInfo.REQUEST_KEY_LANGUAGE] = AppInfo.DEFAULT_API_LANGUAGE
    
                    AppConstants.get_thread_pool_executor().submit(self.__call_method_by_id, **kwargs)
        except Exception as e:
            Logger.log_debug("Rule Execution Ex:", e)

    def __update_rule_status(self, ruleId):
        try:
            ruleDTO = self.__ruleContainer.get_by_id(ruleId)
        except:
            return

        try:
            methodDTOs = ruleDTO.get_conditions() + ruleDTO.get_executions()
            isRequireFireEvent = False

            #=======================================================================
            # Only update if all methods are processed successfully
            #=======================================================================
            processedStatus = ruleDTO.get_status_processed()
            if processedStatus != RuleDTO.RULE_STATUS_PROCESSED_UPDATED:
                methodIds = [methodDTO.get_method_id() for methodDTO in methodDTOs]
                if self.__methodTracker.check_is_updated(methodIds):
                    ruleDTO.set_status_processed(RuleDTO.RULE_STATUS_PROCESSED_UPDATED)
                    isRequireFireEvent = True
                else:
                    return

            #=======================================================================
            # Update rule status code
            #=======================================================================
            ruleStatusCode = AppConstants.METHOD_ERROR_OK[0]
            for methodDTO in methodDTOs:
                try:
                    methodId = methodDTO.get_method_id()
                    realMethodDTO = self.__methodTracker.get_method(methodId)
                    ruleStatusCode = ruleStatusCode | realMethodDTO.get_status_code()
                except:
                    continue

            ruleDTO.set_status_code(ruleStatusCode)
            ruleDTO.set_status_message(AppConstants.RULE_CODE[ruleStatusCode])

            if isRequireFireEvent is True:
                self.__fire_rule_updated_event(ruleId)
                self.__enable_rule(ruleId, ruleDTO.get_enabled())

        except Exception as e:
            Logger.log_debug(e)

    def __fire_rule_updated_event(self, ruleId):
        if self.__fireEventFunc is not None:
            ruleDTO = self.__get_rule_summary(ruleId)
            summaryDict = self.__filter_rule_summary(ruleDTO)

            #===================================================================
            # Fire the event back to server
            #===================================================================
            eventTag = AppConstants.EVENT_RULE_UPDATED
            eventData = json.dumps(summaryDict)

            self.__fireEventFunc(eventTag, eventData)
            Logger.log_debug("Rule Updated Event:", eventTag, "---", eventData)

    def __fire_rule_update_started_event(self, ruleId):
        if self.__fireEventFunc is not None:
            eventTag = AppConstants.EVENT_RULE_UPDATE_STARTED
            eventData = json.dumps({RuleDTO.PROP_RULE_ID:ruleId})

            self.__fireEventFunc(eventTag, eventData)
            Logger.log_debug("Rule Start Update:", eventTag, "---", eventData)

    def __call_method_by_id(self, **kwargs):
        methodId = kwargs["kbxMethodId"]
        try:
            result = SharedMethod.call_by_method_id(**kwargs)
            Logger.log_debug("Rule Exec --- Action Run Completed (Id:%s) --- Results (%s)" % (str(methodId), str(result)))
        except Exception as e:
            Logger.log_debug("Rule Exec --- Action Run Error (Id:%s) --- Error (%s)" % (str(methodId), str(e)))

    #===========================================================================
    # Callbacks
    #===========================================================================
    def timer_callback(self, ruleId=None, **kwargs):
        del(kwargs)
        if self.__ruleContainer.has_id(ruleId):
            self.trigger_rule(ruleId, True)

    def __method_tracker_update_notify(self, methodId, *ruleIds):
        #=======================================================================
        # Update event listener because a method is updated
        #=======================================================================
        for ruleId in ruleIds:
            try:
                ruleDTO = self.__ruleContainer.get_by_id(ruleId)
            except:
                continue

            self.__update_rule_status(ruleId)

            #=======================================================================
            # Enable rule if necessary
            #=======================================================================
            condDTOs = ruleDTO.get_conditions()
            methodIds = [condDTO.get_method_id() for condDTO in condDTOs]

            if ruleDTO.get_enabled() is True:
                if methodId in methodIds:
                    try:
                        self.__enable_rule(ruleId, True)
                    except Exception as e:
                        Logger.log_debug("Unable to re-enable rule on method changed:", e)


    def __event_tracker_event_callback(self, ruleId, eventTag, eventData):
        if self.__ruleContainer.has_id(ruleId):
            self.trigger_rule(ruleId, True, eventTag, eventData)
