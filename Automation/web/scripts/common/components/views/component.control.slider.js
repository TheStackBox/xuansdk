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
    'libs/utils/browser',
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';
    var spr = AbstractControlComponent.prototype;
    var kbxSlider = AbstractControlComponent.extend({
    	template: JST['app/scripts/common/components/templates/component.control.slider.ejs'],
    	events: {
            'input #slider': 'on_value_changed'
        },
    	initialize: function() {
            if (BrowserUtil.isMobile()) {
                if (navigator.userAgent.match('AppleWebKit') == undefined) {
                    // android
                    this.events['touchend #slider'] = 'on_value_confirmed';
                } else {
                    // ios
                    // change event will fired everything the value changed
                    this.events['change #slider'] = 'on_value_changed';
                    this.events['touchend #slider'] = 'on_value_confirmed';
                }
            } else {
                this.events['change #slider'] = 'on_value_confirmed';
            }
            spr.initialize.apply(this, arguments);
        },

    	render: function(model) {
    		this.model = model;
            this.sizeRange = (this.model.get('extra').kbxParamMaxValue || 100) - (this.model.get('extra').kbxParamMinValue || 0);

    		console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            this.$el.html(this.template({model: model}));

            _.defer(function() {
                // define initial slider
                this.oriSliderWidth = this.$('#range').width();
                this.update_slider_range(this.model.get('value') || this.model.get('extra').kbxParamMinValue || 0);
                
                this.trigger(this.EVT_INIT);
            }.bind(this))

    	},

    	get_value: function() {
    		return this.$('#slider').prop('value');
    	},

        set_value: function(value) {
            this.update_slider_range(value);
        },

        update_slider_range: function(val) {
            var range_width = (val / this.sizeRange) * this.oriSliderWidth;
            this.$('#range').css('width',range_width);
        },

    	on_value_confirmed: function() {
            var value = this._handleDecimal(this.$('#slider').prop('value'), this.model.get('extra').kbxParamDecimal);
    		this.$('#rangevalue').text(value);
            this.update_slider_range(value);

            this.trigger('change', this);
    	},

    	on_value_changed: function() {
            var value = this._handleDecimal(this.$('#slider').prop('value'), this.model.get('extra').kbxParamDecimal);
    		this.$('#rangevalue').text(value);
            this.update_slider_range(value);
    	},

        _handleDecimal: function(val, decimal) {
            if (decimal === undefined) return val;
            return parseFloat(val).toFixed(decimal);
        }
    });

    return kbxSlider;
});