##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxList import KBXList
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator
from collections.abc import Sequence

class KBXFiles(KBXList, KBXParamComponent):

    COM_NAME = "kbxFiles"
    
    PROP_KBX_PARAM_FILTERS = "kbxParamFilters"
    PROP_KBX_PARAM_BROWSE_TYPES = "kbxParamBrowseTypes"
    PROP_KBX_PARAM_SELECT_DIRECTORIES = "kbxParamSelectDirectories"
    
    BROWSE_TYPE_UPNP = "upnp"
    BROWSE_TYPE_LOCAL = "local"
    
    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinSize=1, kbxParamMaxSize=None, kbxParamDuplicate=False,
                 kbxParamFilters=None, kbxParamBrowseTypes=[BROWSE_TYPE_UPNP], kbxParamSelectDirectories=False,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Create a file selection component, users can select file(s) from there.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMaxSize:Number - [Optional] Maximum amount of items in received list allowed. None by default.
        kbxParamMinSize:Number - [Optional] Minimum amount of items in received list required. None by default.
        kbxParamDuplicate:Boolean - [Optional] False if duplication is allowed in received list. True by default.
        kbxParamFilters:List - [Optional] Set filters to filter by extensions. None by default.
        kbxParamSelectDirectories:Boolean - [Optional] Indicates if select directories is allowed. False by default.
        kbxParamBrowseTypes:List - [Optional] Indicates browse types (protocols) allowed. All by default.
        kbxParamDefaultValue:Integer - [Optional] List of file paths.
        kbxParamLabel:String - [Optional] Label of this parameter.
        kbxParamDesc:String - [Optional] Description of this parameter.
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

    def set_kbx_param_select_directories(self, value):
        '''
        Set True if select directories is allowed.
        
        Params:
        value:Boolean - [Required] True if select directories is allowed.
        '''
        pass

    def set_kbx_param_browse_types(self, value):
        '''
        Set browse types. This value is used by UI only.
        
        Params:
        value:List - [Required] List of allowed browse types.
        '''
        pass

    def set_kbx_param_filters(self, value):
        '''
        Set list of filters.
        
        Params:
        value:List - [Required] Set the list of filters, None if no filter should be applied. (e.g [".mp3", ".mp4"])
        '''
        pass

    def get_kbx_param_select_directories(self):
        '''
        Get select directories option.
        
        Returns:
        True if select directories is allowed.
        '''
        pass

    def get_kbx_param_filters(self):
        '''
        Get filters list.
        
        Returns:
        None or list of string indicates the filters.
        '''
        pass

    def get_kbx_param_browse_types(self):
        '''
        Get browse types/protocols allowed. 
        
        Returns:
        List of protocols. See KBXFiles.BROWSE_TYPE_xxxx
        '''
        pass

    def cast(self, value):
        '''
        Converts all items into KBXFiles.KBXFile dictionary.
        
        Params:
        value - Can be a list of dictionaries or None depends on the configurations.
        
        Returns:
        None or list of KBXFiles.KBXFile dictionaries.
        '''
        pass

    class KBXFile(dict):
        
        
        PROP_LABEL = "label"
        PROP_PATH = "path"
        PROP_IS_DIRECTORY = "isDirectory"
        PROP_FILE_TYPE = "fileType" # of the path, eg "upnp"

        @staticmethod
        def build(path, label=None, isDirectory=False, fileType=None, **fileProps):
            pass

        def __init__(self, path, label=None, isDirectory=False, fileType=None, **fileProps):
            pass

        def set_path(self, value):
            pass

        def set_label(self, value):
            pass

        def set_is_directory(self, value):
            pass

        def set_file_type(self, value):
            pass

        def set_prop(self, key, value):
            pass

        def get_path(self):
            pass

        def get_label(self):
            pass

        def is_directory(self):
            pass

        def get_file_type(self):
            pass

        def get_prop(self, key):
            pass

