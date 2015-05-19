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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class KBXOptionWithIcon(KBXOption):
    '''
    Sample:
    iconpaths = ['/allweb/2000500/styles/fonts/RemoteIcon.woff', 
             '/allweb/2000500/styles/fonts/RemoteIcon.woff', 
             '/allweb/2000500/styles/fonts/RemoteIcon.svg']
             
    # You can build param items using either way (paramItem or paramItem2)
    paramItem = KBXOptionWithIcon.KBXOptionWithIconItem.build("item1", "&#ex6542", iconpaths, "RemoteIcon")
    paramItem2 = {"kbxItemValue":"item2", 
                  "kbxItemLabel":"label2",
                  "kbxItemIcon":"&#ex6543",
                  "kbxItemIconPaths":iconpaths,
                  "kbxItemIconFamily":"RemoteIcon"}

    kbxOptionWithIcon = KBXOptionWithIcon(kbxParamName="option_w_icon", kbxParamItems=[paramItem, paramItem2])
    '''

    COM_NAME = "kbxOptionWithIcon"

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

    def _parse_item(self, value):
        '''
        Convert value into KBXOptionWithIconItem.

        raise SystemException on failure
        '''
        pass

    class KBXOptionWithIconItem(KBXOption.KBXOptionItem):

        @staticmethod
        def build(kbxItemValue, kbxItemIcon, kbxItemIconPaths, kbxItemIconFamily, kbxItemIconStyle=None, kbxItemIconColor=None, kbxItemLabel=None, **kbxItemProps):
            pass

        def set_kbx_item_icon(self, value):
            pass

        def set_kbx_item_icon_paths(self, value):
            pass

        def set_kbx_item_icon_family(self, value):
            pass

        def set_kbx_item_icon_style(self, value):
            pass

        def set_kbx_item_icon_color(self, value):
            pass

        def get_kbx_item_icon(self):
            pass

        def get_kbx_item_icon_paths(self):
            pass

        def get_kbx_item_icon_family(self):
            pass

        def get_kbx_item_icon_style(self):
            pass

        def get_kbx_item_icon_color(self):
            pass

