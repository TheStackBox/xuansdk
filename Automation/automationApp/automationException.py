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

from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang


class AutomationException(Exception):

    '''
    1500 - 1599: DTO Related Error
    1600 - 1699: API Service Error
    1700 - 1799: Rule Service Error
    1800 - 1899: Timer Module Error
    '''
    __all_exceptions = {
        1095: KBXLang("error_1095"), # "Interpreter Exception", # only possible to be raised if python interpreter goes wrong.
        1096: KBXLang("error_1096"), # "System app is not behaving correctly", # everything related to system app issue.
        1097: KBXLang("error_1097"), # "Invalid parameter", # very common error raised when unexpected value is passed in.
        1098: KBXLang("error_1098"), # "Module Exception",
        1099: KBXLang("error_1099"), # "Unhandled Exception",

        1501: KBXLang("error_1501"), # "Invalid timer type",
        1502: KBXLang("error_1502"), # "Invalid timer value",

        1701: KBXLang("error_1701"), # "Invalid json string",
        1702: KBXLang("error_1702"), # "Unable to create trigger timer",
        1703: KBXLang("error_1703"), # "Trigger object does not have setter information",
        1704: KBXLang("error_1704"), # "Rule updating",
        1705: KBXLang("error_1705"), # "Invalid Params Current Value",
        1706: KBXLang("error_1706"), # "Method size exceeded allowed value (%s)",
        1707: KBXLang("error_1707"), # "RuleId not found",
        1708: KBXLang("error_1708") # "Rule size reached limit",
    }

    def __init__(self, exCode, exExtra=None):
        try:
            exCode = int(str(exCode))
            if not exCode in AutomationException.__all_exceptions:
                raise Exception()
            else:
                self.__code = exCode
        except Exception:
            self.__code = 1099
        self.__code = exCode
        self.__extra = exExtra
        super().__init__(AutomationException.__all_exceptions.get(exCode, ""))

    def err_to_dict(self):
        exCode = self.__code
        return {"returnValue": exCode, "returnMesssage":AutomationException.__all_exceptions.get(exCode, ""), "debugMessage":self.__extra}

    def err_to_json_str(self):
        return json.dumps(self.err_to_dict(), sort_keys=True)

    def get_error_code(self):
        return self.__code

    def get_error_message(self):
        return AutomationException.__all_exceptions.get(self.__code)

    def get_debug_message(self):
        return self.__extra
