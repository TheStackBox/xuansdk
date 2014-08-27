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

], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var Upnp = {};

    Upnp.model = KuroboxModel.extend({
    	defaults: {
    		name: '',
            path: '',
            protocoldId: ''
    	},

        pair: function(options, pair_info) {
            this.url = 'set_device_pair';
            this.dev_opt = {
                method: 'GET',
                param: {
                    module: 'device_manager',
                    protocolId: this.attributes.protocolId,
                    deviceId: this.attributes.id,
                    pairInfo: (typeof pair_info === "string") ? pair_info : JSON.stringify(pair_info),
                }
            }
            KuroboxModel.prototype.fetch.call(this, options);
        }
    });

    Upnp.collection = KuroboxCollection.extend({
        model: Upnp.model,

    	fetch: function(protocol_id, options) {
            //https://192.168.0.79/cgi-bin/syb_reqresp_cgi?app_id=99&module=device_manager&method=get_device_list&protocolId=1
    		this.url = 'get_device_list';
    		this.dev_opt = {
    			method: 'GET',
                param: {
                    module: 'device_manager',
                    protocolId: protocol_id
                }
    		}
    		KuroboxCollection.prototype.fetch.call(this, options);
    	},

        parse: function(resp) {
            return resp.response.device;
        }
    });

    return Upnp;
});
