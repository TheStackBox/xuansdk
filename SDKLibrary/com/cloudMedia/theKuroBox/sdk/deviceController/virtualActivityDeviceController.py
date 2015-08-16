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
from threading import Lock

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.deviceController import DeviceController
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.dto.deviceDTO import DeviceDTO
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxHidden import KBXHidden
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObject
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class VirtualActivityDeviceController(DeviceController):

    def __init__(self, kbxModuleName, parentPath, name="", protocolId="", uniqueId="", icon="", isCtrlPanelExist=False, isAdvCtrlPanelExist=False, uniqueType=None, advDeviceControllerDTO=None):
        pass

    def get_capabilities(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def get_activities(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def set_activity_start(self, pairedDeviceId, deviceDTO, activityIndex):
        '''
        child class should override this function to implement their body
        '''
        pass

    def get_status(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def on_device_initial(self, pairedDeviceId, deviceDTO, groupName, groupId, methodInitialStatus):
        '''
        child class should override this function to implement their body
        '''
        pass

    def on_device_remove(self, pairedDeviceId, deviceDTO, groupName, groupId):
        '''
        child class should override this function to implement their body
        '''
        pass

    def get_device_status(self, pairedDeviceId):
        pass

    def on_device_enable(self, pairedDeviceId, deviceDTO, groupName, groupId):
        '''
        child class should override this function to implement their body
        '''
        pass

    def on_device_disable(self, pairedDeviceId, deviceDTO, groupName, groupId):
        '''
        child class should override this function to implement their body
        '''
        pass

    def on_request_device_status_update(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

