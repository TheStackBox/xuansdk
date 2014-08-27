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
        module: 'device_manager.ip_camera_controller',
    }
    var spr = KuroboxModel.prototype;
    var IPCamera = KuroboxModel.extend({

    	fetch: function(options) {
    		this._retrieveData('get_camera_stream_configuration', this._parse_camera_config, options);
    	},

    	_parse_camera_config: function(data) {
    		if (typeof data.response.streamConfiguration === 'undefined') throw 'Unable to parse camera configuration';
    		
    		return {
    			stream_config: data.response.streamConfiguration
    		};
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

		_retrieveData: function(method, parser, options, param) {
			validate(this);

			if (param === undefined) {
				param = {};
			}

			this.parse = parser;
			this.url = method;

			// inject pairedDeviceId
			param.pairedDeviceId = this.get('id');

			this.dev_opt = {
				param: _.extend(param, defaultParam),
				method: 'GET'
			}
			KuroboxModel.prototype.fetch.call(this, options);
		},

		_plainAPICall: function(options) {
            // set custom param by developer
            var param = this._handleParam(this.dev_opt);

            console.log('api call plain stylo: ', this.url, param);
             // call the server
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        }
	});

	return IPCamera;
});