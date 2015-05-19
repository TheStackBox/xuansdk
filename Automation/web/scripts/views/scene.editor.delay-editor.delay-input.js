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
    'common/components/views/component.control.time',
    'common/components/models/kbx.time',
    'moment'
], function ($, _, TimeComponent, KbxTime) {

	var spr = TimeComponent.prototype;
	var DelayInputComponent = TimeComponent.extend({
		time_setting: {
            mode: 'scroller',
            display: 'inline',
            timeWheels: 'HHiiss',
            showLabel: true,
            minDate: new Date(null, null, null, 0, 0, 1)
        },

         get_value: function() {
         	var v = spr.get_value.call(this);
         	if (v != undefined) {
         		var value = this.$('#time-container').mobiscroll('getDate');
         		var m = moment(value);
         		v += m.second();
         	}

         	return v
        },

	})

	return DelayInputComponent;
});
