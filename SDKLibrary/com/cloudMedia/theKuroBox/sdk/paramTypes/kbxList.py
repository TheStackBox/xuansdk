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

import sys

from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBooleanType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxDateTime import KBXDateTimeType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumberType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXStringType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxTime import KBXTimeType
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator

class KBXListType(KBXParamType):

    TYPE_NAME = "kbxList"

    PROP_KBX_PARAM_TYPE_INFERENCE = "kbxParamTypeInference"
    PROP_KBX_PARAM_MAX_SIZE = "kbxParamMaxSize"
    PROP_KBX_PARAM_MIN_SIZE = "kbxParamMinSize"
    PROP_KBX_PARAM_DUPLICATE = "kbxParamDuplicate"

    def __init__(self, kbxParamIsRequired=True,
                 kbxParamTypeInference=None, kbxParamMaxSize=None, kbxParamMinSize=1, kbxParamDuplicate=True):
        pass

    def set_kbx_param_type_inference(self, value):
        pass

    def set_kbx_param_min_size(self, value):
        pass

    def set_kbx_param_max_size(self, value):
        pass

    def set_kbx_param_duplicate(self, value):
        pass

    def get_kbx_param_type_inference(self):
        pass

    def get_kbx_param_min_size(self):
        pass

    def get_kbx_param_max_size(self):
        pass

    def get_kbx_param_duplicate(self):
        pass

    def cast(self, value):
        pass

    class KBXDict(dict): 
        def __init__(self):
            pass

        def cast(self, value):
            pass

    class KBXNumber(KBXDict):
        
        def __init__(self, kbxParamIsRequired=True, kbxParamDecimal=0, kbxParamMinValue=-(sys.maxsize), kbxParamMaxValue=sys.maxsize):
            pass

        def cast(self, value):
            pass

    class KBXString(KBXDict):

        def __init__(self, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None):
            pass

        def cast(self, value):
            pass

    class KBXBoolean(KBXDict):

        def __init__(self, kbxParamIsRequired=True):
            pass

        def cast(self, value):
            pass

    class KBXDateTime(KBXDict):
        
        def __init__(self, kbxParamIsRequired=True):
            pass

        def cast(self, value):
            pass

    class KBXTime(KBXDict):
        
        def __init__(self, kbxParamIsRequired=True):
            pass

        def cast(self, value):
            pass

class KBXList(KBXListType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamTypeInference=None, kbxParamMaxSize=None, kbxParamMinSize=1, kbxParamDuplicate=True, **kbxParamProps):
        pass

