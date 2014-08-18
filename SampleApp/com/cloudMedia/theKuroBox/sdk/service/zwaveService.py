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
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod


class ZWaveService():

    @staticmethod
    def reset(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reset Z-Wave Controller Stick.
        '''
        pass
    

    @staticmethod
    def network_add(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Network Add.
        '''
        pass
    
    
    @staticmethod
    def network_remove(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Network Remove.
        '''
        pass
    
    
    @staticmethod
    def network_abort(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Abort add and stop.
        '''
        pass
    
    
    @staticmethod
    def network_list(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List paired node.
        '''
        pass
    
    
    @staticmethod
    def network_update(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Update network.
        '''
        pass
    
    
    @staticmethod
    def network_learn(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Z-Wave learn mode.
        '''
        pass
    
    
    @staticmethod
    def basic_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Basic get.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def basic_set(node, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Basic set.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def door_lock_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Door get.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def door_lock_set(node, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Door set.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def user_number_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        User number get.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def user_code_set(node, user, status, code, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        User code set.
        node:String :- return from API network_list
        user:String :- 
        status:String :- 
        code:String :- 
        '''
        pass
    
    
    @staticmethod
    def user_code_get(node, user, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        User code get.
        node:String :- return from API network_list
        user:String :- 
        '''
        pass
    
    
    @staticmethod
    def switch_multilevel_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel get.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def switch_multilevel_set(node, level, duration, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel set.
        node:String :- return from API network_list
        duration:Number :- duration
        '''
        pass
    
    
    @staticmethod
    def switch_multilevel_supported_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel supported get.
        node:String :- return from API network_list
        '''
        pass
    
    
    @staticmethod
    def switch_multilevel_start(node, primarySwitchDirection, primaryStartLevel, secondarySwitchDirection, secondarySwitchStep, duration, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel start.
        node:String :-  return from API network_list
        primarySwitchDirection:String :- 
        primaryStartLevel:String :- 
        secondarySwitchDirection:String :- 
        secondarySwitchStep:String :- 
        duration:String :- 
        '''
        pass
    
    
    @staticmethod
    def switch_multilevel_stop(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel stop.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def meter_capabilities_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Meter capabilities get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def meter_get(node, unit, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Meter get.
        node:String :-  return from API network_list
        unit:String :-  meter unit
        '''
        pass
    
    
    @staticmethod
    def meter_reset(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Meter reset.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def alarm_setup(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Alarm setup.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def alarm_get(node, vendorType, zwaveType, zwaveEvent, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Alarm get.
        node:String :-  return from API network_list
        vendorType:String :- 
        zwaveType:String :- 
        zwaveEvent:String :- 
        '''
        pass
    
    
    @staticmethod
    def alarm_set(node, zwaveType, status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Alarm set.
        node:String :-  return from API network_list
        zwaveType:String :- 
        status:String :- 
        '''
        pass
    
    
    @staticmethod
    def alarm_supported_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Alarm supported get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def alarm_supported_event_get(node, alarmType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Alarm setup.
        node:String :-  return from API network_list
        alarmType:String
        '''
        pass
    
    
    @staticmethod
    def binary_sensor_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Binary sensor get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def binary_switch_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Binary switch get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def binary_switch_set(node,value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Binary switch set.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def sensor_multilevel_get(node, sensorType, unit, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Sensor multilevel get.
        node:String :- return from API network_list
        sensorType:String :-  sensor type.
        unit:String :-  sensor unit.
        '''
        pass
    
    
    @staticmethod
    def sensor_multilevel_supported_get_sensor(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel supported get sensor.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def sensor_multilevel_supported_scale_get_scale(node, scaleType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Switch multilevel supported scale get scale.
        node:String :-  return from API network_list
        scaleType:String :- 
        '''
        pass
    
    
    @staticmethod
    def battery_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Battery get status.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def wakeup_get(node, scaleType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Wakeup get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def wakeup_set(node, receiveNode, interval, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Wakeup set.
        node:String :-  return from API network_list
        receiveNode:String :- 
        interval:String :- 
        '''
        pass
    
    
    @staticmethod
    def configuration_get(node, parameter, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Configuration get.
        node:String :-  return from API network_list
        parameter:String :- 
        '''
        pass
    
    
    @staticmethod
    def configuration_set(node, parameter, size, default, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Configuration set.
        node:String :-  return from API network_list
        parameter:String :- 
        size:String :- 
        default:String :- 
        value:String :- 
        '''
        pass
    
    
    @staticmethod
    def association_groupings_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Association groupings get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def association_specific_group_get(node, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Association specific group get.
        node:String :-  return from API network_list
        '''
        pass
    
    
    @staticmethod
    def association_get(node, group, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Association get.
        node:String :-  return from API network_list
        group:String
        '''
        pass
    
    
    @staticmethod
    def association_set(node, group, setNode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Association set.
        node:String :-  return from API network_list
        group:String :- 
        setNode:String :- 
        '''
        pass
    
    
    @staticmethod
    def association_remove(node, group, removeNode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Association remove.
        node:String :-  return from API network_list
        group:String :- 
        removeNode:String :- 
        '''
        pass
