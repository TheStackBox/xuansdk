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
from automationApp.core.eventController import EventController
from automationApp.core.groupController import GroupController
from automationApp.module.controllerModule import ControllerModule
from automationApp.utils.sharedMethodWrapper import SharedMethodWrapper
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class MethodController:
    '''
    Keep tracks and process methods.
    
    * No remove method's method because it will be handled by database.
    '''


    __INSTANCE = None
    __LOCK = threading.Lock()


    @staticmethod
    def instance():
        with MethodController.__LOCK:
            MethodController.__INSTANCE or MethodController()
            return MethodController.__INSTANCE

    def __init__(self):
        MethodController.__INSTANCE = self
        
        self.__db = Database.instance()
        self.__groupController = GroupController.instance()
        self.__eventController = EventController.instance()
        self.__lock___add = threading.Lock()
        self.__lock___method_status_change = threading.Lock()
        self.__method_status_change_callbacks = set([])
        
        ControllerModule.ON_SHARED_METHOD_UPDATED = self.__on_shared_method_updated
        ControllerModule.ON_SHARED_METHOD_DELETED = self.__on_shared_method_deleted
        
        Database.KBX_METHOD_AFTER_DELETE = self.__on_kbx_method_deleted
        
    def listen_to_method_status_change(self, aFunc):
        '''
        Callback when a rule is:
        1. Re-enabled. (enabled)
        2. One of the conditions re-activated. (condition_activated)
        3. Just changed statusProcessed from "updating" to "updated". (updated)
    
        aFunc:Function - Parameters (kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus))
        '''
        with self.__lock___method_status_change:
            
            # Listen to database change if this is the first time register.
            if len(self.__method_status_change_callbacks) == 0:
                
                def on_method_status_change(*args, **kwargs):
                    
                    with self.__lock___method_status_change: 

                        for callback in self.__method_status_change_callbacks:
                            try:
                                callback(*args, **kwargs)
                            except Exception as e:
                                Logger.log_warning("MethodController.listen_to_method_status_change.on_method_status_change callback ex:", e)
                    
                Database.KBX_METHOD_AFTER_UPDATE_ON_KBX_METHOD_STATUS = on_method_status_change
            
            self.__method_status_change_callbacks.add(aFunc)
                
    def add(self, kbxMethodIds):
        '''
        Receive a list of method Ids and;
        1. Check which one is not yet exists in database
        2. Get all groups in methods and pass to "groupController.py" for process.
        3. Register method events with "eventController.py" (where necessary and not yet exists).
        4. Insert all methods into database (if not yet exists).
        '''
        with self.__lock___add:
            kbxMethodIds = set(kbxMethodIds)
            
            # Check which methods exists in database "kbx_method"
            methodIdsSQL = ",".join((str(methodId) for methodId in kbxMethodIds))
            result = self.__db.execute_and_fetch_all('SELECT "kbxMethodId" FROM "kbx_method" WHERE "kbxMethodId" IN (%s)' % methodIdsSQL)
            existMethodIds = [row["kbxMethodId"] for row in result]
            
            # Find out method IDs which ain't exists.
            nonexistMethodIds = kbxMethodIds.difference(existMethodIds)
            expectedNumbersOfMethods = len(nonexistMethodIds)
            if expectedNumbersOfMethods == 0:
                return # Returns if all IDs already exist.
            
            # Sekali gus get all methods from system app.
            # And parse the data.
            
            try:
                kbxMethods = SharedMethodWrapper.list_shared_methods(kbxMethodId=nonexistMethodIds, 
                                                                     kbxMethodStatus=[1, 0])
            except:
                kbxMethods = []
                
            uniqueGroupIds, methodDictionary, methodEvents = set([]), {}, {}
            for kbxMethod in kbxMethods:
                # Generate 1:object(kbxMethod) combinations.
                kbxMethodId = kbxMethod["kbxMethodId"]
                methodDictionary[kbxMethodId] = kbxMethod
                # Generate unique group IDs from methods.
                groupId = kbxMethod["kbxGroupId"]
                if not Util.is_empty(groupId):
                    uniqueGroupIds.add(groupId)
                # Generate 1:tuple(str(methodEvent), str(kbxMethodIdentifier)) combinations
                kbxMethodTag = kbxMethod.get("kbxMethodEvent")
                kbxMethodIdentifier = kbxMethod.get("kbxMethodIdentifier")
                if not Util.is_empty(kbxMethodTag) and not Util.is_empty(kbxMethodIdentifier):
                    methodEvents[kbxMethodId] = (str(kbxMethodTag), str(kbxMethodIdentifier))
                    
            # Add groups which not exists
            self.__groupController.add(uniqueGroupIds)

            # Sekali gus insert into database. Check here for multiple inserts in one statement: http://stackoverflow.com/a/5009740/1640033
            def build_parameter(methodId):
                defaultMethod = {"kbxMethodId":methodId,
                                 "kbxMethodName":None,
                                 "kbxModuleName":None,
                                 "kbxGroupId":None,
                                 "kbxMethodLabel":None,
                                 "kbxMethodStatus":-1,
                                 "kbxMethodAppId":None}
            
                kbxMethod = methodDictionary.get(methodId, defaultMethod)
                return [kbxMethod["kbxMethodId"], kbxMethod["kbxMethodName"], \
                        kbxMethod["kbxGroupId"], kbxMethod.get("kbxMethodLabel"), \
                        kbxMethod["kbxMethodStatus"], kbxMethod["kbxMethodAppId"], \
                        kbxMethod["kbxModuleName"]]
            
            bulkInsertSQLs = ['INSERT INTO "kbx_method" ("kbxMethodId", "kbxMethodName", "kbxGroupId", "kbxMethodLabel", "kbxMethodStatus", "kbxMethodAppId", "kbxModuleName")'] + \
                             ['SELECT ? AS "kbxMethodId", ? AS "kbxMethodName", ? AS "kbxGroupId", ? AS "kbxMethodLabel", ? AS "kbxMethodStatus", ? AS "kbxMethodAppId", ? AS "kbxModuleName"'] + \
                             ['UNION SELECT ?, ?, ?, ?, ?, ?, ?'] * (expectedNumbersOfMethods - 1)
            
            parameters = deque()
            for methodId in nonexistMethodIds:
                parameters.extend(build_parameter(methodId))
            
            self.__db.execute(" ".join(bulkInsertSQLs), tuple(parameters))
            
            # Find out methods which have events to registers.
            for kbxMethodId, (kbxMethodEvent, kbxMethodIdentifier) in methodEvents.items():
                self.__eventController.add(kbxMethodId, kbxMethodEvent, kbxMethodIdentifier)

    def update(self, kbxMethod):
        with self.__lock___add:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
                
            # Update database where applicable.
            row = self.__db.execute_and_fetch_one('SELECT * FROM "kbx_method" WHERE "kbxMethodId"=? LIMIT 1', (kbxMethodId,))
            if row is None:
                return
            
            # Variables
            kbxMethodStatus = kbxMethod["kbxMethodStatus"]
            kbxMethodName = kbxMethod["kbxMethodName"]
            kbxMethodAppId = kbxMethod["kbxMethodAppId"]
            kbxGroupId = kbxMethod["kbxGroupId"]
            kbxModuleName = kbxMethod["kbxModuleName"]
            kbxMethodLabel = kbxMethod.get("kbxMethodLabel", None)
            
            updateSQLs = deque()
            updateSQLValues = deque()
            
            
            if row["kbxMethodName"] != kbxMethodName and not Util.is_empty(kbxMethodName):
                updateSQLs.append('"kbxMethodName"=?')
                updateSQLValues.append(str(kbxMethodName))
                
            if row["kbxModuleName"] != kbxModuleName:
                if Util.is_empty(kbxModuleName):
                    kbxModuleName = None
                else:
                    kbxModuleName = str(kbxModuleName)
                updateSQLs.append('"kbxModuleName"=?')
                updateSQLValues.append(str(kbxModuleName))
                
            if row["kbxMethodAppId"] != kbxMethodAppId and not Util.is_empty(kbxMethodAppId):
                updateSQLs.append('"kbxMethodAppId"=?')
                updateSQLValues.append(int(kbxMethodAppId))
                
            if row["kbxMethodLabel"] != kbxMethodLabel and not Util.is_empty(kbxMethodLabel):
                updateSQLs.append('"kbxMethodLabel"=?')
                updateSQLValues.append(str(kbxMethodLabel))
                
            if row["kbxMethodStatus"] != kbxMethodStatus:
                updateSQLs.append('"kbxMethodStatus"=?')
                updateSQLValues.append(kbxMethodStatus)
                
            if row["kbxGroupId"] != kbxGroupId and not Util.is_empty(kbxGroupId):
                self.__groupController.add(set([kbxGroupId]))
                updateSQLs.append('"kbxGroupId"=?')
                updateSQLValues.append(kbxGroupId)
            
            if len(updateSQLs) > 0:
                updateSQLValues.append(kbxMethodId)
                updateSQL = 'UPDATE "kbx_method" SET ' + ", ".join(updateSQLs) + ' WHERE "kbxMethodId"=?'
                self.__db.execute(updateSQL, tuple(updateSQLValues))
                self.__db.commit()
                
        # Register events again if necessary.
        self.__eventController.delete(kbxMethodId)
        if kbxMethodStatus in (SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE):
            # Variables
            kbxMethodEvent = kbxMethod.get("kbxMethodEvent")
            kbxMethodIdentifier = kbxMethod.get("kbxMethodIdentifier")
            
            if not Util.is_empty(kbxMethodEvent) and not Util.is_empty(kbxMethodIdentifier):
                self.__eventController.add(kbxMethodId, str(kbxMethodEvent), str(kbxMethodIdentifier))
                
    def delete(self, kbxMethodId):
        with self.__lock___add:
            result = self.__db.execute_and_fetch_all('SELECT "kbxMethodStatus" FROM "kbx_method" WHERE "kbxMethodId"=? LIMIT 1', (kbxMethodId,))
            if len(result) == 1:
                row = result[0]
                if row["kbxMethodStatus"] != -1:
                    self.__db.execute('UPDATE "kbx_method" SET "kbxMethodStatus"=? WHERE "kbxMethodId"=?', (-1, kbxMethodId))
                    self.__db.commit()
                    self.__eventController.delete(kbxMethodId)
                    
    def list(self, offset, limit):
        result = self.__db.execute_and_fetch_all('SELECT * FROM "kbx_method" LIMIT ?, ?', (offset, limit))
        return result
                
    def __on_shared_method_updated(self, eventObject):
        '''
        Triggered based on event broadcasted by system app.
        '''
        try:
            kbxMethod = json.loads(eventObject["eventData"]) # eventData = kbxMethod
            self.update(kbxMethod)
        except Exception as e:
            Logger.log_error("MethodController.__on_shared_method_updated ex:", e)
            traceback.print_exc()
                    
    def __on_shared_method_deleted(self, eventObject):
        '''
        Triggered based on event broadcasted by system app.
        '''
        try:
            eventData = json.loads(eventObject["eventData"])
            kbxMethodId = eventData["kbxMethodId"]
            self.delete(kbxMethodId)
        except Exception as e:
            Logger.log_error("MethodController.__on_shared_method_deleted ex:", e)
            traceback.print_exc()
                    
    def __on_kbx_method_deleted(self, kbxMethodId):
        '''
        Triggered by database (when a method has no more references).
        '''
        self.__eventController.delete(kbxMethodId)
            
            