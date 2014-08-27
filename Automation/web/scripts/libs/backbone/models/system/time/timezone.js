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
    'libs/backbone/models/kurobox-model'
], function (_, Backbone, KuroboxModel) {
    'use strict';

    var SystemTimezoneModel = KuroboxModel.extend({
        idAttribute: 'timezone',
        defaults: {
            timezone: '',
            offset: ''
        },        
        fetch: function(options) {
        	this.url = 'get_time_zone';
        	this.dev_opt = {
        			//url: 'json/example.get_timezone.json',
        			bypassSession: true,
        			method: 'GET'
        		};
            
        	KuroboxModel.prototype.fetch.call(this, options);
        },
        save: function(key, val, options) {
        	this.url = 'set_time_zone';
        	this.dev_opt = {
        			//url: 'json/example.set_timezone.json',
        			bypassSession: true,
        			method: 'GET',
                    param_attr: { timezone: 'timezone', offset:'offset' }
        		};

            KuroboxModel.prototype.save.apply(this, arguments)
        },
        parse: function(data) {
        	return {
        		timezone: data.response.timezone,
        		offset: data.response.offset
        	}
        }
    });

    var SystemTimezoneCollection = Backbone.Collection.extend({
    	url: 'json/timezone.json',
    	model: SystemTimezoneModel,
    	fetch: function(options) {
    		// getting the timezone list
            $.getJSON(this.url, null, function(json, textStatus) {

            	// adding data
    			this.set(json.tz, options);

    			// callback
    			if (options.success) options.success(this, json.tz, options)
            }.bind(this)).fail(function() {
            	// callback
				if (options.error) options.error(this, null, options);
            }.bind(this));
    	}
    })

    var SystemTimezoneBundle = {
    	model: SystemTimezoneModel,
    	collection: SystemTimezoneCollection
    }

    return SystemTimezoneBundle;
});
