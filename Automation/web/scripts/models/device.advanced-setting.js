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
    'models/device.advanced-setting.setting',
], function (_, KuroboxModel, Setting) {
	'use strict';
    // default param
    var defaultParam = {}

	// to validate model id
    var validate = function(model, extra_param) {
        if (model.get('id') === undefined) throw 'Undefined device ID';
        var p = _.extend({pairedDeviceId: model.get('id'), module:'device_manager'}, defaultParam);
        if (extra_param) p = _.extend(extra_param, p);
        return p;
    }

	var DeviceSetting = KuroboxModel.extend({
		defaults: {
			'settings': new Setting.collection()
		},

		fetch: function(options) {
			var param = validate(this);
			this.url = 'get_advanced_control_list';
			this.dev_opt = {
				// url: 'json/example.advanced_setting.json',
				method: 'GET',
				param: param
			}
			KuroboxModel.prototype.fetch.call(this, options);
		},

		parse: function(data) {
			var resp = data.response;
			var o = {}
			o.settings = new Setting.collection(resp.methodList, {parse:true});

			return o;
		},

		_plainAPICall: function(options) {
            // set custom param by developer
            var param = this._handleParam(this.dev_opt);

             // call the server
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        }
	});

	return DeviceSetting;
});