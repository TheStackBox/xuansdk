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

class AppConstants:
    
    
    GROUP_ID_AUTOMATION = None
    GROUP_ID_NOTIFICATION = None
    GROUP_ID_SERVICE = None
    GROUP_ID_UNKNOWN_LOCATION = None

    UPPER_LIMIT = 50

    TAG_ACTION = "automation_action"
    TAG_CONDITION = "automation_condition"

    SECTION_CONDITION = "if"
    SECTION_EXECUTION = "then"

    MAX_METHOD_SIZE = 10
    
    MAX_RULE_SIZE = 50
    MAX_RULE_EXEC_THREAD_SIZE = 50
    
    MAX_SCENE_SIZE = 50
    MAX_SCENE_EXEC_THREAD_SIZE = 50

    METHOD_ERROR_OK = 0 # ok
    METHOD_ERROR_GROUP_REMOVED = 1 # group is removed
    METHOD_ERROR_METHOD_REMOVED = 2 # method is removed 
    METHOD_ERROR_METHOD_OFF = 4 # method is inactive

    ARG_NAME = "kbxParamName"
    ARG_CURRENT_VALUE = "kbxParamCurrentValue"

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

    EVENT_RULE_UPDATE_STARTED = "AUTOMATION_RULE_UPDATE_STARTED"
    EVENT_RULE_UPDATED = "AUTOMATION_RULE_UPDATED"
    EVENT_RULE_UPDATE_FAILED = "AUTOMATION_RULE_UPDATE_FAILED"
    EVENT_RULE_DELETED = "AUTOMATION_RULE_DELETED"
    
    EVENT_SCENE_UPDATE_STARTED = "AUTOMATION_SCENE_UPDATE_STARTED"
    EVENT_SCENE_UPDATED = "AUTOMATION_SCENE_UPDATED"
    EVENT_SCENE_UPDATE_FAILED = "AUTOMATION_SCENE_UPDATE_FAILED"
    EVENT_SCENE_DELETED = "AUTOMATION_SCENE_DELETED"
    
    EVENT_AUTOMATION_GROUP_ADDED = "AUTOMATION_GROUP_ADDED"
    EVENT_AUTOMATION_GROUP_DELETED = "AUTOMATION_GROUP_DELETED"
    EVENT_AUTOMATION_GROUP_UPDATED = "AUTOMATION_GROUP_UPDATED"

    EVENT_SER_DELETED = "AUTOMATION_SCENE_EXECUTION_RESULT_REMOVED"
    EVENT_SERI_RETRY_STARTED = "AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_STARTED"
    EVENT_SERI_RETRY_COMPLETED = "AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_ENDED"
    
    EVENT_FAVORITED_SCENE_ADDED = "AUTOMATION_FAVORITED_SCENE_ADDED"
    EVENT_FAVORITED_SCENE_DELETED = "AUTOMATION_FAVORITED_SCENE_DELETED"
    
    RULE_STATUS_UPDATING = "updating"
    RULE_STATUS_UPDATED = "updated"
    
    SCENE_STATUS_UPDATING = "updating"
    SCENE_STATUS_UPDATED = "updated"
    
    TRIGGER_TYPE_EVENT = 0 # receive no value
    TRIGGER_TYPE_TIME = 1 # receive value as "HH:MM" ranged from 0-23 and 0-59
    TRIGGER_TYPE_INTERVAL = 2 # receive seconds
    
    