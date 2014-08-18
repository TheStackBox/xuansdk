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
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumberType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator


class KBXRangeType(KBXNumberType):

    TYPE_NAME = "kbxRange"

    PROP_KBX_PARAM_STEP = "kbxParamStep"

    def set_kbx_param_step(self, value):
        '''
        Set the step of the movement of the value

        Params:
        value:Integer - [Required] Value to indicates the step of the movement of the value.
        '''
        pass
        
    def get_kbx_param_step(self):
        '''
        Get the step of the movement of the value.

        Returns:
        Value that indicates the step of the movement of the value.
        '''
        pass

class KBXRange(KBXRangeType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamMinValue, kbxParamMaxValue, kbxParamIsRequired=True,
                 kbxParamDecimal=0, kbxParamStep=1, **kbxParamProps):
        '''
        Parameter that accepts only number value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamMinValue:Integer - [Required] Lower boundary for the value of this parameter
        kbxParamMaxValue:Integer - [Required] Upper boundary for the value of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamDecimal:Boolean - [Optional] True if decimal point is allowed and vice versa. False by default.
        kbxParamStep:Integer - [Optional] A value to indicates the step of the movement of the value.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
