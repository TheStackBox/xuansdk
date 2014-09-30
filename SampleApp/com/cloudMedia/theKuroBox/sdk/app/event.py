##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
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
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
class Event(object):
### BEGIN
    ### Application Manager
    '''
    Raise when application is starting.
    eventData:{}
    '''
    EVENT_APP_LAUNCH_STARTING = "APP_LAUNCH_STARTING"
    '''
    Raise when application is launch completed.
    eventData:{}
    '''
    EVENT_APP_LAUNCH_COMPLETE = "APP_LAUNCH_COMPLETE"
    '''
    Raise when application is exit.
    eventData:{}
    '''
    EVENT_APP_EXIT = "APP_EXIT"
    '''
    Raise when application is installed.
    eventData:{}
    '''
    EVENT_APP_INSTALL_COMPLETED = "APP_INSTALL_COMPLETED"
    '''
    Raise when application is uninstalled.
    eventData:{}
    '''
    EVENT_APP_UNINSTALL_COMPLETED = "APP_UNINSTALL_COMPLETED"
    '''
    Raise when application process is terminated.
    eventData:{}
    '''
    EVENT_SYSTEM_PROCESS_TERMINATE = "SYSTEM_PROCESS_TERMINATE"
    ### 
    
    ### Driver Manager
    '''
    Raise when driver is up
    eventData:{}
    '''
    EVENT_DRIVER_UP = "DRIVER_UP"
    '''
    Raise when driver is down
    eventData:{}
    '''
    EVENT_DRIVER_DOWN = "DRIVER_DOWN"
    ### 

    ### Device Manager
    '''
    Raise when a protocol is enabled
    eventData:{}
    '''
    EVENT_DEVICE_MANAGER_PROTOCOL_ENABLED = "DEVICE_MANAGER_PROTOCOL_ENABLED"
    '''
    Raise when a protocol is disabled
    eventData:{}
    '''
    EVENT_DEVICE_MANAGER_PROTOCOL_DISABLED = "DEVICE_MANAGER_PROTOCOL_DISABLED"
    '''
    Raise when pair device is started
    eventData:{}
    '''
    EVENT_UPDATE_PAIRED_DEVICE_START = "UPDATE_PAIRED_DEVICE_START"
    '''
    Raise when pair device is enabled
    eventData:{}
    '''
    EVENT_PAIRED_DEVICE_ENABLED = "PAIRED_DEVICE_ENABLED"
    '''
    Raise when pair device is disabled
    eventData:{}
    '''
    EVENT_PAIRED_DEVICE_DISABLED = "PAIRED_DEVICE_DISABLED"
    '''
    Raise when pair device is finished
    eventData:{}
    '''
    EVENT_UPDATE_PAIRED_DEVICE_END = "UPDATE_PAIRED_DEVICE_DONE"
    '''
    Raise when devices is scanned
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_DONE = "SCAN_DEVICE_DONE"
    '''
    Raise when scan devices process is stopped
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_STOP = "SCAN_DEVICE_STOP"
    '''
    Raise when scan devices process unknown error occured.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_ERROR_UNKNOWN = "SCAN_DEVICE_ERROR_UNKNOWN"
    '''
    Raise when scan devices process error exist.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_ERROR_EXIST = "SCAN_DEVICE_ERROR_EXIST"
    '''
    Raise when zwave device request user action during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED = "SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED"
    '''
    Raise when zwave device user action is detected during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_ZWAVE_USER_ACTION_DETECTED = "SCAN_DEVICE_ZWAVE_USER_ACTION_DETECTED"
    '''
    Raise when x10 device request user action during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_X10_USER_ACTION_REQUIRED = "SCAN_DEVICE_X10_USER_ACTION_REQUIRED"
    '''
    Raise when x10 device user action is detected during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_X10_USER_ACTION_DETECTED = "SCAN_DEVICE_X10_USER_ACTION_DETECTED"
    '''
    Raise when x10 device request user input during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_X10_USER_INPUT_REQUIRED = "SCAN_DEVICE_X10_USER_INPUT_REQUIRED"
    '''
    Raise when x10 device request setup during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED = "SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED"
    '''
    Raise when wifi philiphue request user action during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED = "SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED"
    '''
    Raise when wifi philiphue user action is detected during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED = "SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED"
    '''
    Raise when user action is timeout during scanning process.
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_USER_ACTION_TIMEOUT = "SCAN_DEVICE_USER_ACTION_TIMEOUT"
    '''
    Raise when upnp is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_UPNP_FOUND = "SCAN_DEVICE_UPNP_FOUND"
    '''
    Raise when bluetooth device is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_BLUETOOTH_FOUND = "SCAN_DEVICE_BLUETOOTH_FOUND"
    '''
    Raise when wemo device is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_WEMO_FOUND = "SCAN_DEVICE_WEMO_FOUND"
    '''
    Raise when wifi philip hue is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_WIFI_PHILIP_HUE_FOUND = "SCAN_DEVICE_WIFI_PHILIP_HUE_FOUND"
    '''
    Raise when zwave device is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_ZWAVE_FOUND = "SCAN_DEVICE_ZWAVE_FOUND"
    '''
    Raise when foscam HD device is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_FOSCAM_HD_FOUND = "SCAN_DEVICE_FOSCAM_HD_FOUND"
    '''
    Raise when x10 device receiver is found during scanning process
    eventData:{}
    '''
    EVENT_SCAN_DEVICE_X10_RECEIVER_FOUND = "SCAN_DEVICE_X10_RECEIVER_FOUND"
    '''
    Raise when pair device is started.
    eventData:{}
    '''
    EVENT_PAIR_DEVICE = "PAIR_DEVICE"
    '''
    Raise when device request user action during pairing proces
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_USER_ACTION_REQUIRED = "PAIR_DEVICE_USER_ACTION_REQUIRED"
    '''
    Raise when error occur during pairing process
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_ERROR_EXIST = "PAIR_DEVICE_ERROR_EXIST"
    '''
    Raise when pair device authentication failed
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_ERROR_AUTHENTICATION_FAIL = "PAIR_DEVICE_ERROR_AUTHENTICATION_FAIL"
    '''
    Raise when invalid parameter error occur during pairing process
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_ERROR_INVALID_PARAMETER = "PAIR_DEVICE_ERROR_INVALID_PARAMETER"
    '''
    Raise when unknown error occur during pairing process
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_ERROR_UNKNOWN = "PAIR_DEVICE_ERROR_UNKNOWN"
    '''
    Raise when pairing process is aborted.
    eventData:{}
    '''
    EVENT_PAIR_DEVICE_ABORT = "PAIR_DEVICE_ABORT"
    '''
    Raise when unpaired device is started.
    eventData:{}
    '''
    EVENT_UNPAIR_DEVICE = "UNPAIR_DEVICE"
    '''
    Raise when zwave request user action during unpaired process
    eventData:{}
    '''
    EVENT_UNPAIR_DEVICE_ZWAVE_USER_ACTION_REQUIRED = "UNPAIR_DEVICE_USER_ACTION_REQUIRED"
    '''
    Raise when invalid parameter error is occurred during unpaired process.
    eventData:{}
    '''
    EVENT_UNPAIR_DEVICE_ERROR_INVALID_PARAMETER = "UNPAIR_DEVICE_ERROR_INVALID_PARAMETER"
    '''
    Raise when unknown error is occurred during unpaired process.
    eventData:{}
    '''
    EVENT_UNPAIR_DEVICE_ERROR_UNKNOWN = "UNPAIR_DEVICE_ERROR_UNKNOWN"
    '''
    Raise when unpaired device process is aborted.
    eventData:{}
    '''
    EVENT_UNPAIR_DEVICE_ABORT = "UNPAIR_DEVICE_ABORT"
    ###
    
    ### Z-Wave Specific
    '''
    Raise when zwave is failed to add secure node.
    eventData:{}
    '''
    EVENT_ZWAVE_ADD_SECURE_NODE_FAILED = "ZWAVE_ADD_SECURE_NODE_FAILED"
    '''
    Raise when unpaired device process is aborted.
    eventData:{}
    '''
    EVENT_ZWAVE_NETWORK_ADD_USER_ACTION_REQUIRED = "ZWAVE_NETWORK_ADD_USER_ACTION_REQUIRED"
    '''
    Raise when zwave network remove user action.
    eventData:{}
    '''
    EVENT_ZWAVE_NETWORK_REMOVE_USER_ACTION_REQUIRED = "ZWAVE_NETWORK_REMOVE_USER_ACTION_REQUIRED"
    '''
    Raise when zwave network learn request user action.
    eventData:{}
    '''
    EVENT_ZWAVE_NETWORK_LEARN_USER_ACTION_REQUIRED = "ZWAVE_NETWORK_LEARN_USER_ACTION_REQUIRED"
    '''
    Raise when zwave network status is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_NETWORK_STATUS = "ZWAVE_NETWORK_STATUS"
    '''
    Raise when zwave network remove failed node is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_NETWORK_REMOVE_FAILED_NODE = "ZWAVE_NETWORK_REMOVE_FAILED_NODE"
    '''
    Raise when zwave node status is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_NODE_STATUS = "ZWAVE_NODE_STATUS"
    '''
    Raise when zwave node info update is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_NODE_INFO_UPDATE = "ZWAVE_NODE_INFO_UPDATE"
    '''
    Raise when zwave transmit status is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_TRANSMIT_STATUS = "ZWAVE_TRANSMIT_STATUS"
    '''
    Raise when zwave basic report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_BASIC_REPORT = "ZWAVE_BASIC_REPORT"
    '''
    Raise when zwave generic report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_GENERIC_REPORT = "ZWAVE_GENERIC_REPORT"
    '''
    Raise when zwave meter capabilities report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_METER_CAPABILITIES_REPORT = "ZWAVE_METER_CAPABILITIES_REPORT"
    '''
    Raise when zwave meter get report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_METER_GET_REPORT = "ZWAVE_METER_GET_REPORT"
    '''
    Raise when zwave lock operation report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_LOCK_OPERATION_REPORT = "ZWAVE_LOCK_OPERATION_REPORT"
    '''
    Raise when zwave battery report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_BATTERY_REPORT = "ZWAVE_BATTERY_REPORT"
    '''
    Raise when zwave alarm report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_ALARM_REPORT = "ZWAVE_ALARM_REPORT"
    '''
    Raise when zwave alarm supported event report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_ALARM_SUPPORTED_EVENT_REPORT = "ZWAVE_ALARM_SUPPORTED_EVENT_REPORT"
    '''
    Raise when zwave sensor multilevel report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SENSOR_MULTILEVEL_REPORT = "ZWAVE_SENSOR_MULTILEVEL_REPORT"
    '''
    Raise when zwave binary report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_BINARY_REPORT = "ZWAVE_BINARY_REPORT"
    '''
    Raise when zwave sensor multilevel supported report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SENSOR_MULTILEVEL_SUPPORTED_REPORT = "ZWAVE_SENSOR_MULTILEVEL_SUPPORTED_REPORT"
    '''
    Raise when zwave sensor multilevel unit report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SENSOR_MULTILEVEL_UNIT_REPORT = "ZWAVE_SENSOR_MULTILEVEL_UNIT_REPORT"
    '''
    Raise when zwave configuration report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_CONFIGURATION_REPORT = "ZWAVE_CONFIGURATION_REPORT"
    '''
    Raise when zwave user code support report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_USER_CODE_SUPPORT_REPORT = "ZWAVE_USER_CODE_SUPPORT_REPORT"
    '''
    Raise when zwave user code get report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_USER_CODE_GET_REPORT = "ZWAVE_USER_CODE_GET_REPORT"
    '''
    Raise when zwave group supported report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_GROUP_SUPPORTED_REPORT = "ZWAVE_GROUP_SUPPORTED_REPORT"
    '''
    Raise when zwave group active report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_GROUP_ACTIVE_REPORT = "ZWAVE_GROUP_ACTIVE_REPORT"
    '''
    Raise when zwave group report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_GROUP_REPORT = "ZWAVE_GROUP_REPORT"
    '''
    Raise when zwave switch multilevel start change is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SWITCH_MULTILEVEL_START_CHANGE = "ZWAVE_SWITCH_MULTILEVEL_START_CHANGE"
    '''
    Raise when zwave switch multilevel stop change is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SWITCH_MULTILEVEL_STOP_CHANGE = "ZWAVE_SWITCH_MULTILEVEL_STOP_CHANGE"
    '''
    Raise when zwave switch multilevel supported report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_SWITCH_MULTILEVEL_SUPPORTED_REPORT = "ZWAVE_SWITCH_MULTILEVEL_SUPPORTED_REPORT"
    '''
    Raise when zwave multilevel sensor supported report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_MULTILEVEL_SENSOR_SUPPORTED_REPORT = "ZWAVE_MULTILEVEL_SENSOR_SUPPORTED_REPORT"
    '''
    Raise when zwave multilevel sensor unit report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_MULTILEVEL_SENSOR_UNIT_REPORT = "ZWAVE_MULTILEVEL_SENSOR_UNIT_REPORT"
    '''
    Raise when zwave wakeup capabilities report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_WAKEUP_CAPABILITIES_REPORT = "ZWAVE_WAKEUP_CAPABILITIES_REPORT"
    '''
    Raise when zwave thermostat fan mode supported report response is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_RESPONSE = "ZWAVE_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_RESPONSE"
    '''
    Raise when zwave thermostat fan mode report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_FAN_MODE_REPORT = "ZWAVE_THERMOSTAT_FAN_MODE_REPORT"
    '''
    Raise when zwave thermostat fan state report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_FAN_STATE_REPORT = "ZWAVE_THERMOSTAT_FAN_STATE_REPORT"
    '''
    Raise when zwave thermostat mode report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_MODE_REPORT = "ZWAVE_THERMOSTAT_MODE_REPORT"
    '''
    Raise when zwave thermostat mode supported report response is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_MODE_SUPPORTED_REPORT_RESPONSE = "ZWAVE_THERMOSTAT_MODE_SUPPORTED_REPORT_RESPONSE"
    '''
    Raise when zwave thermostat operating state report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_OPERATING_STATE_REPORT = "ZWAVE_THERMOSTAT_OPERATING_STATE_REPORT"
    '''
    Raise when zwave thermostat setback report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_SETBACK_REPORT = "ZWAVE_THERMOSTAT_SETBACK_REPORT"
    '''
    Raise when zwave thermostat setpoint report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_SETPOINT_REPORT = "ZWAVE_THERMOSTAT_SETPOINT_REPORT"
    '''
    Raise when zwave thermostat setpoint supported report response is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_THERMOSTAT_SETPOINT_SUPPORTED_REPORT_RESPONSE = "ZWAVE_THERMOSTAT_SETPOINT_SUPPORTED_REPORT_RESPONSE"
    '''
    Raise when zwave binary sensor report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_BINARY_SENSOR_REPORT = "ZWAVE_BINARY_SENSOR_REPORT"
    '''
    Raise when zwave neighbor update status is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_NEIGHBOR_UPDATE_STATUS = "ZWAVE_NEIGHBOR_UPDATE_STATUS"
    '''
    Raise when zwave alarm supported report is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_ALARM_SUPPORTED_REPORT = "ZWAVE_ALARM_SUPPORTED_REPORT"
    '''
    Raise when zwave unknown is occurred.
    eventData:{}
    '''
    EVENT_ZWAVE_UNKNOWN = "ZWAVE_UNKNOWN"
    ###
    
    ### X-10 Specific
    '''
    Raise when x10 scanning event is occurred.
    eventData:{}
    '''
    EVENT_X10_SCANNING_EVENT = "X10_SCANNING_EVENT"
    '''
    Raise when x10 motion sensor event is occurred.
    eventData:{}
    '''
    EVENT_X10_MOTION_SENSOR_EVENT = "X10_MOTION_SENSOR_EVENT"
    '''
    Raise when x10 door window sensor event is occurred.
    eventData:{}
    '''
    EVENT_X10_DOOR_WINDOW_SENSOR_EVENT = "X10_DOOR_WINDOW_SENSOR_EVENT"
    '''
    Raise when x10 keychain remote event is occurred.
    eventData:{}
    '''
    EVENT_X10_KEYCHAIN_REMOTE_EVENT = "X10_KEYCHAIN_REMOTE_EVENT"
    '''
    Raise when x10 panic button event is occurred.
    eventData:{}
    '''
    EVENT_X10_PANIC_BUTTON_EVENT = "X10_PANIC_BUTTON_EVENT"
    '''
    Raise when x10 unknown model event is occurred.
    eventData:{}
    '''
    EVENT_X10_UNKNOWN_MODEL_EVENT = "X10_UNKNOWN_MODEL_EVENT"
    ### 

    ### Dust Specific
    '''
    Raise when dust reply is occurred.
    eventData:{}
    '''
    EVENT_DUST_REPLY = "DUST_REPLY"
    '''
    Raise when dust status is occurred.
    eventData:{}
    '''
    EVENT_DUST_STATUS = "DUST_STATUS"
    '''
    Raise when dust notif event mote reset is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_RESET = "DUST_NOTIF_EVENT_MOTE_RESET"
    '''
    Raise when dust notif event network reset is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_NETWORK_RESET = "DUST_NOTIF_EVENT_NETWORK_RESET"
    '''
    Raise when dust notif event command finish is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_COMMAND_FINISH = "DUST_NOTIF_EVENT_COMMAND_FINISH"
    '''
    Raise when dust notif event mote join is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_JOIN = "DUST_NOTIF_EVENT_MOTE_JOIN"
    '''
    Raise when dust notif event mote operational is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_OPERATIONAL = "DUST_NOTIF_EVENT_MOTE_OPERATIONAL"
    '''
    Raise when dust notif event mote lost is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_LOST = "DUST_NOTIF_EVENT_MOTE_LOST"
    '''
    Raise when dust notif event network time is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_NETWORK_TIME = "DUST_NOTIF_EVENT_NETWORK_TIME"
    '''
    Raise when dust notif event ping response is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_PING_RESPONSE = "DUST_NOTIF_EVENT_PING_RESPONSE"
    '''
    Raise when dust notif event path create is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_PATH_CREATE = "DUST_NOTIF_EVENT_PATH_CREATE"
    '''
    Raise when dust notif event path delete is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_PATH_DELETE = "DUST_NOTIF_EVENT_PATH_DELETE"
    '''
    Raise when dust notif event packet sent is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_PACKET_SENT = "DUST_NOTIF_EVENT_PACKET_SENT"
    '''
    Raise when dust notif event mote create is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_CREATE = "DUST_NOTIF_EVENT_MOTE_CREATE"
    '''
    Raise when dust notif event mote delete is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_EVENT_MOTE_DELETE = "DUST_NOTIF_EVENT_MOTE_DELETE"
    '''
    Raise when dust notif log is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_LOG = "DUST_NOTIF_LOG"
    '''
    Raise when dust notif data is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_DATA = "DUST_NOTIF_DATA"
    '''
    Raise when dust notif IP data is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_IP_DATA = "DUST_NOTIF_IP_DATA"
    '''
    Raise when dust notif health report is occurred.
    eventData:{}
    '''
    EVENT_DUST_NOTIF_HEALTH_REPORT = "DUST_NOTIF_HEALTH_REPORT"
    ### 
    
    ### Insteon Specific
    '''
    Raise when insteon device status is occurred.
    eventData:{}
    '''
    EVENT_INSTEON_DEVICE_STATUS = "INSTEON_DEVICE_STATUS"
    '''
    Raise when insteon liking completed is occurred.
    eventData:{}
    '''
    EVENT_INSTEON_LINKING_COMPLETE = "INSTEON_LINKING_COMPLETE"
    '''
    Raise when insteon delete link completed is occurred.
    eventData:{}
    '''
    EVENT_INSTEON_DELETE_LINK_COMPLETE = "INSTEON_DELETE_LINK_COMPLETE"
    ### 
    
    ### FTDI Specific
    '''
    Raise when ftdi read is occurred.
    eventData:{}
    '''
    EVENT_FTDI_READ = "FTDI_READ"
    ### 
    
    ### AFFINEX's FTDI Specific
    '''
    Raise when affinex ftdi dev kit input press is occurred.
    eventData:{}
    '''
    EVENT_AFFINEX_FTDI_DEV_KIT_INPUT_PRESS = "AFFINEX_FTDI_DEV_KIT_INPUT_PRESS"
    '''
    Raise when affinex ftdi dev kit turn on led is occurred.
    eventData:{}
    '''
    EVENT_AFFINEX_FTDI_DEV_KIT_TURN_ON_LED = "AFFINEX_FTDI_DEV_KIT_TURN_ON_LED"
    ### 
    
    ### UPNP Service Specific
    '''
    Raise when upnp service playback is started is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_STARTED = "UPNP_SERVICE_PLAYBACK_STARTED"
    '''
    Raise when upnp service playback is playing is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_PLAYING = "UPNP_SERVICE_PLAYBACK_PLAYING"
    '''
    Raise when upnp service playback is paused is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_PAUSED = "UPNP_SERVICE_PLAYBACK_PAUSED"
    '''
    Raise when upnp service playback is stopped is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_STOPPED = "UPNP_SERVICE_PLAYBACK_STOPPED"
    '''
    Raise when upnp service playback volume changed is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_VOLUME_CHANGED = "UPNP_SERVICE_PLAYBACK_VOLUME_CHANGED"
    '''
    Raise when upnp service playback mute state changed is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_MUTE_STATE_CHANGED = "UPNP_SERVICE_PLAYBACK_MUTE_STATE_CHANGED"
    '''
    Raise when upnp service playback info updated is occurred.
    eventData:{}
    '''
    EVENT_UPNP_SERVICE_PLAYBACK_INFO_UPDATED = "UPNP_SERVICE_PLAYBACK_INFO_UPDATED"
    ### 

    ### SYB Player Specific
    '''
    Raise when syb player info is occurred.
    eventData:{}
    '''
    EVENT_SYB_PLAYER_INFO = "SYB_PLAYER_INFO"
    ### 
    
    ### WeMo Service Specific
    '''
    Raise when wemo sensor motion is detected
    eventData:{}
    '''
    EVENT_WEMO_SENSOR_MOTION_DETECTED = "WEMO_SENSOR_MOTION_DETECTED"
    ### 
    
    ### Speaker Controller Specific
    '''
    Raise when speaker controller playback info updated is occurred
    eventData:{}
    '''
    EVENT_SPEAKER_CONTROLLER_PLAYBACK_INFO_UPDATED = "SPEAKER_CONTROLLER_PLAYBACK_INFO_UPDATED"
    ### 
    
    ### Sensor Controller Specific
    '''
    Raise when sensor controller motion is occurred.
    eventData:{}
    '''
    EVENT_SENSOR_CONTROLLER_MOTION = "SENSOR_CONTROLLER_MOTION"
    '''
    Raise when sensor controller light is occurred.
    eventData:{}
    '''
    EVENT_SENSOR_CONTROLLER_LIGHT = "SENSOR_CONTROLLER_LIGHT"
    '''
    Raise when sensor controller door window is occurred.
    eventData:{}
    '''
    EVENT_SENSOR_CONTROLLER_DOOR_WINDOW = "SENSOR_CONTROLLER_DOOR_WINDOW"
    '''
    Raise when sensor controller sensor is occurred.
    eventData:{}
    '''
    EVENT_SENSOR_CONTROLLER_SENSOR = "SENSOR_CONTROLLER_SENSOR"
    '''
    Raise when sensor controller alarm is occurred.
    eventData:{}
    '''
    EVENT_SENSOR_CONTROLLER_ALARM = "SENSOR_CONTROLLER_ALARM"
    ### 
    
    ### Switch Controller Specific
    '''
    Raise when switch controller state changed is occurred.
    eventData:{}
    '''
    EVENT_SWITCH_CONTROLLER_STATE_CHANGED = "SWITCH_CONTROLLER_STATE_CHANGED"
    ### 
    
    ### Dimmer Controller Specific
    '''
    Raise when dimmer controller state changed is occurred.
    eventData:{}
    '''
    EVENT_DIMMER_CONTROLLER_STATE_CHANGED = "DIMMER_CONTROLLER_STATE_CHANGED"
    ### 
        
    ### Dimmer Stepper Controller Specific
    '''
    Raise when dimmer step controller state changed is occurred.
    eventData:{}
    '''
    EVENT_DIMMER_STEPPER_CONTROLLER_STATE_CHANGED = "DIMMER_STEPPER_CONTROLLER_STATE_CHANGED"
    ### 
    
    ### Horn Controller Specific
    '''
    Raise when horn controller state changed is occurred.
    eventData:{}
    '''
    EVENT_HORN_CONTROLLER_STATE_CHANGED = "HORN_CONTROLLER_STATE_CHANGED"
    ### 
    
    ### Power Strip Controller Specific
    '''
    Raise when power strip controller state changed is occurred.
    eventData:{}
    '''
    EVENT_POWER_STRIP_CONTROLLER_STATE_CHANGED = "POWER_STRIP_CONTROLLER_STATE_CHANGED"
    ### 
    
    ### Hue Controller Specific
    '''
    Raise when hue controller state changed is occurred.
    eventData:{}
    '''
    EVENT_HUE_CONTROLLER_STATE_CHANGED = "HUE_CONTROLLER_STATE_CHANGED"
    ### 
    
    ### Door Lock Controller Specific
    '''
    Raise when door lock controller state changed is occurred.
    eventData:{}
    '''
    EVENT_DOOR_LOCK_CONTROLLER_STATE_CHANGED = "DOOR_LOCK_CONTROLLER_STATE_CHANGED"
    '''
    Raise when door lock controller battery low is occurred.
    eventData:{}
    '''
    EVENT_DOOR_LOCK_CONTROLLER_BATTERY_LOW = "DOOR_LOCK_CONTROLLER_BATTERY_LOW"
    ### 
    
    ### Weather Service Specific
    '''
    Raise when weather service weather status is changed.
    eventData:{}
    '''
    EVENT_WEATHER_SERVICE_WEATHER_STATUS_CHANGED = "WEATHER_STATUS_CHANGED"
    '''
    Raise when weather service wind direction is changed.
    eventData:{}
    '''
    EVENT_WEATHER_SERVICE_WIND_DIRECTION_CHANGED = "WEATHER_WIND_DIRECTION_CHANGED"
    '''
    Raise when weather temperature unit is changed.
    eventData:{}
    '''
    EVENT_WEATHER_TEMPERATURE_UNIT_CHANGED = "WEATHER_TEMPERATURE_UNIT_CHANGED"
    ### 
    
    ### Bluetooth
    '''
    Raise when event bluetooth is occurred.
    eventData:{}
    '''
    EVENT_BLUETOOTH = "BLUETOOTH"
    ### 
    
    ### Bluetooth Low Energy
    '''
    Raise when ble is paired.
    eventData:{}
    '''
    EVENT_BLE_PAIRED = "BLE_PAIRED"
    '''
    Raise when ble is unpaired.
    eventData:{}
    '''
    EVENT_BLE_UNPAIRED = "BLE_UNPAIRED"
    '''
    Raise when ble is connected.
    eventData:{}
    '''
    EVENT_BLE_CONNECTED = "BLE_CONNECTED"
    '''
    Raise when ble is disconnected.
    eventData:{}
    '''
    EVENT_BLE_DISCONNECTED = "BLE_DISCONNECTED"
    '''
    Raise when event ble services is occurred.
    eventData:{}
    '''
    EVENT_BLE_SERVICES = "BLE_SERVICES"
    '''
    Raise when event ble characteristics is occurred.
    eventData:{}
    '''
    EVENT_BLE_CHARACTERISTICS = "BLE_CHARACTERISTICS"
    '''
    Raise when ble is response.
    eventData:{}
    '''
    EVENT_BLE_RESPONSE = "BLE_RESPONSE"
    ### 
    
    ### Tiny Finder
    '''
    Raise when event tiny finder battery is occurred.
    eventData:{}
    '''
    EVENT_TINY_FINDER_BATTERY = "TINY_FINDER_BATTERY"
    '''
    Raise when event tiny finder link loss is occurred.
    eventData:{}
    '''
    EVENT_TINY_FINDER_LINK_LOSS = "TINY_FINDER_LINK_LOSS"
    ### 
    
    ### Shared Methods
    '''
    Raise when shared method is deleted.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_DELETED = "SHARED_METHOD_DELETED"
    '''
    Raise when shared method is activated.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_ACTIVATED = "SHARED_METHOD_ACTIVATED"
    '''
    Raise when shared method is activated.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_DEACTIVATED = "SHARED_METHOD_DEACTIVATED"
    '''
    Raise when shared method group is deleted.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_GROUP_DELETED = "SHARED_METHOD_GROUP_DELETED"
    '''
    Raise when shared method is updated.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_UPDATED = "SHARED_METHOD_UPDATED"
    '''
    Raise when shared method group is updated.
    eventData:{}
    '''
    EVENT_SHARED_METHOD_GROUP_UPDATED = "SHARED_METHOD_GROUP_UPDATED"
    ### 
### END