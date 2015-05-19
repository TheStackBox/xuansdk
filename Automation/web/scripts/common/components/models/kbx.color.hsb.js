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

// this is similar support for kbxComponents

define([
    'underscore',
    'common/components/models/kbx.color',
    'common/components/models/kbx.slider',
    'libs/utils/color',
], function (_, kbxColor, kbxSlider) {
	
	var SATURATION_MAX = 100;
	var SATURATION_MIN = 0;
	var SATURATION_STEP = 1;

	var BRIGHTNESS_MAX = 100;
	var BRIGHTNESS_MIN = 1;
	var BRIGHTNESS_STEP = 1;

	var spr = kbxColor.prototype;
	var kbxHSBColor = kbxColor.extend({
		className: 'kbx.kbxHSBColor',
		default_value: {
			h: 0,
			s: 1,
			b: 1
		},

		parse: function(data) {
			// sample data
			// data.

			var o = spr.parse.call(this, data);

			// create slider model later use by component
			var create_slider_model = function(min, max, value, step, value_ratio) {
				var m = new kbxSlider({
					extra: {
						kbxParamMaxValue: max,
						kbxParamMinValue: min,
						kbxParamStep: step,
					},
				})

				if (value_ratio == undefined) {
					m.set('value', Math.round(value * (max-min)));
				} else {
					m.set('value', Math.round(value * value_ratio));
				}
				return m;
			}
			
			if (data.kbxParamCurrentValue != undefined) {
				// float number
				o.value = {
					h: Number(parseFloat(data.kbxParamCurrentValue.h).toFixed(2)),
					s: Number(parseFloat(data.kbxParamCurrentValue.s).toFixed(2)),
					b: Number(parseFloat(data.kbxParamCurrentValue.b).toFixed(2))
				}

				o._saturation = create_slider_model(SATURATION_MIN, SATURATION_MAX, o.value.s, SATURATION_STEP)
				o._brightness = create_slider_model(BRIGHTNESS_MIN, BRIGHTNESS_MAX, o.value.b, BRIGHTNESS_STEP, BRIGHTNESS_MAX)

				console.log('o.saturation', o._saturation)
				console.log('o._brightness', o._brightness)
			} else {
				o.value = _.extend({}, this.default_value)
				o._saturation = create_slider_model(SATURATION_MIN, SATURATION_MAX, o.default_value.s, SATURATION_STEP)
				o._brightness = create_slider_model(BRIGHTNESS_MIN, BRIGHTNESS_MAX, o.default_value.b, BRIGHTNESS_STEP, BRIGHTNESS_MAX)
			}
			
			return o;
		},

		clone: function() {
			var o = spr.clone.call(this);
			// cloning sliders
			o.set('_saturation', this.get('_saturation').clone());
			o.set('_brightness', this.get('_brightness').clone());

			return o;
		},

		toDisplayValue: function() {
			if (this.get('value') != undefined) {
				return this._hslString(this.get('value'));
			}
			return;
		},

		getDefaultColor: function() {
			var v = this.get('default_value') || this.default_value;
			return this._hslString(v);
		},

		_hslString: function(v) {
			if (v != undefined) {
				var rv = 'hsl(';
					rv += Math.round(this.get('value').h) +', ';
					rv += Math.round(this.get('value').s * (SATURATION_MAX - SATURATION_MIN))+'%, ';
					rv += Math.round(this.get('value').b * (BRIGHTNESS_MAX))+'%)';
				return rv;
			}
			return;	
		},

		set_hue: function(v) {
			this.get('value').h = v;
			console.log('test value>>>>>', this.get('value'), this.toDisplayValue());
		},

		set_brightness: function(v) {
			this.get('value').b = v / (BRIGHTNESS_MAX);

			// update kbx slider model
			this.get('_brightness').set('value', v);
			console.log('test value>>>>>', this.get('value'), this.toDisplayValue());
		},

		set_saturation: function(v) {
			this.get('value').s = v / (SATURATION_MAX - SATURATION_MIN);

			// update kbx slider model
			this.get('_saturation').set('value', v);
			console.log('test value>>>>>', this.get('value'), this.toDisplayValue());
		}

	}, {
		// constant
		SATURATION_MAX: SATURATION_MAX,
		SATURATION_MIN: SATURATION_MIN,
		SATURATION_STEP: SATURATION_STEP,

		BRIGHTNESS_MAX: BRIGHTNESS_MAX,
		BRIGHTNESS_MIN: BRIGHTNESS_MIN,
		BRIGHTNESS_STEP: BRIGHTNESS_STEP
	})

	return kbxHSBColor;

});