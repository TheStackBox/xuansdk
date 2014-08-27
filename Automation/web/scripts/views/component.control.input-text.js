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
    'models/kbx.input-text'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var kbxTextInput = AbstractControlComponent.extend({
        template: JST['app/scripts/templates/component.control.input-text.ejs'],
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

            this.type = (this.model.get('extra').kbxParamTypeInput) ? this.model.get('extra').kbxParamTypeInput : 'text';

            this.$el.html(this.template({type: this.type, model: model}));

            this.trigger(this.EVT_INIT);
        },

        get_value: function() {
            // validate value
            if (this.validate()) {
                if (this.type === 'number') {
                    // parse as number
                    return Number(this.$('#textinput').prop('value'));
                } else {
                    // render as string
                    return this.$('#textinput').prop('value');
                }
            } else {
                // validation failed
                return;
            }
        },

        validate: function(e) {
            var $target = this.$('#textinput')
            var result = $target.prop('value');

            // temporarily add border
            if (e) {
                $target.removeClass( 'notfocussed' );
                $target.addClass( 'error-border' );
                $target.addClass( 'error-msg' );
            }

            if (result === '') {
                this.trigger(this.EVT_INVALID);

                if (e) {
                    // show no value entered
                    $target.removeClass('error-data')
                }

                return false;
            } else 
            if (result.length < parseInt(this.model.get('extra').kbxParamMinLength)) {
                this.trigger(this.EVT_INVALID);

                if (e) {
                    // show not enof characters
                    $target.addClass('error-data')
                }

                return false;
            }

            // no error happen
            // perfect!
            if (e) {
                $target.addClass( 'notfocussed' );
                $target.removeClass( 'error-border' );
                $target.removeClass( 'error-msg' );
                $target.removeClass('error-data');
            }
            this.trigger(this.EVT_VALID)
            return true;
        }
    })

    return kbxTextInput;
});