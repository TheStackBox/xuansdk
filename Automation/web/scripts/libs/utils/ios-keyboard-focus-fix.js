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

	// for ios only; prevent fixed position element not glue to the
	// desired position. be sure that @import 'libs/ios-fixed-keyboard-focus'

	var $ = require('jquery');
	var $body = $('body');
	$(document).on('focus', 'input,textarea', function(){
        $body.addClass('ios-keyboard-focus-fix');
    }).on('blur', 'input,textarea', function(){
        $body.removeClass('ios-keyboard-focus-fix');
    });

	console.log('-- applying ios keyboard fix')
});