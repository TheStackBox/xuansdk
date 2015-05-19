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

from collections import deque

from automationApp.utils.valueParser import ValueParser
from com.cloudMedia.theKuroBox.sdk.service.storageManagerService import StorageManagerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class Storage(object):

    STORAGE_GROUP = "automation_group"
    STORAGE_RULE = "automation_rule"
    STORAGE_METHOD_GROUP = "automation_method_group"
    
    @staticmethod
    def list_all_rules():
        offset = 0
        limit = 50

        totalCount = 1
        allRules = deque()
        while(offset < totalCount):
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

        totalCount = 1
        allGroupLabels = {}
        while(offset < totalCount):
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

        totalCount = 1
        allMethodGroupIdPairs = {}
        while(offset < totalCount):
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
    def delete_all_rules():
        try:
            StorageManagerService.del_data(Storage.STORAGE_RULE)
        except Exception as e:
            Logger.log_warning("Migration.Storage.delete_all_rules ex:", e)

    @staticmethod
    def delete_all_groups():
        try:
            StorageManagerService.del_data(Storage.STORAGE_GROUP)
        except Exception as e:
            Logger.log_warning("Migration.Storage.delete_all_groups ex:", e)

    @staticmethod
    def delete_all_method_groups():
        try:
            StorageManagerService.del_data(Storage.STORAGE_METHOD_GROUP)
        except Exception as e:
            Logger.log_warning("Migration.Storage.delete_all_method_groups ex:", e)

