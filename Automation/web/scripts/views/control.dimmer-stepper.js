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
    'views/control.abstract',
    'templates',
    'Kurobox',
    'models/control.dimmer-stepper',
    'libs/utils/browser',
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';
    var spr = AbstractCtrl.prototype;
    var DimmerControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.dimmer-stepper.ejs'],
        model_class: Model,
        events: {
            'click #power-btn': 'on_user_turn_on_off',
            'click #dim': 'on_user_dim',
            'click #brighten': 'on_user_brighten',
        },

        destroy: function() {
            AbstractCtrl.prototype.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function(data) {
            spr.init.call(this);
            
            spr.initialize.apply(this, arguments);

            this.stat = new Object();

            // listen to events
            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:DIMMER_STEPPER_CONTROLLER_STATE_CHANGED', this.on_dimmer_state_changed, this)
            Kurobox.socket.on('connected', function() {
                this.stat.power = data.response.status.dimmerStepper;
                // power status
                this.invalidate_power_status();

                // brightness
                this.bOrigWidth = this.$('#range').width();
                this.$('#dimmer-slide').prop('value', this.stat.level)
            }, this)
            Kurobox.socket.start();
        },

        on_user_dim: function(e) {          
            var $e = $(e.currentTarget);
            this.model.dim();
        },

        on_user_brighten: function(e) {
            var $e = $(e.currentTarget);
            this.model.brighten();
        },

        invalidate_power_status: function() {
            console.log('power: ', this.stat.power)
            if (this.stat.power=='ON') {
                // power on
                this.$('#power-btn').removeClass('disabled');
            } else {
                this.$('#power-btn').addClass('disabled');
            }
        },

         on_user_turn_on_off: function(e) {
            if (this.stat.power=='ON') {
                // power on
                this.stat.power = 'OFF'
                this.model.power_off();
            } else {
                this.stat.power = 'ON'
                this.model.power_on();
            }
            this.invalidate_power_status();
        },


        on_dimmer_state_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.stat.power = data.response.dimmerStepper;
                this.invalidate_power_status();
            }
        }
    });

    return DimmerControl;
});
