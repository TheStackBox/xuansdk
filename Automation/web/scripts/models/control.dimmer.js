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
        module: 'device_manager.dimmer_controller',
    }

	var HueControlModel = KuroboxModel.extend({
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
            //this.parse = this._parse_status;
            this.url = 'get_status';
            this.dev_opt = {
                param: _.extend({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

		power_on: function(options) {
			this._writeAndSave('set_on', undefined, options);
		},

		power_off: function(options) {
			this._writeAndSave('set_off', undefined, options);
		},

		dim: function(brightness, options) {
			this._writeAndSave('set_dim_level', {level: brightness}, options);
		},

		_writeAndSave: function(method, value_obj, options) {
			validate(this);

			// save
			if (value_obj !== undefined) {
				this.set(value_obj);
			} else {
				value_obj = {};
			}

			// inject pairedDeviceId
			value_obj.pairedDeviceId = this.get('id');

			this.url = method;
			this.dev_opt = {
				param: _.extend(value_obj, defaultParam),
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
        }
	});

	return HueControlModel;
});