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

from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxMetric import KBXMetricType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.temperatureUtils import TemperatureUtils

class KBXTemperatureMetricType(KBXMetricType):

    TYPE_NAME = "kbxTemperature"

    # base unit is Kelvin, everything is kept as Kelvin
    '''
    Constants for temperature units.
    '''
    UNIT_ROEMER = TemperatureUtils.UNIT_ROEMER
    UNIT_REAUMUR = TemperatureUtils.UNIT_REAUMUR
    UNIT_RANKINE = TemperatureUtils.UNIT_RANKINE
    UNIT_KELVIN = TemperatureUtils.UNIT_KELVIN
    UNIT_CELSIUS = TemperatureUtils.UNIT_CELSIUS
    UNIT_FAHRENHEIT = TemperatureUtils.UNIT_FAHRENHEIT
    UNIT_DELISLE = TemperatureUtils.UNIT_DELISLE
    UNIT_NEWTON = TemperatureUtils.UNIT_NEWTON

    def __init__(self, kbxParamIsRequired=True):
        '''
        Parameter that accepts only temperature value. Does not accepts value falls below absolute zero (0K)

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamLabel:String - [Optional] Label of this parameter.
        kbxParamDesc:String - [Optional] Description of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        kbxParamDefaultValue:Boolean - [Optional] Default value of this parameter.
        kbxParamUnit:String - [Optional] Unit used to operate in this parameter. KBXTemperature.UNIT_CELSIUS by default.
        kbxParamMinValue:Integer - [Optional] Lower boundary for the value of this parameter
        kbxParamMaxValue:Integer - [Optional] Upper boundary for the value of this parameter.
        kbxParamDecimal:Boolean - [Optional] True if decimal point is allowed and vice versa. False by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''
        pass

class KBXTemperatureMetric(KBXTemperatureMetricType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        pass

