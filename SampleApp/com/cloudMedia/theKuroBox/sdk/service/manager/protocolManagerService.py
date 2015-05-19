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

class ProtocolManagerService():

    @staticmethod
    def get_supported_protocol_list(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get supported protocol list.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_supported_event_tag_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get supported event tag list.
        protocolId:String - protocol id return from get_supported_protocol_list
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_protocol_details(appId, name, uniqueType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get protocol details.
        appId:Number :- Application id of the application created this protocol
        name:String - name of the protocol
        uniqueType:String - unique type of the protocol
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_protocol_details_by_id(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get protocol details by protocol id.
        protocolId:String - protocol id return from get_supported_protocol_list
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def update_paired_devices_status(protocolId, deviceList, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Update paired devices status.
        protocolId:String - protocol id return from get_supported_protocol_list
        deviceList:Object - {"devices":[], "totalItem":0}
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_scan_start(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set device scan start.
        protocolId:String - protocol id return from get_supported_protocol_list
        rescan:Boolean - [optional] clear cache and start new scanning.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_scan_stop(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set device scan stop.
        protocolId:String - protocol id return from get_supported_protocol_list
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_device_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get device list.
        protocolId:String - protocol id return from get_supported_protocol_list
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_pair(protocolId, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set device pair.
        protocolId:String - protocol id return from get_supported_protocol_list
        deviceId:Number - id return from get_device_list
        pairInfo:String - extra info require when pairing
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_unpair(pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set device unpair.
        pairedDeviceId:String - paired device id
        deviceDTO:Object - Device DTO object
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_device_enable_status(pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device enable status.
        pairedDeviceId:String - paired device id
        deviceDTO:Object - Device DTO object
        return:Dictionary :eg- {}
        '''
        pass

