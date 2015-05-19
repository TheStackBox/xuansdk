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

from com.cloudMedia.theKuroBox.sdk.dto.deviceDTO import DeviceDTO

class RemoteControlDeviceDTO(DeviceDTO):
    
    def __init__(self, deviceDTO=None):
        pass

    def set_remote_control_type(self, rctype):
        pass

    def get_remote_control_type(self):
        pass

    def set_remote_control_data(self, rcdata):
        pass

    def get_remote_control_data(self):
        pass

    def set_key_data(self, keys):
        pass

    def get_key_data(self):
        pass

    def get_remote_info(self):
        pass

    def set_remote_info(self, info):
        pass

    def get_page(self, pageIndex=None):
        pass

    def add_page(self):
        pass

    def update_page_info(self, index, name, info):
        pass

    def remove_page(self, index):
        pass

    def add_key(self, pageIndex, keyId, data=None):
        pass

    def remove_key(self, pageIndex, keyId):
        pass

    def update_key_data(self, pageIndex, keyId, data=None):
        pass

    def update_keys_data(self, pageIndex, data=[]):
        pass

