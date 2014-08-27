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
    'models/control.dimmer',
    'libs/utils/browser',
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';
    var spr = AbstractCtrl.prototype;
    var DimmerControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.dimmer.ejs'],
        model_class: Model,
        events: {
            'click #power-btn': 'on_user_turn_on_off',
            'input #dimmer-slide': 'on_user_change_brightness'
        },

        initialize: function() {
            spr.initialize.apply(this, arguments);
            if (BrowserUtil.isMobile()) {
                this.events['touchend #dimmer-slide'] = 'on_user_confirm_brightness';
            } else {
                this.events['change #dimmer-slide'] = 'on_user_confirm_brightness';
            }
        },

        destroy: function() {
            AbstractCtrl.prototype.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function(data) {
            spr.init.call(this);

            this.stat = new Object();
            this.stat.power = data.response.status.dimmer;
            this.stat.level = data.response.status.level;
            
            // power status
            this.invalidate_power_status();

            // brightness
            this.bOrigWidth = this.$('#range').width();
            this.$('#dimmer-slide').prop('value', this.stat.level)
            this.invalidate_brightness_range_bar();

            // listen to events
            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:DIMMER_CONTROLLER_STATE_CHANGED', this.on_dimmer_state_changed, this)
            
            Kurobox.socket.start();
        },

        on_user_turn_on_off: function(e) {
            if (this.stat.power=='ON') {
                // power on
                this.model.power_off();
            } else {
                this.model.power_on();
            }
            this.invalidate_power_status();
        },

        on_user_change_brightness: function(e) {          
            var $e = $(e.currentTarget);
            this.invalidate_brightness_range_bar($e.prop('value'));
        },

        on_user_confirm_brightness: function(e) {
            var $e = $(e.currentTarget);
            this.model.dim($e.prop('value'));
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

        invalidate_brightness_range_bar: function(value) {
            var b = value || this.stat.level;
            var p = (b/99)*this.bOrigWidth;
            this.$('#range').css('width', p);

            // change value prop in range
            this.$('#dimmer-slide').prop('value', b);
        },

        on_dimmer_state_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.stat.level = data.response.level;
                this.stat.power = data.response.dimmer;
      
                if (this.stat.level <= 0) {
                    // assume it's off
                    this.stat.power = 'OFF';
                }

                // invalidate
                this.invalidate_power_status();
                this.invalidate_brightness_range_bar();
            }
        }
    });

    return DimmerControl;
});
