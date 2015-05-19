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

import json

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParam import KBXParam
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class KBXParamComponent(KBXParam):
    '''
    Base class that serve as an interface and should not be instantiated directly.
    '''
    #===========================================================================
    # Common properties by all KBXParamType
    #===========================================================================
    PROP_KBX_PARAM_COM = "kbxParamCom"
    PROP_KBX_PARAM_LABEL = "kbxParamLabel"
    PROP_KBX_PARAM_DESC = "kbxParamDesc"
    PROP_KBX_PARAM_DEFAULT_VALUE = "kbxParamDefaultValue"

    def __init__(self, reservedProps=[]):
        pass

    def set_kbx_param_label(self, value):
        pass

    def set_kbx_param_desc(self, value):
        pass

    def set_kbx_param_default_value(self, value):
        pass

    def get_kbx_param_com(self):
        '''
        Get the corresponding KBXParam type name.

        Returns:
        A string of the name of this KBXParam type.
        '''
        pass

    def get_kbx_param_label(self):
        pass

    def get_kbx_param_desc(self):
        pass

    def get_kbx_param_default_value(self):
        pass

