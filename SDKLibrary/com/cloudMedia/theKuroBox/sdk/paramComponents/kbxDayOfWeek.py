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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption


class KBXDayOfWeek(KBXOption):

    COM_NAME = "kbxDayOfWeek"

    ''' Constants for the days of the week in integers. '''
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinSize=None, kbxParamMaxSize=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Parameter for that accepts days of week values.

        Params:
        kbxParamName:String - [Required] Name of this component.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamMinSize:Integer - [Optional] Minimum required size of selected items. None by default.
        kbxParamMaxSize:Integer - [Optional] Maximum allowed size of selected items. None by default.
        kbxParamDefaultValue:List - [Option] The default value(s); enclose the value(s) in a list.
        kbxParamLabel:String - [Optional] Label of this component.
        kbxParamDesc:String - [Optional] Description of this component.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_day_label(self, day, label):
        '''
        Set label for the days.
        
        Params:
        day:Integer - [Required] The day to set the label.
        label:String - [Required] Label text.
        '''
        pass