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
    'Kurobox',
    'models/upnp',
    // 'eventsource'
], function ($, _, Abstract, JST, Kurobox, Upnp) {
    'use strict';
    var s = Abstract.prototype;
    var ModulePairingUpnpView = Abstract.extend({
        template: JST['app/scripts/templates/module.pairing.upnp.ejs'],
        disable_template: JST['app/scripts/templates/module.pairing.upnp.disable.ejs'],

        server_template: JST['app/scripts/templates/module.pairing.upnp.server.ejs'],
        empty_server_template: JST['app/scripts/templates/module.pairing.upnp.server_empty.ejs'],
        pairing_msg: JST['app/scripts/templates/module.pairing.pairing_msg.ejs'],
        scanning_msg: JST['app/scripts/templates/module.pairing.scanning_msg.ejs'],
        prompt_msg: JST['app/scripts/templates/module.pairing.message_prompt.ejs'],
        events: {
            'click .upnp-server-item' : 'on_server_selected',
            'click #zwave-stop-pair' : 'prompt_stop_paring',
            'click #z-wave-dark' : 'stop_paring_prompt',
            'click .nav-icon-refresh': 'refresh_list'
        },

        initialize: function() {
            s.initialize.call(this);

            console.log('initialize upnp!!!');
        	this.collection = new Upnp.collection();
            this.paired_device = undefined;

            this.clear_socket_events();

            // initialise event source
            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:SCAN_DEVICE_DONE', function(data) {
                console.log('----- SCAN_DEVICE_DONE', data.parameter.protocolId == this.options.protocol);
                if (data.parameter.protocolId == this.options.protocol) {
                    // assume device finish scanned
                    // call get device list
                    this.collection.fetch(this.options.protocol, {
                        success: function(){
                            this.options.parent.hide_dark();
                            if (this.collection.length > 0) {
                                this.render_list();
                            } else {
                                this.render_empty_list();
                            }
                        }.bind(this),
                        error: function(collection, resp, options){
                            console.error('Getting device list error', resp);
                            this.render_empty_list();
                            this.trigger('pair_failed');
                        }.bind(this)
                    });
                }

            }, this);
            Kurobox.socket.on('socket:SCAN_DEVICE_ERROR_UNKNOWN', function(data){
                console.log('Unable to start device scanning');

                if (data.parameter.protocolId == this.options.protocol) {
                    // retry
                    /*if (++retryCount < maxRetry) {
                        $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol)
                    } else {*/
                        this.options.parent.show_dark(this.prompt_msg({title: 'error_device', message: 'error_start_device_scan'}),
                        {
                            'click #confirm-button': function() {
                                this.options.parent.hide_dark();
                            }.bind(this),
                            'click .icon-close': function() {
                                this.options.parent.hide_dark();
                            }.bind(this)
                        });
                        this.trigger('pair_failed');

                        this.render_empty_list();
                    // }
                }
            }, this);
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_EXIST', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    // reset dark content
                    this.options.parent.show_dark('');

                    this.show_pairing_error({title: 'error_device', message: 'msg_x10_exist'});
                }
            }, this),
            Kurobox.socket.on('socket:PAIR_DEVICE', function(data) {
                // close dark
                if (data.parameter.protocolId == this.options.protocol) {
                    this.options.parent.hide_dark();

                    var res = data.response;
                    this.paired_device = this._target_pair_device;
                    this.paired_device.set('id', res.pairedDeviceId);
                    $('#device-added-success').fadeIn('fast');
                    $('#dark').show();

                    this.trigger('paired', this._target_pair_device);
                }
            }.bind(this))
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_UNKNOWN', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    this.show_pairing_error({title: 'error_device', message: 'error_unable_pair'});
                }
            }.bind(this))
        },

        render: function() {
            s.render.call(this);

            if (this.options.enabled) {
                _.defer(function() {
                    console.log('call scan list 1st time...');
                    this.scan_list(false);
                }.bind(this))
            }
        },

        refresh_list: function() {
            $('#list-container').empty();
            this.scan_list(true);
        },

        scan_list: function( rescan ) {
            var retryCount = 0;
            var maxRetry = 1;
            // show scanning status screen
            this.options.parent.show_dark(this.scanning_msg(), {
                'click button': function(e) {
                    // stop pairing
                    s.stop_discover_device.call(this);
                    this.options.parent.hide_dark();
                }.bind(this)
            });
            // $('#dark').show();
            
            
            $.ajax(Kurobox.host+'/cgi-bin/syb_reqresp_cgi?app_id='+Kurobox.app_id+'&module=device_manager&method=set_device_scan&protocolId='+this.options.protocol+'&rescan='+rescan)
        },

        render_list: function() {
            $('#list-container').html(this.server_template({collection:this.collection}));
        },

        render_empty_list: function() {
             $('#list-container').html(this.empty_server_template());
        },

        device_model:function () {
            return this.paired_device;
        },

        on_server_selected:function (e) {
            var $e = $(e.currentTarget);

            //paring is progress
            $('body').scrollTop( 0 );
            $('.protocol-pane').css( 'top', 50 );
            this.trigger('pairing');
            
            var device = this.collection.get($e.data('id'));

            // show pairing message
            this.options.parent.show_dark(this.pairing_msg({device: device}),
                {
                    'click #pairing-stop-btn': function(e) {
                        // cancel pairing
                        this.stop_pairing_device();
                        this.options.parent.hide_dark();
                    }.bind(this)
                });

            this.begin_pair_device(device);
        },

        begin_pair_device: function(device) {
            // listen to server socket on PAIR_DEVICE
            this._target_pair_device = device;

            if (!Kurobox.socket.connected) {
                Kurobox.socket.on('connected', function() {
                    this.call_device_pair(device);
                }.bind(this))
                Kurobox.socket.start();
            } else {
                this.call_device_pair(device);
            }
        },

        call_device_pair: function(device) {

            device.pair({
                success: function() {
                    // refer to socket response (PAIR_DEVICE & PAIR_DEVICE_ERROR_UNKNOWN)
                }.bind(this),
                error: function(model, resp, options) {
                    this.show_pairing_error({title: 'Device Error', message: 'error_unable_pair'});
                }.bind(this)
            }, this.pair_info);
        },

        show_pairing_error: function(message_obj) {
            this.options.parent.show_dark(this.prompt_msg(message_obj),
            {
                'click #confirm-button': function() {
                    this.options.parent.hide_dark();
                }.bind(this),
                'click .icon-close': function() {
                    this.options.parent.hide_dark();
                }.bind(this)
            });
            this.trigger('pair_failed');
        },

        clear_socket_events: function() {
            console.log('---- clear socket -----')
            Kurobox.socket.off('socket:SCAN_DEVICE_DONE');
            Kurobox.socket.off('socket:SCAN_DEVICE_ERROR_UNKNOWN');
            Kurobox.socket.off('socket:PAIR_DEVICE');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_UNKNOWN');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_EXIST');
        },

        destroy: function() {
            if (typeof this.collection !== 'undefined') {
                this.collection.destroy();
                this.collection = undefined;
            }

            if (typeof this.paired_device !== 'undefined') {
                this.paired_device.destroy();
                this.paired_device = undefined;
            }

            this.clear_socket_events();

            s.destroy.call(this);
        }
    });

    return ModulePairingUpnpView;
});
