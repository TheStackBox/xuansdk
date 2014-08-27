/**
 * Copyright 2014 Cloud Media Sdn. Bhd.
 * 
 * This file is part of Xuan Automation Application.
 * 
 * Xuan Automation Application is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This project is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public License
 * along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
*/

define([
    'jquery',
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/system/info/boxinfo',
    'libs/backbone/models/system/network/port',
    'Kurobox'
], function ($, _, KuroboxModel, BoxinfoModel, PortModel) {
    'use strict';
    var CloudPassword = KuroboxModel.extend({

        initialize: function(session){
            this.session = session || '';
            Kurobox.cloudhost = Kurobox.cloudhost || 'https://user.thexuan.com';
            this.url = 'server_request';
            this.dev_opt = {
                method: 'GET',
                //url: 'json/example.cloud_login_success.json',
                bypassSession: true,
                param: {}
            }
        },

        //login
        fetch: function(currentPassword, newPassword, options) {
            Kurobox.native('getLanguage', function(lang){
                var paramObj = {};
                paramObj.sapi = '1.0';
                paramObj.lang = lang;
                paramObj.passwd = currentPassword;
                paramObj.newPasswd = newPassword;

                //generate url
                var str = '';
                for (var v in paramObj) {
                    if (str != '') {
                        str += '&';
                    }
                    str += v + '=' + paramObj[v];
                }
                this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/updatePasswd;jsessionid='+this.session+'?'+str;

                //generate sum
                var a = [];
                for (var i in paramObj) {
                    a.push(paramObj[i]);
                }
                this.dev_opt.param.concate = a.sort().join('');

                //call
                KuroboxModel.prototype.fetch.call(this, options);
            }.bind(this), null, 'en')
        }

    });

    return CloudPassword;
});