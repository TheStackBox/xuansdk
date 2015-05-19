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

class TrackerControllerService(object):
    '''
    Controller Service for Tracker Device.
    '''
    
    
    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the tracker.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get status of the tracker.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def alert(pairedDeviceId, alertLevel=1, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Signal tracker to alert.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        alertLevel:Number :- Alert level ranging from 0 (No alert) - 2 (High alert)
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def set_link_loss_value(pairedDeviceId, alertLevel=1, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set link loss value of the tracker.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        alertLevel:Number :- Alert level ranging from 0 (No alert) - 2 (High alert)
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def get_battery_level(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery status.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"value":50}
        '''
        pass

    @staticmethod
    def get_link_loss_value(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get link loss value.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"value":true}
        '''
        pass

    @staticmethod
    def get_signal_info(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get signal strength RSSI and approximate distance info.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"rssi":-66, "distance":0.1223}
        '''
        pass

