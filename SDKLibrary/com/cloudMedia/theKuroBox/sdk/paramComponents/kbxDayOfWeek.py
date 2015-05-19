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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class KBXDayOfWeek(KBXOption):

    COM_NAME = "kbxDayOfWeek"

    '''
    Constants for the days of the week in integers.
    '''
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    def __init__(self, kbxParamName, kbxParamIsRequired=True, kbxParamMinSize=1, kbxParamMaxSize=None,
                 kbxParamDefaultValue=None, kbxParamLabel=None, kbxParamDesc=None, **kbxParamProps):
        '''
        Parameter for that accepts days of week values.

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamLabel:String - [Optional] Label of this parameter.
        kbxParamDesc:String - [Optional] Description of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamDefaultSelectedIndex:Integer - [Option] The default selected index of options.
        kbxParamMultiSelect:Boolean - [Optional] True if multiple values is allowed. False by default.
        kbxParamMinSize:Integer - [Optional] Minimum size of selected indexes is required. 1 by default.
        kbxParamMaxSize:Integer - [Optional] Maximum size of selected indexes is allowed. 5 by default.
        kbxParamDelimiter:String - [Optional] Delimiter to separate multiple values.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

    def set_day_label(self, day, label):
        pass

