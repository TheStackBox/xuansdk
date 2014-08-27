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
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxTime import KBXTime
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.schedulerService import SchedulerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class TimerModule(Module):

    METHOD_ID_DAILY_TASK = None

    SCHEDULER_ID_TRACKER = set([])

    def __init__(self, kbxModuleName, kbxParentPath):
        super(TimerModule, self).__init__(kbxModuleName, kbxParentPath)


    def on_system_connected(self):
        EVENT_TAG = "AUTOMATION_TIMER_SERVICE"

        self.register_event(EVENT_TAG)

        self.register_shared_method(kbxMethodName="trigger_daily_task_scheduler",
                                    kbxMethodFunc=self.__trigger_daily_task_scheduler,
                                    kbxMethodIsPrivate=True)

        #=======================================================================
        # Register For Automation
        #=======================================================================
        timerGroupId = self.register_shared_method_group(kbxGroupName="timer",
                                                         kbxGroupParentId=AppConstants.GROUP_ID_SERVICE,
                                                         kbxGroupLabel=KBXLang("timer.groupLabel"),
                                                         kbxGroupDesc=KBXLang("timer.groupDesc"),
                                                         kbxGroupIcon="&#xe62b")

        TimerModule.METHOD_ID_DAILY_TASK = self.register_shared_method(kbxMethodName="daily_task",
                                                                       kbxMethodFunc=self.__daily_task,
                                                                       kbxMethodLabel=KBXLang("timer.dailyTask.label"),
                                                                       kbxMethodDesc=KBXLang("timer.dailyTask.desc"),
                                                                       kbxGroupId=timerGroupId,
                                                                       kbxMethodTag=AppConstants.TAG_CONDITION,
                                                                       kbxMethodEvent=EVENT_TAG,
                                                                       kbxMethodParams=[KBXTime(kbxParamName="time")])

    @staticmethod
    def add_daily_task_scheduler(ruleId, timeValue):
        try:
            ruleId = KBXString(kbxParamName="ruleId").cast(ruleId)

            dateTimeDTO = KBXTime(kbxParamName="time").cast(timeValue)
            dateTimeObj = dateTimeDTO.get_date_time_obj()

            hours = dateTimeObj.hour
            minutes = dateTimeObj.minute
            seconds = dateTimeObj.second

            schedulerName = "AUTO_TIMER_%s_%s_%s_%s" % (ruleId, str(hours), str(minutes), str(seconds))
            SchedulerService.add_cron_job(schedulerName,
                                          kbxTargetAppId=AppInfo.get_app_id(),
                                          kbxTargetMethod="trigger_daily_task_scheduler",
                                          kbxTargetModule="timer_module",
                                          second=str(seconds),
                                          minute=str(minutes),
                                          hour=str(minutes),
                                          store=False)

            TimerModule.SCHEDULER_ID_TRACKER.add(schedulerName)
            Logger.log_debug("Added Timer:", schedulerName)

        except Exception as e:
            Logger.log_debug(e)

    @staticmethod
    def delete_daily_task_scheduler(ruleId, timeValue):
        try:
            ruleId = KBXString(kbxParamName="ruleId").cast(ruleId)

            dateTimeDTO = KBXTime(kbxParamName="time").cast(timeValue)
            dateTimeObj = dateTimeDTO.get_date_time_obj()

            hours = dateTimeObj.hour
            minutes = dateTimeObj.minute
            seconds = dateTimeObj.second

            schedulerName = "AUTO_TIMER_%s_%s_%s_%s" % (ruleId, str(hours), str(minutes), str(seconds))

            if schedulerName in TimerModule.SCHEDULER_ID_TRACKER:
                SchedulerService.remove_job(schedulerName)
                TimerModule.SCHEDULER_ID_TRACKER.remove(schedulerName)
                Logger.log_debug("Removed Timer:", schedulerName)

        except Exception as e:
            Logger.log_debug(e)

    def __trigger_daily_task_scheduler(self, request):
        EVENT_TAG = "AUTOMATION_TIMER_SERVICE"
        self.send_response({}, request.requestId)
        self.send_system_event(EVENT_TAG, "{}")

    def __daily_task(self, request):
        try:
            dateTimeDTO = request.get_value("time")
            dateTimeObj = dateTimeDTO.get_date_time_obj()

            from datetime import datetime
            currentDateTimeObj = datetime.now()

            timeDelta = abs((currentDateTimeObj - dateTimeObj).total_seconds()) # IGNORE:maybe-no-member

            result = timeDelta < 59 # allows delta of 59 seconds

            self.send_response({AppConstants.KEY_CONDITION_RESPONSE:result}, request.requestId)
        except AutomationException as ae:
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
        except Exception as e:
            ae = AutomationException(1098, str(e))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
