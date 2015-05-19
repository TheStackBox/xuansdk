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
    'jquery'
], function ($) {
	'use strict';
    //reset element with fixed position while focus input page scroll 
    var timer;
    $(document).on('focus', 'input', function(){
        window.clearTimeout(timer);
        timer = window.setTimeout(function(){
            window.scrollTo(document.body.scrollLeft, document.body.scrollTop);
        }, 300);
    }.bind(this)).on('blur', 'input', function(){
        window.clearTimeout(timer);
        timer = window.setTimeout(function(){
            window.scrollTo(document.body.scrollLeft, document.body.scrollTop);
        }, 300);
    }.bind(this));

});