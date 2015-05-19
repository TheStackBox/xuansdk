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

from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util

class KBXHidden(KBXString, KBXParamComponent):

    COM_NAME = "kbxHidden"

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Parameter which is not visible to end-user.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamDefaultValue - [Required] Default value of this parameter, it can be in any data type as long as it can be converted into json string.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_default_value(self, value):
        '''
        Set default value for this parameter.

        Params:
        value - Any value as long as it can be converted into json string.
        '''
        pass

