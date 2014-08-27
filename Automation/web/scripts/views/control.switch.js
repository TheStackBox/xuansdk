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
    'models/control.switch'
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';

    var spr = AbstractCtrl.prototype;
    var SwitchControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.switch.ejs'],
        model_class: Model,
        events: {
            'click #power-btn': 'on_user_toggle_switch'
        },

        destroy: function() {
            spr.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function() {
            spr.init();

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:SWITCH_CONTROLLER_STATE_CHANGED', this.on_state_changed, this);
            if (Kurobox.socket.connected) {
                this.invalidate_ui();
            } else {
                Kurobox.socket.on('connected', this.invalidate_ui, this);
                Kurobox.socket.start();
            }
        },

        invalidate_ui: function() {
            // this.$el.html(this.template({model: this.model, device: this.options.device}));
            _.defer(function() {
                spr.init.call(this);
                // initialise door lock status
                this.invalidate_switch_status(this.model.get('switch_status'));
            }.bind(this))
        },

        on_user_toggle_switch: function(e) {
            var status = this.model.get('switch_status');
            if (status=='ON') {
                // switch off
                this.model.power_off();
                this.model.set('switch_status', 'OFF');
            } else {
                // switch on
                this.model.power_on();
                this.model.set('switch_status', 'ON');
            }
            this.invalidate_switch_status( this.model.get('switch_status') );
        },

        on_state_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.model.set('switch_status', data.response.switch);
                this.invalidate_switch_status(this.model.get('switch_status'));
            }
        },

        invalidate_switch_status: function(status) {
            if (status=='ON') {
                // switch on
                this.$('#power-btn').removeClass('disabled')
            } else {
                // switch on
                this.$('#power-btn').addClass('disabled');
            }
        }
    });

    return SwitchControl;
});
