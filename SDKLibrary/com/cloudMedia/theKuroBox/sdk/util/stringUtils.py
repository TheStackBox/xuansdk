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

class StringUtils(object):

    @staticmethod
    def to_string(obj):
        '''Cast to String'''
        pass

    @staticmethod
    def is_string(obj):
        '''
        Check whether obj is a str object
        '''
        pass

    @staticmethod
    def append_if_missing(oriString, stringToAppend):
        '''
        Append stringToAppend to the back of oriString if stringToAppend is not found at the back of oriString
        oriString:String       - The string to check
        stringToAppend:String  - The string to append if missing
        
        return:String          - The final string after append (if necessary) 
        '''
        pass

    @staticmethod
    def prepend_if_missing(oriString, stringToPrepend):
        '''
        Prepend stringToPrepend to the front of oriString if stringToPrepend is not found at the front of oriString
        oriString:String        - The string to check
        stringToPrepend:String  - The string to prepend if missing
        
        return:String           - The final string after prepend (if necessary) 
        '''
        pass

