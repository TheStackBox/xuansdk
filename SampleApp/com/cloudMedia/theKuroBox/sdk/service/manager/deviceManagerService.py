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

class DeviceManagerService():
    @staticmethod
    def set_paired_devices_scan(protocolId=None, pairedDeviceId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set update paired devices status start.
        protocolId:Number :- return from API get_supported_protocol_list
        pairedDeviceId:Number :- return from API get_paired_device_list.
        return:Dictionary :eg- {"success": "true"}
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
    def get_supported_event_tag_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get supported event tag required by protocol.
        protocolId:Number :- return from API get_supported_protocol_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_scan(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set scan device start.
        protocolId:Number :- return from API get_supported_protocol_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"success": "true"}
        '''
        pass

    @staticmethod
    def set_device_scan_stop(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Set scan device stop.
        protocolId:Number :- return from API get_supported_protocol_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"success": "true"}
        '''
        pass

    @staticmethod
    def get_device_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get device list.
        protocolId:Number :- return from API get_supported_protocol_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"device": [{"protocolId": "1", "name": "A(Bxxxxx-xxxxxxx-xxxxxx-xxxxxxxx)", "id": 0, "path": "uuid:Bxxxxxxx-xxxxxxxx-xxxxxxxxx-xxxxxxx"}]}
        '''
        pass

    @staticmethod
    def get_device_exist(protocolId, unique, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device exist.
        protocolId:Number :- return from API get_supported_protocol_list
        unique:String :- unique string set in deviceDTO. Device Manager will convert it to upper case.  
        return:Dictionary :eg- {"exist": true}
        '''
        pass

    @staticmethod
    def set_device_pair(protocolId, deviceId=None, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Pair device.
        protocolId:Number :- return from API get_supported_protocol_list
        deviceId:Number :- return from API get_device_list
        pairInfo:String :- Extra pair device info
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"success": "true"}
        '''
        pass

    @staticmethod
    def get_paired_device_list(offset, limit, protocolId=None, deviceTypeId=None, enable=None, locationId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get paired device list.
        offset:Number :- offset to get paired device list
        limit:Number :- total data return. Max 50 item
        locationId:Number :- target location for the data return
        return:Dictionary :eg- {"devices": [{"statusUnit": "", "protocolId": 1, "enable": 1, "status": "", "controlPanel": 1, "advanceControlPanel": 1,
                                             "id": 1, "description": "UPNP Speaker", "protocol": null, "deviceTypeId": 7, "deviceType": null, "icon": "&#xe62d",
                                             "name": "XW-SMA1 217F45", "groupId": 0}], "totalItem": 1}
        '''
        pass

    @staticmethod
    def get_paired_device_count(protocolId=None, deviceTypeId=None, enable=None, language=AppInfo.DEFAULT_API_LANGUAGE):
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
    def call_device_controller_method(pairedDeviceId, methodName, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Call device controller method.
        pairedDeviceId:Number :- return from API get_paired_device_list.
        methodName:String :- method name in device controller to be call.
        **param :- any parameter required by that specific device controller.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_unpair(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Unpair device.
        pairedDeviceId:Number :- return from API get_paired_device_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"success": "true"}
        '''
        pass

    @staticmethod
    def get_device_enable_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get the device enable status
        pairedDeviceId:Number :- return from API get_paired_device_list
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"success": "true"}
        '''
        pass

    @staticmethod
    def set_group_unpair(protocolId, groupId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Abort unpair device.
        pairedDeviceId:Number :- return from API get_paired_device_list
        **param :- any parameter required by that specific protocol.
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
    def get_paired_device_info_by_protocol_unique_id(protocolId, uniqueId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get paired device info.
        protocolId:String :- protocol id
        uniqueId:String :- unique id insert when pairing
        return:Dictionary :eg- {"deviceInfo": {"statusUnit": "", "protocolId": 1, "enable": 1, "status": "", "groupId": 0,
                                               "advanceControlPanel": 1, "id": 2, "description": "UPNP Speaker", "protocol": {"name": "UPNP", "icon": "&#xe61c", "id": 1, "protocolType": "autoScan"},
                                               "deviceTypeId": 7, "deviceType": {"controlPanel": "true", "name": "Speaker", "advanceControlPanel": "true", "icon": "&#xe62d", "id": 7}, "icon": "&#xe62d",
                                               "name": "XW-SMA1 217F45", "controlPanel": 1}}
        '''
        pass

    @staticmethod
    def set_paired_device_info(pairedDeviceId=None, name=None, description=None, typeId=None, groupId=None, icon=None, status=None, statusUnit=None, extraInfo=None, deviceData=None, locationId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
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
        extraInfo:String :- extra info, normally store pairing information
        deviceData:String :- device data
        locationId:Number :- location Id
        return:Dictionary :eg- {"deviceInfo": {"data": [{"name": "my speaker", "uniqueId": "UUID:5F9EC1B3-ED59-79FF-4530-745E1C217F45", "groupId": 0, "icon": "speaker icon",
                                                         "protocolId": 1, "extraInfo": "{\"path\": \"uuid:5F9EC1B3-ED59-79FF-4530-745E1C217F45\", \"protocolId\": \"1\", \"id\": 22,
                                                         \"name\": \"XW-SMA1 217F45\"}", "description": "my living room speaker", "controlPanelExist": 1, "deviceData": "null",
                                                         "modifyTime": "2014-06-09 07:13:55.257150", "statusUnit": "", "typeId": 7, "status": "No song", "enable": 1, "createTime": "2014-06-09 07:08:05",
                                                         "id": 1, "advanceControlPanelExist": 1}], "success": "true"}}
        '''
        pass

    @staticmethod
    def get_device_type_list(protocolId, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Get available device type.
        protocolId:Number :- return from API get_supported_protocol_list
        offset:Number :- offset to get paired device list
        limit:Number :- total data return. Max 50 item
        **param :- any parameter required by that specific protocol.
        return:Dictionary :eg- {"types": [{"controlPanel": "true", "name": "Speaker", "advanceControlPanel": "true", "icon": "&#xe62d", "id": 7}]}
        '''
        pass

    @staticmethod
    def get_advanced_control_list(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get advanced controller methods.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"controllerModule": "device_manager.speaker_controller"}
        '''
        pass

    @staticmethod
    def set_paired_device_status(pairedDeviceId, enabled, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Manually set the device status to up/down.
        pairedDeviceId:Number :- return from API get_paired_device_list
        return:Dictionary :eg- {"success": true}
        '''
        pass

