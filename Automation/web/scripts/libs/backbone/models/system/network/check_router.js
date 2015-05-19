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
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/system/network/network'
], function (_, KuroboxModel, NetworkInfo) {
    'use strict';

    var CheckRouterModel = KuroboxModel.extend({
        fetch: function(options) {
        	this.url = 'check_router_connectivity';
        	this.dev_opt = {
        		//url: 'json/example.check_router_connectivity.json',
        		method: 'GET',
        		bypassSession: true
        	};

        	KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function(key, val, options) {
        	console.warn('This modal has no set method');
        	return;
        },

        parse: function(data) {
            console.log('parse1', data.response.status)
            var netinfo = {
                dhcp_mode: (data.response.info.dhcp_mode === 'true'),
                dns_mode: (data.response.info.dns_mode === 'true'),
                ip: (data.response.info.ip ? data.response.info.ip : '-'),
                subnet: (data.response.info.subnet ? data.response.info.subnet: '-'),
                gateway: (data.response.info.gateway ? data.response.info.gateway :'-'),
                dns1: (data.response.info.dns1 ? data.response.info.dns1 : '-'),
                dns2: (data.response.info.dns2 ? data.response.info.dns2 : '-')
            }
            
            return {
                status: (data.response.status === 'ok'),
                network_info: new NetworkInfo(netinfo)
            }
        }
    });

    return CheckRouterModel;
});
