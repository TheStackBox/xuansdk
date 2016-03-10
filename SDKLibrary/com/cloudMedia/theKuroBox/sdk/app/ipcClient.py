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

import json

from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from threading import Thread, Event
from urllib.parse import urlencode, parse_qs

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.timeout import timelimit

class IPCRequest(object):
    '''
    Request object of request coming from IPC
    '''
    def __init__(self, requestId, args):
        pass

    def get_value(self, argName):
        '''
        Get parsed argument value.
        '''
        pass

    def get_arg(self, argName):
        '''
        Get raw argument value from request. Return None if not found.
        '''
        pass

    def get_all_args(self):
        '''
        Return a dictionary object with all argument values
        '''
        pass

    def get_method_param(self, paramName):
        pass

    def has_arg(self, name):
        '''
        Check whether the request contains all the argNames
        '''
        pass

    def get_method_config(self, name):
        pass

class IPCClient(object):
    '''
    Interprocess Communication client class. Handles interaction between current app with System
    '''

    KEY_REQUEST_ID = "ipcRequestId" # The key for requestId in method call
    KEY_REQUEST_CONNECTION = "ipcRequestConnection"
    KEY_REQUEST_INTERNAL = "ipcInternalCall"

    @staticmethod
    def response(data, requestId, returnValue=100, returnMessage=""):
        '''
        Respond result to API Call from IPC
        data : The data in string format
        requestId : The request ID in the request object
        '''
        pass

    @staticmethod
    def call(targetId, targetMethod, targetModule, **params):
        '''
        Call targetMethod of a remote app
        targetId : The targetId appid
        targetMethod : The targetMethod name
        targetModule : The targetModule name
        **params : Any parameters required by the targetMethod

        Returns : The result of IPC call
        '''
        pass

    @staticmethod
    def register_event(eventTag):
        '''
        Register an event tag
        eventTag : The eventTag type tag

        Returns    - True if register successful, False otherwise
        '''
        pass

    @staticmethod
    def unregister_event(eventTag):
        '''
        Unregister an event tag
        eventTag : The eventTag type tag

        Returns    - JSON str with format of :
                         1. returnValue:Number    - The return value
                         2. returnMessage:String  - The message associated to the return value
        '''
        pass

    @staticmethod
    def register_event_listener(eventTag, callback):
        '''
        Register an event listener
        eventTag : The eventTag type tag
        callback : Callback function. It receives a event dict with properties of "eventTag" and "eventData"


        Returns    - True if register successful, False otherwise
        '''
        pass

    @staticmethod
    def unregister_event_listener(eventTag, callback):
        '''
        Unregister an event listener
        eventTag : The eventTag type tag
        callback : Callback function
        '''
        pass

    @staticmethod
    def fire_event(eventTag, eventData):
        '''
        Fire event to System
        eventTag : The event tag
        eventData : The event data to send in string
        '''
        pass

