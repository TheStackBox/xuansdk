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
// the kurobox library
// simple api class for easing developer works
// function:
// handle tokens
// call api
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['exports', 'jquery'], function(exports, $) {
        	root.Kurobox = factory(root, exports, $);
        });
    } else if (typeof exports === 'object') {
        // CommonJS
        var $ = require('jquery')
        factory(root, exports, $);
    } else {
        // Browser globals
       root.Kurobox = factory(root, {}, root.jQuery);
    }
}(this, function (root, Kurobox, $) {
    'use strict'

    // initial setup
    var session = null;

    Kurobox.host = '//127.0.0.1:1111';
    Kurobox.appName = null;

    Kurobox.getSession = function() {
    	return this.session;
    };

    Kurobox.login = function(username, password, callback) {
    	// login to the kurobox
    	Kurobox.api(null, 'login', {username: username, password:password}, callback);
    };

    Kurobox.api = function(method, parameter, callback) {
    	if (session === null) {
    		// no session available, require login
    		callback({returnValue:500, message: 'Login required'});
    	} else {
    		// app process is unknown

    		// send data
    		var url = Kurobox.host + '?func='+method;
    		$.post(Kurobox.host+'func='+method, parameter, function(json, textStatus) {
    			/*optional stuff to do after success */
    		});
    	}
    };

}));