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
    'backbone',
    'templates',
], function ($, Backbone, JST) {
	'use strict';

	var SceneItemListView = Backbone.View.extend({
		item_template: JST['app/scripts/templates/scene.item.list.ejs'],
		empty_list_template: JST['app/scripts/templates/scene.item.list.empty.ejs'],
		events: {
			'click .scene-list-item': 'on_user_selected_item',
			'click [data-event]': 'dispatch_custom_event'
		},
		initialize: function() {
		},

		destroy: function() {
			this.reset();
			this.undelegateEvents();
		},

		reset: function() {
			this.$el.empty();
		},

		render: function(item_template, empty_template) {
			if (item_template !== undefined) {
				this.item_template = item_template;
			}

			if (empty_template != undefined) {
				this.empty_list_template = empty_template;
			}
		},

		invalidate: function(options) {
			options = (options) ? options : {};
			if (this.data.length > 0) {
				this.data.each(function(item, index) {
					options.index = index;
					this.$el.append(this.item_template({item: item, options: options}));
				}.bind(this))
			} else {
				// nothing to display
				this.$el.html(this.empty_list_template({options: options}));				
			}
		},

		list: function(data, options) {
			this.data = data;

			this.$el.empty();

			var params = options.list_params || [];
			params = params.concat([{
				success: function() {
					this.invalidate();

					// data is ready to use
					this.trigger('data_ready');
				}.bind(this),
				error: function(model, error) {
					// show error message
					this.trigger('data_error', error)
				}.bind(this)
			}])

			console.log('params..', params)

			this.data.fetch.apply(this.data, params);
		},

		on_user_selected_item: function(e) {
			var $ct = $(e.currentTarget);
			this.trigger('select', $ct.data('id'), this.data.get($ct.data('id')));
		},

		dispatch_custom_event: function(e) {
			var $ct = $(e.currentTarget);
			this.trigger($ct.data('event'), e);
		},

		render_spacer: function($target) {
 			return '<div class="clear" style="height:'+$target.outerHeight(true)+'px"></div>'
   		},
	})

	return SceneItemListView;
});