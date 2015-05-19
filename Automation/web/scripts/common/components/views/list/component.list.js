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
    'common/status-item/views/list',
    'templates',
    'backbone'
], function (AbstractStatusListView, JST, Backbone) {
    'use strict';

    var spr = AbstractStatusListView.prototype;
    var ComponentItemListView = AbstractStatusListView.extend({
    	render: function(settings) {
            // renew everything
            this.$el.empty();
            this.store = new Backbone.Collection();

    		settings.each(function(item) {
    			this.$el.append(this.render_item(item).$el);
    		}.bind(this))
    	},

    	render_item: function(item) {
    		var itm_view = spr.render_item.call(this, item);

    		// set value to item renderer
    		itm_view.set_value(item.toDisplayValue());

    		// register click event
    		itm_view.$el.click(function() {
    			this.trigger('select', item);
    		}.bind(this))
    		return itm_view;
    	},

        update: function(item) {
            var itm_view = this.get_status_item(item);
            itm_view.set_value(item.get('value'));
        }
    });

    return ComponentItemListView;

});