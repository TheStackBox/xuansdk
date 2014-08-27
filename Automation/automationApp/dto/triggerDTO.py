##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
#    Xuan Automation Application is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from automationApp.utils.valueParser import ValueParser


class TriggerDTO(dict):

    TYPE_EVENT = 0 # receive no value
    TYPE_TIME = 1 # receive value as "HH:MM" ranged from 0-23 and 0-59
    TYPE_INTERVAL = 2 # receive seconds

    PROP_TYPE = "type"
    PROP_VALUE = "value"
    PROP_PARSED_VALUE = "parsedValue"

    def __init__(self, **kwargs):
        super().__init__()
        mappers = {TriggerDTO.PROP_TYPE:self.set_type,
                  TriggerDTO.PROP_VALUE:self.set_value}

        keys = []
        for key, method in mappers.items():
            keys.append(key)
            try:
                method(kwargs[key])
            except:
                method(None)

        for key, value in kwargs.items():
            if key not in keys:
                self[key] = value

    def get_type(self):
        return self.get(TriggerDTO.PROP_TYPE)

    def get_value(self):
        return self.get(TriggerDTO.PROP_VALUE)

    def get_parsed_value(self):
        return self.get(TriggerDTO.PROP_PARSED_VALUE)

    def is_no_callback(self):
        return self.get_type() not in (TriggerDTO.TYPE_TIME, TriggerDTO.TYPE_INTERVAL)

    def set_type(self, value):
        self[TriggerDTO.PROP_TYPE] = ValueParser.get_number(value)

    def set_value(self, value):
        self[TriggerDTO.PROP_VALUE] = value

    def set_parsed_value(self, value):
        self[TriggerDTO.PROP_PARSED_VALUE] = value
