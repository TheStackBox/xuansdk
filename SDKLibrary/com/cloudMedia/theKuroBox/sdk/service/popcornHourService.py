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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class PopcornHourService():
    
    @staticmethod
    def get_popcorn_firmware_version(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the firwmare version.
        @param hostIP:String               - IP of the device
        
        @return:
        A dictionary with following information:
        1. firmwareVersion:String          - The firmware version. None if failed
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod    
    def get_popcorn_board_id(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the Board ID (MAC Address).
        @param hostIP:String               - IP of the device

        @return:
        A dictionary with following information:
        1. boardId:String          - The firmware version. None if failed
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod
    def get_popcorn_device_name(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the device name.
        @param hostIP:String               - IP of the device

        @return:
        A dictionary with following information:
        1. deviceName:String          - The firmware version. None if failed
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod
    def get_popcorn_mute_status(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the mute status.
        @param hostIP:String               - IP of the device

        @return:
        A dictionary with following information:
        1. mute:Boolean          - Mute status, True for muted, False for not muted
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod
    def set_popcorn_send_key(hostIP, keyId, environment=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Send a key command
        @param hostIP:String               - IP of the device
        @param key:String                  - Key to send
        @param environment:String          - The environment to execute the key command. Possible value : playback, photo  

        @return:
        A dictionary with following information:
        1. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod
    def get_popcorn_video_playback_info(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the video playback status.
        @param hostIP:String               - IP of the device

        @return:
        A dictionary with following information:
        1. info:Dictionary                 - The info from PCH firmware, None if failed
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

    @staticmethod
    def get_popcorn_audio_playback_info(hostIP, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the audio playback status.
        @param hostIP:String               - IP of the device

        @return:
        A dictionary with following information:
        1. info:Dictionary                 - The info from PCH firmware, None if failed
        2. success:Boolean                 - Whether the API call success 
        '''
        pass

