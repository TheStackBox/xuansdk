##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
# Xuan Automation Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Automation Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.mediaPlayerControllerService import MediaPlayerControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class MediaPlayerControllerModule(Module):

    def __init__(self, kbxModuleName, parentPath):
        '''
        Constructor
        '''
        super().__init__(kbxModuleName, parentPath)

    def on_system_connected(self):
        super().on_system_connected()
        
        self.register_method(kbxMethodName="get_capabilities",
                             kbxMethodFunc=self.get_capabilities,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_pause",
                             kbxMethodFunc=self.set_player_pause,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_resume",
                             kbxMethodFunc=self.set_player_resume,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_stop",
                             kbxMethodFunc=self.set_player_stop,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_volume_increase",
                             kbxMethodFunc=self.set_player_volume_increase,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_volume_decrease",
                             kbxMethodFunc=self.set_player_volume_decrease,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_mute",
                             kbxMethodFunc=self.set_player_mute,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_unmute",
                             kbxMethodFunc=self.set_player_unmute,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_player_mute_status",
                             kbxMethodFunc=self.get_player_mute_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_status",
                             kbxMethodFunc=self.get_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_send_key",
                             kbxMethodFunc=self.set_player_send_key,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="keyCode", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_play_link",
                             kbxMethodFunc=self.set_player_play_link,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="link", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="mediaType", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="title", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="get_recently_played_list",
                             kbxMethodFunc=self.get_recently_played_list,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_player_play_recently_played",
                             kbxMethodFunc=self.set_player_play_recently_played,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="playbackArgs", kbxParamIsRequired=True)])
        
    def post_system_connected(self):
        super().post_system_connected()
        
        self.register_event_listener(Event.EVENT_MEDIA_PLAYER_PLAYBACK_STATE_CHANGED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_MEDIA_PLAYER_MUTE_STATE_CHANGED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_MEDIA_PLAYER_PLAYBACK_STATUS_RECEIVED, self.__receive_system_event)
        

    def __receive_system_event(self, eventObj):
        Logger.log_debug("MediaPlayerControllerModule.__receive_system_event: ", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])
        
        
    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.get_capabilities(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_pause(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_pause(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
        
    def set_player_resume(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_resume(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_stop(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_stop(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_volume_increase(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_volume_increase(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_volume_decrease(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_volume_decrease(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_mute(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_mute(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_unmute(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_unmute(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def get_player_mute_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.get_player_mute_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.get_player_play_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_send_key(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            keyCode = request.get_arg("keyCode")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_send_key(pairedDeviceId, keyCode=keyCode, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def set_player_play_link(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            link = request.get_arg("link")
            mediaType = request.get_arg("mediaType")
            title = request.get_arg("title")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_play_link(pairedDeviceId, link=link, mediaType=mediaType, title=title, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def get_recently_played_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.get_recently_played_list(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_player_play_recently_played(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            playbackArgs = request.get_arg("playbackArgs")
            
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = MediaPlayerControllerService.set_player_play_recently_played(pairedDeviceId, playbackArgs=playbackArgs, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
