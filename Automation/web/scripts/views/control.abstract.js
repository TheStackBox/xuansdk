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
    'underscore',
    'backbone',
    'libs/spin/spin',
], function (_, Backbone, Spinner) {
    'use strict';

    var AbstractDeviceControl = Backbone.View.extend({
        initialize: function() {
            if (this.events !== undefined) {
                this.events['click #refresh-btn'] = 'on_refresh';
            }
        },

        render: function() {
            if (this.template !== undefined) {
                this.$el.html(this.template({
                    device: this.options.device
                }));
                Shell.removePreloadingEvents();
                var opts = {
                    lines: 11, // The number of lines to draw
                    length: 4, // The length of each line
                    width: 2, // The line thickness
                    radius: 5, // The radius of the inner circle
                    corners: 1, // Corner roundness (0..1)
                    rotate: 0, // The rotation offset
                    direction: 1, // 1: clockwise, -1: counterclockwise
                    color: '#000', // #rgb or #rrggbb or array of colors
                    speed: 1, // Rounds per second
                    trail: 54, // Afterglow percentage
                    shadow: false, // Whether to render a shadow
                    hwaccel: false, // Whether to use hardware acceleration
                    className: 'spinner2', // The CSS class to assign to the spinner
                    zIndex: 2e9, // The z-index (defaults to 2000000000)
                    top: 'auto', // Top position relative to parent in px
                    left: 'auto' // Left position relative to parent in px
                };
                this.spinner = new Spinner(opts);
            }

            // constructing model
            if (this.model_class === undefined) throw 'Undefined model class';
            this.model = new this.model_class({id: this.options.device.get('id')});
            this.get_initial_data();
        },

        get_initial_data: function() {
            // spin the ass
            this.$("#main_loader").show();
            this.spinner.spin();
            this.$("#main_loader").html(this.spinner.el)

            if (this.model.get_capabilities === undefined) throw 'Undefined get_capabilities function in model';
            if (this.model.get_status === undefined) throw 'Undefined get_status function in model';
            this.model.get_capabilities({
                skipGlobalError: true,
                success: function(m, r, o) {
                    var enabled = r.response.enabled;
                    
                    this.spinner.stop();
                    $("#main_loader", this.el).html("");
                    this.$("#main_loader").hide();

                    if (enabled) {
                        this.model.get_status({
                            skipGlobalError: true,
                            success: function(m, r, o) {
                                // assume we can get control panel's data
                                this.$("#main_content").show();
                                this.init(r);
                            }.bind(this),
                            error: function() {
                                this.render_error();
                            }.bind(this)
                        })
                    } else {
                        this.render_error();
                    }
                }.bind(this),
                error: function() {
                     this.spinner.stop();
                    $("#main_loader", this.el).html("");
                    this.$("#main_loader").hide();
                    
                    this.render_error();
                }.bind(this)
            })
        },

        render_error: function() {
            this.$("#main_message").show();
        },

        init: function() {

        },

        on_refresh: function(){
            this.$("#main_message").hide();
            this.spinner.spin();
            this.$("#main_loader").html(this.spinner.el)
            this.get_initial_data();
        },

        destroy: function() {
            // restore global preloading events
            Shell.restorePreloadingEvents();
            
            if (typeof this.model !== 'undefined') {
                this.model.destroy();
                this.model = undefined;
            }
            if (this.$el !== undefined) this.$el.empty();
            this.undelegateEvents();
        }

    });

    return AbstractDeviceControl;
});
