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


class SpeakerControllerService():

    @staticmethod
    def get_capabilities(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_init(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def speak(pairedDeviceId, text, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Speak given text.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        text:String :- Text to speak.
        '''
        pass
    
    @staticmethod
    def set_start(pairedDeviceId, url, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Start playback.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        url:String :- Media URL
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    @staticmethod
    def set_pause(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pause playback.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        '''
        pass
    
    @staticmethod
    def set_resume(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Resume playback.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    @staticmethod
    def set_stop(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop playback.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    @staticmethod
    def get_mute_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get mute status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"mute": "1"}
        '''
        pass
    
    @staticmethod
    def set_mute_status(pairedDeviceId, mute, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set mute status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        mute:Boolean :- mute status. True=mute, False=unmute
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    @staticmethod
    def get_volume(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get volume.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"volume": "37"}
        '''
        pass
    
    @staticmethod
    def set_volume(pairedDeviceId, volume, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set volume.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        volume:Number :- volume in number
        return:Dictionary :eg- {"success": "true"}
        '''
        pass
    
    @staticmethod
    def get_now_playing_status(pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get now playing status.
        pairedDeviceId:Number :- Paired Device ID return from DeviceManagerService.get_paired_device_list
        return:Dictionary :eg- {"url": "http://23.23.136.93/alsghoaeiw/test.mp3", "currentTime": 8, "status": "PLAYING", "totalTime": 173, "album": "", "albumArt": "", "artist": "", "name": ""}
        '''
        pass
    