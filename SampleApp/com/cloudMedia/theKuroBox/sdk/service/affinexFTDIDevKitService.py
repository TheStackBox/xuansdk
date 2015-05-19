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

class AffinexFTDIDevKitService():

    @staticmethod
    def get_dip_sw_id_option(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get dip sw id option list.
        return:Dictionary :eg- {"option":["01"]}
        '''
        pass

    @staticmethod 
    def get_output_no_option(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get output number option list.
        return:Dictionary :eg- {"option":[0, 1, 2, 3, 4]}
        '''
        pass

    @staticmethod
    def turn_on_led(deviceId, dipSwId, outputNo, status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on LED.
        deviceId:Number - target device id
        dipSwId:String - DIP SW ID. 00
        outputNo:Number - Output No. 0-4
        status:Boolean - True=Turn On, False=Turn Off
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def input_press(deviceId, dipSwId, outputNo, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Input press.
        deviceId:Number - target device id
        dipSwId:String - DIP SW ID. 00
        outputNo:Number - Output No. 0-4
        return:Dictionary :eg- {"success":true}
        '''
        pass

