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
from automationApp.module.ipCameraControllerModule import IPCameraControllerModule
from automationApp.module.dimmerControllerModule import DimmerControllerModule
from automationApp.module.dimmerStepperControllerModule import DimmerStepperControllerModule
from automationApp.module.doorLockControllerModule import DoorLockControllerModule
from automationApp.module.hornControllerModule import HornControllerModule
from automationApp.module.hueControllerModule import HueControllerModule
from automationApp.module.powerStripControllerModule import PowerStripControllerModule
from automationApp.module.sensorControllerModule import SensorControllerModule
from automationApp.module.speakerControllerModule import SpeakerControllerModule
from automationApp.module.switchControllerModule import SwitchControllerModule
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.deviceManager.deviceManagerService import DeviceManagerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sys import Sys


class DeviceManagerModule(Module):
    '''
    Device Manager Class
    '''
    __deviceManagerExecutor = None

    def __init__(self, kbxModuleName, parentPath):
        super().__init__(kbxModuleName, parentPath)

        self.register_module(DimmerControllerModule("dimmer_controller", self.get_abs_module_path()))
        self.register_module(DimmerStepperControllerModule("dimmer_stepper_controller", self.get_abs_module_path()))
        self.register_module(DoorLockControllerModule("door_lock_controller", self.get_abs_module_path()))
        self.register_module(HornControllerModule("horn_controller", self.get_abs_module_path()))
        self.register_module(HueControllerModule("hue_controller", self.get_abs_module_path()))
        self.register_module(IPCameraControllerModule("ip_camera_controller", self.get_abs_module_path()))
        self.register_module(PowerStripControllerModule("power_strip_controller", self.get_abs_module_path()))
        self.register_module(SensorControllerModule("sensor_controller", self.get_abs_module_path()))
        self.register_module(SpeakerControllerModule("speaker_controller", self.get_abs_module_path()))
        self.register_module(SwitchControllerModule("switch_controller", self.get_abs_module_path()))

        self.register_method(kbxMethodName="set_paired_devices_scan",
                             kbxMethodFunc=self.set_paired_devices_scan,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_supported_protocol_list",
                             kbxMethodFunc=self.get_supported_protocol_list)

        self.register_method(kbxMethodName="set_device_scan",
                             kbxMethodFunc=self.set_device_scan,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXBoolean(kbxParamName="rescan", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_scan_stop",
                             kbxMethodFunc=self.set_device_scan_stop,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_device_list",
                             kbxMethodFunc=self.get_device_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_device_pair",
                             kbxMethodFunc=self.set_device_pair,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="deviceId", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="pairInfo", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_pair_abort",
                             kbxMethodFunc=self.set_device_pair_abort,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_paired_device_list",
                             kbxMethodFunc=self.get_paired_device_list,
                             kbxMethodParams=[KBXRange(kbxParamName="offset", kbxParamMinValue=1, kbxParamMaxValue=1000, kbxParamStep=1, kbxParamDefaultValue=1, kbxParamDecimal=False),
                                              KBXRange(kbxParamName="limit", kbxParamMinValue=1, kbxParamMaxValue=50, kbxParamStep=1, kbxParamDefaultValue=50, kbxParamDecimal=False),
                                              KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="deviceTypeId", kbxParamIsRequired=False),
                                              KBXBoolean(kbxParamName="enable", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_unpair",
                             kbxMethodFunc=self.set_device_unpair,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_device_unpair_abort",
                             kbxMethodFunc=self.set_device_unpair_abort,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_paired_device_info",
                             kbxMethodFunc=self.get_paired_device_info,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_paired_device_info",
                             kbxMethodFunc=self.set_paired_device_info,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="name", kbxParamMinLength=1, kbxParamMaxLength=255, kbxParamIsRequired=True, kbxParamDefaultValue="Device Name"),
                                              KBXString(kbxParamName="description", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="typeId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="deviceGroupId", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="icon", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="status", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="statusUnit", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_device_type_list",
                             kbxMethodFunc=self.get_device_type_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXRange(kbxParamName="offset", kbxParamMinValue=1, kbxParamMaxValue=100, kbxParamStep=1, kbxParamIsRequired=False),
                                              KBXRange(kbxParamName="limit", kbxParamMinValue=1, kbxParamMaxValue=50, kbxParamStep=1, kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_device_control_module",
                             kbxMethodFunc=self.get_device_control_module,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

    def on_system_connected(self):
        self.register_event_listener(Event.EVENT_DEVICE_MANAGER_PROTOCOL_ENABLED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_DEVICE_MANAGER_PROTOCOL_DISABLED, self.__receive_system_event)

        self.register_event_listener(Event.EVENT_UPDATE_PAIRED_DEVICE_START, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIRED_DEVICE_ENABLED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIRED_DEVICE_DISABLED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_UPDATE_PAIRED_DEVICE_END, self.__receive_system_event)

        self.register_event_listener(Event.EVENT_SCAN_DEVICE_DONE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_STOP, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_ERROR_UNKNOWN, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_ERROR_EXIST, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_USER_INPUT_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_USER_ACTION_TIMEOUT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_ERROR_EXIST, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_ERROR_INVALID_PARAMETER, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_ERROR_UNKNOWN, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_ABORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_UNPAIR_DEVICE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_UNPAIR_DEVICE_ZWAVE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_UNPAIR_DEVICE_ERROR_UNKNOWN, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_UNPAIR_DEVICE_ABORT, self.__receive_system_event)

        self.register_event_listener(Event.EVENT_SCAN_DEVICE_UPNP_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_BLUETOOTH_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WEMO_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WIFI_PHILIP_HUE_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_ZWAVE_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_FOSCAM_HD_FOUND, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_RECEIVER_FOUND, self.__receive_system_event)


    '''
    Update Paired Devices Method
    '''
    def __receive_system_event(self, eventObj):
        Logger.log_debug("Automation DeviceManagerModule.__receive_system_event:", eventObj)
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def set_paired_devices_scan(self, request):
        try:
            pairedDeviceId = request.get_value("pairedDeviceId")
            returnStr = DeviceManagerService.set_paired_devices_scan(deviceId=pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    '''
    Driver Method
    '''
    def get_supported_protocol_list(self, request):
        try:
            returnStr = DeviceManagerService.get_supported_protocol_list()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_device_scan(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            rescan = request.get_arg("rescan")
            returnStr = DeviceManagerService.set_device_scan(protocolId, rescan)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_device_scan_stop(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            returnStr = DeviceManagerService.set_device_scan_stop(protocolId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_device_list(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            returnStr = DeviceManagerService.get_device_list(protocolId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_device_type_list(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            offset = request.get_arg("offset")
            limit = request.get_arg("limit")
            returnStr = DeviceManagerService.get_device_type_list(protocolId, offset, limit)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_device_pair(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            deviceId = request.get_arg("deviceId")
            pairInfo = request.get_arg("pairInfo")
            returnStr = DeviceManagerService.set_device_pair(protocolId, deviceId, pairInfo)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_device_pair_abort(self, request):
        try:
            protocolId = request.get_arg("protocolId")
            returnStr = DeviceManagerService.set_device_pair_abort(protocolId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    '''
    Device Method
    '''
    def set_device_unpair(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DeviceManagerService.set_device_unpair(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_device_unpair_abort(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DeviceManagerService.set_device_unpair_abort(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_paired_device_list(self, request):
        try:
            offset = request.get_arg("offset")
            limit = request.get_arg("limit")
            protocolId = request.get_arg("protocolId")
            deviceTypeId = request.get_arg("deviceTypeId")
            enable = request.get_arg("enable")
            returnStr = DeviceManagerService.get_paired_device_list(offset, limit, protocolId=protocolId, deviceTypeId=deviceTypeId, enable=enable)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_paired_device_info(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DeviceManagerService.get_paired_device_info(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def set_paired_device_info(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            name = request.get_arg("name")
            description = request.get_arg("description")
            typeId = request.get_arg("typeId")
            groupId = request.get_arg("deviceGroupId")
            icon = request.get_arg("icon")
            status = request.get_arg("status")
            statusUnit = request.get_arg("statusUnit")
            returnStr = DeviceManagerService.set_paired_device_info(pairedDeviceId, name, description, typeId, groupId, icon, status, statusUnit)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def get_device_control_module(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DeviceManagerService.get_device_control_module(pairedDeviceId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)
