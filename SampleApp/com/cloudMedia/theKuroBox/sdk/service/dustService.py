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

class DustService():
    
    @staticmethod
    def get_system_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Return system-level information about the hardware and software
        event:DUST_REPLY :eg-  {"macAddr":"00170D0000383013", "cmdId": 46, "swVer":"1.2.1.12", "hwVer":"16.33"}
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-  {"cmdId": 46}
        '''
        pass
    
    @staticmethod
    def get_manager_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get manager API statistics
        event:DUST_REPLY :eg-  {"apiRxOk": 26, "serRxCRCErr": 0, "apiTxFail": 0, "serRxOverruns": 0, "serRxCnt": 0, "apiTxErr": 0, 
                                "serTxCnt": 0, "cmdId": 53, "apiEstabConn": 2, "apiRxProtErr": 0, "apiTxOk": 0, "apiDroppedConn": 1};
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-  {"cmdId": 53}
        '''
        pass
    
    @staticmethod
    def clear_manager_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Clear accumulated network statistics
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":31}
        '''
        pass
    
    @staticmethod
    def get_time(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Return the current manager UTC time and absolute slot number (ASN)
        event:DUST_REPLY :eg-  {"utcUsecs": 503113, "asnOffset": 3863, "utcSecs": "000000003D227A3D", 
                                "cmdId": 23, "asn": "0000097511", "uptime": 4494};
        language:String - [Optional] Preferred language. Default is en.                        
        return:Dictionary :eg-  {"cmdId":23}
        '''
        pass
    
    @staticmethod
    def reset(address, resetType, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reset the system, network, or a mote
        address:String - mac address.
        resetType:String - reset type for the dust network.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-  {"cmdId":21}
        '''
        pass
    
    @staticmethod
    def set_time(utcs, utcus, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the UTC time on the manager
        utcs:String - utcs.
        utcus:String - utcus.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg-  {}
        '''
        pass
    
    @staticmethod
    def get_network_config(language=AppInfo.DEFAULT_API_LANGUAGE): 
        '''
        Retrieve network configuration parameters.
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 63}
        '''
        pass
    
    @staticmethod
    def get_ip_config(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Return manager's IP configuration parameters
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 67}
        '''
        pass
      
    @staticmethod
    def restore_factory_defaults(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Restore default configuration and clear the ACL
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 61}
        '''
        pass
      
    @staticmethod
    def get_license(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Return the current license key
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 55}
        '''
        pass
    
    @staticmethod
    def set_license(dustLicense, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Update the software license key
        dustLicense:String - dust license
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":56}
        '''
        pass
     
    @staticmethod
    def start_network(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        start network forming (auto join)
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 45}
        '''
        pass
     
    @staticmethod
    def get_mote_config_by_id(dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve a mote's configuration by mote ID
        dustId:String - dust id
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":65}
        '''
        pass
     
    @staticmethod
    def get_mote_config(address, nextMote, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve mote configuration parameters
        address:String - mac address
        nextMote:String - next Mote
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":47}
        '''
        pass
    
    @staticmethod
    def get_mote_info(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get mote statistics
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":62}
        '''
        pass
    
    @staticmethod
    def ping_mote(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send a ping (echo request) to a mote
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":42}
        '''
        pass
    
    @staticmethod
    def delete_mote(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Delete a mote from the Manager's database (when not in operational mode, i.e. Lost)
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":69}
        '''
        pass
    
    @staticmethod
    def get_mote_links(address, idx, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get information about mote's links (idx start from 0)
        address:String - mac address
        idx:String - idx
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":70}
        '''
        pass
    
    @staticmethod
    def exchange_network_id(moteId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send a new network ID to a mote
        moteId:String - mote id
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":34}
        '''
        pass
      
    @staticmethod
    def exchange_mote_join_key(address, key, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send a new join key to a mote
        address:String - mac address
        key:String - key
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":33}
        '''
        pass
    
    @staticmethod
    def set_mote_led(address, state, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set mote led for 'indicator 0'
        address:String - mac address
        state:String - state
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":2}
        '''
        pass
     
    @staticmethod
    def get_network_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get network statistics
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 64}
        '''
        pass
     
    @staticmethod
    def get_log(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve diagnostic logs from a mote
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":43}
        '''
        pass
    
    @staticmethod
    def get_path_info(source, dest, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get information about communication between two motes
        source:String - source path
        dest:String - destination path
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 48}
        '''
        pass
      
    @staticmethod
    def set_acl_entry(address, key, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add a new ACL entry or update an existing entry
        address:String - mac address
        dest:String - destination path
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":39}
        '''
        pass
      
    @staticmethod
    def subscribe(dustFilter, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Subscribe to notifications
        dustFilter:String - filter. eg.2
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":22}
        '''
        pass
    
    @staticmethod
    def set_network_config(networkId, apTxPower, frameProfile, maxMotes, baseBandwidth, downFrameMultVal, numParents, ccaMode,
                           channelList, autoStartNetwork, locMode, bbMode, bbSize, isRadioTest, bwMult,oneChannel, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set network configuration parameters
        networkId:String - filter. eg.2
        apTxPower:String -  apTxPower
        frameProfile:String - frame profile
        maxNotes:String - max notes
        baseBandwidth:String - base bandwidth
        downFrameMultVal:String -  down frame multval
        numParents:String -  number of Parents
        ccaMode:String - cca mode
        channelList:String -  channel list
        autoStartNetwork:String -  auto start network
        locMode:String - loc mode
        bbMode:String -  bb mode
        bbSize:String - bb size
        isRadioTest:String - is radio test
        bwMult:String -  bw mult
        oneChannel:String - one channel
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":26}
        '''
        pass
    
    @staticmethod
    def set_ip_config(address, mask, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set manager's IP configuration parameters
        address:String - mac address
        mask:String - mask
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":68}
        '''
        pass
      
    @staticmethod
    def radiotest_tx(testType, chanMask, repeatCnt, txPower, seqSize, delay1, pkLen1, pkLen2, delay2, pkLen3, delay3, pkLen4, delay4,
                     pkLen5, delay5, pkLen6, delay6, pkLen7, delay7, pkLen8, delay8,pkLen9, delay9, pkLen10, delay10, stationId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Command for testing the radio
        testType:String - mac address
        chanMask:String - mask
        repeatCnt:String - repeat cnt 
        txPower:String - tx power
        seqSize:String - sequence size
        delay1:String - delay 1
        pkLen1:String - pk length 1
        pkLen2:String - pk length 2
        delay2:String - delay 2
        pkLen3:String - pk length 3
        delay3:String - delay 3
        pkLen4:String - pk length 4
        delay4:String - delay 4 
        pkLen5:String - pk length 5
        delay5:String - delay 5
        pkLen6:String - pk length 6
        delay6:String - delay 6
        pkLen7:String - pk length 7
        delay7:String - delay 7
        pkLen8:String - pk length 8
        delay8:String - delay 8
        pkLen9:String - pk length 9
        delay9:String - delay 9
        pkLen10:String - pk length 10
        delay10:String - delay 10
        stationId:String - station id 
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":35}
        '''
        pass
     
    @staticmethod
    def radiotest_rx(duration, mask, dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Command for testing the radio
        duration:String - duration
        mask:String - mask
        dustId:String - dustId
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 38}
        '''
        pass
    
    @staticmethod
    def get_radiotest_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get radiotest stat
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId": 38}
        '''
        pass
    
    @staticmethod
    def get_next_path_info(address, dustFilter, dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Iterate through a mote's neighbors
        address:String - mac address
        dustFilter:String - filter
        dustId:String - dust id
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":49}
        '''
        pass
     
    @staticmethod
    def get_next_acl_entry(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Iterate through the ACL entries
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":40}
        '''
        pass
    
    @staticmethod
    def delete_acl_entry(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Remove a mote from the ACL
        address:String - mac address
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":41}
        '''
        pass
    
    @staticmethod
    def set_advertising(activate, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Turn on or off advertising
        activate:String - set on/off
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":50}
        '''
        pass
     
    @staticmethod
    def set_downstream_frame_mode(mode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Shorten or extend the downstream slotframe
        mode:String - mode
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":51}
        '''
        pass
    
    @staticmethod
    def set_cli_user(role, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Update CLI logins
        role:String - role
        password:String - password
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":58}
        '''
        pass
     
    @staticmethod
    def send_ip(address, priority, options, encryptedOffset, data, dataLen, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send IP data to a mote (via 6LowPAN)
        address:String - mac address
        priority:String - priority
        options:String - options
        encryptedOffset:String - encrytedOffset
        data:String - data
        dataLen:String - data length
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":59}
        '''
        pass
    
    @staticmethod
    def send_data(address, priority, options, srcPort, dstPort, data,dataLen, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Send a data packet to a mote
        address:String - mac address
        priority:String - priority
        options:String - options
        srcPort:String - source port
        dstPort:String - destination port
        data:String - data
        dataLen:String - data length
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":44}
        '''
        pass
    
    @staticmethod
    def set_common_join_key(key, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set new value for common join key
        key:String - key
        language:String - [Optional] Preferred language. Default is en.
        return:Dictionary :eg- {"cmdId":66}
        '''  
        pass
