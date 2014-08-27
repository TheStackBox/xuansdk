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
], function ($, _, Backbone, JST) {
    'use strict';

    // 'value_enabled' event trigger when component has proper value
    // 'value_disabled' event trigger when component has no proper value

    var AbstractControlComponent = Backbone.View.extend({
        error_template: JST['app/scripts/templates/component.control.abstract.error.ejs'],
        EVT_INVALID: 'invalid',
        EVT_VALID: 'valid',
        EVT_INIT: 'init',
        EVT_ERROR: 'error',
        get_value: function() {
            // always validate your value properly
            // before return out

            console.warn('You have to return something')
            return undefined;
        },

    	destroy: function() {
    		this.$el.remove();
            this.undelegateEvents();
    	},

        show_error: function(message, id) {
            this.$el.html(this.error_template({message: message}));
            this.trigger(this.EVT_ERROR, id);
        }
    })

    return AbstractControlComponent;
});