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
    'common/components/models/kbx.abstract',
    'common/models/label_value'
], function (_, kbxOption, KbxGeneric, LabelValue) {

	var kbxFileListValueLabel = {};
	kbxFileListValueLabel.model = LabelValue.model.extend({
		idAttribute: 'value',
		parse: function(data) {
			var o = {
				label: data.label,
				value: data.path,
				isDirectory: data.isDirectory,
				fileType: data.fileType
			}
			return o;
		},
		clone: function() {
			return new kbxFileListValueLabel.model({
				label: this.attributes.label,
				value: this.attributes.value,
				isDirectory: this.attributes.isDirectory,
				fileType: this.attributes.fileType
			})
		}
	})

	kbxFileListValueLabel.collection = LabelValue.collection.extend({
		model: kbxFileListValueLabel.model,
		clone: function() {
			var o = new kbxFileListValueLabel.collection();
			this.each(function(item) {
				o.add(item.clone());
			})
			return o;
		},

		toObject: function() {
			var o = [];
			this.each(function(item) {
				o.push({
					label: item.get('label'),
					path: item.get('value'),
					isDirectory: item.get('isDirectory'),
					fileType: item.get('fileType')
				});
			})
			return o;
		}
	})

	// similar to option, just that they don't have
	// list provided to user instead

	// used file is value
	var spr = kbxOption.prototype;
	var kbxInputText = kbxOption.extend({
		className: 'kbx.File',
		valueLabelClass: kbxFileListValueLabel.collection,

		defaults: {
			is_required: false,
    		label: undefined,
    		name: undefined,
    		type: undefined,
            value: new kbxFileListValueLabel.collection(),
            value_label: '',
            description: '',
            relationship: [],
    		extra: {},
    		list: new kbxFileListValueLabel.collection()
		},
		
        parse: function(data) {
        	//NOTE: due to current item is not the item list

			var o = KbxGeneric.prototype.parse.call(this, data);

			// pushing list item
			o.list = new this.valueLabelClass(o.extra.kbxParamItems, {parse: true});
			delete o.extra.kbxParamItems;

			// set value using value label class
			var _v;
			if (o.value !== undefined) {
				_v = new this.valueLabelClass();
				_.each(o.value, function(item) {
					_v.add(item, {parse: true});
				})

				// set as value
				o.value = _v;
			}

			if (o.default_value !== undefined) {
				_v = new this.valueLabelClass();
				_.each(o.default_value, function(item){
					_v.add(item, {parse: true});
				})

				// set as default value
				o.default_value = _v;
			}

			return o;
		},
	})

	return kbxInputText;

});