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

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumberType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class KBXTimeType(KBXNumberType):

    TYPE_NAME = "kbxTime"

    def __init__(self, kbxParamIsRequired=True):
        pass

    def cast(self, value):
        pass

    class DTO(int):

        @staticmethod
        def build(value):
            pass

        def get_date_time_obj(self):
            pass

        def get_second(self):
            pass

        def get_minute(self):
            pass

        def get_hour(self):
            pass

class KBXTime(KBXTimeType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        pass

