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

from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class KBXTextInput(KBXString, KBXParamComponent):

    COM_NAME = "kbxTextInput"

    PROP_KBX_PARAM_PLACEHOLDER = "kbxParamPlaceholder"
    PROP_KBX_PARAM_SUGGESTIONS = "kbxParamSuggestions"
    PROP_KBX_PARAM_INPUT_TYPE = "kbxParamInputType"

    INPUT_NUMBER = "number"
    INPUT_TEXT = "text"
    INPUT_PASSWORD = "password"
    INPUT_EMAIL = "email"

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, kbxParamPlaceholder=None,
                 kbxParamSuggestions=None, kbxParamInputType=INPUT_TEXT, **kbxParamProps):
        pass

    def set_kbx_param_default_value(self, value):
        pass

    def set_kbx_param_placeholder(self, value):
        pass

    def set_kbx_param_suggestions(self, value):
        pass

    def set_kbx_param_input_type(self, value):
        pass

    def get_kbx_param_placeholder(self):
        pass

    def get_kbx_param_suggestions(self):
        pass

    def get_kbx_param_input_type(self):
        pass

