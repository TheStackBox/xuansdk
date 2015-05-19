##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
# Xuan Automation Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Automation Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

import urllib

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString

from com.cloudMedia.theKuroBox.sdk.service.deviceManager.virtualRemoteControlControllerService import VirtualRemoteControlControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class VirtualRemoteControlControllerModule(Module):
    '''
    Hue Controller Class
    '''

    def __init__(self, kbxModuleName, parentPath):
        '''
        Constructor
        '''
        super().__init__(kbxModuleName, parentPath)

        self.register_method(kbxMethodName="get_capabilities",
                             kbxMethodFunc=self.get_capabilities,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(
                                        kbxMethodName="get_all_keys",
                                        kbxMethodFunc=self.get_all_keys,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="set_key_info",
                                        kbxMethodFunc=self.set_key_info,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="keyId", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="data", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="add_page",
                                        kbxMethodFunc=self.add_page,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="pageName", kbxParamIsRequired=False),
                                                            KBXString(kbxParamName="info", kbxParamIsRequired=False)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="edit_page_info",
                                        kbxMethodFunc=self.edit_page_info,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="pageName", kbxParamIsRequired=False),
                                                            KBXString(kbxParamName="info", kbxParamIsRequired=False)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="remove_key",
                                        kbxMethodFunc=self.remove_key,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="keyId", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="remove_page",
                                        kbxMethodFunc=self.remove_page,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="set_keys_info",
                                        kbxMethodFunc=self.set_keys_info,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="keysData", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="record_key",
                                        kbxMethodFunc=self.record_key,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="keyId", kbxParamIsRequired=False)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="cancel_record_key",
                                        kbxMethodFunc=self.cancel_record_key,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="send_key",
                                        kbxMethodFunc=self.send_key,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXNumber(kbxParamName="pageNum", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="keyId", kbxParamIsRequired=True)
                                                        ]
                                     )
        
        self.register_method(
                                        kbxMethodName="edit_remote_info",
                                        kbxMethodFunc=self.edit_remote_info,
                                        kbxMethodParams=[
                                                            KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                            KBXString(kbxParamName="info", kbxParamIsRequired=False)
                                                        ]
                                     )


    def post_system_connected(self):
        super().post_system_connected()
        
        self.register_event_listener(Event.EVENT_VIRTUAL_REMOTE_CONTROL_KEY_CHANGED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_VIRTUAL_REMOTE_CONTROL_RECORD_KEY_ERROR, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_VIRTUAL_REMOTE_CONTROL_RECORD_KEY_FINISH, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_VIRTUAL_REMOTE_CONTROL_RECORD_KEY_START, self.__receive_system_event)

    def __receive_system_event(self, eventObj):
        Logger.log_debug("HueControllerModule.__receive_system_event: ", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = VirtualRemoteControlControllerService.get_capabilities(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_all_keys(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.get_all_keys(pairedDeviceId, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def set_key_info(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            keyId = request.get_value("keyId")
            data = request.get_value("data")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.set_key_info(pairedDeviceId, pageNum, keyId, data, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def add_page(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageName = request.get_value("pageName")
            info = request.get_value("info")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.add_page(pairedDeviceId, pageName, info, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
            
    def edit_page_info(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            pageName = request.get_value("pageName")
            info = request.get_value("info")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.edit_page_info(pairedDeviceId, pageNum, pageName, info, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    
    def remove_key(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            keyId = request.get_value("keyId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.remove_key(pairedDeviceId, pageNum, keyId, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
                
    def remove_page(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.remove_page(pairedDeviceId, pageNum, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def set_keys_info(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            contentRaw = request.get_post_data()
            contentDecoded = contentRaw.decode("utf-8")
            contentDecoded = urllib.parse.parse_qs(contentDecoded)
            
            keysData = contentDecoded.get("keysData")
            if keysData is not None and len(keysData) > 0:
                keysData = keysData[0]
                response = VirtualRemoteControlControllerService.set_keys_info(pairedDeviceId, pageNum, keysData, language)
                self.send_response(response, request.requestId)
            else:
                raise SystemException({ "returnValue":1002 })
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
        
    def record_key(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            keyId = request.get_value("keyId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.record_key(pairedDeviceId, pageNum, keyId, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def cancel_record_key(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.cancel_record_key(pairedDeviceId, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def send_key(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            pageNum = request.get_value("pageNum")
            keyId = request.get_value("keyId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.send_key(pairedDeviceId, pageNum, keyId, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    
    def edit_remote_info(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            info = request.get_value("info")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            response = VirtualRemoteControlControllerService.edit_remote_info(pairedDeviceId, info, language)
            self.send_response(response, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
               

