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
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod


class DoorLockControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    

    @staticmethod
    def set_lock(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Lock door.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    

    @staticmethod
    def set_unlock(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Unlock door.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    

    @staticmethod
    def get_battery_level(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    

    @staticmethod
    def get_lock_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    
