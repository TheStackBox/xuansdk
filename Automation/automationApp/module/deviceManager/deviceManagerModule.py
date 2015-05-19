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

import json
import urllib.parse

from automationApp.module.deviceManager.dimmerControllerModule import DimmerControllerModule
from automationApp.module.deviceManager.dimmerStepperControllerModule import DimmerStepperControllerModule
from automationApp.module.deviceManager.doorLockControllerModule import DoorLockControllerModule
from automationApp.module.deviceManager.hornControllerModule import HornControllerModule
from automationApp.module.deviceManager.hueControllerModule import HueControllerModule
from automationApp.module.deviceManager.ipCameraControllerModule import IPCameraControllerModule
from automationApp.module.deviceManager.mediaPlayerControllerModule import MediaPlayerControllerModule
from automationApp.module.deviceManager.powerStripControllerModule import PowerStripControllerModule
from automationApp.module.deviceManager.sensorControllerModule import SensorControllerModule
from automationApp.module.deviceManager.speakerControllerModule import SpeakerControllerModule
from automationApp.module.deviceManager.switchControllerModule import SwitchControllerModule
from automationApp.module.deviceManager.switchNoStatusControllerModule import SwitchNoStatusControllerModule
from automationApp.module.deviceManager.thermostatControllerModule import ThermostatControllerModule
from automationApp.module.deviceManager.trackerControllerModule import TrackerControllerModule
from automationApp.module.deviceManager.virtualActivityControllerModule import VirtualActivityControllerModule
from automationApp.module.deviceManager.virtualRemoteControllerControlModule import VirtualRemoteControlControllerModule
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.event import Event
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxRange import KBXRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.manager.deviceManagerService import DeviceManagerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


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
        self.register_module(MediaPlayerControllerModule("media_player_controller", self.get_abs_module_path()))
        self.register_module(PowerStripControllerModule("power_strip_controller", self.get_abs_module_path()))
        self.register_module(SensorControllerModule("sensor_controller", self.get_abs_module_path()))
        self.register_module(SpeakerControllerModule("speaker_controller", self.get_abs_module_path()))
        self.register_module(SwitchControllerModule("switch_controller", self.get_abs_module_path()))
        self.register_module(SwitchNoStatusControllerModule("switch_no_status_controller", self.get_abs_module_path()))
        self.register_module(TrackerControllerModule("tracker_controller", self.get_abs_module_path()))
        self.register_module(ThermostatControllerModule("thermostat_controller", self.get_abs_module_path()))
        self.register_module(VirtualRemoteControlControllerModule("virtual_remote_control_controller", self.get_abs_module_path()))
        self.register_module(VirtualActivityControllerModule("virtual_activity_controller", self.get_abs_module_path()))
        
        
        self.register_method(kbxMethodName="set_paired_devices_scan",
                             kbxMethodFunc=self.set_paired_devices_scan,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_supported_protocol_list",
                             kbxMethodFunc=self.get_supported_protocol_list)

        self.register_method(kbxMethodName="set_device_scan",
                             kbxMethodFunc=self.set_device_scan,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="rescan", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="data", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_scan_stop",
                             kbxMethodFunc=self.set_device_scan_stop,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="data", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_device_list",
                             kbxMethodFunc=self.get_device_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXString(kbxParamName="data", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_pair",
                             kbxMethodFunc=self.set_device_pair,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="deviceId", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="locationId", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_paired_device_list",
                             kbxMethodFunc=self.get_paired_device_list,
                             kbxMethodParams=[KBXRange(kbxParamName="offset", kbxParamMinValue=1, kbxParamMaxValue=1000, kbxParamStep=1, kbxParamDefaultValue=1, kbxParamDecimal=False),
                                              KBXRange(kbxParamName="limit", kbxParamMinValue=1, kbxParamMaxValue=50, kbxParamStep=1, kbxParamDefaultValue=50, kbxParamDecimal=False),
                                              KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="deviceTypeId", kbxParamIsRequired=False),
                                              KBXBoolean(kbxParamName="enable", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="locationId", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="set_device_unpair",
                             kbxMethodFunc=self.set_device_unpair,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="set_device_unpair_abort",
                             kbxMethodFunc=self.set_device_unpair_abort,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_group_unpair",
                             kbxMethodFunc=self.set_group_unpair,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True),
                                              KBXNumber(kbxParamName="groupId", kbxParamIsRequired=True)])

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
                                              KBXString(kbxParamName="statusUnit", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="locationId", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="get_device_type_list",
                             kbxMethodFunc=self.get_device_type_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="protocolId", kbxParamIsRequired=True)])

        self.register_method(kbxMethodName="get_advanced_control_list",
                             kbxMethodFunc=self.get_advanced_control_list,
                             kbxMethodParams=[KBXNumber(kbxParamName="pairedDeviceId", kbxParamIsRequired=True)])
        
        self.register_method(kbxMethodName="set_advanced_setting",
                             kbxMethodFunc=self.set_advanced_setting)

    def post_system_connected(self):
        super().post_system_connected()
        
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
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_FAIL, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_USER_INPUT_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_INSTEON_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_INSTEON_HUB_AUTHENTICATION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_INSTEON_HUB_AUTHENTICATION_TIMEOUT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_SCAN_DEVICE_USER_ACTION_TIMEOUT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_INSTEON_HUB_ACCESS_TIMEOUT, self.__receive_system_event)
        
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
        self.register_event_listener(Event.EVENT_PAIR_DEVICE_ERROR_AUTHENTICATION_FAIL, self.__receive_system_event)

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
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.set_paired_devices_scan(pairedDeviceId=pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    '''
    Driver Method
    '''
    def get_supported_protocol_list(self, request):
        try:
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.get_supported_protocol_list(language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_device_scan(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.set_device_scan(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_device_scan_stop(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.set_device_scan_stop(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_device_list(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.get_device_list(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
    
    def get_device_type_list(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.get_device_type_list(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def set_device_pair(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.set_device_pair(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    '''
    Device Method
    '''
    def set_device_unpair(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.set_device_unpair(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def set_device_unpair_abort(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.set_device_unpair_abort(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
      
    def set_group_unpair(self, request):
        try:
            args = request.get_all_args()
            returnStr = DeviceManagerService.set_group_unpair(**args)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def get_paired_device_list(self, request):
        try:
            offset = request.get_arg("offset")
            limit = request.get_arg("limit")
            protocolId = request.get_arg("protocolId")
            deviceTypeId = request.get_arg("deviceTypeId")
            enable = request.get_arg("enable")
            locationId = request.get_arg("locationId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.get_paired_device_list(offset, limit, protocolId=protocolId, deviceTypeId=deviceTypeId, enable=enable, language=language, locationId=locationId)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_paired_device_info(self, request):
        try:
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            pairedDeviceId = request.get_arg("pairedDeviceId")
            returnStr = DeviceManagerService.get_paired_device_info(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

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
            locationId = request.get_arg("locationId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.set_paired_device_info(pairedDeviceId, name, description, typeId, groupId, icon, status, statusUnit, locationId=locationId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

    def get_advanced_control_list(self, request):
        try:
            pairedDeviceId = request.get_arg("pairedDeviceId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            returnStr = DeviceManagerService.get_advanced_control_list(pairedDeviceId, language=language)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)
            
    def set_advanced_setting(self, request):
        try:
            contentRaw = request.get_post_data()
            contentDecoded = contentRaw.decode("utf-8")
            contentDecoded = urllib.parse.unquote_plus(contentDecoded)
            kwargs = {str(x[0]):str(x[1]) for x in (i.split("=", 1) for i in contentDecoded.split("&"))}
            
            params = json.loads(kwargs["kbxMethodParam"])
            params = {str(param["kbxParamName"]):param.get("kbxParamCurrentValue", None) for param in params}
            params["kbxMethodId"] = int(kwargs["kbxMethodId"])
            
            returnStr = SharedMethod.call_by_method_id(**params)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(se.value, request.requestId, se.value["returnValue"], se.value["returnMessage"])
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId, 1001)

