/**
 * Copyright 2014 Cloud Media Sdn. Bhd.
 * 
 * This file is part of Xuan Automation Application.
 * 
 * Xuan Automation Application is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This project is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public License
 * along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
*/

define([
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection'
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var SenderModel = KuroboxModel.extend({
        defaults: {
            screenName: ''
        },

        fetch: function(options) {
            this.url = 'get_twitter_sender';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                //url: 'json/example.get_smtp_sender.json',
                param:{module:'twitter_module'}
            };
            KuroboxModel.prototype.fetch.apply(this, arguments);
        },

        save: function(oauthToken, oauthVerifier, isRecipient, options) {
            this.url = 'add_twitter_sender';
            this.dev_opt = {
                    //url: 'json/example.set_timezone.json',
                    bypassSession: true,
                    method: 'GET',
                    app_id: '2000100',
                    param:{oauthToken:oauthToken, oauthVerifier:oauthVerifier, isRecipient:isRecipient, module:'twitter_module'}
                };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        delete: function(screenName, options) {
            this.url = 'remove_twitter_sender';
            this.dev_opt = {
                    //url: 'json/example.set_timezone.json',
                    bypassSession: true,
                    method: 'GET',
                    app_id: '2000100',
                    param: { screenName: screenName , module:'twitter_module'}
                };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            if(data.response.sender){
                if(data.response.sender.length){
                    return {
                        screenName: data.response.sender[0].screenName
                    }                  
                }else{
                    return {
                        screenName: ''
                    }
                }
            }else{
                return {
                    screenName: ''
                }                
            }
        }
    });

    var SenderIsRecipientModel = KuroboxModel.extend({
        defaults: {
            isRecipient: false
        },

        fetch: function(options) {
            this.url = 'get_twitter_sender_as_recipient';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param: {module:'twitter_module'}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        setAsRecipient: function(isRecipient, options) {
            // 0 = sender not include in the recipient list
            // 1 = sender include in the recipient list (Default is 1)      
                  
            this.url = 'set_twitter_sender_as_recipient';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param: {isRecipient:isRecipient, module:'twitter_module'}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            return {
                isRecipient: data.response.isRecipient
            }
        }
    });

    var SmtpModel = KuroboxModel.extend({
        idAttribute: "smtpServerName",
        defaults: {
            label: '',
            smtpServerName: '',
            smtpServerPort: '465'
        }
    });

    var SmtpCollection = KuroboxCollection.extend({
        model: SmtpModel,
        fetch: function(options) {
            this.url = 'get_smtp_server';
            this.dev_opt = {
                //url: 'json/smtp.json',
                method: 'GET',
                bypassSession: true,
                app_id: '2000100',
                param:{module:'smtp_module'}
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            console.log('data >> ', data)
            return data.response.smtpServerList;
        }
    });

    var SenderBundle = {
        model: SenderModel,
        setting: SenderIsRecipientModel,
        collection: SmtpCollection
    };
    return SenderBundle;
});
