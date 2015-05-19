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
    'underscore',
    'libs/utils/browser'
], function (_) {
    'use strict';


    if (BrowserUtil.isMobile()) {

    	// hijack log
        var _console = console;

        var _trigger_console = function(func, arg) {
            try {
                var output = '';
                var length = arg.length;
                _.each(arg, function(value, index) {
                    switch (typeof value) {
                        case 'string':
                        output += value;
                        break;

                        default:
                        output += JSON.stringify(value);
                        break;
                    }
                    
                    // add space
                    if (index < length - 1) {
                        output += ' ';
                    }
                });
                _console[func].apply(_console, [output]);
            } catch (e) {
                _console.error('!! console_hijack '+e)
            }
        }

        window.console = {};
        window.console.error = function() {
            _trigger_console('error', arguments);
        }
    	window.console.log = function() {
    		_trigger_console('log', arguments);
    	}
        window.console.warn = function() {
            _trigger_console('warn', arguments);
        }

    	console.log('console.log got hijacked!');
    }

});