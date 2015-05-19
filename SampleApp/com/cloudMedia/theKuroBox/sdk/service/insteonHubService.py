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

class InsteonHubService():
    
    @staticmethod
    def set_hub_scan(timeout=15, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Do network scan to discover the Insteon hub.
        timeout:Number :- scanning timeout.
        langauge:String :- language to use for the api.
        '''
        pass

    @staticmethod
    def set_hub_local_scan(timeout=240, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Do network scan (local) to discover the Insteon hub.
        timeout:Number :- scanning timeout.
        langauge:String :- language to use for the api.
        '''
        pass

    @staticmethod
    def get_authentication(username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the authentication token.
        username:String :- Hub's username 
        password:String :- Hub's password
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"token": "ABC123456789"}
        '''
        pass

    @staticmethod
    def get_IM_info(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the Insteon hub's information.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"ip":"198.0.0.1", "port":25105, "firmware":"9C", "deviceId":"26.2E.9B"}
        '''
        pass

    @staticmethod
    def set_scan_device_stop(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set scan Insteon's devices stopped.
        language:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_device_scan(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set scan Insteon's devices before list_device is called.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_enter_allink_mode(ip, port, token, group, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set enter allink mode
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        group:String :- Initial group for allink mode 
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_cancel_allink_mode(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set cancel allink mode
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def list_device(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the list after set_device_scan is called.
        return:Dictionary :eg- {"devices":[{"deviceId":"11.11.11", "category":"SwitchController"}]}
        '''
        pass

    @staticmethod
    def get_product_data(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set scan Insteon's devices before list_device is called.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_on(ip, port, token, deviceId, level=255, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set on Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        level:Integer :- the initial dim level for the device.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_fast_on(ip, port, token, deviceId, level=255, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set fast on Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        level:Integer :- the initial dim level for the device.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_off(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set off Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_fast_off(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set fast off Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_bright(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set bright one step Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def set_dim(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set dim one step Insteon's devices.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def ping(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Ping the Insteon's device to get the response from the target device.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod   
    def get_status_request(ip, port, token, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get the Insteon's device status.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1, "level":58}
        '''
        pass

    @staticmethod
    def send_command(ip, port, token, cmd, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send Insteon command.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        cmd:String :- Insteon Command.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def get_buffer_status(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get Insteon hub's buffer.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"buffer":000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
        '''
        pass

    @staticmethod
    def clear_buffer_status(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Clear Insteon hub's buffer.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod
    def get_first_all_link_record(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get first Insteon Hub all link record.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_next_all_link_record(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get next Insteon Hub all link record.
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod  
    def set_start_all_link_mode(ip, port, token, group, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Insteon hub enter all link mode
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        group:String :- Insteon device group Id
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod 
    def set_stop_all_link_mode(ip, port, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop Insteon hub all link mode
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod 
    def set_delete_all_link_mode(ip, port, token, group, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Insteon hub to delete all link mode
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        group:String :- Insteon device group Id
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

    @staticmethod 
    def delete_all_link_record(ip, port, token, group, deviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove Insteon Hub's record
        ip:String :- Hub's ip 
        port:String :- Hub's port
        token:String :- Authentication token
        group:String :- Insteon device group Id
        deviceId:String :- the target device's Id return from list_device api.
        langauge:String :- language to use for the api.
        return:Dictionary :eg- {"status":1}
        '''
        pass

