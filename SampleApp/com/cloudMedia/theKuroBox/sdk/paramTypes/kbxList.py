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


class KBXListType(KBXParamType):

    TYPE_NAME = "kbxList"

    PROP_KBX_PARAM_TYPE_INFERENCE = "kbxParamTypeInference"
    PROP_KBX_PARAM_MAX_SIZE = "kbxParamMaxSize"
    PROP_KBX_PARAM_MIN_SIZE = "kbxParamMinSize"
    PROP_KBX_PARAM_DUPLICATE = "kbxParamDuplicate"

    def set_kbx_param_type_inference(self, value):
        '''
        Set the instance that list will validate the received values against it.
        
        Params:
        value - [Optional] Any instance from KBXList.KBXNumber, KBXList.KBXString, and KBXList.KBXBoolean; 
                  or None if you don't want to validate the received values.
        '''
        pass

    def set_kbx_param_min_size(self, value):
        '''
        Set minimum amount of items received list should contains.
        
        Params:
        value:Integer - [Required] None if you do not want to limit the minimum size. 
        '''
        pass

    def set_kbx_param_max_size(self, value):
        '''
        Set maximum amount of items received list can have.
        
        Params:
        value:Integer - [Required] None if you do not want to limit the maximum size.
        '''
        pass

    def set_kbx_param_duplicate(self, value):
        '''
        Set whether items in received list can be repeated.
        
        Params:
        value:Boolean - [Required] True if values in received list can be repeated.
        '''
        pass

    def get_kbx_param_type_inference(self):
        '''
        Get current instance for casting.
        
        Returns:
        Instance of KBXList.KBXNumber, KBXList.KBXString, KBXList.KBXBoolean, or None.
        '''
        pass

    def get_kbx_param_min_size(self):
        '''
        Get value of minimum size required.
        
        Returns:
        An integer or None.
        '''
        pass

    def get_kbx_param_max_size(self):
        '''
        Get value of maximum size allowed.
        
        Returns:
        An integer or None.
        '''
        pass

    def get_kbx_param_duplicate(self):
        '''
        Get current state of duplication blocking.
        
        Returns:
        Boolean value. True means duplication in received list is allowed and vice versa.
        '''
        pass

    class KBXNumber(dict):
        '''
        Items in received list will be casted into number.
        '''
        def __init__(self, kbxParamIsRequired=True, kbxParamDecimal=0, kbxParamMinValue=-(sys.maxsize), kbxParamMaxValue=sys.maxsize):
            pass

    class KBXString(dict):
        '''
        Items in received list will be casted into string.
        '''
        def __init__(self, kbxParamIsRequired=True, kbxParamMinLength=None, kbxParamMaxLength=None):
            pass

    class KBXBoolean(dict):
        '''
        Items in received list will be casted into boolean.
        '''
        def __init__(self, kbxParamIsRequired=True):
            pass

class KBXList(KBXListType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamTypeInference=None, 
                 kbxParamMaxSize=None, kbxParamMinSize=None, kbxParamDuplicate=True, **kbxParamProps):
        '''
        Parameter that accepts list as value.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamTypeInference - [Optional] Any instance from KBXList.KBXNumber, KBXList.KBXString, and KBXList.KBXBoolean; or None if you don't want to validate the received values.
        kbxParamMaxSize:Number - [Optional] Maximum amount of items in received list allowed. None by default.
        kbxParamMinSize:Number - [Optional] Minimum amount of items in received list required. None by default.
        kbxParamDuplicate:Boolean - [Optional] False if duplication is allowed in received list. True by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
