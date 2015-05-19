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
    'libs/backbone/models/kurobox-collection'
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    var RuleDeviceType = {};

    RuleDeviceType.model = KuroboxModel.extend({
    });

    RuleDeviceType.collection = KuroboxCollection.extend({
    	model: RuleDeviceType.model,
    	fetch: function(scope, options) {
            this.section = scope;
            console.log('this.scope', this.section)
    		this.url = 'list_groups';
    		this.dev_opt = {
    			method: 'GET',
                param: {
                    section: this.section
                }
    		}
    		KuroboxCollection.prototype.fetch.call(this, options)
    	},

        parse: function(data) {
            // filter scope
            var o = [];
            _.each(data.response.data, function(typeData, index){
                o.push({
                    id: typeData.kbxGroupId,
                    label: typeData.kbxGroupLabel || undefined,
                    icon: typeData.kbxGroupIcon || undefined,
                    description: typeData.kbxGroupDesc || typeData.zoneName || '',
                })
            }.bind(this))
            return o;
        }
    })

    return RuleDeviceType;
});
