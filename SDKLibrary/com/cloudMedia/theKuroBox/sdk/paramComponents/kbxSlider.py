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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange


class KBXSlider(KBXRange, KBXParamComponent):

    COM_NAME = "kbxSlider"

    def __init__(self, kbxParamName, kbxParamMinValue, kbxParamMaxValue, kbxParamIsRequired=True, kbxParamDecimal=0, kbxParamStep=1,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Slider component.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamMinValue:Integer - [Required] Lower boundary for the value of this component
        kbxParamMaxValue:Integer - [Required] Upper boundary for the value of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamDecimal:Boolean - [Optional] True if decimal point is allowed and vice versa. False by default.
        kbxParamStep:Integer - [Optional] A value to indicates the step of the movement of the value.
        kbxParamDefaultValue - [Optional] Default value of this component.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDecs:String - [Optional] Description of this component.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_param_default_value(self, value):
        '''
        Set default value of this component.
        
        Params:
        value:Number - [Required] A default number.
        '''
        pass