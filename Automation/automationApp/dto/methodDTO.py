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
from automationApp.dto.groupDTO import GroupDTO
from automationApp.utils.valueParser import ValueParser


class MethodDTO(dict):

    PROP_METHOD_ID = "kbxMethodId"
    PROP_METHOD_LABEL = "kbxMethodLabel"
    PROP_METHOD_NAME = "kbxMethodName"
    PROP_METHOD_ARGS = "kbxMethodParams"
    PROP_METHOD_APP_ID = "kbxMethodAppId"
    PROP_METHOD_HAS_EVENT = "kbxMethodHasEvent"
    PROP_METHOD_EVENT = "kbxMethodEvent"
    PROP_METHOD_STATUS = "kbxMethodStatus"
    PROP_STATUS_CODE = "statusCode"
    PROP_STATUS_MESSAGE = "statusMessage"
    PROP_GROUP_ID = GroupDTO.PROP_GROUP_ID

    def __init__(self, **kwargs):
        super().__init__()
        mappers = {MethodDTO.PROP_METHOD_ID:self.set_method_id,
                   MethodDTO.PROP_METHOD_NAME:self.set_method_name,
                   MethodDTO.PROP_METHOD_LABEL:self.set_method_label,
                   MethodDTO.PROP_METHOD_ARGS:self.set_method_args,
                   MethodDTO.PROP_METHOD_HAS_EVENT:self.set_method_has_event,
                   MethodDTO.PROP_METHOD_EVENT:self.set_method_event,
                   MethodDTO.PROP_METHOD_APP_ID:self.set_method_app_id,
                   MethodDTO.PROP_METHOD_STATUS:self.set_method_status,
                   MethodDTO.PROP_STATUS_CODE:self.set_status_code,
                   MethodDTO.PROP_STATUS_MESSAGE:self.set_status_message,
                   MethodDTO.PROP_GROUP_ID:self.set_group_id}

        keys = []
        for key, method in mappers.items():
            keys.append(key)
            try:
                method(kwargs[key])
            except:
                method(None)

        for key, value in kwargs.items():
            if key not in keys:
                self[key] = value

    def get_method_id(self):
        return self.get(MethodDTO.PROP_METHOD_ID)

    def get_method_name(self):
        return self.get(MethodDTO.PROP_METHOD_NAME)

    def get_method_label(self):
        return self.get(MethodDTO.PROP_METHOD_LABEL)

    def get_method_args(self):
        return self.get(MethodDTO.PROP_METHOD_ARGS)

    def get_method_has_event(self):
        return self.get(MethodDTO.PROP_METHOD_HAS_EVENT)

    def get_method_event(self):
        return self.get(MethodDTO.PROP_METHOD_EVENT)

    def get_method_app_id(self):
        return self.get(MethodDTO.PROP_METHOD_APP_ID)

    def get_method_status(self):
        return self.get(MethodDTO.PROP_METHOD_STATUS)

    def get_group_id(self):
        return self.get(MethodDTO.PROP_GROUP_ID)

    def get_status_code(self):
        return self.get(MethodDTO.PROP_STATUS_CODE)

    def get_status_message(self):
        return self.get(MethodDTO.PROP_STATUS_MESSAGE)

    def set_method_id(self, value):
        self[MethodDTO.PROP_METHOD_ID] = ValueParser.get_number(value)

    def set_method_name(self, value):
        self[MethodDTO.PROP_METHOD_NAME] = ValueParser.get_string(value)

    def set_method_label(self, value):
        self[MethodDTO.PROP_METHOD_LABEL] = ValueParser.get_string(value)

    def set_method_args(self, value):
        self[MethodDTO.PROP_METHOD_ARGS] = ValueParser.get_list(value)

    def set_method_has_event(self, value):
        self[MethodDTO.PROP_METHOD_HAS_EVENT] = ValueParser.get_boolean(value)

    def set_method_event(self, value):
        self[MethodDTO.PROP_METHOD_EVENT] = value

    def set_method_app_id(self, value):
        self[MethodDTO.PROP_METHOD_APP_ID] = ValueParser.get_positive_number(value)

    def set_method_status(self, value):
        self[MethodDTO.PROP_METHOD_STATUS] = ValueParser.get_number(value)

    def set_group_id(self, value):
        groupId = ValueParser.get_number(value)
        self[MethodDTO.PROP_GROUP_ID] = groupId if groupId is not None else -1

    def set_status_code(self, value):
        self[MethodDTO.PROP_STATUS_CODE] = ValueParser.get_number(value)

    def set_status_message(self, value):
        self[MethodDTO.PROP_STATUS_MESSAGE] = value
        
    def reset(self):
        ignores = [MethodDTO.PROP_METHOD_ID, MethodDTO.PROP_GROUP_ID, MethodDTO.PROP_METHOD_ARGS, MethodDTO.PROP_METHOD_HAS_EVENT]
        mappers = {MethodDTO.PROP_METHOD_NAME:self.set_method_name,
                   MethodDTO.PROP_METHOD_LABEL:self.set_method_label,
                   MethodDTO.PROP_METHOD_EVENT:self.set_method_event,
                   MethodDTO.PROP_METHOD_APP_ID:self.set_method_app_id,
                   MethodDTO.PROP_METHOD_STATUS:self.set_method_status,
                   MethodDTO.PROP_STATUS_CODE:self.set_status_code,
                   MethodDTO.PROP_STATUS_MESSAGE:self.set_status_message}
        
        keys = [key for key in self.keys()]
        for key in keys:
            if key in ignores:
                continue
            elif key in mappers:
                mappers[key](None)
            else:
                del(self[key])
