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

    var AppModel = KuroboxModel.extend({
        idAttribute: 'id',
        defaults: {
            id: '',
            name: '',
            image_url: '.png',
            app_ver: '1',
            path: '/system',
            url: '',
            type:'app',
            status:'off'
        },

        fetch: function() {
        },

        save: function() {
        },

        start_app: function(id, app_type, options) {
            this.url = 'start_app';
            this.dev_opt = {
                //url: 'https://192.168.0.19/cgi-bin/syb_reqresp_cgi',
                method: 'GET',
                bypassSession: true,
                param: {app_id: id, app_type:app_type}
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        stop_app: function(id, options) {
            this.url = 'stop_app';
            this.dev_opt = {
                //url: 'https://192.168.0.19/cgi-bin/syb_reqresp_cgi',
                method: 'GET',
                bypassSession: true,
                param: {app_id: id}
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        delete: function() {
        },

        parse: function() {
        }
    });

    var AppCollection = KuroboxCollection.extend({
        model: AppModel,
        fetch: function(begin, total, type, options) {
            this.url = 'list_app';
            this.dev_opt = {
                //url: 'https://192.168.0.19/cgi-bin/syb_reqresp_cgi',
                //method: 'GET',
                bypassSession: true,
                param: {start: begin, max: total, app_type: type}
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        delete: function(id, options) {
            this.url = 'uninstall_app';
            this.dev_opt = {
                method: 'GET',
                bypassSession: true,
                param: {app_id: id}
            }

            var callback = {};
                callback.success = function(){
                    this.remove(model);
                    options.success();
                }.bind(this);
                callback.error = function(){
                    options.error();
                }.bind(this);

            var model = this.get(id);
            var param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, this.url, param, callback, this.dev_opt);
        },

        parse: function(data) {
            console.log('data >> ', data)
            AppCollection.total = data.response.total;
            console.log('data total>> ', AppCollection.total)
            return data.response.app;
        }
    });
    var AppBundle = {
        model:AppModel,
        collection:AppCollection
    }
    return AppBundle;
});