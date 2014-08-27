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
    'libs/backbone/models/kurobox-collection',
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';
    var API = {};
    API.methodModel = KuroboxModel.extend({
        parse: function(data) {
            console.log('method', data);
            return data;
        }
    })

    API.collection = KuroboxCollection.extend({
        fetch: function(controller, paired_device_id, options) {
            if (!controller) throw 'Undefined controller'
            this.url = 'list_api';
            this.dev_opt = {
                param: {
                    module: 'device_manager.'+controller,
                    pairedDeviceId: paired_device_id
                },
                method: 'GET'
            }
            KuroboxCollection.prototype.fetch.call(this, options);
        },

        parse: function(data) {
            var r = [], o;
            _.each(data.response.method, function(m, idx) {
                o = {};
                var keys = _.keys(m);
                if (keys.length > 1) throw 'Method @ '+idx+' contains more than 1 key '+ keys.toString();
                o.id = keys[0];
                o.param = [];

                _.each(m[o.id].params, function(val, idx) {
                    o.param.push(val.paramName);
                })
                r.push(new API.methodModel(o));
            })
            return r;
        }
    })

    return API;
});
