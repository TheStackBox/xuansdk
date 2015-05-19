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
    'farbtastic',
    'libs/utils/color'
], function ($, _, AbstractControlComponent, JST) {
    'use strict';

    // model: kbx.color

    var kbxTextInput = AbstractControlComponent.extend({
        template: JST['app/scripts/common/components/templates/component.control.color.ejs'],
    	render: function(model) {
            this.model = model;


            console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            // convert to hex format
            this.selected_color_hex = this.model.toDisplayValue() || this.model.getDefaultColor();
            this.$el.html(this.template({type: this.type, model: model}));

            _.defer(function() {
                // initialize picker
                this.farbtastic = $.farbtastic(this.$('#picker'), this.on_user_pick_color.bind(this));
                this.farbtastic.radius = 93;
                this.farbtastic.square = 0;
                this.farbtastic.width = 250;
                this.farbtastic.setColor(this.selected_color_hex);

                // disable inner square marker
                // added a div to display color output
                this.$('.color').before( '<div id="output"></div>' );
                this.$('.sl-marker').css('display', 'none');

                this.invalidate_color_output();

                this.trigger(this.EVT_INIT)
            }.bind(this))
        },

        on_user_pick_color: function(code) {
            this.selected_color_hex = code;
            this.invalidate_color_output();
        },

        invalidate_color_output: function() {
            this.$("#output").css("background-color", this.selected_color_hex);
        },

        get_value: function() {
            // validate value
            if (this.validate()) {
                return ColorUtil.hex2rgb(this.selected_color_hex);
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