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
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class TemperatureUtils(object):

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
