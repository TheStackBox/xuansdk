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


class X10Service():
    
    @staticmethod
    def on(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on x10 device
        address:String :- Address of the X10 device eg. a1
        return:Dictionary :eg- {"response": {}, "returnValue": 100, "returnMessage": "Ok"},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    
    
    @staticmethod    
    def off(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off x10 device
        address:String :- Address of the X10 device eg. a1
        return:Dictionary :eg- {"response": {}, "returnValue": 100, "returnMessage": "Ok"},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    
    
    @staticmethod    
    def on_horn(address, modelId, timeout, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on horn
        address:String :- Address of the X10 device eg. a1
        modelId: PH508, SH10A, PSH01, PSH02
        return:Dictionary :eg- {"response": {}, "returnValue": 100, "returnMessage": "Ok"}
        '''
        pass
    
    
    @staticmethod    
    def off_horn(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn off horn
        address:String :- Address of the X10 device eg. a1
        return:Dictionary :eg- {"response": {}, "returnValue": 100, "returnMessage": "Ok"}
        '''
        pass
    
    
    @staticmethod    
    def dim(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Dim lamp
        address:String :- Address of the X10 device eg. a1
        return:Dictionary :eg- {"response":{"returnMessage": "Ok", "returnValue": 100, "response": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    
    
    @staticmethod    
    def bright(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Brighten lamp
        address:String :- Address of the X10 device eg. a1
        return:Dictionary :eg- {"returnMessage": "Ok", "returnValue": 100, "response": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    
     
    @staticmethod    
    def scanning(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Scan for motion detection
        return:Dictionary :eg- {'model_id': 'MS10A', 'event': 'Scanning', 'address': '01:00:00', 'model_name': 'P. I. R. Motion Detector'}, 
                                'eventTag': 'X10_SCANNING_EVENT', 'parameter': {}}
        '''
        pass
    
    
    @staticmethod    
    def set_brightness_level(address, level, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set brightness level
        address: device address
        level: 0-10
        return:Dictionary :eg- {"returnMessage": "Ok", "returnValue": 100, "response": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    
    
    @staticmethod    
    def get_driver_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get driver status
        return:Dictionary :eg- {}
        '''
        pass
    
    