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

// this is similar support for kbxComponents

define([
    'underscore',
    'models/kbx.option',
    'models/label_value',
], function (_, kbxOption, LabelValue) {

	// model

	var spr = kbxOption.prototype;
	var kbxToggle = kbxOption.extend({
		className: 'kbx.kbxToogle',
		initialize: function(attr, options) {
			spr.initialize.call(this, arguments);

			// for making the list to select as one
			this.get('extra').kbxParamMaxSize = 1;
			this.get('extra').kbxParamMinSize = 1;
			this.get('extra').kbxParamMultiSelect = false;

			// manipulate list
			var list = this.get('list')
			if (list.length <= 0) {
				list.add([
					{label: 'Yes', value: true},
					{label: 'No', value: false}
				])
			}

			// manipulate value
			var _value = this.get('value');
			if (_value === undefined || typeof _value === 'boolean') {
				this.set('value', new this.valueLabelClass());
				if (_value === undefined) {
					this.get('value').add(list.get(false));
				} else {
					this.get('value').add(list.get(_value));
				}
			}
		},

		parse: function(data) {
			// wrap value with array
			if (data.kbxParamCurrentValue !== undefined) data.kbxParamCurrentValue = [data.kbxParamCurrentValue];

			// manipulate true and false item into a list
			// so that can be used by option component
			data.kbxParamItems = [
				{
					kbxItemLabel: data.kbxParamTrueLabel || 'Yes',
					kbxItemValue: data.kbxParamTrueValue || true
				},
				{
					kbxItemLabel: data.kbxParamFalseLabel || 'No',
					kbxItemValue: data.kbxParamFalseValue || false
				}
			]

			delete data.kbxParamTrueLabel;
			delete data.kbxParamTrueValue;
			delete data.kbxParamFalseLabel;
			delete data.kbxParamFalseValue;

			// manipulate default value
			data.kbxParamDefaultValue = [data.kbxParamDefaultValue || data.kbxParamFalseValue || false];

			// parse
			return spr.parse.call(this, data);
		},

		toObject: function() {
			var o = spr.toObject.call(this);

			// reassign value from list to single item (string)
			o.kbxParamCurrentValue = this.get('value').at(0).get('value');

			return o;
		}

	})

	return kbxToggle;

});