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
    'libs/backbone/models/kurobox-model'
], function (_, KuroboxModel) {
    'use strict';

    var NetworkModel = KuroboxModel.extend({
        fetch: function(options) {
        	this.url = 'get_network_info';
        	this.dev_opt = {
        		bypassSession: true,
                //url: 'json/example.get_network_info.json',
        		method: 'GET'
        	}

        	KuroboxModel.prototype.fetch.apply(this, arguments);
        },

        dhcp: function(key, val, options) {
            this.url = 'set_network_info';
            this.dev_opt = {
                bypassSession: true,
                //url: 'json/example.set_timezone.json',
                method: 'GET'
            }

            //dns auto no need passing dns1 and dns2 param
            if(this.get('dns_mode') == 'true'){
                this.dev_opt.param = {
                    dhcp_mode:this.get('dhcp_mode'), 
                    dns_mode:this.get('dns_mode'),
                    ip:this.get('ip'),
                    subnet:this.get('subnet'),
                    gateway:this.get('gateway')           
                }
            }else{
                this.dev_opt.param = {
                    dhcp_mode:this.get('dhcp_mode'), 
                    dns_mode:this.get('dns_mode'),
                    ip:this.get('ip'),
                    subnet:this.get('subnet'),
                    gateway:this.get('gateway'),
                    dns1:this.get('dns1'),
                    dns2:this.get('dns2')                            
                }
            }

            KuroboxModel.prototype.save.call(this, key, val, options);
        },

        save: function(key, val, options) {
        	this.url = 'set_network_info';
        	this.dev_opt = {
        		bypassSession: true,
                //url: 'json/example.set_timezone.json',
        		method: 'GET'
        	}

            //dns auto no need passing dns1 and dns2 param

            // if(this.get('dhcp_mode') == 'true' || this.get('dns_mode') == 'true'){

            // }else if(this.get('dhcp_mode') == 'false' || this.get('dns_mode') == 'true'){
            //     this.dev_opt.param = {
            //         dhcp_mode:this.get('dhcp_mode'), 
            //         dns_mode:this.get('dns_mode'),
            //         ip:this.get('ip'),
            //         subnet:this.get('subnet'),
            //         gateway:this.get('gateway')       
            //     }
            // }
            this.dev_opt.param = {};
            if(this.get('dhcp_mode') == true){
                this.dev_opt.param.dhcp_mode = this.get('dhcp_mode');
            }else{
                this.dev_opt.param.dhcp_mode = this.get('dhcp_mode');
                this.dev_opt.param.ip = this.get('ip');
                this.dev_opt.param.subnet = this.get('subnet');
                this.dev_opt.param.gateway = this.get('gateway');
            }

            if(this.get('dns_mode') == true){
                this.dev_opt.param.dns_mode = this.get('dns_mode');
            }else{
                this.dev_opt.param.dns_mode = this.get('dns_mode');
                this.dev_opt.param.dns1 = this.get('dns1');
                this.dev_opt.param.dns2 = this.get('dns2');
            }

        	KuroboxModel.prototype.save.call(this, key, val, options);
        },

        parse: function(data) {
           return {
                dhcp_mode: (data.response.dhcp_mode === 'true'),
                dns_mode: (data.response.dns_mode === 'true'),
                ip: (data.response.ip ? data.response.ip : '-'),
                subnet: (data.response.subnet ? data.response.subnet: '-'),
                gateway: (data.response.gateway ? data.response.gateway :'-'),
                dns1: (data.response.dns1 ? data.response.dns1 : '-'),
                dns2: (data.response.dns2 ? data.response.dns2 : '-')
            }
        }
    });

    return NetworkModel;
});