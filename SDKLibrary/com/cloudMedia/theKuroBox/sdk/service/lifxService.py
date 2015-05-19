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

class LifxService():
    
    @staticmethod
    def get_light_info(host, port, mac, site, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the light info.
        @param host:String               - IP of the light
        @param port:int                  - Port of the call
        @param mac:String                - MAC address of the light WITHOUT ":" or "-"
        @param site:String               - MAC address of the master device WITHOUT ":" or "-"

        @return:
        A dictionary with following information:
        1. color:dict                    - Dictionary with the following information:
                                                a. h:int       - The hue value
                                                b. s:double    - The saturation value
                                                c. b:double    - The brightness value
                                                d. k:int       - The kelvin value
        2. deviceLabel:String            - The device label
        3. mac:String                    - The MAC Address
        4. success:boolean               - Whether the call is success
        '''
        pass

    @staticmethod    
    def set_light_color_hue(host, port, mac, site, hue, saturation, brightness, kelvin=3500, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Set HSBK value for the light
        @param host:String               - IP of the light
        @param port:int                  - Port of the call
        @param mac:String                - MAC address of the light WITHOUT ":" or "-"
        @param site:String               - MAC address of the master device WITHOUT ":" or "-"
        @param hue:Number                - The hue value [0 - 360]
        @param saturation:Number         - The saturation value [0 - 1]
        @param brightness:Number         - The brightness value [0 - 1]
        @param kelvin:Number             - The kelvin value [2500 -9000]

        @return:
        A dictionary with the same format as get_light_info
        '''
        pass

    @staticmethod
    def get_light_power_state(host, port, mac, site, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the light power state.
        @param host:String               - IP of the light
        @param port:int                  - Port of the call
        @param mac:String                - MAC address of the light WITHOUT ":" or "-"
        @param site:String               - MAC address of the master device WITHOUT ":" or "-"

        @return:
        A dictionary with following information:
        1. powerState:boolean            - True : On, False : Off
        3. success:boolean               - Whether the call is success
        '''
        pass

    @staticmethod
    def set_light_power_state(host, port, mac, site, state=True, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the light power state.
        @param host:String               - IP of the light
        @param port:int                  - Port of the call
        @param mac:String                - MAC address of the light WITHOUT ":" or "-"
        @param site:String               - MAC address of the master device WITHOUT ":" or "-"
        @param state:Boolean             - Whether to turn on / off the power. True [default] - On, False - Off

        @return:
        A dictionary with following information:
        1. powerState:boolean            - True : On, False : Off
        3. success:boolean               - Whether the call is success
        '''
        pass

