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

import json
import traceback

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.methodController import MethodController
from automationApp.service.apiService import APIService
from automationApp.service.bootstrapService import BootstrapService
from automationApp.service.ruleService import RuleService
from automationApp.service.sceneExecutionResultService import SceneExecutionResultService
from automationApp.service.sceneService import SceneService
from automationApp.utils.helper import Helper
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class AutomationModuleWrapper:
    '''
    Implementations of web entries (register_method) in automationApp.py.
    '''
    

    def __init__(self):
        self.__apiService = None
        self.__ruleService = None
        self.__sceneService = None
        self.__serService = None

    def start(self):
        '''
        Initialize all services required by automation app.
        '''
        MethodController.instance() # Must listen to groups and methods added event before bootstrap.
        
        # Bootstrap
        try:
            bs = BootstrapService()
            Logger.log_info("Bootstrap update kbx method ...")
            bs.update_kbx_method()
            Logger.log_info("Bootstrap update kbx group ...")
            bs.update_kbx_group()
            Logger.log_info("Bootstrap register trigger schedulers ...")
            bs.register_trigger_schedulers()
            Logger.log_info("Bootstrap register timer module schedulers ...")
            bs.register_timer_module_schedulers()
        except Exception as e:
            bs.rollback()
            Logger.log_error("AutomationModuleWrapper.start bootstrap ex:", e)
            traceback.print_exc()
            raise e
        else:
            bs.commit()
            Logger.log_info("Bootstrap process completed!")
        
        self.__apiService = APIService()
        self.__ruleService = RuleService()
        self.__sceneService = SceneService()
        self.__serService = SceneExecutionResultService.instance()
        
        Logger.log_info("Attempts to execute all enabled rules ...")
        self.__ruleService.run_all_enabled_rules()

    def list_groups(self, request):
        '''
        List all groups, parentId is optional.
        '''
        # Parameters
        try:
            paramKey = "parentId"
            parentId = request.get_value(paramKey)
            
            paramKey = "section"
            section = request.get_value(paramKey)
            section = self.__parse_section(section)

            paramKey = "language"
            language = request.get_arg(paramKey)
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            parentGroup, groupList = self.__apiService.list_groups(section=section, parentId=parentId, language=language)

            self.send_response(request.requestId, data={"parentGroup":parentGroup, "data": groupList})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def list_methods(self, request):
        '''
        List all methods by groupId(required), section(required) accepts "if/then".
        '''
        # Parameters
        try:
            paramKey = "groupId"
            groupId = request.get_value(paramKey)
            
            paramKey = "section"
            section = request.get_value(paramKey)
            section = self.__parse_section(section)
            
            paramKey = "language"
            language = request.get_arg(paramKey)
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language

        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            methodList, groupDict = self.__apiService.list_methods(section=section, groupId=groupId, language=language)

            self.send_response(request.requestId, data={"group":groupDict, "data":methodList})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def update_kbx_method(self, request):
        '''
        Update shared method in use manually.
        '''
        # Parameters
        try:
            paramKey = "kbxMethodId"
            kbxMethodId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__apiService.update_kbx_method(kbxMethodId)
            
            if result is None:
                methodStatus = "Method Removed"
            elif result is True:
                methodStatus = "Method Active"
            else:
                methodStatus = "Method Inactive"
            
            self.send_response(request.requestId, data={"methodStatus":methodStatus})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def update_kbx_group(self, request):
        '''
        Update shared method group in use manually.
        '''
        # Parameters
        try:
            paramKey = "kbxGroupId"
            kbxGroupId = request.get_value(paramKey)

        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__apiService.update_kbx_group(kbxGroupId)
            if result is None:
                groupStatus = "Group Removed"
            else:
                groupStatus = "Group Exists"
            
            self.send_response(request.requestId, data={"groupStatus":groupStatus})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def list_kbx_methods(self, request):
        '''
        List kbx_methods, mostly for debugging purpose.
        '''
        # Parameters
        try:
            paramKey = "offset"
            offset = request.get_value(paramKey)
            if offset is None:
                offset = 0
                
            paramKey = "limit"
            limit = request.get_value(paramKey)
            if limit is None:
                limit = 200

        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__apiService.list_kbx_methods(offset, limit)
            kbxMethods = [dict(val) for val in result]
            self.send_response(request.requestId, data={"kbxMethods":kbxMethods})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def list_kbx_groups(self, request):
        '''
        List kbx_groups, mostly for debugging purpose.
        '''
        # Parameters
        try:
            paramKey = "offset"
            offset = request.get_value(paramKey)
            if offset is None:
                offset = 0
                
            paramKey = "limit"
            limit = request.get_value(paramKey)
            if limit is None:
                limit = 200

        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__apiService.list_kbx_groups(offset, limit)
            kbxGroups = [dict(val) for val in result]
            self.send_response(request.requestId, data={"kbxGroups":kbxGroups})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)


    def set_rule(self, request):
        '''
        Set rule is the combination of both "update/insert rule".
        '''
        # Parameters
        try:
            paramKey = "Process post data"
            params = Helper.parse_post_data(request.get_post_data())
            
            paramKey = "condition"
            condition = json.loads(params[paramKey])
            if len(condition) == 0:
                raise Exception("'condition' cannot be empty")
            
            paramKey = "execution"
            execution = json.loads(params[paramKey])
            if len(condition) == 0:
                raise Exception("'execution' cannot be empty")
            
            paramKey = "trigger"
            trigger = json.loads(params[paramKey])
            
            paramKey = "ruleId"
            ruleId = params.get(paramKey)
            ruleId = None if Util.is_empty(ruleId) else int(ruleId)
            
            paramKey = "ruleName"
            ruleName = params[paramKey]
            if Util.is_empty(ruleName):
                raise Exception("'ruleName' cannot be empty")
            ruleName = str(ruleName)
            
            paramKey = "enabled"
            boolValidator = KBXBoolean(kbxParamName="boolValidator", kbxParamIsRequired=False)
            enabled = boolValidator.cast(params.get(paramKey))
            enabled = enabled is not False # always True unless False is specified
            
            paramKey = "ruleProtected"
            ruleProtected = boolValidator.cast(params.get(paramKey))
            ruleProtected = ruleProtected is True # Always False unless True is specified.
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
            
        # Implementations
        try:
            self.__ruleService.set_rule(trigger=trigger, condition=condition, execution=execution, ruleId=ruleId, \
                                        ruleName=ruleName, ruleProtected=ruleProtected, enabled=enabled)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def list_rules(self, request):
        '''
        List all rules summary.
        '''
        # Parameters
        try:
            paramKey = "limit"
            limit = request.get_value(paramKey)
            limit = AppConstants.UPPER_LIMIT if limit is None else limit
            
            paramKey = "offset"
            offset = request.get_value(paramKey)
            offset = 0 if offset is None else offset
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return

        # Implementations
        try:
            result, total = self.__ruleService.list_rules(limit=limit, offset=offset)
            
            self.send_response(request.requestId, data={"totalCount": total, "data": result})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def get_rule(self, request):
        '''
        Get single rule detail by rule id.
        '''
        # Parameters
        try:
            paramKey = "ruleId"
            ruleId = request.get_value(paramKey)
            
            paramKey = "language"
            language = request.get_arg(paramKey)
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__ruleService.get_rule(ruleId=ruleId, language=language)
            
            self.send_response(request.requestId, data=result)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def delete_rule(self, request):
        '''
        Completely remove a rule by rule id.
        '''
        # Parameters
        try:
            paramKey = "ruleId"
            ruleId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__ruleService.delete_rule(ruleId=ruleId)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def trigger_rule(self, request):
        '''
        Trigger a rule manually
        '''
        # Parameters
        try:
            paramKey = "ruleId"
            ruleId = request.get_value(paramKey)
            
            paramKey = "checkCondition"
            checkCondition = request.get_value(paramKey)
            checkCondition = not (checkCondition is False)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__ruleService.trigger_rule(ruleId=ruleId, checkCondition=checkCondition)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def enable_rule(self, request):
        '''
        Enable/Disable a rule.
        '''
        # Parameters
        try:
            paramKey = "ruleId"
            ruleId = request.get_value(paramKey)
            
            paramKey = "enabled"
            enabled = request.get_value("enabled")
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__ruleService.enable_rule(ruleId=ruleId, enabled=enabled)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def set_scene(self, request):
        '''
        Set scene is the combination of both "update/insert scene".
        '''
        # Parameters
        try:
            paramKey = "Process post data"
            params = Helper.parse_post_data(request.get_post_data())

            paramKey = "execution"
            execution = json.loads(params[paramKey])
            if len(execution) == 0:
                raise Exception("'execution' cannot be empty")
            
            paramKey = "sceneId"
            sceneId = params.get(paramKey)
            sceneId = None if Util.is_empty(sceneId) else int(sceneId)
            
            paramKey = "sceneName"
            sceneName = params[paramKey]
            if Util.is_empty(sceneName):
                raise Exception("'sceneName' cannot be empty")
            sceneName = str(sceneName)
            
            paramKey = "sceneIcon"
            sceneIcon = params[paramKey]
            if Util.is_empty(sceneIcon):
                raise Exception("'sceneIcon' cannot be empty")
            sceneIcon = str(sceneIcon)
            
            paramKey = "sceneProtected"
            boolValidator = KBXBoolean(kbxParamName="boolValidator", kbxParamIsRequired=False)
            sceneProtected = boolValidator.cast(params.get(paramKey))
            sceneProtected = sceneProtected is True # Always False unless True is specified.
        
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            sceneId = self.__sceneService.set_scene(execution=execution, sceneId=sceneId, sceneName=sceneName, \
                                                    sceneProtected=sceneProtected, sceneIcon=sceneIcon)

            self.send_response(request.requestId, data={"sceneId":sceneId})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def delete_scene(self, request):
        '''
        Remove scene by sceneId.
        '''
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__sceneService.delete_scene(sceneId=sceneId)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def execute_scene(self, request):
        '''
        Execute a scene.
        '''
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
            paramKey = "serUrl"
            serUrl = request.get_value(paramKey)
            
            paramKey = "language"
            language = request.get_arg(paramKey)
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
            
        # Implementations
        try:
            self.__sceneService.execute_scene(sceneId=sceneId, serUrl=serUrl, language=language)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def stop_scene(self, request):
        '''
        Force stop execution of a scene.
        '''
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__sceneService.stop_scene(sceneId=sceneId)

            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def get_scene(self, request):
        '''
        Get single scene detail by scene id.
        '''
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
            paramKey = "language"
            language = request.get_arg("language")
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__sceneService.get_scene(sceneId=sceneId, language=language)

            self.send_response(request.requestId, data=result)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def list_scenes(self, request):
        '''
        List all scene summaries.
        '''
        # Parameters
        try:
            paramKey = "limit"
            limit = request.get_value(paramKey)
            limit = AppConstants.UPPER_LIMIT if limit is None else limit
            
            paramKey = "offset"
            offset = request.get_value(paramKey)
            offset = 0 if offset is None else offset
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result, total = self.__sceneService.list_scenes(limit=limit, offset=offset)

            self.send_response(request.requestId, data={"totalCount":total, "data":result})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def get_scene_execution_result(self, request):
        '''
        Get scene execution result (aggregates details base on preferred language).
        '''
        # Parameters
        try:
            paramKey = "serId"
            serId = request.get_value(paramKey)
            
            paramKey = "language"
            language = request.get_arg(paramKey)
            language = AppInfo.DEFAULT_API_LANGUAGE if language is None else language
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            serObject = self.__serService.get_scene_execution_result(serId, language)

            self.send_response(request.requestId, data=serObject)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def retry_scene_execution_result_item(self, request):
        '''
        Retry a specific or all items with error sequentially.
        '''
        # Parameters
        try:
            paramKey = "serId"
            serId = request.get_value(paramKey)
            
            paramKey = "seriIndex"
            seriIndex = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            seriIndexes = self.__serService.retry_scene_execution_result_item(serId, seriIndex)

            self.send_response(request.requestId, data={"serId":serId, "seriIndexes":seriIndexes})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def list_scene_execution_results(self, request):
        '''
        List all scene execution results without items. (For debugging)
        '''
        # Parameters
        try:
            paramKey = "limit"
            limit = request.get_value(paramKey)
            limit = 50 if limit is None else limit
            
            paramKey = "offset"
            offset = request.get_value(paramKey)
            offset = 0 if offset is None else offset
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result = self.__serService.list_scene_execution_results(offset, limit)

            self.send_response(request.requestId, {"data":result})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def delete_scene_execution_result(self, request):
        '''
        Delete scene execution result. (For debugging)
        '''
        # Parameters
        try:
            paramKey = "serId"
            serId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__serService.delete_scene_execution_result(serId)
            
            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
            
    def set_favorited_scene(self, request):
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
            paramKey = "prevSceneId"
            prevSceneId = request.get_value(paramKey)
            
            if sceneId == prevSceneId:
                raise Exception("sceneId cannot equals to prevSceneId")
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__sceneService.set_favorited_scene(sceneId, prevSceneId)
            
            self.send_response(request.requestId, data={"prevSceneId":prevSceneId})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
    
    def delete_favorited_scene(self, request):
        # Parameters
        try:
            paramKey = "sceneId"
            sceneId = request.get_value(paramKey)
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            self.__sceneService.delete_favorited_scene(sceneId)
            
            self.send_response(request.requestId)
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)
    
    def list_favorited_scenes(self, request):
        # Parameters
        try:
            paramKey = "limit"
            limit = request.get_value(paramKey)
            limit = 200 if limit is None else limit
            
            paramKey = "offset"
            offset = request.get_value(paramKey)
            offset = 0 if offset is None else offset
            
        except Exception as e:
            self.send_response(request.requestId, data=AutomationException(11097, " - ".join((paramKey, str(e)))))
            return
        
        # Implementations
        try:
            result, total = self.__sceneService.list_favorited_scene(offset, limit)

            self.send_response(request.requestId, {"data":result, "total":total})
            
        except Exception as e:
            if not isinstance(e, AutomationException):
                traceback.print_exc()
                e = AutomationException(11099, str(e))
            self.send_response(request.requestId, data=e)

    def send_response(self, requestId, data={}):
        '''
        Act as send_response for a real module. (This class do the works of module but it isn't module instance)
        '''
        if isinstance(data, AutomationException):
            Application.send_response({"status":"error", "debug":data.get_debug_message()},# IGNORE:maybe-no-member
                                      requestId, 
                                      returnValue=data.get_error_code(), # IGNORE:maybe-no-member
                                      returnMessage=data.get_error_message()) # IGNORE:maybe-no-member
        else:
            data["status"] = "ok"
            Application.send_response(data, requestId)
            
    def __parse_section(self, section):
        '''
        Convert if/then into correlated automation tags.
        '''
        section = str(section).lower()

        mapDict = {AppConstants.SECTION_CONDITION:AppConstants.TAG_CONDITION,
                   AppConstants.SECTION_EXECUTION:AppConstants.TAG_ACTION}
        
        try:
            return mapDict[section]
        
        except:
            Logger.log_error("__parse_section ex: given value(%s), type(%s), allowed values(%s)" % (str(section), str(type(section)), str(mapDict.keys())))
            raise AutomationException(11097, "section param must be either value from " + str(mapDict.keys())) # invalid parameter
