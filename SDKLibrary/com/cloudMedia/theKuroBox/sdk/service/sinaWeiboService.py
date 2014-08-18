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


class SinaWeiboService(object):

    @staticmethod
    def get_sinaweibo_callback_url(redirectURI, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get the sina weibo callback url to get the access code to add sina weibo sender
        redirectURI:String :- The redirect page URL after success authorise from sina weibo.
        return:Dictionary :eg- {"redirectUrl": "http://service.thexuan.com/weibo/CallbackURL.php?redirectURL=http://myredirectpage/"}
        '''
        pass
    
    @staticmethod    
    def add_sinaweibo_recipient(code, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        add sinaweibo recipient
        code:String :- get the authenticated code from get_sinaweibo_callback_url and set to system as service user.
        return:Dictionary :eg- {"success": "id": 5007766004,
                                "expire_in":61234",
                                "screen_name": "xuan",
                                "name": "xuan"}
        '''
        pass
    
    @staticmethod    
    def get_sinaweibo_recipient(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get sinaweibo recipient
        return:Dictionary :eg- {"success": "id": 5007766004,
                                "expire_in":61234",
                                "screen_name": "xuan",
                                "name": "xuan"}
        '''
        pass
    
    
    @staticmethod            
    def remove_sinaweibo_recipient(uid, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove the selected sender 
        return:Dictionary :eg- {"recipient": []}
        '''
        pass
    
    
    @staticmethod      
    def send_sinaweibo_private_message_text(text, receiverId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        send sinaweibo private message text 
        return:Dictionary :eg- {"result": "true", "data": {}, "sender_id": 222222, "type": "text", "receiver_id": 1234567, "text": "notification text", "created_at": "Thu Aug 07 18:14:24  0800 2014"}
        '''
        pass
    
    
    @staticmethod
    def set_service_status(status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set service status
        status:Boolean :- Turn on/off the service.1 = on, 0 = off
        return:Dictionary :eg- {"status": 1}
        '''
        pass
        
        
    @staticmethod
    def get_service_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get sina weibo service current status
        return:Dictionary :eg- {"status": 1}
        '''
        pass  
                        