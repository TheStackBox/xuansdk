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

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObjectType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class KBXHSBColorType(KBXObjectType):

    TYPE_NAME = "kbxHSBColor"

    PROP_KBX_PARAM_OBJ_KEY_HUE = "h"
    PROP_KBX_PARAM_OBJ_KEY_SATURATION = "s"
    PROP_KBX_PARAM_OBJ_KEY_BRIGHTNESS = "b"

    def __init__(self, kbxParamIsRequired=True):
        pass

    def cast(self, value):
        pass

    class DTO(dict):

        @staticmethod
        def build(h, s, b):
            pass

        def set_hue(self, value):
            pass

        def set_saturation(self, value):
            pass

        def set_brightness(self, value):
            pass

        def get_hue(self):
            pass

        def get_saturation(self):
            pass

        def get_brightness(self):
            pass

class KBXHSBColor(KBXHSBColorType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        pass

