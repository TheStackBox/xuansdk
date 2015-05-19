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
import threading
import time

from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class DebugModule(Module):
    
    
    DEBUG_AUTOMATION_VERSION = "2.1 (update 4)"
    
    DEBUG_ON_SYSTEM_CONNECTED = deque()
    DEBUG_POST_SYSTEM_CONNECTED = deque()
    DEBUG_PROCESS_UP_TIME = time.time()
    
    DEBUG_TEST_EVENT = "AUTOMATION_DEBUG_TEST_EVENT"
    
    
    def on_system_connected(self):
        super().on_system_connected()
        
        self.register_method(kbxMethodName="get_version", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.get_version)
        self.register_method(kbxMethodName="get_process_info", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.get_process_info)
        self.register_method(kbxMethodName="enable_logger", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.enable_logger)
        self.register_method(kbxMethodName="disable_logger", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.disable_logger)
        self.register_method(kbxMethodName="test_system_event", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.test_system_event)
        self.register_method(kbxMethodName="test_web_event", kbxMethodIsPrivate=True,
                             kbxMethodFunc=self.test_web_event)
        
    def get_version(self, request):
        self.send_response({"version":DebugModule.DEBUG_AUTOMATION_VERSION}, request.requestId)
        
    def get_process_info(self, request):
        self.send_response({"process_up_time":DebugModule.DEBUG_PROCESS_UP_TIME,
                            "current_time":time.time(),
                            "on_system_connected":DebugModule.DEBUG_ON_SYSTEM_CONNECTED,
                            "post_system_connected":DebugModule.DEBUG_POST_SYSTEM_CONNECTED}, request.requestId)
        
    def enable_logger(self, request):
        Logger.set_enable_debug(True)
        self.send_response({"status":"ok"}, request.requestId)
        
    def disable_logger(self, request):
        Logger.set_enable_debug(False)
        self.send_response({"status":"ok"}, request.requestId)
        
    def test_system_event(self, request):
        
        event = threading.Event()
        steps = deque()
        
        def event_listener(eventObject):
            event.set()
            return
        
        try:
            steps.append("Test Register Event Tag ... (" + str(int(time.time())) + ")")
            self.register_event(DebugModule.DEBUG_TEST_EVENT)
            steps.append("Register Event Tag: OK (" + str(int(time.time())) + ")")
            
            steps.append("Test Register Event Listener ... (" + str(int(time.time())) + ")")
            self.register_event_listener(DebugModule.DEBUG_TEST_EVENT, event_listener)
            steps.append("Register Event Listener: OK (" + str(int(time.time())) + ")")
            
            steps.append("Test Send System Event... (" + str(int(time.time())) + ")")
            self.send_system_event(DebugModule.DEBUG_TEST_EVENT, "{}")
            steps.append("Send System Event: OK (" + str(int(time.time())) + ")")
            
            steps.append("Wait System Event At Most 30 SEC... (" + str(int(time.time())) + ")")
            isSet = event.wait(30)
            if not isSet:
                steps.append("System Event TIMEOUT... (" + str(int(time.time())) + ")")
            else:
                steps.append("System Event Respond: OK (" + str(int(time.time())) + ")")
            
            steps.append("Test Unregister Event Listener ... (" + str(int(time.time())) + ")")
            self.unregister_event_listener(DebugModule.DEBUG_TEST_EVENT, event_listener)
            steps.append("Unregister Event Listener: OK (" + str(int(time.time())) + ")")
            
            steps.append("Test Unregister Event Tag ... (" + str(int(time.time())) + ")")
            self.unregister_event(DebugModule.DEBUG_TEST_EVENT)
            steps.append("Unregister Event Tag: OK (" + str(int(time.time())) + ")")
        
        except Exception as e:
            steps.append("Error:" + str(e) + " ... (" + str(int(time.time())) + ")")
        
        self.send_response({"status":"ok", "steps":steps}, request.requestId)
        
    def test_web_event(self, request):
        
        try:
            eventTag = DebugModule.DEBUG_TEST_EVENT
            eventData = '{"status":"ok", "humans":"Automation web server event tester"}'
            
            self.send_web_server_event(eventTag, eventData)
            
            self.send_response({"status":"ok", "eventTag":eventTag, "eventData":eventData}, request.requestId)
            
        except Exception as e:
            self.send_response({"status":"error", "reason":str(e)}, request.requestId)