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
    'templates'
], function ($, _, Backbone, JST) {
    'use strict';

    var NavigationView = Backbone.View.extend({
        NAV_HOME : 'nav-home',
        ADD_RULE : 'nav-circle-add nav-icon-add',
        EDIT_RULE : 'nav-circle-edit nav-icon-edit',
        EXIT_EDIT_RULE : 'nav-circle-done nav-icon-done',
        SAVE_RULE : 'nav-circle-done nav-icon-done',
        BACK : 'nav-icon-back',
        ADVANCE : 'nav-circle-done nav-icon-advance',

    	template: JST['app/scripts/templates/navigation.ejs'],
    	icon_tpl: JST['app/scripts/templates/nav-item.ejs'],
    	events: {
    		'click #nav-button': 'on_nav_button_clicked'
    	}, 

        show: function() {
            this.$el.show();
        },

        hide: function() {
            this.$el.hide();
        },

    	render: function() {
    		$(this.el).html(this.template());
    		return this;
    	},

        update_buttons: function(left_pane_setting, right_pane_setting, callback) {
        	if (left_pane_setting !== undefined) {
                this.update_button_set('.nav-left', left_pane_setting)
            }
            if (right_pane_setting !== undefined) {
                this.update_button_set('.nav-right', right_pane_setting)
            }

        	if (callback !== undefined) {

                this.callback = callback;
            }
        },

        update_button_set: function(el, buttons_item) {
            $(el).empty();

            var item_el;

            _.each(buttons_item, function(item){
                item_el = this.icon_tpl({item: this[item]});
                $(el).append(item_el);
                // click event: on_nav_button_clicked
            }.bind(this));
        },

        on_nav_button_clicked: function(evt) {
        	if (this.callback !== undefined) this.callback($(evt.currentTarget).data('item'), this);
        },

        update_title:function(title) {
        	//if (title !== undefined) $('#nav-title').text(title.toUpperCase());
            if (title !== undefined) $('#nav-title').text(title);
        }
    });

    return NavigationView;
});
