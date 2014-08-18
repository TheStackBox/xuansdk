##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
import json
import os, signal

from com.cloudMedia.theKuroBox.core.sharedMethodRepo import SharedMethodRepo
from com.cloudMedia.theKuroBox.core.spine import Spine
from com.cloudMedia.theKuroBox.core.webServer import WebServer
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.ipcClient import IPCClient
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class Application(object):
    '''
    Base class of an Application. All application MUST extends this class
    '''
    
    __unset__ = []
    
    def get_app_runnig_status(self):
        '''
        Get whether this app is running or paused
        Return True / False
        '''
        pass

    def on_start(self):
        '''
        Daemon App should override this function to implement their body
        '''
        pass

    def on_stop(self):
        '''
        Daemon App should override this function to implement their body
        '''
        pass

    def on_destroy(self):
        '''
        Daemon App should override this function to implement their body
        '''
        pass

    def on_system_connected(self):
        '''
        Daemon App should override this function to implement their body
        Developer should put their code for dealing with system here, such as:
        - Register Event
        - Register Event Listener
        - Register Shared Method

        For System Connected timing in Module, please refer to Module.on_system_connected
        '''
        pass

    def post_system_connected(self):
        '''
        Daemon App should override this function to implement their body
        This timing is located after on_system_connected timing in application and all modules
        '''
        pass

    def register_module(self, module):
        '''
        Register the module developer want to expose to external user
        modulename - The module name
        module - The module class
        '''
        pass

    def register_method(self, kbxMethodName, kbxMethodFunc, kbxMethodIsPrivate=False,
                        kbxMethodLabel=None, kbxMethodDesc=None, kbxMethodParams=None, **kbxMethodExtra):
        '''
        Expose a method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        kbxMethodFunc:Callable - [Required] Reference to a callable instance.
        kbxMethodIsPrivate:Boolean - [Optional] Private method is not visible (but callable) to third party. False by default.
        kbxMethodLabel:String - [Optional] Label for the method.
        kbxMethodDesc:String - [Optional] Description for the method.
        kbxMethodParams:List<KBXParam> - Description of the arguments the method expected to receive.
        **kbxMethodExtra - Any extra key-values. They must be able to be converted into json string altogether
        '''
        pass


    def update_method(self, kbxMethodName, kbxMethodFunc=__unset__, kbxMethodIsPrivate=__unset__,
                        kbxMethodLabel=__unset__, kbxMethodDesc=__unset__, kbxMethodParams=__unset__,
                        **kbxMethodProps):
        '''
        Update an exposed method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        kbxMethodFunc:Callable - [Required] Reference to a callable instance.
        kbxMethodIsPrivate:Boolean - [Optional] Private method is not visible (but callable) to third party. False by default.
        kbxMethodLabel:String - [Optional] Label for the method.
        kbxMethodDesc:String - [Optional] Description for the method.
        kbxMethodParams:List<KBXParam> - Description of the arguments the method expected to receive.
        **kbxMethodExtra - Any extra key-values. They must be able to be converted into json string altogether
        '''
        pass

    def activate_method(self, kbxMethodName):
        '''
        Activate an exposed method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        '''
        pass

    def deactivate_method(self, kbxMethodName):
        '''
        Deactivate an exposed method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        '''
        pass

    def delete_method(self, kbxMethodName):
        '''
        Delete an exposed method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        '''
        pass

    def register_shared_method(self, kbxMethodName, kbxMethodFunc, kbxMethodIsPrivate=False, kbxGroupId=None,
                               kbxMethodLabel=None, kbxMethodDesc=None, kbxMethodTag=None, kbxMethodParams=None, **kbxMethodProps):
        '''
        Expose a method to external application as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        kbxMethodFunc:Callable - [Required] Reference to a callable instance.
        kbxMethodIsPrivate:Boolean - [Optional] Private method is not visible (but callable) to third party. False by default.
        kbxGroupId:Integer - [Optional] Id of shared method group. Group can be registered through "register_shared_method_group".
        kbxMethodLabel:String - [Optional] Label for the method.
        kbxMethodDesc:String - [Optional] Description for the method.
        kbxMethodTag:List<String> - Semantic tags for the method.
        kbxMethodParams:List<KBXParam> - Description of the arguments the method expected to receive.
        **kbxMethodProps - Any extra key-values. They must be able to be converted into json string altogether.

        Returns:
        Unique method id if kbxMethodIsPrivate = False.

        Automation:
        kbxMethodTag:String - [Required] "automation_action" or "automation_condition" so that automation app is able to identify this method.
        kbxMethodEvent:String - [Optional] Inform automation app that this method does fire event as a trigger.

        * For "automation_condition", include a key named "value" which has boolean value for automation app to determine if the criteria for this condition has been met.
        '''
        pass

    def update_shared_method(self, kbxMethodName, kbxGroupId=None, kbxMethodFunc=__unset__, kbxMethodIsPrivate=__unset__,
                             kbxMethodLabel=__unset__, kbxMethodDesc=__unset__,
                             kbxMethodTag=__unset__, kbxMethodParams=__unset__, **kbxMethodProps):
        '''
        Update an exposed method to external application as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the shared method.
        kbxMethodFunc:Callable - [Required] Reference to a callable instance.
        kbxMethodIsPrivate:Boolean - [Optional] Private method is not visible (but callable) to third party. False by default.
        kbxGroupId:Integer - [Optional] Id of shared method group. Group can be registered through "register_shared_method_group".
        kbxMethodLabel:String - [Optional] Label for the method.
        kbxMethodDesc:String - [Optional] Description for the method.
        kbxMethodTag:List<String> - Semantic tags for the method.
        kbxMethodParams:List<KBXParam> - Description of the arguments the method expected to receive.
        **kbxMethodExtra - Any extra key-values. They must be able to be converted into json string altogether
        '''

        pass

    def activate_shared_method(self, kbxMethodName, kbxGroupId=None):
        '''
        Activate an exposed method to external application as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the shared method.
        '''
        pass

    def deactivate_shared_method(self, kbxMethodName, kbxGroupId=None):
        '''
        Deactivate an exposed method to external application as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the shared method.
        '''
        pass

    def delete_shared_method(self, kbxMethodName, kbxGroupId=None):
        '''
        Delete an exposed method to external application as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the shared method.
        '''
        pass

    def register_shared_method_group(self, kbxGroupName, kbxGroupLabel=None, kbxGroupDesc=None, kbxGroupParentId=None, **kbxGroupProps):
        '''
        Register a group for methods. SystemException will be raised on error.

        Params:
        kbxGroupName:String - [Required] Name of the group, it must be unique per app.
        kbxGroupDesc:String - [Optional] Semantically describing the group.
        kbxParentId:Integer - [Optional] Parent id (if any) of this group.
        **kbxGroupExtraInfo - [Optional] Any extra info in key value pairs.

        Returns:
        group id (integer)

        Automation:
        kbxGroupIcon:String - [Required] Icon of this group for automation app.
        '''
        pass

    def update_shared_method_group(self, kbxGroupName, kbxGroupParentId=None,
                                   kbxGroupLabel=__unset__, kbxGroupDesc=__unset__, **kbxGroupProps):
        '''
        Update registered shared method group by group properties.

        Params:
        kbxGroupName:String - [Required] Name of the group.
        kbxGroupParentId:Integer - [Required] Parent group id of the group
        kbxMethodLabel:String - [Optional] New label for the group.
        kbxMethodDesc:String - [Optional] New description for the group.
        '''
        pass


    def delete_shared_method_group(self, kbxGroupName, kbxGroupParentId=None):
        '''
        Delete registered shared method group by unique group id. All sub-groups and corresponding shared methods will be deleted.

        Params:
        kbxGroupName:String - [Required] Name of the group.
        kbxGroupParentId:Integer - [Required] Parent group id of the group
        '''
        pass

    @staticmethod
    def send_response(data, requestId, returnValue=100, returnMessage=""):
        '''
        Respond data to a particular request
        data : The data to respond
        requestId : The request ID to respond
        returnValue : 100 for success, other value for error
        '''
        pass

    @staticmethod
    def send_web_server_event(eventTag, eventData):
        '''
        Fire an event out to any external interface registered through web server
        eventTag : A string to indicate what event to fire
        eventData : The data / content of the event
        '''
        pass

    @staticmethod
    def send_system_event(eventTag, eventData):
        '''
        Fire an event to system to broadcast to any python app listening to this event
        eventTag : A string to indicate what event to fire
        eventData : The data / content of the event
        '''
        pass

    @staticmethod
    def register_event(eventTag):
        '''
        Register an event tag
        eventTag : The eventTag type tag

        Return : true if the register is successful, false otherwise
        '''
        pass

    @staticmethod
    def unregister_event(eventTag):
        '''
        Unregister an event tag
        eventTag : The eventTag type tag
        '''
        pass

    @staticmethod
    def register_event_listener(eventTag, callback):
        '''
        Register an event listener
        eventTag : The eventTag type tag
        callback : Callback function

        Return : true if the register is successful, false otherwise
        '''
        pass

    @staticmethod
    def unregister_event_listener(eventTag, callback):
        '''
        Unregister an event listener
        eventTag : The eventTag type tag
        callback : Callback function
        '''
        pass
