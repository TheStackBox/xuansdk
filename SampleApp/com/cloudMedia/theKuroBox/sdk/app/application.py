##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

import json
import os, signal
import traceback

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
        NOTE: If you override this method, remember to call super().on_system_connected().
        
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
        NOTE: If you override this method, remember to call super().post_system_connected().
        
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

        Returns:
        Unique method id.
        '''
        pass

    def update_method(self, kbxMethodName, kbxMethodFunc=SharedMethod.get_empty_placeholder(), kbxMethodIsPrivate=SharedMethod.get_empty_placeholder(),
                        kbxMethodLabel=SharedMethod.get_empty_placeholder(), kbxMethodDesc=SharedMethod.get_empty_placeholder(), kbxMethodParams=SharedMethod.get_empty_placeholder(),
                        **kbxMethodProps):
        pass

    def activate_method(self, kbxMethodName):
        pass

    def deactivate_method(self, kbxMethodName):
        pass

    def delete_method(self, kbxMethodName):
        pass

    def get_method(self, kbxMethodName):
        '''
        Get registered method properties.
        You can only get methods registered by this module.
        
        "kbxMethodFunc" is NOT included in return dictionary.

        Params:
        kbxMethodName:String - [Required] Method name.
        
        Returns
        Dictionary contains of method properties.
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
        **kbxMethodExtra - Any extra key-values. They must be able to be converted into json string altogether

        Returns:
        Unique method id.
        '''
        pass

    def update_shared_method(self, kbxMethodName, kbxGroupId=None, kbxMethodFunc=SharedMethod.get_empty_placeholder(), kbxMethodIsPrivate=SharedMethod.get_empty_placeholder(),
                             kbxMethodLabel=SharedMethod.get_empty_placeholder(), kbxMethodDesc=SharedMethod.get_empty_placeholder(),
                             kbxMethodTag=SharedMethod.get_empty_placeholder(), kbxMethodParams=SharedMethod.get_empty_placeholder(), **kbxMethodProps):
        pass

    def activate_shared_method(self, kbxMethodName, kbxGroupId=None):
        pass

    def deactivate_shared_method(self, kbxMethodName, kbxGroupId=None):
        pass

    def delete_shared_method(self, kbxMethodName, kbxGroupId=None):
        pass

    def get_shared_method(self, kbxMethodName, kbxGroupId=None):
        '''
        Get registered shared method properties.
        You can only get shared methods registered by this module.
        For shared methods registered by other modules or apps, see APIs in SharedMethod.py.
        
        "kbxMethodId" is included in return dictionary.
        "kbxMethodFunc" is NOT included in return dictionary.

        Params:
        kbxMethodName:String - [Required] Method name.
        kbxGroupId:Integer - [Required] Method group id.
        
        Returns
        Dictionary contains of shared method properties.
        '''
        pass

    def register_shared_method_group(self, kbxGroupName, kbxGroupLabel=None, kbxGroupDesc=None, kbxGroupParentId=None, **kbxGroupProps):
        pass

    def update_shared_method_group(self, kbxGroupName, kbxGroupParentId=None,
                                   kbxGroupLabel=SharedMethod.get_empty_placeholder(), kbxGroupDesc=SharedMethod.get_empty_placeholder(), **kbxGroupProps):
        '''
        Update registered shared method group by group properties.

        Params:
        kbxGroupName:String - [Required] Name of the group.
        kbxGroupParentId:Integer - [Required] Parent group id of the group
        kbxMethodLabel:String - [Optional] New label for the group.
        kbxMethodDesc:String - [Optional] New description for the group.
        '''
        pass

    def update_shared_method_group_parent_id(self, newKBXGroupParentId, kbxGroupName, kbxGroupParentId=None):
        '''
        Update shared method group's kbxGroupParentId.
        
        Params:
        newKBXGroupParentId:Integer - [Required] New parent group id.
        kbxGroupName:String - [Required] Name of the group to be updated.
        kbxGroupParentId:Integer - [Required] Current parent group id.
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

    def get_shared_method_group(self, kbxGroupName, kbxGroupParentId=None):
        '''
        Get properties of registered shared method group. 
        You can get group registered at different module as long as it is within the same app. 
        To get groups registered by other apps, see APIs in SharedMethod.py.
        
        "kbxGroupId" is included in return dictionary.
        
        Params:
        kbxGroupName:String - [Required] Name of the group.
        kbxGroupParentId:Integer - [Required] Parent group id of the group.
        
        Returns:
        Dictionary which contains of group properties.
        '''
        pass

    @staticmethod
    def send_response(data, requestId, returnValue=100, returnMessage=""):
        '''
        Respond data to a particular request
        data : The data to respond (must be dictionary and is a valid JSON object)
        requestId : The request ID to respond
        returnValue : 100 for success, 10000 and above for error
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

