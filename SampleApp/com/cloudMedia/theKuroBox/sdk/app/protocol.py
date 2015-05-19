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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.dto.deviceDTO import DeviceDTO
from com.cloudMedia.theKuroBox.sdk.dto.protocolDTO import ProtocolDTO
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObject
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class Protocol(Module):

      
    def __init__(self, kbxModuleName, parentPath, protocolName="", protocolIcon="", isEnable=False, uniqueType=""):
        pass

    def on_system_connected(self):
        pass

    def get_protocol_details(self):
        '''
        Caution: child class should not override this function
        '''
        pass

    def get_supported_event_tag_list(self, protocolId, **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def update_paired_devices_status(self, protocolId, deviceList):
        '''
        child class should override this function to implement their body
        '''
        pass

    def notify_device_status_update(self, deviceDTO=None):
        '''
        Caution: child class should not override this function
        '''
        pass

    def set_protocol_status(self, enable=False):
        '''
        Caution: child class should not override this function
        '''
        pass

    def refresh_device_status(self, pairedDeviceId=""):
        '''
        Caution: child class should not override this function
        '''
        pass

    def set_device_scan_start(self, protocolId="", **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def notify_device_scan_done(self, success=True, errorCode="", errorMessage=""):
        '''
        Caution: child class should not override this function
        '''
        pass

    def set_device_scan_stop(self, protocolId="", **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def notify_device_scan_stop(self, success=True, errorCode="", errorMessage=""):
        '''
        Caution: child class should not override this function
        '''
        pass

    def get_device_list(self, protocolId="", **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def set_device_pair(self, protocolId="", deviceId=None, **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def notify_device_pair_done(self, deviceDTO=None, success=True, errorCode="", errorMessage=""):
        '''
        Caution: child class should not override this function
        '''
        pass

    def set_device_unpair(self, pairedDeviceId="", deviceDTO=None, **param):
        '''
        child class should override this function to implement their body
        '''
        pass

    def notify_device_unpair_done(self, pairedDeviceId="", deviceDTO=None, success=True, errorCode="", errorMessage=""):
        '''
        Caution: child class should not override this function
        '''
        pass

    def get_device_enable_status(self, pairedDeviceId="", deviceDTO=None):
        '''
        child class should override this function to implement their body
        '''
        pass

