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


class KBXParamWrapper(KBXParam):
    
    '''
    Wrapper class for KBXParams.
    It wraps KBXParamTypes with identifiable name.
    '''
    
    PROP_KBX_PARAM_NAME = "kbxParamName"

    def set_kbx_param_name(self, value):
        '''
        Set the name of this parameter.

        Params:
        value:String - [Required] Name of this parameter.
        '''
        pass 
    
    def get_kbx_param_name(self):
        '''
        Get the name of this parameter.

        Returns:
        Name of this parameter as string.
        '''
        pass