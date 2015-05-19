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
    'jquery',
    'underscore',
    'common/components/views/component.control.abstract',
    'templates',
    'common/components/models/kbx.input-text',
    'mobiscroll',
    'moment'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var kbxDateTime = AbstractControlComponent.extend({
        template: JST['app/scripts/common/components/templates/component.control.datetime.ejs'],
        pop_date_tmpl: JST['app/scripts/common/components/templates/component.control.datetime.pop.date.ejs'],
        events: {
            'click #date-value': 'on_user_change_date',
            'click #time-value': 'on_user_change_time'
        },
    	render: function(model) {
            this.model = model;

            console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            if (this.model.get('extra') !== undefined && this.model.get('extra').kbxParamMinValue !== undefined) {
                this.min_limit = moment.unix(this.model.get('extra').kbxParamMinValue);
            } else {
                this.min_limit = moment();
            }

            if (this.model.get('extra') !== undefined && this.model.get('extra').kbxParamMaxValue !== undefined) {
                this.max_limit = moment.unix(this.model.get('extra').kbxParamMaxValue);
            } else {
                this.max_limit = moment(new Date(this.min_limit.toDate())).add(10, 'y');
            }
            
            this._value = this.model.generateMoment() || this.min_limit.clone() || moment();
            this._value.second(0); // reset second

            this.$el.html(this.template({value: this._value}));

            this.trigger(this.EVT_INIT);
        },

        destroy: function() {
            spr.destroy.call();

            this.$('#time-container').mobiscroll('destroy');
        },

        get_value: function() {
            // validate value
            if (this.validate()) {
                return this._value.unix();
            } else {
                // validation failed
                return;
            }
        },

        validate: function(e) {
            this.trigger(this.EVT_VALID)
            return true;
        },

        on_user_change_date: function() {
            // prompt popup
            this.prompt_pop({
                title: 'date',
                mobiscroll: {
                    type: 'date',
                    options: {
                        minDate: this.min_limit.toDate(),
                        maxDate: this.max_limit.toDate(),
                        dateOrder: 'ddMyyyy'
                    }
                },
                value: this._value.toDate()
            }, this.on_user_entered_date.bind(this), this.on_user_cancel.bind(this));
        },

        on_user_change_time: function() {

            // determine if date is out of min limit
            var min;
            var max;
            var isAtMin = moment(this.min_limit.format('YYYY-M-D')).isSame(moment(this._value.format('YYYY-M-D')));
            var isAtMax = moment(this.max_limit.format('YYYY-M-D')).isSame(moment(this._value.format('YYYY-M-D')));
            if (isAtMin) {
                min = this.min_limit.toDate();
                max = moment('23:59', 'hh:mm').toDate();
            } else if (isAtMax) {
                min = moment('00:00', 'hh:mm').toDate();
                max = this.max_limit.toDate();
            }

            // prompt popup
            this.prompt_pop({
                title: 'time',
                mobiscroll: {
                    type: 'time',
                    options: {
                        minDate: min,
                        maxDate: max,
                    }
                },
                value: this._value.toDate()
            }, this.on_user_entered_time.bind(this), this.on_user_cancel.bind(this));
        },

        on_user_entered_date: function() {
            // get value from prompt
            var theValue = this.$pf('#datetime-container').mobiscroll('getDate');

            // update value
            this._value.set('year', theValue.getFullYear());
            this._value.set('month', theValue.getMonth());
            this._value.set('date', theValue.getDate());

            // auto correct time
            if (this._value.isBefore(this.min_limit)) {
                // over the min
                // correct time with min
                this._value.set('h', this.min_limit.hours());
                this._value.set('m', this.min_limit.minutes());
            } else if (this._value.isAfter(this.max_limit)) {
                // beyond the max
                this._value.set('h', this.max_limit.hours());
                this._value.set('m', this.max_limit.minutes());
            }

            this.render_value();

            // close
            this.on_user_cancel();
        },

        on_user_entered_time: function() {
            // get value from prompt
            var theValue = this.$pf('#datetime-container').mobiscroll('getDate');

            // update value
            this._value.set('hour', theValue.getHours());
            this._value.set('minute', theValue.getMinutes());

            // display the value
            this.render_value();

            // close
            this.on_user_cancel();
        },

        on_user_cancel: function() {
            delete this.$prompt_content;

            Shell.hide_pop_message();
        },

        render_value: function() {
            // display the value
            this.$('#date-value').text(this._value.format('DD MMM YYYY'));
            this.$('#time-value').text(this._value.format('hh:mm A'));

        },

        prompt_pop: function(options, ok_cb, cancel_cb) {
            this.$prompt_content = Shell.show_pop_message(
                this.pop_date_tmpl({title: options.title}),
                {
                    'click #ok-btn': ok_cb,
                    'click #cancel-btn': cancel_cb
                },
                cancel_cb
            )
            this.$prompt_content.hide();

            // init mobiscroll
            _.defer(function() {
                // $pf('#datetime-container').mobiscroll().date
                var opts = {
                    mode: 'scroller',
                    display: 'inline',
                }
                _.extend(opts, options.mobiscroll.options || {})
                this.$pf('#datetime-container').mobiscroll()[options.mobiscroll.type](opts)

                if (options.value !== undefined) 
                    this.$pf('#datetime-container').mobiscroll('setDate', options.value);

                // show time!
                this.$prompt_content.slideToggle();
            }.bind(this))
        },

        $pf: function(selector) {
            if (this.$prompt_content != undefined) {
                return this.$prompt_content.find(selector);
            }
            return;
        }
    })

    return kbxDateTime;
});
