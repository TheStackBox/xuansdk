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
    'common/status-item/views/list',
    'templates',
    'common/components/models/kbx.unsupported'
], function ($, _, RuleDeviceStatusListView, JST, UnsupportedComponent) {
    'use strict';

    var spr = RuleDeviceStatusListView.prototype;
    var OptionalParamListView = RuleDeviceStatusListView.extend({
        method_header: JST['app/scripts/templates/module.rule.device-setting.method-header.ejs'],
        prompt_dialog_msg: JST['app/scripts/common/templates/prompt.dialog.ejs'],
        prompt_pop_dialog_msg: JST['app/scripts/common/templates/prompt.pop.ejs'],
        render: function(method_id, device, user) {
            this.method_id = method_id;
            this.device = device;
            this.user = user;

            this._has_setting = (this.user.get('methods').get(this.method_id) !== undefined)
            // clone user params if any
            // else create a new one
            this.user_params = this._defining_user_params();

            // to determine if user has changed their own setting
            // if quit from param list view, need to prompt to discard changes
            this._has_setting_changed = false;

            // render template and header
            spr.render.call(this)

            // render item
            this.render_param(method_id, device);

            // render buttons
            this.render_action_buttons(this.$('#footer'), {
                'done-btn': 'on_user_done',
                'reset-btn': 'on_user_reset'
            });

            if (!this._has_setting) {
                // nothing to reset
                // swtch to 1 btn css 
                this.$('#footer #action-buttons').attr( "class", 'btn-1-stretch' );
                this.$('#footer #reset-btn').remove();
            }

            // render spacer in setting content
            this.$('#setting-content').append(this.render_spacer(this.$('#footer button')));
        },

        update: function(param_id) {
            this._has_setting_changed = true;

            // update status item's view
            this._invalidate_status_item(param_id);
        },

        render_header: function() {
            return this.method_header({model: this.device, method: this.device.get('methods').get(this.method_id)})
        },

        render_param: function(method_id, device) {
            var prop = {
                label: 'label',
                description: 'description',
                value: 'value',
                required: 'is_required'
            }

            device.get('methods').get(method_id).get('ui_components').each(function(param, index) {
                this.$('#setting-content').append(this.render_item(param, prop).$el);
            }.bind(this));
        },

        render_item: function(model, prop) {
            var status_item = spr.render_item.call(this, model, prop);

            if (model.className !== UnsupportedComponent.CLASS_NAME) {
                // invalidate status item's value renderer
                this._determine_value_renderer_by_comp(status_item, model);

                // invalidate status item view
                this._invalidate_status_item(model.id, status_item);

                // on click
                status_item.$el.click(function(e) {
                    // route to another url
                    window.location = window.location+'&pid='+model.id;
                });
            } else {
                this._handle_unsupported_component(status_item);
            }
 
            return status_item;
        },

        _handle_unsupported_component: function(status_item) {
            status_item.set_value();
        },

        _invalidate_status_item: function(id, status_item) {
            if (status_item === undefined) {
                // search on status list's store
                status_item = this.get_status_item(id);
            }

            if (this.user_params.get(id).get('value') !== undefined) {
                // has user setting
                status_item.set_value(this.user_params.get(id));
            } else {
                // has no user setting
                status_item.set_value();
            }
        },

        on_user_done: function(e) {
            var validated = this.validate_params();

            if (!validated) {
                // some params is not filled yet
                Shell.show_message(this.prompt_dialog_msg({
                    title: 'Opps... Something wrong',
                    message: 'You may miss some important fields',
                    icon: 'error'
                }), {
                    'click #ok-btn': this.on_user_acknowledge_prompt_message
                },
                this.on_user_acknowledge_validation_error
                )
            } else {
                // everythings ok
                this.trigger('done', this.user_params, this.method_id);
            }
        },

        validate_params: function() {
            var validated = true;
            this.user_params.each(function(param) {
                if (param.get('is_required')) {
                    if (!param.isValueValid()) {
                        validated = false;
                        console.log('param',param.id,'error')
                        
                        var status_itm = this.get_status_item(param.id);
                        if (status_itm) {
                            this.get_status_item(param.id).set_error(true);
                        }
                        // return false;
                    }
                }
            }.bind(this));

            return validated;
        },

        on_user_reset: function(e) {
            // user disable the method
            this._destroy_method_entry_in_user_profile();
            this.trigger('reset', this.method_id);
        },

        on_user_acknowledge_prompt_message: function(e) {
            // after error has being known
            Shell.hide_message();
            Shell.hide_pop_message();
        },

        on_user_navigate_back: function(e) {
            // detect if any changes
            if (this._has_setting_changed) {
                Shell.show_pop_message(
                    this.prompt_pop_dialog_msg({
                        title: 'There are some changes',
                        message: 'Are you sure you want to discard changes?',
                        ok_btn_label: 'Discard',
                        cancel_btn_label: 'Cancel'
                    }),
                    {
                        'click #modal-ok-btn': this.discard_changes.bind(this),
                        'click #modal-cancel-btn': this.on_user_acknowledge_prompt_message.bind(this)
                    },
                    this.on_user_acknowledge_prompt_message.bind(this)
                )
            } else {
                this.discard_changes();
            }
        },

        discard_changes: function() {
            this.on_user_acknowledge_prompt_message();
            spr.on_user_navigate_back.call(this);
        },

        _destroy_method_entry_in_user_profile: function() {
            if (this.user.get('methods').get(this.method_id) !== undefined) {
                var method = this.user.get('methods').get(this.method_id);
                if (method) {
                    this.user.get('methods').remove(method);
                }
            }
        },

        _defining_user_params: function() {
            if (this.user.get('methods').get(this.method_id)) {
                return this.user.get('methods').get(this.method_id).get('params').clone()
            } else {
                return this.device.get('methods').get(this.method_id).get('params').clone();
            }
        }
    })

    return OptionalParamListView;
});
