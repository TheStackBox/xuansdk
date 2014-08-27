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

define([
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'models/rule.device'
], function (_, KuroboxModel, KuroboxCollection, RuleDevice) {
    'use strict';
    var Device = {};

    var emptyRuleDevices = function() {
        return new RuleDevice.collection();
    }

    var _parseDeviceRule = function(rules, allowOverriding) {
        allowOverriding = allowOverriding || false;
        var r = new RuleDevice.collection();
        var okToSet = false;
        var methodId;
        _.each(rules, function(method, index) {
            /* iterate through array or object */
            okToSet = allowOverriding;
            if (!allowOverriding) {
                if (r.get(method.kbxGroupId) === undefined) {
                    okToSet = true;
                } else {
                    if (r.get(method.kbxGroupId).get('status') === 'ok') {
                        okToSet = true;
                    }
                }
            }
            if (okToSet) {
                // set device
                var d = {
                    id: method.kbxGroupId, 
                    name: method.kbxGroupLabel || method.kbxGroupName || ''
                }

                if (method.kbxGroupIcon !== null) {
                    d.icon = method.kbxGroupIcon;
                }

                r.add(d);
            }

            // filter devices and arguments
            if (method.kbxMethodId !== undefined && method.kbxMethodId !== null) {
                methodId = method.kbxMethodId;
                if (r.get(method.kbxGroupId).get('methods').get(method.kbxMethodId) === undefined) {
                    // set method + arguments
                    r.get(method.kbxGroupId).get('methods').add(method, {parse:true});
                }

                if (method.statusCode === 1) {
                    // group has being removed
                    r.get(method.kbxGroupId).set('status', 1);
                }
            }

        });

        return r;
    }

    Device.model = KuroboxModel.extend({
        defaults: {
        	id: undefined,
        	name: '',
        	status: '',
        	enabled: true,
        	// condition: emptyRuleDevices(), //RuleDevice
            // execution: emptyRuleDevices(),  // RuleDevice
            trigger: {
                type: 2,
                value: 300,
            }
        },
        initialize: function() {
            if (this.attributes.condition === undefined) {
                this.attributes.condition = emptyRuleDevices();
            }
            if (this.attributes.execution === undefined) {
                this.attributes.execution = emptyRuleDevices();
            }
            KuroboxModel.prototype.initialize.apply(this, arguments);
        },
        fetch: function(options) {
            this.url = 'get_rule';
            this.dev_opt = {
                param: {
                    ruleId: this.attributes.id
                },
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },
        save: function(key, val, options) {
           this.url = 'set_rule';
           this.dev_opt = {
                method: 'POST'
           }

            var attrs, api_param;
            // set property
           // Handle both `"key", value` and `{key: value}` -style arguments.
            if (typeof key === 'object') {
                if (!key.success && !key.error) {
                    attrs = key;
                    options = (val) ? val : {};
                } else {
                    options = key;
                }
            } else {
                (attrs = {})[key] = val;
                options || (options = {});
            }


            if (key !== undefined) {
                // save to server
                // Run validation.
                if (!this._validate(attrs, options)) return false;

                // set local
                if (typeof key === 'object' && !options.success && !options.error) {
                    this.set(attrs, options);
                } else {
                    this.set(attrs, val, options);
                }
            }

           this.dev_opt.param = this.toObject();

           // customize param
            api_param = this._handleParam(this.dev_opt);

            console.log('testing output', this.dev_opt.param);

           this._triggerKuroboxApi(this, this.url, api_param, options, this.dev_opt);
        },
        destroy: function(options) {
           this.url = 'delete_rule';
           this.dev_opt = {
                method: 'GET',
                param: {
                    ruleId: this.attributes.id
                }
           }
           this._triggerKuroboxApi(this, this.url, this._handleParam(this.dev_opt), options, this.dev_opt);
        },
        execute: function(check_condition, options) {
            check_condition = check_condition || false;
            this.url = 'trigger_rule';
            this.dev_opt = {
                method: 'GET',
                param: {
                    ruleId: this.attributes.id,
                    checkCondition: check_condition
                }
            }
            this._triggerKuroboxApi(this, this.url, this._handleParam(this.dev_opt), options, this.dev_opt);
        },
        set_enable: function(enable, options) {
            this.url = 'enable_rule';
            this.dev_opt = {
                method: 'GET',
                param: {
                    ruleId: this.attributes.id,
                    enabled: enable
                }
            }
            this._triggerKuroboxApi(this, this.url, this._handleParam(this.dev_opt), options, this.dev_opt);
        },
        parse: function(data) {
            var res = data.response;
            var o = {};
            o.id = res.ruleId;
            o.name = res.ruleName;
            o.status = res.statusMessage;
            o.enabled = res.enabled;
            o.trigger = res.trigger;

            o.condition = _parseDeviceRule(res.condition);
            o.execution = _parseDeviceRule(res.execution);
            return o;
        },
        toObject: function() {
            var o = _.clone(this.attributes);
            o.ruleName = o.name;
            o.name = undefined;
            delete o.name;

            o.ruleId = o.id;
            o.trigger = JSON.stringify(this.attributes.trigger);
            o.condition = JSON.stringify(this.attributes.condition.toObject());
            o.execution = JSON.stringify(this.attributes.execution.toObject());

            // remove
            o.status = undefined;
            o.id = undefined;
            return o;
        }
    });

    Device.collection = KuroboxCollection.extend({
    	model: Device.model,

        set_enable: function(id, enable, options) {
            this.url = 'set_status';
            this.dev_opt = {
                url: 'json/example.set_timezone.json',
                method: 'GET',
                bypassSession: true,
                param: {id: id, enable: enable}
            }
            
            var param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, 'set_status', param, options, this.dev_opt);
        },

    	parse: function(data) {
            var o = [], r;
            _.each(data, function(rule, index) {
                r = {
                    id: rule.ruleId,
                    name: rule.ruleName,
                    enabled: rule.enabled,
                    status: rule.statusCode,
                    // condition: new RuleDevice.collection(rule.condition, {parse: true}),
                    // execution: new RuleDevice.collection(rule.execution, {parse: true})
                }


                // manage condition and execution devices
                r.condition = _parseDeviceRule(rule.condition);
                r.execution = _parseDeviceRule(rule.execution);
                o.push(r)
            });
    		return o;
    	}
    })

    return Device;
});
