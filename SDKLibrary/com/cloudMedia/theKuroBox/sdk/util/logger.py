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

from datetime import datetime
import inspect, os, threading, traceback, sys, json
import fcntl

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.util.httpUtil import HttpUtil

class Logger(object):
    '''
    Logger class
    '''

    @staticmethod
    def set_enable_debug(enable):
        '''
        (OBSOLETED)
        Set whether to enable debug or not
        enable:Boolean        - Set whether to activate logger feature
        '''
        pass

    @staticmethod
    def get_enable_debug():
        '''
        Get whether debug is enabled or not
        return:Boolean       - A boolean value stating whether the logger feature is activated
        '''
        pass

    @staticmethod
    def add_include():
        '''
        Add calling file into include field. If a file is included, only the debug message from the included files will be logged
        '''
        pass

    @staticmethod
    def add_include_file(filename):
        '''
        Add file into include field. If a file is included, only the debug message from the included files will be logged
        filename:String         - The filename which to be included.
        '''
        pass

    @staticmethod
    def remove_include():
        '''
        Remove calling file from include field
        '''
        pass

    @staticmethod
    def remove_include_file(filename):
        '''
        Remove file from include field
        filename:String         - The filename to be removed.
        '''
        pass

    @staticmethod
    def log_info(*info):
        '''
        Log as info
        '''
        pass

    @staticmethod
    def log_debug(*info):
        '''
        Log as debug
        '''
        pass

    @staticmethod
    def log_warning(*info):
        '''
        Log as warning
        '''
        pass

    @staticmethod
    def log_error(*info):
        '''
        Log as error
        '''
        pass

    @staticmethod
    def get_thread_stacks():
        '''
        Get a the stack status of all threads
        Return a dictionary with the following:
        1. count:Number            - Number of alive threads
        2. threads:List            - A list of dictionary object representing a thread with the following:
                                            1. id:number        - The Thread id.
                                            2. stack:List       - A list of stack trace information with the following:
                                                                    1. filename:String        - The filename of the trace
                                                                    2. line:Number            - The line number of the execution
                                                                    3. function:String        - The function name of the execution
        '''
        pass

    @staticmethod
    def _listen_spine_event():
        '''
        Listen to spine notifications.
        '''
        pass

    @staticmethod
    def _sync_debug_status_from_fw():
        '''
        Sync debug status from firmware.
        -- Calls to get_log_path, 
        -- ENABLE logging when successfully retrieves a valid logPath;
        -- DISABLE logging on vice versa.
        '''
        pass

    @staticmethod
    def _register_event():
        pass

    @staticmethod
    def _ipc_logger_status_changed(eventObj):
        '''
        For enabled, sample eventData format: {"isEnabled":false, "logPath":"mnt/sdcard/file", "forLogLevel":12}
        For disabled, sample eventData format: {"isEnabled":false}
        '''
        pass

