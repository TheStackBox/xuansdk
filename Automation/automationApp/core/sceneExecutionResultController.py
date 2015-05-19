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

import sqlite3
import threading


class SceneExecutionResultDataHandler:
    '''
    Keep track of retry states and scene executions histories.
    '''
    
    
    AFTER_RECORD_DELETE = lambda serId: True
    
    
    def __init__(self):
        self.__lock = threading.Lock()

        self.__db = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.__db.row_factory = sqlite3.Row
        
        def after_ser_added():
            result = self.__db.execute('SELECT "serCreatedTime" ' +
                                       'FROM "scene_execution_result" ' +
                                       'ORDER BY "serCreatedTime" DESC LIMIT 10, 1') # Remove since the 11th record
            row = result.fetchone()
            if row is not None: # If 11th exists
                serCreatedTimeToStartRemove = row["serCreatedTime"]
                self.__db.execute('DELETE FROM "scene_execution_result" WHERE "serCreatedTime" <= ?', 
                                  (serCreatedTimeToStartRemove,))

        def before_ser_delete(serId):
            self.__db.execute('DELETE FROM "scene_execution_result_item" WHERE "serId"=?', (serId,))
                                           
        def after_ser_deleted(serId):
            SceneExecutionResultDataHandler.AFTER_RECORD_DELETE(serId)
            
        self.__db.create_function("after_ser_added", 0, after_ser_added)
        self.__db.create_function("before_ser_delete", 1, before_ser_delete)
        self.__db.create_function("after_ser_deleted", 1, after_ser_deleted)
        
        self.__db.execute('CREATE TABLE "scene_execution_result" (' +
                            '"serId" TEXT UNIQUE PRIMARY KEY, ' +
                            '"serStartTime" REAL NOT NULL,' +
                            '"serEndTime" REAL NOT NULL,' +
                            '"serCreatedTime" REAL NOT NULL,'
                            '"sceneId" INTEGER NOT NULL,' +
                            '"sceneName" TEXT,' +
                            '"sceneProtected" BOOLVAL NOT NULL' +
                          ')')
        self.__db.execute('CREATE TABLE "scene_execution_result_item" (' +
                            '"serId" TEXT NOT NULL,' +
                            '"kbxMethodId" INTEGER NOT NULL,' +
                            '"kbxMethodName" TEXT,' +
                            '"kbxMethodParams" LIST NOT NULL,' +
                            '"kbxGroupLabel" TEXT,' +
                            '"seriStatus" TEXT NOT NULL,' +
                            '"seriError" TEXT,' +
                            '"seriIndex" INTEGER NOT NULL,' +
                            'CONSTRAINT "fkey0" FOREIGN KEY ("serId") REFERENCES "scene_execution_result" ("serId")'
                          ')')
        self.__db.execute('CREATE TRIGGER "before_ser_delete" BEFORE DELETE ON "scene_execution_result" BEGIN ' +
                            'SELECT before_ser_delete(OLD."serId"); ' +
                          'END')
        self.__db.execute('CREATE TRIGGER "after_ser_deleted" AFTER DELETE ON "scene_execution_result" BEGIN ' +
                            'SELECT after_ser_deleted(OLD."serId"); ' +
                          'END')
        self.__db.execute('CREATE TRIGGER "after_ser_added" AFTER INSERT ON "scene_execution_result" BEGIN ' +
                            'SELECT after_ser_added(); ' +
                          'END')
        
        self.__db.commit()
        
    def add(self, serId, serCreatedTime, serStartTime, serEndTime, sceneId, sceneName, sceneProtected, execution):
        '''
        serId:String, 
        serStartTime:Integer, 
        serEndTime:Integer, 
        sceneId:Integer, 
        sceneName:String, 
        sceneProtected:Boolean, 
        execution:List -
        [{     
            kbxMethodId:Integer, 
            kbxMethodName:String, 
            kbxGroupLabel:String, 
            seriStatus:Enum("ok", "error", "busy"), 
            seriError:String, 
            seriIIndex:Integer
            kbxMethodParams:List, -
            [{
                kbxParamName:String,
                kbxParamCurrentValue:Anything.
            }]
        }]
        '''
        with self.__lock:
            try:
                self.__db.execute('INSERT INTO "scene_execution_result" ' +
                                  'VALUES (?, ?, ?, ?, ?, ?, ?)', 
                                  (serId, serStartTime, serEndTime, serCreatedTime, sceneId, sceneName, sceneProtected))
                
                def seri_generator():
                    for seriIndex, seriItem in enumerate(execution):
                        yield (serId, seriItem["kbxMethodId"], seriItem["kbxMethodName"], seriItem["kbxMethodParams"], 
                               seriItem["kbxGroupLabel"], seriItem["seriStatus"], 
                               seriItem["seriError"], seriIndex)
                        
                self.__db.executemany('INSERT INTO "scene_execution_result_item" ' +
                                      'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                      seri_generator())
                
            except Exception as e:
                self.__db.rollback()
                raise e
            else:
                self.__db.commit()
                
    def update_seri_status(self, serId, seriIndexes, seriStatus, seriError):
        with self.__lock:
            try:
                if len(seriIndexes) == 1:
                    whereClause = 'WHERE "serId"=? AND "seriIndex"=' + str(seriIndexes[0])
                else:
                    whereClause = 'WHERE "serId"=? AND "seriIndex" IN (%s)' % (",".join((str(seriIndex) for seriIndex in seriIndexes)),)
                
                self.__db.execute('UPDATE "scene_execution_result_item" ' +
                                  'SET "seriStatus"=?, "seriError"=? ' +
                                  whereClause, (seriStatus, seriError, serId))
            except Exception as e:
                self.__db.rollback()
                raise e
            else:
                self.__db.commit()
                
    def list_seris_with_error(self, serId):
        with self.__lock:
            result = self.__db.execute('SELECT * ' +
                                       'FROM "scene_execution_result_item" ' +
                                       'WHERE "serId"=? AND "seriStatus"=? ' +
                                       'ORDER BY "seriIndex"', (serId, "error"))
            return result.fetchall()
    
    def get_seri_by_index(self, serId, seriIndex):
        with self.__lock:
            result = self.__db.execute('SELECT * ' +
                                       'FROM "scene_execution_result_item" ' +
                                       'WHERE "serId"=? AND "seriIndex"=?', (serId, seriIndex))
            row = result.fetchone()
            return row
    
    def get_ser_and_seris(self, serId):
        '''
        Aggregates ser and seri into ser.execution.
        '''
        with self.__lock:
            serObject = self.__db.execute('SELECT * FROM "scene_execution_result" WHERE "serId"=? LIMIT 1', (serId,)).fetchone()
            if serObject is None:
                raise Exception("serId not found")
            else:
                serObject = dict(serObject)
            
            seris = self.__db.execute('SELECT * FROM "scene_execution_result_item" WHERE "serId"=?', (serId,)).fetchall()
            serObject["execution"] = [dict(seri) for seri in seris]
            return serObject
        
    def list(self, offset, limit):
        '''
        List all ser items. (For debugging only)
        '''
        with self.__lock:
            result = self.__db.execute('SELECT * FROM "scene_execution_result" LIMIT ?, ?', (offset, limit)).fetchall()
            return [dict(row) for row in result]
        
    def delete(self, serId):
        '''
        Delete ser.
        '''
        with self.__lock:
            self.__db.execute('DELETE FROM "scene_execution_result" WHERE "serId"=?', (serId,))

            
class SceneExecutionResultController(SceneExecutionResultDataHandler):
    '''
    Keep tracks of scene executions status.
    '''
    
    
    def __init__(self):
        super().__init__()
        
