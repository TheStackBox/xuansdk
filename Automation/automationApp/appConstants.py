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
from concurrent.futures.thread import ThreadPoolExecutor

class AppConstants(object):

    GROUP_ID_AUTOMATION = None
    GROUP_ID_SERVICE = None
    GROUP_ID_SPEAKER = None
    GROUP_ID_SWITCH = None
    GROUP_ID_DOOR_LOCK = None
    GROUP_ID_HUE = None
    GROUP_ID_DIMMER = None
    GROUP_ID_HORN = None
    GROUP_ID_IPCAMERA = None
    GROUP_ID_POWER_STRIP = None
    GROUP_ID_SENSOR = None
    GROUP_ID_NOTIFICATION = None
    GROUP_ID_SERVICE = None

    UPPER_LIMIT = 200
    MIN_TRIGGER_INTERVAL = 1

    TAG_ACTION = "automation_action"
    TAG_CONDITION = "automation_condition"

    SECTION_CONDITION = "if"
    SECTION_EXECUTION = "then"

    MAX_METHOD_SIZE = 10
    MAX_RULE_SIZE = 20

    METHOD_ERROR_OK = (0, "ok")
    METHOD_ERROR_GROUP_REMOVED = (1, "group is removed")
    METHOD_ERROR_METHOD_REMOVED = (2, "method is removed")
    METHOD_ERROR_METHOD_OFF = (4, "method is inactive")

    ARG_NAME = "kbxParamName"
    ARG_CURRENT_VALUE = "kbxParamCurrentValue"

    KEY_CONDITION_RESPONSE = "value"
    KEY_CONDITION_TIMESTAMP = "timestamp"
    KEY_CONDITION_EVENT_TAG = "eventTag"
    KEY_CONDITION_EVENT_DATA = "eventData"
    KEY_ACTION_TIMESTAMP = "timestamp"

    RULE_CODE = {
            0: "ok",
            1: "group(s) is removed",
            2: "method(s) is removed",
            3: "group(s) and method(s) are removed",
            4: "method(s) is inactive",
            5: "group(s) is removed and method(s) is inactive",
            6: "methods are removed and inactive",
            7: "group(s) and method(s) are removed, and method(s) is inactive"
        }

    GROUP_DESC = {"speaker":"group_speaker_desc",
                 "switch":"group_switch_desc",
                 "door_lock":"group_door_lock_desc",
                 "hue":"group_hue_desc",
                 "dimmer":"group_dimmer_desc",
                 "horn":"group_horn_desc",
                 "ipcamera":"group_ipcamera_desc",
                 "power_strip":"group_power_strip_desc",
                 "sensor":"group_sensor_desc",
                 "notification":"group_notification_desc",
                 "service":"group_service_desc"}

    ThreadPoolExecutor = None

    EVENT_RULE_UPDATE_STARTED = "AUTOMATION_RULE_UPDATE_STARTED"
    EVENT_RULE_UPDATED = "AUTOMATION_RULE_UPDATED"

    @staticmethod
    def get_thread_pool_executor():
        if AppConstants.ThreadPoolExecutor is None:
            AppConstants.ThreadPoolExecutor = ThreadPoolExecutor(max_workers=10)
        return AppConstants.ThreadPoolExecutor

