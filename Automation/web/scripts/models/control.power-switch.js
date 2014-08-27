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
    'libs/backbone/models/kurobox-collection',
], function (_, KuroboxModel, KuroboxCollection) {
	// to validate model id
    var validate = function(model) {
        if (model.get('id') === undefined) throw 'Undefined device ID';
    }

    // default param
    var defaultParam = {
        module: 'device_manager.power_strip_controller',
    }

    var PowerSwitch = {};

	PowerSwitch.model = KuroboxModel.extend({
        get_capabilities: function(options) {
            this.url = 'get_capabilities';
            this.dev_opt = {
                param: _.extend({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        get_status: function(options) {
            this.parse = this._parse_status;
            this.url = 'get_status';
            this.dev_opt = {
                param: _.extend({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        _parse_status: function(data) {
            console.log('data', data)
            return data.response.status;
        },

        power_on: function(Index, options) {
            this.url = 'set_on';
            this.dev_opt = {
                param: _.extend({
                    pairedDeviceId: this.get('id'), index: Index
                }, defaultParam),
                method: 'GET'
            }
            this._plainAPICall(options);
        },

        power_off: function(Index, options) {
            this.url = 'set_off';
            this.dev_opt = {
                param: _.extend({
                    pairedDeviceId: this.get('id'), index: Index
                }, defaultParam),
                method: 'GET'
            }
            this._plainAPICall(options);
        },

        _plainAPICall: function(options) {
            // set custom param by developer
            var param = this._handleParam(this.dev_opt);

            console.log('api call plain stylo: ', this.url, param);
             // call the server
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        },
	});

	PowerSwitch.collection = KuroboxCollection.extend({
    	model: PowerSwitch.model,
    	
    });

    return PowerSwitch;
});