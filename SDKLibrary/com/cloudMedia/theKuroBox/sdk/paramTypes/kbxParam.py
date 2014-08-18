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
class KBXParam(object):
    '''
    Base class for all KBXParams, do not instantiate it directly.
    '''
    
    ''' Error code used by KBXParams '''
    ERR_INVALID_DATA_TYPE = 1501
    ERR_INVALID_TIMESTAMP = 1502
    ERR_INVALID_VALUE = 1503
    ERR_INVALID_VALUE_RANGE = 1504
    ERR_INVALID_VALUE_LENGTH = 1505
    ERR_INVALID_OBJECT_SIZE = 1506
    ERR_INVALID_STRING_FORMAT = 1507
    ERR_INVALID_STRING_CHARACTER = 1508
    ERR_INDEX_OUT_OF_BOUND = 1509
    ERR_INDEX_DUPLICATED = 1510
    ERR_FIELD_REQUIRED = 1511
    ERR_OPERATION_FAILED = 1512

    def set_property(self, prop, value):
        '''
        Define a new property.

        Params:
        prop:String - [Required] Key of the property.
        value - [Required] Can be any data type as long as it can be convert into json string.
        '''
        pass

    def get_property(self, prop):
        '''
        Get value of custom property.

        Params:
        prop:String - [Required] Key of the property.

        Returns:
        Value of the property.
        '''
        pass

    def get_properties(self):
        '''
        Retrieve properties of this parameter descriptor.

        Returns:
        A dictionary contains of the properties of this parameter.
        '''
        pass

    def has_property(self, prop):
        '''
        Check if a particular property key exists.

        Params:
        prop:String - [Required] Key to check.

        Returns:
        True if exists and vice versa.
        '''
        pass
