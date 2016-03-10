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
from concurrent.futures.thread import ThreadPoolExecutor
import copy
import json
import threading
import time
import traceback

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.groupController import GroupController
from automationApp.core.methodController import MethodController
from automationApp.core.sceneController import SceneController
from automationApp.service.sceneExecutionResultService import SceneExecutionResultService
from automationApp.utils.automationJSONEncoder import AutomationJSONEncoder
from automationApp.utils.sharedMethodWrapper import SharedMethodWrapper
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator


class SceneExecLock:
    '''
    Locks down a scene execution and raise error.
    '''


    def __init__(self):
        self.__isStop = False
        self.__threadEvent = threading.Event()
        self.__lock = threading.Lock()

    def get_thread_event(self):
        return self.__threadEvent
    
    def set_stop(self):
        self.__isStop = True
        self.__threadEvent.set()
        
    def is_stop(self):
        return self.__isStop
    
    def acquire(self, *args, **kwargs):
        return self.__lock.acquire(*args, **kwargs)
        
    def release(self, *args, **kwargs):
        return self.__lock.release(*args, **kwargs)
    
    
def SCENE_PROCESS_SYNC(fn):
    def locker(*args, **kwargs):
        with SceneService.SCENE_PROCESS_LOCK:
            return fn(*args, **kwargs)
    return locker

class SceneService:

    
    # Locks down edit/delete/execute    
    SCENE_PROCESS_LOCK = threading.Lock()

    
    def __init__(self):
        # Scene processors.
        self.__sceneController = SceneController.instance()
        self.__methodController = MethodController.instance()

        self.__sceneUpdateThreadPool = ThreadPoolExecutor(max_workers=1)
        self.__sceneExecThreadPool = ThreadPoolExecutor(max_workers=AppConstants.MAX_SCENE_EXEC_THREAD_SIZE)
        self.__sceneExecutionResultThreadPool = ThreadPoolExecutor(max_workers=5)

        # Scene run workers.
        self.__sceneExecLocks = {}
        
        # Favorite edit lock
        self.__fav_lock = threading.Lock()

        # Listeners.
        GroupController.instance().listen_to_group_icon_change(self.__on_group_icon_changed)
        self.__methodController.listen_to_method_status_change(self.__on_method_status_changed)
        
    def __on_group_icon_changed(self, kbxGroupId):
        '''
        Trigger Source: GroupController --> This
        Callback when kbxGroupIcon changed.
        '''
        sceneIds = self.__sceneController.list_scene_ids_which_has_kbx_group_id_as_execution(kbxGroupId)
        # Broadcast scenes updated messages.
        for sceneId in sceneIds:
            self.__broadcast_message__scene_updated(sceneId)

    def __on_method_status_changed(self, kbxMethodId, oldKBXMethodStatus, newKBXMethodStatus):
        '''
        Trigger Source: MethodController --> This
        Callback when kbxMethodStatus changed.
        '''
        if oldKBXMethodStatus != newKBXMethodStatus:
            sceneIds = self.__sceneController.list_scene_ids_which_has_kbx_method_id_as_execution(kbxMethodId)

            # Broadcast scenes updated messages.
            for sceneId in sceneIds:
                self.__broadcast_message__scene_updated(sceneId)

    @SCENE_PROCESS_SYNC
    def set_scene(self, execution, sceneId=None, sceneName=None, sceneProtected=False, sceneIcon=None):
        '''
        Create/Edit(with sceneId provided) an existing scene.
        
        execution:Dictionary
        sceneId:Integer <Optional>
        sceneName:String <Optional>
        sceneProtected:Boolean <Optional>
        sceneIcon:Boolean
        
        Returns "sceneId"
        '''

        def process_method_list(methodList):
            #===================================================================
            # Basic type validation
            #===================================================================
            if not isinstance(methodList, list):
                Logger.log_error("SceneService.set_scene: 'execution' must be type of list.")
                Logger.log_debug("type:", type(methodList), "value:", methodList)
                raise AutomationException(11904, "List is required for both 'execution'")

            #===================================================================
            # Check allowed size, raise error if exceeded.
            #===================================================================
            if len(methodList) > AppConstants.MAX_METHOD_SIZE:
                Logger.log_error("SceneService.set_scene: 'execution' cannot have more than",
                                 AppConstants.MAX_METHOD_SIZE, "items.")
                raise AutomationException(11907, "Only a maximum of " + \
                            str(AppConstants.MAX_METHOD_SIZE) + " items is allowed for each 'execution'",
                            lambda text: str(AppConstants.MAX_METHOD_SIZE).join(text.split(":max_item_size:")))

            #===================================================================
            # Check if all kbxMethodIds are valid and all kbxMethodParams are list
            #===================================================================
            idValidator = NumberValidator(isRequired=True, decimalPoint=False)
            if not all([idValidator.is_valid(eachMethod["kbxMethodId"])
                        and isinstance(eachMethod["kbxMethodParams"], list)
                        for eachMethod in methodList]):
                raise AutomationException(11904, "'execution' have incorrect data structure.")

            #===================================================================
            # Check if all kbxParamName and kbxParamCurrentValue exists
            #===================================================================
            paramNameValidator = StringValidator(isRequired=True)
            for eachMethod in methodList:
                methodArgs = eachMethod["kbxMethodParams"]
                for methodArg in methodArgs:
                    if not paramNameValidator.is_valid(methodArg[AppConstants.ARG_NAME]):
                        raise AutomationException(11904, "'execution' have invalid params structure")

                    if not AppConstants.ARG_CURRENT_VALUE in methodArg:
                        methodArg[AppConstants.ARG_CURRENT_VALUE] = None

            return methodList

        #=======================================================================
        # Data structure validations
        #=======================================================================
        sceneId = NumberValidator(isRequired=False, decimalPoint=False).get_value(sceneId)
        execution = process_method_list(execution)

        #=======================================================================
        # Add to database
        #=======================================================================
        if Util.is_empty(sceneId):
            # Validate_max_scene_size
            if self.__sceneController.count() >= AppConstants.MAX_SCENE_SIZE:
                raise AutomationException(11908, 
                                          "Scene size cannot be more than " + str(AppConstants.MAX_SCENE_SIZE),
                                          lambda text: str(AppConstants.MAX_SCENE_SIZE).join(text.split(":max_scene_size:")))
            sceneId = self.__sceneController.generate_id(sceneName)
            scene = {}
        elif self.__sceneController.has(sceneId):
            self.__verify_scene_updated(sceneId)
            self.__sceneController.change_to_updating(sceneId, sceneName)
            scene = self.__sceneController.get(sceneId)
            scene = dict(scene)
        else:
            raise AutomationException(11902, "Scene not found")

        #=======================================================================
        # Broadcast message: starts to update scene.
        #=======================================================================
        self.__broadcast_message__scene_update_started(sceneId, sceneName)

        #=======================================================================
        # Set basic information of the scene
        #=======================================================================
        scene["sceneId"] = sceneId
        scene["sceneName"] = sceneName
        scene["sceneProtected"] = sceneProtected
        scene["sceneIcon"] = sceneIcon
        scene["execution"] = execution

        #=======================================================================
        # Append if its new scene
        #=======================================================================
        def __update_scene(scene):
            try:
                # Fire scene update start event
                sceneId = scene["sceneId"]
                sceneName = scene["sceneName"]
                    
                # Add methods to subscribe list
                methodIds = [kbxMethod["kbxMethodId"] for kbxMethod in scene["execution"]]
                self.__methodController.add(methodIds)
                    
                # Update "scene" base table
                self.__sceneController.update(scene)
                self.__sceneController.commit()

            except Exception as e:
                self.__sceneController.rollback()
                self.__broadcast_message__scene_update_failed(sceneId, sceneName)
                Logger.log_error("SceneService __update_scene failed:", e, "-- rolledback")
            else:
                # Broadcast message: completed updating a scene
                self.__broadcast_message__scene_updated(sceneId)

        #=======================================================================
        # Submit to a thread to process other info, and return... performance...
        #=======================================================================
        # Only 1 worker in the threadPool, it works as threading.Lock
        self.__sceneUpdateThreadPool.submit(__update_scene, scene)
        
        return sceneId

    @SCENE_PROCESS_SYNC
    def delete_scene(self, sceneId):
        self.__verify_scene_updated(sceneId)
        
        try:
            favSort = self.__sceneController.get_favsort_of(sceneId) # To determine should favorited_Scene_deleted broadcasted
            self.__sceneController.delete(sceneId)
            self.__sceneController.commit()
        except Exception as e:
            self.__sceneController.rollback()
            traceback.print_exc()
            Logger.log_error("SceneService delete_scene ex:", e, "-- rolled back")
            raise AutomationException(11906, "Unable to delete scene, problem - " + str(e))
        else:
            self.__broadcast_message__scene_deleted(sceneId)
            if favSort is not None:
                self.__broadcast_message__favorited_scene_deleted(sceneId)

    @SCENE_PROCESS_SYNC
    def execute_scene(self, sceneId, serUrl=None, language="en"):
        '''
        Execute a scene.
        Scene execution will only be recorded if serUrl is specified.
        '''
        self.__verify_scene_updated(sceneId)
        
        self.__sceneExecLocks.setdefault(sceneId, SceneExecLock())
        sceneExecLock = self.__sceneExecLocks.get(sceneId)
        isAcquired = sceneExecLock.acquire(False) # Raise error if failed to acquire.
        if isAcquired == True:
            try:
                #===================================================================
                # Should record execution? Depends on serUrl.
                #===================================================================
                if not Util.is_empty(serUrl):
                    # Get sceneName and sceneProtected
                    scene = self.__sceneController.get(sceneId)
                    sceneName, sceneProtected = scene["sceneName"], scene["sceneProtected"]
                    serObj = {"serUrl":serUrl, "sceneName":sceneName, "sceneProtected":sceneProtected}
                else:
                    serObj = None
                    
                #=======================================================================
                # List execution methods
                #=======================================================================
                execution = self.__sceneController.list_executions(sceneId)
                
                self.__sceneExecThreadPool.submit(self.__execute_scene_implementation, 
                                                  sceneId=sceneId, 
                                                  execution=execution,
                                                  serObj=serObj, 
                                                  language=language)
            except Exception as e:
                del(self.__sceneExecLocks[sceneId])
                sceneExecLock.release()
                traceback.print_exc() # This is unusual error
                raise e

        else:
            raise AutomationException(11901, "the scene is already executing. " + \
                                      "Use 'stop_scene' to cancel its execution.")

    def stop_scene(self, sceneId):
        '''
        Stop a scene execution.
        '''
        sceneExecLock = self.__sceneExecLocks.get(sceneId, None)
        if sceneExecLock is None:
            raise AutomationException(11905, "Call stop only after execute_scene is called")
        else:
            sceneExecLock.set_stop()
        
    def get_scene(self, sceneId, language=AppInfo.DEFAULT_API_LANGUAGE):
        try:
            scene = self.__sceneController.get_detail(sceneId)
        except:
            raise AutomationException(11902, "Scene ID provided: " + str(sceneId))

        kbxMethods = scene["execution"]

        # -------------- Compile lists of kbxMethod and group IDs contains in this scene.
        kbxMethodIdsToList = {}
        kbxGroupIdsToList = set([])

        for kbxMethod in kbxMethods:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
            kbxMethodAppId = kbxMethod["kbxMethodAppId"]
            kbxMethodStatus = kbxMethod["kbxMethodStatus"]
            kbxGroupId = kbxMethod["kbxGroupId"]
            kbxGroupStatus = kbxMethod["kbxGroupStatus"]

            if kbxMethodStatus is not -1 and kbxMethodAppId is not None:
                kbxMethodIdsToList.setdefault(kbxMethodAppId, set([]))
                kbxMethodIdsToList[kbxMethodAppId].add(kbxMethodId)
            if kbxGroupId is not None and kbxGroupStatus is not -1:
                kbxGroupIdsToList.add(kbxGroupId)

        # -------------- Get methods and groups based on requested language.
        kbxMethodIdsListed = {}
        kbxGroupIdsListed = {}

        for kbxMethodAppId, kbxMethodIds in kbxMethodIdsToList.items():
            kbxMethodIdsListed[kbxMethodAppId] = SharedMethodWrapper.list_shared_methods_by_app_id(kbxMethodAppId,
                                                                                                   kbxMethodIds,
                                                                                                   language=language)

        groupList = SharedMethodWrapper.list_shared_method_groups(kbxGroupId=kbxGroupIdsToList, language=language)
        for row in groupList:
            kbxGroupIdsListed[row["kbxGroupId"]] = row

        # -------------- Set method and group data into scene.
        for kbxMethod in kbxMethods:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
            kbxMethodAppId = kbxMethod["kbxMethodAppId"]
            kbxMethodStatus = kbxMethod["kbxMethodStatus"]
            kbxGroupId = kbxMethod["kbxGroupId"]
            kbxGroupStatus = kbxMethod["kbxGroupStatus"]

            if kbxMethodStatus is not -1 and kbxMethodAppId is not None:
                kbxMethodParamsWithCurrentValue = {
                    kbxMethodParam["kbxParamName"]: kbxMethodParam["kbxParamCurrentValue"] \
                    for kbxMethodParam in kbxMethod["kbxMethodParams"]
                }
                kbxMethodWithDetails = kbxMethodIdsListed[kbxMethodAppId][kbxMethodId]
                if kbxMethodWithDetails is not None:
                    kbxMethodParamsWithDetails = kbxMethodWithDetails["kbxMethodParams"]
                    kbxMethodParamsWithDetails = copy.deepcopy(kbxMethodParamsWithDetails)
                    
                    for kbxMethodParam in kbxMethodParamsWithDetails:
                        kbxMethodParam["kbxParamCurrentValue"] = kbxMethodParamsWithCurrentValue.get(
                            kbxMethodParam["kbxParamName"], None)
    
                    kbxMethod["kbxMethodParams"] = kbxMethodParamsWithDetails
                    kbxMethod["kbxMethodLabel"] = kbxMethodWithDetails.get("kbxMethodLabel")
                    kbxMethod["kbxMethodDesc"] = kbxMethodWithDetails.get("kbxMethodDesc")
                    
                else:
                    kbxMethod["atDebug"] = "Unable to get shared method, caused by a method which never register itself on this bootup."
                    
            if kbxGroupId is not None and kbxGroupStatus is not -1:
                try:
                    kbxMethod["kbxGroupLabel"] = kbxGroupIdsListed[kbxGroupId]["kbxGroupLabel"]
                    kbxMethod["kbxGroupDesc"] = kbxGroupIdsListed[kbxGroupId]["kbxGroupDesc"]
                except:
                    kbxMethod["atDebugGroup"] = "Unable to get shared method group, caused by a group which never register itself on this bootup."
                    
        return scene

    def list_scenes(self, offset=0, limit=20):
        return self.__sceneController.list(offset, limit), \
               self.__sceneController.count()
               
    def set_favorited_scene(self, sceneId, prevSceneId=None):
        '''
        sceneId - can be either favorited/non-favorited scene, but must be a valid scene id.
        prevSceneId - must be another favorited scene or error is raised.
        
        Both updating and executing doesn't blocks a scene from adding to/removing from favorited list.
        '''
        with self.__fav_lock:
            # Validation for sceneId.
            if not self.__sceneController.has(sceneId):
                raise AutomationException(11092, "sceneId does not belongs to any scene - sceneId provided: " + str(sceneId))
            
            # Because UI display in reversed order, hence their prevSceneId == our nextSceneId
            nextSceneId = prevSceneId or None
            
            # Get favSort before sceneId of nextSceneId
            if nextSceneId is None:
                maxFavSort = self.__sceneController.get_largest_favsort_num() # If len of favorited list is 0, maxFavSort = 0
                # favSort stores number to be assigned to sceneId.
                favSort = maxFavSort + 1
            else:
                try:
                    # favSort stores number to be assigned to sceneId.
                    # current favSort of prevSceneId will becomes favSort of sceneId.
                    favSort = self.__sceneController.get_favsort_of(nextSceneId)
                except Exception as e:
                    raise AutomationException(11092, "prevSceneId does not belongs to any scene - " + \
                                                    "prevSceneId provided: " + str(nextSceneId) + ", error: " + str(e))
                else:
                    if favSort is None:
                        raise AutomationException(13000, "prevSceneId does not belongs to any favorited scene - " + \
                                                        "prevSceneId provided: " + str(nextSceneId) + ", error: " + str(e))
                
            # Update favSort of the scene
            try:
                self.__sceneController.update_favorited_scene(sceneId, favSort)
                self.__sceneController.commit()
            except Exception as e:
                self.__sceneController.rollback()
                Logger.log_error("SceneService.set_favorited_scene failed to update favorited scene, ex:", str(e))
                raise AutomationException(13001, "unexpected error: " + str(e))
    
            # Broadcast events
            self.__broadcast_message__scene_updated(sceneId)
            self.__broadcast_message__favorited_scene_added(sceneId, prevSceneId)
    
    def delete_favorited_scene(self, sceneId):
        '''
        sceneId - must be a favorited scene.
        '''
        with self.__fav_lock:
            try:
                favSort = self.__sceneController.get_favsort_of(sceneId)
            except Exception as e:
                raise AutomationException(11092, "prevSceneId does not belongs to any scene - " + \
                                                "prevSceneId provided: " + str(sceneId) + ", error: " + str(e))
            else:
                if favSort is None:
                    raise AutomationException(13000, "sceneId does not belongs to any favorited scene - " + \
                                                    "sceneId provided: " + str(sceneId))
            
            # This method raise error and rollback automatically if failed, or commit once succeed.
            try:
                self.__sceneController.delete_favorited_scene(sceneId)
                self.__sceneController.commit()
            except Exception as e:
                self.__sceneController.rollback()
                Logger.log_error("SceneService.delete_favorited_scene failed to delete favorited scene, ex:", str(e))
                raise AutomationException(13002, "unexpected error: " + str(e))
            
            #Broadcast event
            self.__broadcast_message__scene_updated(sceneId)
            self.__broadcast_message__favorited_scene_deleted(sceneId)
    
    def list_favorited_scene(self, offset=0, limit=200):
        '''
        Favorited scenes.
        '''
        return self.__sceneController.list_favorited_scenes_reversed(offset, limit), \
                self.__sceneController.count_favorited_scenes()

    def __verify_scene_updated(self, sceneId):
        try:
            statusProcessed = self.__sceneController.get_status_processed(sceneId)
            if statusProcessed == AppConstants.SCENE_STATUS_UPDATING:
                raise AutomationException(11903, "edit/execute/delete scene is not allowed when its updating. " + \
                                          "Wait until the update process is completed.")
        except:
            raise AutomationException(11902, "Scene ID provided:" + str(sceneId))
        
    def __broadcast_message__scene_update_started(self, sceneId, sceneName=None):
        eventTag = AppConstants.EVENT_SCENE_UPDATE_STARTED
        eventData = {"sceneId": sceneId, "newSceneName":sceneName}
    
        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Scene Start Update:", sceneName)
        
    def __broadcast_message__scene_updated(self, sceneId):
        try:
            scene = self.__sceneController.get_summary(sceneId)
        except Exception as e:
            Logger.log_error("SceneService.__broadcast_message__scene_updated get_summary ex:", e)
            scene = None
            
        eventTag = AppConstants.EVENT_SCENE_UPDATED
        eventData = {"sceneId":sceneId, "newSceneSummary":scene}

        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Scene Updated:", scene["sceneName"])

    def __broadcast_message__scene_update_failed(self, sceneId, sceneName=None):
        '''
        sceneName - For debugging purpose.
        '''
        try:
            scene = self.__sceneController.get_summary(sceneId)
        except Exception:
            scene = None
        
        eventTag = AppConstants.EVENT_SCENE_UPDATE_FAILED
        eventData = {"sceneId": sceneId, "oldSceneSummary":scene}

        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Scene Update Failed:", sceneName)
        
    def __broadcast_message__scene_deleted(self, sceneId):
        eventTag = AppConstants.EVENT_SCENE_DELETED
        eventData = {"sceneId": sceneId}

        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Scene Deleted: Id -", sceneId)
        
    def __broadcast_message__favorited_scene_added(self, sceneId, prevSceneId):
        eventTag = AppConstants.EVENT_FAVORITED_SCENE_ADDED
        eventData = {"sceneId":sceneId, "prevSceneId":prevSceneId}
        
        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Favorited scene added/updated: Id", sceneId, "prevId:", prevSceneId)
    
    def __broadcast_message__favorited_scene_deleted(self, sceneId):
        eventTag = AppConstants.EVENT_FAVORITED_SCENE_DELETED
        eventData = {"sceneId":sceneId}
        
        self.__broadcast_message(eventTag, eventData)
        Logger.log_info("Favorited scene deleted: Id", sceneId)

    def __broadcast_message(self, eventTag, eventData):
        eventData = json.dumps(eventData, cls=AutomationJSONEncoder)
        Application.send_web_server_event(eventTag, eventData)

    def __execute_scene_implementation(self, sceneId, execution, serObj, language):
        '''
        ** Call execute_scene; DO NOT call this function directly.
        '''
        Logger.log_info("execute scene id:", sceneId)
        
        def execution_func(sceneThreadEvent, kbxMethodId, seri, **kwargs):
            try:
                if kbxMethodId == -291:
                    # Delay Timer
                    delayInSec = kwargs["delayInSec"]
                    sceneThreadEvent.wait(delayInSec)
                    seri["seriError"] = None
                else:
                    # Execute method
                    result = SharedMethod.call(**kwargs)
                    seri["seriError"] = str(result)
                    
                seri["seriStatus"] = "ok"
            
            except Exception as e:
                seri["seriStatus"] = "error"
                seri["seriError"] = str(e)
                Logger.log_debug("Execution failed, method:", kwargs["kbxMethodName"])
            
            finally:
                sceneThreadEvent.set()
                
            
        try:
            # Record for debugging purpose
            serStartTime = time.time()
            
            #===================================================================
            # Prepare to execute execution methods
            #===================================================================
            sceneExecLock = self.__sceneExecLocks.get(sceneId)
            sceneThreadEvent = sceneExecLock.get_thread_event()
            seris = deque()
            
            methodExecTime = int(time.time())
            isLoopCompleted = True
            for row in execution:
                kbxMethodId = row["kbxMethodId"]
                kbxMethodName = row["kbxMethodName"]
                kbxGroupId = row["kbxGroupId"]
                kbxMethodStatus = row["kbxMethodStatus"]
                methodParamsWithCurrentValues = row["kbxMethodParams"]
                seri = {"kbxMethodId":kbxMethodId,
                        "kbxGroupId":kbxGroupId,
                        "kbxMethodName":kbxMethodName,
                        "kbxMethodParams":methodParamsWithCurrentValues}
                seris.append(seri)
                # Check is stop
                if sceneExecLock.is_stop():
                    if not isLoopCompleted:
                        serEndTime = time.time()
                        isLoopCompleted = False
                        # === Execution interrupted ===
                    continue
                
                # Check is method not removed
                elif kbxMethodStatus not in (SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE):
                    seri["seriStatus"] = "error"
                    seri["seriError"] = "method is removed"
                    continue
    
                kwargs = {methodParam[AppConstants.ARG_NAME]: methodParam[AppConstants.ARG_CURRENT_VALUE]
                          for methodParam in methodParamsWithCurrentValues}
    
                if AppInfo.REQUEST_KEY_LANGUAGE not in kwargs:
                    kwargs[AppInfo.REQUEST_KEY_LANGUAGE] = AppInfo.DEFAULT_API_LANGUAGE
                
                kwargs["kbxMethodName"] = kbxMethodName
                kwargs["kbxGroupId"] = kbxGroupId
                kwargs["kbxModuleName"] = row["kbxModuleName"]
                kwargs["kbxMethodAppId"] = row["kbxMethodAppId"]
                kwargs[AppConstants.KEY_ACTION_TIMESTAMP] = methodExecTime
                
                #===========================================================
                # Execute method
                #===========================================================
                sceneThreadEvent.clear()
                
                execThread = threading.Thread(target=execution_func, args=[sceneThreadEvent, row["kbxMethodId"], seri], kwargs=kwargs)
                execThread.daemon = False
                execThread.start()
                
                sceneThreadEvent.wait() # Event will be set by "stop_scene" or SharedMethod.call returns.
                
                # Check is stop
                if sceneExecLock.is_stop():
                    if not isLoopCompleted:
                        serEndTime = time.time()
                        isLoopCompleted = False
                        # === Execution interrupted ===
                    continue
                
            if isLoopCompleted:
                # Record for debugging purpose
                serEndTime = time.time()
                # === Execution completed ===
            
        except Exception as e:
            # This is unexpected error. Execution will not be recorded by Scene Execution Result.
            Logger.log_error("SceneService.__execute_scene_implementation ex:", e)
            # === Execution completed with errors ===
            
        else:
            if serObj is not None:
                # Log to sceneExecutionResultService
                self.__sceneExecutionResultThreadPool.submit(self.__add_scene_execution_result,
                                                             serUrl=serObj["serUrl"], 
                                                             serStartTime=serStartTime, 
                                                             serEndTime=serEndTime, 
                                                             sceneName=serObj["sceneName"], 
                                                             sceneProtected=serObj["sceneProtected"],
                                                             sceneId=sceneId, 
                                                             execution=seris, 
                                                             language=language)
            
        finally:
            del(self.__sceneExecLocks[sceneId])  # Delete exec lock
            sceneExecLock.release()
            
    def __add_scene_execution_result(self, serUrl, serStartTime, serEndTime, sceneName, sceneProtected, sceneId, execution, language):
            try:
                SceneExecutionResultService.instance().add_scene_execution_result(serUrl=serUrl, 
                                                                                  serStartTime=serStartTime, 
                                                                                  serEndTime=serEndTime, 
                                                                                  sceneName=sceneName, 
                                                                                  sceneProtected=sceneProtected, 
                                                                                  sceneId=sceneId, 
                                                                                  execution=execution, 
                                                                                  language=language)
            except Exception as e:
                Logger.log_error("SceneService.__add_scene_execution_result ex:", e)
                
            