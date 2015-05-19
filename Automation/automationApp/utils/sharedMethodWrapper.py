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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxTime import KBXTime
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber


class SharedMethodWrapper:
    '''
    Wrap sdk/app/SharedMethod.py for additional features used only in Automation app.
    '''
    
    
    PRIVATE_GROUPS = {-291: {"kbxGroupId":-291,
                             "kbxGroupParentId":None,
                             "kbxGroupName":"delay",
                             "kbxGroupLabel":KBXLang("group_-291_label"),
                             "kbxGroupDesc":"",
                             "kbxGroupIcon":"&#xe62b"},
                      -292: {"kbxGroupId":-292,
                             "kbxGroupParentId":None,
                             "kbxGroupName":"condition",
                             "kbxGroupLabel":"condition",
                             "kbxGroupDesc":"",
                             "kbxGroupIcon":"C"}}
    
    PRIVATE_METHODS = {-291: {"kbxMethodId":-291,
                              "kbxMethodName":"delay",
                              "kbxModuleName":None,
                              "kbxGroupId":-291,
                              "kbxMethodLabel":KBXLang("method_-291_label"),
                              "kbxMethodStatus":1,
                              "kbxMethodAppId":2000300,
                              "kbxMethodParams":[KBXTime(kbxParamName="delayInSec").get_properties()]},
                       -292: {"kbxMethodId":-292,
                              "kbxMethodName":"condition",
                              "kbxModuleName":None,
                              "kbxGroupId":-292,
                              "kbxMethodLabel":None,
                              "kbxMethodStatus":1,
                              "kbxMethodAppId":2000300,
                              "kbxMethodParams":[KBXNumber(kbxParamName="condId").get_properties()]}}
    
    @staticmethod
    def list_shared_method_groups(kbxGroupId, language=AppInfo.DEFAULT_API_LANGUAGE, limit=100, **kwargs):
        '''
        limit - This will be override no matter what. Do not pass any argument for it.
        '''
        KBXLang.set_preferred_lang(language)
        
        kbxGroupIds = set(kbxGroupId)
        publicGroupIds, privateGroupIds = [gId for gId in kbxGroupIds if gId > 0], (gId for gId in kbxGroupIds if gId < 0)
        finalGroupList = deque()
        
        publicGroupIdsLen = len(publicGroupIds)
        if publicGroupIdsLen > 0:
            result = SharedMethod.list_shared_method_groups(kbxGroupId=publicGroupIds, 
                                                            limit=publicGroupIdsLen, 
                                                            language=language, 
                                                            **kwargs)
            finalGroupList.extend(result["groupList"])

        for privateGroupId in privateGroupIds:
            privateGroup = SharedMethodWrapper.PRIVATE_GROUPS.get(privateGroupId)
            if privateGroup is not None:
                privateGroup["kbxGroupLabel"] = str(privateGroup["kbxGroupLabel"])
                finalGroupList.append(privateGroup)
                
        return finalGroupList
        
    @staticmethod
    def list_shared_methods(kbxMethodId, language=AppInfo.DEFAULT_API_LANGUAGE, limit=100, **kwargs):
        '''
        limit - This will be override no matter what. Do not pass any argument for it.
        '''
        KBXLang.set_preferred_lang(language)
        
        kbxMethodIds = set(kbxMethodId)
        publicMethodIds, privateMethodIds = [mId for mId in kbxMethodIds if mId > 0], (mId for mId in kbxMethodIds if mId < 0)
        finalMethodList = deque()
        
        publicMethodIdsLen = len(publicMethodIds)
        if publicMethodIdsLen > 0:
            result = SharedMethod.list_shared_methods(kbxMethodId=publicMethodIds, 
                                                      limit=publicMethodIdsLen, 
                                                      language=language, 
                                                      **kwargs)
            finalMethodList.extend(result["methodList"])

        for privateMethodId in privateMethodIds:
            privateMethod = SharedMethodWrapper.PRIVATE_METHODS.get(privateMethodId)
            if privateMethod is not None:
                privateMethod["kbxMethodLabel"] = str(privateMethod["kbxMethodLabel"])
                finalMethodList.append(privateMethod)
                
        return finalMethodList
    
    @staticmethod
    def list_shared_methods_by_app_id(kbxMethodAppId, kbxMethodIds, language=AppInfo.DEFAULT_API_LANGUAGE):
        KBXLang.set_preferred_lang(language)
        
        kbxMethodIds = set(kbxMethodIds)
        publicMethodIds, privateMethodIds = [mId for mId in kbxMethodIds if mId > 0], (mId for mId in kbxMethodIds if mId < 0)
        finalMethodDict = {}
        
        publicMethodIdsLen = len(publicMethodIds)
        if publicMethodIdsLen > 0:
            result = SharedMethod.list_shared_methods_by_app_id(kbxMethodAppId=kbxMethodAppId, 
                                                                kbxMethodIds=publicMethodIds, 
                                                                language=language)
            finalMethodDict.update(result)

        for privateMethodId in privateMethodIds:
            privateMethod = SharedMethodWrapper.PRIVATE_METHODS.get(privateMethodId)
            if privateMethod is not None:
                privateMethod["kbxMethodLabel"] = str(privateMethod["kbxMethodLabel"])
                finalMethodDict[privateMethodId] = privateMethod
            else:
                finalMethodDict[privateMethodId] = None
                
        return finalMethodDict
    
    @staticmethod
    def get_shared_method_group_by_id(kbxGroupId, enableTagCount=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        KBXLang.set_preferred_lang(language)
        
        if kbxGroupId < 0:
            privateGroup = SharedMethodWrapper.PRIVATE_GROUPS[kbxGroupId]
            if privateGroup is not None:
                privateGroup["kbxGroupLabel"] = str(privateGroup["kbxGroupLabel"])
                return privateGroup
            
        return SharedMethod.get_shared_method_group_by_id(kbxGroupId, enableTagCount, language)
    
    @staticmethod
    def get_shared_method_by_id(kbxMethodId, language=AppInfo.DEFAULT_API_LANGUAGE):
        KBXLang.set_preferred_lang(language)
        
        if kbxMethodId < 0:
            privateMethod = SharedMethodWrapper.PRIVATE_METHODS[kbxMethodId]
            if privateMethod is not None:
                privateMethod["kbxMethodLabel"] = str(privateMethod["kbxMethodLabel"])
                return privateMethod
            
        return SharedMethod.get_shared_method_by_id(kbxMethodId, language)
    
    
    
    