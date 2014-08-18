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


class StorageManagerService():
    
    @staticmethod    
    def set_data(group, key, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set data to persistent storage
        group:String :- group of the data.
        key:String :- the id of the data.
        value:String :- the value of the data
        return:Dictionary :eg- {"lastRowId": 1}
        '''
        pass

    @staticmethod
    def get_data(group=None, key="", limit=50, offset=0, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get persistent storage data
        group:String :- the group of data.
        key:String :- the id of the data.
        limit:Number :- limit of data to get
        offset:Number :- offset of data to get
        return:Dictionary :eg- {"totalRecord": 1, "data": [{"appId": 2222222, "id": 1, "appDataKey": "1", "appDataGroup": "99", "appDataValue": "test"}]}
        '''
        pass
        
    @staticmethod    
    def del_data(group=None, key="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        permanent delete persistent storage key and data
        group:String :- the group of data.
        key:String :- the id of the data.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
        