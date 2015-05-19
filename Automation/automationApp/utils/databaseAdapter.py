##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
# Xuan Automation Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Automation Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

import json


class DatabaseAdapter:
    
    
    @staticmethod    
    def ADAPT_BOOLEAN(boolValue):
        if boolValue == None:
            return None
        return b'1' if boolValue is True else b'0'
    
    @staticmethod
    def CONVERT_BOOLEAN(byteString):
        if byteString == None:
            return None
        return True if byteString == b'1' else False
            
    @staticmethod
    def ADAPT_DICTIONARY(dictValue):
        if dictValue == None:
            return None
        return json.dumps(dictValue).encode()
    
    @staticmethod
    def CONVERT_DICTIONARY(byteString):
        if byteString == None:
            return None
        return json.loads(byteString.decode())
    
    @staticmethod
    def ADAPT_LIST(listValue):
        if listValue == None:
            return None
        return json.dumps(listValue).encode()
    
    @staticmethod
    def CONVERT_LIST(byteString):
        if byteString == None:
            return None
        return json.loads(byteString.decode())
