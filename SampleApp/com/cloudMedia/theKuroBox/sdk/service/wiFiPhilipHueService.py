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


class WiFiPhilipHueService():
    
    @staticmethod
    def nupnp(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Discover bridge IP Address and ID
        return:Dictionary :eg- {"bridgeIP": [{"internalipaddress": "192.xxx.xxx.xxx", "id": "xxxxxxxxxx"}]}
        '''
        pass
    
    
    @staticmethod
    def authorize(bridgeIP, deviceType, username, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Authorize user.
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        devicetype:String :- device type
        username:String :- username set when authorize 
        return:Dictionary :eg- {"Authorzation": [{"error": {"type": 101, "address": "", "description": "link button not pressed"}}]}
        '''
        pass
    
    
    @staticmethod
    def get_all_lights(bridgeIP, username, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get all lights
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        return:Dictionary :eg- {"1": {"name": "My Hue"}, "2": {"name": "lamp2"}}
        '''
        pass
    
    
    @staticmethod
    def search_new_lights(bridgeIP, username, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Search new light
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        return:Dictionary :eg- {"New Lights": [{"success": {"lights": "Searching for new devices"}}]}
        '''
        pass
    
    
    @staticmethod
    def get_new_lights(bridgeIP, username, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get new lights
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        return:Dictionary :eg- {"lastscan": "2014-06-12T05:50:01"}
        '''
        pass
    
    
    @staticmethod
    def get_light_attributes_and_state(bridgeIP, username, lightId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get light attributes and state
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        lightId:String :- light id return from get_all_lights or get_new_lights
        return:Dictionary :eg- {"state": {"hue": 14922, "xy": [0.45950000000000002, 0.41049999999999998], "alert": "none", "bri": 254, "ct": 369, "sat": 144, 
                                          "colormode": "ct", "reachable": true, "on": true, "effect": "none"}, "name": "My light", 
                                          "pointsymbol": {"8": "none", "1": "none", "2": "none", "3": "none", "4": "none", "5": "none", "6": "none", "7": "none"}, 
                                          "modelid": "LCT001", "swversion": "66009663", "type": "Extended color light"}
        '''
        pass
    
    
    @staticmethod
    def rename_light(bridgeIP, username, lightId, newName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Rename light
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        lightId:String :- light id return from get_all_lights or get_new_lights
        newName:String :- new name for light
        return:Dictionary :eg- {"New Hue Name": [{"success": {"lights1name": "My Hue"}}]}
        '''
        pass
    
    
    @staticmethod
    def set_light_state(bridgeIP, username, lightId, on=None, brightness=None, hue=None, saturation=None, xCoordColor=None, yCoordColor=None, colorTemperature=None, alert=None, effect=None, transitionTime=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set light state
        bridgeIP:String :- ip address. Eg: 192.168.xxx.xxx
        username:String :- username set when authorize
        lightId:String :- light id return from get_all_lights or get_new_lights
        on:Boolean :- [Optional] On/Off state of the light.true=Turn on, false=Turn off 
        brightness:Number :- [Optional] the brightness value to set the light to.Brightness is a scale from 0 (the minimum the light is capable of) to 255 (the maximum). Note: a brightness of 0 is not off.
        hue:Number :- [Optional] the hue value to set light to. Value between 0 and 65535. Both 0 and 65535 are red, 25500 is green and 46920 is blue.
        saturation:Number :- [Optional] saturation of the light. 255 is the most saturated (colored) and 0 is the least saturated (white)
        xCoordColor:Number :- [Optional] this value must set together with yCoordColor. The x coordinates of a color in CIE color space. Must be between 0 and 1. If the specified coordinates are not in the CIE color space, the closest color to the coordinates will be chosen.
        yCoordColor:Number :- [Optional] this value must set together with xCoordColor. The y coordinates of a color in CIE color space. Must be between 0 and 1. If the specified coordinates are not in the CIE color space, the closest color to the coordinates will be chosen.
        colorTemperature:Number :- [Optional] The Mired Color temperature of the light. 2012 connected lights are capable of 153 (6500K) to 500 (2000K).
        alert:String :- [Optional] the alert effect, is a temporary change to the bulb's state, and has one of the following values:none=The light is not performing an alert effect.select=The light is performing one breathe cycle.lselect=The light is performing breathe cycles for 30 seconds or until an alert or none command is received.
        effect:String :- [Optional] the dynamic effect of the light. Other values will generate an error of type 7.none=no effect,colorloop=setting the effect to colorloop will cycle through all hues using the current brightness and saturation settings.
        transitionTime:Number :- [Optional] the duration of the transition from the light's current state to the new state. This is given as a multiple of 100ms and defaults to 4 (400ms). 
        return:Dictionary :eg- {"Light State": [{"success": {"/lights/1/state/transitiontime": 4}}, {"success": {"/lights/1/state/on": true}}, {"success": {"/lights/1/state/hue": 25500}}, 
                                                {"success": {"/lights/1/state/sat": 255}}, {"success": {"/lights/1/state/ct": 250}}, {"success": {"/lights/1/state/xy": [0.0, 1.0]}}, 
                                                {"success": {"/lights/1/state/bri": 100}}, {"success": {"/lights/1/state/alert": "select"}}, {"success": {"/lights/1/state/effect": "colorloop"}}]}
        '''
        pass
    
    
