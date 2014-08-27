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
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo


class BluetoothService():
    
    @staticmethod
    def bluetooth_scan(doStart):
        '''
        Start/Stop bluetooth device discovery process.
        doStart:Boolean :- True to start and False to stop.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    
    @staticmethod
    def bluetooth_scan_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth scan status. 'Idle' or 'Scanning'
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"status": "Scanning"}
        '''
        pass
    
    @staticmethod
    def bluetooth_pair(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth pair device.
        device:String :- Bluetooth device return from API bluetooth_list_devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_connect(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth connect device.
        device:String :- Bluetooth device return from API bluetooth_list_paired_devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_disconnect(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth disconnect device.
        device:String :- Bluetooth device return from API bluetooth_list_paired_devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_remove(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth remove device.
        device:String :- Bluetooth device return from API bluetooth_list_paired_devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_get_device_info(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth get device information.
        device:String :- Bluetooth device return from API bluetooth_list_paired_devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"Address": "00:00:00:00:00:00", "LE": "0", "Name": "Ener", "Class": "0x240404", "RSSI": "-49"}
        '''
        pass
    
    @staticmethod
    def bluetooth_list_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth list devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"Name": "tiny", "Address": "D9:00:00:00:00:00"}
        '''
        pass
    
    @staticmethod
    def bluetooth_list_connected_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth list connected devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"devices": {"Address": "00:00:00:00:00:00", "Name": "EnerPlex"}}
        '''
        pass
    
    @staticmethod
    def bluetooth_list_paired_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth list paired devices.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"devices": [{"Address": "00:00:00:00:00:00", "Name": "EnerPlex"}]}
        '''
        pass
    
    @staticmethod
    def bluetooth_low_energy_start(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth low energy start
        device:String - mac address of the device. e.g. 00:00:00:00:00:00
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_low_energy_stop(device, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth low energy stop
        device:String - mac address of the device. e.g. 00:00:00:00:00:00
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_low_energy_write(device, args, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth low energy write
        device:String - mac address of the device. e.g. 00:00:00:00:00:00
        args:String - GATTTOOL Commands and arguments:
                    primary [UUID]-Primary Service Discovery
                    included  [start hnd [end hnd]]  - Find Included Services
                    characteristics [start hnd [end hnd [UUID]]]  - Characteristics Discovery
                    char-desc [start hnd] [end hnd]  - Characteristics Descriptor Discovery
                    char-read-hnd <handle>  - Characteristics Value/Descriptor Read by handle
                    char-read-uuid <UUID> [start hnd] [end hnd] - Characteristics Value/Descriptor Read by UUID
                    char-write-req <handle> <new value>  - Characteristic Value Write (Write Request)
                    char-write-cmd <handle> <new value>  - Characteristic Value Write (No response)
                    sec-level [low | medium | high]  - Set security level. Default: low
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"success": true}
        '''
        pass
    
    @staticmethod
    def bluetooth_list_low_energy_connected_devices(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Bluetooth list low energy connected devices
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"devices": []}
        '''
        pass
    