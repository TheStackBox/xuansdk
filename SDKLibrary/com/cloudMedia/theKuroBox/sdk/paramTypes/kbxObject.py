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
import sys

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamType import KBXParamType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper


class KBXObjectType(KBXParamType):

    TYPE_NAME = "kbxObject"

    PROP_KBX_PARAM_OBJ_PROPS = "kbxParamObjProps"
    PROP_KBX_PARAM_STRICT = "kbxParamStrict"

    def set_kbx_param_obj_prop(self, propName, propType=None):
        '''
        Set object property and corresponded validation.
        
        Params:
        propName:String - [Required] Object key name.
        propType - [Optional] Any instance from KBXObject.KBXNumber, KBXObject.KBXString, and KBXObject.KBXBoolean; 
                    or None if you don't want to validate the received value.
        '''
        pass
        
    def set_kbx_param_obj_props(self, value):
        '''
        Bulk update object properties. 
        
        Params:
        value:Dictionary - [Required] Key-value pairs in {[propName]:[propType]} format.
        '''
        pass
    
    def unset_kbx_param_obj_prop(self, propName):
        '''
        Remove any object key set before.
        
        Params:
        propName:String - [Required] Name of the key.
        '''
        pass

    def set_kbx_param_strict(self, value):
        '''
        Specify if received object value should contains only keys that you had defined.
        
        Params:
        value:Boolean - [Required] True if only keys defined are allowed in received object value.
        '''
        pass

    def get_kbx_param_obj_props(self):
        '''
        Retrieve all properties you have set previously.
        
        Returns:
        A dictionary contains of all propName-propType pairs.
        '''
        pass

    def get_kbx_param_strict(self):
        '''
        True if received values must follow strictly the structure you defined.
        
        Returns:
        Boolean value.
        '''
        pass

    class KBXNumber(dict):
        '''
        Used as "propType" for KBXObject.
        Property set as KBXObject.KBXNumber will be casted into number.
        '''
        def __init__(self, kbxParamIsRequired=True, kbxParamDecimal=0, kbxParamMinValue=-(sys.maxsize), kbxParamMaxValue=sys.maxsize):
            pass

    class KBXString(dict):
        '''
        Used as "propType" for KBXObject.
        Property set as KBXObject.KBXString will be casted into string value.
        '''
        def __init__(self, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None):
            pass
        
    class KBXBoolean(dict):
        '''
        Used as "propType" for KBXObject.
        Property set as KBXObject.KBXBoolean will be casted into boolean value.
        '''
        def __init__(self, kbxParamIsRequired=True):
            pass

    class DTO(dict):

        @staticmethod
        def build(**kwargs):
            '''
            Build a dictionary value.
            
            Params:
            **kwargs - [Optional] Key-value pairs will be converted into the dictionary.
            
            Returns:
            Dictionary value built from **kwargs.
            '''
            pass

class KBXObject(KBXObjectType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamObjProps=None, kbxParamStrict=False, **kbxParamProps):
        '''
        Parameter that accepts dictionary/object value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamObjProps:Dictionary - [Optional] Define keys and validation that this parameter accepts. Pass in as {[propName]:[propType]} format.
        kbxParamStrict:Boolean - [Optional] True if you want received value to contain keys that you defined only.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass