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
define([
	'underscore',
    'common/models/label_value',
    'libs/backbone/models/kurobox-collection'
], function (_, LabelValue, KuroboxCollection) {
	
	var spr;
	var model = LabelValue.model.extend({

	})
	spr = KuroboxCollection.prototype;
	var collection = KuroboxCollection.extend({
		model: model,
		fetch: function(options) {
    		this.url = 'get_categories';
    		this.dev_opt = {
    			url: 'json/example.scene.locations.json',
    			param: {
    				filter: 'location'
    			}
    		}
    		spr.fetch.call(this, options)
    	},
    	parse: function(data) {
    		var d = [];
    		var loc
    		_.each(data.response.location, function(locItem) {
    			loc = {};
    			loc.label = locItem.locationLabel;
    			loc.value = locItem.locationId;

    			delete locItem.locationLabel;
    			delete locItem.locationId;

    			loc.extra = locItem;

    			d.push(loc);
    		});
    		return d;
    	}
	})
	return collection;
})