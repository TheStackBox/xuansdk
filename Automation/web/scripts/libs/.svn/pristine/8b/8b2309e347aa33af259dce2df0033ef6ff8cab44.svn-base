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