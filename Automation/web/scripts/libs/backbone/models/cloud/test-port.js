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
    'jquery',
    'underscore',
    'libs/backbone/models/kurobox-model'
], function ($, _, KuroboxModel) {
    'use strict';
    var CloudHost = 'http://192.168.0.231:8080';

    var TestPort = KuroboxModel.extend({
        default: {
            port1_status: false,
            port2_status: false
        },

        test: function(port, options) {
            this.url = 'server_request';
            this.dev_opt = {
                method: 'GET',
                //url: 'json/example.set_timezone.json',
                bypassSession: true,
                param: {}
            }

            //generate url
            this.dev_opt.param.url = CloudHost+'/davidbox/c/client/testPorts?sapi1.0&port1='+port;//+'&port2=16888';
            //generate sum
            this.dev_opt.param.concate = port;//+'16888';

            KuroboxModel.prototype.fetch.call(this, options);
        },
        /*test: function(port1, port2, options) {
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
        },*/

        fetch: function() {},
        save: function() {},

        parse: function(data) {
            return {
                port1_status: data.response.port1_status,
                port2_status: data.response.port2_status
            }
        }
    });

    return TestPort;
});