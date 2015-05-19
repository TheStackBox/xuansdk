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

import datetime
import threading

from automationApp.appConstants import AppConstants
from automationApp.automationException import AutomationException
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxDateTimeRange import KBXDateTimeRange
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxDayOfWeek import KBXDayOfWeek
from com.cloudMedia.theKuroBox.sdk.paramComponents.kbxTimeRange import KBXTimeRange
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxTime import KBXTime
from com.cloudMedia.theKuroBox.sdk.service.schedulerService import SchedulerService
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class TimerModule(Module):


    METHOD_ID_DATE_TIME_RANGE = None
    METHOD_ID_TIME_RANGE = None
    METHOD_ID_DAY_OF_WEEK = None

    SCHEDULER_ID_TRACKER = {}
    RULE_ID_SCHEDULER_TRACKER = {}
    SCHEDULER_LOCK = threading.Lock()

    EVENT_TAG = "AUTOMATION_TIMER_SERVICE"
    
    _PARAM_DT_RANGE = KBXDateTimeRange(kbxParamName="date_time_range")
    _PARAM_TIME_RANGE = KBXTimeRange(kbxParamName="time_range")
    _PARAM_DOW = KBXDayOfWeek(kbxParamName="day_of_week")


    @staticmethod
    def reset():
        TimerModule.METHOD_ID_DATE_TIME_RANGE = None
        TimerModule.METHOD_ID_TIME_RANGE = None
        TimerModule.METHOD_ID_DAY_OF_WEEK = None
    
        TimerModule.SCHEDULER_ID_TRACKER = {}
        TimerModule.RULE_ID_SCHEDULER_TRACKER = {}
        TimerModule.SCHEDULER_LOCK = threading.Lock()


    def __init__(self, kbxModuleName, kbxParentPath):
        super(TimerModule, self).__init__(kbxModuleName, kbxParentPath)
        
        self.register_method(kbxMethodName="list_scheduler",
                             kbxMethodFunc=self.__list_scheduler, 
                             kbxMethodIsPrivate=True)
        
    def __list_scheduler(self, request):
        try:
            jobs = SchedulerService.list_all_jobs()
            self.send_response({"jobs":jobs}, request.requestId)
        except Exception as e:
            self.send_response({"error":str(e)}, request.requestId)

    def on_system_connected(self):
        super().on_system_connected()
        
        self.register_event(TimerModule.EVENT_TAG)

        self.register_shared_method(kbxMethodName="scheduler_callback",
                                    kbxMethodFunc=self.__scheduler_callback,
                                    kbxMethodIsPrivate=True)
        
        #=======================================================================
        # Register For Automation
        #=======================================================================
        timerGroupId = self.register_shared_method_group(kbxGroupName="timer",
                                                         kbxGroupParentId=AppConstants.GROUP_ID_SERVICE,
                                                         kbxGroupLabel=KBXLang("timer.groupLabel"),
                                                         kbxGroupDesc=KBXLang("timer.groupDesc"),
                                                         kbxGroupIcon="&#xe62b")
        
        TimerModule.METHOD_ID_DATE_TIME_RANGE = self.register_shared_method(kbxMethodName="date_time_range",
                                                                            kbxMethodFunc=self.__date_time_range,
                                                                            kbxMethodLabel=KBXLang("timer.date_time_range.label"),
                                                                            kbxMethodDesc=KBXLang("timer.date_time_range.desc"),
                                                                            kbxGroupId=timerGroupId,
                                                                            kbxMethodTag=AppConstants.TAG_CONDITION,
                                                                            kbxMethodEvent=TimerModule.EVENT_TAG,
                                                                            kbxMethodIdentifier="date_time_range",
                                                                            kbxMethodParams=[TimerModule._PARAM_DT_RANGE])
        
        # backward compatible to daily_task
        TimerModule.METHOD_ID_TIME_RANGE = self.register_shared_method(kbxMethodName="daily_task",
                                                                       kbxMethodFunc=self.__time_range,
                                                                       kbxMethodLabel=KBXLang("timer.time_range.label"),
                                                                       kbxMethodDesc=KBXLang("timer.time_range.desc"),
                                                                       kbxGroupId=timerGroupId,
                                                                       kbxMethodTag=AppConstants.TAG_CONDITION,
                                                                       kbxMethodEvent=TimerModule.EVENT_TAG,
                                                                       kbxMethodIdentifier="time_range",
                                                                       kbxMethodParams=[TimerModule._PARAM_TIME_RANGE])
        
        TimerModule.METHOD_ID_DAY_OF_WEEK = self.register_shared_method(kbxMethodName="day_of_week", 
                                                                        kbxMethodFunc=self.__day_of_week,
                                                                        kbxMethodLabel=KBXLang("timer.day_of_week.label"),
                                                                        kbxMethodDesc=KBXLang("timer.day_of_week.desc"),
                                                                        kbxGroupId=timerGroupId,
                                                                        kbxMethodTag=AppConstants.TAG_CONDITION,
                                                                        kbxMethodEvent=TimerModule.EVENT_TAG, 
                                                                        kbxMethodIdentifier="day_of_week",
                                                                        kbxMethodParams=[TimerModule._PARAM_DOW])
    
    @staticmethod
    def handle_date_time_range(ruleId, methodParams):
        with TimerModule.SCHEDULER_LOCK:
            keyName = TimerModule._PARAM_DT_RANGE.get_kbx_param_name()
            dtVal = TimerModule.__get_arg(keyName, methodParams)
            try:
                dtVal = TimerModule._PARAM_DT_RANGE.cast(dtVal)
            except Exception as e:
                Logger.log_warning("Invalid date time range value, val:", dtVal, "ex:", e)
                return
            
            # Add scheduler
            startDateTime = dtVal.get_start_date_time()
            dtObj = startDateTime.get_date_time_obj()
            weekday = dtObj.isoweekday() % 7
            TimerModule.__add_scheduler(ruleId, "date_time_range", str(dtObj.second), str(dtObj.minute), str(dtObj.hour), str(dtObj.day), str(dtObj.month), str(weekday))
        
    @staticmethod
    def handle_time_range(ruleId, methodParams):
        with TimerModule.SCHEDULER_LOCK:
            keyName = TimerModule._PARAM_TIME_RANGE.get_kbx_param_name()
            tVal = TimerModule.__get_arg(keyName, methodParams)
            
            if tVal is not None:
                try:
                    tVal = TimerModule._PARAM_TIME_RANGE.cast(tVal)
                    startTime = tVal.get_start_time()
                except Exception as e:
                    Logger.log_warning("Invalid time range value, val:", tVal, "ex:", e)
                    return
            else:
                # Backward compatible to daily_task.
                kbxTime = KBXTime(kbxParamName="time")
                try:
                    startTime = kbxTime.cast(TimerModule.__get_arg("time", methodParams))
                except Exception as e:
                    Logger.log_warning("Invalid time range value (old), val:", tVal, "ex:", e)
                    return
            
            # Add scheduler
            TimerModule.__add_scheduler(ruleId, "time_range", str(startTime.get_second()), str(startTime.get_minute()), str(startTime.get_hour()), "*", "*", "*")
    
    @staticmethod
    def handle_dow(ruleId, methodParams):
        with TimerModule.SCHEDULER_LOCK:
            keyName = TimerModule._PARAM_DOW.get_kbx_param_name()
            dowVal = TimerModule.__get_arg(keyName, methodParams)
            try:
                dowVal = TimerModule._PARAM_DOW.cast(dowVal)
            except Exception as e:
                Logger.log_warning("Invalid day of week value, val:", dowVal, "ex:", e)
                return
            
            # Add scheduler
            dayOfWeek = ",".join((str(d) for d in dowVal))
            TimerModule.__add_scheduler(ruleId, "day_of_week", "0", "0", "0", "*", "*", dayOfWeek)
        
    @staticmethod
    def delete_scheduler(ruleId):
        with TimerModule.SCHEDULER_LOCK:
            try:
                schedulerNames = TimerModule.RULE_ID_SCHEDULER_TRACKER.pop(ruleId, set({}))
                for schedulerName in schedulerNames:
                    TimerModule.SCHEDULER_ID_TRACKER[schedulerName].remove(ruleId)
                    
                    if not TimerModule.SCHEDULER_ID_TRACKER[schedulerName]:
                        SchedulerService.remove_job(str(schedulerName))
                        del(TimerModule.SCHEDULER_ID_TRACKER[schedulerName])
                        
                        Logger.log_debug("Removed Timer:", schedulerName)
    
            except Exception as e:
                Logger.log_warning("Failed to remove timer:", e)
    
    @staticmethod
    def __get_arg(keyName, methodParams):
        '''
        Method to parse out corresponding value from methodParams.
        '''
        for methodParam in methodParams:
            if methodParam.get(AppConstants.ARG_NAME) == keyName:
                return methodParam.get(AppConstants.ARG_CURRENT_VALUE)
        else:
            Logger.log_warning("Unable to find value:", keyName)
            return None
        
    @staticmethod
    def __add_scheduler(ruleId, kbxMethodIdentifier, second, minute, hour, dayOfMonth, month, dayOfWeek):
        '''
        second="0", minute="*", hour="*", dayOfMonth="*", month="*", dayOfWeek="*"
        '''
        try:
            uniqueName = "_".join([kbxMethodIdentifier, second, minute, hour, dayOfMonth, month, dayOfWeek])
            schedulerName = hash(uniqueName)
            
            if schedulerName not in TimerModule.SCHEDULER_ID_TRACKER:
                SchedulerService.add_cron_job(str(schedulerName),
                                              kbxTargetAppId=AppInfo.get_app_id(),
                                              kbxTargetMethod="scheduler_callback",
                                              kbxTargetModule="timer_module",
                                              second=second,
                                              minute=minute,
                                              hour=hour,
                                              dayOfMonth=dayOfMonth,
                                              month=month,
                                              dayOfWeek=dayOfWeek,
                                              kbxTargetParams={"kbxMethodIdentifier":kbxMethodIdentifier},
                                              store=False)
    
                TimerModule.SCHEDULER_ID_TRACKER[schedulerName] = [ruleId]
                TimerModule.RULE_ID_SCHEDULER_TRACKER[ruleId] = [schedulerName]
                
                Logger.log_debug("Added Timer:", schedulerName, uniqueName)
            else:
                TimerModule.SCHEDULER_ID_TRACKER[schedulerName].append(ruleId)
                TimerModule.RULE_ID_SCHEDULER_TRACKER[ruleId].append(schedulerName)

        except Exception as e:
            Logger.log_warning("Failed to add timer:", e)
    
    def __scheduler_callback(self, request):
        self.send_response({}, request.requestId)
        try:
            self.send_system_event(TimerModule.EVENT_TAG, "".join(("{\"kbxMethodIdentifier\":\"", str(request.get_arg("kbxMethodIdentifier")), "\"}")))
        except Exception as e:
            Logger.log_warning("Timer Module failed to process scheduler callback:", str(e))

    def __date_time_range(self, request):
        try:
            dtVal = request.get_value(TimerModule._PARAM_DT_RANGE.get_kbx_param_name())
            startDateTime = dtVal.get_start_date_time()
            endDateTime = dtVal.get_end_date_time()
            
            execTime = request.get_arg(AppConstants.KEY_CONDITION_TIMESTAMP)
            execTime = int(execTime)
            
            if execTime > endDateTime:
                # Allow a time delta of 59 seconds
                response = bool(abs(execTime - endDateTime) <= 59)
            else:
                response =  bool(startDateTime <= execTime <= endDateTime)
            
            if not response:
                raise AutomationException(11800)
                
            self.send_response({}, request.requestId)
        except AutomationException as ae:
            Logger.log_error("TimerModule date_time range failed on comparison:", str(ae))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
        except Exception as e:
            Logger.log_error("TimerModule date_time range failed on comparison (unexpected):", str(e))
            ae = AutomationException(11099, str(e))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
    
    def __time_range(self, request):
        try:
            try:
                tVal = request.get_value(TimerModule._PARAM_TIME_RANGE.get_kbx_param_name())
                startTime = tVal.get_start_time()
                endTime = tVal.get_end_time()
            except:
                # Backward compatible to daily_task
                kbxTime = KBXTime(kbxParamName="time")
                startTime = endTime = kbxTime.cast(request.get_arg("time"))
            
            execTime = request.get_arg(AppConstants.KEY_CONDITION_TIMESTAMP)
            execTime = datetime.datetime.fromtimestamp(execTime)
            execTime = (execTime.hour * 3600) + (execTime.minute * 60) + (execTime.second)
            
            if endTime < startTime:
                checkRange = [(startTime, 86400), (0, endTime + 59)]
            else:
                checkRange = [(startTime, endTime + 59)]
                
            for startVal, endVal in checkRange:
                if startVal <= execTime <= endVal:
                    response = True
                    break
            else:
                response = False
                
            if not response:
                raise AutomationException(11800)
            
            self.send_response({}, request.requestId)
        except AutomationException as ae:
            Logger.log_error("TimerModule time range failed on comparison:", str(ae))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
        except Exception as e:
            Logger.log_error("TimerModule time range failed on comparison (unexpected):", str(e))
            ae = AutomationException(11099, str(e))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
    
    def __day_of_week(self, request):
        try:
            dows = request.get_value(TimerModule._PARAM_DOW.get_kbx_param_name())
            
            execTime = request.get_arg(AppConstants.KEY_CONDITION_TIMESTAMP)
            execTime = datetime.datetime.fromtimestamp(execTime)
            execDow = execTime.isoweekday() % 7
            
            response = bool(execDow in dows)
            
            if not response:
                raise AutomationException(11800)
            
            self.send_response({}, request.requestId)
        except AutomationException as ae:
            Logger.log_error("TimerModule day_of_week failed on comparison:", str(ae))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())
        except Exception as e:
            Logger.log_error("TimerModule day_of_week failed on comparison (unexpected):", str(e))
            ae = AutomationException(11099, str(e))
            self.send_response({}, request.requestId, ae.get_error_code(), ae.get_error_message())


        
