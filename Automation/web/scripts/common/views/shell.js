/**
* Copyright 2014-2015 Cloud Media Sdn. Bhd.
*
* This file is part of Xuan Automation Application.
*
* Xuan Automation Application is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* Xuan Automation Application is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
*/
/*global define*/

define([
    'jquery',
    'underscore',
    'libs/backbone/view/shell/main.shell',
    'templates',
    'common/views/navigation',
    'moment'
], function ($, _, KuroboxBasicShell, JST, NavigationView, moment) {
    'use strict';

    var spr = KuroboxBasicShell.prototype;
    var ShellView = KuroboxBasicShell.extend({
        template: JST['app/scripts/common/templates/shell.ejs'],
        error_message: JST['app/scripts/common/templates/prompt.global-error.ejs'],
        initialize: function() {
        },

        render: function() {
        	KuroboxBasicShell.prototype.render.apply(this, arguments);
            delete this.spinner;

            this.nav = new NavigationView({el: $('.nav')});
            this.nav.render();

            //remove page margin
            $('#main-container').removeClass( "container" );

            // register function to ajax event
            this.restorePreloadingEvents();

        },

        show_preload: function(hide) {
            if (!hide) {
                // this.spinner.stop();
                $("#spin_holder").hide();
                this.$('#shell-preload-dark').hide();
            } else {
                // this.spinner.spin();
                $("#spin_holder").show();
                this.$('#shell-preload-dark').show();
            }
        },

        restorePreloadingEvents: function() {
            // register ajax function
            this.removePreloadingEvents();
            $(document).ajaxStart(this.addPreloadingPage.bind(this));
            $(document).ajaxStop(this.removePreloadingPage.bind(this));
            console.error('>>>> restore preload!')
        },

        removePreloadingEvents: function() {
            // unregister ajax function
            console.error('>>>> remove preload!')
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
            callback = callback || function() {}
            if (error.ajax.textStatus !== 'abort') {
                var _on_err_acknowledged = function() {
                    this.hide_message();
                    callback();
                }.bind(this)

                var error_msg = 'error_something_went_wrong';
                var error_ref = '';

                if (error.error.code === -1) {
                    // ajax error
                    if (error.ajax.status === 0) {
                        error_msg = 'error_network_error';
                    } else if (error.ajax.status === 404) {
                        error_msg = 'Data not found';
                    } else if (error.ajax.status === 500) {
                        error_msg = 'error_not_found';
                    } else if (error.ajax.textStatus === 'parsererror') {
                        error_msg = 'error_data_parse_failure';
                    } else if (error.ajax.textStatus === 'timeout') {
                        error_msg = 'error_timeout';
                    } else {
                        error_ref = error.ajax.jqXHR.responseText;
                    }
                } else {
                    // api error
                    error_msg = error.error.message;
                    error_ref = 'Err '+error.error.code;
                }
                // define height for overflow-y= scroll
                var screenHeight= $( window ).height();
                this.$('.message').css('height', screenHeight);

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
