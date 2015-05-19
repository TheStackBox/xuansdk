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

class BLEService(object):
    '''
    Service class to deal with Bluetooth Low Energy technology.
    '''
    DEVICE_TINY_FINDER = "BLEDevice.TinyFinder"
    DEVICE_YEELIGHT_BLUE = "BLEDevice.YeelightBlue"
    DEVICE_UNSUPPORTED = "BLEDevice.Unsupported"
    

    @staticmethod
    def connect(address, connectTimeout=5, autoDisconnect=70, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Connect to a BLE compliance device.
        ** Device will be connected automatically when any of the functions from below is invoked.
        address:String - Device MAC address.
        connectTimeout:Integer - Max delay for device to respond. Unit in seconds. Validation [5-15]
        autoDisconnect:Integer - Automatically disconnect after delay in seconds. 0 always stay connected. Validation [0-420]
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def disconnect(address, disconnectTimeout=5, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Disconnect to a BLE compliance device.
        address:String - Device MAC address.
        disconnectTimeout:Integer - Max delay for device to respond. Unit in seconds. Validation [5-15]
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_security_level(address,level, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set security level of the device.
        address:String - Device MAC address.
        level:String - Security level. Allowed values: ["high", "medium", "low"].
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def list_services(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List all services supported by the device.
        address:String - Device MAC address.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"BLE_SERVICES"}
        '''
        pass

    @staticmethod
    def list_characteristics(address,handleStart,handleEnd, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List characteristics of the device.
        address:String - Device MAC address.
        handleStart:String - Starting memory address in hex string.(GATTTOOL Commands argument)
        handleEnd:String - Ending memory address in hex string.(GATTTOOL Commands argument)
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"BLE_CHARACTERISTICS"}
        '''
        pass

    @staticmethod
    def char_read_by_handle(address,handle, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Read characteristic value by handle.
        address:String - Device MAC address.
        handle:String - Handle in hex string.(GATTTOOL Commands argument)
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"BLE_READ_HANDLE_RESPONSE"}
        '''
        pass

    @staticmethod
    def char_read_by_type(address, uuid, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Read characteristic value by uuid.
        address:String - Device MAC address.
        uuid:String - UUID in string.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"BLE_READ_TYPE_RESPONSE"}
        '''
        pass

    @staticmethod
    def char_write_request(address, handle, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Write request to characteristic with response.
        address:String - Device MAC address.
        handle:String - Handle in hex string.(GATTTOOL Commands argument)
        value:String - Value to write.(GATTTOOL Commands argument)
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"BLE_WRITE_REQUEST_RESPONSE"}
        '''
        pass

    @staticmethod
    def char_write_command(address, handle, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send command to characteristic (No response).
        address:String - Device MAC address.
        handle:String - Handle in hex string.(GATTTOOL Commands argument)
        value:String - Value to write.(GATTTOOL Commands argument)
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def get_ble_device_type(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Check if the device is supported by system.
        address:String - Device MAC address.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "data":"BLEDevice.YeelightBlue"}
        '''
        pass

    @staticmethod
    def is_device_alive(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get alive status of a BLE device.
        address:String - Device MAC address.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "data":true}
        '''
        pass

