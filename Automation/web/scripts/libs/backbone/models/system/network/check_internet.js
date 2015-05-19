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
    'libs/backbone/models/kurobox-model'
], function (_, KuroboxModel) {
    'use strict';

    var CheckInternetModel = KuroboxModel.extend({
        fetch: function(options) {
        	this.url = 'check_internet_connectivity';
        	this.dev_opt = {
        		//url: 'json/example.check_internet.json',
        		method: 'GET',
        		bypassSession: true
        	}
        	KuroboxModel.prototype.fetch.call(this, options);
        },

        save: function(key, val, options) {
        	console.warn('This modal has no set method');
        	return;
        },

        parse: function(data) {
            console.log('parse1', data.response.status)
            
            return {
                status: (data.response.status === 'ok')
            }
        }
    });

    return CheckInternetModel;
});
