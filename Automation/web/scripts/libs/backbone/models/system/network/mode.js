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
    'libs/backbone/models/kurobox-model'
], function (_, KuroboxModel) {
    'use strict';

    var NetworkModeModel = KuroboxModel.extend({
        fetch: function(options) {
        	this.url = 'get_network_mode';
        	this.dev_opt = {
        		bypassSession: true,
                //url: 'json/network/get-network-mode.json',
        		method: 'GET'
        	}

        	KuroboxModel.prototype.fetch.apply(this, arguments);
        },

        save: function(connection, options) {
            console.log('set_network_mode!!!');
            console.log(connection);
        	this.url = 'set_network_mode';
        	this.dev_opt = {
        		bypassSession: true,
        		method: 'GET',
                param:{mode:connection}
        	}

            this.set('mode', connection);
            var param = {mode:connection};
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        },

        parse: function(data) {
           return {
                lan: data.response.status.lan,
                wifi: data.response.status.wifi,
                hotspot: data.response.status.hotspot,
                mode: data.response.status.mode
            }
        }
    });

    return NetworkModeModel;
});
