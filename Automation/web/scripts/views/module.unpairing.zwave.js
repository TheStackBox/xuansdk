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
    'jquery',
    'underscore',
    'views/module.unpairing.generic',
    'templates',
    'Kurobox',
], function ($, _, GenericUnpairModule, JST, Kurobox) {
    'use strict';
    var spr = GenericUnpairModule.prototype;

    var ZwaveUnpairModule = GenericUnpairModule.extend({
        template: JST['app/scripts/templates/module.unpairing.zwave.ejs'],
        events: {
            'click #z-wave-dark': 'stop'
        },
        render: function() {
            console.log('zwave: begin unpair', this.el, this.device)
            // there's no rendering happen
            this.$el.html(this.template());
            $('#z-wave-dark').show();
            _.defer(function() {
                // open socket
                Kurobox.socket.verbose = true;
                if (Kurobox.socket.connected) Kurobox.socket.stop();
                Kurobox.socket.on('socket:UNPAIR_DEVICE_USER_ACTION_REQUIRED', function() {
                    // ask user to trigger the button
                    this.$('#z-wave-unpair').fadeIn('fast');
                }, this);
                Kurobox.socket.on('socket:UNPAIR_DEVICE', function() {
                    // the device has being removed
                    this.$('#z-wave-dark').hide();
                    this.$('#z-wave-unpair').hide();
                    Kurobox.socket.stop();

                    spr.render.call(this);
                }, this);
                Kurobox.socket.on('connected', function() {
                    console.log('socket connected')
                    // socket is ready to request for action
                    this.device.destroy({
                        error: function(model, resp, options) {
                            this.$('#z-wave-dark').hide();
                            console.error('ZWave unable to get into unpair mode', resp)
                        }.bind(this),
                    });
                }, this);
                console.log('begin socket connection')
                Kurobox.socket.start();
            }.bind(this))
        },

        stop: function() {
            console.log('cancelling unpairing...')
            Kurobox.api('set_device_unpair_abort', 
            // param
            {
                module: 'device_manager',
                pairedDeviceId: this.device.get('id')
            }, 
            // options
            {
                httpMethod: 'GET'
            })
            spr.stop.call(this);
        },

        destroy: function() {
            Kurobox.socket.stop();
            spr.destroy.call(this);
        }
    });

    return ZwaveUnpairModule;
});
