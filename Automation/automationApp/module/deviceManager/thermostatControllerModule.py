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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.thermostatControllerService import ThermostatControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class ThermostatControllerModule(Module):
    '''
    Thermostat Controller Class
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

        self.register_method(kbxMethodName="set_mode",
                             kbxMethodFunc=self.set_mode,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="mode", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_fan_mode",
                             kbxMethodFunc=self.set_fan_mode,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="fanMode", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_setpoint",
                             kbxMethodFunc=self.set_setpoint,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="mode", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="target", kbxParamIsRequired=True, kbxParamDecimal=1)])

    def on_system_connected(self):
        super().on_system_connected()
        #self.register_event_listener(Event.EVENT_SWITCH_CONTROLLER_STATE_CHANGED, self.__receive_system_event)

    def __receive_system_event(self, eventObj):
        Logger.log_debug("ThermostatControllerModule.__receive_system_event: " + str(eventObj))
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = ThermostatControllerService.get_capabilities(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = ThermostatControllerService.get_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_mode(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            mode = request.get_arg("mode")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = ThermostatControllerService.set_mode(pairedDeviceId, mode, language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":"Unknown Error: " + str(e)}, request.requestId, 1)

    def set_fan_mode(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            fanMode = request.get_arg("fanMode")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = ThermostatControllerService.set_fan_mode(pairedDeviceId, fanMode, language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_setpoint(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            mode = request.get_arg("mode")
            target = request.get_arg("target")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = ThermostatControllerService.set_setpoint(pairedDeviceId, mode, target, language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)