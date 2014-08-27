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
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo


class BLEService():

    ''' Bluetooth Low Energy Service '''
    
    @staticmethod
    def disconnect(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Disconnect to a BLE compliance device.
        
        address:String - mac address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def list_services(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List all services supported by the device.
        address:String - mac address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def set_security_level(address, level, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set security level of the device.
        address:String - mac address.
        level:String - security level eg:high,medium, or low.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def list_characteristics(address, handleStart, handleEnd, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List characteristics of the device.
        address:String - mac address.
        handleStart:String - starting memory address in hex string.(GATTTOOL Commands argument)
        handleEnd:String - ending memory address in hex string.(GATTTOOL Commands argument)
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def char_read_by_handle(address, handle, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Read characteristic value by handle.
        address:String - mac address.
        handle:String - handle in hex string.(GATTTOOL Commands argument)
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def char_read_by_type(address, uuid, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Read characteristic value by uuid.
        address:String - mac address.
        uuid:String - UUID in string.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def char_write_request(address, handle, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Write request to characteristic with response.
        address:String - mac address.
        handle:String - handle in hex string.(GATTTOOL Commands argument)
        value:String - value to write.(GATTTOOL Commands argument)
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
        
    @staticmethod
    def char_write_command(address, handle,value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send command to characteristic (No response).
        address:String - mac address.
        handle:String - hanle in hex string.(GATTTOOL Commands argument)
        value:String - value to write.(GATTTOOL Commands argument)
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass