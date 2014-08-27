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
], function (_, KuroboxModel) {
    'use strict';

    var UserModel = KuroboxModel.extend({
        defaults: {
        	username: 'admin'
        },

        fetch: function(options) {
        },

        save: function (key, val, options) {
            this.url = 'create_user';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                param_attr: {username: 'username', password: 'password'}
            };

            KuroboxModel.prototype.save.call(this, key, val, options);
        },

        change_user: function (key, val, options) {
            this.url = 'change_user';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                param_attr: {old_username: 'old_username', old_password: 'old_password', new_username: 'new_username', new_password: 'new_password'}
            };

            KuroboxModel.prototype.save.call(this, key, val, options);
        },

        delete: function (username, options) {
            this.url = 'remove_user';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                param: {username: username}
            };

            KuroboxModel.prototype.save.call(this, options);
        },

        login_as_anonymous: function (options) {
            this.url = 'login';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                redirectLogin: false,
                param: {username: 'anonymous', password: 'anonymous'}
            };

            KuroboxModel.prototype.fetch.call(this, options);   
        },

        login: function (username, password, options) {
            this.url = 'login';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                redirectLogin: false,
                param: {username: username, password: password}
            };

            KuroboxModel.prototype.fetch.call(this, options);   
        },

        testing:function (username) {
            console.log('testomg!!!');
        },

        logout: function (username, options) {
            this.url = 'logout';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                param: {username: username}
            };

            KuroboxModel.prototype.fetch.call(this, options);
        },        

        parse: function(data) {
        }
    });

    return UserModel;
});
