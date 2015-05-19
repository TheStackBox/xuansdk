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

from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class TemperatureUtils(object):

    UNIT_ROEMER = "Ro"
    UNIT_REAUMUR = "Re"
    UNIT_RANKINE = "R"
    UNIT_KELVIN = "K"
    UNIT_CELSIUS = "C"
    UNIT_FAHRENHEIT = "F"
    UNIT_DELISLE = "D"
    UNIT_NEWTON = "N"

    UNITS = {UNIT_ROEMER:{__LABEL:"R\u00F8mer", __SYMBOL:"\u00B0R\u00F8", __TO_KELVIN:lambda x: (x - 7.5) * 40 / 21 + 273.15, __FROM_KELVIN:lambda x: (x - 273.15) * 21 / 40 + 7.5},
             UNIT_REAUMUR:{__LABEL:"R\u00E9aumur", __SYMBOL:"\u00B0R\u00E9", __TO_KELVIN:lambda x: x * 5 / 4 + 273.15, __FROM_KELVIN:lambda x: (x - 273.15) * 4 / 5},
             UNIT_RANKINE:{__LABEL:"Rankine", __SYMBOL:"\u00B0R", __TO_KELVIN:lambda x: x * 5 / 9, __FROM_KELVIN:lambda x: x * 9 / 5},
             UNIT_KELVIN:{__LABEL:"Kelvin", __SYMBOL:"K", __TO_KELVIN:lambda x: x, __FROM_KELVIN:lambda x: x},
             UNIT_CELSIUS:{__LABEL:"Celsius", __SYMBOL:"\u00B0C", __TO_KELVIN:lambda x: x + 273.15, __FROM_KELVIN:lambda x: x - 273.15},
             UNIT_FAHRENHEIT:{__LABEL:"Fahrenheit", __SYMBOL:"\u00B0F", __TO_KELVIN:lambda x: (x + 459.67) * 5 / 9, __FROM_KELVIN:lambda x: x * 9 / 5 - 459.67},
             UNIT_DELISLE:{__LABEL:"Delisle", __SYMBOL:"\u00B0D", __TO_KELVIN:lambda x: 373.15 - x * 2 / 3, __FROM_KELVIN:lambda x: (373.15 - x) * 3 / 2},
             UNIT_NEWTON:{__LABEL:"Newton", __SYMBOL:"\u00B0N", __TO_KELVIN:lambda x: x * 100 / 33 + 273.15, __FROM_KELVIN:lambda x: (x - 273.15) * 33 / 100}}

    @staticmethod
    def convert(value, fromUnit, toUnit):
        '''
        Convert a value between two units.

        Params:
        value:Integer - [Required] The number to be converted. (Note that a value which drops below absolute zero will be rejected)
        fromUnit:String - [Required] Convert the value from this unit. eg TemperatureUtils.UNIT_KELVIN
        toUnit:String - [Required] Convert the value into this unit. eg TemperatureUtils.UNIT_CELSIUS

        Returns:
        Converted value.
        '''
        pass

    @staticmethod
    def get_unit_label(unit):
        '''
        Get the label of a particular unit.

        Params:
        unit:String - [Required] The unit of the label. eg TemperatureUtils.UNIT_FAHRENHEIT

        Returns:
        Label of the unit.
        '''
        pass

    @staticmethod
    def get_unit_symbol(unit):
        '''
        Get the scientific symbol of a particular unit.

        Params:
        unit:String - [Required] The unit of the symbol. eg TemperatureUtils.UNIT_NEWTON

        Returns:
        Symbol of the unit.
        '''
        pass

