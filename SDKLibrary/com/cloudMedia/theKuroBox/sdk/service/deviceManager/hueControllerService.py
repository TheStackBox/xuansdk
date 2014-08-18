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


class HueControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    

    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    

    @staticmethod
    def set_on(pairedDeviceId, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_off(pairedDeviceId, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_brightness(pairedDeviceId, brightness, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        brightness :Number :- the brightness value to set the light to.
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_hue(pairedDeviceId, hue, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        hue:Number :- the hue value to set light to.
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_saturation(pairedDeviceId, saturation, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        saturation:Number :- saturation of the light.
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_color_rgb(pairedDeviceId, r, g, b, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        r:Number :- r value [0-255]
        g:Number :- g value [0-255]
        b:Number :- b value [0-255]
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def set_color_temperature(pairedDeviceId, ct, transitionTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off switch.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        ct:Number :- The Mired Color temperature of the light.
        transitionTime:Number :- Optional. the duration of the transition from the light's current state to the new state.
        '''
        pass
    

    @staticmethod
    def get_hue_state(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get hue state
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    
