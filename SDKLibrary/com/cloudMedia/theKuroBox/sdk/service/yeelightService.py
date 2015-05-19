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

class YeelightService(object):
    '''
    Service class for Yeelight Blue
    '''
    
    
    @staticmethod
    def enable_notification(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Enable notification of Yeelight Blue.
        address:String :- MAC address of Yeelight Blue.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light_on(address, lightness=100, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on light
        address:String :- MAC address of Yeelight Blue.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light_off(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off light
        address:String :- MAC address of Yeelight Blue.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light_lightness(address, lightness, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Adjust brightness of the light
        address:String :- MAC address of Yeelight Blue.
        lightness:Number :- Light brightness value. Range 0-100.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light_color(address, red, green, blue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Change color of the light
        address:String :- MAC address of Yeelight Blue.
        red:Number :- Light's red value. Range 0-255
        green:Number :- Light's green value. Range 0-255
        blue:Number :- Light's blue value. Range 0-255
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light(address, red, green, blue, lightness, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Change color of the light
        address:String :- MAC address of Yeelight Blue.
        red:Number :- Light's red value. Range 0-255
        green:Number :- Light's green value. Range 0-255
        blue:Number :- Light's blue value. Range 0-255
        lightness:Number :- Light brightness value. Range 0-100.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_turn_on_after_delay(address, time, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set auto turn on light after a specified duration
        address:String :- MAC address of Yeelight Blue.
        time:Number :- Duration in minutes. Minimum value = 1
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_turn_off_after_delay(address, time, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set auto turn off light after a specified duration
        address:String :- MAC address of Yeelight Blue.
        time:Number :- Duration in minutes. Minimum value = 1
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def cancel_delay_settings(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set auto turn off light after a specified duration
        address:String :- MAC address of Yeelight Blue.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_light_effect(address, lightMode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set auto turn off light after a specified duration
        address:String :- MAC address of Yeelight Blue.
        lightMode:String :- TS: Color gradual mode, color will change smoothly during a change in color, TE: Color non gradual mode, color will immediately change when a change is called,DF: Current color will be set as the default color when powered up
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def get_light_status(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set auto turn off light after a specified duration
        address:String :- MAC address of Yeelight Blue.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "status":{"R":255, "G":255, "B":255, "L":100, "CF":0, "DL":0}}
        '''
        pass

