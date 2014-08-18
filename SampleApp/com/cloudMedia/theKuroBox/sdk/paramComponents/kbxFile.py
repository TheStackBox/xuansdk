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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxList import KBXList


class KBXFile(KBXList, KBXParamComponent):

    COM_NAME = "kbxFile"

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinSize=None, kbxParamMaxSize=None, kbxParamDuplicate=False,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Let end users select file(s) from file dialogue.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMaxSize:Number - [Optional] Maximum amount of items in received list allowed. None by default.
        kbxParamMinSize:Number - [Optional] Minimum amount of items in received list required. None by default.
        kbxParamDuplicate:Boolean - [Optional] False if duplication is allowed in received list. True by default.
        kbxParamDefaultValue:Integer - [Optional] List of file paths.
        kbxParamLabel:String - [Optional] Label of this parameter.
        kbxParamDesc:String - [Optional] Description of this parameter.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass


    def set_kbx_param_default_value(self, value):
        '''
        Set default value for this component.

        Params:
        value:List<String> - [Required] List of file paths.
        '''
        pass
