/*global define*/

define([
    'jquery',
    'underscore'
], function ($, _) {
	'use strict';
	var ObjUtil = window.ObjUtil = function() {};

	var clone = function(obj) {
        var target = {};
        for (var i in obj) {
            if (obj.hasOwnProperty(i)) {
                target[i] = obj[i];
            }
        }
        return target;
	}

	ObjUtil.clone = clone;
});