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
    'models/scene.filter',
], function ($, Backbone, JST, SceneFilterOption) {
	
	var FilterOptionView = Backbone.View.extend({
		template: JST['app/scripts/templates/scene.filter-option.ejs'],
		item_template: JST['app/scripts/templates/scene.filter-option.item.ejs'],
		events: {
			'click .item': 'select_item',
			'click .dark-layer-90': 'close_option',
		},
		destroy: function() {
			this.$el.empty();
		},

		render: function() {
			this.$el.html(this.template());
			// console.log('---> templated')

			this.data = new SceneFilterOption()
			this.data.fetch({
				success: function() {
					// insert all
					this.data.add({label: 'All', value: 'all'}, {at: 0})
					console.log('this.data', this.data)
					var config;
					this.data.each(function(location) {
						config = {label: location.get('label'), id: location.get('value')};
						if (location.get('extra') != undefined) {
							config.zone = location.get('extra').zoneName
						}
						this.$('#filter-list').append(this.item_template(config))
					}.bind(this))

				}.bind(this),
				error: function() {
					
				}
			})

			return this;
		},

		trigger_view: function() {
			if (this.$el.is(':hidden')) {
				this.$el.show();
				$('body').css('overflow-y', 'hidden');
				this.trigger('open');
			} else {
				this.$el.hide();
				$('body').css('overflow-y', '');
				this.trigger('close');
			}
		},

		select_item: function(e) {
			// this.trigger('select', e.currentTarget)
			var $e = $(e.currentTarget);
			var id = $e.data('id')

			this.trigger('select', this.data.get(id), id)
		},

		close_option: function(e) {
			this.trigger_view();
		}
	});

	return FilterOptionView;
});