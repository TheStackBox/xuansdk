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
import json

from automationApp.appConstants import AppConstants
from automationApp.core.groupTracker import GroupTracker
from automationApp.core.methodTracker import MethodTracker
from automationApp.dto.groupDTO import GroupDTO
from automationApp.module.automationModule import AutomationModule
from automationApp.module.deviceManagerModule import DeviceManagerModule
from automationApp.module.timerModule import TimerModule
from automationApp.module.zwaveModule import ZWaveModule
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class AutomationApp(Application):

    def __init__(self):
        pass

    def on_start(self):
        self.__module = AutomationModule()

        #=======================================================================
        # Timer Module
        #=======================================================================
        self.register_module(TimerModule("timer_module", None))

        #=======================================================================
        # Device Module (Mapping to system device manager)
        #=======================================================================
        self.register_module(DeviceManagerModule("device_manager", None))
        self.register_module(ZWaveModule("zwave_module", None))

        #=======================================================================
        # Register methods
        #=======================================================================
        paramLimit = KBXNumber(kbxParamName="limit", kbxParamIsRequired=False, kbxParamMinValue=0, kbxParamMaxValue=AppConstants.UPPER_LIMIT)
        paramOffset = KBXNumber(kbxParamName="offset", kbxParamIsRequired=False, kbxParamMinValue=0)
        paramRuleId = KBXString(kbxParamName="ruleId", kbxParamIsRequired=False)

        self.register_method(kbxMethodName="list_groups", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.list_groups,
                             kbxMethodParams=[KBXNumber(kbxParamName="parentId", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="section"),
                                              paramLimit, paramOffset])
        self.register_method(kbxMethodName="list_methods", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.list_methods,
                             kbxMethodParams=[KBXNumber(kbxParamName="groupId", kbxParamMinValue=0),
                                              KBXString(kbxParamName="section"),
                                              paramLimit, paramOffset])


        self.register_method(kbxMethodName="set_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.set_rule,
                             kbxMethodParams=[KBXString(kbxParamName="trigger", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="condition", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="execution", kbxParamIsRequired=True),
                                              paramRuleId,
                                              KBXString(kbxParamName="ruleName", kbxParamIsRequired=False),
                                              KBXBoolean(kbxParamName="enabled", kbxParamIsRequired=False)]) # -- overwritting mechanism (insert/update)
        self.register_method(kbxMethodName="list_rules", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.list_rules,
                             kbxMethodParams=[paramLimit,
                                              paramOffset])
        self.register_method(kbxMethodName="get_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.get_rule,
                             kbxMethodParams=[paramRuleId])
        self.register_method(kbxMethodName="delete_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.delete_rule,
                             kbxMethodParams=[paramRuleId])
        self.register_method(kbxMethodName="trigger_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.trigger_rule,
                             kbxMethodParams=[paramRuleId,
                                              KBXBoolean(kbxParamName="checkCondition", kbxParamIsRequired=False)])
        self.register_method(kbxMethodName="enable_rule", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.__module.enable_rule,
                             kbxMethodParams=[paramRuleId,
                                              KBXBoolean(kbxParamName="enabled", kbxParamIsRequired=True)])

    def on_system_connected(self):
        #=======================================================================
        # Get all group ids from system app.
        #=======================================================================
        self.__get_default_group_ids()

        #=======================================================================
        # Register shared methods
        #=======================================================================
        self.register_shared_method(kbxMethodName="automation_timer_callback", kbxMethodIsPrivate=True,
                                    kbxMethodFunc=self.__module.timer_callback) # redirect to ruleService.timer_callback

        self.register_shared_method(kbxMethodName="list_group_ids",
                                    kbxMethodFunc=self.__list_group_ids) # allow developer to get the sub groups info.

    def post_system_connected(self):
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_ACTIVATED, self.__update_method_tracker)
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_DEACTIVATED, self.__update_method_tracker)
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_DELETED, self.__update_method_tracker)
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_UPDATED, self.__update_method_tracker)
        
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_DELETED, self.__update_group_tracker)
        Application.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_UPDATED, self.__update_group_tracker)

        self.__module.start()

    def on_stop(self):
        pass

    def on_destroy(self):
        pass

    def __get_default_group_ids(self):
        try:
            systemId = SharedMethod.get_system_id()
            groups, total = SharedMethod.list_shared_method_groups(kbxGroupAppId=[systemId],
                                                                   kbxGroupName=["automation_app",
                                                                                 "speaker",
                                                                                 "switch",
                                                                                 "door_lock",
                                                                                 "hue",
                                                                                 "dimmer",
                                                                                 "horn",
                                                                                 "ipcamera",
                                                                                 "power_strip",
                                                                                 "sensor",
                                                                                 "notification",
                                                                                 "service"])
            if total != 12:
                Logger.log_debug("Default Groups incorrect count:", total)

            groups = {group.get(GroupDTO.PROP_GROUP_NAME, "_"):group.get(GroupDTO.PROP_GROUP_ID) for group in groups}

            AppConstants.GROUP_ID_AUTOMATION = groups.get("automation_app")
            AppConstants.GROUP_ID_SPEAKER = groups.get("speaker")
            AppConstants.GROUP_ID_SWITCH = groups.get("switch")
            AppConstants.GROUP_ID_DOOR_LOCK = groups.get("door_lock")
            AppConstants.GROUP_ID_HUE = groups.get("hue")
            AppConstants.GROUP_ID_DIMMER = groups.get("dimmer")
            AppConstants.GROUP_ID_HORN = groups.get("horn")
            AppConstants.GROUP_ID_IPCAMERA = groups.get("ipcamera")
            AppConstants.GROUP_ID_POWER_STRIP = groups.get("power_strip")
            AppConstants.GROUP_ID_SENSOR = groups.get("sensor")
            AppConstants.GROUP_ID_NOTIFICATION = groups.get("notification")
            AppConstants.GROUP_ID_SERVICE = groups.get("service")

        except Exception as e:
            Logger.log_debug("__get_all_group_ids ex: ", e)
            raise Exception("Unable to get groups from system app.")

    def __list_group_ids(self, request):
            self.send_response({"speaker":AppConstants.GROUP_ID_SPEAKER,
                                "switch":AppConstants.GROUP_ID_SWITCH,
                                "door_lock":AppConstants.GROUP_ID_DOOR_LOCK,
                                "hue":AppConstants.GROUP_ID_HUE,
                                "dimmer":AppConstants.GROUP_ID_DIMMER,
                                "horn":AppConstants.GROUP_ID_HORN,
                                "ipcamera":AppConstants.GROUP_ID_IPCAMERA,
                                "power_strip":AppConstants.GROUP_ID_POWER_STRIP,
                                "sensor":AppConstants.GROUP_ID_SENSOR,
                                "notification":AppConstants.GROUP_ID_NOTIFICATION,
                                "service":AppConstants.GROUP_ID_SERVICE}, request.requestId)


    def __update_method_tracker(self, eventObj):
        try:
            Logger.log_debug("Received method update event:", eventObj)
            
            eventTag = eventObj["eventTag"]
            eventData = json.loads(eventObj["eventData"])

            methodId = eventData["kbxMethodId"]
            if eventTag == Event.EVENT_SHARED_METHOD_ACTIVATED:
                MethodTracker.METHOD_ACTIVATED_CB(methodId)
            elif eventTag == Event.EVENT_SHARED_METHOD_DEACTIVATED:
                MethodTracker.METHOD_DEACTIVATED_CB(methodId)
            elif eventTag == Event.EVENT_SHARED_METHOD_DELETED:
                MethodTracker.METHOD_REMOVED_CB(methodId)
            elif eventTag == Event.EVENT_SHARED_METHOD_UPDATED:
                MethodTracker.METHOD_UPDATED_CB(methodId)
        except Exception as e:
            Logger.log_debug("Unknown Method Update Error:", e)

    def __update_group_tracker(self, eventObj):
        try:
            Logger.log_debug("Received group update event:", eventObj)
            
            eventTag = eventObj["eventTag"]
            eventData = json.loads(eventObj["eventData"])

            groupId = eventData["kbxGroupId"]
            if eventTag == Event.EVENT_SHARED_METHOD_GROUP_DELETED:
                GroupTracker.GROUP_REMOVED_CB(groupId)
            elif eventTag == Event.EVENT_SHARED_METHOD_GROUP_UPDATED:
                GroupTracker.GROUP_UPDATED_CB(groupId)
        except Exception as e:
            Logger.log_debug("Unknown Group Update Error:", e)


