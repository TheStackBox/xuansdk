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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.speakerControllerService import SpeakerControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class SpeakerControllerModule(Module):
    '''
    Speaker Controller Class
    '''

    def __init__(self, kbxModuleName, parentPath):
        '''
        Constructor
        '''
        super().__init__(kbxModuleName, parentPath)

        self.register_method(kbxMethodName="get_capabilities",
                             kbxMethodFunc=self.get_capabilities,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_status",
                             kbxMethodFunc=self.get_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxparamIsRequired=True)])

        self.register_method(kbxMethodName="set_init",
                             kbxMethodFunc=self.set_init,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXBoolean(kbxParamName="forceInit", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_speak",
                             kbxMethodFunc=self.set_speak,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="text", kbxParamIsRequired=True, kbxParamMaxLength=100),
                                              KBXString(kbxParamName="serviceProvider", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="lang", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_start",
                             kbxMethodFunc=self.set_start,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="url", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="name", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="album", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="artist", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="albumArt", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="urlDetails", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="urlFormat", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_pause",
                             kbxMethodFunc=self.set_pause,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_resume",
                             kbxMethodFunc=self.set_resume,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_stop",
                             kbxMethodFunc=self.set_stop,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_mute_status",
                             kbxMethodFunc=self.get_mute_status,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_mute_status",
                             kbxMethodFunc=self.set_mute_status,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXBoolean(kbxParamName="mute", kbxParamTrueLabel="Mute", kbxParamFalseLabel="Unmute", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_volume",
                             kbxMethodFunc=self.get_volume,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_volume",
                             kbxMethodFunc=self.set_volume,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="volume", kbxParamMinValue=0, kbxParamMaxValue=100, kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_now_playing_status",
                             kbxMethodFunc=self.get_now_playing_status,
                             kbxMethodIsPrivate=False,
                             kbxMethodLabel="Get Now Playing Status",
                             kbxMethodDesc="Get now playing status",
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

    def post_system_connected(self):
        super().post_system_connected()
        
#         self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_PLAYBACK_STARTED, self.__receive_system_event)
#         self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_PLAYBACK_STATE_CHANGED, self.__receive_system_event)
#         self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_PLAYBACK_VOLUME_CHANGED, self.__receive_system_event)
#         self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_PLAYBACK_MUTE_STATE_CHANGED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_PLAYBACK_INFO_UPDATED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_INIT_STATUS, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_CONNECTING, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_CONNECTED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_DISCONNECTING, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SPEAKER_CONTROLLER_DISCONNECTED, self.__receive_system_event)


    def __receive_system_event(self, eventObj):
        Logger.log_debug("SpeakerControllerModule.__receive_system_event: " + str(eventObj))
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.get_capabilities(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.get_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_init(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            forceInit = request.get_arg("forceInit")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_init(pairedDeviceId, forceInit, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_speak(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            text = request.get_arg("text")
            serviceProvider = request.get_arg("serviceProvider")
            lang = request.get_arg("lang")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_speak(pairedDeviceId, text, 
                                                           serviceProvider=serviceProvider, lang=lang, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_start(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            url = request.get_arg("url")
            name = request.get_value("name")
            album = request.get_value("album")
            artist = request.get_value("artist")
            albumArt = request.get_value("albumArt")
            urlDetails = request.get_value("urlDetails")
            urlFormat = request.get_value("urlFormat")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_start(pairedDeviceId, url, name, album, artist, albumArt, urlDetails, urlFormat, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_pause(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_pause(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_resume(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_resume(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_stop(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_stop(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_mute_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.get_mute_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_mute_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            mute = request.get_arg("mute")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_mute_status(pairedDeviceId, mute, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_volume(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.get_volume(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_volume(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            volume = request.get_arg("volume")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.set_volume(pairedDeviceId, volume, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_now_playing_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = SpeakerControllerService.get_now_playing_status(pairedDeviceId, language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

