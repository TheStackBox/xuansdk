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
from automationApp.utils.valueParser import ValueParser


class GroupDTO(dict):

    PROP_GROUP_ID = "kbxGroupId"
    PROP_GROUP_NAME = "kbxGroupName"
    PROP_GROUP_LABEL = "kbxGroupLabel"
    PROP_GROUP_DESC = "kbxGroupDesc"
    PROP_GROUP_ICON = "kbxGroupIcon"
    PROP_GROUP_APP_ID = "kbxGroupAppId"
    PROP_STATUS_CODE = "statusCode"
    PROP_STATUS_MESSAGE = "statusMessage"

    def __init__(self, **kwargs):
        super().__init__()
        mappers = {GroupDTO.PROP_GROUP_ID:self.set_group_id,
                  GroupDTO.PROP_GROUP_NAME:self.set_group_name,
                  GroupDTO.PROP_GROUP_LABEL:self.set_group_label,
                  GroupDTO.PROP_GROUP_DESC:self.set_group_desc,
                  GroupDTO.PROP_GROUP_ICON:self.set_group_icon,
                  GroupDTO.PROP_GROUP_APP_ID:self.set_group_app_id,
                  GroupDTO.PROP_STATUS_CODE:self.set_status_code,
                  GroupDTO.PROP_STATUS_MESSAGE:self.set_status_message}

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

    def get_group_id(self):
        return self.get(GroupDTO.PROP_GROUP_ID)

    def get_group_icon(self):
        return self.get(GroupDTO.PROP_GROUP_ICON)

    def get_group_label(self):
        return self.get(GroupDTO.PROP_GROUP_LABEL)

    def get_group_name(self):
        return self.get(GroupDTO.PROP_GROUP_NAME)

    def get_group_desc(self):
        return self.get(GroupDTO.PROP_GROUP_DESC)

    def get_group_app_id(self):
        return self.get(GroupDTO.PROP_GROUP_APP_ID)

    def get_status_code(self):
        return self.get(GroupDTO.PROP_STATUS_CODE)

    def get_status_message(self):
        return self.get(GroupDTO.PROP_STATUS_MESSAGE)

    def set_group_id(self, value):
        self[GroupDTO.PROP_GROUP_ID] = ValueParser.get_number(value)

    def set_group_icon(self, value):
        self[GroupDTO.PROP_GROUP_ICON] = ValueParser.get_string(value)

    def set_group_label(self, value):
        self[GroupDTO.PROP_GROUP_LABEL] = ValueParser.get_string(value)

    def set_group_name(self, value):
        self[GroupDTO.PROP_GROUP_NAME] = ValueParser.get_string(value)

    def set_group_desc(self, value):
        self[GroupDTO.PROP_GROUP_DESC] = value # Prevent Override KBXLang

    def set_group_app_id(self, value):
        self[GroupDTO.PROP_GROUP_APP_ID] = ValueParser.get_positive_number(value)

    def set_status_code(self, value):
        self[GroupDTO.PROP_STATUS_CODE] = ValueParser.get_number(value)

    def set_status_message(self, value):
        self[GroupDTO.PROP_STATUS_MESSAGE] = value
    
    def reset(self):
        ignores = [GroupDTO.PROP_GROUP_ID, GroupDTO.PROP_STATUS_CODE, GroupDTO.PROP_STATUS_MESSAGE]
        mappers = {GroupDTO.PROP_GROUP_NAME:self.set_group_name,
                  GroupDTO.PROP_GROUP_LABEL:self.set_group_label,
                  GroupDTO.PROP_GROUP_DESC:self.set_group_desc,
                  GroupDTO.PROP_GROUP_ICON:self.set_group_icon,
                  GroupDTO.PROP_GROUP_APP_ID:self.set_group_app_id}
        
        keys = [key for key in self.keys()]
        for key in keys:
            if key in ignores:
                continue
            elif key in mappers:
                mappers[key](None)
            else:
                del(self[key])
