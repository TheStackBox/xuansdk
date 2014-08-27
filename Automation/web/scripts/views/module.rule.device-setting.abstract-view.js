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
    'views/component.status-item'
], function ($, _, Backbone, JST, StatusItemRenderer) {
    'use strict';

    var AbstractRuleDeviceSettingView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.rule.device-setting.ejs'],
        header_template: JST['app/scripts/templates/module.rule.grey-header.ejs'],
        rule_action_button: JST['app/scripts/templates/module.rule.device-setting.action-buttons.ejs'],
        events: {
            'click #nav-back-btn': 'on_user_navigate_back'
        },
        render: function() {
            this.$el.html(this.template());

            // render header first
            var $header = this.header_template({
                content: this.render_header()
            });
            this.$('#header').append($header);

            // show time
            this.$el.show();
            this.delegateEvents();
        },

        render_spacer: function($target) {
            return '<div class="clear" style="height:'+$target.outerHeight(true)+'px"></div>'
        },

        render_header: function() {
            // return this.method_header({model: device, method: device.get('methods').get(method_id)})
            return '';
        },

        /*
        event_handler = {
            'id-btn': 'function in string'
        }
        */
        render_action_buttons: function(el, event_handlers) {
            el.append(this.rule_action_button());

            // register events
            _.each(event_handlers, function(callback, id) {
                this.events['click #'+el.attr('id')+' > #action-buttons > #'+id] = callback;
            }.bind(this));

            // re-delegate events
            this.undelegateEvents();
            this.delegateEvents();
        },

        on_user_navigate_back: function() {
            // navigate back to its parent
            window.history.back();
        },

        close: function() {
            this.undelegateEvents();
            this.$el.hide();
        },

        show: function() {
            this.delegateEvents();
            this.$el.show();
        },

        destroy: function() {
            this.undelegateEvents();
            this.$el.remove();
        }
        
    })

    return AbstractRuleDeviceSettingView;
});