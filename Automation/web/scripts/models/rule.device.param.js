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

define(function (require) {
	'use strict';

    // global import
    require('libs/utils/obj');

    // class import
    var _ = require('underscore'),
        KuroboxModel = require('libs/backbone/models/kurobox-model'),
        KuroboxCollection = require('libs/backbone/models/kurobox-collection'),
        GenericKbx = require('models/kbx.abstract'),
        UnsupportedKbx = require('models/kbx.unsupported');

    // component class import
    // old type
    var component_store = {};
    component_store['kbxBoolean'] = require('models/kbx.toggle');
    component_store['kbxRange'] = require('models/kbx.slider');
    component_store['kbxHidden'] = require('models/kbx.hidden');

    // new time
    component_store['kbxTextInput'] = require('models/kbx.input-text');
    component_store['kbxToggle'] = component_store['kbxBoolean'];
    component_store['kbxOption'] = require('models/kbx.option');
    component_store['kbxTextArea'] = require('models/kbx.text-area');
    component_store['kbxSlider'] = component_store['kbxRange'];
    component_store['kbxTime'] = require('models/kbx.time');
    component_store['kbxColor'] = require('models/kbx.color');

	var DeviceMethodParams = KuroboxCollection.extend({
		// model: DeviceMethodParam.model,
        parse: function(data) {
            var o = [];
            var constructor, comp;
            _.each(data, function(param) {
                constructor = eval('component_store[\''+param.kbxParamCom+'\']');
                if (param.kbxParamCom !== undefined && constructor !== undefined) {
                    try {
                        comp = new constructor(param, {parse: true});
                    } catch (e) {
                        comp = new GenericKbx(param, {parse: true});
                        console.log('Component error', param.kbxParamCom);
                    }
                } else {
                    console.warn(param.kbxParamName +' does not have component. Use generic');
                    comp = new UnsupportedKbx(param, {parse: true});
                }
                // if (comp === undefined) comp = new GenericKbx(param, {parse: true});
                o.push(comp);
            })
            return o;
        },

        clone: function() {
            var o = new DeviceMethodParams();
            this.each(function(param) {
                console.log('cloning', param.get('name'));
                o.add(param.clone());
            })
            return o;
        },

        toObject: function() {
            var o = [];
            this.each(function(param) {
                o.push(param.toObject());
            })

            return o;
        },

        get_total_required_parameter: function() {
            if (this._require_params === undefined) {
                this._validate_parameter_required();
            }

            return this._require_params;
        },

        get_total_optional_parameter: function() {
            if (this._optional_params === undefined) {
                this._validate_parameter_required();
            }
            
            return this._optional_params;
        },

        _validate_parameter_required: function() {
            this._require_params = 0;
            this._optional_params = 0;
            this.each(function(param) {
                if (param.get('is_required') === true) {
                    this._require_params ++;
                } else {
                    this._optional_params ++;
                }
            }.bind(this))
        }
	})

    return DeviceMethodParams;
});
