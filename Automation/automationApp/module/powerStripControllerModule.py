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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.powerStripControllerService import PowerStripControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sys import Sys


class PowerStripControllerModule(Module):
    '''
    Power Strip Controller Class
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
                             kbxMethodLabel="Turn On",
                             kbxMethodDesc="Turn on switch",
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                KBXString(kbxParamName="index", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_off",
                             kbxMethodFunc=self.set_off,
                             kbxMethodLabel="Turn Off",
                             kbxMethodDesc="Turn off switch",
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                                KBXString(kbxParamName="index", kbxParamIsRequired=False)])

    def on_system_connected(self):
        self.register_event_listener(Event.EVENT_POWER_STRIP_CONTROLLER_STATE_CHANGED, self.__receive_system_event)

    def __receive_system_event(self, eventObj):
        Logger.log_debug("PowerStripControllerModule.__receive_system_event: ", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = PowerStripControllerService.get_capabilities(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = PowerStripControllerService.get_status(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_on(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            index = request.get_value("index")
            returnStr = PowerStripControllerService.set_on(pairedDeviceId, index)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_off(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            index = request.get_value("index")
            returnStr = PowerStripControllerService.set_off(pairedDeviceId, index)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)
