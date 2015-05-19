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

    var SystemTimeTimesettingModel = KuroboxModel.extend({
        defaults: {
        	twenty_four: true,
        	auto_daylight: true
        },

        fetch: function(options) {
            this.url = 'get_data';
            this.dev_opt = {
               // url: 'json/example.get_timesetting.json',
                bypassSession: true,
                method: 'GET',
                param: {
                    ids: 'twenty_four,auto_daylight'
                }
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function(key, val, options) {
            this.url = 'set_data';
            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET'
            };
            var attrs;

            // Handle both `"key", value` and `{key: value}` -style arguments.
            if (typeof key === 'object') {
                attrs = key;
                options = val;
            } else {
                (attrs = {})[key] = val;
            }

            options || (options = {});

            // save to server
            // Run validation.
            if (!this._validate(attrs, options)) return false;

            // set local
            if (typeof key === 'object') {
                this.set(attrs, options);
            } else {
                this.set(attrs, val, options);
            }

            var param = {data:JSON.stringify(this.attributes)};
            console.log(param);
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        },

        parse: function(data) {
            return {
                twenty_four: (data.response.twenty_four == null ? false : data.response.twenty_four),
                auto_daylight: (data.response.auto_daylight == null ? false : data.response.auto_daylight)
            }
        }
    });

    return SystemTimeTimesettingModel;
});
