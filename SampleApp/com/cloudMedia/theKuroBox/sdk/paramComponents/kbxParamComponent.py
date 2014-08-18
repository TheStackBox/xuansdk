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
import json

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParam import KBXParam


class KBXParamComponent(KBXParam):
    '''
    Wrapper that adds display information to KBXParams. 
    Do not instantiate this class directly.
    '''
    PROP_KBX_PARAM_COM = "kbxParamCom"
    PROP_KBX_PARAM_LABEL = "kbxParamLabel"
    PROP_KBX_PARAM_DESC = "kbxParamDesc"
    PROP_KBX_PARAM_DEFAULT_VALUE = "kbxParamDefaultValue"

    def set_kbx_param_label(self, value):
        '''
        Set label of this component.
        
        Params:
        label:String - [Required] Label of this component.
        '''
        pass

    def set_kbx_param_desc(self, value):
        '''
        Set description of this component.
        
        Params:
        desc:String - [Required] Description of this component.
        '''
        pass

    def set_kbx_param_default_value(self, value):
        '''
        Set default value of this component.
        
        Params:
        value - [Required] Default value.
        '''
        pass
        
    def get_kbx_param_com(self):
        '''
        Get the corresponding KBXParam type name.

        Returns:
        A string of the name of this KBXParam type.
        '''
        pass

    def get_kbx_param_label(self):
        '''
        Get label of this component.
        
        Returns:
        Label text.
        '''
        pass

    def get_kbx_param_desc(self):
        '''
        Get description of this component.
        
        Returns:
        Description text.
        '''
        pass

    def get_kbx_param_default_value(self):
        '''
        Get default value of this component.
        
        Returns:
        Default value.
        '''
        pass
