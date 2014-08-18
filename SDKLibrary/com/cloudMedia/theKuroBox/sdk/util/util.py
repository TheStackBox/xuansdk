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
import importlib
import re

class Util(object):

    @staticmethod
    def is_empty(data=""):
        '''
        Return True if argument is an empty string or is None
        '''
        pass
        
    @staticmethod
    def is_email(email=""):
        '''
        Return True if argument is an valid email format
        '''
        pass
            
    @staticmethod
    def is_in_range(indexInt, fromInt, toInt):
        '''
        Return True if indexInt is in range from fromInt to toInt.
        '''
        pass
    
    @staticmethod
    def is_min_max_value(minValue, maxValue):
        '''
        Return True if maxValue is more than minValue.
        '''
        pass
    
    @staticmethod
    def is_str_in_length(string, minLength, maxLength):
        '''
        Return True if string length is in range from minLength to maxLength.
        '''
        pass
    
    @staticmethod
    def get_class(name):
        '''
        Return class object specified by name.
        The name should be in format of: [package].[package]......[filename].[class name]
        '''
        pass