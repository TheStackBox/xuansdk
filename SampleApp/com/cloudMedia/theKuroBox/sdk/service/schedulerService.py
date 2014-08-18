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


class SchedulerService(object):

    @staticmethod
    def add_cron_job(jobName, kbxTargetAppId, kbxTargetMethod, kbxTargetModule=None, kbxTargetGroupId=None, kbxTargetParams=None, second="0", minute="*", hour="*",
                     dayOfMonth="*", month="*", dayOfWeek="*", ttl=-1, misfireGraceTime=60, startTime=None, endTime=None, priority=3, store=True, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add cron job
        Default trigger interval is 1 minute.

        Params:
        jobName:String - [Required] Name of the job. (Job with the same name will override per app)
        kbxTargetAppId:Integer - [Required] Callback app id.
        kbxTargetMethod:String - [Required] Callback method name.
        kbxTargetModule:String - [Optional] Callback module name.
        kbxTargetGroupId:Integer - [Optional] Callback group name.
        kbxTargetParams:Dictionary - [Optional] Callback arguments.
        second:String - [Optional] Value ranged 0 - 59, supported cron syntax are [/,-].
        minute:String - [Optional] Value ranged 0 - 59, supported cron syntax are [/,-].
        hour:String - [Optional] Value ranged 0 - 23, supported cron syntax are [/,-].
        dayOfMonth:String - [Optional] Value ranged 1 - 31, supported cron syntax are [/,-]
        month:String - [Optional] Value ranged 1 - 12, supported cron syntax are [/,-]
        dayOfWeek:String - [Optional] Value ranged 0 - 6 where 0 is Sunday and 6 is Monday, supported cron syntax are [/,-]
        ttl:Integer - [Optional] Time to live indicates maximum amount of times a particular job can be executed.
        kwargs:String - [Optional] Extra callback parameter for apiCall in json string format.
        misfireGraceTime:Integer - [Optional] Tolerable delay in seconds if a particular job is not able to fire at given time.
        startTime:Integer - [Optional] Unix timestamp that specifies when the job should begins.
        endTime:Integer - [Optional] Unix timestamp that specifies when the job will expires.
        priority:Integer - [Optional] Priority is used to determine the order of executions for jobs that are triggered at the same time. From 1 - most prioritized to 5 - least prioritized
        store:Boolean - [Optional] True to store the job into system database. True by default.

        Returns:
        Job object as dictionary.
        '''
        pass

    @staticmethod
    def add_interval_job(jobName, kbxTargetAppId, kbxTargetMethod, kbxTargetModule=None, kbxTargetGroupId=None, kbxTargetParams=None, days=None, hours=None, minutes=None, seconds=None,
                         ttl=-1, misfireGraceTime=60, startTime=None, endTime=None, priority=3, store=True, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add interval job.

        Params:
        jobName:String - [Required] Name of the job. (Job with the same name will override per app)
        kbxTargetAppId:Integer - [Required] Callback app id.
        kbxTargetMethod:String - [Required] Callback method name.
        kbxTargetModule:String - [Optional] Callback module name.
        kbxTargetGroupId:Integer - [Optional] Callback group name.
        kbxTargetParams:Dictionary - [Optional] Callback arguments.
        days:Integer - [Required Either One] Execute every specified day(s).
        hours:Integer - [Required Either One] Execute every specified hour(s).
        minutes:Integer - [Required Either One] Execute every specified minute(s).
        seconds:Integer - [Required Either One] Execute every specified seconds.
        ttl:Integer - [Optional] Time to live indicates maximum amount of times a particular job can be executed.
        kwargs:String - [Optional] Extra callback parameter for apiCall in json string format.
        misfireGraceTime:Integer - [Optional] Tolerable delay in seconds if a particular job is not able to fire at given time.
        startTime:String - [Optional] Unix timestamp that specifes when the job should begins.
        endTime:String - [Optional] Unix timestamp that specifies when the job will expires.
        priority:Integer - [Optional] Priority is used to determine the order of executions for jobs that are triggered at the same time. From 1 - most prioritized to 5 - least prioritized.
        store:Boolean - [Optional] True to store the job into system database. True by default.

        Returns:
        Job object as dictionary.
        '''
        pass

    @staticmethod
    def add_date_job(jobName, kbxTargetAppId, kbxTargetMethod, timestamp, kbxTargetModule=None, kbxTargetGroupId=None, kbxTargetParams=None,
                     misfireGraceTime=60, priority=3, store=True, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add date job.

        Params:
        jobName:String - [Required] Name of the job. (Job with the same name will override per app)
        kbxTargetAppId:Integer - [Required] Callback app id.
        kbxTargetMethod:String - [Required] Callback method name.
        timestamp:String - [Required] Unix timestamp for the execution time.
        kbxTargetModule:String - [Optional] Callback module name.
        kbxTargetGroupId:Integer - [Optional] Callback group name.
        kbxTargetParams:Dictionary - [Optional] Callback arguments.
        kwargs:String = [Optional] Extra callback parameter for apiCall in json string format.
        misfireGraceTime:Integer - [Optional] Tolerable delay in seconds if a particular job is not able to fire at given time.
        priority:Integer - [Optional] Priority is used to determine the order of executions for jobs that are triggered at the same time. From 1 - most prioritized to 5 - least prioritized.
        store:Boolean - [Optional] True to store the job into system database. True by default.
        **kwargs - Additional callback key-value pairs.

        Returns:
        Job object as dictionary.
        '''
        pass

    @staticmethod
    def update_job_priority(jobName, priority, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Update job priority.

        Params:
        jobName:String - [Required] Name of the job.
        priority:Number - [Required] Priority of the job ranging from 1 (Highest) - 5 (Lowest).

        Returns:
        Job object as dictionary.
        '''
        pass

    @staticmethod
    def list_all_jobs(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List all jobs created by this app.

        Returns:
        Job objects as list of dictionary.
        '''
        pass

    @staticmethod
    def get_job(jobName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get Job Info.

        Params:
        jobName:String - [Required] Name of the job.

        Returns:
        Job object as dictionary.
        '''
        pass

    @staticmethod
    def remove_job(jobName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove job.

        Params:
        jobName:String - [Required] Name of the job.
        '''
        pass

    @staticmethod
    def remove_all_jobs(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove all jobs registered by your app.
        '''
        pass
