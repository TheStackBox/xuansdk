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

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.core.apiController import APIController
from automationApp.core.groupController import GroupController
from automationApp.core.methodController import MethodController
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class APIService(object):


    def __init__(self):
        self.__apiController = APIController()
        self.__methodController = MethodController.instance()
        self.__groupController = GroupController.instance()

    def list_groups(self, language, section, parentId=None):
        try:
            def sort_group_list(value):
                name = value.get("kbxGroupLabel")
                if name is None:
                    return ""
                else:
                    return str(name).lower()
                
            
            unknownGroupDict = {}
            unknownGroupId = self.__get_group_ids()
                
            parentId = AppConstants.GROUP_ID_AUTOMATION if parentId is None else parentId

            result = SharedMethod.list_shared_method_groups(kbxGroupParentId=parentId, kbxMethodTag=section,
                                                            enableTagCount=True, language=language)
            
            groupList = result["groupList"]
            
            # Level 1 groups which contain of SERVICES and LOCATIONS.
            if parentId == AppConstants.GROUP_ID_AUTOMATION:
                services = deque()
                groups =  deque()
                
                for groupDict in groupList:
                    kbxGroupId = groupDict["kbxGroupId"]
                    
                    # Add indicator for UI
                    groupDict["kbxGroupHasChild"] = True

                    # Reordering
                    if kbxGroupId == AppConstants.GROUP_ID_NOTIFICATION:
                        groupDict["kbxGroupDesc"] = KBXLang("group_notification_" + section)
                        services.appendleft(groupDict)
                    elif kbxGroupId == AppConstants.GROUP_ID_SERVICE:
                        groupDict["kbxGroupDesc"] = KBXLang("group_service_" + section)
                        services.append(groupDict)
                    elif kbxGroupId == unknownGroupId:
                        #append the group dict
                        unknownGroupDict = groupDict
                    else:
                        groups.append(groupDict)
                groups = sorted(groups, key=sort_group_list)
                if len(unknownGroupDict) > 0:
                    groups.append(unknownGroupDict)
                services.extend(groups)
                groupList = services
                parentGroup = None
                
            # Level 2 groups which are DEVICES or SERVICES.
            else:
                parentGroup = SharedMethod.get_shared_method_group_by_id(kbxGroupId=parentId, language=language)

            return parentGroup, groupList

        except Exception as e:
            Logger.log_error("APIService.list_groups ex:", e)
            raise AutomationException(11601, "Unexpected error - " + str(e))

    def list_methods(self, language, section, groupId):
        try:
            result = SharedMethod.list_shared_methods(kbxGroupId=groupId,
                                                      kbxMethodTag=section,
                                                      kbxMethodStatus=[SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE],
                                                      language=language)

            methodList = result["methodList"]

            #===================================================================
            # Get group information
            #===================================================================
            groupDict = SharedMethod.get_shared_method_group_by_id(kbxGroupId=groupId, language=language)
            
            # Append "kbxMethodHasEvent" indicator.
            for kbxMethod in methodList:
                kbxMethodEvent = kbxMethod.get("kbxMethodEvent")
                kbxMethodIdentifier = kbxMethod.get("kbxMethodIdentifier")
                kbxMethod["kbxMethodHasEvent"] = not Util.is_empty(kbxMethodEvent) and not Util.is_empty(kbxMethodIdentifier)

            return methodList, groupDict
        except Exception as e:
            Logger.log_error("APIService.list_methods ex:", e)
            raise AutomationException(11601, "Unexpected error - " + str(e))

    def update_kbx_method(self, kbxMethodId):
        '''
        Returns: 
        None: Method Removed
        True: Method Active
        False: Method Inactive
        '''
        hasKBXMethod = self.__apiController.has_kbx_method(kbxMethodId)
        if not hasKBXMethod:
            raise AutomationException(11602, "Method ID provided: " + str(kbxMethodId))
        
        try:
            kbxMethod = SharedMethod.get_shared_method_by_id(kbxMethodId, language=AppInfo.DEFAULT_API_LANGUAGE)
        except SystemException as se:
            if se.value["returnValue"] == 1608:
                self.__methodController.delete(kbxMethodId)
                return None # None: Method Removed
            else:
                raise AutomationException(11601, "Unexpected returnValue when get method: " + str(se))
        else:
            self.__methodController.update(kbxMethod)
            return kbxMethod["kbxMethodStatus"] == SharedMethod.METHOD_STATUS_ACTIVE # True: Active, False: Inactive
            
    def update_kbx_group(self, kbxGroupId):
        '''
        Returns
        None: Group Removed
        True: Group Exists
        '''
        hasKBXGroup = self.__apiController.has_kbx_group(kbxGroupId)
        if not hasKBXGroup:
            raise AutomationException(11603, "Group ID provided: " + str(kbxGroupId))
        
        try:
            kbxGroup = SharedMethod.get_shared_method_group_by_id(kbxGroupId, enableTagCount=False, 
                                                                  language=AppInfo.DEFAULT_API_LANGUAGE)
        except SystemException as se:
            if se.value["returnValue"] == 1609:
                self.__groupController.delete(kbxGroupId)
                return None
            else:
                raise AutomationException(11601, "Unexpected returnValue when get method group: " + str(se))
        else:
            self.__groupController.update(kbxGroup)
            return True

    def list_kbx_methods(self, offset, limit):
        '''
        For debugging purpose.
        '''
        return self.__methodController.list(offset, limit)
    
    def list_kbx_groups(self, offset, limit):
        '''
        For debugging purpose.
        '''
        return self.__groupController.list(offset, limit)
    
    def __get_group_ids(self):
        try:
            if AppConstants.GROUP_ID_UNKNOWN_LOCATION is None:
                systemId = SharedMethod.get_system_id()
                results = SharedMethod.list_shared_method_groups(kbxGroupAppId=[systemId],
                                                                 kbxGroupParentId=AppConstants.GROUP_ID_AUTOMATION)
    
                #groups = {group.get("kbxGroupName", "_"):group.get("kbxGroupId") for group in results["groupList"]}
                for group in results["groupList"]:
                    if group.get("otherLocation") == True:
                        AppConstants.GROUP_ID_UNKNOWN_LOCATION = group.get("kbxGroupId")
                        break
                    
            return AppConstants.GROUP_ID_UNKNOWN_LOCATION

        except Exception as e:
            raise e