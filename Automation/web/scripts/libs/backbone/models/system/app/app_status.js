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
    'libs/backbone/models/kurobox-model'
], function (_, KuroboxModel) {
    'use strict';

   var AppModel = KuroboxModel.extend({
        idAttribute: 'id',
        defaults: {
            appId: '',
            status: '',
            statusId: ''
        },

        fetch: function(appId, options) {
            this.url = 'get_app_running_status';
            this.dev_opt = {
                //url: 'json/app_status.json',
                method: 'GET',
                bypassSession: true,
                app_id: '2000100',                
                param:{appId:appId , module:'application_manager'}
            }
            KuroboxModel.prototype.fetch.call(this, options);            
        },

        parse: function(data) {
            return {
                appId: data.response.appId,
                status: data.response.status,
                statusId: data.response.statusId
            }            
        }
    });

    return AppModel;
});
