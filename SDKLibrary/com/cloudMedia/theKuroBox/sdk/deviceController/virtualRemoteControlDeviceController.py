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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class VirtualRemoteControlDeviceController(DeviceController):
    
    
    def __init__(self, kbxModuleName, parentPath, name="", protocolId="", uniqueId="", icon="", isCtrlPanelExist=False, isAdvCtrlPanelExist=False, uniqueType=None, advDeviceControllerDTO=None):
        '''
        Constructor
        '''
        pass

    def get_device_status(self, pairedDeviceId):
        pass

    def get_capabilities(self, pairedDeviceId):
        pass

    def get_all_keys(self, pairedDeviceId):
        pass

    def set_key_info(self, pairedDeviceId, pageNum, keyId, data):
        pass

    def add_page(self, pairedDeviceId, pageName, info):
        pass

    def edit_page_info(self, pairedDeviceId, pageNum, pageName, info):
        pass

    def remove_key(self, pairedDeviceId, pageNum, keyId):
        pass

    def remove_page(self, pairedDeviceId, pageNum):
        pass

    def set_keys_info(self, pairedDeviceId, pageNum, keysData):
        pass

    def record_key(self, pairedDeviceId, pageNum, keyId=None):
        pass

    def cancel_record_key(self, pairedDeviceId):
        pass

    def send_key(self, pairedDeviceId, pageNum, keyId):
        pass

    def edit_remote_info(self, pairedDeviceId, info):
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

    def on_request_device_status_update(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

