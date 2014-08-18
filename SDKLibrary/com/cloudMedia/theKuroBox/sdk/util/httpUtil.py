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
import urllib.request
import http.server
from urllib.error import URLError, HTTPError

class HttpUtil(object):
    
    
    @staticmethod
    def url_encode(data=""):
        '''
        url encode the data
        '''
        pass
    

    @staticmethod
    def send_load(_url, method="GET", _data=None, _timeout=30, val={'header':{},'encode_method':'utf-8'}):
        '''
        Use http method to send data to server.
        _url = the url to be call
        method = the http method to be use. eg. GET, POST ..
        _data = the data to be send. (for HTTP POST, PUSH ...)
        _timeout= the session will be hold.
        val = the object to stored the header and data encode method
            = header: http header
            = encode method: fixed to utf-8
        '''
        pass
    