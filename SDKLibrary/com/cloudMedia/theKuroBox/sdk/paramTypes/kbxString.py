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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper


class KBXStringType(KBXParamType):

    TYPE_NAME = "kbxString"

    PROP_KBX_PARAM_MIN_LENGTH = "kbxParamMinLength"
    PROP_KBX_PARAM_MAX_LENGTH = "kbxParamMaxLength"

    def set_kbx_param_min_length(self, value):
        '''
        Set the minimum required length of the value of this parameter.

        Params:
        value:Integer - [Required] Value of the minimum length of the value of this parameter is required.
        '''
        pass

    def set_kbx_param_max_length(self, value):
        '''
        Set the maximum allowed length of the value of this parameter.

        Params:
        value:Integer - [Required] Value of the maximum length of the value of this parameter is allowed
        '''
        pass

    def get_kbx_param_min_length(self):
        '''
        Get minimum required length.

        Returns:
        Value of the minimum required length.
        '''
        pass

    def get_kbx_param_max_length(self):
        '''
        Get maximum allowed length.

        Returns:
        Value of the maximum allowed length.
        '''
        pass
    
class KBXString(KBXStringType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None, **kbxParamProps):
        '''
        Parameter that accepts only string value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMinLength:Integer - [Optional] Minimum length of the value of this parameter is required.
        kbxParamMaxLength:Integer - [Optional] Maximum length of the value of this parameter is allowed.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
