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
    'Kurobox',
], function ($, _, Backbone, JST, Kurobox) {
    'use strict';

    var GenericUnpairModule = Backbone.View.extend({
        template: undefined,
        initialize: function(el, device, collection) {
            this.$el = el;
            this.device = device;
            this.collection = collection;
        },

        stop: function() {
            this.trigger('cancel');
        },

        render: function() {
            // there's no rendering happen
            this.collection.remove(this.device);
            this.trigger('unpair', this.device);
        },

        destroy: function() {
            this.undelegateEvents();
            if (this.$el !== undefined) {
        	   this.$el.empty();
            }
            // nothing to render
            this.device = undefined;
            this.collection = undefined;
        }
    });

    return GenericUnpairModule;
});
