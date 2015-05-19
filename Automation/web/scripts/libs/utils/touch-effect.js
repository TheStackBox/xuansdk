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
	function on_touch_end(e){
        var el = $(e.target);
        var el_type = el.prop('tagName');
        if(el_type == 'BUTTON'){
            //el.css("background-color","#fa2283");
            el.removeClass("button-touch");
        }else{            
            if(el.attr('touch') == "true"){
                el.removeClass("element-touch");
            }else if(el.parent().attr('touch') == "true"){
                $(el.parent()).removeClass("element-touch");
            }else if(el.parent().parent().attr('touch') == "true"){
                $(el.parent().parent()).removeClass("element-touch");
            }else if(el.parent().parent().parent().attr('touch') == "true"){
                $(el.parent().parent().parent()).removeClass("element-touch");
            }
        }
	}

    $(document).bind('touchstart', function(e){
        var el = $(e.target);
        var el_type = el.prop('tagName');
        //if allow to touchable
        if(el_type == 'BUTTON' && el.is(':disabled') == false){
            //el.css("background-color","#cdcdcd");
            el.addClass("button-touch");
        }else{
            if(el.attr('touch') == "true"){
                el.addClass("element-touch");
            }else if(el.parent().attr('touch') == "true"){
                $(el.parent()).addClass("element-touch");
            }else if(el.parent().parent().attr('touch') == "true"){
                $(el.parent().parent()).addClass("element-touch");
            }else if(el.parent().parent().parent().attr('touch') == "true"){
                $(el.parent().parent().parent()).addClass("element-touch");
            }
        }
    }).bind('touchend', on_touch_end.bind(this)).bind('touchmove', on_touch_end.bind(this));

});