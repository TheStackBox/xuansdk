##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from collections import deque
import json
from threading import Event
import traceback

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.ipcClient import IPCClient
from com.cloudMedia.theKuroBox.sdk.ex.appException import AppException
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger
from com.cloudMedia.theKuroBox.sdk.util.methodCallGroup import MethodCallGroup
from com.cloudMedia.theKuroBox.sdk.util.validator.booleanValidator import BooleanValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.numberValidator import NumberValidator
from com.cloudMedia.theKuroBox.sdk.util.validator.stringValidator import StringValidator

from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang

class SharedMethod(object):
    '''
    Shared Method.
    '''

    ''' Currently callable shared method '''
    METHOD_STATUS_ACTIVE = 1
    ''' Shared method which is registered but not callable currently '''
    METHOD_STATUS_INACTIVE = 0

    __empty_placeholder = {} # KEEP_FOR_SDK

    @staticmethod
    def get_empty_placeholder():
        pass

    @staticmethod
    def get_system_id():
        '''
        Get system unique app id.

        Returns:
        An integer of system unique app id.
        '''
        pass

    @staticmethod
    def get_pyapi():
        '''
        Get System python api version
        '''
        pass

    @staticmethod
    def call(kbxMethodName, kbxMethodAppId=None, kbxModuleName=None, kbxGroupId=None, **kwargs):
        '''
        Invoke external app's registered method using Inter-process Communication (IPC) protocol.

        Params:
        kbxMethodName:String - [Required] Target method's name.
        kbxMethodAppId:Integer - [Optional] Unique app id of target method. It's system app id by default.
        kbxModuleName:String - [Optional] Targeted method's module name. It's empty by default.
        kbxGroupId:Integer - [Optional] Method group id of targeted method. It's empty by default.
        **kwargs - Any extra key value pairs will be passed as arguments when calling the targeted method. They must be able to be converted into json string altogether.

        Returns:
        A dictionary of target method's corresponding response.
        '''
        pass

    @staticmethod
    def call_by_method_id(kbxMethodId, **kwargs):
        '''
        Similar functionality to "call" method except registered methods' unique ids is used instead of their properties.

        Params:
        kbxMethodId:Integer - [Required] Unique method id of targeted method.
        **kwargs - Any extra key value pairs will be passed as arguments when calling the targeted method. They must be able to be converted into json string altogether.

        Returns:
        A dictionary of target method's corresponding response.
        '''
        pass

    @staticmethod
    def get_shared_method(kbxMethodName, kbxMethodAppId, kbxModuleName=None, kbxGroupId=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get a publicly shared method. SystemException raised if no shared method match the criteria.

        Params:
        kbxMethodName:String - [Required] Name of the method.
        kbxMethodAppId:Integer - [Required] Unique app id of the app that registered the method.
        kbxModuleName:String - [Optional] Name of the module which holds the method.
        kbxGroupId:Integer [Optional] Group id of the method if any.

        Returns:
        An object contains of the shared method's information.
        '''
        pass

    @staticmethod
    def get_shared_method_by_id(kbxMethodId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get a publicly shared method by their unique id. SystemException raised if no shared method with that id does not exists.

        Params:
        kbxMethodId:Number - [Required] Unique of the method.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary contains of the shared method's information.
        '''
        pass

    @staticmethod
    def list_shared_methods(kbxMethodId=__empty_placeholder, kbxMethodAppId=__empty_placeholder, kbxModuleName=__empty_placeholder, kbxMethodName=__empty_placeholder,
                            kbxGroupId=__empty_placeholder, kbxMethodTag=__empty_placeholder, kbxMethodStatus=METHOD_STATUS_ACTIVE, limit=50, offset=0,
                            language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve list of registered shared methods based on given criteria.

        Params:
        kbxMethodId:List<Integer> - [Optional] Filter based on unique method ids .
        kbxMethodAppId:List<Integer> - [Optional] Filter based on app ids that registered the methods.
        kbxModuleName:List<String> - [Optional] Filter based on names of the modules.
        kbxMethodName:List<String> - [Optional] Filter based on names of the methods.
        kbxGroupId:List<Integer> - [Optional] Filter based on method group ids.
        kbxMethodTag:List<String> - [Optional] Filter based on method tags.
        kbxMethodStatus:List<Integer> - [Optional] Filter based on method status. Available options are "SharedMethod.METHOD_STATUS_ON" and "SharedMethod.METHOD_STATUS_OFF"
        limit:Integer - [Optional] Maximum number of records per retrieve. 50 by default.
        offset:Integer - [Optional] Starting index of the list of records. 0 by default.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary contains of a list of method properties [methodList] and total number of records [totalItem].
        '''
        pass

    @staticmethod
    def get_shared_methods_count(kbxMethodId=__empty_placeholder, kbxMethodAppId=__empty_placeholder, kbxModuleName=__empty_placeholder, kbxMethodName=__empty_placeholder,
                            kbxGroupId=__empty_placeholder, kbxMethodTag=__empty_placeholder, kbxMethodStatus=METHOD_STATUS_ACTIVE, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get total count of registered shared methods which matched given criteria.

        Params:
        kbxMethodId:List<Integer> - [Optional] Filter based on unique method ids .
        kbxMethodAppId:List<Integer> - [Optional] Filter based on app ids that registered the methods.
        kbxModuleName:List<String> - [Optional] Filter based on names of the modules.
        kbxMethodName:List<String> - [Optional] Filter based on names of the methods.
        kbxGroupId:List<Integer> - [Optional] Filter based on method group ids.
        kbxMethodTag:List<String> - [Optional] Filter based on method tags.
        kbxMethodStatus:List<Integer> - [Optional] Filter based on method status. Available options are "SharedMethod.METHOD_STATUS_ON" and "SharedMethod.METHOD_STATUS_OFF"
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary contains of total records count [totalItem].
        '''
        pass

    @staticmethod
    def list_shared_methods_by_app_id(kbxMethodAppId, kbxMethodIds, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List method configuration of given method unique IDs. 
        This is a faster approach compared to "list_shared_methods" because you know the unique app IDs of the methods.

        Params:
        kbxMethodAppId:Integer - [Required] Unique app ID which registered the methods.
        kbxMethodIds:List<Integer> - [Required] List of unique method IDs.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary which contains of methodId-methodObject pairs.
        eg. 
        {57: {'kbxMethodTag': ['sample_method_tag'], 
              'kbxMethodDesc': 'Method Description',
              'kbxMethodStatus': 1,
              'kbxMethodLabel': 'Method Label',
            'kbxMethodName': 'method_identifier',
              'kbxMethodParams': [{'kbxParamLabel': None,
                                   'kbxParamName': 'param1',
                                   'kbxParamDefaultValue': 'defaultValue', 
                                   'kbxParamMaxLength': None, 
                                   'kbxParamType': 'kbxString', 
                                   'kbxParamDesc': None, 
                                   'kbxParamIsRequired': True, 
                                   'kbxParamMinLength': None, 
                                   'kbxParamCom': 'kbxHidden'}], 
              'kbxModuleName': 'sample_module', 
              'kbxGroupId': None, 
              'kbxMethodIsPrivate': False}} 
        
        * For ID which is not registered under that app, it returns None.
        eg.
        {24: None}
        '''
        pass

    @staticmethod
    def get_shared_method_group(kbxGroupName, kbxGroupAppId, kbxGroupParentId=None, enableTagCount=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get shared method group. SystemException raised if no shared method group found matching the criteria.

        Params:
        kbxGroupName:String - [Required] Name of the group.
        kbxGroupAppId:Number - [Required] Unique app id of the app that registered the group.
        kbxGroupParentId:Number - [Optional] Unique group id of the parent group if any.
        enableTagCount:Boolean - [Optional] If enabled then return info will contains count of each unique tags for all methods registered under this group.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary contains of the shared method group's information
        '''
        pass

    @staticmethod
    def get_shared_method_group_by_id(kbxGroupId, enableTagCount=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get shared method group by unique group id. SystemException raised if no shared method group registered as the id

        Params:
        kbxGroupId:Number - [Required] Unique group id.
        enableTagCount:Boolean - [Optional] If enabled then return info will contains count of each unique tags for all methods registered under this group.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary contains of the shared method group's information
        '''
        pass

    @staticmethod
    def list_shared_method_groups(kbxGroupId=__empty_placeholder, kbxGroupAppId=__empty_placeholder, kbxGroupName=__empty_placeholder,
                                  kbxGroupParentId=__empty_placeholder, kbxMethodTag=__empty_placeholder, enableTagCount=False, limit=50, offset=0, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve list of registered shared methods based on given criteria.

        Params:
        kbxGroupId:List<Integer> - [Optional] Filter based on group ids.
        kbxGroupAppId:List<Integer> - [Optional] Filter based on app ids that registered the groups.
        kbxGroupName:List<String> - [Optional] Filter based on group names.
        kbxGroupParentId:List<String> - [Optional] Filter based on group parent ids. For groups that does not have a parent id, use None.
        limit:Integer - Maximum number of records per retrieve. 50 by default.
        offset:Integer - Starting index of the list of records. 0 by default.

        Returns:
        A dictionary contains of a list of group properties [groupList] and total number of records [totalItem].
        '''
        pass

    @staticmethod
    def list_shared_method_groups_by_app_id(kbxGroupAppId, kbxGroupIds, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List group configuration of given group unique IDs. 
        This is a faster approach compared to "list_shared_methods" because you know the unique app IDs of the methods.

        Params:
        kbxGroupAppId:Integer - [Required] Unique app ID which registered the groups.
        kbxGroupIds:List<Integer> - [Required] List of unique group IDs.
        language:String - [Optional] Preferred language.

        Returns:
        A dictionary which contains of groupId-groupObject pairs.
        eg. 
        {23: {'kbxGroupDesc': 'Group ABC description', 
              'kbxGroupName': 'group_abc', 
              'kbxGroupParentId': 2, 
              'kbxGroupLabel': 'Group ABC'}}
        
        * For ID which is not registered under that app, it returns None.
        eg.
        {24: None}
        '''
        pass

