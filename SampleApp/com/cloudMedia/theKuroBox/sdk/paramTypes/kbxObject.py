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
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class KBXObjectType(KBXParamType):

    TYPE_NAME = "kbxObject"

    PROP_KBX_PARAM_OBJ_PROPS = "kbxParamObjProps"
    PROP_KBX_PARAM_STRICT = "kbxParamStrict"

    def __init__(self, kbxParamIsRequired=True,
                 kbxParamObjProps=None, kbxParamStrict=False):
        pass

    def set_kbx_param_obj_props(self, value):
        pass

    def set_kbx_param_obj_prop(self, propName, propType=None):
        pass

    def unset_kbx_param_obj_prop(self, propName):
        pass

    def set_kbx_param_strict(self, value):
        pass

    def get_kbx_param_obj_props(self):
        pass

    def get_kbx_param_strict(self):
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

    class DTO(dict):

        @staticmethod
        def build(**kwargs):
            pass

class KBXObject(KBXObjectType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamObjProps=None, kbxParamStrict=False, **kbxParamProps):
        pass

