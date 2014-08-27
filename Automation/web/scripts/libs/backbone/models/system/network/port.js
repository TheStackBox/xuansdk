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

    var PortModel = KuroboxModel.extend({
        defaults: {
            http_port: '',
            https_port: ''
        },

        fetch: function(options) {
            this.url = 'get_port';
            this.dev_opt = {
                bypassSession: true,
                method: 'GET',
                param:{}
            };
            KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function (key, options) {
            console.log(key);
            this.url = 'set_port';

            this.set('http_port', key.http_port);
            this.set('https_port', key.https_port);

            this.dev_opt = {
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                method: 'GET'
            };
            KuroboxModel.prototype.fetch.call(this, options);   
        },
        
        test: function(port1, port2, options) {
            this.url = 'test_port'
            this.dev_opt = {
                url: 'json/example.cloud_test_port.json',
                bypassSession: true,
                method: 'GET'
            }

            if (options.success) {
                var successCb = options.success;
                options.success = function(model, data, options) {
                    // parse data
                    this.set(this.parse(data), {silent: (successCb !== null)});

                    if (this.attributes.port1_status && this.attributes.port2_status) {
                        // run callback
                        if (successCb) successCb(model, data, options);
                    } else {
                        // test port failed
                        if (options.error) options.error(model, data, options);
                    }
                }.bind(this);
            }; 

            this._triggerKuroboxApi(this, this.url, {port1: port1, port2: port2}, options, this.dev_opt);
        },

        parse: function(data) {
            return {
                http_port: data.response.http_port,
                https_port: data.response.https_port
            };
        }
    });

    return PortModel;
});
