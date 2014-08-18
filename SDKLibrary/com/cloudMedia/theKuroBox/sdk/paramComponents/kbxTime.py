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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxDateTime import KBXDateTime


class KBXTime(KBXDateTime, KBXParamComponent):

    COM_NAME = "kbxTime"

    def __init__(self, kbxParamName, kbxParamIsRequired=True,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        A true/false toggling component.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
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
        value:Integer - [Required] Seconds.
        '''
        pass

    class DTO(int):

        @staticmethod
        def build(value):
            '''
            Build an instance of KBXDateTime.DTO.
            
            Params:
            value:Integer - [Required] Seconds.
            '''
            pass

        def get_date_time_obj(self):
            '''
            Cast this integer value into datetime object.
            
            Returns:
            Python built-in  datetime object.
            '''
            pass

        def get_second(self):
            '''
            Get seconds portion of this value.
            
            Returns:
            Integer between 0 - 59 inclusively.
            '''
            pass

        def get_minute(self):
            '''
            Get minute portion of this value.
            
            Returns:
            Integer between 0 - 59 inclusively.
            '''
            pass

        def get_hour(self):
            '''
            Get hour portion of this value.
            
            Returns:
            Integer between 0 - 23 inclusively.
            '''
            pass