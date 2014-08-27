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

// this is similar support for kbxComponents

define([
    'underscore',
    'models/kbx.abstract',
    'libs/utils/color'
], function (_, kbxGeneric) {

	var spr = kbxGeneric.prototype;
	var kbxColor = kbxGeneric.extend({
		className: 'kbx.kbxColor',
		default_value: {
			r: 255,
			g: 0,
			b: 0
		},
		toDisplayValue: function() {
			var v = this.get('value');
			return (v) ? ColorUtil.rgb2hex(v.r, v.g, v.b) : undefined;
		},

		getDefaultColor: function() {
			var v = this.get('default_value') || this.default_value;
			return ColorUtil.rgb2hex(v.r, v.g, v.b);
		}

	})

	return kbxColor;

});