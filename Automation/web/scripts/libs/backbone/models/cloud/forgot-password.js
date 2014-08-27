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
    'libs/backbone/models/kurobox-model'
], function ($, _, KuroboxModel) {
    'use strict';
    var ForgotPasswordModel = KuroboxModel.extend({
        initialize:function (e) {
            Kurobox.cloudhost = Kurobox.cloudhost || 'https://user.thexuan.com';
        },
        //forgot password
        fetch: function(username, email, lang, options) {
            this.url = 'server_request';
            var paramObj = {};
            paramObj.sapi ='1.0';
            paramObj.uname = username;
            paramObj.email = email;
            paramObj.lang = lang;

            //generate url
            var str = '';
            for (var v in paramObj) {
                if (str != '') {
                    str += '&';
                }
                str += v + '=' + paramObj[v];
            }

            var concat_str = '';
            for (var i in paramObj) {
                concat_str += paramObj[i];
            }

            this.dev_opt = {
                method: 'GET',
                //url: 'json/example.set_timezone.json',
                bypassSession: true,

                param: {url:Kurobox.cloudhost+'/c/client/forgotPasswd?'+str, concate:concat_str}
            }
            //call
            KuroboxModel.prototype.fetch.call(this, options);
        }
    });

    return ForgotPasswordModel;
});