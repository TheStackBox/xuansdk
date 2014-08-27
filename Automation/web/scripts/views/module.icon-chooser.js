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
    'templates'
], function ($, _, Backbone, JST) {
    'use strict';

    var ModuleIconChooserView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.icon-chooser.ejs'],
        events: {
        	'click .icon-picker-item': 'on_user_selected_icon'
        },
        render: function() {
            console.log('render')
        	if (this.options.data_url === undefined) {
        		console.error("Undefined icon data");
        		return;
        	}

        	// reading icon data
        	$.ajax({
        		url: this.options.data_url,
        		dataType: 'json',
        		success: function(data, status, xhr) {
                     console.log('success render')
        			// render it out
        			data._ = _;
        			$(this.el).html(this.template(data));
        		}.bind(this),
        		error: function(xhr, status, httpErr) {
        			// throw error
        			var err = 'Unable to read icon data file'
        			console.error(err, xhr)
        			this.trigger('error', 'Unable to read icon data file', xhr);
        		}.bind(this)

        	})
        },
        on_user_selected_icon: function(evt) {
        	var id = $(evt.currentTarget).data('id');
        	this.trigger('select', id);
        }
    });

    return ModuleIconChooserView;
});
