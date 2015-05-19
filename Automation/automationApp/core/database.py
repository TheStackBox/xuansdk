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
import json
import os
import sqlite3
import threading
import time
import traceback

from automationApp.core.triggerController import TriggerController
from automationApp.utils.databaseAdapter import DatabaseAdapter
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class Database:
    
    
    RESOURCE_PATH = "/install/python/2000300/resources/sqlscripts" # Arrange sub folders according to version number.
    DATABASE = "/install/python/2000300/.sybdata/database.db"
    
    __LOCK = threading.Lock()
    __INSTANCE = None
    
    # Callback Functions (Override them)
    KBX_GROUP_AFTER_UPDATE_ON_KBX_GROUP_ICON = lambda kbxGroupId: True
    KBX_METHOD_AFTER_DELETE = lambda kbxMethodId: True
    KBX_METHOD_AFTER_UPDATE_ON_KBX_METHOD_STATUS = lambda kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus: True
    RULE_AFTER_UPDATE_ON_STATUS_PROCESSED_ENABLED = lambda ruleId, oldEnabled, newEnabled, oldStatusProcessed, newStatusProcessed: True
    
    @staticmethod
    def instance():
        with Database.__LOCK:
            Database.__INSTANCE or Database()
            return Database.__INSTANCE
    
    def __init__(self):
        Database.__INSTANCE = self

        #=======================================================================
        # *** Do not change to threading.Lock()
        # RLock is required because db callback methods might call to execute functions 
        # (which is currently locked by the caller, but both of them are in the same thread)
        #=======================================================================
        self.__rlock = threading.RLock()
        
        # Build hidden path if not exists.
        if not os.path.exists("/install/python/2000300/.sybdata/"):
            os.mkdir("/install/python/2000300/.sybdata/")
        
        #=======================================================================
        # Add custom data type to SQLite.
        #=======================================================================
        # Supports type 'BOOLVAL'
        sqlite3.register_adapter(bool, DatabaseAdapter.ADAPT_BOOLEAN)
        sqlite3.register_converter("BOOLVAL", DatabaseAdapter.CONVERT_BOOLEAN) # Not sure why "BOOLEAN" is not working in XUAN box.
        
        # Support type 'DICTIONARY'
        sqlite3.register_adapter(dict, DatabaseAdapter.ADAPT_DICTIONARY)
        sqlite3.register_converter("DICTIONARY", DatabaseAdapter.CONVERT_DICTIONARY)
        
        # Support type 'LIST'
        sqlite3.register_adapter(list, DatabaseAdapter.ADAPT_LIST)
        sqlite3.register_converter("LIST", DatabaseAdapter.CONVERT_LIST)
        
        self.__con = sqlite3.connect(Database.DATABASE, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.__con.row_factory = sqlite3.Row
        
        #=======================================================================
        # ** DO NOT modify existing updates. **
        # @UPDATE: Just append. Database version will be increased automatically. 
        # Append here for statements to be executed only once per version upgrade.
        # Signature: [lambda path: True]
        #=======================================================================
        self.__runOnce = deque()
        self.__runOnce.append(self.db_1_update) # 1
        self.__runOnce.append(self.db_2_update) # 2
        self.__runOnce.append(self.db_3_update) # 3
        
        #=======================================================================
        # ** DO NOT modify existing updates. **
        # @UPDATE: Append and each versions will runs.
        # Append here for statements to be executed on each reboot.
        # Signature: [lambda: True]
        #=======================================================================
        self.__run = deque()
        self.__run.append(self.db_1_functions) # 1
        self.__run.append(self.db_2_functions) # 2
        self.__run.append(self.db_3_functions) # 3
        
    def initialize(self):
        currentVersion = self.get_user_version()
        for updateToVersion, (__runOnce, __run) in enumerate(zip(self.__runOnce, self.__run), 1): # First version = 1, not 0.
            if updateToVersion > currentVersion:
                # Performs run once function call on later versions only.
                try:
                    __runOnce("/".join((Database.RESOURCE_PATH, str(updateToVersion))))
                except Exception as e:
                    Logger.log_error("Error on updating to version", updateToVersion, "ex:", e)
                    raise Exception("Failed to initialize database: error on run-once function for version " +
                                    str(updateToVersion))
                
            # Executes all custom functions
            try:
                __run()
            except Exception as e:
                Logger.log_error("Error on version", updateToVersion, "function execution, ex:", e)
                raise Exception("Failed to initialize database: error on run-everytime function for version " +
                                str(updateToVersion))
        else:
            del(self.__runOnce)
            del(self.__run)
                
        self.set_user_version(updateToVersion)
        
    def get_user_version(self):
        cursor = self.__con.cursor()
        cursor.execute("PRAGMA user_version")
        userVersion = cursor.fetchone()["user_version"]
        cursor.close()
        return userVersion
    
    def set_user_version(self, version):
        cursor = self.__con.cursor()
        cursor.execute("PRAGMA user_version=" + str(int(version)))
        cursor.close()
        
    def execute(self, stmt, bindings=None):
        '''
        Execute only the statement without any return value.
        '''
        with self.__rlock:
            cursor = self.__con.cursor()
            try:
                if bindings is None:
                    cursor.execute(str(stmt))
                else:
                    cursor.execute(str(stmt), tuple(bindings))
            except Exception as e:
                Logger.log_error("Database.execute ex:", e)
                traceback.print_exc()
                raise e
            finally:
                cursor.close()
                
    def insert(self, stmt, bindings):
        '''
        The only different from "execute" is that this function returns lastrowid.
        '''
        with self.__rlock:
            cursor = self.__con.cursor()
            try:
                cursor.execute(stmt, bindings)
                lastrowid = cursor.lastrowid
                return lastrowid
            except Exception as e:
                Logger.log_error("Database.insert ex:", e)
                Logger.log_debug("Statement:", stmt, "bindings:", bindings)
                traceback.print_exc()
                raise e
            finally:
                cursor.close()
    
    def execute_and_fetch_all(self, stmt, bindings=None):
        '''
        Returns a list of sqlite.Row instances.
        The "list" if empty if no result was fetched.
        '''
        with self.__rlock:
            cursor = self.__con.cursor()
            try:
                if bindings is None:
                    cursor.execute(str(stmt))
                else:
                    cursor.execute(str(stmt), tuple(bindings))
                    
                return cursor.fetchall()
            except Exception as e:
                Logger.log_error("Database.execute_and_fetch_all ex:", e)
                traceback.print_exc()
                raise e
            finally:
                cursor.close()
            
    def execute_and_fetch_one(self, stmt, bindings=None):
        '''
        Returns an sqlite.Row instance.
        Return value is None if the statement fetch no result.
        '''
        with self.__rlock:
            cursor = self.__con.cursor()
            try:
                if bindings is None:
                    cursor.execute(str(stmt))
                else:
                    cursor.execute(str(stmt), tuple(bindings))
                    
                return cursor.fetchone()
            except Exception as e:
                Logger.log_error("Database.execute_and_fetch_all ex:", e)
                traceback.print_exc()
                raise e
            finally:
                cursor.close()
            
    def rollback(self):
        with self.__rlock:
            try:
                return self.__con.rollback()
            except Exception as e:
                Logger.log_error("Database.rollback ex:", e)
                traceback.print_exc()

    def commit(self):
        with self.__rlock:
            try:
                return self.__con.commit()
            except Exception as e:
                Logger.log_error("Database.commit ex:", e)
                traceback.print_exc()

    #===========================================================================
    # Version migrating functions
    # @UPDATE: Add migration code here
    #===========================================================================
    def __execute_script(self, scriptFile):
        with open(scriptFile, mode='r') as sqlFile:
            scripts = sqlFile.read()
            self.__con.executescript(scripts)
            self.__con.commit()
    
    def db_1_update(self, resourcePath):
        
        Logger.log_info("Database v1 update started")
                
        self.__execute_script("/".join([resourcePath, "tablestructure.sql"]))
        Logger.log_info("Database v1 update: Table structures built")
        
        # #################### Migration codes ####################
        try:
            from automationApp.migration.storage import Storage
            allGroups = Storage.list_all_groups()
            if len(allGroups) > 0: # Probably no rule is set.
                '''
                All Groups: e.g. {25: 'Yeelight Blue II'}
                '''
                for kbxGroupId, kbxGroupLabel in allGroups.items():
                    self.__con.execute('INSERT INTO "kbx_group"("kbxGroupId", "kbxGroupLabel", "kbxGroupStatus") VALUES (?, ?, ?)', 
                                       (kbxGroupId, kbxGroupLabel, -1))
                del(allGroups)
                    
                '''
                All Groups Methods: e.g. {69: 25, 71: 25}
                '''
                allMethodGroups = Storage.list_all_method_groups()
                for kbxMethodId, kbxGroupId in allMethodGroups.items():
                    self.__con.execute('INSERT INTO "kbx_method"("kbxMethodId", "kbxGroupId", "kbxMethodStatus") ' + \
                                       'VALUES (?, ?, ?)',
                                       (kbxMethodId, kbxGroupId, -1))
                    
                '''
                All Rules: e.g. [{
                    'execution': [{'kbxMethodId': 71, 'kbxMethodParams': [{'kbxParamCurrentValue': '4', 'kbxParamName': 'pairedDeviceId'},{'kbxParamCurrentValue': [False], 'kbxParamName': 'on'}]}], 
                    'trigger': {'type': 0, 'value': None}, 
                    'ruleId': '1425284835.0756288', 
                    'enabled': True, 
                    'condition': [{'kbxMethodId': 69, 'kbxMethodParams': [{'kbxParamCurrentValue': '4', 'kbxParamName': 'pairedDeviceId'}, {'kbxParamCurrentValue': [True], 'kbxParamName': 'on'}]}], 
                    'ruleName': 'ReTestet'
                }]
                '''
                allRules = Storage.list_all_rules()
                cursor = self.__con.cursor()
                createdTime = updatedTime = time.time()
                triggerController = TriggerController.instance()
                for sort, rule in enumerate(allRules):
                    trigger = triggerController.parse_to_trigger_dto(rule["trigger"])
                    cursor.execute('INSERT INTO "rule"("ruleName", "ruleProtected", "trigger", "enabled", "statusProcessed", "createdTime", "updatedTime", "sort") ' + \
                                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                   (rule["ruleName"], False, json.dumps(trigger), 
                                    rule["enabled"], "updated", createdTime, 
                                    updatedTime, sort))
                    
                    ruleId = cursor.lastrowid
                    for vals in (["execution", "rule_execution", "reRuleId"], ["condition", "rule_condition", "rcRuleId"]):
                        for kbxMethodSort, kbxMethodWithCurrentValue in enumerate(rule[vals[0]]):
                            self.__con.execute('INSERT INTO "' + vals[1] + '"("' + vals[2] + '", "kbxMethodId", "kbxMethodParams", "createdTime", "sort") ' + \
                                               'VALUES (?, ?, ?, ?, ?)',
                                               (ruleId, kbxMethodWithCurrentValue["kbxMethodId"], 
                                                json.dumps(kbxMethodWithCurrentValue["kbxMethodParams"]), 
                                                createdTime, kbxMethodSort))
                cursor.close()
                del(allRules)
                
                self.__con.commit()
                
        except Exception as e:
            self.__con.rollback()
            Logger.log_warning("Database failed to migrate rules from system, ex:", e , "---- rolled back")
            
        else:
            Logger.log_info("Database v1 update: Rules migrated")
            try:
                Storage.delete_all_rules()
                Storage.delete_all_method_groups()
                Storage.delete_all_groups()
            except Exception as e:
                Logger.log_warning("Database failed to remove rules from system after migration, ex:", e)
        # #################### End of migration codes ####################
        
        self.__execute_script("/".join([resourcePath, "triggers.sql"]))
        Logger.log_info("Database v1 update: Triggers built")

        self.__execute_script("/".join([resourcePath, "indexes.sql"]))
        Logger.log_info("Database v1 update: Indexes built")
                
        Logger.log_info("Database v1 update completed")
        
    def db_2_update(self, resourcePath):
        self.__execute_script("/".join([resourcePath, "tablestructure.sql"]))
        Logger.log_info("Database v2 update: Table structures built")
        
        Logger.log_info("Database v2 update completed")
        
    def db_3_update(self, resourcePath):
        ''' convert all "rgb" to "hsb" '''
        from com.cloudMedia.theKuroBox.sdk.util.colorUtils import ColorUtils
        
        for idCol, tableName in [("reId", "rule_execution"), ("seId", "scene_execution")]:
        
            toBeUpdateds = deque()
            rows = self.__con.execute('SELECT "' + idCol + '", "kbxMethodParams" ' + \
                                      'FROM "' + tableName + '" ' + \
                                      'WHERE "kbxMethodParams" LIKE ?', ('%"r"%', )).fetchall()
            for row in rows:
                methodRow = dict(row)
                kbxMethodParams = methodRow["kbxMethodParams"]
                for kbxMethodParam in kbxMethodParams:
                    kbxParamCurrentValue = kbxMethodParam["kbxParamCurrentValue"]
                    if isinstance(kbxParamCurrentValue, dict):
                        if not {"r", "g", "b"}.difference(kbxParamCurrentValue):
                            hsbDict = ColorUtils.rgb_to_hsb(kbxParamCurrentValue["r"], 
                                                            kbxParamCurrentValue["g"], 
                                                            kbxParamCurrentValue["b"])
                            kbxMethodParam["kbxParamCurrentValue"] = hsbDict
                            toBeUpdateds.append(methodRow)
            
            for methodRow in toBeUpdateds:
                self.__con.execute('UPDATE "' + tableName + '" SET "kbxMethodParams"=? WHERE "' + idCol + '"=?', 
                                   (methodRow["kbxMethodParams"], methodRow[idCol]))
                
            Logger.log_info("Database v3 update: RGB -> HSB (%i entries from %s migrated)" % (len(toBeUpdateds), str(tableName)))    
                
        Logger.log_info("Database v3 update completed")
                            
    #===========================================================================
    # Custom functions for database
    # @UPDATE: Add custom functions right here
    #===========================================================================
    def db_1_functions(self):
        # Internally processed relationships among tables.
        self.__con.create_function("kbx_group_after_update_on_kbxGroupIcon", 1, self.kbx_group_after_update_on_kbxGroupIcon)
        self.__con.create_function("kbx_method_after_update_on_kbxGroupId", 3, self.kbx_method_after_update_on_kbxGroupId)
        self.__con.create_function("kbx_method_after_delete", 2, self.kbx_method_after_delete)
        self.__con.create_function("rule_after_delete", 1, self.rule_after_delete)
        self.__con.create_function("scene_after_delete", 1, self.scene_after_delete)
        self.__con.create_function("rule_condition_after_delete", 1, self.rule_condition_after_delete)
        self.__con.create_function("rule_execution_after_delete", 1, self.rule_execution_after_delete)
        self.__con.create_function("scene_execution_after_delete", 1, self.scene_execution_after_delete)
        
        # Notify when to execute rules.
        self.__con.create_function("rule_after_update_on_statusProcessed_and_enabled", 5, self.rule_after_update_on_statusProcessed_enabled)
        self.__con.create_function("kbx_method_after_update_on_kbxMethodStatus", 3, self.kbx_method_after_update_on_kbxMethodStatus)
        
    def db_2_functions(self):
        return
    
    def db_3_functions(self):
        return
        
    #===========================================================================
    # Database callback functions
    # @UPDATE: Add callback function entries here.
    #===========================================================================
    # ----- kbx_group -----
    def kbx_group_after_update_on_kbxGroupIcon(self, kbxGroupId):
        '''
        As per observed, only if kbxGroupIcon updated requires to notify.
        '''
        Database.KBX_GROUP_AFTER_UPDATE_ON_KBX_GROUP_ICON(kbxGroupId)

    # ----- kbx_method -----
    def kbx_method_after_update_on_kbxGroupId(self, kbxMethodId, oldKBXGroupId, newKBXGroupId):
        if oldKBXGroupId != newKBXGroupId:
            if Util.is_empty(oldKBXGroupId):
                return
            
            self.__delete_kbx_group_if_necessary(oldKBXGroupId)
    
    def kbx_method_after_delete(self, kbxMethodId, kbxGroupId):
        if Util.is_empty(kbxGroupId):
            return
        self.__delete_kbx_group_if_necessary(kbxGroupId)
        
        try:
            Database.KBX_METHOD_AFTER_DELETE(kbxMethodId)
        except Exception as e:
            Logger.log_warning("Database.KBX_METHOD_AFTER_DELETE raised error:", e)
            
    # ----- rule -----
    def rule_after_delete(self, ruleId):
        # Remove entries from "rule_condition" and "rule_execution".
        self.__con.execute('DELETE FROM "rule_condition" WHERE rcRuleId=?', (ruleId,))
        self.__con.execute('DELETE FROM "rule_execution" WHERE reRuleId=?', (ruleId,))
    
    # ----- scene -----
    def scene_after_delete(self, sceneId):
        # Remove entries from "scene_execution".
        self.__con.execute('DELETE FROM "scene_execution" WHERE seSceneId=?', (sceneId,))
        
    # ----- rule_condition -----
    def rule_condition_after_delete(self, kbxMethodId):
        self.__delete_kbx_method_if_neccessary(kbxMethodId)
        
    # ----- rule_execution -----
    def rule_execution_after_delete(self, kbxMethodId):
        self.__delete_kbx_method_if_neccessary(kbxMethodId)
        
    # ----- scene_execution -----
    def scene_execution_after_delete(self, kbxMethodId):
        self.__delete_kbx_method_if_neccessary(kbxMethodId)
        
    def rule_after_update_on_statusProcessed_enabled(self, ruleId, oldEnabled, newEnabled, oldStatusProcessed, newStatusProcessed):
        Database.RULE_AFTER_UPDATE_ON_STATUS_PROCESSED_ENABLED(ruleId, DatabaseAdapter.CONVERT_BOOLEAN(oldEnabled), 
                                                               DatabaseAdapter.CONVERT_BOOLEAN(newEnabled), 
                                                               oldStatusProcessed, newStatusProcessed)
        
    def kbx_method_after_update_on_kbxMethodStatus(self, kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus):
        Database.KBX_METHOD_AFTER_UPDATE_ON_KBX_METHOD_STATUS(kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus)
        
    def __delete_kbx_group_if_necessary(self, kbxGroupId):
        # Remove group from kbx_group if no more reference.
        result = self.__con.execute('SELECT "kbxGroupId" FROM "kbx_method" WHERE "kbxGroupId"=? LIMIT 1', (kbxGroupId,))
        if result.fetchone() is None:
            self.__con.execute('DELETE FROM "kbx_group" WHERE kbxGroupId=?', (kbxGroupId,))
        
    def __delete_kbx_method_if_neccessary(self, kbxMethodId):
        for tableToCheck in ("rule_condition", "rule_execution", "scene_execution"):
            result = self.__con.execute('SELECT "kbxMethodId" ' + 
                                        'FROM "' + tableToCheck + 
                                        '" WHERE "kbxMethodId"=? LIMIT 1', 
                                        (kbxMethodId,))
            if result.fetchone() is not None:
                # Return if at least one row is still referencing.
                return
        
        # Remove because no more referencing.
        self.__con.execute('DELETE FROM "kbx_method" WHERE "kbxMethodId"=?', (kbxMethodId,))
        
    #===========================================================================
    # End of Database callback functions
    #===========================================================================
        
