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
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

class Logger(object):
    '''
    Logger class
    '''
    
    @staticmethod
    def set_enable_debug(enable):
        '''
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
        info:[Multiple Object Input]       - the message to be logged
        '''
        pass
        
    @staticmethod
    def log_debug(*info):
        '''
        Log as debug
        info:[Multiple Object Input]       - the message to be logged
        '''
        pass
    
    @staticmethod
    def log_warning(*info):
        '''
        Log as warning
        info:[Multiple Object Input]       - the message to be logged
        '''
        pass
        
    @staticmethod
    def log_error(*info):
        '''
        Log as error
        info:[Multiple Object Input]       - the message to be logged
        '''
        pass
        