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
    'libs/spin/spin'
], function ($, _, Backbone, JST, Spinner) {
    'use strict';
    var delegateEventSplitter = /^(\S+)\s*(.*)$/
    var ShellView = Backbone.View.extend({
        template: JST['app/scripts/libs/backbone/view/templates/main.shell.ejs'],
       	events: {
            'click #shell-dark': 'on_user_clicked_dark'
        },
        render: function(templateContent) {
        	if (templateContent == null) {
        		templateContent = this.template();
        	}

        	$(this.el).append(templateContent);

            var opts = _.defaults(this.spinner_opt || {}, {
                lines: 11, // The number of lines to draw
                length: 4, // The length of each line
                width: 2, // The line thickness
                radius: 5, // The radius of the inner circle
                corners: 1, // Corner roundness (0..1)
                rotate: 0, // The rotation offset
                direction: 1, // 1: clockwise, -1: counterclockwise
                color: '#FFF', // #rgb or #rrggbb or array of colors
                speed: 1, // Rounds per second
                trail: 54, // Afterglow percentage
                shadow: false, // Whether to render a shadow
                hwaccel: false, // Whether to use hardware acceleration
                className: 'spinner', // The CSS class to assign to the spinner
                zIndex: 2e9, // The z-index (defaults to 2000000000)
                top: 'auto', // Top position relative to parent in px
                left: 'auto' // Left position relative to parent in px
            })
			this.spinner = new Spinner(opts);

        	this.show_preload(true);
        },

        show_preload: function(hide) {
        	if (!hide) {
        		this.spinner.stop();
        		$("#loadingIndicator", this.el).html("");
        	} else {
        		this.spinner.spin();
        		$("#loadingIndicator", this.el).html(this.spinner.el)
        	}
        },

        show_message: function(msg_html, events, on_dark_clicked) {
            var $content = this.$el.find('#shell-dark-content');
            this._show_dark_message($content, msg_html, events, on_dark_clicked);
            $content.show();
            return $content;
        },

        hide_message: function() {
            var $content = this.$el.find('#shell-dark-content');
            this._hide_dark_message($content);
        },

        show_pop_message: function(msg_html, events, on_dark_clicked) {
            var $content = this.$('#shell-pop-content');
            this._show_dark_message($content, msg_html, events, on_dark_clicked);
            
            if ($content.is(':hidden')) {
                $content.slideToggle();
            }
            return $content;
        },

        hide_pop_message: function() {
            var $content = this.$('#shell-pop-content');
            var completeFunc = function() {
                this._hide_dark_message($content);
            }.bind(this);

            if ($content.is(':visible')) {
                $content.slideToggle({
                    duration:'fast',
                    complete: completeFunc
                });
            } else {
                completeFunc();
            }
            
        },

        on_user_clicked_dark: function(e) {
            // call dark click event
            if (this._on_dark_clicked !== undefined) {
                this._on_dark_clicked(e);
            }
        },

        _show_dark_message: function($content, msg_html, events, on_dark_clicked) {
            if (msg_html !== undefined) {
                $content.html(msg_html);
            }

            // reset events
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

            this._on_dark_clicked = on_dark_clicked;
            $('#shell-dark').show();

            return $content;
        },

        _hide_dark_message: function($content) {
            $content.off('.darkEvents' + this.cid);
            $content.empty();

            this._on_dark_clicked = undefined;

            $('#shell-dark').hide();
        }
    });

    return ShellView;
});
