##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
# Xuan Automation Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Automation Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from collections import deque
from concurrent.futures.thread import ThreadPoolExecutor
import copy
import json
import threading
import time

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.eventController import EventController
from automationApp.core.groupController import GroupController
from automationApp.core.methodController import MethodController
from automationApp.core.ruleController import RuleController
from automationApp.core.triggerController import TriggerController
from automationApp.module.timerModule import TimerModule
from automationApp.utils.automationJSONEncoder import AutomationJSONEncoder
from automationApp.utils.methodCallGroup import MethodCallGroup
from automationApp.utils.sharedMethodWrapper import SharedMethodWrapper
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator


class RuleExecResult(threading.Event):
    '''
    Rule methods execution result tracker.
    '''


    def __init__(self, totalResultRequested):
        super().__init__()
        self.__result = None
        self.__totalResultRequested = totalResultRequested
        self.__totalResultResponsed = 0
        self.__lock = threading.Lock()
    
    def set_result(self, result):
        with self.__lock:
            if self.__result is None:
                self.__result = not isinstance(result, Exception)
            else:
                self.__result = self.__result and not isinstance(result, Exception)
                
            self.__totalResultResponsed += 1
            if self.__totalResultResponsed == self.__totalResultRequested:
                self.set()
    
    def get_result(self):
        return self.__result is True


class RuleExecInfo:
    '''
    Keep tracks the total count of a rule being requested to trigger.
    '''

    
    def __init__(self):
        self.__lock = threading.Lock()
        self.__triggerCount = 0
                
    def get_rlock(self):
        return self.__lock
    
    def get_trigger_count(self):
        return self.__triggerCount
    
    def increase_trigger_count(self):
        self.__triggerCount = (self.__triggerCount + 1) % 100000


class RuleService:


    def __init__(self):
        # Rule processors.
        self.__ruleController = RuleController()
        self.__methodController = MethodController()
        self.__triggerController = TriggerController.instance()
        
        self.__ruleUpdateThreadPool = ThreadPoolExecutor(max_workers=1)
        self.__ruleExecThreadPool = ThreadPoolExecutor(max_workers=AppConstants.MAX_RULE_EXEC_THREAD_SIZE)
        
        # Rule run workers.
        self.__ruleExecInfos = {}
        self.__condCallGroup = MethodCallGroup()
        self.__execCallGroup = MethodCallGroup()
        
        # Listeners.
        self.__ruleController.listen_to_rule_status_change(self.__on_rule_status_changed)
        GroupController.instance().listen_to_group_icon_change(self.__on_group_icon_changed)
        self.__methodController.listen_to_method_status_change(self.__on_method_status_changed)
        EventController.instance().listen_to_event_callback(self.__on_method_event_callback)
        self.__triggerController.listen_to_trigger_callback(self.__on_trigger_callback)
        
    def __on_rule_status_changed(self, ruleId, oldEnabled, newEnabled, oldStatusProcessed, newStatusProcessed):
        '''
        Trigger Source: RuleController --> This
        Callback when a rule is re-enabled OR statusProcessed changed to "updated".
        '''
        if newEnabled == True and newStatusProcessed == AppConstants.RULE_STATUS_UPDATED:
            if oldEnabled != newEnabled or oldStatusProcessed != newStatusProcessed:
                self.__ruleExecThreadPool.submit(self.__trigger_rule_implementation, ruleId=ruleId, checkCondition=True)
        
    def __on_group_icon_changed(self, kbxGroupId):
        '''
        Trigger Source: GroupController --> This
        Callback when kbxGroupIcon changed.
        '''
        ruleIdsFromCond = self.__ruleController.list_rule_ids_which_has_kbx_group_id_as_condition(kbxGroupId)
        ruleIdsFromExec = self.__ruleController.list_rule_ids_which_has_kbx_group_id_as_execution(kbxGroupId)
            
        # Broadcast rules updated messages.
        for ruleId in set(ruleIdsFromCond + ruleIdsFromExec):
            self.__broadcast_message__rule_updated(ruleId)

    def __on_method_status_changed(self, kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus):
        '''
        Trigger Source: MethodController --> This
        Callback when kbxMethodStatus changed.
        '''
        if oldKBXMethodStatus != newKBXMethodStatus:
            ruleIdsFromCond = self.__ruleController.list_rule_ids_which_has_kbx_method_id_as_condition(kbxMethodId)
            ruleIdsFromExec = self.__ruleController.list_rule_ids_which_has_kbx_method_id_as_execution(kbxMethodId)
                
            # Executes rules with conditions affected.
            if newKBXMethodStatus == SharedMethod.METHOD_STATUS_ACTIVE:
                for ruleId in ruleIdsFromCond:
                    self.__ruleExecThreadPool.submit(self.__trigger_rule_implementation, ruleId=ruleId, checkCondition=True)
            
            # Broadcast rules updated messages.
            for ruleId in set(ruleIdsFromCond + ruleIdsFromExec):
                self.__broadcast_message__rule_updated(ruleId)
                
    def __on_method_event_callback(self, kbxMethodId, eventTag, eventData):
        '''
        Trigger Source: EventController --> MethodController --> This
        Callback when a method with event broadcasted event.
        '''
        ruleIds = self.__ruleController.list_rule_ids_which_has_kbx_method_id_as_condition(kbxMethodId)
        for ruleId in ruleIds:
            self.__ruleExecThreadPool.submit(self.__trigger_rule_implementation, ruleId=ruleId, 
                                             checkCondition=True, eventTag=eventTag, 
                                             eventData=eventData, eventMethodId=kbxMethodId)
        
    def __on_trigger_callback(self, ruleId):
        '''
        Trigger Source: TriggerController --> This
        Callback when a rule is triggered.
        '''
        self.__ruleExecThreadPool.submit(self.__trigger_rule_implementation, ruleId=ruleId, checkCondition=True)
        
    def set_rule(self, trigger, condition, execution, ruleId=None, ruleName=None, ruleProtected=False, enabled=True):
        '''
        Create/Edit(with ruleId provided) an existing rule.
        
        trigger:Dictionary
        condition:List
        execution:List
        ruleId:Integer <Optional>
        ruleName:String <Optional>
        ruleProtected:Boolean <Optional>
        enabled:Boolean
        
        Returns "ruleId"
        '''
        def process_method_list(methodList):
            #===================================================================
            # Basic type validation
            #===================================================================
            if not isinstance(methodList, list):
                Logger.log_error("RuleService.set_rule: 'condition' and 'execution' must be type of list.")
                Logger.log_debug("type:", type(methodList), "value:", methodList)
                raise AutomationException(11704, "List is required for both 'condition' and 'execution'")

            #===================================================================
            # Check allowed size, raise error if exceeded.
            #===================================================================
            methodListLen = len(methodList)
            if methodListLen > AppConstants.MAX_METHOD_SIZE:
                Logger.log_error("RuleService.set_rule: 'condition' and 'execution' cannot have more than", AppConstants.MAX_METHOD_SIZE, "items respectively.")
                raise AutomationException(11705, "Only a maximum of " + \
                                          str(AppConstants.MAX_METHOD_SIZE) + \
                                          " items is allowed for each 'condition' and 'execution' - given size " + \
                                          str(methodListLen),
                                          lambda text: str(AppConstants.MAX_METHOD_SIZE).join(text.split(":max_item_size:")))

            #===================================================================
            # Check if all kbxMethodIds are valid and all kbxMethodParams are list
            #===================================================================
            idValidator = NumberValidator(isRequired=True, decimalPoint=False)
            if not all([idValidator.is_valid(eachMethod["kbxMethodId"])
                        and isinstance(eachMethod["kbxMethodParams"], list)
                        for eachMethod in methodList]):
                raise AutomationException(11704, "'condition' and 'execution' have incorrect data structure.")

            #===================================================================
            # Check if all kbxParamName and kbxParamCurrentValue exists
            #===================================================================
            paramNameValidator = StringValidator(isRequired=True)
            for eachMethod in methodList:
                methodArgs = eachMethod["kbxMethodParams"]
                for methodArg in methodArgs:
                    if not paramNameValidator.is_valid(methodArg[AppConstants.ARG_NAME]):
                        raise AutomationException(11704, "'condition' and 'execution' have invalid params structure")

                    if not AppConstants.ARG_CURRENT_VALUE in methodArg:
                        methodArg[AppConstants.ARG_CURRENT_VALUE] = None
            
            return methodList

        #=======================================================================
        # Data structure validations
        #=======================================================================
        ruleId = NumberValidator(isRequired=False, decimalPoint=False).get_value(ruleId)
        triggerDTO = self.__triggerController.parse_to_trigger_dto(trigger)
        condition = process_method_list(condition)
        execution = process_method_list(execution)
        
        #=======================================================================
        # Add to database
        #=======================================================================
        if Util.is_empty(ruleId):
            # Validate_max_rule_size
            if self.__ruleController.count() >= AppConstants.MAX_RULE_SIZE:
                raise AutomationException(11706, 
                                          "Total amount of rules cannot be more than " + str(AppConstants.MAX_RULE_SIZE),
                                          lambda text: str(AppConstants.MAX_RULE_SIZE).join(text.split(":max_rule_size:")))
            ruleId = self.__ruleController.generate_id(ruleName)
            rule = {}
        elif self.__ruleController.has(ruleId):
            ruleFromDB = self.__ruleController.get(ruleId)
            rule = dict(ruleFromDB)
            self.__check_rule_process_status(ruleId)
            self.__ruleController.change_to_updating(ruleId, ruleName)
        else:
            raise AutomationException(11704, "Rule ID provided not found - " + str(ruleId))

        #=======================================================================
        # Broadcast message: starts to update rule.
        #=======================================================================
        self.__broadcast_message__rule_update_started(ruleId, ruleName)

        #=======================================================================
        # Set basic information of the rule
        #=======================================================================
        rule["ruleId"] = ruleId
        rule["ruleName"] = ruleName
        rule["ruleProtected"] = ruleProtected
        rule["trigger"] = triggerDTO
        rule["enabled"] = enabled
        
        rule["condition"] = condition
        rule["execution"] = execution

        #=======================================================================
        # Update rule
        #=======================================================================
        def __update_rule(rule):
            try:
                # Fire rule update start event
                ruleId = rule["ruleId"]
                
                # Add methods to subscribe list
                methodIds = [kbxMethod["kbxMethodId"] for kbxMethod in rule["condition"] + rule["execution"]]
                self.__methodController.add(methodIds)
                
                # Update "rule" base table
                self.__ruleController.update(rule)
                self.__ruleController.commit()
            
            except Exception as e:
                self.__ruleController.rollback()
                self.__broadcast_message__rule_update_failed(ruleId, ruleName)
                Logger.log_error("RuleService __update_rule failed:", e, "-- rolledback")
            else:
                # Process for Timer Module
                TimerModule.delete_scheduler(ruleId)
                
                timerModuleHandlers = {TimerModule.METHOD_ID_DATE_TIME_RANGE:TimerModule.handle_date_time_range,
                                       TimerModule.METHOD_ID_DAY_OF_WEEK:TimerModule.handle_dow,
                                       TimerModule.METHOD_ID_TIME_RANGE:TimerModule.handle_time_range}
                
                for kbxMethod in rule["condition"]:
                    kbxMethodId = kbxMethod["kbxMethodId"]
                    timerModuleHandler = timerModuleHandlers.get(kbxMethodId, None)
                    if timerModuleHandler is not None:
                        timerModuleHandler(ruleId, kbxMethod["kbxMethodParams"])
                    
                # Broadcast message: completed updating a rule
                self.__broadcast_message__rule_updated(ruleId)

        #=======================================================================
        # Submit to a thread to process other info, and return... performance...
        #=======================================================================
        self.__ruleUpdateThreadPool.submit(__update_rule, rule)

    def delete_rule(self, ruleId):
        self.__check_rule_process_status(ruleId)
        try:
            self.__ruleController.delete(ruleId)
            self.__ruleController.commit()
        except Exception as e:
            self.__ruleController.rollback()
            Logger.log_error("RuleService delete_rule ex:", e, "-- rolled back")
        else:
            self.__broadcast_message__rule_deleted(ruleId)
            self.__triggerController.unregister_listener(ruleId)
            TimerModule.delete_scheduler(ruleId)

    def trigger_rule(self, ruleId, checkCondition=False):
        '''
        self.__check_rule_process_status(ruleId) <-- Check again in self.__trigger_rule_implementation.
        '''
        self.__trigger_rule_implementation(ruleId=ruleId, checkCondition=checkCondition)
    
    def enable_rule(self, ruleId, enabled):
        self.__check_rule_process_status(ruleId)
        try:
            self.__ruleController.enable(ruleId, enabled)
            self.__ruleController.commit()
        except Exception as e:
            self.__ruleController.rollback()
            Logger.log_error("RuleService enable_rule ex:", e, "-- rolled back")
        else:
            self.__broadcast_message__rule_updated(ruleId)

    def get_rule(self, ruleId, language=AppInfo.DEFAULT_API_LANGUAGE):
        try:
            rule = self.__ruleController.get_detail(ruleId)
        except:
            raise AutomationException(11702, "Rule ID provided not found - " + str(ruleId))
        
        kbxMethods = list(rule["condition"]) + list(rule["execution"])
        
        # -------------- Compile lists of kbxMethod and group IDs contains in this rule.
        kbxMethodIdsToList = {}
        kbxGroupIdsToList = set([])
        
        for kbxMethod in kbxMethods:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
            kbxMethodAppId = kbxMethod["kbxMethodAppId"]
            kbxMethodStatus = kbxMethod["kbxMethodStatus"]
            kbxGroupId = kbxMethod["kbxGroupId"]
            kbxGroupStatus = kbxMethod["kbxGroupStatus"]
            
            if kbxMethodStatus is not -1 and kbxMethodAppId is not None:
                kbxMethodIdsToList.setdefault(kbxMethodAppId, set([]))
                kbxMethodIdsToList[kbxMethodAppId].add(kbxMethodId)
            if kbxGroupId is not None and kbxGroupStatus is not -1:
                kbxGroupIdsToList.add(kbxGroupId)
                
        # -------------- Get methods and groups based on requested language.
        kbxMethodIdsListed = {}
        kbxGroupIdsListed = {}
                
        for kbxMethodAppId, kbxMethodIds in kbxMethodIdsToList.items():
            kbxMethodIdsListed[kbxMethodAppId] = SharedMethodWrapper.list_shared_methods_by_app_id(kbxMethodAppId, 
                                                                                                   list(kbxMethodIds), 
                                                                                                   language=language)
            
        groupList = SharedMethodWrapper.list_shared_method_groups(kbxGroupId=kbxGroupIdsToList, language=language)
        for row in groupList:
            kbxGroupIdsListed[row["kbxGroupId"]] = row
        
        # -------------- Set method and group data into rule.
        for kbxMethod in kbxMethods:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
            kbxMethodAppId = kbxMethod["kbxMethodAppId"]
            kbxMethodStatus = kbxMethod["kbxMethodStatus"]
            kbxGroupId = kbxMethod["kbxGroupId"]
            kbxGroupStatus = kbxMethod["kbxGroupStatus"]
            
            if kbxMethodStatus is not -1 and kbxMethodAppId is not None:
                kbxMethodParamsWithCurrentValue = {kbxMethodParam["kbxParamName"]:kbxMethodParam["kbxParamCurrentValue"] \
                                                   for kbxMethodParam in kbxMethod["kbxMethodParams"]}
                kbxMethodWithDetails = kbxMethodIdsListed[kbxMethodAppId][kbxMethodId]
                if kbxMethodWithDetails is not None:
                    kbxMethodParamsWithDetails = kbxMethodWithDetails["kbxMethodParams"]
                    kbxMethodParamsWithDetails = copy.deepcopy(kbxMethodParamsWithDetails)
                    
                    for kbxMethodParam in kbxMethodParamsWithDetails:
                        kbxMethodParam["kbxParamCurrentValue"] = kbxMethodParamsWithCurrentValue.get(kbxMethodParam["kbxParamName"], None)
                    
                    kbxMethod["kbxMethodParams"] = kbxMethodParamsWithDetails
                    kbxMethod["kbxMethodHasEvent"] = not Util.is_empty(kbxMethodWithDetails.get("kbxMethodEvent", None)) \
                                                        and not Util.is_empty(kbxMethodWithDetails.get("kbxMethodIdentifier", None))
                    kbxMethod["kbxMethodLabel"] = kbxMethodWithDetails.get("kbxMethodLabel")
                    kbxMethod["kbxMethodDesc"] = kbxMethodWithDetails.get("kbxMethodDesc")
                
                else:
                    kbxMethod["atDebugMethod"] = "Unable to get shared method, caused by a method which never register itself on this bootup."
                    
            else:
                kbxMethod["kbxMethodHasEvent"] = False
                
            if kbxGroupId is not None and kbxGroupStatus is not -1:
                try:
                    kbxMethod["kbxGroupLabel"] = kbxGroupIdsListed[kbxGroupId]["kbxGroupLabel"]
                    kbxMethod["kbxGroupDesc"] = kbxGroupIdsListed[kbxGroupId]["kbxGroupDesc"]
                except:
                    kbxMethod["atDebugGroup"] = "Unable to get shared method group, caused by a group which never register itself on this bootup."
                    
        return rule

    def list_rules(self, offset=0, limit=20):
        return self.__ruleController.list(offset, limit), \
                self.__ruleController.count()
                
    def run_all_enabled_rules(self):
        ruleIds = self.__ruleController.list_rule_ids_which_are_enabled()
        for ruleId in ruleIds:
            self.__ruleExecThreadPool.submit(self.__trigger_rule_implementation, ruleId=ruleId, checkCondition=True)
                
    def __check_rule_process_status(self, ruleId):
        try:
            statusProcessed = self.__ruleController.get_status_processed(ruleId)
            if statusProcessed != AppConstants.RULE_STATUS_UPDATED:
                raise AutomationException(11703, "edit/delete/execute is not allowed on rule update in progress")
        except:
            raise AutomationException(11702, "Rule ID provided not found - " + str(ruleId))
        
    def __broadcast_message__rule_update_started(self, ruleId, ruleName=None):
        eventTag = AppConstants.EVENT_RULE_UPDATE_STARTED
        eventData = {"ruleId":ruleId, "newRuleName":ruleName}
        
        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Rule Start Update:", ruleName)

    def __broadcast_message__rule_updated(self, ruleId):
        try:
            rule = self.__ruleController.get_summary(ruleId)
        except Exception as e:
            Logger.log_error("RuleService.__broadcast_message__rule_updated get_summary ex:", e)
            return

        eventTag = AppConstants.EVENT_RULE_UPDATED
        eventData = rule
        
        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Rule Updated:", rule["ruleName"])
        
    def __broadcast_message__rule_update_failed(self, ruleId, ruleName=None):
        '''
        ruleName - For debugging purpose.
        '''
        try:
            rule = self.__ruleController.get_summary(ruleId)
        except Exception:
            rule = None
        
        eventTag = AppConstants.EVENT_RULE_UPDATE_FAILED
        eventData = {"ruleId": ruleId, "oldRuleSummary":rule}

        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Rule Update Failed:", ruleName)
        
    def __broadcast_message__rule_deleted(self, ruleId):
        eventTag = AppConstants.EVENT_RULE_DELETED
        eventData = {"ruleId": ruleId}

        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Rule Deleted: Id -", ruleId)
            
    def __broadcast_message(self, eventTag, eventData):
        eventData = json.dumps(eventData, cls=AutomationJSONEncoder)
        Application.send_web_server_event(eventTag, eventData)
        
    def __trigger_rule_implementation(self, ruleId, checkCondition=False, eventTag=None, eventData=None, eventMethodId=None):
        '''
        Triggers a rule by given ruleId.
        '''
        # Check if rule is "updated" AND enabled.
        statusProcessed, enabled = self.__ruleController.get_status_processed_and_enabled(ruleId)
        if statusProcessed != AppConstants.RULE_STATUS_UPDATED or enabled != True:
            return
        
        self.__ruleExecInfos.setdefault(ruleId, RuleExecInfo())
        
        ruleExecInfo = self.__ruleExecInfos.get(ruleId)
        ruleExecInfo.increase_trigger_count()
        triggerCountInThisSession = ruleExecInfo.get_trigger_count()
        
        with ruleExecInfo.get_rlock():
            #=======================================================================
            # Check conditions
            #=======================================================================
            if checkCondition is True:
                # Check if we should proceed (stop if there is another pending request on the same ruleId).
                if triggerCountInThisSession != ruleExecInfo.get_trigger_count():
                    return
                
                methodListToCheck = deque()
                result = self.__ruleController.list_conditions(ruleId)
                methodCheckingTime = int(time.time())
                for row in result:
                    if row["kbxMethodStatus"] not in (SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE):
                        return
                    else:
                        methodArgs = row["kbxMethodParams"]
    
                        kwargs = {methodArg[AppConstants.ARG_NAME]:methodArg[AppConstants.ARG_CURRENT_VALUE] for methodArg in methodArgs}
                        
                        if eventTag is not None and eventMethodId == row["kbxMethodId"]:
                            kwargs[AppConstants.KEY_CONDITION_EVENT_TAG] = eventTag
                            kwargs[AppConstants.KEY_CONDITION_EVENT_DATA] = eventData
                            
                        if AppInfo.REQUEST_KEY_LANGUAGE not in kwargs:
                            kwargs[AppInfo.REQUEST_KEY_LANGUAGE] = AppInfo.DEFAULT_API_LANGUAGE
                            
                        kwargs["kbxMethodName"] = row["kbxMethodName"]
                        kwargs["kbxModuleName"] = row["kbxModuleName"]
                        kwargs["kbxGroupId"] = row["kbxGroupId"]
                        kwargs["kbxMethodAppId"] = row["kbxMethodAppId"]
                        callId = hash(str(kwargs)) # Generate condition checking ID
                        kwargs[AppConstants.KEY_CONDITION_TIMESTAMP] = methodCheckingTime # So that timestamp will not caused the generated id to be different
                        methodListToCheck.append({"callId":callId,
                                                  "callFn":SharedMethod.call,
                                                  "callKwargs":kwargs})
                    
                #===============================================================
                # Submit all conditions for checking
                #===============================================================
                methodListToCheckLen = len(methodListToCheck)
                if methodListToCheckLen > 0:
                    ruleExecResult = RuleExecResult(methodListToCheckLen)
                    
                    for methodItem in methodListToCheck:
                        self.__condCallGroup.submit(callbackFn=self.__on_method_call_complete, ruleExecResult=ruleExecResult, **methodItem)
                    
                    result = ruleExecResult.wait(40.0)
                    
                    if result is False or ruleExecResult.get_result() is False:
                        return # Failed at condition checking.
            
                # Clear cache
                del(methodListToCheck)
                del(methodCheckingTime)
                del(methodListToCheckLen)
                
                # Check if we should proceed (stop if there is another pending request on the same ruleId).
                if triggerCountInThisSession != ruleExecInfo.get_trigger_count():
                    return

            #=======================================================================
            # Execute executions
            #=======================================================================
            methodListToExec = deque()
            result = self.__ruleController.list_executions(ruleId)
            methodExecTime = int(time.time())
            for row in result:
                if row["kbxMethodStatus"] not in (SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE):
                    continue
                else:
                    methodArgs = row["kbxMethodParams"]
                    kwargs = {methodArg[AppConstants.ARG_NAME]:methodArg[AppConstants.ARG_CURRENT_VALUE] for methodArg in methodArgs}
                    if AppInfo.REQUEST_KEY_LANGUAGE not in kwargs:
                        kwargs[AppInfo.REQUEST_KEY_LANGUAGE] = AppInfo.DEFAULT_API_LANGUAGE
                    
                    kwargs["kbxMethodName"] = row["kbxMethodName"]
                    kwargs["kbxModuleName"] = row["kbxModuleName"]
                    kwargs["kbxGroupId"] = row["kbxGroupId"]
                    kwargs["kbxMethodAppId"] = row["kbxMethodAppId"]
                    
                    callId = hash(str(kwargs)) # Generate execution id
                    kwargs[AppConstants.KEY_ACTION_TIMESTAMP] = methodExecTime
                    methodListToExec.append({"callId":callId,
                                             "callFn":SharedMethod.call,
                                             "callKwargs":kwargs})

            #===============================================================
            # Submit all methods for executions
            #===============================================================
            methodListToExecLen = len(methodListToExec)
            if methodListToExecLen > 0:
                ruleExecResult = RuleExecResult(methodListToExecLen)
                
                for methodItem in methodListToExec:
                    self.__execCallGroup.submit(callbackFn=self.__on_method_call_complete, ruleExecResult=ruleExecResult, **methodItem)
                
                result = ruleExecResult.wait(30.0)
                
                return
            
    def __on_method_call_complete(self, checkingId, result, ruleExecResult):
        '''
        When rule/execution checking is completed.
        '''
        ruleExecResult.set_result(result)

