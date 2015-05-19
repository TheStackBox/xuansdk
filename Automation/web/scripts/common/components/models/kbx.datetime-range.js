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
    'common/components/models/kbx.datetime',
    'moment'
], function (_, kbxGeneric, kbxDateTime) {
	var spr = kbxGeneric.prototype;
	var kbxInputText = kbxGeneric.extend({
		className: 'kbx.DateTimeRange',

		// composition of kbxDateTime

		parse: function(data) {
			var o = spr.parse.call(this, data);

			if (data.kbxParamCurrentValue != undefined) {
				o.value = {
					startDateTime: new kbxDateTime({value: data.kbxParamCurrentValue.startDateTime}),
					endDateTime: new kbxDateTime({value: data.kbxParamCurrentValue.endDateTime}),
				}
			}

			if (data.kbxParamDefaultValue != undefined) {
				o.default_value = {
					startDateTime: new kbxDateTime({value: data.kbxParamDefaultValue.startDateTime}),
					endDateTime: new kbxDateTime({value: data.kbxParamDefaultValue.endDateTime}),
				}
			}
			return o;
		},

		toDisplayValue: function() {
			if (this.get('value') != undefined) {
				var start = this.get('value').startDateTime.generateMoment();
				var end;
				if (this.get('value').endDateTime != undefined) {
					end = this.get('value').endDateTime.generateMoment();
				}

				var str = start.format('YYYY-MM-DD hh:mm A');
				if (end !== undefined) {
					str += ' > ' + end.format('YYYY-MM-DD hh:mm A');
				}
				return str;
			}
			return;
		},

		toObject: function() {
			var o = spr.toObject.call(this)
            o.kbxParamCurrentValue = {
            	startDateTime: this.attributes.value.startDateTime.get('value'),
            }

            if (this.attributes.value.endDateTime != undefined && this.attributes.value.endDateTime.get('value') != undefined) {
            	o.kbxParamCurrentValue.endDateTime = this.attributes.value.endDateTime.get('value')
            } else {
            	o.kbxParamCurrentValue.endDateTime = o.kbxParamCurrentValue.startDateTime;
            }

            return o;
		},
	})

	return kbxInputText;

});
