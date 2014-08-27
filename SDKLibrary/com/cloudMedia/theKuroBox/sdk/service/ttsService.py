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
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo

class TTSService(object):

    @staticmethod
    def speak(text, pairedDeviceId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Speak a given piece of text.
        
        text:String - [Required] Text to speak out.
        pairedDeviceId:Number - [Required] Paired device id from get_paired_device_list
        language:String - [Optional] Preferred language. Default is en.
        '''
        pass
    
        
    @staticmethod
    def get_speech_url(text, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get speech url of given piece of text.
        
        text:String - [Required] Text to speak out.
        language:String - [Optional] Preferred language. Default is en.
        return:String :eg- {"value":"http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=hello"}
        '''
        pass
    
        