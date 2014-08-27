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
    'Kurobox',
    'models/upnp',
    'models/device'
], function ($, _, Backbone, JST, Kurobox, Upnp, DeviceModel) {
    'use strict';
    var PAIRING_TIMEOUT = 360000; // 1 min
    var RETRY_MAX = 5;

    var ModulePairingZwaveView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.pairing.zwave.ejs'],
        disable_template: JST['app/scripts/templates/module.pairing.zwave.disable.ejs'],
        busy_msg: JST['app/scripts/templates/module.pairing.busy.ejs'],
        events: {
            'click #zwave-pair-btn' : 'pair_device',
            'click #zwave-stop-pair' : 'prompt_stop_paring',
            'click #zwave-stop-unpair' : 'prompt_stop_unparing',
            'click #register-others' : 'prompt_register_others',
            'click #zwave-unpair' : 'unpair_device',
            'click #zwave-retry' : 'pair_device',
            'click #exit-options' : 'close_prompt',
        },

        initialize: function() {
        	this.collection = new Upnp.collection();
        	if (this.options.protocol === undefined) {
        		throw 'Undefined protocol id for pairing device'
        	}
        	this.render();
            Kurobox.socket.verbose = true;
        },

        render: function() {
            if (this.options.enabled) {
                if (typeof this.template !== 'undefined') {
                    $(this.el).html(this.template());
                    // reset to body position due to avoid the body scroll affected by other page 
                    $('body').scrollTop(0);
                }
            } else {
                if (typeof this.disable_template !== 'undefined') this.$el.html(this.disable_template);
            }
        },

        destroy: function() {
            $('#dark').hide();
            $('#z-wave-dark').hide();
            this.$el.empty();

            this.clear_socket_events();
        },

        clear_socket_events: function() {
            Kurobox.socket.off('socket:ZWAVE_NETWORK_REMOVE_USER_ACTION_REQUIRED');
            Kurobox.socket.off('socket:ZWAVE_NETWORK_STATUS');
            Kurobox.socket.off('socket:ZWAVE_NODE_STATUS');
            Kurobox.socket.off('socket:SCAN_DEVICE_DONE');
            Kurobox.socket.off('socket:PAIR_DEVICE');
            Kurobox.socket.off('socket:SCAN_DEVICE_ERROR_EXIST');
            Kurobox.socket.off('socket:SCAN_DEVICE_USER_ACTION_REQUIRED');
            Kurobox.socket.off('socket:SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED');
            Kurobox.socket.off('socket:SCAN_DEVICE_ERROR_UNKNOWN');
        },

        //prompt stop paring 
        prompt_stop_paring:function () {
            clearTimeout(this.pairing_timeout);
            this.pairing_timeout = undefined;

            if($('#prompt-modal').is(':hidden')){
                $('#prompt-modal:hidden').slideToggle();
                var conf = {};
                conf.title = 'stop_pair';
                conf.message = 'msg_are_u_sure_stop_pairing';
                conf.confirm_label = 'Stop';
                conf.confirm_callback = function(){

                    this.stop_pair_device();
                }.bind(this);
                conf.cancel_callback = function(){
                    //resume pairing
                    this.prepare_pairing_timeout();
                }.bind(this);
                this.trigger('prompt', conf);
            }
        },

        //prompt for stop unparing
        prompt_stop_unparing:function () {
            if($('#prompt-modal').is(':hidden')){
                $('#prompt-modal:hidden').slideToggle();
                var conf = {};
                conf.title = 'stop_unpair';
                conf.message = 'msg_are_u_sure_stop_unpairing';
                conf.confirm_label = 'btn_stop';
                conf.confirm_callback = function(){
                    //pause pairing
                    $('#z-wave-unpair').hide();
                    $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=zwave_module&method=network_abort');

                    // stop socket
                    this.clear_socket_events();
                    this.trigger('pair_cancelled');
                }.bind(this);
                conf.cancel_callback = function(){
                    //resume pairing
                }.bind(this);
                this.trigger('prompt', conf);
            }
        },

        prompt_register_others:function () {
            if($('#prompt-modal').is(':hidden')){
                $('#dark').show();
                $('#prompt-modal:hidden').slideToggle();
                var conf = {};
                conf.title = 'instruction_zwave_already_register_to_others';
                conf.message = 'msg_zwave_remove_device_from_other_b4_add';
                conf.confirm_label = 'btn_remove';
                conf.confirm_callback = function(){
                   this.unpair_device();
                }.bind(this);
                conf.cancel_callback = function(){
                    //resume pairing
                    $('#dark').hide();
                    $('#prompt-modal:not(:hidden)').slideToggle();
                }.bind(this);
                this.trigger('prompt', conf);
            }
        },

        //stop pair device
        stop_pair_device:function () {
            this.close_prompt();

            // call api
            this.stop_discover_device();
            this.clear_socket_events();

            console.log('pairing canceling from here')
            this.trigger('pair_cancelled');
        },

        close_prompt: function() {
            this.options.parent.hide_dark();
            $('#z-wave-detected').fadeOut('fast');
            $('#z-wave-pair').fadeOut('fast');
            $('#z-wave-paired').fadeOut('fast');
            $('#z-wave-dark').fadeOut('fast');
            $('#z-wave-fail').hide();
            $('#z-wave-no-response').hide();
        },

        unpair_device:function () {
            console.log('begin unpair device...')
            $('#z-wave-fail').hide();
            $('#z-wave-no-response').hide();
            
            $('#zwave-label').text('btn_remove');
            $('#zwave-sub-label').text('msg_removing');
            $('#dark').show();

            // show please wait
            this.show_please_wait();

            var device = new DeviceModel.model({protocolId: 4});
            // prepare socket
            this.clear_socket_events();
            Kurobox.socket.on('socket:ZWAVE_NETWORK_REMOVE_USER_ACTION_REQUIRED', function() {
                // remove please wait message
                this.options.parent.hide_dark();
                $('#dark').show();
                
                $('#z-wave-unpair').fadeIn('fast');
            }, this);
            Kurobox.socket.on('socket:ZWAVE_NETWORK_STATUS', function() {
                $('#z-wave-unpair').hide();
                this.clear_socket_events();

                this.trigger('unpaired');
            }, this)

            this.unpair_problematic_device({
                success: function(model, resp, options) {
                    // a device unpaired
                    console.log('force unpairing started')
                }.bind(this),
                error: function(model, resp, options) {
                    console.error('ZWave unable to get into unpair mode', resp)
                }.bind(this)
            })
        },

        prepare_pairing_timeout: function() {
            console.log('--- set pairing timeout')
            this.pairing_timeout = setTimeout(function() {
                // show no response message
                $('#z-wave-pair').hide();
                $('#z-wave-no-response').fadeIn('fast');

                // stop scanning
                this.stop_discover_device();

                // close socket
                this.clear_socket_events();

                this.trigger('pair_failed')
            }.bind(this), PAIRING_TIMEOUT);
        },

        pair_device: function() {
            console.log('pairing started...');

            this.clear_socket_events();

            $('#z-wave-fail').hide();
            $('#z-wave-paired').hide();
            $('#z-wave-no-response').hide();
            $('#zwave-label').text('btn_add');
            $('#zwave-sub-label').text('msg_adding_to_box');
            this.trigger('pairing');

            var retryCount = 0;

            this.show_please_wait();

            Kurobox.socket.on('socket:ZWAVE_NODE_STATUS', function(data) {
                // stop pairing timeout
                clearTimeout(this.pairing_timeout);
                this.pairing_timeout = undefined;

                // assume device finish scanned
                $('#z-wave-pair').fadeOut('fast');
                $('#z-wave-detected').fadeIn('fast');
            });
            Kurobox.socket.on('socket:SCAN_DEVICE_DONE', function(data) {
                // double confirm 
                if (this.pairing_timeout !== undefined) {
                    // stop pairing timeout
                    clearTimeout(this.pairing_timeout);
                    this.pairing_timeout = undefined;

                    // assume device finish scanned
                    $('#z-wave-pair').fadeOut('fast');
                    $('#z-wave-detected').fadeIn('fast');
                }
                
                // call get device list
                this.collection.fetch(this.options.protocol, {
                    success: function() {
                        // only pair single device
                        // install the device
                        if (this.collection.length > 0) {
                            var c_device = this.collection.models[0];

                            // listen to socket device pair
                            Kurobox.socket.on('socket:PAIR_DEVICE', function(data) {
                                if (data.parameter.protocolId == this.options.protocol) {
                                    // set new device id
                                    var res = data.response;
                                    c_device.set('id', res.pairedDeviceId);
                                    this.selectedIndex = 0;

                                    $('#z-wave-detected').hide();
                                    $('#device-added-success').fadeIn('fast');

                                    // close socket
                                    this.clear_socket_events();

                                    this.trigger('paired');
                                }
                            }.bind(this));

                            c_device.pair({
                                error: function(model, resp, options) {
                                    console.error('Unable to set pair device', resp)
                                    this.render_pair_device_fail();
                                    this.trigger('pair_failed', resp);
                                }.bind(this)
                            })
                        } else {
                            // the list is empty
                            console.error('Pair Device: Not able to get device list');
                            this.render_pair_device_fail();
                            this.trigger('pair_failed');
                        }

                    }.bind(this), 
                error: function(collection, resp, options) {
                    console.error('Unable to get device info', resp);
                    this.render_pair_device_fail();
                    // maybe user need to unpair the device
                    this.trigger('pair_failed', resp);
                }.bind(this)
            });
            }, this);
            Kurobox.socket.on('socket:SCAN_DEVICE_ERROR_EXIST', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    // reset dark content
                    this.options.parent.show_dark('');

                    $('#z-wave-pair').hide();
                    $('#z-wave-detected').hide();
                    $('#z-wave-paired').fadeIn('fast');

                    // clear pairing timeout
                    clearTimeout(this.pairing_timeout);
                    this.pairing_timeout = undefined;

                    this.clear_socket_events();
                }
            }, this),
            Kurobox.socket.on('socket:SCAN_DEVICE_USER_ACTION_REQUIRED', this.on_user_action_required, this)
            Kurobox.socket.on('socket:SCAN_DEVICE_ZWAVE_USER_ACTION_REQUIRED', this.on_user_action_required, this)
            Kurobox.socket.on('socket:SCAN_DEVICE_ERROR_UNKNOWN', function(data){
                if (data.parameter.protocolId == this.options.protocol) {
                    // reset dark content
                    this.options.parent.show_dark('');

                    console.warn('Unable to start device scanning');
                    if (++ retryCount < RETRY_MAX) {

                        $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol)
                    } else {
                        console.error('Unable to scan device');
                        $('#z-wave-pair').hide();
                        $('#z-wave-fail').fadeIn('fast');
                        this.trigger('pair_failed')
                    }
                }
            }, this);
            if (Kurobox.socket.connected) {
                console.warn('socket has being connected!!')
                // call scan device
                this.discover_device();
            } else {
                Kurobox.socket.on('connected', function(e) {
                    // assume socket connected
                    // call scan device
                    this.discover_device();
                }, this)
                Kurobox.socket.start();
            }
        },

        render_pair_device_fail: function() {
            $('#z-wave-pair').fadeOut('fast');
            $('#z-wave-fail').fadeIn('fast');
        },

        on_user_action_required: function(data) {
            if (data.parameter.protocolId == this.options.protocol) {
                if (this.pairing_timeout === undefined) {

                    // reset dark content
                    this.options.parent.show_dark('');

                    // show instruction
                    //pairing is progress
                    $('#z-wave-pair').fadeIn('fast');
                    $('#z-wave-dark').fadeOut('fast');
                    $('#zwave-label').text('btn_add');
                    $('#zwave-sub-label').text('msg_adding_to_box');

                    // begin pairing timeout timer
                    this.prepare_pairing_timeout();
                } else {
                    console.log('user action requested before');
                }
            }
        },

        device_model:function () {
            return this.collection.at(0);
        },

        discover_device: function() {
            console.log('begin discovery');
            $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol)
        },

        stop_discover_device: function() {
            console.log('stop discovery');
            $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan_stop&protocolId='+this.options.protocol);
        },

        unpair_problematic_device: function(options) {
            options.url = Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=zwave_module&method=network_remove';
            $.ajax(options);
        },

        show_please_wait: function() {
            this.options.parent.show_dark(this.busy_msg(), {
                'click #pairing-stop-btn': function(e) {
                    // cancel pairing?
                    this.stop_pair_device();
                }.bind(this)
            });
        }
    });

    return ModulePairingZwaveView;
});
