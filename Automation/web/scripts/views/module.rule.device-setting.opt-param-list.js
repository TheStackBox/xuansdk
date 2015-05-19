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
    'views/module.rule.device-setting.req-param-list',
    'templates',
    'common/status-item/views/list',
    'views/module.rule.device-setting.method-enabler',
    'common/components/models/kbx.toggle',
    'common/components/views/component.control.toggle'
], function ($, _, RequiredParamListView, JST, RuleDeviceStatusListView, MethodEnablerView, kbxToggle, kbxToggleComponentView) {
    'use strict';

    var spr = RequiredParamListView.prototype;
    var OptionalParamListView = RequiredParamListView.extend({
        template: JST['app/scripts/templates/module.rule.device-setting.opt-param-list.ejs'],
        destroy: function() {
            spr.destroy.call(this);

            if (this.activation_toggle !== undefined) {
                this.activation_toggle.destroy();
                this.activation_toggle = undefined;
            }

            if (this.activation_content !== undefined) {
                this.activation_content.destroy();
                this.activation_content = undefined;
            }

        },

        render: function(method_id, device, user) {
            spr.render.call(this, method_id, device, user);

            // prepare activation content
            this.activation_content = new kbxToggleComponentView({el: this.$('#activation-content')});

            // render activation toggle
            this.render_method_activation_toggle();

        },

        render_method_activation_toggle: function() {
            this.activation_model = new kbxToggle({
                label: 'Enable this method',
                name: MethodEnablerView.ID,
                value: this._has_setting
            })

            this.activation_toggle = RuleDeviceStatusListView.prototype.render_item.call(this, this.activation_model);
            this.$('#setting-activation-toggle').html(this.activation_toggle.el);

            if (this._has_setting) {
                // has user setting
                this.activation_toggle.set_value(this.activation_model.toDisplayValue());
            } else {
                // has no user setting
                this.activation_toggle.set_value();
                // this.activation_toggle.$('#status-item').removeClass('rule-status-enabled');

                // hide setting content
                this.$('#setting-content').hide();
            }

            // click handler
            this.activation_toggle.$el.click(this.render_activation_content.bind(this))
        },

        render_activation_content: function() {
            // redirect to ui method
            window.location += '&mid='+this.method_id+'&pid='+MethodEnablerView.ID;
        },

        on_user_method_status: function(e) {
            this.is_method_activated = this.activation_content.get_value();
            this._update_activation_toggle(this.is_method_activated);
        },

        on_user_method_reset: function(e) {
            this._update_activation_toggle(false);
        },

        update_method: function(status) {
            // update setting changed
            this._has_setting_changed = (this._has_setting !== status);

            // change activation model's value
            var replaceResult = this.activation_model.get('list').get(status);
            this.activation_model.get('value').remove(this.activation_model.get('value').at(0));
            this.activation_model.get('value').add(replaceResult);

            // according to the value
            switch (status) {
                case true:
                // update activation toggle
                this.activation_toggle.$('#status-item').addClass('rule-status-enabled');
                this.activation_toggle.$('#value').text(this.activation_model.get('list').get(status).get('label'));

                this.$('#setting-content').show();

                // set user param
                if (this.user_param === undefined) {
                    this.user_param = this._defining_user_params();
                }
                break;

                default:
                // update activation toggle
                this.activation_toggle.$('#status-item').removeClass('rule-status-enabled');
                this.activation_toggle.$('#value').text('Tap To Set');

                this.$('#setting-content').hide();

                // remove user param
                if (this.user_param !== undefined) {
                    this.user_param = undefined;
                }
                break;
            }

            // this._show_param_list();

            // change back header, maybe?
        },

        _show_param_list: function() {
            // show back the activation toggle item
            this.$('#setting-activation-toggle').show();
            this.$('#footer').show();

            // hide activation content
            this.activation_content.$el.empty();

            // show setting if method available
            if (this.is_method_activated) {
                this.$('#setting-content').show();
            } else {
                this.$('#setting-content').hide();
            }
        },

        on_user_done: function() {
            if (this._has_setting_changed && this._has_setting && this.user_param === undefined) {
                // asked to reset method
                spr.on_user_reset.call(this);
            } else {
                spr.on_user_done.call(this);
            }

        }
    })

    return OptionalParamListView;
});
