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
import threading
import time

from automationApp.appConstants import AppConstants
from automationApp.core.database import Database


class SceneController:


    __INSTANCE = None
    __LOCK = threading.Lock()
    

    @staticmethod
    def instance():
        with SceneController.__LOCK:
            SceneController.__INSTANCE or SceneController()
            return SceneController.__INSTANCE

    def __init__(self):
        self.__db = Database.instance()
        SceneController.__INSTANCE = self
        
    def update(self, scene):
        ''' UPDATE INTO DATABASE '''
        sceneId = scene["sceneId"]
        sceneName = scene["sceneName"]
        sceneProtected = scene["sceneProtected"]
        sceneIcon = scene["sceneIcon"]
        execution = scene["execution"]
        
        createdTime = updatedTime = int(time.time())
        
        def build_parameters(kbxMethod):
            return [sceneId, kbxMethod["kbxMethodId"], kbxMethod["kbxMethodParams"], createdTime]
        
        # Update executions
        expectedNumbersOfExecs = len(execution)
        if expectedNumbersOfExecs > 0:
            bulkInsertSQLs = ['INSERT INTO "scene_execution" ("seSceneId", "kbxMethodId", "kbxMethodParams", "createdTime", "sort")'] + \
                             ['SELECT ? AS "seSceneId", ? AS "kbxMethodId", ? AS "kbxMethodParams", ? AS "createdTime", ? AS "sort"'] + \
                             ['UNION SELECT ?, ?, ?, ?, ?'] * (expectedNumbersOfExecs - 1)
            parameters = deque()
            for sort, kbxMethod in enumerate(execution, 1):
                parameters.extend(build_parameters(kbxMethod))
                parameters.append(sort)
            self.__db.execute(" ".join(bulkInsertSQLs), tuple(parameters))
        
        self.__db.execute('DELETE FROM "scene_execution" WHERE "seSceneId"=? AND "createdTime"<>?', (sceneId, createdTime))
        
        # Update scene info.
        # Follows the sequence of RuleController.
        self.__db.execute('UPDATE "scene" ' + \
                          'SET "sceneProtected"=?, "sceneName"=?, "sceneIcon"=?, "statusProcessed"=?, "updatedTime"=? ' + \
                          'WHERE "sceneId"=?', \
                          (sceneProtected, sceneName, sceneIcon, AppConstants.SCENE_STATUS_UPDATED, updatedTime, sceneId))
    
    def delete(self, sceneId):
        self.__db.execute('DELETE FROM "scene" WHERE "sceneId"=?', (sceneId,))
        
    def change_to_updating(self, sceneId, sceneName):
        '''
        Change an existing scene status to "updating".
        '''
        self.__db.execute('UPDATE "scene" SET "statusProcessed"=?, "sceneName"=? WHERE "sceneId"=?', \
                          (AppConstants.SCENE_STATUS_UPDATING, sceneName, sceneId))
        
    def generate_id(self, sceneName):
        '''
        Generate a new entry for a scene, set the status to "updating" and return the newly generated row ID.
        '''
        sort = updatedTime = createdTime = int(time.time()) # Temporary use timestamp as sorting mechanism
        sceneId = self.__db.insert('INSERT INTO "scene"("statusProcessed", "sceneName", "createdTime", "updatedTime", "sort") ' + \
                                   'VALUES (?, ?, ?, ?, ?)', \
                                   (AppConstants.SCENE_STATUS_UPDATING, sceneName, createdTime, updatedTime, sort))
        return sceneId
        
    def has(self, sceneId):
        '''
        Check if a given sceneId exists.
        '''
        result = self.__db.execute_and_fetch_one('SELECT "sceneId" FROM "scene" WHERE "sceneId"=? LIMIT 1', (sceneId,))
        return result is not None
    
    def get_status_processed(self, sceneId):
        result = self.__db.execute_and_fetch_one('SELECT "statusProcessed" FROM "scene" WHERE "sceneId"=? LIMIT 1', (sceneId,))
        return result["statusProcessed"]
    
    def get(self, sceneId):
        '''
        Get scene without aggregating any execution and condition.
        '''
        result = self.__db.execute_and_fetch_all('SELECT * FROM "scene" WHERE "sceneId"=?', (sceneId,))
        return result[0] # Do not use fetch_one so that it will raise error.

    def get_detail(self, sceneId):
        '''
        Get scene's full details based on a given sceneId.
        '''
        result = self.__db.execute_and_fetch_all('SELECT "sceneId", "sceneName", "sceneProtected", "sceneIcon", "statusProcessed", "sort", "favSort" ' + \
                                                 'FROM "scene" ' + \
                                                 'WHERE "sceneId"=? ' + \
                                                 'LIMIT 1', \
                                                 (sceneId,))
        scene = dict(result[0])
        
        # Constants
        statusCodes = {-1:AppConstants.METHOD_ERROR_METHOD_REMOVED, 0:AppConstants.METHOD_ERROR_METHOD_OFF, 1:AppConstants.METHOD_ERROR_OK}
        
        sceneId = scene["sceneId"]
        sceneExecs = scene["execution"] = deque()
        sceneStatusCode = AppConstants.METHOD_ERROR_OK
        if scene["statusProcessed"] == AppConstants.SCENE_STATUS_UPDATED:
            # Aggregate scene executions
            result1 = self.__db.execute_and_fetch_all('SELECT "m"."kbxGroupId", "kbxGroupLabel", "kbxGroupName", "kbxGroupIcon", "m"."kbxMethodId", ' + \
                                                      '"kbxMethodLabel", "kbxMethodName", "kbxMethodStatus", "kbxGroupStatus", "kbxMethodAppId", "kbxMethodParams" ' + \
                                                      'FROM "scene_execution" AS "c", "kbx_method" AS "m", "kbx_group" AS "g" ' + \
                                                      'WHERE "seSceneId"=? AND "c"."kbxMethodId"="m"."kbxMethodId" AND "m"."kbxGroupId"="g"."kbxGroupId" ' + \
                                                      'ORDER BY "sort"', (sceneId,))
                  
            for row1 in result1:
                item = dict(row1)
                if item["kbxGroupStatus"] == -1:
                    statusCode = AppConstants.METHOD_ERROR_GROUP_REMOVED
                    item["statusCode"] = statusCode
                    sceneStatusCode |= statusCode
                else:
                    statusCode = statusCodes[item["kbxMethodStatus"]]
                    item["statusCode"] = statusCode
                    sceneStatusCode |= statusCode
                
                sceneExecs.append(item)
            
            scene["statusCode"] = sceneStatusCode
        
        return scene
    
    def get_summary(self, sceneId):
        '''
        Get scene's summary based on scene ID.
        '''
        result = self.__db.execute_and_fetch_all('SELECT "sceneId", "sceneName", "sceneIcon", "statusProcessed", "sort", "favSort" ' + \
                                                 'FROM "scene" ' + \
                                                 'WHERE "sceneId"=? ' + \
                                                 'LIMIT 1', (sceneId,))
        scene = dict(result[0])
        self.__aggregate_execution(scene) # Modified by reference.
        return scene
        
    def list(self, offset=0, limit=20):
        '''
        List scenes' summaries based on offset and limit.
        '''
        # Variables
        scenes = deque()
        
        # List scenes from offset to limit
        result = self.__db.execute_and_fetch_all('SELECT "sceneId", "sceneName", "sceneIcon", "statusProcessed", "sort", "favSort" ' + \
                                                 'FROM "scene" ' + \
                                                 'ORDER BY "sort" ' + \
                                                 'LIMIT ?, ?', (offset, limit))
        for row in result:
            scene = dict(row)
            self.__aggregate_execution(scene) # Modified by reference.
            scenes.append(scene)
            
        return scenes
    
    def count(self):
        '''
        Count total existing scenes.
        '''
        result = self.__db.execute_and_fetch_one('SELECT count("sceneId") AS "total" FROM "scene"')
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
    
    def list_executions(self, sceneId):
        '''
        List executions by scene ID.
        '''
        return self.__db.execute_and_fetch_all('SELECT * FROM "scene_execution", "kbx_method" ' + \
                                               'WHERE "seSceneId"=? AND "kbx_method"."kbxMethodId"="scene_execution"."kbxMethodId" ' + \
                                               'ORDER BY "sort"', (sceneId,))
    
    def list_scene_ids_which_has_kbx_method_id_as_execution(self, kbxMethodId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "seSceneId" FROM "scene_execution" WHERE "kbxMethodId"=?', (kbxMethodId,))
        return (row["seSceneId"] for row in result)
    
    def list_scene_ids_which_has_kbx_group_id_as_execution(self, kbxGroupId):
        result = self.__db.execute_and_fetch_all('SELECT DISTINCT "se"."seSceneId" ' + \
                                                 'FROM "scene_execution" AS "se", "kbx_method" AS "km" ' + \
                                                 'WHERE "se"."kbxMethodId"="km"."kbxMethodId" AND "km"."kbxGroupId"=?',
                                                 (kbxGroupId,))
        return (row["seSceneId"] for row in result)

    #===========================================================================
    # For favorited scenes
    #===========================================================================
    def get_largest_favsort_num(self):
        '''
        Returns largest favSort number.
        0 means no favorited scene.
        '''
        result = self.__db.execute_and_fetch_one('SELECT MAX("favSort") AS "maxFavSort" FROM "scene"')
        return result["maxFavSort"] or 0 # Returns 0 if largest favSort is None or 0
    
    def get_favsort_of(self, sceneId):
        '''
        Returns favSort of a sceneId. 
        It can be a number or None (if it's not a favorite item)
        '''
        result = self.__db.execute_and_fetch_one('SELECT "favSort" FROM "scene" ' + \
                                                 'WHERE "sceneId"=?', (sceneId,))
        return result["favSort"] # Raise error for invalid sceneId

    def update_favorited_scene(self, sceneId, favSort):
        '''
        nextSceneId, provide this and we will prepend sceneId to it; 
        else we always append sceneId to the end of the list. 
        '''
            
        # 1, 2, 3, >>favSort, 4 -> 5, 5 -> 6 ...
        self.__db.execute('UPDATE "scene" SET "favSort"="favSort" + 1 WHERE "favSort" >= ?', (favSort,)) # 4 -> 5, 5 -> 6 ...
        self.__db.execute('UPDATE "scene" SET "favSort"=? WHERE "sceneId"=?', (favSort, sceneId)) # >>favSort
    
    def delete_favorited_scene(self, sceneId):
        '''
        If sceneId does not favorited before, Exception will be raised.
        '''
        self.__db.execute('UPDATE "scene" SET "favSort"=? WHERE "sceneId"=?', (None, sceneId))
    
    def list_favorited_scenes_reversed(self, offset=0, limit=200):
        '''
        For optimized performance, item is always append to end of the list, 
        but we have to create visual effect where favorited scene 
        is added to the first item of the list. 
        '''
        # Variables
        scenes = deque()
        
        # List scenes from offset to limit
        result = self.__db.execute_and_fetch_all('SELECT "sceneId", "sceneName", "sceneIcon", "statusProcessed", "sort", "favSort"' + \
                                                 'FROM "scene" ' + \
                                                 'WHERE "favSort" IS NOT NULL ' + \
                                                 'ORDER BY "favSort" DESC ' + \
                                                 'LIMIT ?, ?', (offset, limit))
        for row in result:
            scene = dict(row)
            self.__aggregate_execution(scene) # Modified by reference.
            scenes.append(scene)
            
        return scenes
    
    def count_favorited_scenes(self):
        '''
        Count total favorited scenes.
        '''
        result = self.__db.execute_and_fetch_one('SELECT count("sceneId") AS "total" ' + \
                                                 'FROM "scene" ' + \
                                                 'WHERE "favSort" IS NOT NULL')
        return result["total"]
    
    def __aggregate_execution(self, scene):
        # Constants
        statusCodes = {-1:AppConstants.METHOD_ERROR_METHOD_REMOVED, 0:AppConstants.METHOD_ERROR_METHOD_OFF, 1:AppConstants.METHOD_ERROR_OK}
        
        sceneId = scene["sceneId"]
        sceneExecs = scene["execution"] = deque()
        sceneStatusCode = AppConstants.METHOD_ERROR_OK
        if scene["statusProcessed"] == AppConstants.SCENE_STATUS_UPDATED:
            # Aggregate scene conditions and executions
            result1 = self.__db.execute_and_fetch_all('SELECT "m"."kbxGroupId", "kbxGroupIcon", "kbxMethodStatus", "kbxGroupStatus" ' + \
                                                      'FROM "scene_execution" AS "c", "kbx_method" AS "m", "kbx_group" AS "g" ' + \
                                                      'WHERE "seSceneId"=? AND "c"."kbxMethodId"="m"."kbxMethodId" AND "m"."kbxGroupId"="g"."kbxGroupId" ' + \
                                                      'ORDER BY "sort"', (sceneId,))
            for row1 in result1:
                item = dict(row1)
                if item["kbxGroupStatus"] == -1:
                    statusCode = AppConstants.METHOD_ERROR_GROUP_REMOVED
                    item["statusCode"] = statusCode
                    sceneStatusCode |= statusCode
                else:
                    statusCode = statusCodes[item["kbxMethodStatus"]]
                    item["statusCode"] = statusCode
                    sceneStatusCode |= statusCode
                
                sceneExecs.append(item)
            
            scene["statusCode"] = sceneStatusCode


    