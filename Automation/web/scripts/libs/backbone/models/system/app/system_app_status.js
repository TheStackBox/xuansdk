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

   var AppModel = KuroboxModel.extend({
        idAttribute: 'id',
        defaults: {
            statusId: '',
            status: ''
        },

        fetch: function(options) {
            this.url = 'get_system_app_status';
            this.dev_opt = {
                //url: 'json/app_status.json',
                method: 'GET',
                bypassSession: true,
                app_id: '2000100',                
                param:{}
            }
            KuroboxModel.prototype.fetch.call(this, options);            
        },

        parse: function(data) {
            return {
                statusId: data.response.statusId,
                status: data.response.status
            }            
        }
    });

    return AppModel;
});
