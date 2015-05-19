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

import json

from com.cloudMedia.theKuroBox.sdk.util.logger import Logger

class LanguageLoader(object):

    LANG_RESOURCES = {}

    @staticmethod
    def get_resource_instance(lang):
        pass

    @staticmethod
    def list_supported_language():
        pass

class LanguageResource(object):

    #===========================================================================
    # Modify only these set of code to add new language
    #===========================================================================
    EN = "en"
    ZH_S = "zh_s"

    @staticmethod
    def list_supported_language():
        pass

    def __init__(self, lang):
        pass

    def get_text(self, tag):
        pass

