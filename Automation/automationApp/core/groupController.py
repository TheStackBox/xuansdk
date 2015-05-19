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
import threading
import traceback

from automationApp.core.database import Database
from automationApp.module.controllerModule import ControllerModule
from automationApp.utils.sharedMethodWrapper import SharedMethodWrapper
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class GroupController:
    '''
    Keep track of groups.
    
    * No remove group method because it will be handled by database.
    '''
    
    
    __INSTANCE = None
    __LOCK = threading.Lock()
    
    
    @staticmethod
    def instance():
        with GroupController.__LOCK:
            GroupController.__INSTANCE or GroupController()
            return GroupController.__INSTANCE
    
    def __init__(self):
        GroupController.__INSTANCE = self

        self.__db = Database.instance()
        self.__lock = threading.Lock()
        self.__lock___group_icon_change = threading.Lock()
        self.__group_icon_change_callbacks = set([])
        
        ControllerModule.ON_SHARED_METHOD_GROUP_UPDATED = self.__on_shared_method_group_updated
        ControllerModule.ON_SHARED_METHOD_GROUP_DELETED = self.__on_shared_method_group_deleted

    def listen_to_group_icon_change(self, aFunc):
        '''
        Callback when a rule is:
        1. Has item group icon is updated.
    
        aFunc:Function - Parameters (kbxGroupId))
        '''
        with self.__lock___group_icon_change:
            
            # Listen to database change if this is the first time register.
            if len(self.__group_icon_change_callbacks) == 0:
                
                def on_group_icon_change(*args, **kwargs):
                    
                    with self.__lock___group_icon_change: 

                        for callback in self.__group_icon_change_callbacks:
                            try:
                                callback(*args, **kwargs)
                            except Exception as e:
                                Logger.log_warning("GroupController.listen_to_group_icon_change.on_group_icon_change callback ex:", e)
                    
                Database.KBX_GROUP_AFTER_UPDATE_ON_KBX_GROUP_ICON = on_group_icon_change
            
            self.__group_icon_change_callbacks.add(aFunc)

    def add(self, kbxGroupIds):
        '''
        Receives a list of group IDs and;
        1. Check which group IDs still not yet in database.
        2. Insert into database (if not yet exists).
        '''
        with self.__lock:
            kbxGroupIds = set(kbxGroupIds)
            
            # Find out group IDs which not yet exists in database.
            groupIdsSQL = ",".join(str(groupId) for groupId in kbxGroupIds)
            result = self.__db.execute_and_fetch_all('SELECT "kbxGroupId" FROM "kbx_group" WHERE "kbxGroupId" IN (%s)' % groupIdsSQL)
            existGroupIds = [row["kbxGroupId"] for row in result]
            nonexistGroupIds = kbxGroupIds.difference(existGroupIds)
            
            expectedNumberOfGroups = len(nonexistGroupIds)
            if expectedNumberOfGroups == 0:
                return # No non-exist group.
            
            # List shared method groups from system app.
            try:
                kbxGroups = SharedMethodWrapper.list_shared_method_groups(kbxGroupId=nonexistGroupIds, enableTagCount=False)
            except:
                kbxGroups = []
            
            # Insert all into database. Check here for multiple inserts in one statement: http://stackoverflow.com/a/5009740/1640033
            groupDictionary = {kbxGroup["kbxGroupId"]:kbxGroup for kbxGroup in kbxGroups}            
            
            def build_parameter(groupId):
                defaultGroup = {"kbxGroupId":groupId,
                                "kbxGroupName":None,
                                "kbxGroupParentId":None,
                                "kbxGroupLabel":None,
                                "kbxGroupIcon":None,
                                "kbxGroupStatus":-1}
                kbxGroup = groupDictionary.get(groupId, defaultGroup)
                return [kbxGroup["kbxGroupId"], kbxGroup["kbxGroupName"], kbxGroup["kbxGroupParentId"], 
                        kbxGroup.get("kbxGroupLabel"), kbxGroup.get("kbxGroupIcon"), kbxGroup.get("kbxGroupStatus", 1)]

            bulkInsertSQLs = ['INSERT INTO "kbx_group" ("kbxGroupId", "kbxGroupName", "kbxGroupParentId", "kbxGroupLabel", "kbxGroupIcon", "kbxGroupStatus")'] + \
                             ['SELECT ? AS "kbxGroupId", ? AS "kbxGroupName", ? AS "kbxGroupParentId", ? AS "kbxGroupLabel", ? AS "kbxGroupIcon", ? AS "kbxGroupStatus"'] + \
                             ['UNION SELECT ?, ?, ?, ?, ? ,?'] * (expectedNumberOfGroups - 1)
            
            parameters = deque()
            for groupId in nonexistGroupIds:
                parameters.extend(build_parameter(groupId))
            
            self.__db.execute(" ".join(bulkInsertSQLs), tuple(parameters))
            
    def update(self, kbxGroup):
        with self.__lock:
            # Variables
            kbxGroupId = kbxGroup["kbxGroupId"]
    
            # Update database where applicable.
            row = self.__db.execute_and_fetch_one('SELECT * FROM "kbx_group" WHERE "kbxGroupId"=? LIMIT 1', (kbxGroupId,))
            if row is None:
                return
            
            # Variables
            kbxGroupName = kbxGroup["kbxGroupName"]
            kbxGroupParentId = kbxGroup.get("kbxGroupParentId", None)
            kbxGroupLabel = kbxGroup.get("kbxGroupLabel", None)
            kbxGroupIcon = kbxGroup.get("kbxGroupIcon", None)
            
            updateSQLs = deque()
            updateSQLValues = deque()
            
            if row["kbxGroupName"] != kbxGroupName and not Util.is_empty(kbxGroupName):
                updateSQLs.append('"kbxGroupName"=?')
                updateSQLValues.append(str(kbxGroupName))
                
            if row["kbxGroupParentId"] != kbxGroupParentId and not Util.is_empty(kbxGroupParentId):
                updateSQLs.append('"kbxGroupParentId"=?')
                updateSQLValues.append(int(kbxGroupParentId))
                
            if row["kbxGroupLabel"] != kbxGroupLabel and not Util.is_empty(kbxGroupLabel):
                updateSQLs.append('"kbxGroupLabel"=?')
                updateSQLValues.append(str(kbxGroupLabel))
                
            if row["kbxGroupIcon"] != kbxGroupIcon and not Util.is_empty(kbxGroupIcon):
                updateSQLs.append('"kbxGroupIcon"=?')
                updateSQLValues.append(str(kbxGroupIcon))
                
            if row["kbxGroupStatus"] != 1:
                updateSQLs.append('"kbxGroupStatus"=?')
                updateSQLValues.append(1)
                
            if len(updateSQLs) > 0:
                updateSQLValues.append(kbxGroupId)
                updateSQL = 'UPDATE "kbx_group" SET %s WHERE "kbxGroupId"=?' % ", ".join(updateSQLs)
                self.__db.execute(updateSQL, tuple(updateSQLValues))
                self.__db.commit()
    
    def delete(self, kbxGroupId):
        with self.__lock:
            result = self.__db.execute_and_fetch_all('SELECT "kbxGroupStatus" FROM "kbx_group" WHERE "kbxGroupId"=? LIMIT 1', (kbxGroupId,))
            if len(result) == 1:
                row = result[0]
                if row["kbxGroupStatus"] != -1:
                    self.__db.execute('UPDATE "kbx_group" SET "kbxGroupStatus"=? WHERE "kbxGroupId"=?', (-1, kbxGroupId))
                    self.__db.commit()
        
    def list(self, offset, limit):
        '''
        Used by APIService for debugging purpose.
        '''
        result = self.__db.execute_and_fetch_all('SELECT * FROM "kbx_group" LIMIT ?, ?', (offset, limit))
        return result
            
    def __on_shared_method_group_updated(self, eventObject):
        '''
        Triggered based on event broadcasted by system app.
        '''
        try:
            eventData = json.loads(eventObject["eventData"])
            self.update(eventData) # eventData = kbxGroup
        except Exception as e:
            Logger.log_error("GroupController.__on_shared_method_group_updated ex:", e)
            traceback.print_exc()
    
    def __on_shared_method_group_deleted(self, eventObject):
        '''
        Triggered based on event broadcasted by system app.
        '''
        try:
            eventData = json.loads(eventObject["eventData"])
            kbxGroupId = eventData["kbxGroupId"]
            self.delete(kbxGroupId)
        except Exception as e:
            Logger.log_error("GroupController.__on_shared_method_group_deleted ex:", e)
            traceback.print_exc()

            