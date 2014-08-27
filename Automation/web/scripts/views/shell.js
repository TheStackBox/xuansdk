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
    'libs/backbone/view/shell/main.shell',
    'templates',
    'views/navigation',
    'moment'
], function ($, _, KuroboxBasicShell, JST, NavigationView, moment) {
    'use strict';

    var spr = KuroboxBasicShell.prototype;
    var ShellView = KuroboxBasicShell.extend({
        template: JST['app/scripts/templates/shell.ejs'],
        error_message: JST['app/scripts/templates/prompt.global-error.ejs'],
        initialize: function() {
            this.spinner_opt = {
                color: '#000'
            }
        },

        render: function() {
        	KuroboxBasicShell.prototype.render.apply(this, arguments);
        	this.nav = new NavigationView({el: $('.nav')});
            this.nav.render();

            //remove page margin
            $('#main-container').removeClass( "container" );

            // register function to ajax event
            this.restorePreloadingEvents();
        },

        restorePreloadingEvents: function() {
            // register ajax function
            this.removePreloadingEvents();
            $(document).ajaxStart(this.addPreloadingPage.bind(this));

            $(document).ajaxStop(this.removePreloadingPage.bind(this));
        },

        removePreloadingEvents: function() {
            
            // unregister ajax function
            $(document).unbind('ajaxStart');
            $(document).unbind('ajaxStop');

            // remove existing preload page
            this.removePreloadingPage();
        },

        removePreloadingPage: function() {
            this.show_preload(false);
            this.$('#shell-preload-dark').hide();
        },

        addPreloadingPage: function() {
            this.show_preload(true);
            this.$('#shell-preload-dark').show();
        },

        // -- global error ui handling
        
        handle_global_error: function(error, callback) {
            if (error.ajax.textStatus !== 'abort') {
                var _on_err_acknowledged = function() {
                    this.hide_message();
                    callback();
                }.bind(this)

                var error_msg = 'There\'s something wents wrong';
                var error_ref = '';

                if (error.error.code === -1) {
                    // ajax error
                    if (error.ajax.status === 0) {
                        error_msg = 'Cannot connect to Internet';
                    } else if (error.ajax.status === 404) {
                        error_msg = 'Data not found';
                    } else if (error.ajax.status === 500) {
                        error_msg = 'Internal server error';
                    } else if (error.ajax.textStatus === 'parsererror') {
                        error_msg = 'Data failed to parse';
                    } else if (error.ajax.textStatus === 'timeout') {
                        error_msg = 'Timeout';
                    } else {
                        error_ref = error.ajax.jqXHR.responseText;
                    }
                } else {
                    // api error
                    error_msg = error.error.message;
                    error_ref = 'API: '+error.error.code;
                }

                this.show_message(this.error_message({
                    message: error_msg,
                    reference: error_ref
                }), {
                    'click #ok-btn': _on_err_acknowledged
                },
                _on_err_acknowledged)
            }
        },

        _on_user_acknowledge_error_message: function() {
            this.hide_message();
        }
    });

    return ShellView;
});
