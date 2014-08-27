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
    var WemoPairingModule = UPNPPairing.extend({
    	template: JST['app/scripts/templates/module.pairing.wemo.ejs'],
    	empty_server_template: JST['app/scripts/templates/module.pairing.wemo.server_empty.ejs'],
    	initialize: function() {
    		// add extra events
    		if (typeof this.events !== 'undefined') {
    			_.extend(this.events, {
    				'click #pair-btn': 'scan_list',
    				'click #refresh-btn': 'refresh_list',
                    'click #pairing-stop-btn': 'cancel_pairing'
    			})
    		}

    		WemoPairingModule.__super__.initialize.call(this);
    	},
    	render: function() {
    		this.paired_device = undefined;
    		this.$el.html(this.template());

    		// wait for user interaction
    		// refer events
    	},
        scan_list: function() {
            // move to top
            $('body').scrollTop(0);

            WemoPairingModule.__super__.scan_list.call(this,true);
        },
    	render_list: function() {
    		// turn off initial-instruction and show list
            this.$('#empty').empty();
            this.$('#empty').hide();
    		this.$('#initial-instruction').hide();
    		this.$('#list').show();

    		// super.render_list();
    		WemoPairingModule.__super__.render_list.call(this);
    	},
    	render_empty_list: function() {
    		// turn off initial-instruction and show list
            this.$('#list').hide();
    		this.$('#initial-instruction').hide();
    		this.$('#empty').show();
    		this.$('#empty').html(this.empty_server_template());
    	},
    });

    return WemoPairingModule;
});
