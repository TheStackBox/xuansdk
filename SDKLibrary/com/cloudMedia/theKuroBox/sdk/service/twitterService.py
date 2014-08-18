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


class TwitterService():
    
    @staticmethod
    def get_twitter_callback_url(callbackURL, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get the twitter callback url to get the verifier to add twitter sender
        callbackURL:String :- Callback URL
        return:Dictionary :eg- {"twitterCallbackURL": "http://goo.gl/uKpTfc"}
        '''
        pass
            
            
    @staticmethod     
    def add_twitter_sender(oauthToken, oauthVerifier, isRecipient=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        add twitter sender
        oauthToken:String :- get the authenticated token from get_twitter_callback_url
        verifier:String :- get the authenticated verifier from get_twitter_callback_url
        isRecipient:Boolean :- add target sender to the recipient list
        return:Dictionary :eg- {"sender": [{"screenName": "sss"}]}
        '''
        pass
        
        
    @staticmethod
    def send_twitter_direct_message(screenName, text, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        send the twitter notification with the provided screenName
        screenName:String :-twitter screenName without prefix @ (must a twitter follower from sender)
        text:String :- sending text, not more than 160 character
        return:Dictionary :eg- {"returnMessage": "", "data": {}, "success": true}
        '''
        pass
        
        
    @staticmethod    
    def get_twitter_recipient(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter recipeint from the system
        return:Dictionary :eg- {"recipient": [{"screenName": "OverTheLineAUS"}]}
        ''' 
        pass
        
        
    @staticmethod    
    def get_twitter_followers_list(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter followers from the system
        return:Dictionary :eg- {"followers": [{"id": 2150014417, "name": "OverTheLineSports", "screenName": "OverTheLineAUS"}]}
        ''' 
        pass
    
    
    @staticmethod    
    def change_twitter_recipient(targetScreenName, newScreenName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        change the selected recipient 
        targetScreenName:String :- the recipient screen name which need to change.
        newScreenName:String :- the new recipient screen name for changed.
        return:Dictionary :eg- {"recipient": [{"screenName": "SamuelDiMaria"}]}
        '''
        pass
    
    
    @staticmethod        
    def get_twitter_sender(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter sender from the system
        return:Dictionary :eg- {"sender": [{"screenName": "SamuelDiMaria"}]}
        ''' 
        pass
    
    
    @staticmethod 
    def remove_twitter_sender(screenName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove twitter sender from the system by twitter screenName
        screenName:String :- twitter screenName without prefix @
        return:Dictionary :eg- {"response":{"sender": [{"screenName": "aaa"}]}
        '''
        pass
    
    
    @staticmethod 
    def remove_twitter_recipient(screenName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove twitter recipient from the system by twitter screenName
        screenName:String :- twitter screenName without prefix @
        return:Dictionary :eg- {"response":{"recipient": [{"screenName": aaa"}]}
        '''
        pass
        
    
    @staticmethod 
    def remove_all_twitter_recipient(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove all twitter recipient from the system.
        return:Dictionary :eg- {"response":{"recipient": [{"screenName": "aaa"}]}}
        '''
        pass
    
    
    @staticmethod
    def add_twitter_recipient(screenName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        add twitter recipient to the system with twitter screenName
        screenName:String :- twitter screenName without prefix @
        return:Dictionary :eg- {"recipient": [{"screenName": "OverTheLineAUS"}]}
        '''
        pass


    @staticmethod
    def set_service_status(status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        status:Boolean :- Turn on/off the service. 0 = On  1 = Off
        return:Dictionary :eg- {"response":{"status": 1}}
        '''
        pass
        
        
    @staticmethod
    def get_service_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter service current status
        return:Dictionary :eg- {"response":{"status": 1}}
        '''
        pass
    
  
    @staticmethod    
    def on_twitter_message_received(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter notification when twitter account received new tweet
        return:Dictionary :eg- {"response":{"value":true}}
        '''
        pass
  
        
        
    