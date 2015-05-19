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
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'models/location',
    'models/rule.device'
], function (_, KuroboxModel, KuroboxCollection, Location, Group) {
    'use strict';
    var _grep_filter;
    var spr = KuroboxCollection.prototype;
    var collection = KuroboxCollection.extend({
    	model: {},
    	parse: function(data) {
    		console.log('data', data)

    		var resp = data.response;
    		var o = [];
    		var data;
    		_.each(_grep_filter, function(key) {
    			console.log('-- grepping data by ', _grep_filter);
    			// sort by filters mentioned
    			if (resp[key] != undefined) {
    				_.each(resp[key], function(value) {
    					switch (key) {
    						case 'locations':
    						data = new Location({
    							id:'location-'+value.locationId,
    							label: value.locationLabel,
    							zoneId: value.zoneId,
    							zoneLabel: value.zoneLabel,
    						});
    						break;

    						case 'services':
    						case 'groups':
    						data = new Group.model({
    							id: key+'-'+value.kbxGroupId,
    							name: value.kbxGroupLabel,
				                icon: value.kbxGroupIcon,
				                description: value.kbxGroupDesc,
    						});
    						break;

    						default:
    						console.warn('Unknown group type', key)
    						data = new KuroboxModel(value);
    						break;
    					}

    					if (typeof value.hasChild != 'undefined') {
    						data.set('hasChild', value.hasChild)
    					} else {
    						data.set('hasChild', true);
    					}

    					o.push(data);
    				});
    			}
    		})

    		return o;
    	},
    	fetch: function(filter, locationId, parentGroupId, options) {
    		console.log('arg', arguments)
    		this.url = 'list_categories';
    		_grep_filter = filter;

    		if (locationId != undefined || parentGroupId != undefined) {
    			_grep_filter = ['groups']
    		}

    		this.dev_opt = {
    			param: {}
    		};

    		if (typeof filter == 'string') {
    			this.dev_opt.param.filter = filter;
    		} else {
    			if (filter.length > 0) {
    				this.dev_opt.param.filter = filter.join(',');
    			}
    		}

    		this.dev_opt.param.locationId = locationId;
    		this.dev_opt.param.parentGroupId = parentGroupId;

    		if (typeof PRODUCTION === 'undefined') {
    			if (this.dev_opt.param.locationId == undefined && this.dev_opt.param.parentGroupId == undefined) {
    				this.dev_opt.url = 'json/example.list_cat.filters.json';
    			} else if (this.dev_opt.param.parentGroupId != undefined) {
    				this.dev_opt.url = 'json/example.list_cat.devices.'+this.dev_opt.param.parentGroupId+'.json';
    			} else if (this.dev_opt.param.locationId != undefined) {
    				this.dev_opt.url = 'json/example.list_cat.locations.json';
    			}
    		}

    		spr.fetch.call(this, options);
    	},

    	list_group_by_location: function(locationId) {

    	},

    	list_group: function(parentId) {

    	}
    })

    return collection;
});