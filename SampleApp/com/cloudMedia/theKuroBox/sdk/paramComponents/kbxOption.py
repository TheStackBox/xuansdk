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


class KBXOption(KBXList, KBXParamComponent):

    def __init__(self, kbxParamName, kbxParamItems=None, kbxParamIsRequired=True, kbxParamMinSize=None, kbxParamMaxSize=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Let user choose from list of items. (Multiple)

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamItems:List<KBXOptionItem> - [Required] List of option items.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this component is required. True by default.
        kbxParamMinSize:Integer - [Optional] Minimum required size of selected items. None by default.
        kbxParamMaxSize:Integer - [Optional] Maximum allowed size of selected items. None by default.
        kbxParamDefaultValue:List - [Option] The default value(s); enclose the value(s) in a list.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDesc:String - [Optional] Description of this component.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_kbx_default_value(self, value):
        '''
        Set default value(s).

        Params:
        value - [Required] Default selected value(s); must be a list.
        '''
        pass

    def set_kbx_param_items(self, value):
        '''
        Set the option list.

        Params:
        value:List<KBXOptionItem> - [Required] List of KBXOption.KBXOptionItem instances.
        '''
        pass

    def set_kbx_param_item(self, index, value):
        '''
        Insert an item into give position.
        
        Params:
        index:Integer - [Required] Position.
        value:Dictionary - [Required] "kbxItemValue" and "kbxItemLabel" must be set in the dictionary.
        '''
        pass

    def append_kbx_param_item(self, value):
        '''
        Append an item to the end of the list.
        
        Params:
        value:Dictionary - [Required] "kbxItemValue" and "kbxItemLabel" must be set in the dictionary.
        '''
        pass

    def prepend_kbx_param_item(self, value):
        '''
        Add an item to the head of the list.
        
        Params:
        value:Dictionary - [Required] "kbxItemValue" and "kbxItemLabel" must be set in the dictionary.
        '''
        pass

    def remove_kbx_param_item(self, index):
        '''
        Remove an item from the list by index.
        
        Params:
        index:Integer - [Required] Position of the item in the list.
        '''
        pass

    def remove_kbx_param_items(self):
        '''
        (Clear) Remove all items from the list.
        '''
        pass

    def get_kbx_param_item_by_index(self, index):
        '''
        Get an item from the list by index.
        
        Params:
        index:Integer - [Required] Position of the item in the list.
        
        Returns:
        Instance of KBXOption.KBXOptionItem.
        '''
        pass

    def get_kbx_param_item_by_value(self, value):
        '''
        Get an item from the list by "kbxItemValue".
        
        Params:
        value - [Required] Value exactly as you set in "kbxItemValue"
        
        Returns:
        Instance of KBXPOption.KBXOptionItem
        '''
        pass

    def get_kbx_param_items(self):
        '''
        Get option list.

        Returns:
        List of KBXOption.KBXOptionItem instances.
        '''
        pass

    class KBXOptionItem(dict):

        @staticmethod
        def build(kbxItemValue, kbxItemLabel=None, **kbxItemProps):
            '''
            Build a valid KBXOptionItem for KBXOption select list.
            
            Params:
            kbxItemValue - [Required] Item value must be unique per list.
            kbxItemLabel:String -[Required] Label of this item.
            **kbxItemProps - Additional properties. Must be able to be converted into json string altogether.
            
            Returns:
            Instance of KBXOption.KBXOptionItem
            '''
            pass

        def set_kbx_item_value(self, value):
            '''
            Set value of this item.
            
            Params:
            value - [Required] Value of this item.
            '''
            pass

        def set_kbx_item_label(self, value):
            '''
            Set label of this item.
            
            Params:
            value:String - [Required] Value of this item.
            '''
            pass

        def set_property(self, key, value):
            '''
            Set additional property value.
            
            Params:
            key - [Required] Key of the property.
            value - [Required] Value of the property.
            '''
            pass

        def get_kbx_item_value(self):
            '''
            Get value of this item.
            
            Returns:
            Value of this item.
            '''
            pass

        def get_kbx_item_label(self):
            '''
            Get label of this item.
            
            Returns:
            Label text of this item.
            '''
            pass

        def get_property(self, key):
            '''
            Get additional property value by key.
            
            Returns:
            Value registered for the key.
            '''
            pass
