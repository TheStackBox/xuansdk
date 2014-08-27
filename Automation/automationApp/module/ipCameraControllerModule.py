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
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.IPCameraControllerService import IPCameraControllerService
from com.cloudMedia.theKuroBox.sys import Sys


class IPCameraControllerModule(Module):

    def __init__(self, kbxModuleName, parentPath):

        super(IPCameraControllerModule, self).__init__(kbxModuleName, parentPath)
        
        self.register_method(kbxMethodName="get_capabilities",
                             kbxMethodFunc=self.get_capabilities,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_status",
                             kbxMethodFunc=self.get_status,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxparamIsRequired=True)])

        self.register_method(kbxMethodName="get_camera_stream_configuration",
                             kbxMethodFunc=self.get_camera_stream_configuration,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_snapshot",
                             kbxMethodFunc=self.set_snapshot,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_snapshot_list",
                             kbxMethodFunc=self.get_snapshot_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_preset_angle_list",
                             kbxMethodFunc=self.get_preset_angle_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_preset_angle",
                             kbxMethodFunc=self.set_preset_angle,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="presetName", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_night_mode",
                             kbxMethodFunc=self.set_night_mode,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXBoolean(kbxParamName="mode", kbxParamTrueLabel="On", kbxParamFalseLabel="Off")])
        
        self.register_method(kbxMethodName="set_zoom_in",
                             kbxMethodFunc=self.set_zoom_in,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_zoom_out",
                             kbxMethodFunc=self.set_zoom_out,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])



        stateList = [{"kbxItemLabel":"LEFT", "kbxItemValue":0},
                     {"kbxItemLabel":"RIGHT", "kbxItemValue":1},
                     {"kbxItemLabel":"UP", "kbxItemValue":2},
                     {"kbxItemLabel":"DOWN", "kbxItemValue":3},
                     {"kbxItemLabel":"LEFT UP", "kbxItemValue":4},
                     {"kbxItemLabel":"RIGHT UP", "kbxItemValue":5},
                     {"kbxItemLabel":"LEFT DOWN", "kbxItemValue":6},
                     {"kbxItemLabel":"RIGHT DOWN", "kbxItemValue":7}]
                      
        self.register_method(kbxMethodName="set_camera_move",
                             kbxMethodFunc=self.set_camera_move,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXOption(kbxParamName="moveTo", kbxParamItems=stateList, kbxParamDefaultValue=0, kbxParamMaxSize=1)])

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.get_capabilities(pairedDeviceId) 
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.get_status(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_camera_stream_configuration(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.get_camera_stream_configuration(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_snapshot(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.set_snapshot(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_snapshot_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.get_snapshot_list(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_preset_angle_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.get_preset_angle_list(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_preset_angle(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            presetName = request.get_arg("presetName")
            returnStr = IPCameraControllerService.set_preset_angle(pairedDeviceId, presetName)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_night_mode(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            mode = request.get_arg("mode")
            returnStr = IPCameraControllerService.set_night_mode(pairedDeviceId, mode)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_zoom_in(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.set_zoom_in(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_zoom_out(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = IPCameraControllerService.set_zoom_out(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_camera_move(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            moveTo = request.get_arg("moveTo")
            returnStr = IPCameraControllerService.set_camera_move(pairedDeviceId, moveTo)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)
