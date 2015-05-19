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

// this is similar support for kbxComponents

define([
    'underscore',
    'common/components/models/kbx.time',
    'common/rule/models/rule.device.method',
    'models/rule.device',
    'common/rule/models/rule.device.param',
    'moment'
], function (_, kbxTime, RuleDeviceMethod, RuleDevice, DeviceParams) {

	var spr = kbxTime.prototype;
	var kbxDelay = kbxTime.extend({
		toDisplayValue: function() {
			// convert to time
			var m = this.generateMoment();
			if (m !== undefined) {
				var str = '';
				if (m.hour() > 0) 
					str += m.hour() + ' ' + (m.hour() > 1 ? lang.translate('hours') : lang.translate('hour')) + ' ';
				if (m.minute() > 0) 
					str += m.minute() + ' ' + (m.minute() > 1 ? lang.translate('minutes') : lang.translate('minute')) + ' ';
				if (m.second() > 0 || str == '')
					str += ' ' + m.second() + ' ' + (m.second() > 1 ? lang.translate('seconds') : lang.translate('second'));
				return str;
			}
			return;
		},

		generateMoment: function() {
			var m = spr.generateMoment.call(this)
			if (m != undefined) {
				m.second((this.get('value')%3600)%60);
			}
			return m;
		}
	})

	var DelayDevice = RuleDevice.model.extend({
		defaults: {
            'id': -291,
            'name': 'Delay',
            'icon': '&#xe62b',
		}
	})

	var DelayMethod = RuleDeviceMethod.model.extend({
		defaults: {
			id: -291,
			label: 'Duration',
			value: 1
		},
		idAttribute: null,

		initialize: function(data, options) {
			if (data == undefined) {
				this.set(this.parse());
			}
		},

  		parse: function(data) {
  			var o = {};
  			var delay_param = new kbxDelay({
                name: 'delayInSec',
                value: 1
            });

            o.device = new DelayDevice();

            if (data != undefined) {
            	if (data.kbxMethodParams.length == 1 && data.kbxMethodParams[0].kbxParamName == 'delayInSec') {
            		delay_param.set('value', data.kbxMethodParams[0].kbxParamCurrentValue);
            		o.device.set('label', data.kbxGroupLabel)
            		o.label = data.kbxMethodLabel;
            	} else {
            		console.error('Invalid kbxDelay data!! ', data)
            	}
            } else {
            	o.device.set('name', window.lang.translate('delay'));
	            o.label = window.lang.translate('duration');
            }

            o.params = o.ui_components = new DeviceParams([delay_param]);
            return o;
  		}
	});

	return DelayMethod;
});
