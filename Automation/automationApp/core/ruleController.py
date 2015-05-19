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
import time

from automationApp.appConstants import AppConstants
from automationApp.core.database import Database
from automationApp.utils.valueParser import ValueParser


class RuleController:


    def __init__(self):
        self.__db = Database.instance()
        
    def listen_to_rule_status_change(self, aFunc):
        '''
        aFunc:Function - Parameters (ruleId, oldEnabled, newEnabled, oldStatusProcessed, newStatusProcessed)
        '''
        Database.RULE_AFTER_UPDATE_ON_STATUS_PROCESSED_ENABLED = aFunc

    def update(self, rule):
        ''' UPDATE INTO DATABASE '''
        ruleId = rule["ruleId"]
        ruleProtected = rule["ruleProtected"]
        ruleName = rule["ruleName"]
        trigger = rule["trigger"]
        enabled = rule["enabled"]
        condition = rule["condition"]
        execution = rule["execution"]
        
        createdTime = updatedTime = int(time.time())
        
        def build_parameters(kbxMethod):
            return [ruleId, kbxMethod["kbxMethodId"], kbxMethod["kbxMethodParams"], createdTime]
        
        # Update conditions
        expectedNumbersOfConds = len(condition)
        if expectedNumbersOfConds > 0:
            bulkInsertSQLs = ['INSERT INTO "rule_condition"("rcRuleId", "kbxMethodId", "kbxMethodParams", "createdTime", "sort")'] + \
                             ['SELECT ? AS "rcRuleId", ? AS "kbxMethodId", ? AS "kbxMethodParams", ? AS "createdTime", ? AS "sort"'] + \
                             ['UNION SELECT ?, ?, ?, ? ,?'] * (expectedNumbersOfConds - 1)
            parameters = deque()
            for sort, kbxMethod in enumerate(condition, 1):
                parameters.extend(build_parameters(kbxMethod))
                parameters.append(sort)
            self.__db.execute(" ".join(bulkInsertSQLs), tuple(parameters))
        
        self.__db.execute('DELETE FROM "rule_condition" WHERE "rcRuleId"=? AND "createdTime"<>?', (ruleId, createdTime))
            
        # Update executions
        expectedNumbersOfExecs = len(execution)
        if expectedNumbersOfExecs > 0:
            bulkInsertSQLs = ['INSERT INTO "rule_execution"("reRuleId", "kbxMethodId", "kbxMethodParams", "createdTime", "sort")'] + \
                             ['SELECT ? AS "reRuleId", ? AS "kbxMethodId", ? AS "kbxMethodParams", ? AS "createdTime", ? AS "sort"'] + \
                             ['UNION SELECT ?, ?, ?, ?, ?'] * (expectedNumbersOfExecs - 1)
            parameters = deque()
            for sort, kbxMethod in enumerate(execution, 1):
                parameters.extend(build_parameters(kbxMethod))
                parameters.append(sort)
            self.__db.execute(" ".join(bulkInsertSQLs), tuple(parameters))
        
        self.__db.execute('DELETE FROM "rule_execution" WHERE "reRuleId"=? AND "createdTime"<>?', (ruleId, createdTime))
            
        # Update rule info.
        # I need to do this last because it will trigger (__run) rule when "enabled" and "statusProcessed" is updated. Methods in rc and re must be up on that time.
        self.__db.execute('UPDATE "rule" ' + \
                          'SET "ruleProtected"=?, "ruleName"=?, "trigger"=?, "enabled"=?, "statusProcessed"=?, "updatedTime"=? ' + \
                          'WHERE "ruleId"=?',
                          (ruleProtected, ruleName, dict(trigger), enabled, AppConstants.RULE_STATUS_UPDATED, updatedTime, ruleId))
        
    def delete(self, ruleId):
        self.__db.execute('DELETE FROM "rule" WHERE "ruleId"=?', (ruleId,))
        
    def change_to_updating(self, ruleId, ruleName):
        '''
        Change an existing rule status to "updating".
        '''
        self.__db.execute('UPDATE "rule" SET "statusProcessed"=?, "ruleName"=? WHERE "ruleId"=?', \
                          (AppConstants.RULE_STATUS_UPDATING, ruleName, ruleId))
        
    def generate_id(self, ruleName):
        '''
        Generate a new entry for a rule, set the status to "updating" and return the newly generated row ID.
        '''
        sort = updatedTime = createdTime = int(time.time()) # Temporary use timestamp as sorting mechanism
        ruleId = self.__db.insert('INSERT INTO "rule"("statusProcessed", "ruleName", "createdTime", "updatedTime", "sort") ' + \
                                  'VALUES (?, ?, ?, ?, ?)', \
                                  (AppConstants.RULE_STATUS_UPDATING, ruleName, createdTime, updatedTime, sort))
        return ruleId
        
    def enable(self, ruleId, enabled):
        '''
        Set True/False to "enabled" of an existing rule.
        '''
        enabled = ValueParser.get_boolean(enabled)
        self.__db.execute('UPDATE "rule" SET "enabled"=? WHERE "ruleId"=?', (enabled, ruleId))
        
    def has(self, ruleId):
        '''
        Check if a given ruleId exists.
        '''
        result = self.__db.execute_and_fetch_one('SELECT "ruleId" FROM "rule" WHERE "ruleId"=? LIMIT 1', (ruleId,))
        return result is not None
    
    def get_status_processed(self, ruleId):
        result = self.__db.execute_and_fetch_all('SELECT "statusProcessed" FROM "rule" WHERE "ruleId"=? LIMIT 1', (ruleId,))
        return result[0]["statusProcessed"]
    
    def get_status_processed_and_enabled(self, ruleId):
        result = self.__db.execute_and_fetch_all('SELECT "statusProcessed", "enabled" FROM "rule" WHERE "ruleId"=? LIMIT 1', (ruleId,))
        row = result[0]
        return row["statusProcessed"], row["enabled"]
    
    def get(self, ruleId):
        '''
        Get rule without aggregating any execution and condition.
        '''
        result = self.__db.execute_and_fetch_all('SELECT * FROM "rule" WHERE "ruleId"=? LIMIT 1', (ruleId,))
        return result[0]

    def get_detail(self, ruleId):
        '''
        Get rule's full details based on a given ruleId.
        '''
        result = self.__db.execute_and_fetch_one('SELECT "ruleId", "ruleName", "ruleProtected", "trigger", "enabled", "statusProcessed", "sort" ' + \
                                                 'FROM "rule" ' + \
                                                 'WHERE "ruleId"=? ' + \
                                                 'LIMIT 1', (ruleId,))
        rule = dict(result)
        
        # Constants
        statusCodes = {-1:AppConstants.METHOD_ERROR_METHOD_REMOVED, 0:AppConstants.METHOD_ERROR_METHOD_OFF, 1:AppConstants.METHOD_ERROR_OK}
        
        ruleId = rule["ruleId"]
        ruleConds = rule["condition"] = deque()
        ruleExecs = rule["execution"] = deque()
        ruleStatusCode = AppConstants.METHOD_ERROR_OK
        if rule["statusProcessed"] == AppConstants.RULE_STATUS_UPDATED:
            # Aggregate rule conditions and executions
            for (table, column), l in {("rule_condition", "rcRuleId"): ruleConds, ("rule_execution", "reRuleId"): ruleExecs}.items():
                result1 = self.__db.execute_and_fetch_all('SELECT "m"."kbxGroupId", "kbxGroupLabel", "kbxGroupName", "kbxGroupIcon", "m"."kbxMethodId", ' + \
                                                          '"kbxMethodLabel", "kbxMethodName", "kbxMethodStatus", "kbxGroupStatus", "kbxMethodAppId", "kbxMethodParams" ' + \
                                                          'FROM "' + str(table) + '" AS "c", "kbx_method" AS "m", "kbx_group" AS "g" ' + \
                                                          'WHERE "' + str(column) + '"=? AND "c"."kbxMethodId"="m"."kbxMethodId" AND "m"."kbxGroupId"="g"."kbxGroupId" ' + \
                                                          'ORDER BY "sort"', (ruleId,))
                for row1 in result1:
                    item = dict(row1)
                    if item["kbxGroupStatus"] == -1:
                        statusCode = AppConstants.METHOD_ERROR_GROUP_REMOVED
                        item["statusCode"] = statusCode
                        ruleStatusCode |= statusCode
                    else:
                        statusCode = statusCodes[item["kbxMethodStatus"]]
                        item["statusCode"] = statusCode
                        ruleStatusCode |= statusCode
                    
                    l.append(item)
            
            rule["statusCode"] = ruleStatusCode
        
        return rule
    
    def get_summary(self, ruleId):
        '''
        Get rule's summary based on rule ID.
        '''
        result = self.__db.execute_and_fetch_one('SELECT "ruleId", "ruleName", "enabled", "statusProcessed", "sort" FROM "rule" WHERE "ruleId"=? LIMIT 1', (ruleId,))
        rule = dict(result)
        self.__aggregate_condition_and_execution(rule) # Modified by reference.
        return rule
        
    def list(self, offset=0, limit=20):
        '''
        List rules' summaries based on offset and limit.
        '''
        # Variables
        rules = deque()
        
        # List rules from offset to limit
        result = self.__db.execute_and_fetch_all('SELECT "ruleId", "ruleName", "enabled", "statusProcessed", "sort" ' + \
                                                 'FROM "rule" ' + \
                                                 'ORDER BY "sort" ' + \
                                                 'LIMIT ?, ?', (offset, limit))
        for row in result:
            rule = dict(row)
            self.__aggregate_condition_and_execution(rule) # Modified by reference.
            rules.append(rule)
            
        return rules
    
    def __aggregate_condition_and_execution(self, rule):
        # Constants
        statusCodes = {-1:AppConstants.METHOD_ERROR_METHOD_REMOVED, 0:AppConstants.METHOD_ERROR_METHOD_OFF, 1:AppConstants.METHOD_ERROR_OK}
        
        ruleId = rule["ruleId"]
        ruleConds = rule["condition"] = deque()
        ruleExecs = rule["execution"] = deque()
        ruleStatusCode = AppConstants.METHOD_ERROR_OK
        if rule["statusProcessed"] == AppConstants.RULE_STATUS_UPDATED:
            # Aggregate rule conditions and executions
            for (table, column), l in {("rule_condition", "rcRuleId"): ruleConds, ("rule_execution", "reRuleId"): ruleExecs}.items():
                result1 = self.__db.execute_and_fetch_all('SELECT "m"."kbxGroupId", "kbxGroupIcon", "kbxMethodStatus", "kbxGroupStatus" ' + \
                                                          'FROM "' + str(table) + '" AS "c", "kbx_method" AS "m", "kbx_group" AS "g" ' + \
                                                          'WHERE "' + str(column) + '"=? AND ' + \
                                                          '"c"."kbxMethodId"="m"."kbxMethodId" AND "m"."kbxGroupId"="g"."kbxGroupId" ' + \
                                                          'ORDER BY "sort"', (ruleId,))
                for row1 in result1:
                    item = dict(row1)
                    if item["kbxGroupStatus"] == -1:
                        statusCode = AppConstants.METHOD_ERROR_GROUP_REMOVED
                        item["statusCode"] = statusCode
                        ruleStatusCode |= statusCode
                    else:
                        statusCode = statusCodes[item["kbxMethodStatus"]]
                        item["statusCode"] = statusCode
                        ruleStatusCode |= statusCode
                    
                    l.append(item)
            
            rule["statusCode"] = ruleStatusCode
    
    def count(self):
        '''
        Count total existing rules.
        '''
        result = self.__db.execute_and_fetch_one('SELECT count("ruleId") AS "total" FROM "rule"')
        return result["total"]
    
    def commit(self):
        '''
        Commit after any update/insert/delete for it to take effect.
        '''
        self.__db.commit()
        
    def rollback(self):
        '''
        You can always rollback if any update/insert/delete failed.
        '''
        self.__db.rollback()
    
    def list_conditions(self, ruleId):
        '''
        List conditions by rule ID.
        '''
        return self.__db.execute_and_fetch_all('SELECT * ' + \
                                               'FROM "rule_condition", "kbx_method" ' + \
                                               'WHERE "rcRuleId"=? AND "kbx_method"."kbxMethodId"="rule_condition"."kbxMethodId"', (ruleId,))

    def list_executions(self, ruleId):
        '''
        List executions by rule ID.
        '''
        return self.__db.execute_and_fetch_all('SELECT * ' + \
                                               'FROM "rule_execution", "kbx_method" ' + \
                                               'WHERE "reRuleId"=? AND "kbx_method"."kbxMethodId"="rule_execution"."kbxMethodId"', (ruleId,))
    
    def list_rule_ids_which_has_kbx_method_id_as_condition(self, kbxMethodId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "rcRuleId" FROM "rule_condition" WHERE "kbxMethodId"=?', (kbxMethodId,))
        return [row["rcRuleId"] for row in result]
    
    def list_rule_ids_which_has_kbx_method_id_as_execution(self, kbxMethodId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "reRuleId" FROM "rule_execution" WHERE "kbxMethodId"=?', (kbxMethodId,))
        return [row["reRuleId"] for row in result]
    
    def list_rule_ids_which_has_kbx_group_id_as_condition(self, kbxGroupId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "rc"."rcRuleId" ' + \
                                                 'FROM "rule_condition" AS "rc", "kbx_method" AS "km" ' + \
                                                 'WHERE "rc"."kbxMethodId"="km"."kbxMethodId" AND "km"."kbxGroupId"=?', 
                                                 (kbxGroupId,))
        return [row["rcRuleId"] for row in result]
    
    def list_rule_ids_which_has_kbx_group_id_as_execution(self, kbxGroupId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "reRuleId" ' + \
                                                 'FROM "rule_execution" AS "re", "kbx_method" AS "km" ' + \
                                                 'WHERE "re"."kbxMethodId"="km"."kbxMethodId" AND "km"."kbxGroupId"=?', 
                                                 (kbxGroupId,))
        return [row["reRuleId"] for row in result]
    
    def list_rule_ids_which_are_enabled(self):
        result = self.__db.execute_and_fetch_all('SELECT "ruleId" FROM "rule" WHERE "enabled"=?', (True,))
        return (row["ruleId"] for row in result)
