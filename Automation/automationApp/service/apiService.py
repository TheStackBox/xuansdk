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
from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.dto.groupDTO import GroupDTO
from automationApp.dto.methodDTO import MethodDTO
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.util import Util


class APIService(object):

    def list_groups(self, language, section, parentId=None, limit=50, offset=0):
        try:
            parentId = AppConstants.GROUP_ID_AUTOMATION if parentId is None else parentId

            groupList, totalCount = SharedMethod.list_shared_method_groups(kbxGroupParentId=parentId, kbxMethodTag=section,
                                                                           limit=limit, offset=offset,
                                                                           enableTagCount=True, language=language)
            if section == AppConstants.TAG_CONDITION:
                appendTo = "_cond"
            elif section == AppConstants.TAG_ACTION:
                appendTo = "_exec"

            if parentId == AppConstants.GROUP_ID_AUTOMATION:
                #===================================================================
                # Overwrite level 1 group (devices parent group) descriptions.
                #===================================================================
                newGroupList = []


                for groupDict in groupList:
                    try:
                        groupDTO = GroupDTO(**groupDict)
                        desc = KBXLang(AppConstants.GROUP_DESC[groupDTO.get_group_name()] + appendTo)
                        groupDTO.set_group_desc(desc)
                        newGroupList.append(groupDTO)
                    except:
                        newGroupList.append(groupDict)

                groupList = newGroupList

                parentGroupDTO = None

            else:
                parentGroup = SharedMethod.get_shared_method_group_by_id(kbxGroupId=parentId, language=language)
                parentGroupDTO = GroupDTO(**parentGroup)
                desc = KBXLang(AppConstants.GROUP_DESC[parentGroupDTO.get_group_name()] + appendTo)
                parentGroupDTO.set_group_desc(desc)

            return parentGroupDTO, groupList, totalCount

        except AutomationException as e:
            Logger.log_debug(e.get_debug_message())
            raise e
        except Exception as e:
            Logger.log_debug(e)
            raise AutomationException(1096, "Unable to list groups from system app")

    def list_methods(self, language, section, groupId, limit=50, offset=0):
        try:
            methodList, totalCount = SharedMethod.list_shared_methods(kbxGroupId=groupId,
                                                                      kbxMethodTag=section,
                                                                      kbxMethodStatus=[SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE],
                                                                      limit=limit,
                                                                      offset=offset,
                                                                      language=language)

            #===================================================================
            # Get group information
            #===================================================================
            try:
                groupDict = SharedMethod.get_shared_method_group_by_id(kbxGroupId=groupId, language=language)
            except Exception as e:
                Logger.log_debug(e)
                raise AutomationException(1096, "Unable to list groups from system app")

            for index in range(0, len(methodList)):
                methodDTO = MethodDTO(**methodList[index])
                methodEvent = methodDTO.get_method_event()

                if isinstance(methodEvent, list):
                    hasEvent = len(methodEvent) > 0
                else:
                    hasEvent = not Util.is_empty(methodEvent)

                methodDTO.set_method_has_event(hasEvent)
                methodList[index] = methodDTO

            return methodList, totalCount, groupDict
        except AutomationException as e:
            Logger.log_debug(e.get_debug_message())
            raise e
        except Exception as e:
            # Mostly raised when getting result from System App
            Logger.log_debug("list_methods unexpected ex:", e)
            raise AutomationException(1096, "Unable to list methods from system app")


