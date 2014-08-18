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
import time
import random
import hashlib
import hmac
import base64
from com.cloudMedia.theKuroBox.sdk.util.httpUtil import HttpUtil
from com.cloudMedia.theKuroBox.sdk.util.util import Util

class OAuth():
    '''
    This is an OAuth class for generate oauth signature.
    '''
      
    @staticmethod
    def nonce():
        '''
        get oauth nonce.
        '''
        pass
    
    @staticmethod 
    def sort(ls):
        '''
        sort the list according alphabetical order.
        '''
        pass
    
    @staticmethod 
    def timestamp():
        '''
        get current timestamp.
        '''
        pass
    
    @staticmethod
    def create_signature(url, body="", _oauth_token="", _oauth_secret="", consumer_key="", consumer_secret="", http_method="POST"):
        '''
        return oauth signature, timestamp and nonce
        '''
        pass

