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
    'common/components/models/kbx.abstract',
    'common/components/models/kbx.time',
    'moment'
], function (_, kbxGeneric, kbxTime) {
	var spr = kbxGeneric.prototype;
	var kbxInputText = kbxGeneric.extend({
		className: 'kbx.TimeRange',

		// composition of kbxTime

		parse: function(data) {
			var o = spr.parse.call(this, data);

			if (data.kbxParamCurrentValue != undefined) {
				o.value = {
					startTime: new kbxTime({value: data.kbxParamCurrentValue.startTime}),
					endTime: new kbxTime({value: data.kbxParamCurrentValue.endTime}),
				}
			}

			if (data.kbxParamDefaultValue != undefined) {
				o.default_value = {
					startTime: new kbxTime({value: data.kbxParamDefaultValue.startTime}),
					endTime: new kbxTime({value: data.kbxParamDefaultValue.endTime}),
				}
			}
			return o;
		},

		toDisplayValue: function() {
			if (this.get('value') != undefined) {
				var start = this.get('value').startTime.generateMoment();
				var end, bubbleDay = false;
				if (this.get('value').endTime != undefined) {
					end = this.get('value').endTime.generateMoment();
					bubbleDay = (end.diff(start) < 0);
				}
				var str = start.format('hh:mm A');
				if (end !== undefined) {
					str += ' - ' + end.format('hh:mm A');
				}
				if (bubbleDay) {
					str += ' ('+lang.translate('next_day')+')';
				}
				return str;
			}
			return;
		},

		toObject: function() {
			var o = spr.toObject.call(this)
            o.kbxParamCurrentValue = {
            	startTime: this.attributes.value.startTime.get('value'),
            }

            if (this.attributes.value.endTime != undefined && this.attributes.value.endTime.get('value') != undefined) {
            	o.kbxParamCurrentValue.endTime = this.attributes.value.endTime.get('value')
            } else {
            	o.kbxParamCurrentValue.endTime = o.kbxParamCurrentValue.startTime;
            }

            return o;
		},
	})

	return kbxInputText;

});
