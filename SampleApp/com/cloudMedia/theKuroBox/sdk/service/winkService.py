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

class WinkService():
    
    @staticmethod
    def login(clientId, clientSecret, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        login to use wink services
        clientId:String :- client id given by wink upon request
        clientSecret:String :- client secret given by wink upon request
        username:String :- username registered 
        password:String :- password registered
        return:Dictionary :eg- {"login_credentials": {"data":{"access_token":"895e2254d7ae52381b8c85079", "refresh_token":"e8e578f882d07b3a94b2f","token_type":"bearer", "token_endpoint":"https://winkapi.quirky.com/oauth2/token"},"errors":[], "pagination":{},"access_token":"c454d7ae52381b8c85079", "refresh_token":"e8e5ddda7b3a94b2f","token_type":"bearer", "token_endpoint":"https://winkapi.quirky.com/oauth2/token"},"returnValue":100,"returnMessage":"Ok"}     
        '''
        pass

    @staticmethod
    def refresh_expired_token(clientId, clientSecret, refreshToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Refresh access token when current access token has expired
        clientId:String :- client id given by wink upon request
        clientSecret:String :- client secret given by wink upon request
        refreshToken:String :- refreshToken given when login 
        return:Dictionary :eg- {"refreshed_tokens_credentials": {"data":{"access_token":"0acd226da0e405b20be7b5", "refresh_token":"e8e5ddda334673a78f8f","token_type":"bearer", "token_endpoint":"https://winkapi.quirky.com/oauth2/token"},"errors":[],"pagination":{}, "access_token":"0aca0e405b20be7b5","refresh_token":"e8e5f882d07b3a94b2f", "token_type":"bearer","token_endpoint":"https://winkapi.quirky.com/oauth2/token"},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def get_user_profile(accessToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        login to use wink services
        accessToken:String :- token obtained during login
        return:Dictionary :eg- {"profile": {"data":{"user_id":"34449","first_name":"calvin","last_name":"teoh", "email":"xuan"}}}
        '''
        pass

    @staticmethod
    def update_user_email(accessToken, email, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Change a new email address
        accessToken:String :- token obtained during login
        email:String :- new email address
        return:Dictionary :eg- {"updated_profile": {"data":{"user_id":"34449","first_name":"cain","last_name":"te", "email":"xuan"}}}
        '''
        pass

    @staticmethod
    def get_all_user_wink_device(accessToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve all devices under user account
        accessToken:String :- token obtained during login
        return:Dictionary :eg- {"wink_devices": {"data":[{"powerstrip_id":"8512","name":"Xuan Powerstrip", "locale":"en_us","units":{},"created_at":1401351304, "hidden_at":null,"subscription":{}, "triggers":[{"trigger_id":"94493", "name":"Motion trigger test", "enabled":false}]}]}}
        '''
        pass

    @staticmethod
    def get_all_user_linked_service(accessToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve all services linked with the account
        accessToken:String :- token obtained during login
        return:Dictionary :eg- {"linked_services": {"data":[{"linked_service_id":"7869","service":"google", "account":"xuan"}]}}
        '''
        pass

    @staticmethod
    def get_all_icon(accessToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve all icons from wink server
        accessToken:String :- token obtained during login
        return:Dictionary :eg- {"icons": {"data":[{"icon_id":"2","name":"coffee maker","object_type":"outlet", "images":{"medium":"http://s3.amazonaws.com/wink-production/icons/ios/coffee.png"}}, {"icon_id":"3","name":"computer","object_type":"outlet"}]}}
        '''
        pass

    @staticmethod
    def get_available_channels(accessToken, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve all available channel from wink 
        accessToken:String :- token obtained during login
        return:Dictionary :eg- {"channels": {"data":[{"channel_id":"1","name":"Time","inbound":true,"outbound":false, "required_parameters":{"timezone":true},"optional_parameters":{"locale":true}}]}}
        '''
        pass

    @staticmethod
    def get_powerstrip_info(accessToken, powerStripID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve a specific pivot powerstrip device information 
        accessToken:String :- token obtained during login
        powerStripID:String :- pivot power strip ID
        return:Dictionary :eg- {"powerstrip_info": {"data":{"powerstrip_id":"8512","name":"Xuan Powerstrip","locale":"en_us","units":{}, "created_at":1401351304,"hidden_at":null,"subscription":{},"triggers":[{"trigger_id":"94493","name":"Motion trigger test", "enabled":false,"trigger_configuration":{"edge":"rising","reading_type":"vibration","threshold":1.0,"object_id":"14431", "object_type":"sensor_pod"},"channel_configuration":{"powered":true,"outlet_index":0,"channel_id":"16", "wink_device_types":["powerstrip"],"wink_device_ids":["8512"]}}]}}}
        '''
        pass

    @staticmethod
    def update_powerstrip_setting(accessToken, powerStripID, deviceName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set a new name for a powerstrip 
        accessToken:String :- token obtained during login
        powerStripID:String :- pivot power strip ID. can be taken from get_all_user_wink_device()
        deviceName:String :- name to identify a specific powerstrip
        return:Dictionary :eg- {"powerstrip_name": {"data":{"powerstrip_id":"8512","name":"Xuan IoT PS"}}}
        '''
        pass

    @staticmethod
    def get_powerstrip_users(accessToken, powerStripID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set a new name for a powerstrip 
        accessToken:String :- token obtained during login
        powerStripID:String :- pivot power strip ID. can be taken from get_all_user_wink_device()
        return:Dictionary :eg- {"powerstrip_users": {"data":[{"actor_type":"user","actor_id":"34449","user_id":"34449","email":"xuan"}]}}
        '''
        pass

    @staticmethod
    def remove_user_from_powerstrip(accessToken, powerStripID, userEmailAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Delete a user from the device shared list
        accessToken:String :- token obtained during login
        powerStripID:String :- pivot power strip ID. can be taken from get_all_user_wink_device()
        userEmailAddress:String :- an user email address to share device with
        '''
        pass

    @staticmethod
    def get_outlet_information(accessToken, outletID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve an outlet information from pivot powerstrip
        accessToken:String :- token obtained during login
        outletID:String :- pivot power strip outlet ID, id is taken from get_powerstrip_info()
        return:Dictionary :eg- {"outlet_info": {"data":{"powered":true,"scheduled_outlet_states":[],"name":"Outlet NO1", "desired_state":{"powered":true},"last_reading":{"powered":true,"powered_updated_at":1404176477.9389703, "desired_powered":true},"outlet_index":0,"outlet_id":"17026","icon_id":"4"},"errors":[],"pagination":{}}, "returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_outlet_setting(accessToken, outletID, powered, name, iconID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set outlet information
        accessToken:String :- token obtained during login
        outletID:String :- pivot power strip outlet ID, id is taken from get_powerstrip_info()
        powered:String :- outlet on or off. Accepted input are true or false (param required)
        name:String :- outlet name a user wants (param not necessary required)
        iconID:String :- id of a icon for that outlet (param not necessary required)
        return:Dictionary :eg- {"new_outlet_setting": {"data":{"powered":"false","name":"xuan2"}}}
        '''
        pass

    @staticmethod
    def set_outlet_event(accessToken, outletID, name, powered, enable, tzid, date, time, alarmRule, days, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set outlet event
        accessToken:String :- token obtained during login
        outletID:String :- pivot power strip outlet ID, id is taken from get_powerstrip_info()
        powered:String :- outlet on or off. Accepted input are true or false
        name:String :- outlet name a user wants
        enable:String :- enable the event directly. Accepted input are true or false
        tzid:String :- time zone id eg: Asia/Kuala_Lumpur
        date:String :- event start date. format: yyyymmdd  eg: 20140627
        time:String :- event start time. format: hhmmss in military time  eg: 150000 for 3:00:00PM
        alarmRule:String :- alarm event occurence. Supported input daily or weekly
        days:String :- days when alarm is activated. only use if alarmRule = "weekly". eg: mo,we,fr,sa
        return:Dictionary :eg- {"new_outlet_event": {"data":{"next_at":1404706500,"enabled":true, "recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T121500\\nRRULE:FREQ=WEEKLY;BYDAY=MO,TU", "scheduled_outlet_state_id":"18253","outlet_id":"17027","name":"boxTest1","powered":true}, "errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def get_nimbus_clock(accessToken, clockID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve information about a nimbus clock
        accessToken:String :- token obtained during login
        clockID:String :- nimbus cloud clock id. can be taken from get_all_user_wink_device()
        return:Dictionary :eg- {"nimbus_info": {"data":{"last_reading":{"connection":true,"connection_updated_at":1404262522.2716076},
                                "dials":[{"name":"Time","value":44002.0,"position":359.0,"label":"12:13 PM",
                                "labels":["12:13 PM","Kuala Lumpur"],"brightness":25}]}}}
        '''
        pass

    @staticmethod
    def update_nimbus_clock(accessToken, clockID, newNimbusName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus cloud clock name
        accessToken:String :- token obtained during login
        clockID:String :- nimbus cloud clock id. can be taken from get_all_user_wink_device()
        newNimbusName:String :- new nimbus name
        return:Dictionary :eg- {"nimbus_info": {"data":{"last_reading":{"connection":true,"connection_updated_at":1404262522.2716076}, "dials":[{"name":"Time","value":44002.0,"position":359.0,"label":"12:13 PM", "labels":["12:13 PM","Kuala Lumpur"],"brightness":25}]}}}
        '''
        pass

    @staticmethod
    def get_clock_users(accessToken, clockID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve shared users of the clock
        accessToken:String :- token obtained during login
        clockID:String :- nimbus cloud clock id. can be taken from get_all_user_wink_device()
        return:Dictionary :eg- {"nimbus_users": {"data":[{"actor_type":"user","actor_id":"34449","user_id":"34449","email":"xuan"}]}}
        '''
        pass

    @staticmethod
    def remove_user_from_clock(accessToken, clockID, userEmailAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove a user from the clock shared list
        accessToken:String :- token obtained during login
        clockID:String :- nimbus cloud clock id. can be taken from get_all_user_wink_device()
        userEmailAddress:String :- email address of a user to add
        '''
        pass

    @staticmethod
    def set_dial_name(accessToken, dialID, newDialName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus dial name
        accessToken:String :- token obtained during login
        dialID:String :- dial id of the clock, taken from get_nimbus_clock()
        newDialName:String :- name for the dial
        return:Dictionary :eg- {"dial_name": {"data":{"name":"hello dial","value":49709.0,"position":359.0, "label":"1:48 PM","labels":["1:48 PM","Kuala Lumpur"],"brightness":25, "channel_configuration":{"timezone":"Asia/Kuala_Lumpur","locale":"en_US","channel_id":"1", "object_type":null,"object_id":null},"dial_configuration":{"rotation":"ccw","max_position":359, "min_value":1,"min_position":100,"scale_type":"linear","max_value":30,"num_ticks":12},"dial_index":0, "dial_id":"28997","refreshed_at":1404280109},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def set_dial_brightness(accessToken, dialID, brightnessValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus dial brightness
        accessToken:String :- token obtained during login
        dialID:String :- dial id of the clock, taken from get_nimbus_clock()
        brightnessValue:String :- brightness for the dial. range 0-100
        return:Dictionary :eg- {"dial_brightness": {"data":{"name":"hello dial","value":50265.0,"position":359.0, "label":"1:57 PM","labels":["1:57 PM","Kuala Lumpur"],"brightness":50}}}
        '''
        pass

    @staticmethod
    def set_label_display(accessToken, dialID, firstLabelValue, secondLabelValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus dial display label to be able to set the label, must first set the channel ID to 10 using update_clock_channel_config()
        accessToken:String :- token obtained during login
        dialID:String :- dial id of the clock, taken from get_nimbus_clock()
        firstLabelValue:String :- the front label to display
        secondLabelValue:string :- the back label to display when the clock button is pressed
        return:Dictionary :eg- {"dial_label": {"data":{"name":"Email","value":0.0,"position":0.0, "label":"Louis","labels":["Louis","Vuitton"],"brightness":100}}}
        '''
        pass

    @staticmethod
    def update_clock_dial_config(accessToken, dialID, scaleType, rotation, minPosition, minValue, maxPosition, maxValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus clock dial configuration
        accessToken:String :- token obtained during login
        dialID:String :- dial id of the clock, taken from get_nimbus_clock()
        scaleType:String :- scale of the dial
        rotation:String :- which way the needle rotate. input cw for clockwise or ccw for counter clockwise
        minPosition:Number :- degree rotation which corresponds to min_value. 0-360 generally but not required to do so
        minValue:Number :- any number. minimum data value the dial should attempt to display at min_position
        maxPosition:Number :- degree rotation which corresponds to max_value. 0-360 generally but not required to do so
        maxValue:Number :- any number greater than min_value. the maximum data value the dial should attempt to display at max_position
        return:Dictionary :eg- {"dial_config": {"data":{"name":"Email","value":0.0,"position":0.0,"label":"Gotze", "labels":["Gotze","Rues"],"brightness":100,"channel_configuration":{"channel_id":"10", "object_type":null,"object_id":null},"dial_configuration":{"max_value":30,"rotation":"cw", "max_position":359,"scale_type":"log","min_position":100,"min_value":1,"num_ticks":12},"dial_index":3, "dial_id":"29000","refreshed_at":null},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_clock_channel_config(accessToken, dialID, channelID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set nimbus clock channel configuration
        accessToken:String :- token obtained during login
        dialID:String :- dial id of the clock, taken from get_nimbus_clock()
        channelID:String :- service channel. eg, google email channel id is 5
        return:Dictionary :eg- {"response":{"dial_config": {"data":{"name":"Email","value":0.0,"position":0.0, "label":"Gotze","labels":["Gotze","Rues"],"brightness":100,"channel_configuration" :{"channel_id":"10","object_type":null,"object_id":null},"dial_configuration" :{"max_value":30,"rotation":"cw","max_position":359,"scale_type":"log", "min_position":100,"min_value":1,"num_ticks":12},"dial_index":3,"dial_id":"29000", "refreshed_at":null},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass

    @staticmethod
    def get_clock_alarm(accessToken, alarmID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get detailed information about an alarm
        accessToken:String :- token obtained during login
        alarmID:String :- alarm id of the clock, taken from get_nimbus_clock()
        return:Dictionary :eg- {"alarm": {"data":{"next_at":null,"enabled":false,"recurrence": "DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA", "alarm_id":"4085","name":"new alarm","media_id":"1"},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def get_all_alarms(accessToken, clockID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get all alarms of the clock
        accessToken:String :- token obtained during login
        clockID:String :- clock id of the clock, taken from get_nimbus_clock()
        return:Dictionary :eg- {"alarm_list": {"data":[{"next_at":null,"enabled":false,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA", "alarm_id":"4085","name":"new alarm","media_id":"1"},{"next_at":null,"enabled":false,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\ nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA","alarm_id":"4104","name":"new alarm","media_id":"1"},{"next_at":null,"enabled":false,"recurrence": "DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,WE,FR","alarm_id":"4105","name":"new alarm","media_id":"1"}, {"next_at":null,"enabled":false,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140701T215000\\nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,WE,FR","alarm_id":"4106", "name":"new alarm","media_id":"1"}]}}    
        '''
        pass

    @staticmethod
    def update_alarm_enable_status(accessToken, alarmID, enableValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set alarm enabled status
        accessToken:String :- token obtained during login
        alarmID:String :- alarm id of the clock, taken from get_nimbus_clock()
        enableValue:String :- enabled status, in true or false
        return:Dictionary :eg- {"alarm_enable": {"data":{"next_at":1404355800,"enabled":true,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\ nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA","alarm_id":"4085","name":"new alarm","media_id":"1"},"errors":[], "pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_alarm_name(accessToken, alarmID, alarmName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new alarm name
        accessToken:String :- token obtained during login
        alarmID:String :- alarm id of the clock, taken from get_nimbus_clock()
        alarmName:String :- new alarm name 
        return:Dictionary :eg- {"alarm_name": {"data":{"next_at":1404355800,"enabled":true,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T105000\\ nRRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA","alarm_id":"4085","name":"IoT alarm","media_id":"1"},"errors":[], "pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_alarm_recurrence(accessToken, alarmID, tzid, date, time, alarmRule, days, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new alarm recurrence
        accessToken:String :- token obtained during login
        alarmID:String :- alarm id of the clock, taken from get_nimbus_clock()
        tzid:String :- time zone id eg: "Asia/Kuala_Lumpur"
        date:String :- event start date. format: yyyymmdd  eg: 20140627
        time:String :- event start time. format: hhmmss in military time  eg: 150000 for 3:00:00PM
        alarmRule:String :- alarm event occurence. Supported input daily or weekly
        days:String :- days when alarm is activated. only used if alarmRule = weekly. eg: mo,we,fr,sa
        return:Dictionary :eg- {"data":{"next_at":1404282600,"enabled":true,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T1430\\nRRULE:FREQ=DAILY", "alarm_id":"4085","name":"IoT alarm","media_id":"1"},"errors":[],"pagination":{},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def set_new_alarm(accessToken, clockID, alarmName, tzid, date, time, alarmRule, enableValue, days, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new alarm 
        accessToken:String :- token obtained during login
        clockID:String :- clock id of the clock, taken from get_all_user_wink_device()
        alarmName:String :- new name for the new alarm
        tzid:String :- time zone id eg: Asia/Kuala_Lumpur
        date:String :- event start date. format: yyyymmdd  eg: 20140627"
        time:String :- event start time. format: hhmmss in military time  eg: 150000 for 3:00:00PM
        alarmRule:String :- alarm event occurence. Supported input daily or weekly
        enableValue:String :- enable to alarm directly or not. Supported true or false
        days:String :- days when alarm is activated. only used if alarmRule = weekly. eg: mo,we,fr,sa
        return:Dictionary :eg- {"alarm_recurrance": {"data":{"next_at":1404295200,"enabled":true,"recurrence":"DTSTART;TZID=Asia/Kuala_Lumpur:20140702T180000\\nRRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR", "alarm_id":"4113","name":"Work over","media_id":"1"},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def delete_clock_alarm(accessToken, alarmID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove current alarm from clock
        accessToken:String :- token obtained during login
        alarmID:String :- alarm id of the clock, taken from get_nimbus_clock()
        return:Dictionary :eg- {"status": "Success","returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def get_spotter_information(accessToken, sensorPodID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get spotter device information
        accessToken:String :- token obtained during login
        sensorPodID:String :- spotter id of the spotter, taken from get_all_user_wink_device()
        return:Dictionary :eg- {"spotter_info": {"data":{"last_event":{"brightness_occurred_at":1404266589.9857657, "loudness_occurred_at":1404282271.8778641,"vibration_occurred_at":1404282267.73207}, "sensor_pod_id":"14431","name":"Xuan Spotter","locale":"en_us","units":{}, "created_at":1401852834,"hidden_at":null,"subscription":{}}}}
        '''
        pass

    @staticmethod
    def update_spotter_name(accessToken, sensorPodID, newSpotterName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new alarm name
        accessToken:String :- token obtained during login
        sensorPodID:String :- spotter id of the spotter, taken from get_all_user_wink_device()
        newSpotterName:String :- new spotter name
        return:Dictionary :eg- {"spotter_name": {"data":{"last_event":{"brightness_occurred_at":1404266589.9857657,"loudness_occurred_at":1404282602.9368386, "vibration_occurred_at":1404282267.73207},"sensor_pod_id":"14431","name":"Xuan IoT Spot","locale":"en_us"}}}
        '''
        pass

    @staticmethod
    def get_spotter_shared_users(accessToken, sensorPodID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get spotter shared user list 
        accessToken:String :- token obtained during login
        sensorPodID:String :- spotter id of the spotter, taken from get_all_user_wink_device()
        return:Dictionary :eg- {"spotter_users": {"data":[{"actor_type":"user","actor_id":"34449","user_id":"34449", "email":"xuan"}]}}
        '''
        pass

    @staticmethod
    def remove_spotter_user(accessToken, sensorPodID, userEmailAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove user from spotter shared list 
        accessToken:String :- token obtained during login
        sensorPodID:String :- spotter id of the spotter, taken from get_all_user_wink_device()
        userEmailAddress:String :- user email which is to be added to the shared list
        '''
        pass

    @staticmethod
    def get_trigger(accessToken, triggerID, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List out all available triggers 
        accessToken:String :- token obtained during login
        triggerID:String :- trigger id for wink devices, taken from get_all_user_wink_device()
        return:Dictionary :eg- {"trigger": {"data":{"trigger_id":"94489","name":"temp 1","enabled":true,"trigger_configuration":{"edge":"falling", "reading_type":"temperature","threshold":26.11111111111111,"object_id":"14431","object_type":"sensor_pod"}, "channel_configuration":{"recipient_user_ids":null,"channel_id":"15","object_type":null,"object_id":null}, "triggered_at":1404263189,"sensor_threshold_event_id":"94489"},"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_trigger(accessToken, triggerID, enabled, name, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Edit a trigger name and enable status
        accessToken:String :- token obtained during login
        triggerID:String :- trigger id for wink devices, taken from get_all_user_wink_device()
        enabled:String :- enable of disable trigger, use true or false
        name:String :- new name for trigger
        return:Dictionary :eg- {"trigger": {"data":{"trigger_id":"94489","name":"noise detect","enabled":true, "trigger_configuration":{"edge":"falling","reading_type":"temperature","threshold":26.11111111111111, "object_id":"14431","object_type":"sensor_pod"},"channel_configuration":{"recipient_user_ids":null, "channel_id":"15","object_type":null,"object_id":null},"triggered_at":1404263189,"sensor_threshold_event_id":"94489"} ,"errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

    @staticmethod
    def update_trigger_config(accessToken, triggerID, edge, readingType, threshold, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Edit a trigger configuration
        accessToken:String :- token obtained during login
        triggerID:String :- trigger id for wink devices, taken from get_all_user_wink_device()
        edge:String :- data goes above or below the threshold. supported in falling or rising
        readingType:String :- readingType of the trigger. Supported values are connection,rightness,loudness,vibration,battery,humidity,temperature
        threshold:String :- a limit which will cause a trigger if reached threshold. eg. 0.8
        return:Dictionary :eg- {"trigger_config": {"data":{"trigger_id":"94489","name":"noise detect","enabled":true, "trigger_configuration":{"threshold":24.0,"edge":"rising","reading_type":"temperature", "object_id":"14431","object_type":"sensor_pod"},"channel_configuration":{"recipient_user_ids":null, "channel_id":"15","object_type":null,"object_id":null},"triggered_at":1404263189,"sensor_threshold_event_id":"94489"}, "errors":[],"pagination":{}},"returnValue":100,"returnMessage":"Ok"}
        '''
        pass

