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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxColor import KBXColor
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.hueControllerService import HueControllerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sys import Sys


class HueControllerModule(Module):
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

        self.register_method(kbxMethodName="get_status",
                             kbxMethodFunc=self.get_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxparamIsRequired=True)])

        self.register_method(kbxMethodName="set_on",
                             kbxMethodFunc=self.set_on,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_off",
                             kbxMethodFunc=self.set_off,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_brightness",
                             kbxMethodFunc=self.set_brightness,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="brightness", kbxParamMinValue=0, kbxParamMaxValue=255, kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_hue",
                             kbxMethodFunc=self.set_hue,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="hue", kbxParamIsRequired=True, kbxParamMinValue=0, kbxParamMaxValue=65535),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_saturation",
                             kbxMethodFunc=self.set_saturation,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="saturation", kbxParamMinValue=0, kbxParamMaxValue=255, kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_color_rgb",
                             kbxMethodFunc=self.set_color_rgb,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXColor(kbxParamName="color", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_color_temperature",
                             kbxMethodFunc=self.set_color_temperature,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="ct", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="transitionTime", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_hue_state",
                             kbxMethodFunc=self.get_hue_state,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

    def on_system_connected(self):
        self.register_event_listener(Event.EVENT_HUE_CONTROLLER_STATE_CHANGED, self.__receive_system_event)

    def __receive_system_event(self, eventObj):
        Logger.log_debug("HueControllerModule.__receive_system_event: ", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = HueControllerService.get_capabilities(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = HueControllerService.get_status(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_on(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_on(pairedDeviceId, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_off(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_off(pairedDeviceId, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_brightness(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            brightness = request.get_arg("brightness")
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_brightness(pairedDeviceId, brightness, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_hue(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            hue = request.get_arg("hue")
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_hue(pairedDeviceId, hue, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_saturation(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            saturation = request.get_arg("saturation")
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_saturation(pairedDeviceId, saturation, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_color_rgb(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            color = request.get_value("color")
            r = color.get_red()
            g = color.get_green()
            b = color.get_blue()
            transitionTime = request.get_value("transitionTime")
            returnStr = HueControllerService.set_color_rgb(pairedDeviceId, r, g, b, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_color_temperature(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            transitionTime = request.get_value("transitionTime")
            ct = request.get_arg("ct")
            returnStr = HueControllerService.set_color_temperature(pairedDeviceId, ct, transitionTime)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_hue_state(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = HueControllerService.get_hue_state(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

