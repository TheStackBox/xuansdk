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

	var list = {}
	list.model = KuroboxModel.extend({
		idAttribute: 'mode'
	});

	list.collection = KuroboxCollection.extend({
		model: list.model
	})

	// to validate model id
    var validate = function(model) {
        if (model.get('id') === undefined) throw 'Undefined device ID';
    }
    // default param
    var defaultParam = {
        module: 'device_manager.thermostat_controller',
    }

	var ThermostatModel = KuroboxModel.extend({
		get_capabilities: function(options) {
			this.parse = this._parse_switch_capabilities;
			this.url = 'get_capabilities';
			this.dev_opt = {
				url: 'json/example.get_capabilities.json',
				param: _.extend({
					pairedDeviceId: this.get('id')
				}, defaultParam),
				method: 'GET'
			}
			KuroboxModel.prototype.fetch.call(this, options);
		},

		get_status: function(options) {
			this.parse = this._parse_switch_status;
			this.url = 'get_status';
			this.dev_opt = {
				url: 'json/example.termostat.json',
				param: _.extend({
					pairedDeviceId: this.get('id')
				}, defaultParam),
				method: 'GET'
			}
			KuroboxModel.prototype.fetch.call(this, options);
		},

		temp_mode: function(mode, options) {
			this._writeAndSave('set_mode', {mode: mode}, options);
		},

		fan_mode: function(fanMode, options) {
			this._writeAndSave('set_fan_mode', {fanMode: fanMode}, options);
		},

		temperature: function(target_temp, mode, options) {
			this._writeAndSave('set_setpoint', {target: target_temp, mode:mode}, options);
			delete this.attributes.target;
			this.set('targetTermperature', target_temp)
		},

		_parse_switch_status: function(data) {
			return {
				currentTermperature: data.response.status.currentTermperature,
				targetTermperature: data.response.status.targetTermperature,
				unit: data.response.status.unitDetails.unit == 1 ? '&deg;F' : '&deg;C',
				showTargetTermperature: data.response.status.showTargetTermperature,
				mode: data.response.status.mode,
				fanMode: data.response.status.fanMode,
				tempModeList: new list.collection(data.response.status.modeList),
				fanModeList: new list.collection(data.response.status.fanModeList)
			}
		},

		_parse_switch_capabilities: function(data) {
			return data.response;
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

	return ThermostatModel;
});