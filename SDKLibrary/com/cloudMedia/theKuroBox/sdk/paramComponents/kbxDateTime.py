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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxDateTime import KBXDateTime as KBXDateTimeSDK


class KBXDateTime(KBXDateTimeSDK, KBXParamComponent):

    COM_NAME = "kbxDateTime"

    def __init__(self, kbxParamName, kbxParamIsRequired=True,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        User will see a date-time picker.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this component is required. True by default.
        kbxParamDefaultValue:Integer - [Optional] Default timestamp for this parameter.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDesc:String - [Optional] Description of this component.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass
    
    def set_kbx_param_default_value(self, value):
        '''
        Set default value for this parameter.

        Params:
        value:Integer - [Required] The default timestamp.
        '''
        pass