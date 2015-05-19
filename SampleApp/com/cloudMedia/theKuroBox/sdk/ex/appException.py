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

class AppException(Exception):
    '''
    SharedMethod.call's receivers can raise this exception to the callers.
    Set "returnValue" in "send_response" to 10000 or above to raise this exception.
    '''
    
    def __init__(self, value):
        '''
        value:Dictionary - A dictionary with keys "returnValue" and "returnMessage".
        * TypeError will be raised if argument provided is not a dictionary.
        '''
        pass

    def get_return_value(self):
        pass

    def get_return_message(self):
        pass

    def get_response(self):
        pass

