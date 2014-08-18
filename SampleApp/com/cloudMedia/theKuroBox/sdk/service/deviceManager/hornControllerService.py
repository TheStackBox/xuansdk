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


class HornControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        return SharedMethod.call(kbxMethodAppId=SharedMethod.get_system_id(),
                                 kbxMethodName="get_capabilities",
                                 kbxModuleName="device_manager.horn_controller",
                                 pyapi=SharedMethod.get_pyapi(),
                                 pairedDeviceId=pairedDeviceId,
                                 **{AppInfo.REQUEST_KEY_LANGUAGE:language})

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        return SharedMethod.call(kbxMethodAppId=SharedMethod.get_system_id(),
                                 kbxMethodName="get_status",
                                 kbxModuleName="device_manager.horn_controller",
                                 pyapi=SharedMethod.get_pyapi(),
                                 pairedDeviceId=pairedDeviceId,
                                 **{AppInfo.REQUEST_KEY_LANGUAGE:language})

    @staticmethod
    def set_on(pairedDeviceId, timeout, language=AppInfo.DEFAULT_API_LANGUAGE):
        return SharedMethod.call(kbxMethodAppId=SharedMethod.get_system_id(),
                                 kbxMethodName="set_on",
                                 kbxModuleName="device_manager.horn_controller",
                                 pyapi=SharedMethod.get_pyapi(),
                                 pairedDeviceId=pairedDeviceId,
                                 timeout=timeout,
                                 **{AppInfo.REQUEST_KEY_LANGUAGE:language})

    @staticmethod
    def set_off(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        return SharedMethod.call(kbxMethodAppId=SharedMethod.get_system_id(),
                                 kbxMethodName="set_off",
                                 kbxModuleName="device_manager.horn_controller",
                                 pyapi=SharedMethod.get_pyapi(),
                                 pairedDeviceId=pairedDeviceId,
                                 **{AppInfo.REQUEST_KEY_LANGUAGE:language})
