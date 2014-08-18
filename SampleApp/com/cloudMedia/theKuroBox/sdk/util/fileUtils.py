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

class FileUtils(object):

    @staticmethod
    def read_file(path):
        '''
        Function : Read content of file specified by "path" and return as string. All exception will return None
        '''
        pass
    

    @staticmethod
    def write_file(path, content, append=False):
        '''
        Function : Write provided content into file specified by "path". 
        Content will be converted to String before writing
        '''
        pass
    

    @staticmethod
    def write_raw_file(path, content, append=False):
        '''
        Function : Write provided content to file specified by "path"
        Content must be bytes
        '''
        pass
    
