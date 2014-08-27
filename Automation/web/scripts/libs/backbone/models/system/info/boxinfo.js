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

    var BoxInfoModel = KuroboxModel.extend({
        defaults: {
            id: '',
        	name: '',
        	mac_address: '',
            firmware_version: '',
            capabilities: '',
        	cpuid: ''
        },

        fetch: function(options) {
            this.url = 'get_box_info';
            this.dev_opt = {
                //url: 'json/example.get_box_info.json',
                bypassSession: true,
                method: 'GET',
                param:{}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function (boxName, options) {
            console.log('boxName', boxName);
            this.url = 'set_box_info';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET',
                param:{name: boxName}
            };
            KuroboxModel.prototype.save.call(this, options);
        },

        parse: function(data) {
            return {
                id: data.response.id,
                name: data.response.name,
                mac_address: data.response.mac_address,
                firmware_version: data.response.firmware_version,
                capabilities: data.response.capabilities,
                cpuid: data.response.cpuid
            };
        }
    });

    return BoxInfoModel;
});
