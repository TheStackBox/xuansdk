##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParam import KBXParam

class KBXParamType(KBXParam):
    '''
    Generic class for KBXParams which defines common characteristics.
    '''
    
    PROP_KBX_PARAM_TYPE = "kbxParamType"
    PROP_KBX_PARAM_IS_REQUIRED = "kbxParamIsRequired"

    def set_kbx_param_is_required(self, value):
        '''
        Set if a value for this parameter is required.

        Params:
        value:Boolean - [Required] True if a value for this parameter is required.
        '''
        pass

    def get_kbx_param_type(self):
        '''
        Get the corresponding KBXParam type name. You are not allowed to set this value explicitly.

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