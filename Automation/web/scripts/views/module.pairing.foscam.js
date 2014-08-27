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
    var FoscamPairingModule = UPNPPairing.extend({
        credential_prompt_tmpl: JST['app/scripts/templates/module.pairing.foscam.cred_prompt.ejs'],
        /* override */ initialize: function() {
            if (typeof PRODUCTION === 'undefined') {
                // NOTE: due to slow response from api
                // we use uPNP protocol instead
                
                // this.options.protocol = 1;
            }
            spr.initialize.call(this);
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_INVALID_PARAMETER', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    this.show_pairing_error({title: 'error_device', message: 'error_unable_pair'});
                }
            }, this);
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_AUTHENTICATION_FAIL', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    this.show_pairing_error({title: 'error_authentication', message: 'msg_wrong_login_credential'});
                }
            }, this);
        },

        /* override */ on_server_selected: function(e) {
            var $e = $(e.currentTarget);
            this.trigger('pairing');
            var device = this.collection.get($e.data('id'));

            if (typeof PRODUCTION === 'undefined') {
                // set what you need to test
                // device.set('usernameRequired', true);
                // device.set('passwordRequired', true);
            }

            if (device.get('passwordRequired') || device.get('usernameRequired')) {
                // request for user credential
                this.on_server_selected_event = e;
                this.prompt_credential(device.get('usernameRequired'), device.get('passwordRequired'));
            } else {
                // life goes on...
                spr.on_server_selected.apply(this, arguments);
            }
        },

        prompt_credential: function(requestUsr, requestPwd) {
            console.log('required u:p', requestUsr, requestPwd);
            this.$_prompt_content = this.options.parent.show_dark(this.credential_prompt_tmpl({requestUsr: requestUsr, requestPwd: requestPwd}),
            {
                'click #cancel-btn': this.on_user_cancel_login.bind(this),
                'submit .form': this.on_user_login.bind(this),
                'keyup #user-field': this.validate_field.bind(this),
                'keyup #password-field': this.validate_field.bind(this),
            });

            this.$_prompt_content.find('.login-box').slideToggle('fast');
        },

        validate_field: function(e) {
            var $e = $(e.currentTarget);
            if ($e.val() === '') {
                $e.addClass('error-border');
            } else {
                if ($e.hasClass('error-border')) $e.removeClass('error-border');
            }

            // validate button as well
            if (this.$p('#user-field').val() !== '' && this.$p('#password-field').val() !== '') {
                this.$p('#login-btn').removeAttr('disabled', 'disabled');
            } else {
                this.$p('#login-btn').attr('disabled', 'disabled');
            }
        },

        on_user_cancel_login: function(e) {
            this.close_prompt_credential(true);
        },

        on_user_login: function(e) {
            // grab some treasure
            this.pair_info = {
                username: this.$p('#user-field').prop('value'),
                password: this.$p('#password-field').prop('value')
            }

            // close credential prompt
            this.close_prompt_credential();

            // begin to pair
            spr.on_server_selected.call(this, this.on_server_selected_event)
            return;
        },

        close_prompt_credential: function(hide_dark) {
            this.$_prompt_content.find('.login-box').slideToggle('fast', function() {
                if (hide_dark) {
                    this.options.parent.hide_dark();
                }
                this.$_prompt_content = undefined;
            }.bind(this));
        },

        $p: function(selector) {
            if (this.$_prompt_content) {
                return this.$_prompt_content.find('.login-box').find(selector);
            }
            return;
        },

        clear_socket_events: function() {
            spr.clear_socket_events.call(this);
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_INVALID_PARAMETER');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_AUTHENTICATION_FAIL');
        }
    });

    return FoscamPairingModule;
});
