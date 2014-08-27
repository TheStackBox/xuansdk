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
    'underscore',
    'backbone',
    'templates',
], function (_, Backbone, JST) {
	'use strict';

	return Backbone.View.extend({
		template: JST['app/scripts/templates/component.tab.ejs'],
		events: {
			'click .tab-item': 'on_user_select_component'
		},
		render: function() {
			if (this.options.data === undefined || this.options.data.length <= 0) throw 'Empty data';
			this.options.selected = this.options.selected || 0;
			this.$el.html(this.template({list: this.options.data, selected: this.options.selected}));
		},

		on_user_select_component: function(e) {
			var $e = $(e.currentTarget);
			var idx = $e.index();
			var value = $e.data('value');
			this.select(idx);
			this.trigger('selected', value, idx, $e);
		},

		select: function(index) {
			var $tabitems = this.$('.tab-item');
			$($tabitems[this.options.selected]).removeClass('icon-menu-on menu-on');
			$($tabitems[index]).addClass('icon-menu-on menu-on');

			this.options.selected = index;
		},

	}) 
});