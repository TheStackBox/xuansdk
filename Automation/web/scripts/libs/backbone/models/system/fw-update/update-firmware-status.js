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

    var BoxInfoModel = KuroboxModel.extend({
        defaults: {
            status: '',
            progress: ''
        },

        fetch: function(options) {
            this.url = 'get_fw_update_status';
            this.dev_opt = {
                //url: 'json/example.get_fw_update_status.json',
                bypassSession: true,
                method: 'GET',
                param:{}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },


        parse: function(data) {
            return {
                status: data.response.status,
                progress: data.response.progress,
            };
        }
    });

    return BoxInfoModel;
});
