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

from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util

class KBXBooleanType(KBXParamType):

    TYPE_NAME = "kbxBoolean"

    PROP_KBX_PARAM_TRUE_VALUE = "kbxParamTrueValue"
    PROP_KBX_PARAM_FALSE_VALUE = "kbxParamFalseValue"

    def __init__(self, kbxParamIsRequired=True, kbxParamTrueValue=True, kbxParamFalseValue=False):
        '''
        Parameter that accepts only Boolean value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamTrueValue - [Optional] Value to be used as True. True by default.
        kbxParamFalseValue - [Optional] Value to be used as False. False by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_param_true_value(self, value):
        '''
        Set the value for True.

        Params:
        value - [Required] Value for True. (Must be able to be parsed into JSON string)
        '''
        pass

    def set_kbx_param_false_value(self, value):
        '''
        Set the value for False.

        Params:
        value - [Required] Value for False. (Must be able to be parsed into JSON string)
        '''
        pass

    def get_kbx_param_true_value(self):
        '''
        Get the value for True.

        Returns:
        Value for True.
        '''
        pass

    def get_kbx_param_false_value(self):
        '''
        Get the value for False.

        Returns:
        Value for False.
        '''
        pass

    def cast(self, value):
        '''
        Cast given input against the properties of this parameter.

        Params:
        value - [Required] Can be any data type. Validation works by stringify the value and check if it's "true" or "false", or value in True/False label, or 1 or 0 after converted into integer.

        Returns:
        True value or False value or None.
        '''
        pass

class KBXBoolean(KBXBooleanType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True,
             kbxParamTrueValue=True, kbxParamFalseValue=False, **kbxParamProps):
        pass

