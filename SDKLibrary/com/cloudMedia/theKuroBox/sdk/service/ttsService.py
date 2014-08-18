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
from com.cloudMedia.theKuroBox.service.ttsService import TTSService as TS

class TTSService(object):

    @staticmethod
    def speak(text, pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Speak a given piece of text.
        text:String :- Words to tts
        pairedDeviceId:Number :- Paired id from get_paired_device_list
        '''
        pass
    
        
    @staticmethod
    def get_speech_url(text, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get speech url of given piece of text.
        text:String :- Words to tts
        Returns:URL of the speech in string. eg http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=hello
        '''
        pass
    
        