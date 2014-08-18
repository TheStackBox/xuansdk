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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxMetric import KBXMetricType
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxParamWrapper import KBXParamWrapper
from com.cloudMedia.theKuroBox.sdk.util.temperatureUtils import TemperatureUtils


class KBXTemperatureMetricType(KBXMetricType):
    ''' Base class for KBXTemperatureMetric. '''
    TYPE_NAME = "kbxTemperature"
    
    ''' Temperature units '''    
    UNIT_ROEMER = "Ro"
    UNIT_REAUMUR = "Re"
    UNIT_RANKINE = "R"
    UNIT_KELVIN = "K"
    UNIT_CELSIUS = "C"
    UNIT_FAHRENHEIT = "F"
    UNIT_DELISLE = "D"
    UNIT_NEWTON = "N"


class KBXTemperatureMetric(KBXTemperatureMetricType, KBXParamWrapper):

    def __init__(self, kbxParamName, kbxParamIsRequired=True, **kbxParamProps):
        '''
        Parameter that accepts only temperature value. Does not accepts value falls below absolute zero (0K)

        Params:
        kbxParamName:String - [Required] Name of this parameter.
        kbxParamIsRequired:Boolean - [Optional] True if a value for this parameter is required. True by default.
        **kbxParamProps - Additional properties. Must be able to be converted into json string altogether.
        '''