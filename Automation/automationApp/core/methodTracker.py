##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
#    Xuan Automation Application is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
import copy
import threading

from automationApp.appConstants import AppConstants
from automationApp.core.groupTracker import GroupTracker
from automationApp.core.storage import Storage
from automationApp.dto.methodDTO import MethodDTO
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class MethodGroupId(object):

    def __init__(self):
        self.__pairs = Storage.list_all_method_groups()
        Logger.log_debug("Restored Method-Group Id from database:", self.__pairs)

    def get_pair(self, methodId):
        Logger.log_debug("Retrieve group:", methodId, " from ", self.__pairs)
        return self.__pairs.get(methodId, None)

    def add_pair(self, methodId, groupId):
        if groupId is None or groupId == -1:
            return
        
        if methodId in self.__pairs:
            currentGroupId = self.__pairs[methodId]
            if currentGroupId == groupId:
                return

        self.__pairs[methodId] = groupId
        Storage.store_method_group(methodId, groupId)
        Logger.log_debug("Method-Group Id Pair Added:", methodId, "-", groupId)

    def delete_pair(self, methodId):
        if methodId in self.__pairs:
            del(self.__pairs[methodId])
            Storage.delete_method_group(methodId)
            Logger.log_debug("Method-Group Id Pair Removed:", methodId)


class MethodTracker(object):

    METHOD_ACTIVATED_CB = None
    METHOD_DEACTIVATED_CB = None
    METHOD_REMOVED_CB = None
    METHOD_UPDATED_CB = None

    def __init__(self, updateCB=None):
        self.__methods = {} # {"ruleIds":set([]), "data":methodDTO, "isUpdated":False}
        self.__updateCB = updateCB # Receives: methodId, *ruleIds

        MethodTracker.METHOD_ACTIVATED_CB = self.__method_activated_system_notify
        MethodTracker.METHOD_DEACTIVATED_CB = self.__method_deactivated_system_notify
        MethodTracker.METHOD_REMOVED_CB = self.__method_removed_system_notify
        MethodTracker.METHOD_UPDATED_CB = self.__method_updated_system_notify

        self.__methodGroupId = MethodGroupId()
        self.__groupTracker = GroupTracker(self.__on_group_updated)
        
    def update_method(self, ruleId, *methodIds):

        methodIdsToProcess = set([])

        #=======================================================================
        # Remove previously recorded entries
        #=======================================================================
        for methodId, methodObj in self.__methods.items():
            if ruleId in methodObj["ruleIds"]:
                methodObj["ruleIds"].remove(ruleId)
                methodIdsToProcess.add(methodId)

        #=======================================================================
        # Re-register all entries
        #=======================================================================
        for methodId in methodIds:
            try:
                methodObj = self.__methods[methodId]
            except:
                methodDTO = MethodDTO()
                methodDTO.set_method_id(methodId)

                methodDTO.set_status_code(AppConstants.METHOD_ERROR_METHOD_REMOVED[0])
                methodDTO.set_status_message(AppConstants.METHOD_ERROR_METHOD_REMOVED[1])

                methodObj = {"ruleIds":set([]), "data":methodDTO, "isUpdated":False, "isGroupUpdated":False, "syncLock":threading.Lock()}
                self.__methods[methodId] = methodObj

            methodObj["ruleIds"].add(ruleId)
            methodIdsToProcess.add(methodId)

        #=======================================================================
        # Process affected entries
        #=======================================================================
        for methodId in methodIdsToProcess:
            self.__process_method(methodId)

    def get_method(self, methodId):
        if methodId not in self.__methods:
            return None
        return self.__methods[methodId]["data"]

    def get_group(self, groupId):
        return self.__groupTracker.get_group(groupId)

    def get_tags_by_id(self, methodIds):
        tags = set([])
        for methodId in methodIds:
            try:
                methodObj = self.__methods[methodId]
                if methodObj["isUpdated"] is True:
                    methodDTO = methodObj["data"]

                    if methodDTO.get_method_status() == SharedMethod.METHOD_STATUS_ACTIVE:
                        eventTag = methodDTO.get_method_event()

                        if isinstance(eventTag, str):
                            tags.add(eventTag)
                        elif isinstance(eventTag, list):
                            for eachEventTag in eventTag:
                                if isinstance(eachEventTag, str):
                                    tags.add(eachEventTag)
            except:
                continue

        return tags

    def check_is_updated(self, methodIds):
        try:
            methodObjs = [self.__methods[methodId] for methodId in methodIds]
            return all([methodObj["isUpdated"] and methodObj["isGroupUpdated"] for methodObj in methodObjs])
        except Exception as e:
            Logger.log_debug(e)
            return False

    def update_language(self, language, methodIds):
        #=======================================================================
        # Group up by app id for methods that requires update
        #=======================================================================
        appMethodDict = {}
        groupIds = set([])

        for methodId in methodIds:
            if methodId in self.__methods:
                methodDTO = self.__methods[methodId]["data"]

                if methodDTO.get_status_code() != AppConstants.METHOD_ERROR_METHOD_REMOVED[0]:
                    methodAppId = methodDTO.get_method_app_id()
                else:
                    methodAppId = "removed"

                if methodAppId not in appMethodDict:
                    appMethodDict[methodAppId] = set([])
                appMethodDict[methodAppId].add(methodId)

                groupIds.add(methodDTO.get_group_id())

        #=======================================================================
        # Update group language
        #=======================================================================
        self.__groupTracker.update_language(language, list(groupIds))

        #=======================================================================
        # Retrieve from each apps
        #=======================================================================
        for eachAppId, eachMethodIds in appMethodDict.items():

            if eachAppId != "removed":
                try:
                    retrievedData = SharedMethod.list_shared_methods_by_app_id(eachAppId, kbxMethodIds=list(eachMethodIds), language=language)
                except:
                    retrievedData = {}
            else:
                retrievedData = {}

            for methodId in eachMethodIds:
                methodDTO = self.__methods[methodId]["data"]
                try:
                    methodDTO.update(retrievedData[methodId])
                except:
                    pass

                try:
                    groupDTO = self.__groupTracker.get_group(methodDTO.get_group_id())
                    groupDTO = copy.deepcopy(groupDTO)
                    del(groupDTO["statusCode"])
                    del(groupDTO["statusMessage"])
                    methodDTO.update(groupDTO)
                except:
                    pass

    def __update_method(self, methodDTO, updateType=None):
        methodId = methodDTO.get_method_id()
        
        try:
            methodObj = self.__methods[methodId]
        except:
            return
        
        with methodObj["syncLock"]:
            try:
                if updateType == None:
                    if methodObj["isUpdated"] is not False:
                        return
                    
                    methodObj["isUpdated"] = None # Means under processing
                    
                    methodDict = SharedMethod.get_shared_method_by_id(methodId, language=AppInfo.DEFAULT_API_LANGUAGE)
                    methodDTO.update(methodDict)
                    
                elif updateType == 1: # Method activated
                    methodDTO.set_method_status(SharedMethod.METHOD_STATUS_ACTIVE)
                elif updateType == 0: # Method deactivated
                    methodDTO.set_method_status(SharedMethod.METHOD_STATUS_INACTIVE)
                elif updateType == -1: # Method removed
                    raise Exception()
                
                #===================================================================
                # Update method status
                #===================================================================
                methodStatus = methodDTO.get_method_status()
                if methodStatus not in (SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE):
                    raise Exception()
    
                if methodStatus == SharedMethod.METHOD_STATUS_ACTIVE:
                    methodDTO.set_status_code(AppConstants.METHOD_ERROR_OK[0])
                    methodDTO.set_status_message(AppConstants.METHOD_ERROR_OK[1])
                elif methodStatus == SharedMethod.METHOD_STATUS_INACTIVE:
                    methodDTO.set_status_code(AppConstants.METHOD_ERROR_METHOD_OFF[0])
                    methodDTO.set_status_message(AppConstants.METHOD_ERROR_METHOD_OFF[1])
    
            except:
                try:
                    methodDTO.reset()
                except Exception as se:
                    Logger.log_debug("Reset Method DTO err:", se)
                
                methodDTO.set_status_code(AppConstants.METHOD_ERROR_METHOD_REMOVED[0])
                methodDTO.set_status_message(AppConstants.METHOD_ERROR_METHOD_REMOVED[1])
                
            #=======================================================================
            # Set method to "isUpdated"
            #=======================================================================
            methodObj["isUpdated"] = True
    
            #===================================================================
            # Process method group if group is updated
            #===================================================================
            groupId = methodDTO.get_group_id()
            if groupId in (None, -1): # Mainly because of method is removed
                groupId = self.__methodGroupId.get_pair(methodId) # Try to restore group id from local history
                
            if groupId not in (None, -1):
                methodDTO.set_group_id(groupId)
                self.__groupTracker.add_group(groupId, methodId)
                self.__methodGroupId.add_pair(methodId, groupId)
    
                isGroupUpdated = self.__groupTracker.check_is_updated(groupId)
                methodObj["isGroupUpdated"] = isGroupUpdated
    
                if isGroupUpdated is True:
                    groupDTO = self.__groupTracker.get_group(groupId)
                    if groupDTO.get_status_code() != AppConstants.METHOD_ERROR_OK[0]:
                        methodDTO.set_status_code(AppConstants.METHOD_ERROR_GROUP_REMOVED[0])
                        methodDTO.set_status_message(AppConstants.METHOD_ERROR_GROUP_REMOVED[1])
            else:
                methodObj["isGroupUpdated"] = True
    
            #===========================================================
            # Determine method has event, and set to 'kbxMethodHasEvent'
            #===========================================================
            methodStatus = methodDTO.get_method_status()
    
            if methodStatus == SharedMethod.METHOD_STATUS_ACTIVE:
                methodEvents = methodDTO.get_method_event()
    
                if isinstance(methodEvents, list):
                    hasEvent = len(methodEvents) > 0
                else:
                    hasEvent = not Util.is_empty(methodEvents)
    
                methodDTO.set_method_has_event(hasEvent)
            else:
                methodDTO.set_method_has_event(False)
    
            #===================================================================
            # Callback to notify changes
            #===================================================================
            ruleIds = self.__methods[methodId]["ruleIds"]
            if len(ruleIds) > 0:
                AppConstants.get_thread_pool_executor().submit(self.__updateCB, methodId, *list(ruleIds))

    def __on_group_updated(self, groupDTO):
        groupId = groupDTO.get_group_id()
        groupStatusCode = groupDTO.get_status_code()

        for methodId, methodObj in self.__methods.items():
            methodDTO = methodObj["data"]
            if groupId == methodDTO.get_group_id():
                if groupStatusCode != AppConstants.METHOD_ERROR_OK[0]:
                    methodDTO.set_status_code(AppConstants.METHOD_ERROR_GROUP_REMOVED[0])
                    methodDTO.set_status_message(AppConstants.METHOD_ERROR_GROUP_REMOVED[1])

                methodObj["isGroupUpdated"] = True

                ruleIds = methodObj["ruleIds"]
                AppConstants.get_thread_pool_executor().submit(self.__updateCB, methodId, *list(ruleIds))

    def __method_activated_system_notify(self, methodId):
        if methodId not in self.__methods:
            return

        methodDTO = self.__methods[methodId]["data"]

        self.__update_method(methodDTO, 1)

    def __method_deactivated_system_notify(self, methodId):
        if methodId not in self.__methods:
            return

        methodDTO = self.__methods[methodId]["data"]

        self.__update_method(methodDTO, 0)

    def __method_removed_system_notify(self, methodId):
        if methodId not in self.__methods:
            return

        methodDTO = self.__methods[methodId]["data"]

        self.__update_method(methodDTO, -1)
        
    def __method_updated_system_notify(self, methodId):
        if methodId not in self.__methods:
            return
        
        methodObj = self.__methods[methodId]
        methodObj["isUpdated"] = False
        
        methodDTO = methodObj["data"]

        self.__update_method(methodDTO)

    def __process_method(self, methodId):
        try:
            methodObj = self.__methods[methodId]
        except:
            return

        if len(methodObj["ruleIds"]) == 0:
            del(self.__methods[methodId])
            self.__methodGroupId.delete_pair(methodId)
            self.__groupTracker.remove_group_by_method_id(methodId)
        else:
            if methodObj["isUpdated"] is False:
                AppConstants.get_thread_pool_executor().submit(self.__update_method, methodObj["data"])

