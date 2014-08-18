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


class SYBPlayerService():

    @staticmethod
    def player_start(url, playerType, startWithState, analyzer, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Start playback.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
     
    @staticmethod
    def player_pause(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pause playback.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_resume(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Resume playback.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_stop(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop playback.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_get_volume(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get volume.
        return:Dictionary :eg- {"volume": "30"}
        '''
        pass
    
    @staticmethod
    def player_set_volume(volume, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set volume.
        volume:Number - volume
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_get_mute(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get mute
        return:Dictionary :eg- {"mute": "1"}
        '''
        pass
    
    @staticmethod
    def player_set_mute(mute, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set mute.
        mute:Boolean :- True=mute, False=unmute
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_seek(time, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Seek to.
        time:Number :- time in seconds
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_set_speed(speed, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set speed.
        speed:Number :- Playback speed. Normal speed is 1
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def player_get_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get current player status.
        '''
        pass
    
    @staticmethod
    def player_get_media_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get media info.
        return:Dictionary :eg- {"mediaInfo": {"CurrentURI": "http://23.23.136.93/alsghoaeiw/test.mp3", "MediaDuration": "0:02:53"}}
        '''
        pass
    
    @staticmethod
    def player_get_device_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get device info.
        return:Dictionary :eg- {"deviceInfo":{"DeviceType":"bluetooth" , "DeviceId": "", "Analyzer":1}}
        '''
        pass
    
    @staticmethod
    def player_get_position_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get position info.
        return:Dictionary :eg- {"positionInfo": {"RelTime": "0:01:41", "AbsTime": "0:01:41", "TrackURI": "http://23.23.136.93/alsghoaeiw/test.mp3", "TrackDuration": "0:02:53"}}
        '''
        pass
    
    @staticmethod
    def player_get_transport_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get transport info.
        return:Dictionary :eg- {"transportInfo": {"CurrentSpeed": "1.0", "CurrentTransportState": "PLAYING"}}
        '''
        pass
    
    @staticmethod
    def player_get_spectrum(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get spectrum.
        return:Dictionary :eg- {"spectrum": {"magnitude": "-1", "frequency": "-1"}}
        '''
        pass
    