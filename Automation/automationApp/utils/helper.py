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

import urllib.parse

class Helper:
    
    
    @staticmethod
    def truncate_by_word(content, length=100, suffix='...'):
        '''
        Hellohowareyou - Hellohowar...
        Hello how are you - Hello how...
        Hello - Hello
        '''
        if len(content) <= length:
            return content
        else:
            result = ' '.join(content[:length+1].split(' ')[0:-1])
            if result == "":
                result = ''.join(content[:length])
            return result + suffix
        
    @staticmethod
    def parse_post_data(paramsRaw):
        '''
        Parse POST data from a chunk of encoded raw data into key-value pairs.
        '''
        paramsDecoded = paramsRaw.decode("utf-8")
        return {str(x[0]):urllib.parse.unquote_plus(str(x[1])) for x in (i.split("=", 1) for i in paramsDecoded.split("&"))}

