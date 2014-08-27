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
    'views/module.pairing.abstract',
    'templates',
    'Kurobox'
], function ($, _, Abstract, JST) {
    'use strict';
    var RETRY_MAX = 5;
    var s = Abstract.prototype;
    return Abstract.extend({
    	template: JST['app/scripts/templates/module.pairing.x10.auto.ejs'],
        disable_template: JST['app/scripts/templates/module.pairing.x10.disable.ejs'],
        busy_msg: JST['app/scripts/templates/module.pairing.busy.ejs'],
    	events: {
    		'click #pair-btn': 'on_user_add_device',
    		'click #retry-btn': 'on_user_add_device',
    		'click #stop-pair': 'on_user_stop_add_device',
    		'click #exit-options': 'on_user_close_model'
    	},
    	initialize: function() {
    		Kurobox.socket.verbose = true;
    		s.initialize.call(this);
    	},

    	device_model: function() {
    		return this.paired_device;
    	},

    	render: function() {
    		s.render.call(this);
    	},

        clear_socket_events: function() {
            Kurobox.socket.off('socket:SCAN_DEVICE_X10_USER_ACTION_REQUIRED');
            Kurobox.socket.off('socket:SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED');
            Kurobox.socket.off('socket:SCAN_DEVICE_ERROR_EXIST');
            Kurobox.socket.off('socket:SCAN_DEVICE_ERROR_UNKNOWN');
            Kurobox.socket.off('socket:SCAN_DEVICE_DONE');
            Kurobox.socket.off('socket:PAIR_DEVICE');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_UNKNOWN');
//            Kurobox.socket.off('socket:SCAN_DEVICE_X10_USER_ACTION_DETECTED');  // wong
            Kurobox.socket.off('socket:SCAN_DEVICE_USER_ACTION_TIMEOUT');   // wong syb org, is timeout
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_EXIST');
        },

    	on_user_add_device: function(e) {
    		var retryCount = 0;

            this.$('#x10-no-respond').hide();
            this.$('#x10-setup-required').hide();
            this.$('#x10-pair-failed').hide();
            this.$('#x10-no-respond').hide();

    		Kurobox.socket.on('socket:SCAN_DEVICE_X10_USER_ACTION_REQUIRED', function() {
    			// ask user to trigger button
    			
    			this.$('#dark-x10').fadeIn('fast');
    			this.$('#x10-pair').fadeIn('fast')

                // remove busy message
                this.options.parent.hide_dark();
    		}, this)

//            Kurobox.socket.on('socket:SCAN_DEVICE_X10_USER_ACTION_DETECTED', function(data){    // wong
//                console.error('-------- x10 user action detected', data)
//                this.show_generic_error();
                
//            }, this);   // wong

            Kurobox.socket.on('socket:SCAN_DEVICE_USER_ACTION_TIMEOUT', function(data){    // wong
                if (data.parameter.protocolId == this.options.protocol) {
                    // assume not receiving from device
                    this.show_timeout();
                }
                
            }, this);   // wong

    		Kurobox.socket.on('socket:SCAN_DEVICE_X10_DEVICE_SETUP_REQUIRED', function() {
    			this.$('#x10-setup-required').fadeIn('fast');
    			this.$('#x10-pair').hide();

                this.clear_socket_events();

                // remove busy message
                this.options.parent.hide_dark();
    		}, this);
    		Kurobox.socket.on('socket:SCAN_DEVICE_ERROR_EXIST', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
        			// device paired before
        			this.$('#x10-pair').hide();
        			this.$('#x10-exist').fadeIn('fast');
        			this.trigger('pair_failed')

                    // remove busy message
                    this.options.parent.hide_dark();
                }
    		}, this);
    		Kurobox.socket.on('socket:SCAN_DEVICE_DONE', function(data) {
    			if (data.parameter.protocolId == this.options.protocol) {
                    // scanning done
        			// user just pressed the button!
        			this.$('#x10-pair').hide();

        			this.collection.fetch(this.options.protocol, {
        				success: this.get_paired_device_info.bind(this),
        				error: this.get_paired_device_info_failed.bind(this)
        			})

                    // remove busy message
                    this.options.parent.hide_dark();
                }
    		}, this);
    		Kurobox.socket.on('socket:SCAN_DEVICE_ERROR_UNKNOWN', function(data){
                if (data.parameter.protocolId == this.options.protocol) {
                    console.warn('Unable to start device scanning');
                    if (++ retryCount < RETRY_MAX) {
                    	this.discover_device();
                    } else {
                        console.error('Unable to scan device');
                        this.trigger('pair_failed')
                    }
                }
            }, this);

            this.options.parent.show_dark(this.busy_msg(), {
                'click #pairing-stop-btn': function(e) {
                    // cancel pairing?
                    this.on_user_stop_add_device();
                }.bind(this)
            });

            this.discover_device();
    	},

    	on_user_stop_add_device: function(e) {
    		this.stop_discover_device();
    		this.on_user_close_model();

            // remove busy message
            this.options.parent.hide_dark();
    	},

    	on_user_close_model: function(e) {
    		this.$('#x10-pair').hide();
    		this.$('#x10-setup-required').hide();
    		this.$('#x10-pair-failed').hide();
            this.$('#x10-exist').hide();
    		this.$('#x10-no-respond').hide();
    		this.$('#dark-x10').fadeOut('fast');

    		this.clear_socket_events();
    	},

    	get_paired_device_info: function() {
    		// got the device infos
    		// pair the first one
    		this.paired_device = this.collection.models[0];

    		Kurobox.socket.on('socket:PAIR_DEVICE', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
        			// the device has being paired with system
        			var res = data.response;
        			this.paired_device.set('id', res.pairedDeviceId);

        			this.clear_socket_events();

        			this.trigger('paired')
                }
    		}, this);

    		Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_UNKNOWN', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
        			console.error('pair device socket error', data)
        			this.show_generic_error();
                }
    		}, this);

//            Kurobox.socket.on('socket:SCAN_DEVICE_X10_USER_ACTION_DETECTED', function(data){    // wong
//                console.error('x10 user action detected', data)
//                this.show_generic_error();
//                
//            }, this);   // wong

    		Kurobox.socket.on('socket:SCAN_DEVICE_USER_ACTION_TIMEOUT', function(data){
                if (data.parameter.protocolId == this.options.protocol) {
        			console.error('timeout', data)
        			this.show_generic_error();
    			}
    		}, this);

            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_EXIST', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    console.error('exist before', data)
                    this.$('#x10-exist').fadeIn('fast');
                    this.$('#x10-pair').hide();
                    this.$('#x10-setup-required').hide();

                    // remove please wait message?
                    this.options.parent.hide_dark();

                    this.clear_socket_events();
                    this.trigger('pair_failed');
                }
            }, this)

    		// pair it
    		this.paired_device.pair({
    			error: function(model, resp) {
    				console.error('Unable to set pair device', resp)
    				this.show_generic_error();
    			}.bind(this)
    		})
    	},

    	get_paired_device_info_failed: function(model, resp) {
    		// unable to get device list
    		console.error('unable to get pair device list', resp)
    		this.show_generic_error();
    	},

    	show_generic_error: function() {
    		this.$('#x10-pair').hide();
    		this.$('#x10-setup-required').hide();
            this.$('#x10-exist').hide();
    		this.$('#x10-pair-failed').fadeIn('fast');

    		this.clear_socket_events();

            this.options.parent.hide_dark();
    		this.trigger('pair_failed');
    	},

        show_timeout: function() {
            this.$('#x10-pair').hide();
            this.$('#x10-setup-required').hide();
            this.$('#x10-exist').hide();
            this.$('#x10-no-respond').fadeIn('fast');

            this.clear_socket_events();

            this.options.parent.hide_dark();
            this.trigger('pair_failed');
        }
    });
});