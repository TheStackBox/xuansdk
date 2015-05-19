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

class VirtualActivityControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device capabilities.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def get_activities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get activities.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"usage":""}
        '''
        pass

    @staticmethod
    def set_activity_start(pairedDeviceId, activityIndex, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set activity start.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        activityIndex:String :- Activity ID return from get_activities
        return:Dictionary :eg- {"success": true}
        '''
        pass

