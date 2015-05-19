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

class GoogleNestService():

    @staticmethod
    def nest_authenticate(code, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Nest authenticate.
        code:String - code
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def nest_set_token(token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Nest set token.
        token:String - token
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def nest_get_token(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Nest get token.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def nest_get_data(path, token, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Nest get data.
        path:String - path
        token:String - token
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def nest_update_data(path, token, data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Nest update data.
        path:String - path
        token:String - token
        data:String - data
        return:Dictionary :eg- {}
        '''
        pass

