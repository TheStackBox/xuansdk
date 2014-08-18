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


class SMTPService():
    
    @staticmethod
    def add_smtp_sender(email, password, smtpServer, port, isRecipient=False, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add a sender for email service 
        email:String :- the sender email
        password:String :- the email password
        smtpServer:String :- the smtp server for the sender, currently support smtp.gmail.com and smtp.mail.yahoo.com
        port:Number :- the smtpServer port
        isRecipient:Boolean :- add target sender to the recipient list
        return:Dictionary :eg- {"sender": [{"smtpServerPort": "587", "smtpServerName": "smtp.gmail.com", "email": "@gmail.com"}]}
        '''
        pass


    @staticmethod
    def add_smtp_recipient(email, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Add a recipient for email service 
        email:String :- the sender email
        return:Dictionary :eg- {"recipient": [{"email": "@yahoo.com"}]}
        '''
        pass
    
    
    @staticmethod
    def get_smtp_recipient(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get a list of recipient from email service 
        return:Dictionary :eg- {"recipient": [{"email": "@yahoo.com"}]}
        '''
        pass
    
    
    @staticmethod
    def get_smtp_sender(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get the sender of the email service 
        return:Dictionary :eg- {"sender": [{"smtpServerPort": "587", "smtpServerName": "smtp.gmail.com", "email": "@gmail.com"}]}
        '''
        pass
        
        
    @staticmethod     
    def remove_smtp_sender(email, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove the selected sender 
        email:String :- the sender email which need to remove
        return:Dictionary :eg- {"sender": []}
        '''
        pass
    
    
    @staticmethod    
    def change_smtp_recipient(targetEmail, newEmail, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        change the selected recipient
        targetEmail:String :- the recipient email which need to change
        newEmail:String :- the new recipient email for change
        return:Dictionary :eg- {"recipient": [{"email": "@yahoo.com"}, {"email": "test@yahoo.com"}]}
        '''
        pass
    
    
    @staticmethod    
    def remove_smtp_recipient(email, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove the selected recipient 
        email:String :- the recipient email which need to remove
        return:Dictionary :eg- {"recipient": [{"email": "@yahoo.com"}]}
        '''
        pass
        
        
    @staticmethod 
    def remove_all_smtp_recipient(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        remove all smtp recipient from the system.
        return:Dictionary :eg- {"response":{"recipient": []}
        '''
        pass
        
        
    @staticmethod
    def send_smtp_mail(recipient, cc, subject, text, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        send notification email to the provided recipient.
        recipient:String :- the notification receiver. Example: johnsmith@gmail.com, abc@yahoo.com"
        cc:String :- carbon copy to other email address
        subject:String :- the subject of the email
        text:String :- the body of the email
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
                                 
                                 
    @staticmethod    
    def get_smtp_server(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get a list of supported smtp server.
        return:Dictionary :eg- {"smtpServerList": [{"smtpServerPort": 587, "label": "Gmail", "smtpServerName": "smtp.gmail.com"}, 
                                                  {"smtpServerPort": 587, "label": "Yahoo! Mail", "smtpServerName": "smtp.mail.yahoo.com"}]}
        '''
        pass
        
        
    @staticmethod
    def set_service_status(status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        status:Boolean :- Turn on/off the service.
        0 = On
        1 = Off
        return:Dictionary :eg- {"status": 1}
        '''
        pass
        
    @staticmethod
    def get_service_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter service current status
        return:Dictionary :eg- {"status": 1}
        '''
        pass  
    