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

define(function (require) {
	'use strict';

    // global import
    require('libs/utils/obj');

    // class import
    var _ = require('underscore'),
        KuroboxModel = require('libs/backbone/models/kurobox-model'),
        KuroboxCollection = require('libs/backbone/models/kurobox-collection'),
        GenericKbx = require('common/components/models/kbx.abstract'),
        UnsupportedKbx = require('common/components/models/kbx.unsupported');

    // component class import
    // old type
    var component_store = {};
    component_store['kbxBoolean'] = require('common/components/models/kbx.toggle');
    component_store['kbxRange'] = require('common/components/models/kbx.slider');
    component_store['kbxHidden'] = require('common/components/models/kbx.hidden');

    // new time
    component_store['kbxTextInput'] = require('common/components/models/kbx.input-text');
    component_store['kbxToggle'] = component_store['kbxBoolean'];
    component_store['kbxOption'] = require('common/components/models/kbx.option');
    component_store['kbxTextArea'] = require('common/components/models/kbx.text-area');
    component_store['kbxSlider'] = component_store['kbxRange'];
    component_store['kbxTime'] = require('common/components/models/kbx.time');
    component_store['kbxColor'] = require('common/components/models/kbx.color');
    component_store['kbxHSBColor'] = require('common/components/models/kbx.color.hsb');
    component_store['kbxFiles'] = require('common/components/models/kbx.file');
    component_store['kbxDateTime'] = require('common/components/models/kbx.datetime');
    component_store['kbxDateTimeRange'] = require('common/components/models/kbx.datetime-range');
    component_store['kbxTimeRange'] = require('common/components/models/kbx.time-range');
    component_store['kbxOption.kbxDayOfWeek'] = require('common/components/models/kbx.weekdays');
    component_store['kbxOption.kbxOptionWithIcon'] = require('common/components/models/kbx.icon-option');

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
                        console.error('Component error ' + param.kbxParamCom);
                        console.error(e)
                    }
                } else {
                    console.warn(param.kbxParamName +' does not have component, '+param.kbxParamCom+'. Use generic');
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
