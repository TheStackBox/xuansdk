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
from com.cloudMedia.theKuroBox.sdk.app.ipcClient import IPCClient
from com.cloudMedia.theKuroBox.sdk.util.logger import Logger


class EventTracker(object):

    def __init__(self, eventFiredCB):
        self.__events = {} # {"ruleIds":set([]), "isListening":False}
        #=======================================================================
        # Receives: ruleId, eventTag, eventData
        #=======================================================================
        self.__callback = eventFiredCB

    def update_listener(self, ruleId, *eventTags):
        '''
        Leave eventTags empty will remove all current eventTags
        '''
        eventTagsToProcess = set([])

        #=======================================================================
        # Remove old events
        #=======================================================================
        for eventTag, eventObj in self.__events.items():
            if ruleId in eventObj["ruleIds"]:
                eventObj["ruleIds"].remove(ruleId)
                eventTagsToProcess.add(eventTag)

        #=======================================================================
        # Register for new events
        #=======================================================================
        for eventTag in eventTags:
            if eventTag not in self.__events:
                self.__events[eventTag] = {"ruleIds":set([]), "isListening":False}

            self.__events[eventTag]["ruleIds"].add(ruleId)
            eventTagsToProcess.add(eventTag)

        #=======================================================================
        # Reprocess all affected event tags
        #=======================================================================
        for eventTag in eventTagsToProcess:
            self.__process_event(eventTag)

    def __process_event(self, eventTag):
        if eventTag not in self.__events:
            return

        eventInfo = self.__events[eventTag]
        ruleIdCount = len(eventInfo["ruleIds"])
        isListening = eventInfo["isListening"]

        if ruleIdCount > 0:
            #===================================================================
            # Register event
            #===================================================================
            if isListening is False:
                eventInfo["isListening"] = True
                IPCClient.register_event_listener(eventTag, self.__event_callback)
                Logger.log_debug("Listened to event:", eventTag)
        else:
            #=======================================================================
            # Unregister event and remove from memory
            #=======================================================================
            if isListening is True:
                IPCClient.unregister_event_listener(eventTag, self.__event_callback)
            del(self.__events[eventTag])

            Logger.log_debug("Removed event listener:", eventTag)


    def __event_callback(self, eventObj):
        eventTag = eventObj["eventTag"]
        eventData = eventObj["eventData"]

        if eventTag in self.__events:
            ruleIds = self.__events[eventTag]["ruleIds"]
            for ruleId in ruleIds:
                AppConstants.get_thread_pool_executor().submit(self.__callback, ruleId, eventTag, eventData)
