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
from com.cloudMedia.theKuroBox.sdk.dto.deviceControllerDTO import DeviceControllerDTO

class AdvDeviceControllerManagerService():

    @staticmethod
    def get_advance_device_controller_details(appId, uniqueId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get advance device controller details.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_advance_device_controller_details_by_id(advanceDeviceControllerId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get advance device controller details.
        advanceDeviceControllerId:String :- Advance Device Controller ID
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def init_device_with_advanced_controller(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Initial advance device controller.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def init_device_with_advanced_controller_by_id(advanceDeviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Initial advance device controller by advance device controller id.
        advanceDeviceControllerId:String :- Advance Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def remove_device_with_advanced_controller(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove device from advance controller.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def remove_device_with_advanced_controller_by_id(advanceDeviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove device from advance controller by advance device controller id.
        advanceDeviceControllerId:String :- Advance Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_status_with_advanced_controller(appId, uniqueId, pairedDeviceId, deviceDTO, enable, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set device status to advance controller.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_status_with_advanced_controller_by_id(advanceDeviceControllerId, pairedDeviceId, deviceDTO, enable, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set device status to advance controller by advance device controller id.
        advanceDeviceControllerId:String :- Advance Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_advanced_control_list(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get advance control method list.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_advanced_control_list_by_id(advanceDeviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get advance control method list by device controller id.
        advanceDeviceControllerId:String :- Advance Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

