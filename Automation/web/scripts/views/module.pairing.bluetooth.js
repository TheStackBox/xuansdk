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
    'templates',
    'models/upnp'
], function ($, _, Backbone, UPNPPairing, JST, UPnp) {
    'use strict';

    var spr = UPNPPairing.prototype;    
    var ModulePairingBluetoothView = UPNPPairing.extend({
        disable_template: JST['app/scripts/templates/module.pairing.bluetooth.disable.ejs'],
        initialize: function() {
            spr.initialize.call(this);
            // fetch list again to render
            var _refetching_list = function() {
                this._fetch_list_and_render(function() {
                    // assume it success
                    // show data
                    this.render_list();
                }.bind(this));
            }.bind(this)

            // remove base setting on scan device done
            Kurobox.socket.off('socket:SCAN_DEVICE_DONE');
            Kurobox.socket.on('socket:SCAN_DEVICE_DONE', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    // assume device finish scanned
                    // call get device list
                    _refetching_list();
                }
            }, this);

            Kurobox.socket.on('socket:SCAN_DEVICE_BLUETOOTH_FOUND', function(data) {
                // call fetch list
                if (data.parameter.protocolId == this.options.protocol) {
                    _refetching_list();
                }
            }, this);
        },

        _fetch_list_and_render: function(success, error) {
            var opt = {}
            opt.success = success;
            if (!error) {
                opt.error = success;
            }
            opt.skipGlobalError = true;

            this.collection.fetch(this.options.protocol, opt);
        },

    	scan_list: function( rescan ) {

            // render data to ui
            var _render_list = function() {
                if (this.collection.length > 0) {
                    this.render_list();
                } else {
                    // TODO: show empty message
                    // this.render_empty_list();
                }
            }.bind(this);

            var _begin = function() {
                // show data to ui
                _render_list();
            }

            // get list from cached list
            /*if (rescan === false) {
                // get from cache list
                this.collection = new UPnp.collection();
                _begin();
            } else {
                // get from non cache
                this._fetch_list_and_render(function() {
                    _begin();
                }.bind(this));
            }*/
            // let's begin
            _begin();
            
            // call scan device
            $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol+'&rescan='+rescan)
 
        },

        begin_pair_device: function(device_id) {
            this.stop_discover_device();
            spr.begin_pair_device.call(this, device_id);
        },

        clear_socket_events: function() {
            spr.clear_socket_events.call(this);
            Kurobox.socket.off('socket:SCAN_DEVICE_BLUETOOTH_FOUND');
        },
    });

    return ModulePairingBluetoothView;
});
