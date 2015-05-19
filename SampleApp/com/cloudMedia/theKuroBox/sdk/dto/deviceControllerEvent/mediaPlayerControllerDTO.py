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

class MediaPlayerControllerDTO(dict):
    '''
    The controller data object
    '''
    
    PLAYBACK_STATUS_STARTED = "playback_started"
    PLAYBACK_STATUS_STOPPED = "playback_stopped"
    PLAYBACK_STATUS_PAUSED = "playback_paused"
    PLAYBACK_STATUS_RESUMED = "playback_resumed"
    
    PLAYBACK_TYPE_VIDEO = "playback_type_video"
    PLAYBACK_TYPE_AUDIO = "playback_type_audio"
    PLAYBACK_TYPE_PHOTO = "playback_type_photo"
    PLAYBACK_TYPE_NONE = "playback_type_none"

    def __init__(self, mediaPlayerControllerDTO=None):
        pass

    def set_paired_device_id(self, pairedDeviceId):
        pass

    def get_paired_device_id(self):
        pass

    def set_playback_status(self, playbackStatus):
        pass

    def get_playback_started(self):
        pass

    def set_playback_type(self, playbackType):
        pass

    def get_playback_type(self):
        pass

    def set_playback_info(self, playbackInfo):
        pass

    def get_playback_info(self):
        pass

    def set_mute_status(self, muteStatus):
        pass

    def get_mute_status(self):
        pass

