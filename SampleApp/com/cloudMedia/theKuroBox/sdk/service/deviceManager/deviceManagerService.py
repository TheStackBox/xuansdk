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


class DeviceManagerService():
    @staticmethod
    def set_paired_devices_scan(deviceId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set update paired devices status start.
        return:Dictionary :eg- {"success": ""true""}
        '''
        pass
    
    
    @staticmethod
    def get_supported_protocol_list(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get supported protocol list.
        return:Dictionary :eg- {"protocols": [{"name": "UPNP", "icon": "&#xe61c", "id": 1, "protocolType": "autoScan"}]}
        '''
        pass
    
    
    @staticmethod
    def set_device_scan(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set scan device start.
        protocolId:Number :- return from API get_supported_protocol_list
        return:Dictionary :eg- {"success": ""true""}
        '''
        pass
    
    
    @staticmethod
    def set_device_scan_stop(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set scan device stop.
        protocolId:Number :- return from API get_supported_protocol_list
        return:Dictionary :eg- {"success": ""true""}
        '''
        pass
    
    
    @staticmethod
    def get_device_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device list.
        protocolId:Number :- return from API get_supported_protocol_list
        return:Dictionary :eg- {"device": [{"protocolId": "1", "name": "A(Bxxxxx-xxxxxxx-xxxxxx-xxxxxxxx)", "id": 0, "path": "uuid:Bxxxxxxx-xxxxxxxx-xxxxxxxxx-xxxxxxx"}]}
        '''
        pass
    
    
    @staticmethod
    def set_device_pair(protocolId, deviceId, pairInfo, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pair device.
        protocolId:Number :- return from API get_supported_protocol_list
        deviceId:Number :- return from API get_device_list
        pairInfo:String :- Extra pair device info
        return:Dictionary :eg- {"success": ""true""}
        '''
        pass
    
    
    @staticmethod
    def set_device_pair_abort(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Abort pair device.
        protocolId:Number :- return from API get_supported_protocol_list
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    
    @staticmethod
    def get_paired_device_list(offset, limit, protocolId=None, deviceTypeId=None, enable=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get paired device list.
        offset:Number :- offset to get paired device list
        limit:Number :- total data return. Max 50 item
        return:Dictionary :eg- {"devices": [{"statusUnit": "", "protocolId": 1, "enable": 1, "status": "", "controlPanel": 1, "advanceControlPanel": 1,
                                             "id": 1, "description": "UPNP Speaker", "protocol": null, "deviceTypeId": 7, "deviceType": null, "icon": "&#xe62d",
                                             "name": "XW-SMA1 217F45", "groupId": 0}], "totalItem": 1}
        '''
        pass
    

    @staticmethod
    def set_device_unpair(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Unpair device.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    

    @staticmethod
    def set_device_unpair_abort(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Abort unpair device.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    

    @staticmethod
    def get_paired_device_info(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get paired device info.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"deviceInfo": {"statusUnit": "", "protocolId": 1, "enable": 1, "status": "", "groupId": 0,
                                               "advanceControlPanel": 1, "id": 2, "description": "UPNP Speaker", "protocol": {"name": "UPNP", "icon": "&#xe61c", "id": 1, "protocolType": "autoScan"},
                                               "deviceTypeId": 7, "deviceType": {"controlPanel": "true", "name": "Speaker", "advanceControlPanel": "true", "icon": "&#xe62d", "id": 7}, "icon": "&#xe62d",
                                               "name": "XW-SMA1 217F45", "controlPanel": 1}}
        '''
        pass
    

    @staticmethod
    def set_paired_device_info(pairedDeviceId, name, description, typeId, groupId, icon, status, statusUnit, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device info.
        pairedDeviceId:Number :- return from API get_paired_device_list
        name:String :- name
        description:String :- description
        typeId:Number :- return from API get_device_type_list
        groupId:Number :- currently set to 0
        icon:String :- icon
        status:String :- device status
        statusUnit:String :- unit of status
        return:Dictionary :eg- {"deviceInfo": {"data": [{"name": "my speaker", "uniqueId": "UUID:5F9EC1B3-ED59-79FF-4530-745E1C217F45", "groupId": 0, "icon": "speaker icon",
                                                         "protocolId": 1, "extraInfo": "{\"path\": \"uuid:5F9EC1B3-ED59-79FF-4530-745E1C217F45\", \"protocolId\": \"1\", \"id\": 22,
                                                         \"name\": \"XW-SMA1 217F45\"}", "description": "my living room speaker", "controlPanelExist": 1, "deviceData": "null",
                                                         "modifyTime": "2014-06-09 07:13:55.257150", "statusUnit": "", "typeId": 7, "status": "No song", "enable": 1, "createTime": "2014-06-09 07:08:05",
                                                         "id": 1, "advanceControlPanelExist": 1}], "success": "true"}}
        '''
        pass
    

    @staticmethod
    def get_device_type_list(protocolId, offset, limit, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get available device type.
        protocolId:Number :- return from API get_supported_protocol_list
        offset:Number :- offset to get paired device list
        limit:Number :- total data return. Max 50 item
        return:Dictionary :eg- {"types": [{"controlPanel": "true", "name": "Speaker", "advanceControlPanel": "true", "icon": "&#xe62d", "id": 7}]}
        '''
        pass
    

    @staticmethod
    def get_device_control_module(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get paired device control module.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"controllerModule": "device_manager.speaker_controller"}
        '''
        pass
    
