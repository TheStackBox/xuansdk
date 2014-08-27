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
import threading

from automationApp.appConstants import AppConstants
from automationApp.core.storage import Storage
from automationApp.dto.groupDTO import GroupDTO
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class GroupLabel(object):

    def __init__(self):
        self.__pairs = Storage.list_all_groups()
        Logger.log_debug("Restored Group-Label from database:", self.__pairs)

    def get_pair(self, groupId):
        Logger.log_debug("Retrieve Group-Label:", groupId, " from ", self.__pairs)
        return self.__pairs.get(groupId, None)

    def add_pair(self, groupId, groupLabel):
        if groupLabel is None:
            return    
    
        if groupId in self.__pairs:
            currentLabel = self.__pairs[groupId]
            if currentLabel == groupLabel:
                return

        self.__pairs[groupId] = groupLabel
        Storage.store_group(groupId, groupLabel)
        Logger.log_debug("Group-Label Pair Added:", groupId, "-", groupLabel)

    def delete_pair(self, groupId):
        if groupId in self.__pairs:
            del(self.__pairs[groupId])
            Storage.delete_group(groupId)
            Logger.log_debug("Group-Label Pair Removed:", groupId)


class GroupTracker(object):

    GROUP_REMOVED_CB = None # Call to this method to inform group removed notification from system. ## Remember to provides groupId.
    GROUP_UPDATED_CB = None

    def __init__(self, updateCB=None):
        self.__groups = {} # {"methodIds": set([]), "data":groupDTO, "isUpdated":False}

        self.__updateCB = updateCB # Receive Group DTO

        GroupTracker.GROUP_REMOVED_CB = self.__group_removed_system_notify
        GroupTracker.GROUP_UPDATED_CB = self.__group_updated_system_notify

        self.__groupLabel = GroupLabel()

    def add_group(self, groupId, methodId):
        if groupId not in self.__groups:
            groupDTO = GroupDTO()

            groupDTO.set_group_id(groupId)

            groupDTO.set_status_code(AppConstants.METHOD_ERROR_GROUP_REMOVED[0])
            groupDTO.set_status_message(AppConstants.METHOD_ERROR_GROUP_REMOVED[1])

            self.__groups[groupId] = {"methodIds": set([]), "data":groupDTO, "isUpdated":False, "syncLock":threading.Lock()}
            AppConstants.get_thread_pool_executor().submit(self.__update_group, groupDTO)

        self.__groups[groupId]["methodIds"].add(methodId)

    def remove_group_by_method_id(self, methodId):
        groupIdsToRemove = set([])
        for groupId, groupObj in self.__groups.items():
            if methodId in groupObj["methodIds"]:
                groupIdsToRemove.add(groupId)

        for groupId in groupIdsToRemove:
            self.__remove_group(groupId, methodId)

    def check_is_updated(self, groupId):
        try:
            groupObj = self.__groups[groupId]
            return groupObj["isUpdated"]
        except:
            return False

    def __remove_group(self, groupId, methodId):
        try:
            self.__groups[groupId]["methodIds"].remove(methodId)
        except:
            return

        #===================================================================
        # Completely remove group if no more method holding it
        #===================================================================
        if len(self.__groups[groupId]["methodIds"]) <= 0:
            del(self.__groups[groupId])
            self.__groupLabel.delete_pair(groupId)

    def get_group(self, groupId):
        if groupId in self.__groups:
            return self.__groups[groupId]["data"]
        else:
            return None

    def update_language(self, language, groupIds):
        #=======================================================================
        # Group up by app id for methods that requires update
        #=======================================================================
        appGroupDict = {}
        for groupId in groupIds:
            if groupId in self.__groups:
                groupDTO = self.__groups[groupId]["data"]

                if groupDTO.get_status_code() != AppConstants.METHOD_ERROR_GROUP_REMOVED[0]:

                    groupAppId = groupDTO.get_group_app_id()
                else:
                    groupAppId = "removed"

                if groupAppId not in appGroupDict:
                    appGroupDict[groupAppId] = set([])
                appGroupDict[groupAppId].add(groupId)

        #=======================================================================
        # Retrieve from each apps
        #=======================================================================
        for eachAppId, eachGroupIds in appGroupDict.items():

            if eachAppId != "removed":
                try:
                    retrievedData = SharedMethod.list_shared_method_groups_by_app_id(eachAppId, kbxGroupIds=list(eachGroupIds), language=language)
                except:
                    retrievedData = {}
            else:
                retrievedData = {}

            for groupId in eachGroupIds:
                groupDTO = self.__groups[groupId]["data"]
                try:
                    groupDTO.update(retrievedData[groupId])
                except:
                    groupDTO.set_group_label(self.__groupLabel.get_pair(groupId))

    def __update_group(self, groupDTO, updateType=None):
        groupId = groupDTO.get_group_id()

        try:
            groupObj = self.__groups[groupId]
        except:
            return
        
        with groupObj["syncLock"]:
            try:
    
                if updateType == None:
                    if groupObj["isUpdated"] is not False:
                        return
                    
                    groupObj["isUpdated"] = None # Means Under processing
    
                    groupDict = SharedMethod.get_shared_method_group_by_id(groupId, language=AppInfo.DEFAULT_API_LANGUAGE)
                    groupDTO.update(groupDict)
    
                elif updateType == -1:
                    raise Exception()
    
                groupDTO.set_status_code(AppConstants.METHOD_ERROR_OK[0])
                groupDTO.set_status_message(AppConstants.METHOD_ERROR_OK[1])
    
                #===================================================================
                # Store into database
                #===================================================================
                groupLabel = groupDTO.get_group_label()
                self.__groupLabel.add_pair(groupId, groupLabel)
                
                Logger.log_debug("Update Group Success: Id -", groupId)
    
            except Exception as e:
                try:
                    groupDTO.reset()
                except Exception as se:
                    Logger.log_debug("Reset Group DTO err:", se)
                
                groupDTO.set_status_code(AppConstants.METHOD_ERROR_GROUP_REMOVED[0])
                groupDTO.set_status_message(AppConstants.METHOD_ERROR_GROUP_REMOVED[1])
    
                groupDTO.set_group_label(self.__groupLabel.get_pair(groupId))
                
                Logger.log_debug("Update Group Error: Id -", groupId, "err -", e)
    
            #=======================================================================
            # Set groupObj status to updated
            #=======================================================================
            groupObj["isUpdated"] = True
            
            #=======================================================================
            # Notify group updated. Get the status in groupDTO by yourself
            #=======================================================================
            if callable(self.__updateCB):
                self.__updateCB(groupDTO)

    def __group_removed_system_notify(self, groupId=None):
        Logger.log_debug("Received remove group request:", groupId)
        if groupId not in self.__groups:
            Logger.log_debug("Drop remove group request:", groupId)
            return
        
        Logger.log_debug("Ready to remove group:", groupId)
        self.__update_group(self.__groups[groupId]["data"], -1)

    def __group_updated_system_notify(self, groupId=None):
        Logger.log_debug("Received update group request:", groupId)
        if groupId not in self.__groups:
            Logger.log_debug("Drop update group request:", groupId)
            return
        
        Logger.log_debug("Ready to update group:", groupId)
        groupObj = self.__groups[groupId]
        groupObj["isUpdated"] = False
        groupDTO = groupObj["data"]
                
        self.__update_group(groupDTO)
