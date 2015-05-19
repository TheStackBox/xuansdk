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

class BroadLinkService():
    
    DEVICE_TYPE_SP2 = 10001
    DEVICE_TYPE_RM2 = 10002
    
    @staticmethod
    def discover_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Return a list of broadlink device

        @return:
        A dictionary with following information:
        1. success:boolean               - Whether the call is success
        2. resultCode:Number             - Error code (if available)
        3. result:List                   - A List of dictionary which contains the following:
                                                a. name:String        - The device name
                                                b. mac:String         - The MAC Address of the device
                                                c. type:Number        - The type of device, refer to class constants.
        '''
        pass

    @staticmethod    
    def sp2_change_power_status(mac, status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function: Change power status of BL switch
        @param mac:String               - The MAC Address of the BL device
        @param status:boolean           - True : turn on [default], False : Turn off
        
        @return: A dictionary with the following properties:
        1. success:boolean              - Whether the request success
        2. resultCode:Number            - Error code (if available)
        '''
        pass

    @staticmethod
    def get_sp2_device_information(mac, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get the information of BL device.
        @param mac:String               - The MAC address of the device
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Dictionary               - The content of the result
                                                a. status:Number            - The power status
                                                b. power:Number             - The power frequency
        '''
        pass

    @staticmethod
    def rm2_get_module_list(mac, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get module list (remote control)
        
        @param mac:String               - The MAC address of the device
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Array                  - An array of dictionary each containing properties below:
                                                a. name:String            - The name of the module
                                                b. id:Number              - The id of the module
                                                c. type:Number            - The type of the module
        
        '''
        pass

    @staticmethod
    def rm2_add_module(mac, moduleName, moduleType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Add a module
        
        @param mac:String               - The MAC address of the device
        @param moduleName:String        - The name of the module
        @param moduleType:Number        - The type of the module. MIBOX1 200, MIBOX1S 201, MITV 202, APPLE_TV 203, STB 204, COMMON_TV 205, COMMON_AIRCON 250 
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Dictionary             - Result containing properties below:
                                                a. id:Number                 - The id of the module
        '''
        pass

    @staticmethod 
    def rm2_change_module_name(mac, moduleId, moduleName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Add a module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module 
        @param moduleName:String        - The name of the module
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod
    def rm2_delete_module(mac, moduleId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Delete a module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod  
    def rm2_get_key_list(mac, moduleId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get a list of key of a module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Array                  - An array of dictionary, each containing following properties:
                                                   a. index:Number                - Index of the key
                                                   b. name:Strign                 - The name of the key
        '''
        pass

    @staticmethod
    def rm2_add_key(mac, moduleId, keyName, keyIndex=0, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Add a key into module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module to add key
        @param keyName:String           - The name of the key
        @param keyIndex:Number          - The index to be inserted
        @param keyAttribute:String      - Unknown usage   
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Dictionary             - Result containing properties below:
                                                a. id:Number                 - The id / index of the key
        '''
        pass

    @staticmethod
    def rm2_change_key_name(mac, moduleId, keyIndex, keyName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Change name of a key
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module to add key
        @param keyName:String           - The name of the key
        @param keyIndex:Number          - The index to be changed
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod
    def rm2_delete_key(mac, moduleId, keyIndex, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Delete a key from module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module to add key
        @param keyIndex:Number          - The index to be removed
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod
    def rm2_start_learn_key(mac, moduleId, keyIndex, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Learn IR key for a particular key in a module
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module 
        @param keyIndex:Number          - The index to be learned
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod
    def rm2_cancel_learn_key(mac, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Cancel IR key learning
        
        @param mac:String               - The MAC address of the device
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

    @staticmethod
    def rm2_get_learn_key_status(mac, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Get key learning status
        
        @param mac:String               - The MAC address of the device
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        3. result:Dictionary             - Result dictionary containing the following properties:
                                                   a. status:Number          - The status of the learning, 0 : successful, 1 : in learing, 2 : failed
        '''
        pass

    @staticmethod
    def rm2_send_key(mac, moduleId, keyIndex, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Send IR Key
        
        @param mac:String               - The MAC address of the device
        @param moduleId:Number          - The id of the module 
        @param keyIndex:Number          - The index to be learned
        
        @return: A dictionary of the device with properties as below:
        1. success:boolean               - Whether the API success
        2. resultCode:Number             - Error code (if available)
        '''
        pass

