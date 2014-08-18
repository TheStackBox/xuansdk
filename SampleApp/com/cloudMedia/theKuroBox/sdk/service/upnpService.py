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


class UPNPService():
    
    @staticmethod
    def upnp_list_upnp_servers(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List UPNP servers.
        return:Dictionary :eg- {"services": [{"UDN": "uuid:f785f8e6-f19e-4b0a-b2fd-ad8ec26386ac", "friendlyName": "aa: a - 23:"}]}

        '''                                
        pass
    
    @staticmethod
    def upnp_list_upnp_renderers(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        List UPNP renderers.
        return:Dictionary :eg- {"renderers": [{"UDN": "uuid:C6F2D312-E40D-4928-B1E2-C837F59B8D75", "friendlyName": "A(C6F2D312-4928-B1E2-C837F59B8D75)"}]}
        '''
        pass
    
    @staticmethod
    def upnp_get_protocol_info(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get protocol info.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"Source": [], "Sink": []}
        '''
        pass
    
    @staticmethod
    def upnp_play(udn, url, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Start playback.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def upnp_pause(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pause playback.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        '''
        pass
    
    @staticmethod
    def upnp_resume(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Resume playback.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        '''
        pass
    
    @staticmethod
    def upnp_stop(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop playback.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def upnp_get_transport_info(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get transport info.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"CurrentSpeed": 1, "CurrentTransportState": "STOPPED"}
        '''
        pass
    
    @staticmethod
    def upnp_get_media_info(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get media info.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"MediaDuration": "0:02:53", "NrTracks": 1, "NextURI": "NOT_IMPLEMENTED", "CurrentURI": "http://23.23.136.93/alsghoaeiw/test.mp3"}
        '''
        pass
    
    @staticmethod
    def upnp_get_track_info(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get track info.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"Track": 1, "RelTime": "0:00:41", "TrackDuration": "0:02:53", "AbsTime": "0:03:34", "TrackURI": "http://23.23.136.93/alsghoaeiw/test.mp3"}
        '''
        pass
    
    @staticmethod
    def upnp_get_mute(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get mute status.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"mute": "0"}
        '''
        pass
    
    @staticmethod
    def upnp_set_mute(udn, mute, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set mute status.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        mute:Boolean :- True=mute, False=unmute
        return:Dictionary :eg- {"response":{"status": "success"}}
        '''
        pass
    
    @staticmethod
    def upnp_get_volume(udn, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get volume.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        return:Dictionary :eg- {"volume": "33"}
        '''
        pass
    
    @staticmethod
    def upnp_set_volume(udn, volume, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set volume.
        udn:String :- UDN return from API upnp_list_upnp_renderers
        volume:Number :- volume.
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod
    def upnp_browse_upnp_dir(udn, objectId, startIndex, reqCount, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Browse UPNP directory.
        udn:String :- UDN return from API upnp_list_upnp_servers
        objectId:String :- First level is 0
        startIndex:Number :- data start index
        reqCount:Number :- data return count
        return:Dictionary :eg- {"folder": {"NumberReturned": 3, "container": [{"objectId": "2", "parent_id": "0", "title": "Videos"}, 
                                          {"objectId": "3", "parent_id": "0", "title": "Pictures"}, 
                                          {"objectId": "12", "parent_id": "0", "title": "Playlists"}]}}
        '''
        pass
