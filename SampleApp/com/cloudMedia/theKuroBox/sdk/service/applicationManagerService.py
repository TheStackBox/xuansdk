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
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo


class ApplicationManagerService(object):
    '''
    Service to call to system application manager
    '''
    
    @staticmethod
    def list_current_running_app(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get a list of running app
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-
        {"apps":
            {
                "2000300":
                {
                    "id":"2000300",
                    "name":"Automation",
                    "app_ver":"19999122",
                    "type":"|ui|daemon|",
                    "status":"running",
                    "statusId":1
                },
                "2000400":
                {
                    "status":"initializing",
                    "statusId":0
                },
                "2000800":
                {
                    "id":"2000300",
                    "name":"Automation",
                    
                    "app_ver":"19999122",
                    "type":"|ui|daemon|",
                    "status":"restarting",
                    "statusId":3
                }
            }
        }
        '''
        pass
    
    @staticmethod
    def get_app_running_status(appId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get running status of an app
        appId:String - the application Id.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-
        {
            "appId":"2000300",
            "status":"running",
            "statusId":1
        }
        '''
        pass
    
    @staticmethod
    def get_system_running_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get running status of an app
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-
        {
            "status":"running",
            "statusId":1
        }
        '''
        pass
        