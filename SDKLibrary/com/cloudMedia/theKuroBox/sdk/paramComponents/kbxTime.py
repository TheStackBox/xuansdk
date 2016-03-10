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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxTime import KBXTime as KBXTimeSDK
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class KBXTime(KBXTimeSDK, KBXParamComponent):

    COM_NAME = "kbxTime"

    PROP_KBX_PARAM_SHOW_SECOND_FIELD = "kbxParamShowSecondField"
    PROP_KBX_PARAM_TIME_FORMAT = "kbxParamTimeFormat"

    TIME_FORMAT_12 = "12"
    TIME_FORMAT_24 = "24"

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamShowSecondField=False, kbxParamTimeFormat=TIME_FORMAT_12,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        pass

    def set_kbx_param_default_value(self, value):
        pass

    def set_kbx_param_show_second_field(self, value):
        pass

    def set_kbx_param_time_format(self, value):
        pass

    def get_kbx_param_show_second_field(self):
        pass

    def get_kbx_param_time_format(self):
        pass

    def cast(self, value):
        pass

