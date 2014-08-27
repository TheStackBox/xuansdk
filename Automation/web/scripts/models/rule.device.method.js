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
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'models/rule.device.param'
], function (_, KuroboxModel, KuroboxCollection, DeviceParams) {
    'use strict';
    var DeviceMethod = {}
    DeviceMethod.model = KuroboxModel.extend({
    	defaults: {
    		id: undefined,
    		label: undefined,
    		hasEvent: false,
            description: '',
            status: 0,
    		params: new DeviceParams(), //DeviceParams,
            ui_components: new DeviceParams() //DeviceParams
    	},
    	parse: function(data) {
            console.log('method data', data)
            var o = {
                label: data.kbxMethodLabel || data.kbxMethodName,
                id: data.kbxMethodId,
                hasEvent: data.kbxMethodHasEvent,
                description: data.kbxMethodDesc,    
                params: new DeviceParams(data.kbxMethodParams, {parse: true}),
                ui_components: new DeviceParams(), // as reference only,
                status: data.statusCode
            }

            // parse ui components
            _.each(data.kbxMethodParams, function(param) {
                if (param.kbxParamCom !== undefined && param.kbxParamCom !== 'kbxHidden') {
                    o.ui_components.add( o.params.get(param.kbxParamName) );
                }
            })

    		return o;
    	},

        clone: function() {
            var o = new DeviceMethod.model({
                label: this.attributes.label,
                id: this.attributes.id,
                hasEvent: this.attributes.hasEvent,
                description: this.attributes.description,
                params: this.attributes.params.clone(),
                ui_components: new DeviceParams(),
            })

            o.get('params').each(function(param) {
                if (param.get('type') !== undefined && param.get('type') !== 'kbxHidden') {
                    console.log('ref param', param.id, param.get('type'))
                    o.get('ui_components').add( param );
                }
            })

            return o;
        },

        toObject: function() {
            var o = {
                kbxMethodId: this.attributes.id,
                kbxMethodParams: this.attributes.params.toObject()
            };

            return o;
        }
    })

    DeviceMethod.collection = KuroboxCollection.extend({
    	model: DeviceMethod.model,

        clone: function() {
            var o = new DeviceMethod.collection();

            this.each(function(model) {
                o.add(model.clone());
            })

            return o;
        }
    })
    return DeviceMethod;
});