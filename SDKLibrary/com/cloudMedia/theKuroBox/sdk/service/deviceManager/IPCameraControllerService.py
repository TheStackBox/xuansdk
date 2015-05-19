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

class IPCameraControllerService(object):

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
    def get_camera_stream_configuration(pairedDeviceId, isRemoteAccess=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get Camera Stream Configuration
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"streamConfiguration":{}}
        '''
        pass

    @staticmethod
    def set_snapshot(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Snapshot
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"snapshot":{}}
        '''
        pass

    @staticmethod
    def get_snapshot_list(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get Snapshot List
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"snapshotList":[]}
        '''
        pass

    @staticmethod
    def get_preset_angle_list(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get preset angle list
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"presetList":[]}
        '''
        pass

    @staticmethod
    def set_preset_angle(pairedDeviceId, presetName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Preset Angle
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        presetName:String :- Preset name
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_night_mode(pairedDeviceId, mode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Night Mode
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        mode:Number :- 0 to off and 1 to on
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_zoom_in(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Zoom in
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_zoom_out(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Zoom out
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_camera_move(pairedDeviceId, moveTo, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera move
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        moveTo:String :- move to 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_update_login(pairedDeviceId, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set update login
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        username:String :- new username
        password:String :- new password 
        return:Dictionary :eg- {"success":true}
        '''
        pass

