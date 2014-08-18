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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObjectType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType


class KBXMetricType(KBXObjectType):
    '''
    Base class for all quantitative KBXParams with units.
    Do not instantiate this class directly.
    '''

    TYPE_NAME = "kbxMetric"

    PROP_KBX_PARAM_UNITS = "kbxParamUnits"

    PROP_KBX_PARAM_OBJ_KEY_VALUE = "value"
    PROP_KBX_PARAM_OBJ_KEY_UNIT = "unit"

    def set_kbx_param_units(self, value):
        '''
        Set list of units allowed for this metric type.
        
        Params:
        value:List - [Required] List of string (duplicate is not allowed) indicates unit symbol allowed for received value.
        '''
        pass

    def get_kbx_param_units(self):
        '''
        Get list of units allowed for this metric type.
        
        Returns:
        List of string.
        '''
        pass

    class DTO(dict):

        @staticmethod
        def build(unit, value):
            '''
            Build the dictionary/value for KBXMetric instance.
            
            Params:
            unit:String - [Required]
            value:Number - [Required]
            
            Returns:
            Instance of KBXMetricType.DTO.
            '''
            pass

        def set_unit(self, value):
            '''
            Explicitly set the unit.
            
            Params
            value:String - [Required]
            '''
            pass
        
        def set_value(self, value):
            '''
            Explicitly set the value.
            
            Params:
            value:Number - [Required]
            '''
            pass

        def get_unit(self):
            '''
            Get the unit.
            
            Returns:
            Unit in string.
            '''
            pass

        def get_value(self):
            '''
            Get the value.
            
            Returns:
            Value in number.
            '''
            pass