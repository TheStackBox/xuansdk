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
    'common/components/views/component.control.color',
    'templates',
    'common/components/views/component.control.slider',
    'farbtastic',
    'libs/utils/color',
    'libs/utils/browser'
], function ($, _, ColorComponent, JST, Slider) {
    'use strict';

    // model: kbx.color.hsb

    var kbxHSBColor = ColorComponent.extend({
        fn: ColorComponent.prototype,
        template: JST['app/scripts/common/components/templates/component.control.color.hsb.ejs'],
        events: {},
        initialize: function() {
            console.log('---> test events', this.events);
            if (BrowserUtil.isMobile()) {
                this.events['touchend #picker'] = 'on_user_confirm_color';
            } else {
                this.events['mouseup #picker'] = 'on_user_confirm_color';
            }
        },

        render: function(model) {
            console.log('---> model', model)
            this.model = model;
            this.$el.html(this.template({type: this.type, model: model}));

            // initialize saturation
            this.saturation_range = new Slider({el:this.$('#saturation-range')});
            this.saturation_range.on('change', this.on_saturation_changed, this);
            this.saturation_range.render(this.model.get('_saturation'));

            // initialize brightness
            this.brightness_range = new Slider({el: this.$('#brightness-range')});
            this.brightness_range.on('change', this.on_brightness_changed, this);
            this.brightness_range.render(this.model.get('_brightness'));

            // initialize picker
            this.farbtastic = $.farbtastic(this.$('#picker'), this.on_user_pick_color.bind(this));
            this.farbtastic.radius = 93;
            this.farbtastic.square = 0;
            this.farbtastic.width = 250;

            // disable inner square marker
            // added a div to display color output
            this.$('.color').before( '<div id="output"></div>' );
            this.$('.sl-marker').css('display', 'none');

            this.invalidate_color_output();

            this.trigger(this.EVT_INIT)

        },

        on_user_pick_color: function(code) {
            this.$("#output").css("background-color", this.farbtastic.color);
        },

        on_user_confirm_color: function(e) {
            this.model.set_hue(Math.round(this.farbtastic.hsl[0] * 365));
        },

        on_saturation_changed: function(slider) {
            console.log('----> saturation changed', slider.get_value())
            this.model.set_saturation(slider.get_value());
        },

        on_brightness_changed: function(slider) {
            console.log('----> brightness changed', slider.get_value())
            this.model.set_brightness(slider.get_value());
        },

        invalidate_color_output: function() {
            // disable callback
            // update color to farbtastic
            this.farbtastic.setHSL(this.get_hsl());
        },

        get_value: function() {
            // validate value
            if (this.validate()) {
                // return ColorUtil.hex2rgb(this.selected_color_hex);
                return _.extend(this.model.get('value'), {});
            } else {
                // validation failed
                return;
            }
        },

        validate: function(e) {
            this.trigger(this.EVT_VALID)
            return true;
        },

        get_hsl: function() {
            var o = [];
            var ref = this.model.get('value');
            // hue
            o[0] = ref.h / 360;
            // saturation
            o[1] = 1;
            // brightness
            o[2] = .5;
            return o;
        }
    })

    return kbxHSBColor;
});