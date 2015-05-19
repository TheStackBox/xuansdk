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
    'libs/backbone/models/kurobox-collection'
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var LocationModel = KuroboxModel.extend({
        idAttribute: 'id',
        defaults: {
            longitude:0,
            name:'',
            id:0,
            latitude:0,
            country:''
        },

    });

    var LocationCollection = KuroboxCollection.extend({
        url: 'get_matching_location_name',
        model: LocationModel,
        fetch: function(location, options) {
            this.dev_opt = {
                //url: 'json/example.get_matching_location_name.json',
                method: 'GET',
                app_id: '2000100',
                bypassSession: true,
                param:{location:location, module:'weather_module'} 
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            console.log('data >> ', data)
            return data.response.matchingLocationName;
        }
    })

    var SearchLocationBundle = {
        model: LocationModel,
        collection: LocationCollection
    }

    return SearchLocationBundle;
});
