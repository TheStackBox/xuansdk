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
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod


class FileOperationService():
    
    @staticmethod
    def list_user_storage_file(path, offset, limit, showFolder, showFile, showInfo, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List user storage file.
        path:String :- path
        offset:Number :- offset
        limit:Number :- limit
        showFolder:Boolean :- show folder
        showFile:Boolean :- show file
        showInfo:Boolean :- show info
        '''                                
        pass
    
    @staticmethod
    def download_file(sourcePath, destinationPath, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List user storage file.
        sourcePath:String :- source path
        destinationPath:String :- destination 
        return:Dictionary :eg- {"success":"True"}

        '''                                
        pass
    
    @staticmethod
    def delete_user_storage_file(filePath, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List user storage file.
        filePath:String :- file path
        return:Dictionary :eg- {"success":"True"}

        '''                                
        pass
    
    @staticmethod
    def get_media_info(file, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List user storage file.
        file:String :- file
        return:Dictionary :eg- {"mediaInfo":{"name":"", "artist":""}}

        '''                                
        pass
    