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
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod


class FileBrowserService(object):
    '''
    SDK Service for File Browser
    '''
    
    @staticmethod
    def get_storage_source_type():
        '''
        Return the type of storage source type. E.g. : UPNP, Local

        '''                                
        pass
     
    @staticmethod
    def browse_file(storageType, path, limit, offset, excludeFiles):
        '''
        Return the content of path
        - storageType:String      - The type of storage, "upnp", "local". (auto detect, unless fail to parse using the path) [Needed if your path is empty]
        - path:String             - The path to browse in JSON array string. Empty string, null, empty array will browse from the root (list UPNP Servers detected, list USB storage attached, etc.)
        - limit:Integer           - total item
        - offset:Integer          - start index
        - excludeFiles:Boolean    - Set true to return only the folders
        '''
        pass
     
    @staticmethod
    def get_media_info(storageType, path):
        '''
        Return the content of path
        - storageType:String      - The type of storage, "upnp", "local". (auto detect, unless fail to parse using the path)
        - path:String             - The media file path in JSON array string.
        '''
        pass
    