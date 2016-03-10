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

import json
import sqlite3
import threading

from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class EventDataHandler:
    '''
    Keep track of event tags to be registered and unregistered.
    '''
    
    def __init__(self):
        self.__db = sqlite3.connect(":memory:", check_same_thread=False)
        self.__db.row_factory = sqlite3.Row
        self.__db.execute('CREATE TABLE "event" (' +
                            '"kbxMethodId" INTEGER UNIQUE PRIMARY KEY, ' +
                            '"kbxMethodEvent" TEXT,' +
                            '"kbxMethodIdentifier" TEXT' +
                          ')')
        self.__db.execute('CREATE TRIGGER "on_record_added" AFTER INSERT ON "event" ' +
                          'BEGIN SELECT on_record_added(NEW.kbxMethodId, NEW.kbxMethodEvent, NEW.kbxMethodIdentifier); END')
        self.__db.execute('CREATE TRIGGER "on_record_updated" AFTER UPDATE ON "event" ' +
                          'BEGIN SELECT on_record_updated(NEW.kbxMethodId, OLD.kbxMethodEvent, OLD.kbxMethodIdentifier, NEW.kbxMethodEvent, NEW.kbxMethodIdentifier); END')
        self.__db.execute('CREATE TRIGGER "on_record_deleted" AFTER DELETE ON "event" ' +
                          'BEGIN SELECT on_record_deleted(OLD.kbxMethodId, OLD.kbxMethodEvent, OLD.kbxMethodIdentifier); END')
        
        self.__db.execute('CREATE INDEX "index0" ON "event" ("kbxMethodEvent")')
        
        self.__db.create_function("on_record_added", 3, self.__on_record_added)
        self.__db.create_function("on_record_deleted", 3, self.__on_record_deleted)
        self.__db.create_function("on_record_updated", 5, self.__on_record_updated)
        
        self.__db.commit()
    
    def add(self, kbxMethodId, kbxMethodEvent, kbxMethodIdentifier):
        result = self.__db.execute('SELECT * FROM "event" WHERE "kbxMethodId"=?', (kbxMethodId,)).fetchall()
        if len(result) == 1:
            record = result[0]
            if kbxMethodEvent == record["kbxMethodId"] and kbxMethodIdentifier == record["kbxMethodIdentifier"]:
                return
            else:
                self.__db.execute('UPDATE "event" SET "kbxMethodEvent"=?, "kbxMethodIdentifier"=? WHERE "kbxMethodId"=?', (kbxMethodEvent, kbxMethodIdentifier, kbxMethodId))
        else:
            self.__db.execute('INSERT INTO "event" ("kbxMethodId", "kbxMethodEvent", "kbxMethodIdentifier") VALUES (?, ?, ?)', (kbxMethodId, kbxMethodEvent, kbxMethodIdentifier))
    
        self.__db.commit()
    
    def delete(self, kbxMethodId):
        self.__db.execute('DELETE FROM "event" WHERE "kbxMethodId"=?', (kbxMethodId,))
        
        self.__db.commit()
        
    def reset(self):
        result = self.__db.execute('SELECT DISTINCT "kbxMethodEvent" FROM "event"').fetchall()
        for row in result:
            kbxMethodEvent = row["kbxMethodEvent"]
            try:
                self.on_event_deleted(kbxMethodEvent)
            except Exception as e:
                Logger.log_warning("EventController.reset on_event_removed ex:", e, "- tag:", kbxMethodEvent)
        
        self.__db.close()
        
        self.__init__()
        
    def list_method_ids(self, kbxMethodEvent, kbxMethodIdentifier):
        result = self.__db.execute('SELECT "kbxMethodId" FROM "event" WHERE "kbxMethodEvent"=? AND "kbxMethodIdentifier"=?', (kbxMethodEvent, kbxMethodIdentifier))
        return result.fetchall()
        
    def __on_record_added(self, kbxMethodId, kbxMethodEvent, kbxMethodIdentifier):
        result = self.__db.execute('SELECT COUNT(kbxMethodId) AS "total" FROM "event" WHERE "kbxMethodEvent"=?', (kbxMethodEvent,)).fetchall()
        if result[0]["total"] == 1:
            try:
                self.on_event_added(kbxMethodEvent)
            except Exception as e:
                Logger.log_warning("EventController.__on_record_added ex:", e, "- tag:", kbxMethodEvent)
    
    def __on_record_deleted(self, kbxMethodId, kbxMethodEvent, kbxMethodIdentifier):
        result = self.__db.execute('SELECT COUNT(kbxMethodId) AS "total" FROM "event" WHERE "kbxMethodEvent"=?', (kbxMethodEvent,)).fetchall()
        if result[0]["total"] == 0:
            try:
                self.on_event_deleted(kbxMethodEvent)
            except Exception as e:
                Logger.log_warning("EventController.__on_record_added ex:", e, "- tag:", kbxMethodEvent)
    
    def __on_record_updated(self, kbxMethodId, oldKBXMethodEvent, oldKBXMethodIdentifier, newKBXMethodEvent, newKBXMethodIdentifier):
        self.__on_record_deleted(kbxMethodId, oldKBXMethodEvent, oldKBXMethodIdentifier)
        self.__on_record_added(kbxMethodId, newKBXMethodEvent, newKBXMethodIdentifier)
        
    def on_event_added(self, kbxMethodEvent):
        '''
        Override: Called when a new event is added.
        '''
    
    def on_event_deleted(self, kbxMethodEvent):
        '''
        Override: Called when an event is removed.
        '''
        
        
class EventController(EventDataHandler):
    '''
    Keep tracks of events.
    '''
    
    
    __INSTANCE = None
    __LOCK = threading.Lock()
    
    
    @staticmethod
    def instance():
        with EventController.__LOCK:
            EventController.__INSTANCE or EventController()
            return EventController.__INSTANCE
        
    def __init__(self):
        super().__init__()
        
        EventController.__INSTANCE = self
        
        self.__lock = threading.Lock()
        self.__aFunc = lambda kbxMethodId, kbxMethodEvent, kbxMethodIdentifier: True
        
    def listen_to_event_callback(self, aFunc):
        '''
        Method event callback.
        
        aFunc:Function - Parameters (kbxMethodId:Integer, eventTag:String, eventData:String)
        '''
        self.__aFunc = aFunc
        
    def add(self, kbxMethodId, kbxMethodEvent, kbxMethodIdentifier):
        with self.__lock:
            super().add(kbxMethodId, kbxMethodEvent, kbxMethodIdentifier)
        
    def delete(self, kbxMethodId):
        with self.__lock:
            super().delete(kbxMethodId)
            
    def on_event_added(self, kbxMethodEvent):
        Application.register_event_listener(kbxMethodEvent, self.__on_event_callback)
    
    def on_event_deleted(self, kbxMethodEvent):
        Application.unregister_event_listener(kbxMethodEvent, self.__on_event_callback)
        
    def __on_event_callback(self, eventObject):
        eventTag = eventObject["eventTag"]
        eventData = eventObject["eventData"]
        eventDataParsed = json.loads(eventData)
        
        kbxMethodIdentifier = eventDataParsed.get("kbxMethodIdentifier")
        
        if not Util.is_empty(kbxMethodIdentifier):
            kbxMethodEvent = str(eventTag)
            kbxMethodIdentifier = str(kbxMethodIdentifier)
            with self.__lock:
                result = self.list_method_ids(kbxMethodEvent, kbxMethodIdentifier)
            for row in result:
                kbxMethodId = row["kbxMethodId"]
                self.__aFunc(kbxMethodId, kbxMethodEvent, eventData)

