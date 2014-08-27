/*global define*/

define([
    'jquery',
    'underscore'
], function ($, _) {
	'use strict';

	var ColorUtil = window.ColorUtil = function() {};
	var componentToHex = function(c) {
	    var hex = Number(c).toString(16);
		console.log('hex', c, hex)
	    return hex.length == 1 ? "0" + hex : hex;
	}

	var hex2rgb = function(hex) {
		var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
	    return result ? {
	        r: parseInt(result[1], 16),
	        g: parseInt(result[2], 16),
	        b: parseInt(result[3], 16)
	    } : null;
	}

	var rgb2hex = function(r, g, b) {
		return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
	}

	ColorUtil.hex2rgb = hex2rgb;
	ColorUtil.rgb2hex = rgb2hex;

});