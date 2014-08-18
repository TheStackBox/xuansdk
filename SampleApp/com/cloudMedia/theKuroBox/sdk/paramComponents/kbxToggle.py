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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean


class KBXToggle(KBXBoolean, KBXParamComponent):

    COM_NAME = "kbxToggle"

    PROP_KBX_PARAM_TRUE_LABEL = "kbxParamTrueLabel"
    PROP_KBX_PARAM_FALSE_LABEL = "kbxParamFalseLabel"


    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamTrueValue=True, kbxParamFalseValue=False,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, kbxParamTrueLabel="True", kbxParamFalseLabel="False", **kbxParamProps):
        '''
        A true/false toggling component.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamTrueValue - [Optional] Value to be used as True. True by default.
        kbxParamFalseValue - [Optional] Value to be used as False. False by default.
        kbxParamDefaultValue - [Optional] Default value of this component.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDecs:String - [Optional] Description of this component.
        kbxParamTrueLabel:String - [Optional] Label of True value.
        kbxParamFalseLabel:String - [Optional] Label of False value.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_param_default_value(self, value):
        '''
        Set default value of this component.
        
        Params:
        value - [Required] Value as in kbxParamTrueValue or kbxParamFalseValue.
        '''
        pass

    def set_kbx_param_true_label(self, value):
        '''
        Set label of True value.
        
        Params:
        value:String - [Required] Label.
        '''
        pass

    def set_kbx_param_false_label(self, value):
        '''
        Set label of False value.
        
        Params:
        value:String - [Required] Label.
        '''
        pass

    def get_kbx_param_true_label(self):
        '''
        Get the label of True value.
        
        Returns:
        Label string.
        '''
        pass

    def get_kbx_param_false_label(self):
        '''
        Get the label of False value.
        
        Returns:
        Label string.
        '''
        pass