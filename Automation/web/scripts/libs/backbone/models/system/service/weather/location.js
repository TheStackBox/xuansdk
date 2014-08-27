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

    var LocationModel = KuroboxModel.extend({
        defaults: {
            longitude:0,
            id: 0,
            location:'',
            latitude: 0,
            country: ''
        },

        fetch: function(options) {
            this.url = 'get_location';
            this.dev_opt = {
                //url: 'json/example.get_location.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param:{module:'weather_module'}
            }

            KuroboxModel.prototype.fetch.apply(this, arguments);
        },

        save: function(locationId , options) {
            this.url = 'set_location_by_id';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                //url: 'json/example.set_timezone.json',
                param:{locationId:locationId, module:'weather_module'}
            }

            KuroboxModel.prototype.save.call(this, options);
        },

        parse: function(data) {
            var pData = {
                longitude: data.response.longitude,
                id: data.response.id,
                location: data.response.location,
                latitude: data.response.latitude,
                country: data.response.country
            }

            var comma = _.isEmpty(pData.location) == false && _.isEmpty(pData.country) == false ? ', ' : ''; 
            pData.address = (pData.location || '')+comma+(pData.country || '');

            return pData;
        }
    });


    return LocationModel;
});
