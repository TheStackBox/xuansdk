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

class DeviceControllerManagerService():

    @staticmethod
    def get_device_controller_list(appId=None, protocolId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device controller details.
        appId:Number :- [optional] Application id of the application created this controller
        protocolId:String :- [optional]protocol id
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_device_controller_details(appId, uniqueId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device controller details.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_device_controller_details_by_id(deviceControllerId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device controller details.
        deviceControllerId:String :- Device Controller ID
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_init_with_device_controller(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device initial with device controller.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_init_with_device_controller_by_id(deviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device initial with device controller by device controller id.
        deviceControllerId:String :- Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_remove_from_device_controller(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device remove from device controller.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_remove_from_device_controller_by_id(deviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device remove from device controller by device controller id.
        deviceControllerId:String :- Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_status(appId, uniqueId, pairedDeviceId, deviceDTO, enable, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device status.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def set_device_status_by_id(deviceControllerId, pairedDeviceId, deviceDTO, enable, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device status by device controller id.
        deviceControllerId:String :- Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        enable:Boolean :- device status enable or disable.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def update_device_info(appId, uniqueId, pairedDeviceId, deviceDTO, enable, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device status.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def update_device_info_by_id(deviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set paired device status by device controller id.
        deviceControllerId:String :- Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def call_device_controller_method(appId, uniqueId, methodName, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Call device controller method.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        methodName:String :- method name register in this controller
        **param:Object :- parameter for the method
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def call_device_controller_method_by_id(deviceControllerId, methodName, language=AppInfo.DEFAULT_API_LANGUAGE, **param):
        '''
        Call device controller method.
        deviceControllerId:String :- Device Controller ID
        methodName:String :- method name register in this controller
        **param:Object :- parameter for the method
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def request_device_status_update(appId, uniqueId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Request device update.
        appId:Number :- Application id of the application created this controller
        uniqueId:String :- uniqueId use by the Application created this controller
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def request_device_status_update_by_id(deviceControllerId, pairedDeviceId, deviceDTO, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Request device update by device controller id.
        deviceControllerId:String :- Device Controller ID
        pairedDeviceId:String :- device id from device manager after device been paired.
        deviceDTO:Object :- device object from device manager after device been paired.
        return:Dictionary :eg- {}
        '''
        pass

