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

import time

class AppInfo(object):
    '''
    Store any app relate information
    '''

    '''
    Constant
    '''
    JSON_ENCODER_CLS = None

    REQUEST_TYPE_IPC = "ipc"
    REQUEST_TYPE_WEB = "web"

    REQUEST_KEY_LANGUAGE = "language"
    DEFAULT_API_LANGUAGE = "en"
    DEFAULT_API_TIMEOUT = 30

    @staticmethod
    def get_client_id():
        '''
        Get the unique process id
        '''
        pass

    @staticmethod
    def get_app_id():
        '''
        Get the app id
        '''
        pass

    @staticmethod
    def get_app_dir():
        '''
        Get the App Directory
        '''
        pass

    @staticmethod
    def get_app_status():
        '''
        Any while loop MUST call this method before doing its tasks
        '''
        pass

