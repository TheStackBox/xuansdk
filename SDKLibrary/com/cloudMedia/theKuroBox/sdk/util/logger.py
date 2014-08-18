##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
import inspect, os

class Logger(object):
    '''
    Logger class
    '''
    
    @staticmethod
    def __initLogger():
        '''
        Init the logger class
        '''
        pass
    
    @staticmethod
    def set_enable_debug(enable):
        '''
        Set whether to enable debug or not
        '''
        pass
    
    @staticmethod
    def get_enable_debug():
        '''
        Get whether debug is enabled or not
        '''
        pass
    
    
    @staticmethod
    def add_include():
        '''
        Add calling file into include field.
        '''
        pass
    
    
    @staticmethod
    def add_include_file(filename):
        '''
        Add file into include field
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
        '''
        if (filename in Logger.__includeFile):
            del Logger.__includeFile[filename]
    
    @staticmethod
    def __get_log_information():
        '''
        Get the log information such as file name, line number
        '''
        
        stackItem = inspect.stack()[2]
        return { "file":os.path.basename(stackItem[1]), "line":stackItem[2] }
        
    
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
        