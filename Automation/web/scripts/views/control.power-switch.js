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
    'models/control.power-switch'
], function (_, AbstractCtrl, JST, Kurobox, PowerSwitchModel) {
    'use strict';

    var spr = AbstractCtrl.prototype;
    var SwitchControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.power-switch.ejs'],
        template_item: JST['app/scripts/templates/control.power-switch.item.ejs'],
        model_class: PowerSwitchModel.model,
        events: {
            'click #power-btn': 'on_user_toggle_switch'
        },

        destroy: function() {
            spr.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function( data) {
            spr.init();
           
            this.info = new Object();
            this.info = data.response.status.status;

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:POWER_STRIP_CONTROLLER_STATE_CHANGED', this.on_status_changed, this);
            Kurobox.socket.start();

            this.$('#main_content').append(this.template_item({info: this.info}));
        },

        on_user_toggle_switch: function(e) {
            var index = $(e.target).data('id');
       
            var status = this.info[index].switch;
            if (status=='ON') {
                // switch off
                this.model.power_off(index);
                this.info[index].switch = 'OFF';
            } else if (status=='OFF') {
                // switch on
                this.model.power_on(index);
                this.info[index].switch = 'ON';
            }

            console.log('this.info[index].switch', this.info[index].switch);
            console.log('index', index);

            this.invalidate_switch_status(this.info[index].switch, index);
        },

        on_status_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                for(var i=0; i<data.response.status.length; i++)
                {
                    console.log(data.response.status[i])
                    if( data.response.status[i].switch=="OFF" || data.response.status[i].switch=="ON")
                        this.info[data.response.status[i].index].switch = data.response.status[i].switch;

                    if( data.response.status[i].meter!=='' )
                        this.info[data.response.status[i].index].meter = data.response.status[i].meter;

                    this.invalidate_switch_status( this.info[data.response.status[i].index].switch, data.response.status[i].index )
                }
            }
        },

        invalidate_switch_status: function(status,index) {

            if (status=='ON') {
                // switch on
                this.$('#power-btn[data-id='+index+']').removeClass('disabled')
            } else if (status=='OFF') {
                // switch off
                this.$('#power-btn[data-id='+index+']').addClass('disabled');
            }
        }
    });

    return SwitchControl;
});
