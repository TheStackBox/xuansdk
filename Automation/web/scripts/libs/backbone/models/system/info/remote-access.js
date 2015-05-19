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
    'libs/backbone/models/kurobox-model'
], function (_, KuroboxModel) {
    'use strict';

    var model = KuroboxModel.extend({
        defaults: {
            access: false,
            user: ''
        },

        fetch: function(options) {
            this.url = 'get_remote_access';
            this.dev_opt = {
                //url: 'json/example.get_remote_access.json',
                bypassSession: true,
                method: 'GET',
                param:{}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function(access, user, options) {
            this.url = 'set_remote_access';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET'
            };

            if(user){
                this.dev_opt.param = {access:access, user:user};
            }else{
                this.dev_opt.param = {access:access};
            }

            KuroboxModel.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            return {
                access: (data.response.access === true),
                user: data.response.user
            };
        }
    });

    return model;
});
