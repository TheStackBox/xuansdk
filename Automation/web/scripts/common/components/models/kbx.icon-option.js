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
    'common/components/models/kbx.option',
    'libs/backbone/models/kurobox-model'
], function (_, kbxOption, KuroboxModel) {

	var fontSettingModel = KuroboxModel.extend({
		generate_fontloader_setting: function() {
			return [
				this.attributes.family,
				this.attributes.srcs,
				this.attributes.style
			]
		},

		clone: function() {
			return new this.constructor({
				family: this.attributes.family,
				srcs: this.attributes.srcs.concat(),
				style: this.attributes.style,
				color: this.attributes.color
			})
		}
	})

	// value-label model
	var kbxIconOptionItem = {};
	kbxIconOptionItem.model = kbxOption.LABEL_VALUE.model.extend({
		fn: kbxOption.LABEL_VALUE.model.prototype,
		parse: function(data) {
			var o = {
				label: data.kbxItemLabel,
				value: data.kbxItemValue,
				icon: data.kbxItemIcon,
				font: new fontSettingModel({
					family: data.kbxItemIconFamily,
					srcs: data.kbxItemIconPaths.concat(),
					style: data.kbxItemIconStyle,
					color: data.kbxItemIconColor,
				})
			}
			return o;
		},
		clone: function() {
			return new kbxIconOptionItem.model({
				label: this.attributes.label,
				value: this.attributes.value,
				icon: this.attributes.icon,
				font: this.attributes.font.clone()
			})
		}
	})

	kbxIconOptionItem.collection = kbxOption.LABEL_VALUE.collection.extend({
		fn: kbxOption.LABEL_VALUE.collection.prototype,
		model: kbxIconOptionItem.model,
		clone: function() {
			var o = new kbxIconOptionItem.collection();
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

	var kbxIconOption = kbxOption.extend({
		fn: kbxOption.prototype,
		className: 'kbx.kbxOptionWithIcon',
		valueLabelClass: kbxIconOptionItem.collection,
		defaults: {
			is_required: false,
    		label: undefined,
    		name: undefined,
    		type: undefined,
            value: new kbxIconOptionItem.collection(),
            value_label: '',
            description: '',
            relationship: [],
    		extra: {},
    		list: new kbxIconOptionItem.collection()
		},
		toDisplayValue: function() {
			console.warn('This will show no icon at display. Use proper item renderer');
			return this.fn.toDisplayValue.apply(this);
		}
	}, {
		VALUE_LABEL: kbxIconOptionItem,
	})

	return kbxIconOption;

});
