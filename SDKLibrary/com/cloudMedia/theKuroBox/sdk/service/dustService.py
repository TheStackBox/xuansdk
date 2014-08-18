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


class DustService():
    
    @staticmethod
    def get_system_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_manager_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def clear_manager_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_time(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def reset(address, resetType, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_time(utcs, utcus, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_network_config(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_ip_config(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def restore_factory_defaults(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def get_license(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_license(dustLicense, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def start_network(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def get_mote_config_by_id(dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def get_mote_config(address, nextMote, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_mote_info(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def ping_mote(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def delete_mote(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_mote_links(address, idx, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def exchange_network_id(moteId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def exchange_mote_join_key(address, key, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_mote_led(address, state, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def get_network_info(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def get_log(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_path_info(source, dest, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def set_acl_entry(address, key, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def subscribe(dustFilter, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_network_config(networkId, apTxPower, frameProfile, maxMotes, baseBandwidth, downFrameMultVal, numParents, ccaMode,
                           channelList, autoStartNetwork, locMode, bbMode, bbSize, isRadioTest, bwMult,oneChannel, language=AppInfo.DEFAULT_API_LANGUAGE):
       pass
    
    @staticmethod
    def set_ip_config(address, mask, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
      
    @staticmethod
    def radiotest_tx(testType, chanMask, repeatCnt, txPower, seqSize, delay1, pkLen1, pkLen2, delay2, pkLen3, delay3, pkLen4, delay4,
                     pkLen5, delay5, pkLen6, delay6, pkLen7, delay7, pkLen8, delay8,pkLen9, delay9, pkLen10, delay10, stationId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def radiotest_rx(duration, mask, dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_radiotest_statistics(language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def get_next_path_info(address, dustFilter, dustId, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def get_next_acl_entry(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def delete_acl_entry(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_advertising(activate, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def set_downstream_frame_mode(mode, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_cli_user(role, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
     
    @staticmethod
    def send_ip(address, priority, options, encryptedOffset, data, dataLen, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def send_data(address, priority, options, srcPort, dstPort, data,dataLen, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
    
    @staticmethod
    def set_common_join_key(key, language=AppInfo.DEFAULT_API_LANGUAGE):
        pass
