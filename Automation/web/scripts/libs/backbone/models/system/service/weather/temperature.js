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

    var TemperatureModel = KuroboxModel.extend({
        defaults: {
            unit: 'celsius',
            temp_max: 0,
            temp: 0,
            temp_min: 0,
            icon: '',
            location: {},
            temp_kf: 0
        },

        fetch: function(options) {
            this.url = 'get_current_temperature';
            this.dev_opt = {
                //url: 'json/example.get_current_temperature.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                param:{module:'weather_module'}
            }

            KuroboxModel.prototype.fetch.apply(this, arguments);
        },

        parse: function(data) {
           return {
                icon: data.response.currentTemp.icon,
                unit: data.response.currentTemp.unit,
                temp_max: data.response.currentTemp.temp_max,
                temp: data.response.currentTemp.temp,
                temp_min: data.response.currentTemp.temp_min,
                location: data.response.currentTemp.location,
                temp_kf: data.response.currentTemp.temp_kf
            }
        }
    });


    return TemperatureModel;
});
