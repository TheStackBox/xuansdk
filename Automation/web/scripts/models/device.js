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
    'libs/backbone/models/kurobox-collection'
], function (_, KuroboxModel, KuroboxCollection, Backbone) {
    'use strict';
    var Device = {};

    Device.model = KuroboxModel.extend({
        defaults: {
        	id: undefined,
        	name: 'Unknown device',
        	icon: '&#xe617',
            isControllable: false,
        	status: '',
        	statusUnit: '',
            description: '',
            protocol: '',
            type: ''
        },
        fetch: function(id, options) {
            this.url = "get_paired_device_info";
            this.dev_opt = {
                method: 'GET',
                param: {
                    module: 'device_manager',
                    pairedDeviceId: id
                }
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },
        save: function(key, val, options) {
            this.url = 'set_paired_device_info';
            this.dev_opt = {
                method: 'GET',
                param: {
                    module: 'device_manager',
                    pairedDeviceId: this.attributes.id
                },
                param_attr: {
                    name: 'name',
                    typeId: 'typeId',
                    groupId: 'groupId',
                    icon: 'icon',
                    status: 'status'
                }
            }
            KuroboxModel.prototype.save.call(this, key, val, options);
        },
        destroy: function(options) {
            // prevent zwave device to call this
            this.url = 'set_device_unpair';
            this.dev_opt = {
                method: 'GET',
                param: {
                    module: 'device_manager',
                    pairedDeviceId: this.attributes.id
                }
            }
            var param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        },
        test: function(options) {
            this.dev_opt = {
                url: 'json/example.set_timezone.json',
                method: 'GET',
                param: {id: this.attributes.id}
            }
            var param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, 'test_device', param, options, this.dev_opt);
        },
        parse: function(data) {
            var resp = data.response.deviceInfo;
            var o = {};
            o.id = resp.id;
            o.name = resp.name;
            if (resp.icon !== undefined && resp.icon !== '') o.icon = resp.icon;
            o.status = resp.status;
            o.statusUnit = resp.statusUnit;
            o.protocol = resp.protocol.name;
            o.protocolId = resp.protocolId;
            o.type = resp.deviceType.name;
            o.typeId = resp.deviceTypeId;
            o.groupId = resp.groupId;
            o.enabled = (resp.enable === 1);
            o.isControllable = (resp.controlPanel === 1)

            return o;
        }
    });

    Device.collection = KuroboxCollection.extend({
    	model: Device.model,

        // fetch paired device
    	fetch: function(start, total, type, options) {
   			this.url = 'get_paired_devices_list';
    		this.dev_opt = {
    			url: 'json/device_list.json',
    			param: {
    				start: start,
    				total: total,
    				type: type
    			},
    			method: 'GET'
    		}
    		KuroboxCollection.prototype.fetch.call(this, options);
    	},

        fetch_new_device: function(protocol, options) {
            this.url = 'get_new_device';
            this.dev_opt = {
                url: 'json/example.get_new_device.json',
                param: {
                    protocol: protocol
                },
                method: 'GET'
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        stop: function(protocol, options) {
            this._triggerKuroboxApi(this, 'stop_discovery', {protocol:protocol}, options, {
                method: 'GET',
                url: 'json/example.set_timezone.json'
            })
        },

    	parse: function(data) {
            // the list content summarized device info
            var o = [];
            var d;
            _.each(data.response.devices, function(device) {
                d = {};
                d.id = device.id;
                d.name = device.name;
                if (device.icon !== undefined && device.icon !== '') d.icon = device.icon;
                d.status = device.status;
                d.statusUnit = device.statusUnit;
                d.protocolId = device.protocolId;
                if (device.deviceType !== null) d.type = device.deviceType.name;
                d.typeId = device.deviceTypeId;
                d.groupId = device.groupId;
                d.enabled = (device.enable === 1);
                d.isControllable = (device.controlPanel === 1);

                o.push(new Device.model(d))
            })
    		return o;
    	}
    })

    return Device;
});
