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

class SetupService():

    @staticmethod
    def set_temperature_unit(temperatureUnit=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set temperature unit to celcius, kelvin, fahrenheit.
        return:Dictionary :eg- {"response":{}}
        '''
        pass
    
    @staticmethod
    def get_temperature_unit(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get temperature unit from setup.
        return:Dictionary :eg- {"temperatureUnit":"celcius"}
        '''
        pass