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


class FTDIService():

    @staticmethod
    def init_ftdi(deviceId, cmdStr="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Initialize ftdi command to device.
        deviceId:Number :- target device id
        cmdStr:String :- command string write to ftdi device
        '''
        pass
    
    @staticmethod
    def write_to_ftdi(deviceId, cmdStr="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Write ftdi command to device.
        deviceId:Number :- target device id
        cmdStr:String :- command string write to ftdi device
        '''
        pass
    
    @staticmethod
    def read_from_ftdi(deviceId, till, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Write ftdi command to device perform read.
        deviceId:Number :- target device id
        till:String :- read until
        '''
        pass
    