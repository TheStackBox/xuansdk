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


from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException

class AppConfig():
    '''
    Extends ConfigParser Class
    '''
    appconfig = None
    
    @staticmethod
    def set(section="", option="", value=""):
        '''
        Set an option/key. [Override set function]
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option:- the specific key for get purpose
        value:- the data to be set into the key
        '''
        pass

    @staticmethod
    def get(option="", section=""):
        '''
        Get an option/key.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option:- the specific key for get purpose
        return the raw value
        '''
        pass

    @staticmethod
    def remove_section(section):
        '''
        Remove a section.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        return a boolean for success remove
        '''
        pass

    @staticmethod
    def remove_option(option, section=""):
        '''
        Remove an option/key.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option: the specific key to remove.
        return a boolean for success remove
        '''
        pass

    @staticmethod
    def getboolean(option="", section=""):
        '''
        Return/Get the value as boolean.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option: the specific key to get purpose.
        return the result as boolean
        '''
        pass

    @staticmethod
    def getfloat(option="", section=""):
        '''
        Return/Get the value as float.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option: the specific key to get purpose.
        return the result as float
        '''
        pass

    @staticmethod
    def getint(option="", section=""): 
        '''
        Return/Get the value as int.
        section:- the specific group for the key-value pairs. Default section is 'DEFAULT'
        option: the specific key to get purpose.
        return the result as int
        '''
        pass

    @staticmethod
    def getconfig():
        '''
        return the appconfig object.
        '''
        pass

    @staticmethod
    def set_encoding(encoding="utf-8"):
        '''
        encoding: set the data encoding method. Default value is utf-8.
        '''
        pass

