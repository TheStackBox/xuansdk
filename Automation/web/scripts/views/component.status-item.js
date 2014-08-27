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
    'views/component.status-item.value.default'
], function ($, _, Backbone, JST, DefaultStatusItemValueRenderer) {
    'use strict';

    var StatusItemRenderer = Backbone.View.extend({
        template: JST['app/scripts/templates/component.status-item.ejs'],
        initialize: function(options) {
            var value_renderer;
            if (options !== undefined) {
                value_renderer = options.value_renderer || DefaultStatusItemValueRenderer;
            } else {
                value_renderer = DefaultStatusItemValueRenderer;
            }
            this._value_renderer = value_renderer;
        },
        render: function() {
            this.$el.html(this.template({
                title: this.options.title,
                description: this.options.description || '',
                value: this.options.value
            }))

            if (!this.options.required) {
                this.$('#require-mark').hide();
            } else {
                this.$('#require-mark').show();
            }

            this.set_value_renderer(this._value_renderer);
            this._value_renderer = undefined;

            return this.$el;
        },

        set_value_renderer: function(renderer) {
            this.$('#value').empty();

            this.value_renderer = new renderer();
            this.value_renderer.$el = this.$('#value');
            this.value_renderer.render();
        },

        set_value: function(val) {
            this.set_error(false);
            if (val === undefined) {
                this.$('#status-item').removeClass('rule-status-enabled');
            } else {
                this.$('#status-item').addClass('rule-status-enabled');
            }
            this.value_renderer.set_value(val);
        },

        set_error: function(isError) {
            if (isError) {
                this.$('#status-item').addClass('rule-status-error');
            } else {
                this.$('#status-item').removeClass('rule-status-error');
            }
        },

        destroy: function() {
            this.$el.remove();
        }
    })

    return StatusItemRenderer;
});