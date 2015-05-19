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

define(function(require) {
    'use strict';

    var $ = require('jquery'),
        _ = require('underscore'),
        AbstractRuleDeviceSettingView = require('common/status-item/views/abstract'),
        JST = require('templates'),
        Backbone = require('backbone'),
        UnsupportedComponent = require('common/components/models/kbx.unsupported'),
        item_renderer = {},
        value_renderer = {}

    // item renderer by class
    item_renderer['abstract'] = require('common/status-item/views/item-renderer/item');
    item_renderer[UnsupportedComponent.CLASS_NAME] = require('common/status-item/views/item-renderer/unsupported');

    // value renderer
    value_renderer['default'] = require('common/status-item/views/value-renderer/default');
    value_renderer['kbxColor'] = require('common/status-item/views/value-renderer/color');
    value_renderer['kbxHSBColor'] = require('common/status-item/views/value-renderer/color');
    value_renderer['kbxOption.kbxOptionWithIcon'] = require('common/status-item/views/value-renderer/icon-option');

    var spr = AbstractRuleDeviceSettingView.prototype;

    var RuleDeviceStatusListView = AbstractRuleDeviceSettingView.extend({
        STATUS_ID: '__ui_status_',
        store: new Backbone.Collection(),
        initialize: function() {
            spr.initialize();
            this.store = new Backbone.Collection();

        },
    	render_item: function(model, prop) {
            prop = _.extend(prop || {}, {
                type: 'type',
                label: 'label',
                description: 'description',
                value: 'value',
                required: 'is_required'
            });

            var itemRenderer = eval('item_renderer[\''+model.className+'\']'),
                status_item;
            if (itemRenderer === undefined) {
                itemRenderer = item_renderer['abstract'];
            }

    		var status_item = new itemRenderer({
                id: this.STATUS_ID+model.id,
				title: model.get(prop.label),
				description: model.get(prop.description),
				value: model.get(prop.value) || 'Tap To Set',
				required: model.get(prop.required),
			});
			status_item.render();

            // push to 
            this.store.add({id: model.id, item: status_item})
			return status_item;
    	},

        get_status_item: function(model) {
            var id;
            if (typeof model === 'string') {
                id = model;
            } else {
                id = model.id;
            }

            if (this.store.get(id)) {
                return this.store.get(id).get('item');
            }
            return;
        },

        destroy: function() {
            this.store.each(function(status_item) {
                status_item.get('item').destroy();
            })
            this.store = undefined;
            spr.destroy.call(this);
        },

        _determine_value_renderer_by_comp: function(status_item, param_model) {
            // this is for private use
            // to determine value renderer

            var renderer;
            var type = param_model.get('type');
            console.log('>> type', type)
            if (type !== undefined) {
                renderer = eval('value_renderer[\''+type+'\']');
                if (renderer === undefined)
                    renderer = value_renderer['default'];
            }
            
            status_item.set_value_renderer(renderer);

            return status_item;
        }

    	
    })

    return RuleDeviceStatusListView;
});