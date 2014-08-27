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
    'models/control.door-lock'
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';

    var LOW_VALUE = 10;

    var spr = AbstractCtrl.prototype;
    var SpeakerControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.door-lock.ejs'],
        model_class: Model,
        events: {
            'click #lock-btn': 'on_user_toggle_door_lock'
        },

        destroy: function() {
            this.model.off();
            this.model.destroy();
            spr.destroy.call(this);
            Kurobox.socket.stop();
            
        },

        init: function( data) {
            spr.init();
           
            this.info = new Object();
            this.info = data.response.status.status;

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:DOOR_LOCK_CONTROLLER_STATE_CHANGED', this.on_status_changed, this);
            Kurobox.socket.start();

            this.batteryBarWidth = this.$('.battery-bar').width();
            
            this.batteryStat = data.response.status.battery;
            this.invalidate_battery_status(this.batteryStat);
            
            this.lockStat = data.response.status.doorLock;
            this.invalidate_door_lock(this.lockStat);
        },

        invalidate_battery_status: function(battery_level) {
            // update bar
            var w = battery_level/100 * this.batteryBarWidth;
            this.$('.battery-bar').css('width', w);

            // update percentage
            this.$('#battery-level').text(battery_level+'%')

            if (battery_level <= LOW_VALUE) {
                this.$('.battery-bar').css('background-color', '#c60202');
            } else {
                this.$('.battery-bar').css('background-color', '');
            }
        },

        on_user_toggle_door_lock: function(e) {
            if (this.lockStat=='LOCK') {
                // unlock the door
                this.model.unlock();
                this.lockStat = 'UNLOCK';
            } else {
                // lock the door
                this.model.lock();
                this.lockStat = 'LOCK';
            }
            this.invalidate_door_lock(this.lockStat);
        },

        invalidate_door_lock: function(locked) {
            if (this.lockStat=='LOCK') {
                // door locked
                this.$('#lock-btn').html('&#xe680');
                this.$('#lock-btn').removeClass('disabled')
            } else {
                // door unlocked
                this.$('#lock-btn').html('&#xe681');
                this.$('#lock-btn').addClass('disabled');
            }
        },

        on_status_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.lockStat = data.response.doorLock;
                this.invalidate_door_lock(this.lockStat);
                
                this.batteryStat = data.response.battery;
                this.invalidate_battery_status(this.batteryStat);
            }
        }
    });

    return SpeakerControl;
});
