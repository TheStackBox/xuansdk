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

from _collections import deque
import json
import threading, signal

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParam import KBXParam
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class Module(object):
    '''
    Module Base Class
    '''

    def __init__(self, kbxModuleName, parentModulePath):
        '''
        Constructor
        '''
        pass

    def register_module(self, module):
        '''
        Register the module developer want to expose to external user
        moduleName - The module name
        module - The module class
        '''
        pass

    def register_protocol(self, protocol):
        '''
        Register the protocol developer want to expose to external user
        protocolName - The protocol name
        protocol - The protocol class
        '''
        pass

    def register_device_controller(self, deviceController):
        '''
        Register the device controller developer want to expose to external user
        deviceControllerName - The device controller name
        deviceController - The device controller class
        '''
        pass

    def register_advance_device_controller(self, advDeviceController):
        '''
        Register the advance device controller developer want to expose to external user
        advDeviceControllerName - The advance device controller name
        advDeviceController - The advance device controller class
        '''
        pass

    def register_method(self, kbxMethodName, kbxMethodFunc, kbxMethodIsPrivate=False,
                        kbxMethodLabel=None, kbxMethodDesc=None, kbxMethodParams=None, 
                        kbxMethodStatus=SharedMethod.METHOD_STATUS_ACTIVE, **kbxMethodProps):
        '''
        Expose a method to web server as a service.

        Params:
        kbxMethodName:String - [Required] An identifiable string of the method for web server.
        kbxMethodFunc:Callable - [Required] Reference to a callable instance.
        kbxMethodIsPrivate:Boolean - [Optional] Private method is not visible (but callable) to third party. False by default.
        kbxMethodLabel:String - [Optional] Label for the method.
        kbxMethodDesc:String - [Optional] Description for the method.
        kbxMethodParams:List<KBXParam> - Description of the arguments the method expected to receive.
        kbxMethodStatus:Integer - [Optional] Initial status of the method. It always revert to active status if invalid status is given.
        **kbxMethodProps - Any extra key-values. They must be able to be converted into json string altogether

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
                               kbxMethodLabel=None, kbxMethodDesc=None, kbxMethodTag=None, kbxMethodParams=None, 
                               kbxMethodStatus=SharedMethod.METHOD_STATUS_ACTIVE, **kbxMethodProps):
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
        kbxMethodStatus:Integer - [Optional] Initial status of the method. It always revert to active status if invalid status is given.
        **kbxMethodProps - Any extra key-values. They must be able to be converted into json string altogether.

        Returns:
        Unique method id.

        Automation:
        kbxMethodTag:String - [Required] "automation_action" or "automation_condition" so that automation app is able to identify this method.
        kbxMethodEvent:String - [Optional] Inform automation app that this method does fire event as a trigger.
        kbxMethodIdentifier:String - [Optional] Identifier used to inform automation app which device is involved (when multiple devices share the same event tag).
        
        * For "automation_condition", include a key named "value" which has boolean value for automation app to determine if the criteria for this condition has been met.
        '''
        pass

    def update_shared_method(self, kbxMethodName, kbxGroupId=None, kbxMethodFunc=SharedMethod.get_empty_placeholder(), kbxMethodIsPrivate=SharedMethod.get_empty_placeholder(),
                             kbxMethodLabel=SharedMethod.get_empty_placeholder(), kbxMethodDesc=SharedMethod.get_empty_placeholder(),
                             kbxMethodTag=SharedMethod.get_empty_placeholder(), kbxMethodParams=SharedMethod.get_empty_placeholder(), **kbxMethodProps):
        '''
        Update registered shared method by method properties.

        Params:
        kbxMethodName:Integer - [Required] Method name.
        kbxGroupId:Integer - [Required] Method group id.
        kbxModuleName:String - [Required] Module name.
        kbxMethodLabel:String - [Optional] New labe for the method.
        kbxMethodDesc:String - [Optional] New description of the method.
        kbxMethodTag:List<String> - [Optional] New method tags.
        kbxMethodParams:List<KBXParam> - [Optional] New method params.
        '''
        pass

    def activate_shared_method(self, kbxMethodName, kbxGroupId=None):
        pass

    def deactivate_shared_method(self, kbxMethodName, kbxGroupId=None):
        pass

    def delete_shared_method(self, kbxMethodName, kbxGroupId=None):
        '''
        Delete registered shared method by method properties.

        Params:
        kbxMethodName:String - [Required] Method name.
        kbxGroupId:Integer - [Required] Method group id.
        kbxModuleName:String - [Required] Module name.
        '''
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

    def register_shared_method_group(self, kbxGroupName, kbxGroupParentId=None, kbxGroupLabel=None, kbxGroupDesc=None, **kbxGroupProps):
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

    def get_abs_module_path(self):
        '''
        Return the absolute path of this module
        '''
        pass

    def get_module_name(self):
        '''
        Return the module name
        '''
        pass

    def on_system_connected(self):
        '''
        Daemon App should override this method to implement its body.
        NOTE: If you override this method, remember to call super().on_system_connected().

        Developer should put their code for dealing with system here, such as:
        - Register Event
        - Register Event Listener
        - Register Shared Method

        For System Connected timing in Application, please refer to Application.on_system_connected
        '''
        pass

    def post_system_connected(self):
        '''
        Daemon App should override this method to implement its body
        NOTE: If you override this method, remember to call super().post_system_connected().
        
        This timing is located after on_system_connected timing in application and all modules, as well as Application.post_system_connected
        '''
        pass

    def send_response(self, data, requestId, returnValue=100, returnMessage=""):
        '''
        Send response back to Web Server / IPC
        '''
        pass

    def send_web_server_event(self, eventTag, eventData):
        '''
        Fire event to external instance listening to web server event
        '''
        pass

    def send_system_event(self, eventTag, eventData):
        '''
        Request System to fire event to all listening app
        '''
        pass

    def register_event(self, eventTag):
        '''
        Register an event tag
        eventTag : The eventTag type tag

        Return : true if the register is successful, false otherwise
        '''
        pass

    def unregister_event(self, eventTag):
        '''
        Unregister an event tag
        eventTag : The eventTag type tag
        '''
        pass

    def register_event_listener(self, eventTag, callback):
        '''
        Register an event listener
        eventTag : The eventTag type tag
        callback : Callback function

        Return : true if the register is successful, false otherwise
        '''
        pass

    def unregister_event_listener(self, eventTag, callback):
        '''
        Unregister an event listener
        eventTag : The eventTag type tag
        callback : Callback function
        '''
        pass

