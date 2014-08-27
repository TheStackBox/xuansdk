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
#    This project is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
class TinyFinderService():
    
    @staticmethod
    def connect(addressCls):
        '''
        Connect to a TinyFinder device. Error will be raised if targeted device is not a TinyFinder.
        addressCls:String - [Required] Device MAC address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        
    @staticmethod
    def disconnect(addressCls):
        '''
        Disconnect from a connected TinyFinder.
        addressCls:String - [Required] Device MAC address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        
    @staticmethod
    def get_battery_level(addressCls):
        '''
        Get current battery level of connected TinyFinder.
        addressCls:String - [Required] Device MAC address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        
    @staticmethod
    def get_link_loss_value(addressCls):
        '''
        Get current link loss behavior value.
        addressCls:String - [Required] Device MAC address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        
    @staticmethod
    def get_signal_strength(addressCls):
        '''
        Get signal strength of connected TinyFinder. Provides also approximate distance from the box to the device.
        addressCls:String - [Required] Device MAC address.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {}
        '''
        pass
    
          
    @staticmethod
    def alert(addressCls,alertLevelCls):
        '''
        Trigger alarm of connected TinyFinder.
        addressCls:String - [Required] Device MAC address.
        alertLevelCls:Integer - [Required] 0 - Stop alert, 1 - Alert in lower Volume , 2 - Alert in higher volume
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        
    @staticmethod
    def set_link_loss_value(addressCls,alertLevelCls):
        '''
        Set link loss behavior value. (When connected device is out of the range from the box)
        addressCls:String - [Required] Device MAC address.
        alertLevelCls:Integer - [Required] 0 - Do not alert, 1 - Alert in lower Volume , 2 - Alert in higher volume
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success":true}
        '''
        pass
    
        