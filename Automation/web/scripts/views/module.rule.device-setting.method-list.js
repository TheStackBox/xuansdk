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
    'views/module.rule.device-setting.status-item-list',
    'templates',
    'views/component.status-item',
    'views/module.rule.device-setting.method-enabler'
], function ($, _, RuleDeviceStatusListView, JST, StatusItemRenderer, MethodEnablerView) {
    'use strict';

    var spr = RuleDeviceStatusListView.prototype;
    var MethodListView = RuleDeviceStatusListView.extend({
    	
    	device_header: JST['app/scripts/templates/module.rule.device-setting.device-header.ejs'],

        update: function(method_id) {
            if (this.user_methods === undefined) {
                // reference back to user setting
                this.user_methods = this.user.get('methods');
            }

            this._invalidate_status_item(method_id);
        },

    	render: function(device, user) {
            this.user = user;
            this.user_methods = this.user.get('methods');
            this.device = device;

            // render template and header
            spr.render.call(this);

            // render item
            var prop = {
                label: 'label',
                description: 'description',
                value: 'value',
                required: 'is_required'
            }

            device.get('methods').each(function(method, index) {
                this.$('#setting-content').append(this.render_item(method, prop).$el);
            }.bind(this));

    	},

        render_header: function() {
            return this.device_header({model: this.device})
        },

    	render_item: function(model, prop) {
    		var status_item = spr.render_item.call(this, model, prop);

            // set value renderer
            if (model.get('ui_components').length === 1) {
                this._determine_value_renderer_by_comp(status_item, model.get('ui_components').at(0));
            }

            this._invalidate_status_item(model.id, status_item);

    		// on click
    		status_item.$el.click(function(e) {
				// route to another url
                if (model.get('ui_components').length === 0) {
                    // redirect to method enabler
                    window.location += '&mid='+model.id+'&pid='+MethodEnablerView.ID;
                } else if (model.get('ui_components').length === 1) {
                    // direct route to component view
                    window.location += '&mid='+model.id+'&pid='+model.get('ui_components').models[0].id;
                } else {   
                    // route to param list
				    window.location = window.location+'&mid='+model.get('id');
                }
			});
			return status_item;
    	},

        _invalidate_status_item: function(id, status_item) {
            if (status_item === undefined) {
                // search on status list's store
                status_item = this.get_status_item(id);
            }

            if (this.user_methods !== undefined && this.user_methods.get(id) !== undefined) {
                // show active method
                if (this.user_methods.get(id).get('ui_components').length > 1) {
                    // show edit
                    status_item.set_value('Tap To Edit');
                } else if (this.user_methods.get(id).get('ui_components').length === 0) {
                    // just enabled
                    status_item.set_value('Tap To Edit');
                } else {
                    // set value
                    var param = this.user_methods.get(id).get('ui_components').models[0];
                    status_item.set_value(param.toDisplayValue());
                }
            } else {
                // has no user setting
                status_item.set_value();
            }
        },

        on_user_navigate_back: function(e) {
            this.trigger('cancel')
        }
    })

    return MethodListView;
});
