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
    'common/components/models/kbx.datetime',
    'moment'
], function (Backbone, AbstractComplexControlComponent, ComponentListItem, ComponentParam, JST, kbxDateTime) {
    'use strict';

    var spr = AbstractComplexControlComponent.prototype;
    var YEAR_MARGIN = 10;
    var kbxDateTimeRange = AbstractComplexControlComponent.extend({

        destroy: function() {
            this.model.destroy();
            this.model = undefined;
        },

    	initialize: function() {
            spr.initialize.call(this);

            this.list_setting.add(new kbxDateTime({
                label: lang.translate('start'),
                type: 'kbxDateTime',
                name: 'startDateTime',
                description: lang.translate('start_datetime_description'),
                is_required: true,
                extra: {}
            }));
            this.list_setting.add(new kbxDateTime({
                label: lang.translate('end'),
                type: 'kbxDateTime',
                name: 'endDateTime',
                description: lang.translate('end_datetime_description'),
                is_required: true,
                extra: {}
            }));

            this.list_view.on('select', this.on_user_select_section, this);
        },

        render: function(model) {
            if (model.get('value') != undefined) {
                var itemValueModel;
                this.list_setting.each(function(item) {
                    itemValueModel = model.get('value')[item.id];
                    if (itemValueModel !== undefined) {
                        item.set('value', itemValueModel.get('value'))
                    }
                }.bind(this))
                
                // update range limit
                // update start date time
                var current = moment();
                var start = this.list_setting.get('startDateTime');
                var startMoment = start.generateMoment();
                if (startMoment.isBefore(current)) {
                    start.get('extra').kbxParamMinValue = startMoment.unix();
                } else {
                    start.get('extra').kbxParamMinValue = current.unix();
                }
  
                // update end date time
                this.list_setting.get('endDateTime').get('extra').kbxParamMinValue = startMoment.unix();
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
                    o[item.id] = item;
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
            // update opposite's limit
            this.update_min_max_range(model);

            spr.on_user_completed_component.call(this, model);

            this.validate();
        },

        update_min_max_range: function(model) {
            var c_timestamp = model.generateMoment();
            var update_setting;
            if (c_timestamp !== undefined) {
                switch (model.id) {
                    case 'startDateTime':
                    // create min limit at endDateTime
                    update_setting = this.list_setting.get('endDateTime');
                    update_setting.get('extra').kbxParamMinValue = c_timestamp.unix();

                    if (update_setting.get('value') != undefined) {
                        var setting_time = update_setting.generateMoment();
                        if (setting_time.diff(c_timestamp) < 0) {
                            // assume start time is earlier than end time
                            update_setting.set('value', c_timestamp.unix());
                        }
                    }
                    break;

                    case 'endDateTime':
                    update_setting = this.list_setting.get('startDateTime');
                    break;
                }

                if (update_setting.get('value') == undefined) {
                    // if either opposition value is empty
                    // auto fill with current time stamp
                    update_setting.set('value', c_timestamp.unix());
                }
            } else {
                // value being reset
                switch (model.id) {
                    case 'startDateTime':
                    // create max limit at endDateTime
                    update_setting = this.list_setting.get('endDateTime').get('extra');
                    update_setting.kbxParamMinValue = undefined;
                    update_setting.kbxParamMaxValue = undefined;
                    break;

                    case 'endDateTime':
                    // create min limit at startDateTime
                    update_setting = this.list_setting.get('startDateTime').get('extra');
                    update_setting.kbxParamMinValue = undefined;
                    update_setting.kbxParamMaxValue = undefined;
                    break;
                }
            }
        },

        render_component: function(model) {
            spr.render_component.call(this, model);

            console.log('render_component', model.attributes);

            this.param_holder.$('#reset-btn').hide();
            this.param_holder.$('#action-buttons').removeClass('btn-2-stretch').addClass('btn-1-stretch');
        },

        _hasListener: function(evt) {
            return !!this._events[evt];
        }
    })

    return kbxDateTimeRange;
});
