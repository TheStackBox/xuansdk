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

class TTSService(object):

    MODULE_NAME = "tts_module"

    @staticmethod
    def speak(text, pairedDeviceId, lang="en", serviceProvider="google", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Speak a given piece of text.
        text:String :- Words to tts.
        pairedDeviceId:Number :- Paired id from get_paired_device_list
        lang:String :- Language of the speech.
        serviceProvider:String :- Either "google" or "baidu".
        return:Dictionary : eg- {"success":true}
        '''
        pass

    @staticmethod
    def get_speech_url(text, lang="en", serviceProvider="google", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get speech url of given piece of text.
        text:String :- Words to tts.
        lang:String :- Language of the speech.
        serviceProvider:String :- Either "google" or "baidu".
        return:Dictionary : eg- {"speechUrl":"http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=hello"}
        '''
        pass

