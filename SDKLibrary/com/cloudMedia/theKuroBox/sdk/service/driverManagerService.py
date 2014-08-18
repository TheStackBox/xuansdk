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


class DriverManagerService(object):
    '''
    Service to call to system application manager
    '''
    
    @staticmethod
    def list_connected_driver(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get a list of connected drivers
        Return:Dictionary :eg-
        {"drivers":
            {
                "dust":
                {
                    "driver":"dust",
                },
                "bluetooth":
                {
                    "driver":"bluetooth"
                }
            }
        }
        '''
        pass
    
    @staticmethod
    def get_is_driver_connected(driverId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Check whether a driver is connected
        Return:Dictionary :eg-
        {"connected":true, "driver":{ "driver":"dust" }}
        '''
        pass
    