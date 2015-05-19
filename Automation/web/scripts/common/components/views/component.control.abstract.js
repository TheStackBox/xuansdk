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
    'backbone',
    'templates',
], function ($, _, Backbone, JST) {
    'use strict';

    // 'value_enabled' event trigger when component has proper value
    // 'value_disabled' event trigger when component has no proper value

    // 'select_elem' event is used for component navigation. output as string as nav id.
    // suggest to use 'navigational string'. eg(id:id2:id3:id4)
    // then component holder should pass nav id back to the component to 
    // proceed ui rendering via 'render' method

    var AbstractControlComponent = Backbone.View.extend({
        error_template: JST['app/scripts/common/components/templates/component.control.abstract.error.ejs'],
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

        set_value: function(value) {
            console.warn('Undefined set_value method');
        },

        navigate: function(nav_id) {
            // just the interface, perhaps
        },

        reset: function() {
            this.$el.empty();
            this.render(this.model);
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