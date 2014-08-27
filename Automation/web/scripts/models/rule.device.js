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
    'models/device',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'models/rule.device.method',
    'models/rule.device-type'
], function (_, Device, KuroboxModel, KuroboxCollection, DeviceMethod, RuleDeviceType) {
    'use strict';

    var COMPONENT_DEMO = false;

    var RuleDevice = {};
    var spr = Device.prototype;
   	RuleDevice.model = KuroboxModel.extend({
        defaults: {
            'section': 'if',
            'description': '',
            'id': 0,
            'name': 'Unknown device',
            'status': 0,
            'icon': '&#xe617',
            'methods': new DeviceMethod.collection() // DeviceMethod.collection
        },
        initialize: function(data, options) {
            if (data !== undefined) {
                if (data.methods === undefined || data.methods === null) {
                    data.methods = new DeviceMethod.collection();
                } else {
                    data.methods = new DeviceMethod.collection(data.methods);
                }
                this.set(data);
            }
        },
        list_methods: function(options) {
            this.url = 'list_methods';
            this.dev_opt = {
                method: 'GET',
                param: {
                    groupId: this.get('id'),
                    section: this.get('section')
                }
            }
            if (typeof PRODUCTION === 'undefined') {
                if (COMPONENT_DEMO) this.dev_opt.url = 'json/sample.components.json';
            }
            this.parse = this._parseListMethods;
            KuroboxModel.prototype.fetch.call(this, options);
        },
        
        _parseListMethods: function(data) {
            console.log('device data', data.response.data)
            var o = {
                name: data.response.group.kbxGroupLabel,
                icon: data.response.group.kbxGroupIcon,
                description: data.response.group.kbxGroupDesc,
                methods: new DeviceMethod.collection(data.response.data, {parse:true})
            }
            console.log('test methods', o.methods);
            console.log('methods length vs data length', o.methods.length, data.response.data.length)
            return o;
        },

        clone: function() {
            var o = new RuleDevice.model({
                section: this.get('section'),
                description: this.get('description'),
                id: this.get('id'),
                name: this.get('name'),
                status: this.get('status'),
                icon: this.get('icon'),
            })

            o.set('methods', this.get('methods').clone())

            return o;
        }
    });

    RuleDevice.collection = Device.collection.extend({
    	model: RuleDevice.model,
    	fetch: function(section, group, options) {
            this.section = (section === 'if') ? 'condition' : 'execution';
    		this.url = 'list_groups';
    		this.dev_opt = {
    			method: 'GET',
    			param: {
                    section: section,
    				parentId: group
    			}
    		}
    		KuroboxCollection.prototype.fetch.call(this, options);
    	},

        parse: function(data) {
            console.log('data', data)
            
            var o = [];
            _.each(data.response.data, function(deviceData, index){
                var extraInfo = ObjUtil.clone(deviceData);
                delete extraInfo.kbxConditionCount;
                delete extraInfo.kbxExecutionCount;
                delete extraInfo.kbxGroupAppId;
                delete extraInfo.kbxGroupDesc;
                delete extraInfo.kbxGroupIcon;
                delete extraInfo.kbxGroupId;
                delete extraInfo.kbxGroupLabel;
                delete extraInfo.kbxGroupName;
                delete extraInfo.kbxGroupParentId;

                o.push({
                    id: deviceData.kbxGroupId,
                    label: deviceData.kbxGroupLabel || deviceData.kbxGroupName || '',
                    icon: deviceData.kbxGroupIcon || undefined,
                    extra_info: extraInfo,
                    description: deviceData.kbxGroupDesc
                })
            }.bind(this))

            // register group info
            this.group = new RuleDeviceType.model({
                id: data.response.parentGroup.kbxGroupId,
                label: data.response.parentGroup.kbxGroupLabel || undefined,
                icon: data.response.parentGroup.kbxGroupIcon || undefined,
                description: data.response.parentGroup.kbxGroupDesc || '',
            })
            return o;
        },

        toObject: function() {
            // consolidate only methods and param
            // without device info
            var o, m;

            o = [];
            this.each(function(device) {
                // getting methods and params
                device.get('methods').each(function(method) {
                    o.push(method.toObject())
                }.bind(this))
            }.bind(this));

            return _.flatten(o);
        }
    });

    return RuleDevice;
});
