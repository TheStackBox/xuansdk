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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class EventLogManagerService():

    @staticmethod
    def add_event_log(description=None, level=None, tag=None, details=[], icon=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Add an event log
        @param level:Number                  - The level of the log. 0: Verbose, 2:Debug, 3:Warning, 4:Error
        @param details:List<Dict>            - The list of details items
                                                      a. description:String                - The description
        @param tag:String                    - The tag of this log
        @param description:String            - The description
        @param icon:String                   - The icon of to be displayed
        @param appId:String                  - The App Id *** Attached using Service Class ***
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        2. logId:String                      - The log ID generated
        
        '''
        pass

    @staticmethod
    def get_log_list(startTime=None, endTime=None, level=None, tag=None, newestComeFirst=False, offset=0, limit=200, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get a list of logs
        @param startTime:Number              - Epoch time for the start time filter in seconds [Optional, default to start of the current logging session].
        @param endTime:Number                - Epoch time for the end time filter in seconds [Optional, default to the current time].
        @param tag:String                    - The tag to be filtered (use searching?) [Optional].
        @param appId:String                  - The App ID to be filtered [Optional, default to show all app].
        @param level:Number                  - The level of log to be filtered [Optional, default to show all]
        @param newestComeFirst:Boolean       - Order the results by newest first [Optional, default to False]
        @param offset:Number                 - The data start offset
        @param limit:Number                  - The total data to return 
        
        @return: A dictionary with the following structure:
        1. totalItem:Number                  - The total item available for this fetch
        2. logs:List                         - A list of log item with each item of the following attributes
                                                      a. logId:String              - The log ID
                                                      b. logTime:Number            - The time of the log in Epoch time seconds
                                                      c. appId:String              - The ID of the app submitting the log
                                                      d. tag:String                - The tag of the log
                                                      e. description:String        - The description of the log
                                                      f. icon:String               - The icon of the log
                                                      g. hasDetail:Boolean         - Whether the log has details
                                                      h. level:Number              - The level of the log
                                    
        '''
        pass

    @staticmethod
    def get_log_details(logId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get details of a log event.
        @param logId:String                  - The ID of the log event item. 
        
        @return: A dictionary with the following structure:
        1. details:List<Dictionary>          - A list of details with each object contains:
                                                      a. index:Number                      - The index of the detail
                                                      b. description:String                - The description of the detail
        '''
        pass

    @staticmethod
    def add_hidden_tag(tag, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Hide certain tag from being listed
        @param tag:String                    - The tag
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def remove_hidden_tag(tag, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Remove certain tag from being hidden
        @param tag:String                    - The tag
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def list_hidden_tag(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get a list of hidden tag from being listed
        
        @return: A dictionary with the following structure:
        1. tags:List<String>                 - The list of tags
        '''
        pass

    @staticmethod
    def remove_logs(endTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Remove a chunk of logs
        @param endTime:Number                - The end time of the removal
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def archive_logs(endTime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Archive and remove the logs
        @param endTime:Number                - The end time of the archive
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def set_log_duration(duration, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Set the duration to keep the log
        @param duration:Number               - The number of days to keep
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def set_log_db_path(newPath, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Set the DB path for the event log
        @param newPath:String                - The new path
        
        @return: A dictionary with the following structure:
        1. success:Boolean
        '''
        pass

    @staticmethod
    def get_event_log_setting(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the settings for event log.
        
        @return: A dictionary with the following structure:
        1. logDBPath:String                  - The path to store log DB. NULL if the DB is store in local
        2. logArchivePath:String             - The path to store archive. NULL if disabled
        3. logStartTime:Number               - The time which the log starts from in the form of Epoch time (seconds with decimal places)
        4. logDuration:Number                - The number of days to keep the log before removal / archive. -1 for Forever
        5. logNotificationEmail:String       - The Email Address to send notification.
        '''
        pass

    @staticmethod
    def get_archive_list(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get a list of archive available
        
        @return: A dictionary with the following structure:
        1. archives:List<Dictionary>         - The list of archives available, each containing
                                                      a. archiveName:String                - The display name of the archive
                                                      b. archiveId:String                  - The ID to identify the archive, used to get the content of the archive
        '''
        pass

    @staticmethod
    def get_archived_log_list(archiveId, startTime=None, endTime=None, level=None, tag=None, newestComeFirst=False, offset=0, limit=200, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get a list of logs from archive
        @param archiveId:String              - The archive ID  
        @param startTime:Number              - Epoch time for the start time filter in seconds [Optional, default to start of the current logging session].
        @param endTime:Number                - Epoch time for the end time filter in seconds [Optional, default to the current time].
        @param tag:String                    - The tag to be filtered (use searching?) [Optional].
        @param appId:String                  - The App ID to be filtered [Optional, default to show all app].
        @param level:Number                  - The level of log to be filtered [Optional, default to show all]
        @param newestComeFirst:Boolean       - Order the results by newest first [Optional, default to False]
        @param offset:Number                 - The data start offset
        @param limit:Number                  - The total data to return
        
        @return: A dictionary with the following structure:
        1. totalItem:Number                  - The total item available for this fetch
        2. logs:List                         - A list of log item with each item of the following attributes
                                                      a. logId:String              - The log ID
                                                      b. logTime:Number            - The time of the log in Epoch time seconds
                                                      c. appId:String              - The ID of the app submitting the log
                                                      d. tag:String                - The tag of the log
                                                      e. description:String        - The description of the log
                                                      f. icon:String               - The icon of the log
                                                      g. hasDetail:Boolean         - Whether the log has details
                                                      h. level:Number              - The level of the log
        '''
        pass

    @staticmethod
    def get_archived_log_details(archiveId, logId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get details of a archived log event.
        @param archiveId:String              - The archive ID
        @param logId:String                  - The ID of the log event item. 
        
        @return: A dictionary with the following structure:
        1. details:List<Dictionary>          - A list of details with each object contains:
                                                      a. index:Number                      - The index of the detail
                                                      b. description:String                - The description of the detail
        '''
        pass

