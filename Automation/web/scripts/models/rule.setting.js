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

define([
    'underscore',
    'backbone',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'models/rule.device',
    'utils/common.utils',
    'libs/utils/color',
    'libs/utils/obj'
], function (_, Backbone, KuroboxModel, KuroboxCollection, RuleDevice, CommonUtils) {
    'use strict';

    var RuleSettingModel = {};
    var utils = new CommonUtils();
    var create_config_arg_collection = function() {
        return new RuleSettingModel.config_args();
    };

    // as user configuration
    RuleSettingModel.config_method = KuroboxModel.extend({
        defaults: {
            label: '',
            func: '',   // methodId
            hasEvent: false,
            editor_value_display: undefined,    // methodDetail
            status: 'ok',
            args: undefined
        },
        idAttribute: 'func',
        initialize: function(data, options) {
            if (!data.args && !data.ui_args) {
                data.args = new RuleSettingModel.config_args();
                data.ui_args = new RuleSettingModel.config_args();
            } else {
                data.args = new RuleSettingModel.config_args(data.args);
                data.ui_args = new RuleSettingModel.config_args(data.ui_args);
            }
            this.set(data);
        }
    }),

    RuleSettingModel.config_methods = KuroboxCollection.extend({
        model: RuleSettingModel.config_method,
        toObject: function() {
            var o, m;
            o = [];
            this.each(function(config) {
                // m = _.clone(config.attributes);
                m = {
                    kbxMethodId: config.attributes.func
                }
                m.kbxMethodParams = config.attributes.args.toObject();
                o.push(m);
            }.bind(this))
            return _.flatten(o);
        }
    })

    // consist of device method
    RuleSettingModel.device_method = KuroboxModel.extend({
    	defaults: {
            hasEvent: false,
    		label: '',
    		func: '',
    		args: [],
            value_display: undefined,
            editor_value_display: undefined,
    	},
        idAttribute: 'func',
        create_config_method: function() {
            return new RuleSettingModel.config_method({
                label: this.attributes.label,
                func: this.attributes.func,
                hasEvent: this.attributes.hasEvent,
                editor_value_display: this.attributes.editor_value_display
            })
        }
    });

    // as device method's collection
    RuleSettingModel.device_methods = KuroboxCollection.extend({
    	model: RuleSettingModel.device_method,
        parse: function(data) {
            var o = [], m;
            _.each(data, function(method, index) {
                m = {
                    label: method.kbxMethodLabel,
                    func: method.kbxMethodId,
                    hasEvent: method.kbxMethodHasEvent,
                    editor_value_display: method.methodDetail,
                    args: new RuleSettingModel.dev_args(method.kbxMethodParams, {parse: true})
                }
                _.extend(m, this.parse_method(method.kbxMethodParams))

                o.push(m);
            }.bind(this));
            return o;
        },

        parse_method: function(data) {
            var o = {};
            o.physical_args_length = 0;
            o.args = new RuleSettingModel.dev_args();
            var m, pys = [], hid = [];
            _.each(data, function(item, index) {
                m = new o.args.model(item, {parse: true});
                if (m.get('component_type') !== 'kbxHidden') {
                    // not hidden
                    o.physical_args_length ++;
                }
                o.args.add(m);
            }.bind(this))

            return o;
        }
    })

    // each method has arguments
    RuleSettingModel.dev_arg = KuroboxModel.extend({
    	defaults: {
            is_required: false,
    		label: '',
    		name: '',
    		component_type: '',
            value: '',
    		component_config: {}
    	},
        idAttribute: 'name',
/*
        set: function(key, val, options) {
            var type = this.get('component_type');
            var config = this.get('component_config');
            if (typeof key === 'string') {
                if (key === 'value') {
                    val = this._set_value(val, type, config);
                }
            } else {
                if (key['value'] !== undefined) {
                    key['value'] = this._set_value(key['value'], key.component_type || type, key.component_config || config);
                }
            }
            console.log('set result', key, val, options)
            KuroboxModel.prototype.set.call(this, key, val, options);
        },

        _set_value: function(value, type, config) {
            switch (type) {
                case 'kbxDateTimeRange':
                console.log('----- value', value)
                if (config.kbxParamDelimiter != undefined) console.warn('[kbxDateTime] Unable to get delimiter');
                var del = config.kbxParamDelimiter || '-';
                var tmp = value.split(del);
                value = utils.dateToUnix(tmp[0])+del+utils.dateToUnix(tmp[1]);
                console.log('-- parse kbx time range', value)
                break;
            }

            return value;
        },*/

        parse: function(data) {
            var o = {
                label: data.kbxParamLabel,
                name: data.kbxParamName,
                is_required: data.kbxParamIsRequired,
                component_type: data.kbxParamType,
                value: data.kbxParamCurrentValue,
                // component_config: data.argConfig
            }

            o.component_config = ObjUtil.clone(data);
            delete o.component_config.kbxParamLabel;
            delete o.component_config.kbxParamName;
            delete o.component_config.kbxParamType;
            delete o.component_config.kbxParamIsRequired;
            delete o.component_config.kbxParamCurrentValue;

            // extra parsing
            console.log('component_type', o.label, o.component_type)
            switch (o.component_type) {
                case 'kbxBoolean':
                o.value_label = (data.kbxParamCurrentValue) ? data.kbxParamTrueLabel : data.kbxParamFalseLabel;
                break;

                case 'kbxColor':
                // parse to hex
                if (typeof o.component_config.kbxParamDefaultValue !== 'undefined') {
                    var del = o.component_config.kbxParamDelimiter || ',';
                    var rgb = o.component_config.kbxParamDefaultValue.split(del);
                    o.component_config.kbxParamDefaultValue = ColorUtil.rgb2hex(parseInt(rgb[0]), parseInt(rgb[1]), parseInt(rgb[2]));
                }

                /*
                case 'kbxDateTimeRange':
                var com_utils = new CommonUtils();
                var apiDelimiter = o.component_config.kbxParamDelimiter
                if (o.component_config.kbxParamDelimiter === '-') {

                    // use ' - '
                    o.component_config.kbxParamDelimiter = ' - ';

                }

                if (o.component_config.kbxParamDefaultValue != undefined) {
                    // parse unix timestamp to date
                    var _tmp = o.component_config.kbxParamDefaultValue = o.component_config.kbxParamDefaultValue.split(apiDelimiter);
                    o.component_config.kbxParamDefaultValue = com_utils.unixToDateString(_tmp[0])+o.component_config.kbxParamDelimiter+com_utils.unixToDateString(_tmp[1]);
                }
                break;*/
            }

            return o;
        }
    });

    // as arguments collection
    RuleSettingModel.dev_args = KuroboxCollection.extend({
        model: RuleSettingModel.dev_arg,
        merge: function(config_args) {
            config_args.each(function(arg) {
                if (this.get(arg.get('name')) !== undefined) {
                    var val;
                    switch (this.get(arg.get('name')).get('component_type')) {
                        case 'kbxColor':
                        // parse rgb to hex
                        var del = this.get(arg.get('name').get('component_type')).kbxParamDelimiter || ',';
                        val = arg.get('value').split(del);
                        val = ColorUtil.rgb2hex(parseInt(val[0]), parseInt(val[1]), parseInt(val[2]));
                        break;

                        default:
                        val = arg.get('value');
                        break;
                    }
                    this.get(arg.get('name')).get('component_config').user_value = val;
                } else {
                    console.warn('Unable to find arg name \''+arg.get('name')+'\'');
                }
            }.bind(this));

            console.log('final', this.models)
        }
    })

    RuleSettingModel.config_args = KuroboxCollection.extend({
        model: RuleSettingModel.dev_arg,
        toObject: function() {
            var o, m;
            o = [];
            this.each(function(arg) {
                console.log('test arg', arg.attributes.component_type);
                // m = _.clone(arg.attributes);
                m = {
                    kbxParamName: arg.attributes.name,
                    kbxParamCurrentValue: arg.attributes.value
                }
                o.push(m);
            }.bind(this))
            return o;
        }
    });
    
    // use as core
    RuleSettingModel.core = KuroboxModel.extend({
        defaults: {
            name: '',
            icon: '',
            setting: []
        },
        fetch: function(id, section, options) {
            this.url = 'list_methods';
            this.dev_opt = {
                method: 'GET',
                param: {
                    groupId: id,
                    section: section
                }
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            var result = {};
            result.name = data.response.group.kbxGroupLabel || data.response.group.kbxGroupName || '';
            result.icon = data.response.group.kbxGroupIcon;
            result.setting = new RuleSettingModel.device_methods(data.response.data, {parse: true});
            return result;
        }
    });

    return RuleSettingModel;
});
