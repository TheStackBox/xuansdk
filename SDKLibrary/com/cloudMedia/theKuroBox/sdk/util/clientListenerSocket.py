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

import select
import socket
from threading import Thread
import time
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException

class ClientListenerSocket(Thread):
    '''
    This class is a thread which will connect to an IP endpoint to listen any incoming message 
    '''
    

    
    '''
    Event fired when the socket is successfully connected.
    Data Dictionary Content: EVENT_DATA_KEY_TAG
    '''
    EVENT_TAG_SOCKET_CONNECTED = "EVENT_SOCKET_CONNECTED"
    
    '''
    Event fired when the socket is disconnected.
    Data Dictionary Content: EVENT_DATA_KEY_TAG, EVENT_DATA_KEY_ERROR_CODE (if any), EVENT_DATA_KEY_EXCEPTION (if any)
    '''
    EVENT_TAG_SOCKET_DISCONNECTED = "EVENT_SOCKET_DISCONNECTED"
    
    '''
    Event fired when there is any error occurred.
    Data Dictionary Content: EVENT_DATA_KEY_TAG, EVENT_DATA_KEY_ERROR_CODE, EVENT_DATA_KEY_EXCEPTION
    '''
    EVENT_TAG_SOCKET_ERROR = "EVENT_SOCKET_ERROR"
    
    '''
    Event fired when the socket is receiving message.
    Data Dictionary Content: EVENT_DATA_KEY_TAG, EVENT_DATA_KEY_DATA
    '''
    EVENT_TAG_SOCKET_DATA = "EVENT_SOCKET_DATA"
    
    
    '''
    Event Tag key for eventData object when event is fired
    Content: String which is the same value as eventTag
    '''
    EVENT_DATA_KEY_TAG = "eventTag"
    
    '''
    Error code key for eventData object when event is fired
    Content: String which describe the error code
    '''
    EVENT_DATA_KEY_ERROR_CODE = "errorCode"
    
    '''
    Message data key for eventData object when event is fired
    Content: Raw bytes which is not decoded.
    '''
    EVENT_DATA_KEY_DATA = "data"
    
    '''
    Exception object key for eventData object when event is fired
    Content: Exception object
    '''
    EVENT_DATA_KEY_EXCEPTION = "exception" 
        
    '''
    Error when cannot create socket object
    '''
    ERROR_CODE_UNABLE_TO_CREATE_SOCKET = "1001"
    
    '''
    Error when provided port is invalid
    '''
    ERROR_CODE_INVALID_PORT = "1002"
    
    '''
    Error when fail to create a connection to the host
    '''
    ERROR_CODE_CONNECTION_ERROR = "1003"
    
    '''
    Error when fail to receive data
    '''
    ERROR_CODE_RECEIVE_DATA_ERROR = "1004"
    
    
    def __init__(self, host, port, callback, bufferSize=4096):
        '''
        Construct a thread object to start the message listening
        1. host:String          - The host to connect to
        2. port:int             - The port to connect to
        3. callback:Function    - The callback function for any event happened which receives a dictionary object with following keys
                                    a. eventTag:String         - The event tag
                                    b. eventData:Dict          - The data associated to the event
                                    c. socket:socket           - The socket object being used
        4. bufferSize:int (optional)        - The size of buffer per read. Default is 4096
                                    
        '''
        pass

    def terminate(self):
        '''
        Terminate the thread.
        '''
        pass

    def run(self):
        '''
        Run the thread
        '''
        pass

