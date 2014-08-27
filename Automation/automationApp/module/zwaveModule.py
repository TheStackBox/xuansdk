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
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.zwaveService import ZWaveService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sys import Sys


class ZWaveModule(Module):


    def __init__(self, kbxModuleName, parentPath):
        super().__init__(kbxModuleName, parentPath)

        self.register_method(kbxMethodName="reset",
                             kbxMethodFunc=self.reset,
                             kbxMethodLabel="Reset",
                             kbxMethodDesc="Reset")

        self.register_method(kbxMethodName="network_add",
                             kbxMethodFunc=self.network_add,
                             kbxMethodLabel="networkAdd",
                             kbxMethodDesc="networkAdd")

        self.register_method(kbxMethodName="network_remove",
                             kbxMethodFunc=self.network_remove,
                             kbxMethodLabel="networkRemove",
                             kbxMethodDesc="networkRemove")

        self.register_method(kbxMethodName="network_abort",
                             kbxMethodFunc=self.network_abort,
                             kbxMethodLabel="Abort Add and Remove",
                             kbxMethodDesc="Abort add and remove")

        self.register_method(kbxMethodName="network_list",
                             kbxMethodFunc=self.network_list,
                             kbxMethodLabel="List Node",
                             kbxMethodDesc="List node")

        self.register_method(kbxMethodName="network_update",
                             kbxMethodFunc=self.network_update,
                             kbxMethodLabel="Network Update",
                             kbxMethodDesc="Network update")

        self.register_method(kbxMethodName="network_learn",
                             kbxMethodFunc=self.network_learn,
                             kbxMethodLabel="Network Learn",
                             kbxMethodDesc="Network learn")

        self.register_method(kbxMethodName="basic_get",
                             kbxMethodFunc=self.basic_get,
                             kbxMethodLabel="Basic Get",
                             kbxMethodDesc="Basic get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="basic_set",
                             kbxMethodFunc=self.basic_set,
                             kbxMethodLabel="Basic Set",
                             kbxMethodDesc="Basic set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="value", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="door_lock_get",
                             kbxMethodFunc=self.door_lock_get,
                             kbxMethodLabel="Door Lock Get",
                             kbxMethodDesc="Door lock get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="door_lock_set",
                             kbxMethodFunc=self.door_lock_set,
                             kbxMethodLabel="Door Lock Set",
                             kbxMethodDesc="Door lock set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="value", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="battery_get",
                             kbxMethodFunc=self.battery_get,
                             kbxMethodLabel="Battery Get",
                             kbxMethodDesc="Battery get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="switch_multilevel_get",
                             kbxMethodFunc=self.switch_multilevel_get,
                             kbxMethodLabel="Switch Multilevel Get",
                             kbxMethodDesc="Switch multilevel get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="switch_multilevel_set",
                             kbxMethodFunc=self.switch_multilevel_set,
                             kbxMethodLabel="Switch Multilevel Set",
                             kbxMethodDesc="Switch multilevel set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="level", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="duration", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="switch_multilevel_start",
                             kbxMethodFunc=self.switch_multilevel_start,
                             kbxMethodLabel="Switch Multilevel Start",
                             kbxMethodDesc="Switch multilevel start",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="primarySwitchDirection", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="primaryStartLevel", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="secondarySwitchDirection", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="secondarySwitchStep", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="duration", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="switch_multilevel_stop",
                             kbxMethodFunc=self.switch_multilevel_stop,
                             kbxMethodLabel="Switch Multilevel Stop",
                             kbxMethodDesc="Switch multilevel stop",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="sensor_multilevel_get",
                             kbxMethodFunc=self.sensor_multilevel_get,
                             kbxMethodLabel="Sensor Multilevel Get",
                             kbxMethodDesc="Sensor multilevel get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="sensorType", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="unit", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="meter_capabilities_get",
                             kbxMethodFunc=self.meter_capabilities_get,
                             kbxMethodLabel="Meter Capabilities Get",
                             kbxMethodDesc="Meter capabilities get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="meter_get",
                             kbxMethodFunc=self.meter_get,
                             kbxMethodLabel="Meter Get",
                             kbxMethodDesc="Meter get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="unit", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="meter_reset",
                             kbxMethodFunc=self.meter_reset,
                             kbxMethodLabel="Meter Reset",
                             kbxMethodDesc="Meter reset",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="alarm_setup",
                             kbxMethodFunc=self.alarm_setup,
                             kbxMethodLabel="Alarm Setup",
                             kbxMethodDesc="Alarm setup",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="alarm_get",
                             kbxMethodFunc=self.alarm_get,
                             kbxMethodLabel="Alarm Get",
                             kbxMethodDesc="Alarm get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="vendorType", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="zwaveType", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="zwaveEvent", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="alarm_set",
                             kbxMethodFunc=self.alarm_set,
                             kbxMethodLabel="Alarm Set",
                             kbxMethodDesc="Alarm set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="zwaveType", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="status", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="alarm_supported_get",
                             kbxMethodFunc=self.alarm_supported_get,
                             kbxMethodLabel="Alarm Supported Get",
                             kbxMethodDesc="Alarm supported get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="alarm_supported_event_get",
                             kbxMethodFunc=self.alarm_supported_event_get,
                             kbxMethodLabel="Alarm Supported Event Get",
                             kbxMethodDesc="Alarm supported event get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="zwaveType", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="binary_sensor_get",
                             kbxMethodFunc=self.binary_sensor_get,
                             kbxMethodLabel="Binary Sensor Get",
                             kbxMethodDesc="Binary sensor get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="binary_switch_get",
                             kbxMethodFunc=self.binary_switch_get,
                             kbxMethodLabel="Binary Switch Get",
                             kbxMethodDesc="Binary switch get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="binary_switch_set",
                             kbxMethodFunc=self.binary_switch_set,
                             kbxMethodLabel="Binary Switch Set",
                             kbxMethodDesc="Binary switch set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="value", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="switch_multilevel_supported_get",
                             kbxMethodFunc=self.switch_multilevel_supported_get,
                             kbxMethodLabel="Switch Multilevel Supported Get",
                             kbxMethodDesc="Switch multilevel supported get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="sensor_multilevel_supported_get_sensor",
                             kbxMethodFunc=self.sensor_multilevel_supported_get_sensor,
                             kbxMethodLabel="Sensor Multilevel Supported Get Sensor",
                             kbxMethodDesc="Sensor multilevel supported get sensor",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="sensor_multilevel_supported_scale_get_scale",
                             kbxMethodFunc=self.sensor_multilevel_supported_scale_get_scale,
                             kbxMethodLabel="Sensor Multilevel Supported Scale Get Scale",
                             kbxMethodDesc="Sensor multilevel supported scale get scale",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="scaleType", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="wakeup_get",
                             kbxMethodFunc=self.wakeup_get,
                             kbxMethodLabel="Wakeup Get",
                             kbxMethodDesc="Wakeup get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="wakeup_set",
                             kbxMethodFunc=self.wakeup_set,
                             kbxMethodLabel="Wakeup Set",
                             kbxMethodDesc="Wakeup set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="receiveNode", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="interval", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="configuration_get",
                             kbxMethodFunc=self.configuration_get,
                             kbxMethodLabel="Configuration Get",
                             kbxMethodDesc="Configuration Get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="parameter", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="configuration_set",
                             kbxMethodFunc=self.configuration_set,
                             kbxMethodLabel="Configuration Set",
                             kbxMethodDesc="Configuration Set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="parameter", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="size", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="default", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="value", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="user_number_get",
                             kbxMethodFunc=self.user_number_get,
                             kbxMethodLabel="User Number Get",
                             kbxMethodDesc="User number get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="user_code_set",
                             kbxMethodFunc=self.user_code_set,
                             kbxMethodLabel="User Code Set",
                             kbxMethodDesc="User code set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="user", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="status", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="code", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="user_code_get",
                             kbxMethodFunc=self.user_code_get,
                             kbxMethodLabel="User Code Get",
                             kbxMethodDesc="User code get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="user", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="association_groupings_get",
                             kbxMethodFunc=self.association_groupings_get,
                             kbxMethodLabel="Association Groupings Get",
                             kbxMethodDesc="Association groupings get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="association_specific_group_get",
                             kbxMethodFunc=self.association_specific_group_get,
                             kbxMethodLabel="Association Specific Groupings Get",
                             kbxMethodDesc="Association specific groupings get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="association_get",
                             kbxMethodFunc=self.association_get,
                             kbxMethodLabel="Association Get",
                             kbxMethodDesc="Association get",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="group", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="association_set",
                             kbxMethodFunc=self.association_set,
                             kbxMethodLabel="Association Set",
                             kbxMethodDesc="Association set",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="group", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="setNode", kbxParamIsRequired=False)])

        self.register_method(kbxMethodName="association_remove",
                             kbxMethodFunc=self.association_remove,
                             kbxMethodLabel="Association Remove",
                             kbxMethodDesc="Association remove",
                             kbxMethodParams=[KBXString(kbxParamName="node", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="group", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="removeNode", kbxParamIsRequired=False)])

    def on_system_connected(self):
        self.register_event_listener(Event.EVENT_ZWAVE_NETWORK_ADD_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NETWORK_REMOVE_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NETWORK_LEARN_USER_ACTION_REQUIRED, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NETWORK_REMOVE_FAILED_NODE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NETWORK_STATUS, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NODE_STATUS, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NODE_INFO_UPDATE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_TRANSMIT_STATUS, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_BASIC_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_GENERIC_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_METER_CAPABILITIES_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_METER_GET_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_LOCK_OPERATION_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_BATTERY_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_ALARM_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SENSOR_MULTILEVEL_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_BINARY_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SENSOR_MULTILEVEL_SUPPORTED_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SENSOR_MULTILEVEL_UNIT_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_CONFIGURATION_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_USER_CODE_SUPPORT_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_USER_CODE_GET_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_GROUP_SUPPORTED_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_GROUP_ACTIVE_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_GROUP_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SWITCH_MULTILEVEL_START_CHANGE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SWITCH_MULTILEVEL_STOP_CHANGE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_SWITCH_MULTILEVEL_SUPPORTED_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_MULTILEVEL_SENSOR_SUPPORTED_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_MULTILEVEL_SENSOR_UNIT_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_WAKEUP_CAPABILITIES_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_RESPONSE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_FAN_MODE_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_FAN_STATE_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_MODE_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_MODE_SUPPORTED_REPORT_RESPONSE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_OPERATING_STATE_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_SETBACK_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_SETPOINT_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_THERMOSTAT_SETPOINT_SUPPORTED_REPORT_RESPONSE, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_BINARY_SENSOR_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_NEIGHBOR_UPDATE_STATUS, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_ALARM_SUPPORTED_REPORT, self.__receive_system_event)
        self.register_event_listener(Event.EVENT_ZWAVE_UNKNOWN, self.__receive_system_event)


    def __receive_system_event(self, eventObj):
        Logger.log_debug("ZwaveModule.__receive_system_event: " + str(eventObj))
        self.send_web_server_event(eventObj["eventTag"], eventObj["eventData"])

    def reset(self, request):
        try:
            returnStr = ZWaveService.reset()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_add(self, request):
        try:
            returnStr = ZWaveService.network_add()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_remove(self, request):
        try:
            returnStr = ZWaveService.network_remove()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_abort(self, request):
        try:
            returnStr = ZWaveService.network_abort()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_list(self, request):
        try:
            returnStr = ZWaveService.network_list()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_update(self, request):
        try:
            returnStr = ZWaveService.network_update()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def network_learn(self, request):
        try:
            returnStr = ZWaveService.network_learn()
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def basic_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.basic_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def basic_set(self, request):
        try:
            node = request.get_arg("node")
            value = request.get_arg("value")
            returnStr = ZWaveService.basic_set(node, value)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def door_lock_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.door_lock_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def door_lock_set(self, request):
        try:
            node = request.get_arg("node")
            value = request.get_arg("value")
            returnStr = ZWaveService.door_lock_set(node, value)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def battery_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.battery_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def switch_multilevel_set(self, request):
        try:
            node = request.get_arg("node")
            level = request.get_arg("level")
            duration = request.get_arg("duration")
            returnStr = ZWaveService.switch_multilevel_set(node, level, duration)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def switch_multilevel_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.switch_multilevel_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def switch_multilevel_start(self, request):
        try:
            node = request.get_arg("node")
            primarySwitchDirection = request.get_arg("primarySwitchDirection")
            primaryStartLevel = request.get_arg("primaryStartLevel")
            secondarySwitchDirection = request.get_arg("secondarySwitchDirection")
            secondarySwitchStep = request.get_arg("secondarySwitchStep")
            duration = request.get_arg("duration")

            returnStr = ZWaveService.switch_multilevel_start(node, primarySwitchDirection, primaryStartLevel, secondarySwitchDirection, secondarySwitchStep, duration)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def switch_multilevel_stop(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.switch_multilevel_stop(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def sensor_multilevel_get(self, request):
        try:
            node = request.get_arg("node")
            sensorType = request.get_arg("sensorType")
            unit = request.get_arg("unit")
            returnStr = ZWaveService.sensor_multilevel_get(node, sensorType, unit)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def meter_capabilities_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.meter_capabilities_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def meter_get(self, request):
        try:
            node = request.get_arg("node")
            unit = request.get_arg("unit")
            returnStr = ZWaveService.meter_get(node, unit)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def meter_reset(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.meter_reset(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def alarm_setup(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.alarm_setup(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def alarm_set(self, request):
        try:
            node = request.get_arg("node")
            zwaveType = request.get_arg("zwaveType")
            status = request.get_arg("status")
            returnStr = ZWaveService.alarm_set(node, zwaveType, status)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def alarm_get(self, request):
        try:
            node = request.get_arg("node")
            vendorType = request.get_arg("vendorType")
            zwaveType = request.get_arg("zwaveType")
            zwaveEvent = request.get_arg("zwaveEvent")
            returnStr = ZWaveService.alarm_get(node, vendorType, zwaveType, zwaveEvent)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def alarm_supported_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.alarm_supported_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def alarm_supported_event_get(self, request):
        try:
            node = request.get_arg("node")
            zwaveType = request.get_arg("zwaveType")
            returnStr = ZWaveService.alarm_supported_event_get(node, zwaveType)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def binary_sensor_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.binary_sensor_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def binary_switch_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.binary_switch_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def binary_switch_set(self, request):
        try:
            node = request.get_arg("node")
            value = request.get_arg("value")
            returnStr = ZWaveService.binary_switch_set(node, value)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def switch_multilevel_supported_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.switch_multilevel_supported_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def sensor_multilevel_supported_get_sensor(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.sensor_multilevel_supported_get_sensor(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def sensor_multilevel_supported_scale_get_scale(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.sensor_multilevel_supported_get_sensor(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def wakeup_get(self, request):
        try:
            node = request.get_arg("node")
            scaleType = request.get_arg("scaleType")
            returnStr = ZWaveService.wakeup_get(node, scaleType)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def wakeup_set(self, request):
        try:
            node = request.get_arg("node")
            receiveNode = request.get_arg("receiveNode")
            interval = request.get_arg("interval")
            returnStr = ZWaveService.wakeup_set(node, receiveNode, interval)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def configuration_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.switch_multilevel_supported_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def configuration_set(self, request):
        try:
            node = request.get_arg("node")
            parameter = request.get_arg("parameter")
            size = request.get_arg("size")
            default = request.get_arg("default")
            value = request.get_arg("value")
            returnStr = ZWaveService.configuration_set(node, parameter, size, default, value)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def user_number_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.user_number_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def user_code_set(self, request):
        try:
            node = request.get_arg("node")
            user = request.get_arg("user")
            status = request.get_arg("status")
            code = request.get_arg("code")
            returnStr = ZWaveService.user_code_set(node, user, status, code)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def user_code_get(self, request):
        try:
            node = request.get_arg("node")
            user = request.get_arg("user")
            returnStr = ZWaveService.user_code_get(node, user)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def association_groupings_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.association_groupings_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def association_specific_group_get(self, request):
        try:
            node = request.get_arg("node")
            returnStr = ZWaveService.association_specific_group_get(node)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def association_get(self, request):
        try:
            node = request.get_arg("node")
            group = request.get_arg("group")
            returnStr = ZWaveService.association_get(node, group)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def association_set(self, request):
        try:
            node = request.get_arg("node")
            group = request.get_arg("group")
            setNode = request.get_arg("setNode")
            returnStr = ZWaveService.association_set(node, group, setNode)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)

    def association_remove(self, request):
        try:
            node = request.get_arg("node")
            group = request.get_arg("group")
            removeNode = request.get_arg("removeNode")
            returnStr = ZWaveService.association_remove(node, group, removeNode)
            self.send_response(returnStr, request.requestId)
        except SystemException as se:
            self.send_response(Sys.get_system_exception_return("en", se.value["returnValue"], se.value["returnMessage"]), request.requestId, se.value["returnValue"])
        except Exception as e:
            self.send_response({"error":"Unknown Error", "errMsg":str(e)}, request.requestId, 1)
