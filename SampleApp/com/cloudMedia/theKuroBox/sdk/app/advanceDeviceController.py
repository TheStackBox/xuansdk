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
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObject
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class AdvanceDeviceController(Module):

    def __init__(self, kbxModuleName, parentPath, name="", uniqueId=""):
        pass

    def init_device_with_advanced_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def get_automation_group_list(self):
        pass

    def get_automation_group(self, id):
        pass

    def remove_device_with_advanced_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def enable_device_status_with_advanced_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def disable_device_status_with_advanced_controller(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

    def get_advanced_control_list(self, pairedDeviceId, deviceDTO):
        '''
        child class should override this function to implement their body
        '''
        pass

