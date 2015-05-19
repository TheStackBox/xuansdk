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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObject
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class DeviceController(Module):

    '''
    #===========================================================================
    # Automation Specific Constants
    #===========================================================================
    GROUP_ID_SPEAKER = None
    GROUP_ID_SWITCH = None
    GROUP_ID_DOOR_LOCK = None
    GROUP_ID_HUE = None
    GROUP_ID_DIMMER = None
    GROUP_ID_HORN = None
    GROUP_ID_IPCAMERA = None
    GROUP_ID_POWER_METER = None
    GROUP_ID_POWER_STRIP = None
    GROUP_ID_SENSOR = None
    GROUP_ID_THERMOSTAT = None
    GROUP_ID_TRACKER = None
    GROUP_ID_OTHER = None
    GROUP_ID_MEDIA_PLAYER = None
    GROUP_ID_VIRTUAL_REMOTE_CONTROL = None
    GROUP_ID_NOTIFICATION = None
    GROUP_ID_SERVICE = None
    GROUP_ID_VIRTUAL_ACTIVITY = None

    #===========================================================================
    # Automation Specific Constants
    #===========================================================================
    '''

    # set when register_shared_method; usage: kbxMethodTag=DeviceController.AUTOMATION_TAG_ACTION
    AUTOMATION_ACTION = "automation_action"
    AUTOMATION_CONDITION = "automation_condition"

    AUTOMATION_CONDITION_REQUEST_TIMESTAMP = "timestamp" # returns everytime automation check for your condition. [request.get_arg("timestamp")]
    AUTOMATION_CONDITION_REQUEST_EVENT_TAG = "eventTag" # returns x, only if your method did register for an event. where x = x in (kbxMethodEvent=x)
    AUTOMATION_CONDITION_REQUEST_EVENT_DATA = "eventData" # at the same time, returns the y (eventData) where you fired at self.send_system_event(x, y)
    AUTOMATION_ACTION_REQUEST_TIMESTAMP = "timestamp" # returns if your method is "action" for automation. [request.get_arg("timestamp")]

    def __init__(self, kbxModuleName, parentPath, name="", protocolId="", uniqueType=None, uniqueId="", icon="", isCtrlPanelExist=False, isAdvCtrlPanelExist=False, advDeviceControllerDTO=None):
        pass

    def set_device_init_with_device_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def set_device_remove_from_device_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def set_device_status(self, pairedDeviceId, deviceDTO, enable):
        '''
        child class should override this function to implement their body
        '''
        pass

    def update_device_info(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def request_device_status_update(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

