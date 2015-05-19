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

class VirtualRemoteControlControllerService(object):
    '''
    Controller Service for Tracker Device.
    '''
    
    
    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def get_all_keys(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def set_key_info(pairedDeviceId, pageNum, keyId, data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def add_page(pairedDeviceId, pageName=None, info=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        pageName:String       :- The name for the page. Default to "Page [PAGE_NO]"
        info:String           :- Any extra info to store for the particular page in JSON string
        
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def edit_page_info(pairedDeviceId, pageNum, pageName=None, info=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        pageName:String       :- The name for the page. Default to "Page [PAGE_NO]"
        pageNum:Number        :- The index of the page
        info:String           :- Any extra info to store for the particular page in JSON string
        
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def remove_key(pairedDeviceId, pageNum, keyId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def remove_page(pairedDeviceId, pageNum, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def set_keys_info(pairedDeviceId, pageNum, keysData, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def record_key(pairedDeviceId, pageNum, keyId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def cancel_record_key(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def send_key(pairedDeviceId, pageNum, keyId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get capabilities of the virtual RC.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg-  {"success":true}
        '''
        pass

    @staticmethod
    def edit_remote_info(pairedDeviceId, info=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Edit the extra info for the remote.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        info:String           :- Any extra info to store in JSON string
        
        return:Dictionary :eg-  {"success":true}
        '''
        pass

