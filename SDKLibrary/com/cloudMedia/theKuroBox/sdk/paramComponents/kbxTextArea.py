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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString


class KBXTextArea(KBXString, KBXParamComponent):

    COM_NAME = "kbxTextArea"

    PROP_KBX_PARAM_PLACEHOLDER = "kbxParamPlaceholder"

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, kbxParamPlaceholder=None, **kbxParamProps):
        '''
        Multiline text input.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMinLength:Integer - [Optional] Minimum required length of the text.
        kbxParamMaxLength:Integer - [Optional] Maximum allowed length of the text.
        kbxParamDefaultValue - [Optional] Default value of this component.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDecs:String - [Optional] Description of this component.
        kbxParamPlaceholder:String - [Optional] Placeholder text.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
    
    def set_kbx_param_default_value(self, value):
        '''
        Set default value of this component.
        
        Params:
        value:String - [Required] Default text.
        '''
        pass
    
    def set_kbx_param_placeholder(self, value):
        '''
        Set placeholder text of this component.
        
        Params:
        value:String - [Required] Placeholder text.
        '''
        pass

    def get_kbx_param_placeholder(self):
        '''
        Get placeholder text.
        
        Returns:
        Placeholder text.
        '''
        pass