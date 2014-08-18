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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumberType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper


class KBXDateTimeType(KBXNumberType):

    TYPE_NAME = "kbxDateTime"

    class DTO(int):

        @staticmethod
        def build(value):
            '''
            Build an instance of KBXDateTime.DTO.
            
            Params:
            value:Integer - [Required] Valid timestamp integer.
            '''
            pass

        def get_date_time_obj(self):
            '''
            Cast this integer value into datetime object.
            
            Returns:
            Python built-in  datetime object.
            '''
            pass

class KBXDateTime(KBXDateTimeType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        '''
        Receive timestamp as parameter.
        You will get KBXDateTimeType.DTO instance which you can get standard datetime object by calling "get_date_time_obj".
        
        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass