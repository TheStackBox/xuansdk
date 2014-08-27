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
    'moment'
], function (_) {
	'use strict';

	var utils = function() {
		this.initialize.apply(this, arguments);
	}

	_.extend(utils.prototype, {
		initialize: function() {},

		dateToUnix: function(date) {
			return moment(date).unix();
		},

		unixToDate: function(unix) {
			return new Date(unix*1000);
		},

		unixToDateString: function(unix, format) {
			return moment(this.unixToDate(unix)).format(format || 'YYYY-MM-DD');
		},

		render_spacer: function($target) {
            return '<div class="clear" style="height:'+$target.outerHeight(true)+'px"></div>'
        },
	})

	return utils;
})