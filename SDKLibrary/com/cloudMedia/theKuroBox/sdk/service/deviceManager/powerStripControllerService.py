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


class PowerStripControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device capabilities.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device status.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    

    @staticmethod
    def set_on(pairedDeviceId, index, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on switch.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        index:String - index return from get_capabilities
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    

    @staticmethod
    def set_off(pairedDeviceId, index, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number - Paired Device ID return from DeviceManagerService.get_paired_device_list
        index:String - index return from get_capabilities
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
