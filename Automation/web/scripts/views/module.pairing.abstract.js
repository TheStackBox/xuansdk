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
    'templates',
    'models/upnp'
], function ($, _, Backbone, JST, Upnp) {
    'use strict';

    return Backbone.View.extend({
    	initialize: function() {
    		if (this.options.protocol === undefined) throw 'Undefined protocol id for pairing device'
            this.collection = new Upnp.collection();
            this.render();
    	},

        render: function() {
            if (this.options.enabled) {
                if (typeof this.template !== 'undefined') $(this.el).html(this.template());
            } else {
                if (typeof this.disable_template !== 'undefined') this.$el.html(this.disable_template);
            }
        },

        discover_device: function() {
            this.device_xhr = $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol)
        },

        stop_discover_device: function() {
            this.device_xhr = $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan_stop&protocolId='+this.options.protocol);
        },

        stop_pairing_device: function() {
            this.device_xhr = $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_pair_abort&protocolId='+this.options.protocol);
        },

        device_model: function() {
            return this.collection.at(0);
        },

        destroy: function() {
            if (typeof this.device_xhr !== 'undefined') this.device_xhr.abort();

            // stop scanning
            this.stop_discover_device();

            this.$el.empty();
            this.undelegateEvents();
        }
    });
});