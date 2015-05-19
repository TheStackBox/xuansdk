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

class TinyFinderService(object):
    '''
    Service class for Tiny Finder.
    '''
    
        
    @staticmethod
    def get_battery_level(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get battery level
        address:String :- MAC address of the Tiny Finder.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"TINY_FINDER_BATTERY"}
        '''
        pass

    @staticmethod
    def get_link_loss_value(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get link loss value
        address:String :- MAC address of the Tiny Finder.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "eventTag":"TINY_FINDER_BATTERY"}
        '''
        pass

    @staticmethod
    def get_signal_strength(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get signal strength value
        address:String :- MAC address of the Tiny Finder.
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true, "rssi":-67, "distance":1.2042}
        '''
        pass

    @staticmethod
    def alert(address, alertLevel=2, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send alert request to Tiny Finder.
        address:String :- MAC address of the Tiny Finder.
        alertLevel:Integer :- Alert level. Validation [0-2]
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def set_link_loss_value(address, alertLevel, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set link loss value of Tiny Finder.
        address:String :- MAC address of the Tiny Finder.
        alertLevel:Integer :- Link loss alert level. Validation [0-2]
        language:String - Preferred language of return texts.
        return:Dictionary :eg- {"success":true}
        '''
        pass

