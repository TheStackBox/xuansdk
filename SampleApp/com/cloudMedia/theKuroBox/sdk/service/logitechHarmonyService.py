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

class LogitechHarmonyService():

    @staticmethod
    def discovery(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Discovery Harmony Hub.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_all_activities(hubIpAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get all activities.
        hubIpAddress:String - ip address
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def get_current_activity(hubIpAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get current activity.
        hubIpAddress:String - ip address
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def start_activity(hubIpAddress, activityId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Start activity.
        hubIpAddress:String - ip address
        activityId:String - activity id to start
        return:Dictionary :eg- {}
        '''
        pass

