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

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParam import KBXParam
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

class KBXParamType(KBXParam):
    '''
    Base class that serve as an interface and should not be instantiated directly.
    '''
    #===========================================================================
    # Common properties by all KBXParamType
    #===========================================================================
    PROP_KBX_PARAM_TYPE = "kbxParamType"
    PROP_KBX_PARAM_IS_REQUIRED = "kbxParamIsRequired"

    def __init__(self, reservedProps=[]):
        pass

    def set_kbx_param_is_required(self, value):
        '''
        Set if a value for this parameter is required.

        Params:
        value:Boolean - [Required] True if a value for this parameter is required.
        '''
        pass

    def get_kbx_param_type(self):
        '''
        Get the corresponding KBXParam type name.

        Returns:
        A string of the name of this KBXParam type.
        '''
        pass

    def get_kbx_param_is_required(self):
        '''
        Check if this parameter is required.

        Returns:
        A boolean value indicates if this parameter is required.
        '''
        pass

    def cast(self, value):
        '''
        Cast any given value if it matches the criteria of the descriptor of this parameter.

        Params:
        value - [Required] Any value for validation.

        Returns:
        The validated value (can be vary from the input value). Format is vary according to the validation implementation of the KBXParam instance.
        '''
        pass

