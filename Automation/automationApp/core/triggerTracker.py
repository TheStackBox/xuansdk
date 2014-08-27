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
import math

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from automationApp.dto.triggerDTO import TriggerDTO
from automationApp.utils.valueParser import ValueParser
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.service.schedulerService import SchedulerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class TriggerTracker(object):

    def __init__(self):
        self.__registeredRuleIds = set([])
        try:
            SchedulerService.remove_all_jobs()
        except:
            pass

    def register_listener(self, ruleId, triggerDTO):
        if not isinstance(ruleId, str):
            return

        self.unregister_listener(ruleId)

        triggerType = triggerDTO.get_type()
        triggerParsedValue = triggerDTO.get_parsed_value()

        #=======================================================================
        # Register trigger to scheduler
        #=======================================================================
        if triggerType == TriggerDTO.TYPE_INTERVAL:

            def __signal_scheduler_add_interval_job(ruleId, seconds, minutes, hours):

                kwargs = {k:v for k, v in {"seconds":seconds, "minutes":minutes, "hours":hours}.items() if v > 0}

                try:
                    SchedulerService.add_interval_job(jobName=ruleId,
                                                      kbxTargetAppId=AppInfo.get_app_id(),
                                                      kbxTargetMethod="automation_timer_callback",
                                                      kbxTargetParams={"ruleId":ruleId},
                                                      store=False,
                                                      **kwargs)

                    self.__registeredRuleIds.add(ruleId)

                except SystemException as e:
                    Logger.log_debug(e)

            AppConstants.get_thread_pool_executor().submit(__signal_scheduler_add_interval_job, ruleId, **triggerParsedValue)

        elif triggerType == TriggerDTO.TYPE_TIME:

            def __signal_scheduler_add_cron_job(ruleId, hour, minute):
                try:
                    SchedulerService.add_cron_job(jobName=ruleId,
                                                  kbxTargetAppId=AppInfo.get_app_id(),
                                                  kbxTargetMethod="automation_timer_callback",
                                                  kbxTargetParams={"ruleId":ruleId},
                                                  store=False,
                                                  hour=str(hour),
                                                  minute=str(minute))

                    self.__registeredRuleIds.add(ruleId)

                except SystemException as e:
                    Logger.log_debug(e)

            AppConstants.get_thread_pool_executor().submit(__signal_scheduler_add_cron_job, ruleId, **triggerParsedValue)

    def unregister_listener(self, ruleId):
        def __signal_scheduler_remove_task(ruleId):
            try:
                SchedulerService.remove_job(ruleId)
                self.__registeredRuleIds.remove(ruleId)
            except SystemException as e:
                Logger.log_debug(e)
        if ruleId in self.__registeredRuleIds:
            AppConstants.get_thread_pool_executor().submit(__signal_scheduler_remove_task, ruleId)

    def parse_to_trigger_dto(self, triggerObject):
        #=======================================================================
        # Check if all required keys must exists
        #=======================================================================
        if TriggerDTO.PROP_TYPE not in triggerObject:
            raise AutomationException(1703, "'type' must exists")

        triggerDTO = TriggerDTO(**triggerObject)

        #=======================================================================
        # Check 'type' against allowed values
        #=======================================================================
        triggerType = triggerDTO.get_type()
        if triggerType not in (TriggerDTO.TYPE_EVENT, TriggerDTO.TYPE_INTERVAL, TriggerDTO.TYPE_TIME):
            raise AutomationException(1703, "'type' has invalid value")

        #=======================================================================
        # Compute 'parsedValue'
        #=======================================================================
        triggerValue = triggerDTO.get_value()
        if triggerType == TriggerDTO.TYPE_INTERVAL:
            triggerValue = ValueParser.get_number(triggerValue) # this must be an integer (seconds)
            if isinstance(triggerValue, int):
                if triggerValue > 0:
                    seconds = triggerValue % 60
                    minutes = math.floor(triggerValue / 60) % 60
                    hours = math.floor((triggerValue / 3600)) % 24

                    triggerDTO.set_parsed_value({"seconds":seconds, "minutes":minutes, "hours":hours})

                else:
                    raise AutomationException(1703, "'value' in 'trigger' must be larger than 0")
            else:
                raise AutomationException(1703, "'value' in 'trigger' must be a number in seconds")

        elif triggerType == TriggerDTO.TYPE_TIME:
            triggerValue = ValueParser.get_string(triggerValue) # this must be in (HH, MM)
            if isinstance(triggerValue, str):
                triggerValue = triggerValue.split(":")

                if len(triggerValue) == 2:
                    #=======================================================
                    # Validate hour
                    #=======================================================
                    hour = ValueParser.get_number(triggerValue[0])

                    if hour is None or not 0 <= hour <= 23:
                        raise AutomationException(1703, "'HH is ranged from 00 - 23'")

                    #=======================================================
                    # Validate minute
                    #=======================================================
                    minute = ValueParser.get_number(triggerValue[1])

                    if minute is None or not 0 <= minute <= 59:
                        raise AutomationException(1703, "MM is ranged from 00 - 59")

                    triggerDTO.set_parsed_value({"hour":hour, "minute":minute})

                else:
                    raise AutomationException(1703, "'value' in 'trigger' must be in HH:MM format")
            else:
                raise AutomationException(1703, "'value' in 'trigger' must be string in HH:MM format")

        return triggerDTO


