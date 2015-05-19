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

from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock

class MethodCallGroup(object):
    '''
    This class groups similar shared method calls, fires only once and replies to all callers with the result.
    '''
    
    def __init__(self, max_workers=5):
        '''
        This is multi-threaded caller.
        max_workers - Maximum simultaneous threads.
        async - Set it to True then "submit" will not wait for the response.
        '''
        pass

    def submit(self, callId, callFn, callKwargs, callbackFn=None, **callbackKwargs):
        '''
        callId - A string. Same call Id will be called only once.
        callFn - A callable function where "**kwargs" will be pass as arguments later.
        callKwargs - A dictionary object which can be passed into callerFn.
        callbackFn - A callable which takes effect only when async = True.
        callbackKwargs - "callback" will accepts the result as the first argument, and **callbackKW as the rest of the arguments.
         -- result can be the return value, or an instance of Exception.
        '''
        pass

