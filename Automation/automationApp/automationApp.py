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

import time
import traceback

from automationApp.appConstants import AppConstants
from automationApp.core.database import Database
from automationApp.module.automationModuleWrapper import AutomationModuleWrapper
from automationApp.module.controllerModule import ControllerModule
from automationApp.module.debugModule import DebugModule
from automationApp.module.deviceManager.deviceManagerModule import DeviceManagerModule
from automationApp.module.deviceManager.zwaveModule import ZWaveModule
from automationApp.module.locationManager.locationManagerModule import LocationManagerModule
from automationApp.module.timerModule import TimerModule
from automationApp.utils.automationJSONEncoder import AutomationJSONEncoder
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class AutomationApp(Application):


    def __init__(self):
#         Logger.set_enable_debug(True)
        self.__automationModule = None

    def on_start(self):
        AppInfo.JSON_ENCODER_CLS = AutomationJSONEncoder
        
        Database.instance().initialize()
        
        self.register_module(DebugModule("debug_module", None))
        
        self.register_module(ControllerModule("controller_module", None))
        self.register_module(TimerModule("timer_module", None))

        self.register_module(DeviceManagerModule("device_manager", None))
        self.register_module(ZWaveModule("zwave_module", None))
        
        self.register_module(LocationManagerModule("location_manager", None))
        
    def on_system_connected(self):
        super().on_system_connected()
        
        DebugModule.DEBUG_ON_SYSTEM_CONNECTED.append(time.time())
        self.__automationModule = AutomationModuleWrapper()
        
        # ID must be retrieved before timer module register groups.
        self.__get_default_group_ids()

        # ===== Register methods =====
        # APIs
        paramSection = KBXString(kbxParamName="section")
        paramLimit = KBXNumber(kbxParamName="limit", kbxParamIsRequired=False, kbxParamMinValue=0, \
                               kbxParamMaxValue=200)
        paramOffset = KBXNumber(kbxParamName="offset", kbxParamIsRequired=False, kbxParamMinValue=0)

        self.register_method(kbxMethodName="list_groups", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_groups,
                             kbxMethodParams=[KBXNumber(kbxParamName="parentId", kbxParamIsRequired=False, kbxParamMinValue=1),
                                              paramSection])
        self.register_method(kbxMethodName="list_methods", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_methods,
                             kbxMethodParams=[KBXNumber(kbxParamName="groupId", kbxParamMinValue=1),
                                              paramSection])
        self.register_method(kbxMethodName="update_kbx_method", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.update_kbx_method,
                             kbxMethodParams=[KBXNumber(kbxParamName="kbxMethodId", kbxParamMinValue=1)])
        self.register_method(kbxMethodName="update_kbx_group", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.update_kbx_group,
                             kbxMethodParams=[KBXNumber(kbxParamName="kbxGroupId", kbxParamMinValue=1)])
        self.register_method(kbxMethodName="list_kbx_methods", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_kbx_methods,
                             kbxMethodParams=[paramLimit,
                                              paramOffset])
        self.register_method(kbxMethodName="list_kbx_groups", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_kbx_groups,
                             kbxMethodParams=[paramLimit,
                                              paramOffset])

        # Rules
        paramRuleId = KBXNumber(kbxParamName="ruleId", kbxParamDecimal=0, kbxParamMinValue=1)

        self.register_method(kbxMethodName="set_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.set_rule)
        self.register_method(kbxMethodName="list_rules", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_rules,
                             kbxMethodParams=[paramLimit,
                                              paramOffset])
        self.register_method(kbxMethodName="get_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.get_rule,
                             kbxMethodParams=[paramRuleId])
        self.register_method(kbxMethodName="delete_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.delete_rule,
                             kbxMethodParams=[paramRuleId])
        self.register_method(kbxMethodName="trigger_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.trigger_rule,
                             kbxMethodParams=[paramRuleId,
                                              KBXBoolean(kbxParamName="checkCondition", kbxParamIsRequired=False)])
        self.register_method(kbxMethodName="enable_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.enable_rule,
                             kbxMethodParams=[paramRuleId,
                                              KBXBoolean(kbxParamName="enabled", kbxParamIsRequired=True)])

        # Scenes
        paramSceneId = KBXNumber(kbxParamName="sceneId", kbxParamdecimal=0, kbxParamMinValue=1)

        self.register_method(kbxMethodName="set_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.set_scene)
        self.register_method(kbxMethodName="execute_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.execute_scene,
                             kbxMethodParams=[paramSceneId,
                                              KBXString(kbxParamName="serUrl", kbxParamIsRequired=False)])
        self.register_method(kbxMethodName="stop_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.stop_scene,
                             kbxMethodParams=[paramSceneId])
        self.register_method(kbxMethodName="delete_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.delete_scene,
                             kbxMethodParams=[paramSceneId])
        self.register_method(kbxMethodName="get_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.get_scene,
                             kbxMethodParams=[paramSceneId])
        self.register_method(kbxMethodName="list_scenes", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_scenes,
                             kbxMethodParams=[paramOffset, paramLimit])
        
        # Scene Execution Results
        paramSerId = KBXString(kbxParamName="serId")
        
        self.register_method(kbxMethodName="get_scene_execution_result", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.get_scene_execution_result,
                             kbxMethodParams=[paramSerId])
        self.register_method(kbxMethodName="retry_scene_execution_result_item", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.retry_scene_execution_result_item,
                             kbxMethodParams=[paramSerId,
                                              KBXNumber(kbxParamName="seriIndex", kbxParamIsRequired=False, kbxParamMinValue=0)])
        self.register_method(kbxMethodName="list_scene_execution_results", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_scene_execution_results,
                             kbxMethodParams=[paramOffset, paramLimit])
        self.register_method(kbxMethodName="delete_scene_execution_result", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.delete_scene_execution_result,
                             kbxMethodParams=[paramSerId])
        
        # Favorited Scenes
        self.register_method(kbxMethodName="set_favorited_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.set_favorited_scene,
                             kbxMethodParams=[paramSceneId,
                                              KBXNumber(kbxParamName="prevSceneId", kbxParamIsRequired=False, kbxParamdecimal=0, kbxParamMinValue=1)])
        self.register_method(kbxMethodName="delete_favorited_scene", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.delete_favorited_scene,
                             kbxMethodParams=[paramSceneId])
        self.register_method(kbxMethodName="list_favorited_scenes", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__automationModule.list_favorited_scenes,
                             kbxMethodParams=[paramLimit,
                                              paramOffset])

    def post_system_connected(self):
        super().post_system_connected()

        DebugModule.DEBUG_POST_SYSTEM_CONNECTED.append(time.time())
        
        self.__automationModule.start()

    def __get_default_group_ids(self):
        try:
            systemId = SharedMethod.get_system_id()

            results = SharedMethod.list_shared_method_groups(kbxGroupAppId=[systemId],
                                                             kbxGroupName=["automation_app", "notification", "service"])

            groups = {group.get("kbxGroupName", "_"):group.get("kbxGroupId") for group in results["groupList"]}

            AppConstants.GROUP_ID_AUTOMATION = groups["automation_app"]
            AppConstants.GROUP_ID_NOTIFICATION = groups["notification"]
            AppConstants.GROUP_ID_SERVICE = groups["service"]

        except Exception as e:
            Logger.log_error("AutomationApp on_system_connected retrying __get_default_group_ids, ex:", e)
            traceback.print_exc()
            raise e
        