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
import math
import threading

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.module.controllerModule import ControllerModule
from automationApp.utils.valueParser import ValueParser
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.service.schedulerService import SchedulerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class TriggerController:


    __INSTANCE = None
    __LOCK = threading.Lock()
    
    
    @staticmethod
    def instance():
        with TriggerController.__LOCK:
            TriggerController.__INSTANCE or TriggerController()
            return TriggerController.__INSTANCE

    def __init__(self):
        TriggerController.__INSTANCE = self
        
        self.__registeredRuleIds = set([])
        self.__threadPool = ThreadPoolExecutor(max_workers=1)
        
    def listen_to_trigger_callback(self, aFunc):
        '''
        aFunc:Function - Parameters (ruleId:Integer)
        '''
        ControllerModule.ON_TRIGGER_CALLBACK = aFunc
        
    def register_listener(self, ruleId, triggerDict):
        self.unregister_listener(ruleId)

        triggerType = triggerDict["type"]
        triggerParsedValue = triggerDict.get("parsedValue")
        
        #=======================================================================
        # Register trigger to scheduler
        #=======================================================================
        if triggerType == AppConstants.TRIGGER_TYPE_INTERVAL:

            def __signal_scheduler_add_interval_job(ruleId, seconds, minutes, hours):

                kwargs = {k:v for k, v in {"seconds":seconds, "minutes":minutes, "hours":hours}.items() if v > 0}

                try:
                    SchedulerService.add_interval_job(jobName=str(ruleId),
                                                      kbxTargetAppId=AppInfo.get_app_id(),
                                                      kbxTargetMethod="on_trigger_callback",
                                                      kbxTargetModule="controller_module",
                                                      kbxTargetParams={"ruleId":ruleId},
                                                      store=False,
                                                      **kwargs)

                    self.__registeredRuleIds.add(ruleId)

                except SystemException as e:
                    Logger.log_debug(e)

            self.__threadPool.submit(__signal_scheduler_add_interval_job, ruleId, **triggerParsedValue)

        elif triggerType == AppConstants.TRIGGER_TYPE_TIME:

            def __signal_scheduler_add_cron_job(ruleId, hour, minute):
                try:
                    SchedulerService.add_cron_job(jobName=str(ruleId),
                                                  kbxTargetAppId=AppInfo.get_app_id(),
                                                  kbxTargetMethod="on_trigger_callback",
                                                  kbxTargetModule="controller_module",
                                                  kbxTargetParams={"ruleId":ruleId},
                                                  store=False,
                                                  hour=str(hour),
                                                  minute=str(minute))

                    self.__registeredRuleIds.add(ruleId)

                except SystemException as e:
                    Logger.log_debug(e)

            self.__threadPool.submit(__signal_scheduler_add_cron_job, ruleId, **triggerParsedValue)

    def unregister_listener(self, ruleId):
        
        def __signal_scheduler_remove_task(ruleId):
            try:
                SchedulerService.remove_job(str(ruleId))
                self.__registeredRuleIds.remove(ruleId)
            except SystemException as e:
                Logger.log_debug(e)
                
        if ruleId in self.__registeredRuleIds:
            self.__threadPool.submit(__signal_scheduler_remove_task, ruleId)

    def parse_to_trigger_dto(self, trigger):
        #=======================================================================
        # Check if all required keys must exists
        #=======================================================================
        if "type" not in trigger:
            raise AutomationException(11703, "'type' must exists")

        #=======================================================================
        # Check 'type' against allowed values
        #=======================================================================
        triggerType = trigger["type"]
        if triggerType not in (AppConstants.TRIGGER_TYPE_EVENT, AppConstants.TRIGGER_TYPE_INTERVAL, AppConstants.TRIGGER_TYPE_TIME):
            raise AutomationException(11703, "'type' has invalid value")

        #=======================================================================
        # Compute 'parsedValue'
        #=======================================================================
        triggerValue = trigger.get("value")
        if triggerType == AppConstants.TRIGGER_TYPE_INTERVAL:
            triggerValue = ValueParser.get_number(triggerValue) # this must be an integer (seconds)
            if isinstance(triggerValue, int):
                if triggerValue > 0:
                    seconds = triggerValue % 60
                    minutes = math.floor(triggerValue / 60) % 60
                    hours = math.floor((triggerValue / 3600)) % 24

                    trigger["parsedValue"] = {"seconds":seconds, "minutes":minutes, "hours":hours}

                else:
                    raise AutomationException(11703, "'value' in 'trigger' must be larger than 0")
            else:
                raise AutomationException(11703, "'value' in 'trigger' must be a number in seconds")

        elif triggerType == AppConstants.TRIGGER_TYPE_TIME:
            triggerValue = ValueParser.get_string(triggerValue) # this must be in (HH, MM)
            if isinstance(triggerValue, str):
                triggerValue = triggerValue.split(":")

                if len(triggerValue) == 2:
                    #=======================================================
                    # Validate hour
                    #=======================================================
                    hour = ValueParser.get_number(triggerValue[0])

                    if hour is None or not 0 <= hour <= 23:
                        raise AutomationException(11703, "'HH is ranged from 00 - 23'")

                    #=======================================================
                    # Validate minute
                    #=======================================================
                    minute = ValueParser.get_number(triggerValue[1])

                    if minute is None or not 0 <= minute <= 59:
                        raise AutomationException(11703, "MM is ranged from 00 - 59")

                    trigger["parsedValue"] = {"hour":hour, "minute":minute}

                else:
                    raise AutomationException(11703, "'value' in 'trigger' must be in HH:MM format")
            else:
                raise AutomationException(11703, "'value' in 'trigger' must be string in HH:MM format")
        
        else:
            trigger["parsedValue"] = None

        return trigger


