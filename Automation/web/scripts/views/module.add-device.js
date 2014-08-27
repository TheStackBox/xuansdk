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
    'models/protocol',
    'views/module.add-device.protocol-selector',
    'views/module.pairing.zwave',
    'views/module.pairing.upnp',
    'views/module.pairing.bluetooth',
    'views/module.pairing.wifi-hue',
    'views/module.pairing.wemo',
    'views/module.pairing.x10.auto',
    'views/module.pairing.x10.manual',
    'views/module.pairing.foscam',
    'Kurobox'
], function ($, _, Backbone, JST, DeviceProtocol, DeviceProtocolSelector, ZwavePairingModule, UpnpPairingModule, BluetoothPairingModule, WifiHuePairingModule, WemoPairingModule, X10AutoPairingModule, X10ManualPairingModule, FoscamPairingModule) {
    'use strict';
    var delegateEventSplitter = /^(\S+)\s*(.*)$/
    var ModuleAddDeviceView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.add-device.ejs'],
        events: {
            'click #success-added-btn' : 'on_device_paired_comfirm',
            'click #success-unpair-btn' : 'on_device_unpaired_confirm',
        },

        pairing_module_conf: {
            '1': UpnpPairingModule,
            '2': BluetoothPairingModule, //bluetooth
            '3': WifiHuePairingModule,
            '4': ZwavePairingModule,
            '5': WemoPairingModule,
            '6': X10AutoPairingModule,
            '7': X10ManualPairingModule,
            '8': FoscamPairingModule,
      	},

        hide: function() {
            this.reset();
            $(this.el).hide();

            this.$('#protocol-setup').empty();
            this.hide_dark();

            // enable global preloading
            Shell.restorePreloadingEvents();

            if (this.protocol_selector !== undefined) {
                this.protocol_selector.reset();
                this.protocol_selector = undefined;
            }

            // clear model
            if (this.protocols !== undefined) this.protocols.destroy();

            // stop socket
            Kurobox.socket.stop();
        },

        show: function() {
            $(this.el).fadeIn('fast');

            // disable global preloading
            Shell.removePreloadingEvents();

            // connect socket
            Kurobox.socket.verbose = true;
            
            // prepare event listener
            Kurobox.socket.on('socket:DEVICE_MANAGER_PROTOCOL_ENABLED', this.on_protocol_updated, this);
            Kurobox.socket.on('socket:DEVICE_MANAGER_PROTOCOL_DISABLED', this.on_protocol_updated, this);

            Kurobox.socket.start();
        },

        render: function() {
        	$(this.el).html(this.template());
        },

        reset: function() {
            $(this.el).scrollTop(0);
            if (this.protocol_selector !== undefined) {
                this.protocol_selector.reset();
            }
            if (this.pairing_module !== undefined) {
                this.pairing_module.destroy();
                this.pairing_module = undefined;
            }
            this.prompt_message('hide');
        },

        navigate: function(uid) {
            this.uid = uid;

            console.log('-- test protocol selector', this.protocol_selector);
            if (this.protocol_selector === undefined) {
                // initialise types of supported protocol
                this.protocols = new DeviceProtocol.collection();
                this.protocols.fetch({
                    success: function(model, resp, options) {
                        // render protocol selector
                        this.protocol_selector = new DeviceProtocolSelector({
                            list: this.protocols
                        });
                        $('#protocol-select').html(this.protocol_selector.el);
                        $('.protocol-pane').css( 'top', 55 );
                        this.protocol_selector.on('select', this.user_select_protocol, this);

                        // invalidate pairing module
                        if (uid !== null) {
                            this._invalidate_pairing_module(uid);
                        } else {
                            // render template
                            //reinit choose protocols list UI 
                            $('#protocol-setup').html(this.template());
                        }
                    }.bind(this),
                    error: function(model, resp, options) { 
                        console.log('Unable to retrieve protocols', resp.error.code, resp.error.message);
                    }.bind(this)
                })

                if (uid === null) {
                    // clear up pairing content
                    this.$('#protocol-setup').html('');
                }
            } else {
                if (uid !== undefined) {
                    // initialising module
                    this._invalidate_pairing_module(uid)
                }
            }
        },

        _invalidate_pairing_module: function(protocol_id) {
            // initialise pairing module 
            if (this.pairing_module !== undefined) {
                if (this.pairing_module.options.protocol !== protocol_id) {
                    // destroy module
                    this.pairing_module.destroy();
                    this.pairing_module = undefined
                }
            }
            // no pairing module has being set
            console.log('-- protocol enabled', this.protocols.get(protocol_id).get('enabled'))
            this.pairing_module = new this.pairing_module_conf[protocol_id]({protocol: protocol_id, parent: this, enabled: this.protocols.get(protocol_id).get('enabled')});
            this.pairing_module.on('pairing', this.on_device_pairing, this);
            this.pairing_module.on('pair_failed', this.on_device_error_pair, this);
            this.pairing_module.on('pair_cancelled', this.on_device_cancel_pair, this);
            this.pairing_module.on('paired', this.on_device_paired, this);
            this.pairing_module.on('unpaired', this.on_device_unpaired, this);
            this.pairing_module.on('prompt', this.prompt, this);

            $('#protocol-setup').html(this.pairing_module.el);
        },

        user_select_protocol: function(protocol_id) {
        	console.log('protocol_id '+ protocol_id);
        	if (this.pairing_module_conf[protocol_id] !== undefined) {
        		location.replace('#/device/add/'+protocol_id);
        	}
        },

        prompt:function (conf) {

            // conf.confirm_callback = function(){
            //     conf.confirm_callback();                
            // }.bind(this);
            // conf.cancel_callback = function(){
            //     conf.cancel_callback();                
            // }.bind(this);
            this.prompt_message(conf);
        },

        on_device_paired_comfirm:function () {
            $('#device-added-success').hide();
            $('#dark').hide();
            this.trigger('paired', this.pairing_module.device_model().clone());
            this.pairing_module.destroy();
            this.pairing_module = undefined;

        },

        on_device_paired: function() {
            // assume device has being pair
            console.log('added!!!!')
            $('body').scrollTop( 0 );
            $('#device-added-success').show();
            $('#dark').show();
            $('#success-label').html('msg_added_success');
            $('#success-sub-label').html('msg_ready_use');            
        },
        
        on_device_unpaired: function() {
            // assume device has being pair
            $('body').scrollTop( 0 );
            $('#device-unpair-success').show();
            $('#dark').show();
        },

        on_device_unpaired_confirm: function() {
            $('#device-unpair-success').hide();
            $('#dark').hide();
            $('body').scrollTop( 0 );
            this.trigger('unpaired');
        },

        on_device_pairing: function() {
            // assume device has being pair
            //$('#dark').show();
            this.trigger('pairing');
        },

        on_device_error_pair: function() {
            // device is pair failed
            $('body').scrollTop( 0 );
            this.trigger('pair failed');
        },

        on_device_cancel_pair: function() {
            // device is pair failed
            $('body').scrollTop( 0 );
            $('#dark').hide();
        },

        stop_paring: function() {
            this.pairing_module.stop_pair_device();
            this.prompt_message('hide');
        },

        cancel_stop_paring: function() {
            this.prompt_message('hide');
            window.location = '#/device/add/'+this.uid;
        },

        prompt_message: function() {
            var action = 'show';
            var conf = {
                confirm_label: 'btn_ok',
                cancel_label: 'btn_cancel',
                confirm_callback: undefined,
                cancel_callback: undefined
            };

            if (typeof arguments[0] === 'string') {
                action = arguments[0];
            } else {
                _.extend(conf, arguments[0]);

                // fill in the blank
                $('#myModalLabel').text(conf.title || '');
                $('#modal-body').text(conf.message || 'msg_are_u_sure');
                $('#modal-cancel-btn').text(conf.cancel_label);
                $('#modal-ok-btn').text(conf.confirm_label);
            }

            // execute action
            // NOTE: prompt callback is handle in device.js
            $('#prompt-modal').data('confirm_cb', conf.confirm_callback);
            $('#prompt-modal').data('cancel_cb', conf.cancel_callback);
            // $('#prompt-modal').modal(action);
            console.log('action prompt = '+  action)
            if (action === 'show') {
                //$('#dark:not(:visible)').show();
                $('#prompt-modal').show();
            } else {
                //$('#dark').hide();
                $('#prompt-modal').hide();
                console.log('test prompt modal = '+$('#prompt-modal').length);
            }
        },

        show_dark: function(msg_html, events) {
            var $content = this.$el.find('#dark-content');
            if (msg_html !== undefined) {
                $content.html(msg_html);
            }

            // reset events
            var $content = this.$el.find('#dark-content');
            $content.off('.darkEvents' + this.cid);

            // delegate event inside dark content
            if (events) {
                for (var key in events) {
                    var method = events[key];
                    var match = key.match(delegateEventSplitter);
                    var eventName = match[1], selector = match[2];
                    method = _.bind(method, this);
                    eventName += '.darkEvents' + this.cid;
                    if (selector !== '') {
                      $content.on(eventName, selector, method);
                    }
                }
            }
            $content.show();

            $('#dark').show();

            return $content;
        },

        hide_dark: function() {
            var $content = this.$el.find('#dark-content');
            $content.off('.darkEvents' + this.cid);
            $content.empty();

            $('#dark').hide();
        },

        on_protocol_updated: function(data) {
            var enable = (data.eventTag === 'DEVICE_MANAGER_PROTOCOL_ENABLED');
            console.log('-- data enable', enable)
            this.protocol_selector.update(enable, data.response.protocolId);

            console.log('pid', this.uid, data.response.protocolId);
            if (this.uid == data.response.protocolId) {
                this._invalidate_pairing_module(this.uid);
            }
        }

    });

    return ModuleAddDeviceView;
});
