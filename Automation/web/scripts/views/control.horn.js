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
    'models/control.horn'
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';

    var spr = AbstractCtrl.prototype;
    var HornControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.horn.ejs'],
        model_class: Model,
        events: {
            'click #power-btn': 'on_user_toggle_switch'
        },

        destroy: function() {
            spr.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function( data) {
            spr.init();
           
            this.horn_stat = data.response.status.horn;

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:HORN_CONTROLLER_STATE_CHANGED', this.on_state_changed, this);
            Kurobox.socket.start();

            this.invalidate_horn_status(this.horn_stat);
        },

        on_user_toggle_switch: function(e) {
            if (this.horn_stat=='ON') {
                // switch off
                this.model.power_off();
                this.horn_stat = 'OFF';
            } else {
                // switch on
                this.model.power_on();
                this.horn_stat = 'ON';
            }
            
            this.invalidate_horn_status( this.horn_stat );
        },

        on_state_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                console.log(data.response);
                this.horn_stat = data.response.horn;
                this.invalidate_horn_status(this.horn_stat);
            }
        },

        invalidate_horn_status: function(status) {
             if (status=='ON') {
                // switch on
                this.$('#power-btn').html('&#xe6a6');
                this.$('#power-btn').removeClass('disabled')
            } else {
                // switch off
                this.$('#power-btn').html('&#xe6a5');
                this.$('#power-btn').addClass('disabled');
            }
        }
    });

    return HornControl;
});
