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
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxOption import KBXOption
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.IPCameraControllerService import IPCameraControllerService


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
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True), KBXBoolean(kbxParamName="isRemoteAccess", kbxParamTrueLabel="Yes", kbxParamFalseLabel="No", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="set_snapshot",
                             kbxMethodFunc=self.set_snapshot,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_snapshot_list",
                             kbxMethodFunc=self.get_snapshot_list,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="get_preset_angle_list",
                             kbxMethodFunc=self.get_preset_angle_list,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_preset_angle",
                             kbxMethodFunc=self.set_preset_angle,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="presetName", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_night_mode",
                             kbxMethodFunc=self.set_night_mode,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXBoolean(kbxParamName="mode", kbxParamTrueLabel="On", kbxParamFalseLabel="Off")])
        
        self.register_method(kbxMethodName="set_zoom_in",
                             kbxMethodFunc=self.set_zoom_in,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_zoom_out",
                             kbxMethodFunc=self.set_zoom_out,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])



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
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXOption(kbxParamName="moveTo", kbxParamItems=stateList, kbxParamDefaultValue=0, kbxParamMaxSize=1)])
        
        ''' KHLEE ADD : 20140902_1756 '''
        self.register_method(kbxMethodName="set_update_login",
                             kbxMethodFunc=self.set_update_login,
                             kbxMethodParams=[KBXString(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="username", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="password", kbxParamIsRequired=True)])
        ''' END ADD '''

    def get_capabilities(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.get_capabilities(pairedDeviceId, language=language) 
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_status(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.get_status(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_camera_stream_configuration(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            isRemoteAccess = request.get_value("isRemoteAccess")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.get_camera_stream_configuration(pairedDeviceId, isRemoteAccess, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_snapshot(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_snapshot(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_snapshot_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.get_snapshot_list(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_preset_angle_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.get_preset_angle_list(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_preset_angle(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            presetName = request.get_arg("presetName")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_preset_angle(pairedDeviceId, presetName, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_night_mode(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            mode = request.get_arg("mode")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_night_mode(pairedDeviceId, mode, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_zoom_in(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_zoom_in(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_zoom_out(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_zoom_out(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_camera_move(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            moveTo = request.get_arg("moveTo")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_camera_move(pairedDeviceId, moveTo, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def set_update_login(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            username = request.get_value("username")
            password = request.get_value("password")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = IPCameraControllerService.set_update_login(pairedDeviceId, username, password, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
