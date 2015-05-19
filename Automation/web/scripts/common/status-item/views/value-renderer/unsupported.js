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
    'common/status-item/views/item-renderer/item',
    'templates',
    'common/status-item/views/value-renderer/unsupported'
], function ($, _, StatusItemRenderer, JST, UnsupportedComponentValueRenderer) {
    'use strict';

    var spr = StatusItemRenderer.prototype;
    var UnsupportedComponentStatusItem = StatusItemRenderer.extend({
        template: JST['app/scripts/common/status-item/templates/item-renderer/item.ejs'],
        initialize: function() {
            this._value_renderer = UnsupportedComponentValueRenderer;
        },
        render: function() {
            spr.render.call(this);
            this.$('#require-mark').hide();
            this.$('#status-content').addClass('no-arrow');
            return this.$el;
        },

        set_value: function(val) {
            this.set_error(true);
            this.$('#status-item').removeClass('rule-status-enabled');
            this.value_renderer.set_value(val);
        },

        destroy: function() {
            this.$el.remove();
        }
    })

    return UnsupportedComponentStatusItem;
});