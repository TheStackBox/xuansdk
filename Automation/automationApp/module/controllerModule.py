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

from automationApp.appConstants import AppConstants
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class ControllerModule(Module):
    '''
    A communicator to external app for *Controllers services.
    '''


    ON_TRIGGER_CALLBACK = lambda ruleId: True

    ON_SHARED_METHOD_UPDATED = lambda eventObject: True
    ON_SHARED_METHOD_DELETED = lambda eventObject: True
    
    ON_SHARED_METHOD_GROUP_UPDATED = lambda eventObject: True
    ON_SHARED_METHOD_GROUP_DELETED = lambda eventObject: True

    def on_system_connected(self):
        super().on_system_connected()
        
        self.register_shared_method(kbxMethodName="on_trigger_callback", kbxMethodFunc=self.on_trigger_callback, kbxMethodIsPrivate=True)
        
        self.register_event_listener(Event.EVENT_SHARED_METHOD_ADDED, self.on_shared_method_updated)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_UPDATED, self.on_shared_method_updated)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_DELETED, self.on_shared_method_deleted)
        
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_ADDED, self.on_shared_method_group_updated)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_UPDATED, self.on_shared_method_group_updated)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_DELETED, self.on_shared_method_group_deleted)
        
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_ADDED, self.__broadcast_group_status_update)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_UPDATED, self.__broadcast_group_status_update)
        self.register_event_listener(Event.EVENT_SHARED_METHOD_GROUP_DELETED, self.__broadcast_group_status_update)

    def on_trigger_callback(self, request):
        self.send_response({"status":"ok"}, request.requestId)
        ControllerModule.ON_TRIGGER_CALLBACK(request.get_arg("ruleId"))
        
    def on_shared_method_updated(self, eventObject):
        ControllerModule.ON_SHARED_METHOD_UPDATED(eventObject)
    
    def on_shared_method_deleted(self, eventObject):
        ControllerModule.ON_SHARED_METHOD_DELETED(eventObject)
    
    def on_shared_method_group_updated(self, eventObject):
        ControllerModule.ON_SHARED_METHOD_GROUP_UPDATED(eventObject)
        
    def on_shared_method_group_deleted(self, eventObject):
        ControllerModule.ON_SHARED_METHOD_GROUP_DELETED(eventObject)
        
    def __broadcast_group_status_update(self, eventObj):
        '''
        Broadcast group updated status so that UI listen to the changes.
        '''
        try:
            eventTag = eventObj["eventTag"]
            eventData = json.loads(eventObj["eventData"])
            
            # Check if group parent id belongs to groups in automation.
            dataToBroadcast = {"kbxGroupId":eventData["kbxGroupId"], 
                               "kbxGroupParentId":eventData["kbxGroupParentId"],
                               "enabled":bool((eventData.get("enabled", True) is not False) and eventTag != Event.EVENT_SHARED_METHOD_GROUP_DELETED)}
    
            eventTagsToBroadcast = {Event.EVENT_SHARED_METHOD_GROUP_ADDED:   AppConstants.EVENT_AUTOMATION_GROUP_ADDED,
                                    Event.EVENT_SHARED_METHOD_GROUP_UPDATED: AppConstants.EVENT_AUTOMATION_GROUP_UPDATED,
                                    Event.EVENT_SHARED_METHOD_GROUP_DELETED: AppConstants.EVENT_AUTOMATION_GROUP_DELETED}
            
            dataToBroadcast = json.dumps(dataToBroadcast)
            
            self.send_web_server_event(eventTagsToBroadcast[eventTag], dataToBroadcast)
        
        except Exception as e:
            Logger.log_warning("AutomationApp __broadcast_group_status_update ex:", e)
