##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo

class SharedMethod(object):
    
    ''' Currently callable shared method'''
    METHOD_STATUS_ACTIVE = SharedMethodManagerService.METHOD_STATUS_ACTIVE
    ''' Shared method which is registered but not callable currently '''
    METHOD_STATUS_INACTIVE = SharedMethodManagerService.METHOD_STATUS_INACTIVE

    __unset__ = []
    
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
        A dictionary of target method's corresponsing response.
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
        A dictionary of target method's corresponsive response.
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
    def list_shared_methods(kbxMethodId=__unset__, kbxMethodAppId=__unset__, kbxModuleName=__unset__, kbxMethodName=__unset__,
                            kbxGroupId=__unset__, kbxMethodTag=__unset__, kbxMethodStatus=METHOD_STATUS_ACTIVE, limit=50, offset=0,
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
        A tuple constains of a list of method properties (dictionaries) and total number of records.
        '''
        pass

    @staticmethod
    def get_shared_methods_count(kbxMethodId=__unset__, kbxMethodAppId=__unset__, kbxModuleName=__unset__, kbxMethodName=__unset__,
                            kbxGroupId=__unset__, kbxMethodTag=__unset__, kbxMethodStatus=METHOD_STATUS_ACTIVE, language=AppInfo.DEFAULT_API_LANGUAGE):
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
        An integer of total records count.
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
    def list_shared_method_groups(kbxGroupId=__unset__, kbxGroupAppId=__unset__, kbxGroupName=__unset__,
                                  kbxGroupParentId=__unset__, kbxMethodTag=__unset__, enableTagCount=False, limit=50, offset=0, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve list of registered shared methods based on given criteria.

        Params:
        kbxGroupId:List<Integer> - [Optional] Filter based on group ids.
        kbxGroupAppId:List<Integer> - [Optional] Filter based on app ids that registered the groups.
        kbxGroupName:List<String> - [Optional] Filter based on group names.
        kbxGroupParentId:List<String> - [Optional] Filter based on group parent ids. For groups that does not have a parent id, use None.
        limit:Integer - Maximum number of records per retrieve. 50 by default.
        offset:Integer - Starting index of the list of records. 0 by default.
        language:String - [Optional] Preferred language.

        Returns:
        A tuple constains of a list of group properties (dictionaries) and total number of records.
        '''
        pass
