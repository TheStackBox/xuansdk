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
    'views/module.rule.device-setting.abstract-view',
    'templates',
    'views/component.control.toggle',
    'models/kbx.toggle'
], function ($, _, AbstractRuleDeviceSettingView, JST, kbxToggleComponentView, kbxToggle) {
    'use strict';
    var ID = '__ui_method_enable';
    var spr = AbstractRuleDeviceSettingView.prototype;
    var MethodEnablerView = AbstractRuleDeviceSettingView.extend({
    	method_header: JST['app/scripts/templates/module.rule.device-setting.method-header.ejs'],
        close: function() {
            this.activation_model = undefined;
            spr.close.call(this)
        },

    	render: function(method_id, device, user_methods, activation_model) {
    		this.method_id = method_id;
    		this.device = device;
    		this.user_methods = user_methods;
            this.activation_model = activation_model;

    		// render template and header
    		spr.render.call(this);

    		// render component
    		this.render_component();

    		// render action buttons
    		this.render_action_buttons(this.$('#footer'), {
                'reset-btn': 'on_user_reset',
                'done-btn': 'on_user_done'
            });

            
            console.log('testing reset btn', this.$('#footer > #reset-btn'))
            // swtch to 1 btn css 
            this.$('#footer #action-buttons').attr( "class", 'btn-1-stretch' );
            // remove reset button
            this.$('#footer #reset-btn').remove();
    	},

    	render_component: function() {
    		// prepare activation content
            this.activation_content = new kbxToggleComponentView({el: this.$('#setting-content')});

    		// render
            this.activation_content.render(this.activation_model);

    	},

    	render_header: function() {
    		return this.method_header({model: this.device, method: this.device.get('methods').get(this.method_id)});
    	},

    	/*
    	on_user_reset: function(e) {
            // literally remove method
            var modal = this.user_methods.get(this.method_id);
            this.user_methods.remove(modal);

            this.trigger('reset', this.method_id);
        },*/

        on_user_navigate_back: function() {
        	this.trigger('cancel', this.method_id);
        },

        on_user_done: function(e) {
        	/*
        	var modal;
        	if (this.activation_content.get_value() === true) {
	            if (!this.user_methods.get(this.method_id)) {
	            	// clone one from device
		            modal = this.device.get('methods').get(this.method_id).clone();
		            this.user_methods.add(modal)
	            }
        	} else {
        		// remove from list
        		modal = this.user_methods.get(this.method_id);
        		if (modal !== undefined) {
            		this.user_methods.remove(modal);
        		}
        	}*/
            this.trigger('done', this.method_id, this.activation_content.get_value().at(0).get('value'));
        },

    })
	MethodEnablerView.ID = ID;

    return MethodEnablerView;
});
