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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObject
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util

class KBXDateTimeRange(KBXObject, KBXParamComponent):

    COM_NAME = "kbxDateTimeRange"
    
    PROP_KBX_PARAM_OBJ_KEY_START_DATE_TIME = "startDateTime"
    PROP_KBX_PARAM_OBJ_KEY_END_DATE_TIME = "endDateTime"

    def __init__(self, kbxParamName, kbxParamIsRequired=True,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        pass

    def set_kbx_param_default_value(self, value):
        pass

    def cast(self, value):
        pass

    class DTO(dict):

        @staticmethod
        def build(startDateTime, endDateTime):
            pass

        def set_start_date_time(self, value):
            pass

        def set_end_date_time(self, value):
            pass

        def get_start_date_time(self):
            pass

        def get_end_date_time(self):
            pass

