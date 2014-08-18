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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxObject import KBXObjectType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper


class KBXColorType(KBXObjectType):

    TYPE_NAME = "kbxColor"

    PROP_KBX_PARAM_OBJ_KEY_RED = "r"
    PROP_KBX_PARAM_OBJ_KEY_GREEN = "g"
    PROP_KBX_PARAM_OBJ_KEY_BLUE = "b"

    class DTO(dict):

        @staticmethod
        def build(red, green, blue):
            '''
            Build a valid color object for KBXColor.
            
            Param:
            red:Number - [Required] Red channel value. Ranging from 0 - 255
            green:Number - [Required] Green channel value. Ranging from 0 - 255
            blue:Number - [Required] Blue channel value. Ranging from 0 - 255
            
            Returns:
            Instance of KBXColor.DTO.
            '''
            pass
        
        def set_red(self, value):
            '''
            Set red channel value.
            
            Param:
            value:Integer - [Required] Between 0 and 255 inclusively.
            '''
            pass

        def set_green(self, value):
            '''
            Set green channel value.
            
            Param:
            value:Integer - [Required] Between 0 and 255 inclusively.
            '''
            pass

        def set_blue(self, value):
            '''
            Set blue channel value.
            
            Param:
            value:Integer - [Required] Between 0 and 255 inclusively.
            '''
            pass

        def get_red(self):
            '''
            Get red channel value.
            
            Returns:
            An integer.
            '''
            pass

        def get_green(self):
            '''
            Get green channel value.
            
            Returns:
            An integer.
            '''
            pass

        def get_blue(self):
            '''
            Get blue channel value.
            
            Returns:
            An integer.
            '''
            pass

class KBXColor(KBXColorType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        '''
        This type of parameter receives color object.
        
        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass