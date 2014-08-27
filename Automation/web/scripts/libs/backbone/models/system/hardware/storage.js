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
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var StorageModel = KuroboxModel.extend({
        defaults: {
            deviceName: '',
            devicePath: '',
            freeDiskSpace: '',
            usedDiskSpace: '',
            totalSize: ''
        },
   });

    var StorageCollection = KuroboxCollection.extend({
        model: StorageModel,
        fetch: function(options) {
            this.url = 'list_storage';
            this.dev_opt = {
                //url: 'json/list_security-type.json',
                method: 'GET',
                bypassSession: true
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            console.log('data >> ', data)
            return data.response.deviceList;
        }
    });

    return StorageCollection;
});
