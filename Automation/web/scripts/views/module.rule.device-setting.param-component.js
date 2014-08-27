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

define(function (require) {
    'use strict';

    var $ = require('jquery'),
        _ = require('underscore'),
        AbstractRuleDeviceSettingView = require('views/module.rule.device-setting.abstract-view'),
        UnsupportedComponent = require('views/component.control.unsupported'),
        JST = require('templates');

    // component import
    var component_store = {};
    // type backward
    component_store['kbxBoolean'] = require('views/component.control.toggle'),
    component_store['kbxString'] = require('views/component.control.input-text'),

    // new type
    component_store['kbxTextInput'] = component_store['kbxString'],
    component_store['kbxTextArea'] = require('views/component.control.text-area'),
    component_store['kbxSlider'] = require('views/component.control.slider'),
    component_store['kbxOption'] = require('views/component.control.option'),
    component_store['kbxToggle'] = component_store['kbxBoolean'],
    component_store['kbxTime'] = require('views/component.control.time'),
    component_store['kbxColor'] = require('views/component.control.color')

    /* composite class to hold component view */

    var spr = AbstractRuleDeviceSettingView.prototype;
    var ComponentHolderView = AbstractRuleDeviceSettingView.extend({
    	param_header: JST['app/scripts/templates/module.rule.device-setting.param-header.ejs'],
        method_header: JST['app/scripts/templates/module.rule.device-setting.method-header.ejs'],
    	error_template: JST['app/scripts/templates/module.rule.device-setting.method-header.ejs'],
    	render: function(method_id, param_id, device, param_model, method_model) {
    		this.method_id = method_id;
    		this.param_id = param_id;
    		this.device = device;
    		this.param_model = param_model;
            this.method_model = method_model;

    		// render template and header
    		spr.render.call(this);

    		// render component
    		this.render_component();

            // render action buttons
            this.render_action_buttons(this.$('#footer'), {
                'reset-btn': 'on_user_reset',
                'done-btn': 'on_user_done'
            });
    	},

    	render_header: function() {
    		if (this.method_model) {
    			// originally come from method list
    			return this.method_header({model: this.device, method: this.method_model});
    		} else {
    			// come from component list
    			return this.param_header({model: this.device, param: this.param_model});
    		}
    	},

    	render_component: function() {
    		var comp_clazz = this.determine_component(this.param_model.get('type'))
            var comp = eval('component_store[\''+comp_clazz+'\']');
            if (comp === undefined) {
                // assume there's no component registered
                console.warn('No component registered under', comp_clazz);
                comp = UnsupportedComponent;
            }

            try {
	    		this.component_view = new comp({el: this.$('#setting-content')});
                this.component_view.on(this.component_view.EVT_INVALID, this.on_component_value_invalid, this);
                this.component_view.on(this.component_view.EVT_VALID, this.on_component_value_valid, this);
                this.component_view.on(this.component_view.EVT_ERROR, this.on_component_error, this);
                this.component_view.on('init', this.on_component_init, this);
		    	this.component_view.render(this.param_model);
    		} catch (e) {
    			console.error('Error component view:', comp_clazz);
    			console.error(e.stack)
    		}
    	},

    	determine_component: function(type) {
    		// return type.substring(type.lastIndexOf('.'), type.length);
            return type;
    		// return 'kbxslider';
    	},

        invalidate_done_buttons: function() {
            var $done_btn = this.$('#footer #done-btn');
            var enabled = true;
            if (this.component_view === undefined) {
                // fail to init component
                enabled = false;
            } else {
                // let component get value to do the validation
                var comp_value = this.component_view.get_value()
                enabled = !(comp_value === undefined)
            }

            if (!enabled) {
                $done_btn.addClass('disabled');
            } else {
                $done_btn.removeClass('disabled');
            }
        },

        on_component_init: function() {
            // once component is rendered,
            
            _.defer(function() {
                // invalidate value in the component
                this.invalidate_done_buttons();
                this.$('#footer').show();
            }.bind(this))
        },

        on_component_error: function(error_id) {
            // remove action buttons
            this.$('#footer').hide();
        },

        on_user_reset: function(e) {
            // literally remove any availabe value
            this.param_model.reset_value();

            this.trigger('reset', this.method_id, this.param_id);
        },

        on_user_done: function(e) {
            // invalidate done buttons before start
            this.invalidate_done_buttons();

            var $me = $(e.currentTarget);
            var value = this.component_view.get_value();

            if (!$me.hasClass('disabled') && (value !== undefined || value !== '')) {
                // save value to method
                this.param_model.set('value', value);

                this.trigger('done', this.method_id, this.param_id);
            }
        },

        on_user_navigate_back: function(e) {
            this.trigger('cancel', this.method_id, this.param_id);
        },

        on_component_value_valid: function() {
            // value is valid
            // enable done button
            this.$('#footer #done-btn').removeClass('disabled');
        },

        on_component_value_invalid: function() {
            // value is invalid
            // disable done button
            this.$('#footer #done-btn').addClass('disabled');
        }

    })

    return ComponentHolderView;
});
