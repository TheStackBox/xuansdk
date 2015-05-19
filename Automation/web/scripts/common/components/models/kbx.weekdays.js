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
    'common/components/models/kbx.option',
    'common/models/label_value',
], function (_, kbxOption, LabelValue) {

	var spr = kbxOption.prototype;
	var kbxDayOfWeek = kbxOption.extend({
		className: 'kbx.dayOfWeek',

		toDisplayValue: function() {
			var isWeekend = (
				this.get('value').get(0) !== undefined &&
				this.get('value').get(1) === undefined &&
				this.get('value').get(2) === undefined &&
				this.get('value').get(3) === undefined &&
				this.get('value').get(4) === undefined &&
				this.get('value').get(5) === undefined &&
				this.get('value').get(6) !== undefined
				);
			var isWeekday = (
				this.get('value').get(0) === undefined &&
				this.get('value').get(1) !== undefined &&
				this.get('value').get(2) !== undefined &&
				this.get('value').get(3) !== undefined &&
				this.get('value').get(4) !== undefined &&
				this.get('value').get(5) !== undefined &&
				this.get('value').get(6) == undefined
				)

			if (this.get('value').length === this.get('list').length) {
				return lang.translate('everyday');
			} else if (isWeekend) {
         		return lang.translate('weekend');
			} else if (isWeekday) {
				return lang.translate('weekday');
			} else {
				var labels = '';
				this.get('value').each(function(value_item, idx) {
					labels += value_item.get('label');
					if (idx < this.get('value').length - 1) {
						labels += ', ';
					}
				}.bind(this))

				return labels;
			}
        }
	})

	return kbxDayOfWeek;

});
