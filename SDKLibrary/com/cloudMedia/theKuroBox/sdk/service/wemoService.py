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


class WemoService():
    
    @staticmethod
    def discover_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Discover wemo devices on the network
        return:Dictionary :eg- {"devices": [{"usn": "uuid:Insight-1_0-221351K120023F::upnp:rootdevice", "port": "49153", 
                                            "type": "Insight", "location": "http://192.168.0.76:49153/setup.xml", 
                                            "ip": "192.168.0.76"}]}
        '''
        pass
    
    
    @staticmethod
    def set_insight_on(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on WeMo Insight Switch
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    
    @staticmethod
    def set_insight_off(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off WeMo Insight Switch
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    
    @staticmethod
    def get_insight_state(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the state of WeMo Insight Switch
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        return:Dictionary :eg- {"InsightState": "ON"}
        '''
        pass
    
    
    @staticmethod
    def get_insight_friendly_name(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get friendly name of the WeMo Insight Switch
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        return:Dictionary :eg- {"friendlyName": "Wemo Insight"}
        '''
        pass
    
     
    @staticmethod
    def set_insight_friendly_name(hostname, newDeviceName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new friendly name for the WeMo Insight Switch
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        newDeviceName:String :- New friendly name for the WeMo Insight Switch
        return:Dictionary :eg- {"newFriendlyName": "WeMo Insight"}
        '''
        pass
    
     
    @staticmethod
    def get_insight_parameter(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve WeMo Insight extra informations such as 
        hostname:String :- The IP Address and Port number of Insight Switch scanned from discover_devices()
        return:Dictionary :eg- {"insightParams": {"wattsUsedNow": "0", "energyUsedTotal": "0.000000", 
                                                  "lastTurnOn": "2014-06-03 06:24:34", "energyUsedToday": "0"}}
        '''
        pass
    
    
    @staticmethod
    def set_switch_on(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on WeMo Switch
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    
    @staticmethod
    def set_switch_off(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off WeMo Switch
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    
    @staticmethod
    def get_switch_state(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current WeMo Switch state
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        return:Dictionary :eg- {"switchState": "OFF"}
        '''
        pass
    
    
    @staticmethod
    def get_switch_friendly_name(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve the current friendly name for the WeMo Switch
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        return:Dictionary :eg- {"switchFriendlyName": "My Switch"}
        '''
        pass
    
    
    @staticmethod
    def set_switch_friendly_name(hostname, newDeviceName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Assign a new friendly name for the Wemo Switch
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        newDeviceName:String :- New friendly name of Wemo Switch
        return:Dictionary :eg- {"newSwitchFriendlyName": "Wemo Switch"}
        '''
        pass
    
    
    @staticmethod
    def get_switch_information(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve Wemo Switch informations
        hostname:String :- The IP Address and Port number of WeMo Switch scanned from discover_devices()
        return:Dictionary :eg- {"switchInformation": "08863BC2D1A4|WeMo_US_2.00.4494.PVT|1|49153|0|Wemo Switch"}
        '''
        pass
    
    
    @staticmethod
    def get_device_information(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve Wemo Insight/Wemo Switch/Wemo Motion information
        hostname:String :- The IP Address and Port number of WeMo Motion scanned from discover_devices()
        return:Dictionary :eg- {"deviceInformation": "08863BC2D1A4|WeMo_US_2.00.4494.PVT|1|49153|0|My Switch"}
        '''
        pass
    
    
    @staticmethod
    def get_motion_state(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve Wemo Motion current state
        hostname:String :- The IP Address and Port number of WeMo Motion scanned from discover_devices()
        return:Dictionary :eg- {"motionState": "Motion Detected"}
        '''
        pass
    
    
    @staticmethod
    def get_motion_friendly_name(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current friendly name of Wemo Motion
        hostname:String :- The IP Address and Port number of WeMo Motion scanned from discover_devices()
        return:Dictionary :eg- {"motionFriendlyName": "Wemo Motion"}
        '''
        pass
    
    
    @staticmethod
    def set_motion_friendly_name(hostname, newDeviceName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Assign a new friendly name to a Wemo Motion
        newDeviceName:String :- New friendly name for Wemo Motion
        hostname:String :- The IP Address and Port number of WeMo Motion scanned from discover_devices()
        return:Dictionary :eg- {"newMotionFriendlyName": "my Wemo Motion"}
        '''
        pass
    
    
    @staticmethod
    def get_motion_information(hostname, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current Wemo Motion information
        hostname:String :- The IP Address and Port number of WeMo Motion scanned from discover_devices()
        return:Dictionary :eg- {"motionInformation": "EC1A5968002C|WeMo_US_2.00.4494.PVT|1|49153|0|Wemo Motion"}
        '''
        pass
    
    
    