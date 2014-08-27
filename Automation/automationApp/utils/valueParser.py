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
import json


class ValueParser(object):

    @staticmethod
    def get_string(value):
        if value is None:
            return None
        return str(value) if value else ""

    @staticmethod
    def get_number(value):
        try:
            return int(value)
        except:
            return None

    @staticmethod
    def get_positive_number(value):
        try:
            value = int(value)
            return value if value >= 0 else None
        except:
            return None

    @staticmethod
    def get_list(value):
        if isinstance(value, list):
            return value
        else:
            try:
                value = json.loads(str(value))
                if isinstance(value, list):
                    return value
            except:
                return None
        return None

    @staticmethod
    def get_boolean(value):
        valueString = str(value)
        return True if value and valueString != "false" and valueString != "0" else False

    @staticmethod
    def get_dict(value):
        if isinstance(value, dict):
            return value
        else:
            try:
                value = json.loads(str(value))
                if isinstance(value, dict):
                    return value
            except:
                return None
        return None
