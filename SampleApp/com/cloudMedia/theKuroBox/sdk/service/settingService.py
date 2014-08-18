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


class SettingService():

    @staticmethod
    def scan_network_device(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Scan network device.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def list_network_device(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List network device.
        return:Dictionary :eg- {"response":{"devices": [{"mac": "00:06:dc:85:05:60", "ip": "192.168.0.102"}, {"mac": "38:e7:d8:ee:42:50", "ip": "192.168.0.95"}, 
                                                         {"mac": "88:32:9b:72:73:11", "ip": "192.168.0.63"}, {"mac": "00:24:e8:16:d1:e4", "ip": "192.168.0.32"}, 
                                                         {"mac": "00:12:3f:80:d8:00", "ip": "192.168.0.26"}, {"mac": "00:26:b9:c3:87:2c", "ip": "192.168.0.93"}]}}
        '''
        pass
