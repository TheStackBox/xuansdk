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
define(['jquery', 'cryptoMD5'], function($) {
	'use strict';

	var KuroboxInternalAPI = {};

	KuroboxInternalAPI.host = 'https://192.168.0.62';
	KuroboxInternalAPI.session = null;
	KuroboxInternalAPI.api = function(method, parameter, callback, dev_opt) {
		//console.log('KuroboxInternalAPI api: method=', method);
		//console.log('KuroboxInternalAPI api: param=', parameter);
		// console.log('session', this.session);
		// console.log('test logic', method === 'login', this.session !== null)
		var sessionPass = (method === 'login' || method === 'set_box' || this.session !== null || (dev_opt !== null && dev_opt.bypassSession === true));
		// console.log('sessionPass', sessionPass);

		if (sessionPass) {
			// assume user has login or going to login
			parameter.func = method;
			if (this.session) {
				parameter.token = this.session.token;
			}

			var url = KuroboxInternalAPI.host+'/cgi-bin/syb_reqresp_cgi';
			if (dev_opt.url !== null) {
				url = dev_opt.url;
			}
			console.log('KuroboxInternalAPI api: url =', url);

			// enable crossdomain setting
			jQuery.support.cors = true;
			$.ajax({
				type: (dev_opt.method === null) ? 'POST' : dev_opt.method,
				url: url,
				data: parameter,
				crossdomain: true,
				dataType: 'json',
				success: function(data, status, xhr) {
					// console.log('KuroboxInternalAPI.api success: data', data);
					// console.log('KuroboxInternalAPI.api success: textstatus', status);
					// console.log('KuroboxInternalAPI.api success: xhr', xhr);
					if (data.returnValue !== 0 || data.returnValue !== undefined) {
						callback(true, data);
					} else {
						callback(false, data);
					}
				},
				error: function(xhr, status, error) {
					//console.log('KuroboxInternalAPI.api error: error', error);
					//console.log('KuroboxInternalAPI.api error: status', status);
					callback(false, xhr);
				}
			});
		} else {
			// user has NOT login
			callback(false, {returnValue:500, message:'Login required'});
		}
	};

	KuroboxInternalAPI.login = function(username, password, callback) {
		var saltedPwd = CryptoJS.MD5(password).toString();
		//console.log('KuroboxInternalAPI login: saltedPwd=',saltedPwd);
		KuroboxInternalAPI.api('login', {username: username, password: saltedPwd}, function(data) {
			// save the session
			KuroboxInternalAPI.session = {
				token: data.token
			};
			callback(data);
		});
	};

	KuroboxInternalAPI.register = function(mac_address, box_name, username, password, callback) {
		var saltedPwd = CryptoJS.MD5(password).toString();
		//console.log('KuroboxInternalAPI login: saltedPwd=',saltedPwd);
		KuroboxInternalAPI.api('set_box', {mac_address: mac_address, box_name: box_name, username: username, password: saltedPwd}, function(data) {
			// save the session
			KuroboxInternalAPI.session = {
				token: data.token
			};
			callback(data);
		});
	}

	return KuroboxInternalAPI;
});