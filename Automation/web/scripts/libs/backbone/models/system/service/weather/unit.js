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

    var TemperatureUnitModel = KuroboxModel.extend({
        defaults: {
            temperatureUnit:'celsius'
        },

        fetch: function(options) {
            this.url = 'get_temperature_unit';
            this.dev_opt = {
                //url: 'json/example.get_temperature_unit.json',
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                 param:{module:'setup_module'}
            }

            KuroboxModel.prototype.fetch.apply(this, arguments);
        },
        
        save: function(temperatureUnit, options) {
            this.set({temperatureUnit:temperatureUnit});

            if(temperatureUnit == 'celsius'){
                temperatureUnit  = '['+0+']';
            }else if(temperatureUnit == 'kelvin'){
                temperatureUnit  = '['+1+']';
            }else if(temperatureUnit == 'fahrenheit'){
                temperatureUnit  = '['+2+']';
            }

            this.url = 'set_temperature_unit';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                app_id: '2000100',
                //url: 'json/example.set_timezone.json',
                param:{module:'setup_module', temperatureUnit:temperatureUnit}
            }

            KuroboxModel.prototype.save.call(this, options);
        },

        parse: function(data) {
           return {
                temperatureUnit: data.response.temperatureUnit
            }
        }
    });


    return TemperatureUnitModel;
});
