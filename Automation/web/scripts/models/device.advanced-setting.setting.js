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
    'models/rule.device.method',
    'models/rule.device.param'
], function (_, DeviceMethod, DeviceParams) {
	'use strict';

	var spr = DeviceMethod.prototype;
	var DeviceSetting = {};
	DeviceSetting.model = DeviceMethod.model.extend({
        className: 'DeviceSettingModel',
		parse: function(data) {
            var params = new DeviceParams(data.kbxMethodParams, {parse: true});

            // reference default value as value
            params.each(function(param) {
                if (param.get('default_value') != undefined) {
                    param.set('value', param.get('default_value'));
                }
            })

			var o = {
				label: data.kbxMethodLabel || data.kbxMethodName,
                id: data.kbxMethodId,
                description: data.kbxMethodDesc,
                params: params,
                ui_components: new DeviceParams(), // as reference only,
                status: data.statusCode
			}

			// parse ui components
            _.each(data.kbxMethodParams, function(param) {
                if (param.kbxParamCom !== undefined && param.kbxParamCom !== 'kbxHidden') {
                    o.ui_components.add( o.params.get(param.kbxParamName) );
                }
            })

    		return o;
		},

        save: function(pairedDeviceId, options) {
            this.url = 'set_advanced_setting';
            this.dev_opt = {
                method: 'POST',
                param: {
                    module: 'device_manager',
                    kbxMethodId: this.id,
                    kbxMethodParam: JSON.stringify(this.attributes.params.toObject())
                },
                //module=device_manager&method=set_advanced_setting&pairedDeviceId=1&kbxMethodId=185&kbxMethodParam=[{pairedDeviceId:31},{foo:'bar'}]
            }
            console.log('--- sampling param', this.dev_opt);
            this._plainAPICall(options);
        },

        clone: function() {
            var o = new DeviceSetting.model({
                label: this.attributes.label,
                id: this.attributes.id,
                description: this.attributes.description,
                params: this.attributes.params.clone(),
                ui_components: new DeviceParams(),
            })

            o.get('params').each(function(param) {
                if (param.get('type') !== undefined && param.get('type') !== 'kbxHidden') {
                    o.get('ui_components').add( param );
                }
            })

            return o;
        },

        _plainAPICall: function(options) {
            // set custom param by developer
            var param = this._handleParam(this.dev_opt);

             // call the server
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        }
	})

    DeviceSetting.collection = DeviceMethod.collection.extend({
        model: DeviceSetting.model
    })

	return DeviceSetting;
});