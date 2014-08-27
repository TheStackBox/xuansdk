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
    'libs/backbone/models/kurobox-model',
], function (_, KuroboxModel) {

	var kbxGeneric = KuroboxModel.extend({
        className: 'kbx.Generic',
        // childClass: this,
		defaults: {
			is_required: false,
    		label: undefined,
    		name: undefined,
    		type: undefined,
            value: undefined,
            value_label: '',
            description: '',
            relationship: [],
    		extra: {}
		},
        idAttribute: 'name',
        initialize: function() {
            if (this.get('default_value') === undefined) {
                if (this.set_default_value !== undefined) {
                    this.set('default_value', this.set_default_value());
                } else {
                    this.set('default_value', this.default_value || undefined);
                }
            }
        },

        reset_value: function() {
            this.set('value', undefined);
        },

		parse: function(data) {
            console.warn('TODO: separate default value and value')
			var o = {
                label: data.kbxParamLabel || data.kbxParamName,
                name: data.kbxParamName,
                is_required: data.kbxParamIsRequired,
                type: data.kbxParamCom,
                value: data.kbxParamCurrentValue,
                description: data.kbxParamDesc,
                default_value: data.kbxParamDefaultValue
            }

            o.extra = ObjUtil.clone(data);
            delete o.extra.kbxParamLabel;
            delete o.extra.kbxParamName;
            delete o.extra.kbxParamCom;
            delete o.extra.kbxParamIsRequired;
            delete o.extra.kbxParamCurrentValue;

            // parse value label
            /*
            switch (o.type) {
                case 'kbxBoolean':
                o.value_label = (data.kbxParamCurrentValue) ? data.kbxParamTrueLabel : data.kbxParamFalseLabel;
                break;
            }*/

            return o;
		},
        toDisplayValue: function() {
            return this.get('value');
        },

        clone: function() {
            var o = new this.__proto__.constructor({
                label: this.attributes.label,
                name: this.attributes.name,
                is_required: this.attributes.is_required,
                type: this.attributes.type,
                value: this.attributes.value,
                default_value: this.attributes.default_value,
                description: this.attributes.description
            });
            o.set('extra', ObjUtil.clone(this.attributes.extra)); 
            return o;
        },

        toObject: function() {
            var o = {
                kbxParamName: this.attributes.name,
                kbxParamCurrentValue: this.attributes.value || null
            }

            return o;
        }
	})

	return kbxGeneric;

});