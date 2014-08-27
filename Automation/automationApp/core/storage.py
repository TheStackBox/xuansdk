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
import json

from automationApp.appConstants import AppConstants
from automationApp.dto.methodDTO import MethodDTO
from automationApp.dto.ruleDTO import RuleDTO
from automationApp.dto.triggerDTO import TriggerDTO
from automationApp.utils.valueParser import ValueParser
from com.cloudMedia.theKuroBox.sdk.service.storageManagerService import StorageManagerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class Storage(object):

    STORAGE_GROUP = "automation_group"
    STORAGE_RULE = "automation_rule"
    STORAGE_METHOD_GROUP = "automation_method_group"

    @staticmethod
    def list_all_rules():
        offset = 0
        limit = 50

        totalCount = offset + limit + 1 # initially set to more than offset+limit so that first while can be triggered.
        allRules = []
        while(offset + limit < totalCount):
            try:
                result = StorageManagerService.get_data(group=Storage.STORAGE_RULE, limit=limit, offset=offset)

                result = ValueParser.get_dict(result)

                rules = ValueParser.get_list(result["data"])
                totalCount = int(result["totalRecord"])
                offset += limit

                if rules:
                    for rule in rules:
                        rule = ValueParser.get_dict(rule.get("appDataValue"))
                        allRules.append(rule)

            except Exception as e:
                Logger.log_debug("Storage.list_all_rules err: " + str(e))
                break
        return allRules

    @staticmethod
    def list_all_groups():
        offset = 0
        limit = 50

        totalCount = offset + limit + 1 # initially set to more than offset+limit so that first while can be triggered.
        allGroupLabels = {}
        while(offset + limit < totalCount):
            try:
                result = StorageManagerService.get_data(group=Storage.STORAGE_GROUP, limit=limit, offset=offset)
                result = ValueParser.get_dict(result)

                groups = ValueParser.get_list(result["data"])
                totalCount = int(result["totalRecord"])
                offset += limit

                if groups:
                    for group in groups:
                        allGroupLabels[ValueParser.get_number(group["appDataKey"])] = ValueParser.get_string(group["appDataValue"])

            except Exception as e:
                Logger.log_debug("Storage.list_all_groups err: " + str(e))
                break

        return allGroupLabels

    @staticmethod
    def list_all_method_groups():
        offset = 0
        limit = 50

        totalCount = offset + limit + 1 # initially set to more than offset+limit so that first while can be triggered.
        allMethodGroupIdPairs = {}
        while(offset + limit < totalCount):
            try:
                result = StorageManagerService.get_data(group=Storage.STORAGE_METHOD_GROUP, limit=limit, offset=offset)
                result = ValueParser.get_dict(result)

                groups = ValueParser.get_list(result["data"])
                totalCount = int(result["totalRecord"])
                offset += limit

                if groups:
                    for group in groups:
                        allMethodGroupIdPairs[ValueParser.get_number(group["appDataKey"])] = ValueParser.get_number(group["appDataValue"])

            except Exception as e:
                Logger.log_debug("Storage.list_all_groups err: " + str(e))
                break

        return allMethodGroupIdPairs

    @staticmethod
    def store_rule(ruleDTO):
        try:
            ruleId = ruleDTO.get_rule_id()

            triggerDTO = ruleDTO.get_trigger()
            triggerDict = {TriggerDTO.PROP_TYPE:triggerDTO.get_type(), TriggerDTO.PROP_VALUE:triggerDTO.get_value()}

            condDTOs = ruleDTO.get_conditions()
            conds = []
            for condDTO in condDTOs:
                conds.append({MethodDTO.PROP_METHOD_ID:condDTO.get_method_id(),
                              MethodDTO.PROP_METHOD_ARGS:[{AppConstants.ARG_NAME:methodArg.get(AppConstants.ARG_NAME),
                                                           AppConstants.ARG_CURRENT_VALUE:methodArg.get(AppConstants.ARG_CURRENT_VALUE)}
                                                          for methodArg in condDTO.get_method_args()]})

            execDTOs = ruleDTO.get_executions()
            execs = []
            for execDTO in execDTOs:
                execs.append({MethodDTO.PROP_METHOD_ID:execDTO.get_method_id(),
                              MethodDTO.PROP_METHOD_ARGS:[{AppConstants.ARG_NAME:methodArg.get(AppConstants.ARG_NAME),
                                                           AppConstants.ARG_CURRENT_VALUE:methodArg.get(AppConstants.ARG_CURRENT_VALUE)}
                                                           for methodArg in execDTO.get_method_args()]})


            StorageManagerService.set_data(Storage.STORAGE_RULE, ruleId, json.dumps({RuleDTO.PROP_TRIGGER:triggerDict,
                                                                                     RuleDTO.PROP_CONDITION:conds,
                                                                                     RuleDTO.PROP_EXECUTION:execs,
                                                                                     RuleDTO.PROP_ENABLED:ruleDTO.get_enabled(),
                                                                                     RuleDTO.PROP_RULE_NAME:ruleDTO.get_rule_name(),
                                                                                     RuleDTO.PROP_RULE_ID:ruleDTO.get_rule_id()}))
        except Exception as e:
            Logger.log_debug("Store Rule Err:", e)

    @staticmethod
    def delete_rule(ruleId):
        try:
            StorageManagerService.del_data(Storage.STORAGE_RULE, ruleId)
        except:
            pass

    @staticmethod
    def store_group(groupId, groupLabel):
        try:
            if not Util.is_empty(groupLabel):
                StorageManagerService.set_data(Storage.STORAGE_GROUP, groupId, groupLabel)
        except Exception as e:
            Logger.log_debug("Store Group Err:", e)

    @staticmethod
    def delete_group(groupId):
        try:
            StorageManagerService.del_data(Storage.STORAGE_GROUP, groupId)
        except:
            pass

    @staticmethod
    def delete_all_groups():
        try:
            StorageManagerService.del_data(Storage.STORAGE_GROUP)
        except:
            pass

    @staticmethod
    def store_method_group(methodId, groupId):
        try:
            StorageManagerService.set_data(Storage.STORAGE_METHOD_GROUP, str(int(methodId)), str(int(groupId)))
        except Exception as e:
            Logger.log_debug("Store Method Group Err:", e)

    @staticmethod
    def delete_method_group(methodId):
        try:
            StorageManagerService.del_data(Storage.STORAGE_METHOD_GROUP, str(int(methodId)))
        except:
            pass

