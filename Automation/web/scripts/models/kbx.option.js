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
    'models/kbx.abstract',
    'models/label_value',
], function (_, kbxGeneric, LabelValue) {

	// value-label model

	var kbxOptionListValueLabel = {};
	kbxOptionListValueLabel.model = LabelValue.model.extend({
		idAttribute: 'value',
		parse: function(data) {
			var o = {
				label: data.kbxItemLabel,
				value: data.kbxItemValue
			}
			return o;
		},
		clone: function() {
			return new kbxOptionListValueLabel.model({
				label: this.attributes.label,
				value: this.attributes.value
			})
		}
	})

	kbxOptionListValueLabel.collection = LabelValue.collection.extend({
		model: kbxOptionListValueLabel.model,
		clone: function() {
			var o = new kbxOptionListValueLabel.collection();
			this.each(function(item) {
				o.add(item.clone());
			})
			return o;
		},

		toObject: function() {
			var o = [];
			this.each(function(item) {
				o.push(item.get('value'));
			})
			return o;
		}
	})

	// model
	// !! NOTE: this will affect kbx.toggle

	var spr = kbxGeneric.prototype;
	var kbxOption = kbxGeneric.extend({
		className: 'kbx.kbxOption',
		valueLabelClass: kbxOptionListValueLabel.collection,
		defaults: {
			is_required: false,
    		label: undefined,
    		name: undefined,
    		type: undefined,
            value: new kbxOptionListValueLabel.collection(),
            value_label: '',
            description: '',
            relationship: [],
    		extra: {},
    		list: new kbxOptionListValueLabel.collection()
		},

		set_default_value: function() {
			// default min and max
			// make it single select
			this.get('extra').kbxParamMaxSize = this.get('extra').kbxParamMinSize = 1;

			// default value can be empty
			return new this.valueLabelClass();
		},

		reset_value: function() {
			this.set('value', new kbxOptionListValueLabel.collection());
		},
		
		parse: function(data) {
			var o = spr.parse.call(this, data);

			// pushing list item
			o.list = new this.valueLabelClass(o.extra.kbxParamItems, {parse: true});
			delete o.extra.kbxParamItems;

			// set value using value label class
			var _v;
			if (o.value !== undefined) {
				_v = new this.valueLabelClass();
				_.each(o.value, function(item) {
					_v.add(o.list.get(item));
				})

				// set as value
				o.value = _v;
			}

			if (o.default_value !== undefined) {
				_v = new this.valueLabelClass();
				_.each(o.default_value, function(item){
					_v.add(o.list.get(item));
				})

				// set as default value
				o.default_value = _v;
			}

			return o;
		},

		clone: function() {
			var list = this.attributes.list.clone();
			var value = this.attributes.value.clone();
			var default_value = this.attributes.default_value.clone();

			var o = spr.clone.call(this);
			o.set('list', list);
			o.set('value', value);
			o.set('default_value', default_value);
			return o;
		},

		toDisplayValue: function() {
			if (this.attributes.value.length === 1) {
         		return this.get('value').at(0).get('label');
			} else if (this.attributes.value.length > 1) {
				var labels = '';
				this.get('value').each(function(value_item, idx) {
					labels += value_item.get('label');
					if (idx < this.get('value').length) {
						labels += ', ';
					}
				}.bind(this))

				return labels;
			} else {
				return;
			}
        },

        toObject: function() {
        	var o = spr.toObject.call(this);
        	o.kbxParamCurrentValue = this.attributes.value.toObject();

        	return o;
        }
	})

	return kbxOption;

});
