##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
#    Xuan Automation Application is free software: you can redistribute it and/or modify
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
#    along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.dimmerControllerService import DimmerControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sys import Sys


class DimmerControllerModule(Module):
    '''
    Switch Controller Class
    '''

    def __init__(self, kbxModuleName, parentPath):
        '''
        Constructor
        '''
        super().__init__(kbxModuleName, parentPath)

        self.register_method(kbxMethodName="get_capabilities",
                             kbxMethodFunc=self.get_capabilities,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_status",
                             kbxMethodFunc=self.get_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxparamIsRequired=True)])

        self.register_method(kbxMethodName="set_on",
                             kbxMethodFunc=self.set_on,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_off",
                             kbxMethodFunc=self.set_off,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamisRequired=True)])

        self.register_method(kbxMethodName="set_dim_level",
                             kbxMethodFunc=self.set_dim_level,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="level", kbxParamIsRequired=True, kbxParamMinValue=0, kbxParamMaxValue=99, kbxParamStep=1)])

        self.register_method(kbxMethodName="get_dim_level",
                             kbxMethodFunc=self.get_dim_level,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_dimmer_status",
                             kbxMethodFunc=self.get_dimmer_status,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

    def on_system_connected(self):
        self.register_event_listener(Event.EVENT_DIMMER_CONTROLLER_STATE_CHANGED, self.__receive_system_event)

    def __receive_system_event(self, eventObj):
        Logger.log_debug("DimmerControllerModule.__receive_system_event: ", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.get_capabilities(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.get_status(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_on(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.set_on(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_off(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.set_off(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_dim_level(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            level = request.get_arg("level")
            returnStr = DimmerControllerService.set_dim_level(pairedDeviceId, level)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_dim_level(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.get_dim_level(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_dimmer_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DimmerControllerService.get_dimmer_status(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)