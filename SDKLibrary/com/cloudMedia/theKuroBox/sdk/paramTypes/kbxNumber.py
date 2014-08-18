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
import sys

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper


class KBXNumberType(KBXParamType):

    TYPE_NAME = "kbxNumber"

    PROP_KBX_PARAM_DECIMAL = "kbxParamDecimal"
    PROP_KBX_PARAM_MIN_VALUE = "kbxParamMinValue"
    PROP_KBX_PARAM_MAX_VALUE = "kbxParamMaxValue"

    def set_kbx_param_decimal(self, value):
        '''
        Set if this parameter allows decimal point.

        Params:
        value:Boolean - [Required] True if decimal point is allowed and vice versa.
        '''
        pass
    
    def set_kbx_param_min_value(self, value):
        '''
        Set the lower boundary for the value of this parameter.

        Params:
        value:Integer - [Required] Lower boundary of the value.
        '''
        pass

    def set_kbx_param_max_value(self, value):
        '''
        Set the upper boundary for the value of this parameter.

        Params:
        value:Integer - [Required] Upper boundary of the value.
        '''
        pass

    def get_kbx_param_decimal(self):
        '''
        Check if this parameter allows decimal point.

        Params:
        A boolean where True if decimal point is allowed and vice versa.
        '''
        pass

    def get_kbx_param_min_value(self):
        '''
        Get value of lower boundary.

        Returns:
        Value of lower boundary.
        '''
        pass

    def get_kbx_param_max_value(self):
        '''
        Get value of upper boundary.

        Returns:
        Value of upper boundary.
        '''
        pass
    
class KBXNumber(KBXNumberType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamDecimal=0, kbxParamMinValue=-(sys.maxsize), kbxParamMaxValue=sys.maxsize, **kbxParamProps):
        '''
        Parameter that accepts only number value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMinValue:Integer - [Optional] Lower boundary for the value of this parameter
        kbxParamMaxValue:Integer - [Optional] Upper boundary for the value of this parameter.
        kbxParamDecimal:Number - [Optional] Number of decimal points allowed. False by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
