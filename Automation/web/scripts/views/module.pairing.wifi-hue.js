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
    'backbone',
    'views/module.pairing.upnp',
    'templates'
], function ($, _, Backbone, UPNPPairing, JST) {
    'use strict';

    var spr = UPNPPairing.prototype;
    var ModulePairingWifiHueView = UPNPPairing.extend({
    	user_trigger_msg: JST['app/scripts/templates/module.pairing.hue.require_user_trigger.ejs'],
        initialize: function() {
            spr.initialize.call(this);

            Kurobox.socket.on('socket:SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED', function(data){
                if (data.parameter.protocolId == this.options.protocol) {
                    // show message to ask user
                    // to trigger button
                    this.options.parent.show_dark(this.user_trigger_msg(), {
                        'click #zwave-stop-pair': function(e) {
                            // stop pairing
                            spr.stop_discover_device.call(this);
                            if (Kurobox.socket.connected) Kurobox.socket.stop();
                            this.options.parent.hide_dark();
                        }.bind(this)
                    });
                }
            }, this);
            Kurobox.socket.on('socket:SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    // begin scan hue
                    // show scanning status screen
                    this.options.parent.show_dark(this.scanning_msg(), {
                        'click button': function(e) {
                            // stop pairing
                            spr.stop_discover_device.call(this);
                            if (Kurobox.socket.connected) Kurobox.socket.stop();
                            this.options.parent.hide_dark();
                        }.bind(this)
                    });
                }

            }, this);
        },

        clear_socket_events: function() {
            Kurobox.socket.off('socket:SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_DETECTED');
            Kurobox.socket.off('socket:SCAN_DEVICE_WIFI_PHILIPHUE_USER_ACTION_REQUIRED');
        },
    });

    return ModulePairingWifiHueView;
});
