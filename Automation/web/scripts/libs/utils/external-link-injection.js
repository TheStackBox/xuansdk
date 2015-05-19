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
define(function(require) {
	'use restrict';

	var $ = require('jquery');
	$('body').off('click').on('click', 'a[target="_blank"]', function(e) {
		if (typeof NativeMethod !== 'undefined' && typeof NativeMethod.openURLInExternalBrowser === 'function') {
			// inside wrapper
			var url = $(e.currentTarget).attr('href');

			// execute wrapper
			NativeMethod.openURLInExternalBrowser(url, function(ok) {
				if (ok) {
					console.log('--- open url in browser'+ url);
				} else {
					console.log('--- failed to open url from wrapper. damn!!!')
					window.location = url;
				}
			});

			return false;
		}
	})
	console.log('--- external link handler injected');
});