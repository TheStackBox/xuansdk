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


class BLEService():

    ''' Bluetooth Low Energy Service '''
    
    @staticmethod
    def disconnect(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Connect to a BLE compliance device.
        
        Params:
        address:String - [Required] Device MAC address.
        
        Returns:
        {"success":True}
        '''
        pass
        
    @staticmethod
    def list_services(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List all services supported by the device.
        
        Params:
        address:String - [Required] Device MAC address.
        
        Returns:
        {"success":True}
        
        Event:
        BLE_SERVICES
        '''
        pass
        
    @staticmethod
    def set_security_level(address, level, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set security level of the device.
        
        Params:
        address:String - [Required] Device MAC address.
        level:String - [Required] high", "medium", or "low".

        Returns:
        {"success":True}
        '''
        pass
        
    @staticmethod
    def list_characteristics(address, handleStart, handleEnd, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List characteristics of the device.
        
        Params:
        address:String - [Required] Device MAC address.
        handleStart:String - [Required] 
        
        Returns:
        {"success":True}
        '''
        pass
        
    @staticmethod
    def char_read_by_handle(address,handle, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
        
    @staticmethod
    def char_read_by_type(address,uuid, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
        
    @staticmethod
    def char_write_request(address,handle,value, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
        
    @staticmethod
    def char_write_command(address,handle,value, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass