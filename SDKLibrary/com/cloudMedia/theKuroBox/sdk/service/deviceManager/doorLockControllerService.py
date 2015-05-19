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
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class DoorLockControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get capabilities of the door lock.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get door lock status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def set_lock(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Lock door.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"lock":true}
        '''
        pass

    @staticmethod
    def set_unlock(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Unlock door.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def get_battery_level(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery status.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"batteryLevel":50}
        '''
        pass

    @staticmethod
    def get_lock_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery status.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"status":true}
        '''
        pass

