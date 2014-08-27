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
from automationApp.dto.triggerDTO import TriggerDTO
from automationApp.utils.valueParser import ValueParser


class RuleDTO(dict):

    RULE_TYPE_SCENE = 0
    RULE_TYPE_RULE = 1

    RULE_STATUS_PROCESSED_UPDATING = "updating"
    RULE_STATUS_PROCESSED_UPDATED = "updated"

    PROP_RULE_ID = "ruleId"
    PROP_RULE_NAME = "ruleName"
    PROP_RULE_TYPE = "ruleType"
    PROP_ENABLED = "enabled"
    PROP_TRIGGER = "trigger"
    PROP_CONDITION = "condition"
    PROP_EXECUTION = "execution"
    PROP_STATUS_CODE = "statusCode"
    PROP_STATUS_MESSAGE = "statusMessage"
    PROP_STATUS_PROCESSED = "statusProcessed"

    def __init__(self, **kwargs):
        super().__init__()
        mappers = {RuleDTO.PROP_RULE_ID:self.set_rule_id,
                   RuleDTO.PROP_RULE_NAME:self.set_rule_name,
                   RuleDTO.PROP_ENABLED:self.set_enabled,
                   RuleDTO.PROP_TRIGGER:self.set_trigger,
                   RuleDTO.PROP_CONDITION:self.set_conditions,
                   RuleDTO.PROP_EXECUTION:self.set_executions,
                   RuleDTO.PROP_STATUS_CODE:self.set_status_code,
                   RuleDTO.PROP_STATUS_MESSAGE:self.set_status_message,
                   RuleDTO.PROP_STATUS_PROCESSED:self.set_status_processed}

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

    def get_rule_id(self):
        return self.get(RuleDTO.PROP_RULE_ID)

    def get_rule_name(self):
        return self.get(RuleDTO.PROP_RULE_NAME)

    def get_rule_type(self):
        return self.get(RuleDTO.PROP_RULE_TYPE)

    def get_enabled(self):
        return self.get(RuleDTO.PROP_ENABLED)

    def get_trigger(self):
        return self.get(RuleDTO.PROP_TRIGGER)

    def get_conditions(self):
        return self.get(RuleDTO.PROP_CONDITION)

    def get_executions(self):
        return self.get(RuleDTO.PROP_EXECUTION)

    def get_status_code(self):
        return self.get(RuleDTO.PROP_STATUS_CODE)

    def get_status_message(self):
        return self.get(RuleDTO.PROP_STATUS_MESSAGE)

    def get_status_processed(self):
        return self.get(RuleDTO.PROP_STATUS_PROCESSED)

    def set_rule_id(self, value):
        self[RuleDTO.PROP_RULE_ID] = ValueParser.get_string(value)

    def set_rule_name(self, value):
        self[RuleDTO.PROP_RULE_NAME] = ValueParser.get_string(value)

    def set_rule_type(self, value):
        self[RuleDTO.PROP_RULE_TYPE] = ValueParser.get_number(value)

    def set_enabled(self, value):
        self[RuleDTO.PROP_ENABLED] = ValueParser.get_boolean(value)

    def set_trigger(self, value):
        if isinstance(value, TriggerDTO):
            self[RuleDTO.PROP_TRIGGER] = value
        else:
            self[RuleDTO.PROP_TRIGGER] = None

    def set_conditions(self, value):
        self[RuleDTO.PROP_CONDITION] = ValueParser.get_list(value)

    def set_executions(self, value):
        self[RuleDTO.PROP_EXECUTION] = ValueParser.get_list(value)

    def set_status_code(self, value):
        self[RuleDTO.PROP_STATUS_CODE] = ValueParser.get_number(value)

    def set_status_message(self, value):
        self[RuleDTO.PROP_STATUS_MESSAGE] = value

    def set_status_processed(self, value):
        self[RuleDTO.PROP_STATUS_PROCESSED] = value

