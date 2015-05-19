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

from automationApp.core.database import Database
from automationApp.core.eventController import EventController
from automationApp.core.groupController import GroupController
from automationApp.core.methodController import MethodController
from automationApp.core.triggerController import TriggerController
from automationApp.module.timerModule import TimerModule
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class BootstrapService:
    '''
    Automation Bootstrap. 
    Basically it do the following stuffs:
    - Update kbx_method
    - Update kbx_group
    - Register event listeners based on methods in kbx_method.
    - Register scheduler callbacks for triggers in rules.
    - Register timer module entries.
    '''
    
    
    def __init__(self):
        self.__db = Database.instance()
        self.__groupController = GroupController.instance()
        self.__eventController = EventController.instance()
        self.__triggerController = TriggerController.instance()
        self.__methodController = MethodController.instance()
        
    def update_kbx_method(self):
        '''
        Update information of kbxMethod.
        Add and remove group ID if kbxGroupId is updated.
        Add listener if necessary.
        '''
        result = self.__db.execute_and_fetch_all('SELECT "kbxMethodId" FROM "kbx_method" WHERE "kbxMethodId" > 0')
        
        if len(result) == 0:
            return
        
        kbxMethodIds = set([])
        
        for row in result:
            kbxMethodId = row["kbxMethodId"]
            kbxMethodIds.add(kbxMethodId)
        
        result = SharedMethod.list_shared_methods(kbxMethodId=list(kbxMethodIds), 
                                                  kbxMethodStatus=[SharedMethod.METHOD_STATUS_ACTIVE, SharedMethod.METHOD_STATUS_INACTIVE], 
                                                  limit=len(kbxMethodIds))
        kbxMethods = result["methodList"]
        for kbxMethod in kbxMethods:
            # Variables
            kbxMethodId = kbxMethod["kbxMethodId"]
            
            kbxMethodIds.remove(kbxMethodId) # For each kbxMethod which has result when listing from system, pop it out from kbxMethodsFromDB
            self.__methodController.update(kbxMethod)
            
        # The kbxMethodIds left here are all removed methods.
        for kbxMethodId in kbxMethodIds:
            self.__methodController.delete(kbxMethodId)
                
    def update_kbx_group(self):
        '''
        Updates information where necessary only.
        '''
        result = self.__db.execute_and_fetch_all('SELECT "kbxGroupId" FROM "kbx_group" WHERE "kbxGroupId" > 0')
        
        if len(result) == 0:
            return
        
        kbxGroupIds = set([])
        
        for row in result:
            kbxGroupId = row["kbxGroupId"]
            kbxGroupIds.add(kbxGroupId)
            
        result = SharedMethod.list_shared_method_groups(kbxGroupId=list(kbxGroupIds), enableTagCount=False, limit=len(kbxGroupIds))
        kbxGroups = result["groupList"]
        
        for kbxGroup in kbxGroups:
            # Variables
            kbxGroupId = kbxGroup["kbxGroupId"]
            
            kbxGroupIds.remove(kbxGroupId)
            self.__groupController.update(kbxGroup)
    
        for kbxGroupId in kbxGroupIds:
            self.__groupController.delete(kbxGroupId)
    
    def register_trigger_schedulers(self):
        result = self.__db.execute_and_fetch_all('SELECT "ruleId", "trigger" FROM "rule"')
        for row in result:
            self.__triggerController.register_listener(row["ruleId"], row["trigger"])
    
    def register_timer_module_schedulers(self):
        # TODO: REMEMBER TO ADD index to kbxMethodId
        timerModuleHnds = {TimerModule.METHOD_ID_DATE_TIME_RANGE: TimerModule.handle_date_time_range,
                           TimerModule.METHOD_ID_TIME_RANGE: TimerModule.handle_time_range,
                           TimerModule.METHOD_ID_DAY_OF_WEEK: TimerModule.handle_dow}
        
        timerMethodIds = (TimerModule.METHOD_ID_DATE_TIME_RANGE, TimerModule.METHOD_ID_TIME_RANGE, TimerModule.METHOD_ID_DAY_OF_WEEK)
        result = self.__db.execute_and_fetch_all('SELECT "rcRuleId", "kbxMethodId", "kbxMethodParams" FROM "rule_condition" WHERE "kbxMethodId" IN (?, ?, ?)',
                                                 timerMethodIds)
        
        for row in result:
            try:
                timerModuleHnd = timerModuleHnds[row["kbxMethodId"]]
                timerModuleHnd(row["rcRuleId"], row["kbxMethodParams"])
            except Exception as e:
                Logger.log_warning("BootstrapService.register_timer_module_schedulers ex:", e, "-- debug info --", dict(row))
                
    def commit(self):
        self.__db.commit()
        
    def rollback(self):
        self.__db.rollback()
        
        