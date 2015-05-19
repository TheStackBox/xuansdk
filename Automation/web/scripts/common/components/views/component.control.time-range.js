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
	'backbone',
    'common/components/views/component.control.complex-abstract',
    'common/components/views/list/component.list',
    'common/components/views/list/component.list.param',
    'templates',
    'common/components/models/kbx.time'
], function (Backbone, AbstractComplexControlComponent, ComponentListItem, ComponentParam, JST, kbxTime) {
    'use strict';

    var spr = AbstractComplexControlComponent.prototype;
    var YEAR_MARGIN = 10;
    var kbxTimeRange = AbstractComplexControlComponent.extend({
    	initialize: function() {
            spr.initialize.call(this);

            this.list_setting.add(new kbxTime({
                label: lang.translate('start'),
                type: 'kbxTime',
                name: 'startTime',
                description: lang.translate('start_time_description'),
                is_required: true
            }));
            this.list_setting.add(new kbxTime({
                label: lang.translate('end'),
                type: 'kbxTime',
                name: 'endTime',
                description: lang.translate('end_time_description'),
                is_required: true
            }));

            this.list_view.on('select', this.on_user_select_section, this);
        },

        render: function(model) {
            if (model.get('value') !== undefined) {
                var itemValueModel;
                this.list_setting.each(function(item) {
                    itemValueModel = model.get('value')[item.id];
                    if (itemValueModel !== undefined) {
                        item.set('value', itemValueModel.get('value'))
                    }
                }.bind(this))
            }

            spr.render.call(this, model);
        },

        navigate: function(nav_id) {
            this.$el.empty();

            var _nav = [];
            if (nav_id !== undefined) _nav = nav_id.split(':');
            switch (_nav.length) {
                case 0:
                this.list_view.render(this.list_setting);

                // update item renderer
                // for create one-day bubbled end's time
                if (this.list_setting.get('startTime').get('value') !== undefined && 
                    this.list_setting.get('endTime').get('value') !== undefined) {

                    // update end's display value
                    var start = this.list_setting.get('startTime').generateMoment();
                    var end = this.list_setting.get('endTime').generateMoment();

                    if (end.diff(start) < 0) {
                        // rewrite item renderer's label
                        var pmodel = this.list_setting.get('endTime');
                        var label = pmodel.toDisplayValue()+' ('+lang.translate('next_day')+')'
                        this.list_view.get_status_item(pmodel).set_value(label);
                    }
                }  

                this.$el.html(this.list_view.$el);
                break;

                case 1:
                var section = this.list_setting.get(_nav[0]);
                this.render_component(section);
                break;
            }
        },

        get_value: function() {
            if (this.validate()) {
                var o = {}; 
                this.list_setting.each(function(item) {
                    console.log('item', item.id, item)
                    if (item.get('value') !== undefined) {
                        o[item.id] = item;
                    }
                })
                return o;
            }
            return;
        },

        validate: function() {
            var valid = true;
            if (this.list_setting !== undefined) {
                this.list_setting.every(function(item) {
                    if (item.get('is_required') === true && item.get('value') == undefined) {
                        valid = false;
                        this.trigger(this.EVT_INVALID);
                        return false; // loop breaker
                    }
                }.bind(this)) 
            } else {
                valid = false;
            }

            this.trigger(this.EVT_VALID);
            return valid;
        },

    	on_user_select_section: function(section) {
    		// show relevant component
            if (this._hasListener(this.EVT_SELECT)) {
                this.trigger(this.EVT_SELECT, section.id);
            } else {
                // TODO: yet to be tested
                this.navigate(section.id);
            }
    	},

        on_user_completed_component: function(model) {
            var update_setting;
            if (model !== undefined) {
                switch (model.id) {
                    case 'startTime':
                    update_setting = this.list_setting.get('endTime');
                    break;

                    case 'endTime':
                    update_setting = this.list_setting.get('startTime');
                    break;
                }

                if (update_setting.get('value') == undefined) {
                    // if either opposition value is empty
                    // auto fill with current time stamp
                    update_setting.set('value', model.get('value'));
                }

            }

            spr.on_user_completed_component.call(this, model);

            this.validate();
        },

        render_component: function(model) {
            spr.render_component.call(this, model);

            this.param_holder.$('#reset-btn').hide();
            this.param_holder.$('#action-buttons').removeClass('btn-2-stretch').addClass('btn-1-stretch');
        },

        _hasListener: function(evt) {
            return !!this._events[evt];
        }
    })

    return kbxTimeRange;
});