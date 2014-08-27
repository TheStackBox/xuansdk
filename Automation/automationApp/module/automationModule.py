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
from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.service.apiService import APIService
from automationApp.service.ruleService import RuleService
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class AutomationModule(object):

    def __init__(self):
        self.__apiService = None
        self.__ruleService = None

    def start(self):
        self.__apiService = APIService()
        self.__ruleService = RuleService(fireEventFunc=Application.send_web_server_event)

    def list_groups(self, request):
        '''
        List all groups, parentId is optional.
        '''
        try:
            #===================================================================
            # Validation
            #===================================================================
            parentId = request.get_value("parentId")
            section = request.get_value("section")
            section = self.__parse_section(section)

            limit = request.get_value("limit")
            limit = 50 if limit is None else limit

            offset = request.get_value("offset")
            offset = 0 if offset is None else offset

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            parentGroup, groupList, totalCount = self.__apiService.list_groups(section=section, parentId=parentId, limit=limit, offset=offset, language=language)

            self.__send_response(request.requestId, {"parentGroup":parentGroup, "data": groupList, "totalCount": totalCount})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def list_methods(self, request):
        '''
        List all methods by groupId(required), section(required) accepts "if/then".
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            groupId = request.get_value("groupId")
            section = request.get_value("section")
            section = self.__parse_section(section)

            limit = request.get_value("limit")
            limit = 50 if limit is None else limit

            offset = request.get_value("offset")
            offset = 0 if offset is None else offset

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            methodList, totalCount, groupDict = self.__apiService.list_methods(section=section, groupId=groupId, limit=limit, offset=offset, language=language)

            self.__send_response(request.requestId, {"group": groupDict, "data": methodList, "totalCount": totalCount})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def set_rule(self, request):
        '''
        Set rule is the combination of both "update/insert rule".
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            trigger = request.get_value("trigger")
            condition = request.get_value("condition")
            execution = request.get_value("execution")
            ruleId = request.get_value("ruleId")
            ruleName = request.get_value("ruleName")

            enabled = request.get_value("enabled")
            enabled = not (enabled is False) # always True unless False is specified

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            self.__ruleService.set_rule(trigger=trigger, condition=condition, execution=execution, ruleId=ruleId, ruleName=ruleName, enabled=enabled)

            self.__send_response(request.requestId, {"status":"ok"})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def list_rules(self, request):
        '''
        List all rules summary.
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            limit = request.get_value("limit")
            limit = AppConstants.UPPER_LIMIT if limit is None else limit

            offset = request.get_value("offset")
            offset = 0 if offset is None else offset

            #===================================================================
            # Executions
            #===================================================================
            result, total = self.__ruleService.list_rules(limit=limit, offset=offset)

            self.__send_response(request.requestId, {"totalCount": total, "data": result})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def get_rule(self, request):
        '''
        Get single rule detail by rule id.
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            ruleId = request.get_value("ruleId")

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            result = self.__ruleService.get_rule(ruleId=ruleId)

            self.__send_response(request.requestId, result)
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def delete_rule(self, request):
        '''
        Completely remove a rule by rule id.
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            ruleId = request.get_value("ruleId")

            #===================================================================
            # Executions
            #===================================================================
            self.__ruleService.delete_rule(ruleId=ruleId)

            self.__send_response(request.requestId, {"status":"ok"})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def trigger_rule(self, request):
        '''
        Trigger a rule manually
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            ruleId = request.get_value("ruleId")

            checkCondition = request.get_value("checkCondition")
            checkCondition = not (checkCondition is False)

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            self.__ruleService.trigger_rule(ruleId=ruleId, checkCondition=checkCondition)

            self.__send_response(request.requestId, {"status":"ok"})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_error_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def enable_rule(self, request):
        '''
        Enable/Disable a rule.
        '''
        try:
            #===================================================================
            # Validations
            #===================================================================
            ruleId = request.get_value("ruleId")

            enabled = request.get_value("enabled")

            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

            #===================================================================
            # Executions
            #===================================================================
            self.__ruleService.enable_rule(ruleId=ruleId, enabled=enabled)

            self.__send_response(request.requestId, {"status":"ok"})
        except AutomationException as e:
            self.__send_response(request.requestId, {}, e.get_error_code(), e.get_debug_message())
        except Exception as e:
            self.__send_response(request.requestId, {}, 1098, str(e))

    def __parse_section(self, section):
        section = str(section).lower()

        mapDict = {AppConstants.SECTION_CONDITION:AppConstants.TAG_CONDITION,
                   AppConstants.SECTION_EXECUTION:AppConstants.TAG_ACTION}

        try:
            return mapDict[section]
        except:
            Logger.log_debug("__parse_section ex: given value(%s), type(%s), allowed values(%s)" % (str(section), str(type(section)), str(mapDict.keys())))
            raise AutomationException(1097, "section param must be either value from " + str(mapDict.keys())) # invalid parameter

    def __send_response(self, requestId, data, returnValue=100, debugMessage=""):
        if returnValue != 100:
            Logger.log_debug("Automation Debug:", debugMessage)
            ae = AutomationException(returnValue, debugMessage)
            Application.send_response(data, requestId, returnValue=ae.get_error_code(), returnMessage=ae.get_error_message())
        else:
            Application.send_response(data, requestId)

    #===========================================================================
    # Callbacks
    #===========================================================================
    def timer_callback(self, request):
        '''
        A redirector for RuleService timer_callback.
        '''
        self.__send_response(request.requestId, {"status":"ok"})

        kwargs = request.get_all_args()
        if not isinstance(kwargs, dict):
            kwargs = {}

        try:
            self.__ruleService.timer_callback(**kwargs)
        except Exception as e:
            Logger.log_debug("Timer_callback exception: ", e)
