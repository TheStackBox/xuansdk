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
    'jquery',
    'underscore',
    'views/component.control.abstract',
    'templates',
    'models/kbx.input-text',
    'mobiscroll',
    'moment'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var kbxTextInput = AbstractControlComponent.extend({
        template: JST['app/scripts/templates/component.control.time.ejs'],
        events: {
            'blur #textinput':'validate',
            'keyup #textinput':'validate',
            'unblur #textinput': 'validate'
        },
    	render: function(model) {
            this.model = model;

            console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            this.$el.html(this.template({type: this.type, model: model}));

            _.defer(function() {
                console.log('init mobiscroll time!!!', this.$('#time-container'));
                this.$('#time-container').mobiscroll().time({
                    mode: 'scroller',
                    display: 'inline',
                })

                this.trigger(this.EVT_INIT);
            }.bind(this))
        },

        destroy: function() {
            spr.destroy.call();

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