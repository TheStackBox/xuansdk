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
from threading import current_thread

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.resource.languageLoader import LanguageLoader
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class KBXLang(object):

    @staticmethod
    def set_default_lang(lang):
        '''
        Set the default language to use if preferred language is not available.
        '''
        pass

    @staticmethod
    def set_preferred_lang(lang):
        '''
        This is a per-thread language setting.
        It is set to the language as received in argument "language" by default.

        Params:
        lang:String - [Required] The preferred language.
        '''
        pass

    def __init__(self, tag, func=None):
        '''
        Create a new instance of language string.

        Params:
        tag:String - [Required] The name of the key of the element which holds the translated text in "resources/languages/" json files.
        func:Callable - [Optional] Additional statements to be called each time translated text is requested.
        The function receive a string argument which is the translated text; and must returns a string value.
        '''
        pass


    def get_text(self, lang=None):
        '''
        You can get translated text for the language you specified through this method. This method is synonym to str().

        Params:
        lang:String - [Optional] Specify the language for the text to be retrieved. It uses preferred language by default.

        Returns:
        Translated text.

        * str() always return you translated text in preferred language.
        '''
        pass
