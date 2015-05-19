/**
* Copyright 2014-2015 Cloud Media Sdn. Bhd.
*
* This file is part of Xuan Automation Application.
*
* Xuan Automation Application is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* Xuan Automation Application is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
*/
/*global define*/

define([
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection'
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var RecipientModel = KuroboxModel.extend({
        idAttribute: "email",
        defaults: {
            email: ''
        },

        fetch: function() {
        },

        parse: function() {
        },

        save: function(key, val, options) {
        	this.url = 'add_smtp_recipient';
        	this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param_attr: {email:'email'},
                param: {module:'smtp_module'}
            };
            KuroboxModel.prototype.save.call(this, key, val, options);
        },

        delete: function(email, options) {
            this.url = 'remove_smtp_recipient';
            this.dev_opt = {
                    //url: 'json/example.set_timezone.json',
                    bypassSession: true,
                    method: 'GET',
                    app_id: '2000100',
                    param: { email: email , module:'smtp_module'}
                };
            KuroboxModel.prototype.fetch.call(this, options);
        }

    });

    var RecipientCollection = KuroboxCollection.extend({
        model: RecipientModel,
        fetch: function(options) {
            this.url = 'get_smtp_recipient';
            this.dev_opt = {
                //url: 'json/example.get_smtp_recipient.json',
                method: 'GET',
                app_id: '2000100',
                bypassSession: true,
                param:{module:'smtp_module'}
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },
        edit: function(targetEmail, newEmail, options) {
            this.url = 'change_smtp_recipient';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param: {targetEmail:targetEmail, newEmail:newEmail, module:'smtp_module'}
            };
            KuroboxCollection.prototype.fetch.call(this, options);
        },
        parse: function(data) {
            console.log('data >> ', data)
            return data.response.recipient;
        }
    });

    var RecipientBundle = {
        model: RecipientModel,
        collection: RecipientCollection
    };

    return RecipientBundle;
});
