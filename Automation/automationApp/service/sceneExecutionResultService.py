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

from concurrent.futures.thread import ThreadPoolExecutor
import json
import threading
import time

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.sceneExecutionResultController import SceneExecutionResultController
from automationApp.core.sceneExecutionResultController import SceneExecutionResultDataHandler
from automationApp.utils.automationJSONEncoder import AutomationJSONEncoder
from automationApp.utils.sharedMethodWrapper import SharedMethodWrapper
from com.cloudMedia.theKuroBox.sdk.app.application import Application
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.service.manager.notificationManagerService import NotificationManagerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class SERLock:
    '''
    Lock serIds to make sure they "retry" safely in multi-threaded environment.
    '''
    
    
    def __init__(self):
        self.__lock = threading.Lock()
        self.__locked = set({})
        self.__deleted = set({})
        
    def lock(self, serId):
        '''
        Lock a serId.
        Request for a lock on locked serId will cause KeyError raised.
        '''
        with self.__lock:
            if serId in self.__locked:
                raise KeyError("item is locked")
            else:
                self.__locked.add(serId)
    
    def unlock(self, serId):
        '''
        Unlock a previously locked serId.
        Exception raised if no "lock" is called previously.
        '''
        with self.__lock:
            self.__locked.remove(serId)
            if serId in self.__deleted:
                self.__deleted.remove(serId)
            
    def declare_as_deleted(self, serId):
        '''
        Declare a record with particular serId is deleted.
        '''
        with self.__lock:
            if serId in self.__locked:
                self.__deleted.add(serId)
                
    def is_deleted(self, serId):
        '''
        Check if a record with particular serId is deleted.
        '''
        with self.__lock:
            return serId in self.__deleted

class SceneExecutionResultService:
    

    __INSTANCE = None
    __LOCK = threading.Lock()
    

    @staticmethod
    def instance():
        with SceneExecutionResultService.__LOCK:
            SceneExecutionResultService.__INSTANCE or SceneExecutionResultService()
            return SceneExecutionResultService.__INSTANCE

    def __init__(self):
        self.__lock = threading.Lock()
        self.__serLock = SERLock()
        self.__serController = SceneExecutionResultController()
        self.__serRetryThreadPool = ThreadPoolExecutor(max_workers=3)
        
        def after_ser_deleted(serId):
            self.__serLock.declare_as_deleted(serId) # Report serId is deleted to SERLock instance. 
            self.__broadcast_message__ser_deleted(serId) # Broadcast event to mobile client.
        
        SceneExecutionResultDataHandler.AFTER_RECORD_DELETE = after_ser_deleted
        SceneExecutionResultService.__INSTANCE = self
        
    def add_scene_execution_result(self, serUrl, serStartTime, serEndTime, sceneName, sceneProtected, sceneId, execution, language="en"):
        '''
        Get kbxGroupLabel for each execution item and pass to serController.
        '''
        # Get kbxGroupLabel
        for item in execution:
            kbxGroupId = item.pop("kbxGroupId", None)
            if kbxGroupId is None:
                item["kbxGroupLabel"] = "-- Unknown --"
            else:
                try:
                    kbxGroup = SharedMethodWrapper.get_shared_method_group_by_id(kbxGroupId, enableTagCount=False, language=language)
                    item["kbxGroupLabel"] = kbxGroup.get("kbxGroupLabel", "-- Unnamed --")
                except:
                    item["kbxGroupLabel"] = "-- Removed --"
                    
        with self.__lock: # Add scene execution result happens sequentially.
            # Make serCreatedTime unique.
            # This is the smallest pause unit to make a difference on each time.time() call.
            time.sleep(0.001)
            serCreatedTime = time.time()
            serId = str(serCreatedTime)
            
            self.__serController.add(serId, serCreatedTime, serStartTime, serEndTime, 
                                     sceneId, sceneName, sceneProtected, execution)
            
            # Build notification information.
            KBXLang.set_preferred_lang(language)
            
            notiLink = str(serUrl) + "?serId=" + str(serId)
            notiLinkLabel = str(KBXLang("ser_noti_link_label"))
            
            for seri in execution:
                if seri["seriStatus"] == "error":
                    notiContent = str(KBXLang("ser_noti_exec_completed_with_error"))
                    break
            else:
                notiContent = str(KBXLang("ser_noti_exec_completed"))
                
            notiContent = str(sceneName).join(notiContent.split(":scenename:"))
                            
            self.__notify_ser_added(notiContent, notiLink, notiLinkLabel)
    
    def get_scene_execution_result(self, serId, language):
        '''
        Get complete serObject from serController, and add in full details obtained from shared method manager.
        '''
        try:
            serObject = self.__serController.get_ser_and_seris(serId)
        except:
            raise AutomationException(12000, "Scene Execution Result not found, ID provided:" + str(serId))
        
        execution = serObject["execution"]
        
        # Add details into each execution item.
        for kbxMethod in execution:
            kbxMethodId = kbxMethod["kbxMethodId"]
            try:
                kbxMethodWithDetails = SharedMethodWrapper.get_shared_method_by_id(kbxMethodId, language)
                kbxMethod["kbxMethodLabel"] = kbxMethodWithDetails.get("kbxMethodLabel")
                
                # Rebuild parameters.
                paramsWithDetails = {}
                for paramWithDetails in kbxMethodWithDetails.get("kbxMethodParams", None):
                    paramsWithDetails[paramWithDetails["kbxParamName"]] = paramWithDetails
                
                for kbxMethodParam in kbxMethod["kbxMethodParams"]:
                    try:
                        # Update kbxMethodParam with the one with details. 
                        kbxParamCurrentValue = kbxMethodParam["kbxParamCurrentValue"]
                        kbxMethodParam.update(paramsWithDetails[kbxMethodParam["kbxParamName"]])
                        kbxMethodParam["kbxParamCurrentValue"] = kbxParamCurrentValue # But remains current value no matter what.
                    except Exception as e:
                        kbxMethodParam["atDebug"] = "Unable to match parameter: " + str(e)
                        continue
            except Exception as e:
                kbxMethod["atDebug"] = "Unable to get shared method:" + str(e)
                continue
                    
        return serObject
    
    def retry_scene_execution_result_item(self, serId, seriIndex=None):
        '''
        Retry all scene execution result item with error according seriIndex
        
        Each ser can be in retry mode one at a time.
        If an item is deleted during execution, execution progress will be completed without event broadcasted.
        '''
        # Lock scene execution result for retry.
        try:
            self.__serLock.lock(serId)
        except Exception:
            raise AutomationException(12004, "Scene execution result is retrying.")
        
        try:
            if Util.is_empty(seriIndex): # Retry all items with error.
                serisWithError = self.__serController.list_seris_with_error(serId)
                if len(serisWithError) == 0:
                    raise AutomationException(12002, "We've found no scene execution result item with error to retry")
                else:
                    serisWithError = [dict(seriWithError) for seriWithError in serisWithError]
            else:
                seriWithError = self.__serController.get_seri_by_index(serId, seriIndex)
                if seriWithError is None:
                    raise AutomationException(12001, "scene execution result item not found, serId: " + str(serId) + " seriIndex: " + str(seriIndex))
                elif seriWithError["seriStatus"] != "error":
                    raise AutomationException(12003, "scene execution result item not error, current status: " + str(seriWithError["seriStatus"]))
                
                serisWithError = [seriWithError]
            
        except Exception as e:
            # Unlock scene execution after retry.
            self.__serLock.unlock(serId)
            raise e
        
        else:
            seriIndexes = [seriWithError["seriIndex"] for seriWithError in serisWithError]
            self.__serRetryThreadPool.submit(self.__retry_seri_implementation, serId, serisWithError, seriIndexes)
            return seriIndexes
            
    def __retry_seri_implementation(self, serId, serisWithError, seriIndexes):
        try:
            # Update statuses of all items to be retried to "busy".
            self.__serController.update_seri_status(serId=serId, seriIndexes=seriIndexes, seriStatus="busy", seriError=None)
            
            # Broadcast event.
            self.__broadcast_message__seri_retry_started(serId, seriIndexes=seriIndexes)
            
            # Retry process starts here.
            for seri in serisWithError:
                try:
                    kbxMethodId = seri["kbxMethodId"]
                    if kbxMethodId != -291: # Skips all -291 and declare as "ok" immediately.
                        params = {kbxMethodParam["kbxParamName"]:kbxMethodParam["kbxParamCurrentValue"] 
                                  for kbxMethodParam in seri["kbxMethodParams"]}
                        result = SharedMethod.call_by_method_id(kbxMethodId, **params)
                        seriError = str(result)
                    else:
                        seriError = None
                    
                    seriStatus = "ok"
                    
                except Exception as e:
                    seriStatus = "error"
                    seriError = str(e)
                    
                finally:
                    seriIndex = seri["seriIndex"]
                    
                    if not self.__serLock.is_deleted(serId):
                        # Update statuses and broadcast events only if ser is not deleted.
                        self.__serController.update_seri_status(serId=serId, seriIndexes=[seriIndex], 
                                                                seriStatus=seriStatus, seriError=seriError)
                        self.__broadcast_message__seri_retry_completed(serId, seriIndex, seriStatus, seriError)
                    
        except Exception as e:
            ''' THIS PORTION SHOULD NEVER RUN. (it's bug if this portion is executed) '''
            Logger.log_error("SceneExecutionResultService.retry_scene_execution_result_item ex:", e)

        finally:
            self.__serLock.unlock(serId)
                
    def list_scene_execution_results(self, offset, limit):
        '''
        List all scene execution results without items.
        '''
        return self.__serController.list(offset, limit)
    
    def delete_scene_execution_result(self, serId):
        '''
        Delete a scene execution result. Relevant events will be broadcasted.
        NOTE: scene execution result records will be maintained automatically to ensure only 10 records in database at most.
        '''
        self.__serController.delete(serId)
            
    def __notify_ser_added(self, notiContent, notiLink, notiLinkLabel):
        Logger.log_debug("Scene Execution Result logged at:", notiLink)
        NotificationManagerService.dispatch_notification(text=notiContent, 
                                                         link=notiLink,
                                                         linkLabel=notiLinkLabel)
                    
    def __broadcast_message__ser_deleted(self, serId):
        eventTag = AppConstants.EVENT_SER_DELETED
        eventData = {"serId":serId}
        self.__broadcast_message(eventTag, eventData)
    
    def __broadcast_message__seri_retry_started(self, serId, seriIndexes):
        eventTag = AppConstants.EVENT_SERI_RETRY_STARTED
        eventData = {"serId":serId, "seriIndexes":seriIndexes}
        self.__broadcast_message(eventTag, eventData)
    
    def __broadcast_message__seri_retry_completed(self, serId, seriIndex, seriStatus, seriError):
        eventTag = AppConstants.EVENT_SERI_RETRY_COMPLETED
        eventData = {"serId":serId, "seriIndex":seriIndex,
                     "seriStatus":seriStatus, "seriError":seriError}
        self.__broadcast_message(eventTag, eventData)

    def __broadcast_message(self, eventTag, eventData):
        eventData = json.dumps(eventData, cls=AutomationJSONEncoder)
        Application.send_web_server_event(eventTag, eventData)

