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
    'libs/backbone/view/shell/main.shell'
], function ($, _, Backbone, ShellView) {
    'use strict';

    var KuroboxRouter = Backbone.Router.extend({
    	initialize: function() {
    		// initialise shell
    		this.shell = new ShellView({el: $('body')});
    		this.shell.render();
    	},

        change_page: function(pageConstructor, extraParam) {
        	var param = this.prepare_page_param(extraParam)
        	var page = new pageConstructor(param);
        	
			// listen to page rendering
			page.once('page.rendered', this.on_page_rendered.bind(this));
			page.once('page.pass_param', this.on_page_pass_param.bind(this));			
			page.render();
			$('#content').html(page.el);

			return page;
		},

		prepare_page_param: function(extra_param) {
			var page_param = {}
			if (!_.isEmpty(this.param)) {
				_.extend(page_param, this.param);
			}

			// merge with extra param
			if (!_.isEmpty(extra_param)) _.extend(page_param, extra_param)
			this.param = null;
			return page_param;
		},
		
		on_page_pass_param: function(param) {
			this.param = param;
		},

		on_page_rendered: function(target) {
			// page rendered
			target.on('page.busy', function(target) {
				this.shell.show_preload(true);
			}.bind(this));
			target.on('page.idle', function(target) {
				this.shell.show_preload(false);
			}.bind(this));
			this.shell.show_preload(false);
		},

       	parse_query: function(queryStr) {
			var search = (typeof queryStr !== 'undefined') ? queryStr : location.search.substring(1);
			if (_.isEmpty(search)) {
            	return null;
			} else {
				return JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}');
			}
		}

    });

    return KuroboxRouter;
});
