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

    var DateTimeRangeSetting = Backbone.View.extend({
    	template: JST['app/scripts/templates/module.rule.rule-setting.datetime-range.ejs'],
    	initialize: function() {
    		console.warn('TODO: validate timestamp');
    		console.log('-- delimiter', this.options.delimiter);

    		this.start_timestamp = '';
    		this.end_timestamp = '';
    		this.delimiter = this.options.delimiter || ' - ';

    		if (this.options.value !== undefined && this.options.value !== '') {
    			var pv = this.options.value.split(this.delimiter);
    			this.start_timestamp = pv[0];
    			this.end_timestamp = pv[1];
    		}

            console.log('-- output', this.start_timestamp + ' --> ' + this.end_timestamp)

    		this.render();
    	},

    	render: function() {
    		this.$el.html(this.template({start: this.start_timestamp, end: this.end_timestamp}));
    	},

    	get_value: function() {
            this.start_timestamp = this.$('#start-timestamp').prop('value');
            this.end_timestamp = this.$('#end-timestamp').prop('value');

    		return {
    			value: this.start_timestamp+this.delimiter+this.end_timestamp,
    			start: this.start_timestamp,
    			end: this.end_timestamp
    		}
    	},

    	close: function() {
    		// data disclose to listener
    		this.trigger('close', this.get_value());

    		this.options = undefined;

    		this.$el.remove();
    		this.undelegateEvents();
    	},

    	_render_component: function() {
    		var $p = this.$el.append();
    	},
    })
    return DateTimeRangeSetting;
});