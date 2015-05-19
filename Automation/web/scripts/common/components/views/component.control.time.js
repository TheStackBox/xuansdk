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

    var spr = AbstractControlComponent.prototype;
    var kbxTextInput = AbstractControlComponent.extend({
        template: JST['app/scripts/common/components/templates/component.control.time.ejs'],
        events: {
            'blur #textinput':'validate',
            'keyup #textinput':'validate',
            'unblur #textinput': 'validate'
        },
        time_setting: {
            mode: 'scroller',
            display: 'inline',
        },
    	render: function(model) {
            this.model = model;

            console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            this.$el.html(this.template({type: this.type, model: model}));

            _.defer(function() {
                console.log('init mobiscroll time!!!', this.$('#time-container'));
                this.$('#time-container').mobiscroll().time(this.time_setting);

                if (this.model.generateMoment() !== undefined) {
                    console.log('--- gen moment', this.model.generateMoment().toDate())
                    // display current value
                    this.$('#time-container').mobiscroll('setDate', this.model.generateMoment().toDate())
                }

                this.trigger(this.EVT_INIT);
            }.bind(this))
        },

        destroy: function() {
            spr.destroy.call(this);

            this.$('#time-container').mobiscroll('destroy');
        },

        get_value: function() {
            // validate value
            if (this.validate()) {
                var value = this.$('#time-container').mobiscroll('getDate');

                // convert to milisecond
                var m = moment(value);
                value = (m.hour() * 3600) + (m.minute() * 60);
                return value;
            } else {
                // validation failed
                return;
            }
        },

        validate: function(e) {
            this.trigger(this.EVT_VALID)
            return true;
        }
    })

    return kbxTextInput;
});
