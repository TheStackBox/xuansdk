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
    'common/components/models/kbx.abstract',
    'moment'
], function (_, kbxGeneric) {

	var kbxInputText = kbxGeneric.extend({
		className: 'kbx.Time',

		toDisplayValue: function() {
			// convert to time
			var m = this.generateMoment();
			if (m !== undefined) {
				return m.format('hh:mm A');
			}
			return;
		},

		generateMoment: function() {
			var m = moment(),
			v = this.get('value')
			if (!isNaN(v)) {
				m.hour(Math.floor(v/3600));
				m.minute((v%3600)/60);

				return m;
			}
			return;
		}

	})

	return kbxInputText;

});