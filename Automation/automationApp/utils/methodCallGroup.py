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
        self.__callId_callbackList = {} # 1-level dict, [callId] -- [callback tasks]
        self.__fs_callbackList = {} # 1-level dict, [fs] = [callback tasks]
        self.__fs_callId = {}
        self.__threadPool = ThreadPoolExecutor(max_workers=max_workers)
        self.__lock = Lock()
        self.__taskId = 0
        
    def submit(self, callId, callFn, callKwargs, callbackFn=None, **callbackKwargs):
        '''
        callId - A string. Same call Id will be called only once.
        callFn - A callable function where "**kwargs" will be pass as arguments later.
        callKwargs - A dictionary object which can be passed into callerFn.
        callbackFn - A callable which takes effect only when async = True.
        callbackKwargs - "callback" will accepts the result as the first argument, and **callbackKW as the rest of the arguments.
         -- result can be the return value, or an instance of Exception.
        '''
        # Generate task id
        taskId = self.__taskId = (self.__taskId + 1) % 9999
        fs = None
        
        with self.__lock:
            
            if callId not in self.__callId_callbackList:
                fs = self.__threadPool.submit(callFn, **callKwargs)
                
                callbackList = {}
                self.__fs_callbackList[fs] = callbackList
                self.__callId_callbackList[callId] = callbackList
                self.__fs_callId[fs] = callId
                
            else:
                callbackList = self.__callId_callbackList[callId]
            
            callbackList[taskId] = (callbackFn, callbackKwargs)
                
        if fs is not None:
            fs.add_done_callback(self.__done_callback)

        return taskId
    
    def __done_callback(self, fs):
        with self.__lock:
            callbackList = self.__fs_callbackList[fs]
            del(self.__fs_callbackList[fs])
            del(self.__callId_callbackList[self.__fs_callId[fs]])
            del(self.__fs_callId[fs])
    
        try:
            result = fs.result()
        except Exception as e:
            result = e
        
        for taskId, (callbackFn, callbackKwargs) in callbackList.items():
            callbackFn(taskId, result, **callbackKwargs)

