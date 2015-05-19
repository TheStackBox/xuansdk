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

from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxParamComponent import KBXParamComponent
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxList import KBXList
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util

class KBXOption(KBXList, KBXParamComponent):

    COM_NAME = "kbxOption"

    PROP_KBX_PARAM_ITEMS = "kbxParamItems"

    def __init__(self, kbxParamName, kbxParamItems=None, kbxParamIsRequired=True, kbxParamMinSize=1, kbxParamMaxSize=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Parameter with selectable options.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamItems:List<KBXOptionItem> - [Required] List of option items.
        kbxParamLabel:String - [Optional] Label of this parameter.
        kbxParamDesc:String - [Optional] Description of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamDefaultValue - [Option] The default value(s); it's a list when multiple selection is enabled.
        kbxParamMultiSelect:Boolean - [Optional] True if multiple values is allowed. False by default.
        kbxParamMinSelectionSize:Integer - [Optional] Minimum size of selected indexes is required. 1 by default.
        kbxParamMaxSelectionSize:Integer - [Optional] Maximum size of selected indexes is allowed. 5 by default.
        kbxParamDelimiter:String - [Optional] Delimiter to separate multiple values.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_default_value(self, value):
        '''
        Set default value(s).

        Params:
        value - [Required] Default selected value(s); can be a list.
        '''
        pass

    def set_kbx_param_items(self, value):
        '''
        Set the option list.

        Params:
        value:List<KBXOptionItem> - [Required] List of KBXOptionItem.
        '''
        pass

    def set_kbx_param_item(self, index, value):
        pass

    def append_kbx_param_item(self, value):
        pass

    def prepend_kbx_param_item(self, value):
        pass

    def remove_kbx_param_item(self, index):
        pass

    def remove_kbx_param_items(self):
        pass

    def get_kbx_param_item_by_index(self, index):
        pass

    def get_kbx_param_item_by_value(self, value):
        pass

    def get_kbx_param_items(self):
        '''
        Get option list.

        Returns:
        List of KBXOptionItem instances.
        '''
        pass

    def _parse_item(self, value):
        '''
        Convert value into KBXOptionItem.

        raise SystemException on failure
        '''
        pass

    def cast(self, value):
        pass

    class KBXOptionItem(dict):

        @staticmethod
        def build(kbxItemValue, kbxItemLabel=None, **kbxItemProps):
            pass

        def set_kbx_item_value(self, value):
            pass

        def set_kbx_item_label(self, value):
            pass

        def set_property(self, key, value):
            pass

        def get_kbx_item_value(self):
            pass

        def get_kbx_item_label(self):
            pass

        def get_property(self, key):
            pass

