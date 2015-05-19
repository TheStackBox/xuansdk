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

from threading import current_thread

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.resource.languageLoader import LanguageLoader
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class KBXLang(object):

    SUPPORTED_LANG = LanguageLoader.list_supported_language()
    

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
        '''
        pass

    @staticmethod
    def get_preferred_lang():
        pass

    @staticmethod
    def enforce_preferred_lang(lang):
        '''
        If this is set, preferred and default lang will be override for entire process.
        Set it to None if you would like to cancel the enforce.
        '''
        pass

    def __init__(self, tag, func=None):
        pass

    def get_tag(self):
        pass

    def get_text(self, lang=None):
        pass

    def list_texts(self):
        '''
        Returns: {"en":"Text", "zh_s":"Text"}
        Same result as "for each supported $lang, get_text($lang).
        '''
        pass

