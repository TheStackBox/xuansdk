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

from threading import Thread
import sys

'''
Timeout an call
NOTE: The call is NOT interrupted, but raise a TimeoutError instead.
timeout:Number    - Timeout in seconds
'''

def timelimit(timeout):
    '''
    Wrap a function call with timeout control. Can be used as annotation as well.
    '''
    def internal(function):
        def internal2(*args, **kw):
            class Calculator(Thread):
                def __init__(self):
                    pass

                def run(self):
                    pass

