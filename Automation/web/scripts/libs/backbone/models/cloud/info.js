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
    'jquery',
    'underscore',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/system/info/boxinfo',
    'libs/backbone/models/system/network/port',
    'Kurobox'
], function ($, _, KuroboxModel, BoxinfoModel, PortModel) {
    'use strict';
    var CloudInfo = KuroboxModel.extend({
        defaults: {
            uname: '',
            email: '',
            heartbeat: 3600,
            link: false,
            bid: '',
            sid: ''            
        },

        initialize: function(session){
            this.session = session;
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
        fetch: function(options) {
            Kurobox.native('getLanguage', function(lang){
                var paramObj = {};
                paramObj.sapi = '1.0';
                paramObj.lang = lang;

                this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/userDetails;jsessionid='+this.session+'?'+this.objToParam(paramObj);
                //generate sum
                this.dev_opt.param.concate = this.concatParam(paramObj);

                console.log(this.dev_opt.param);
                //call
                console.log(options);
                KuroboxModel.prototype.fetch.call(this, options);
            }.bind(this), null, 'en')
        },

        parse: function(data) {
            return {
                uname: data.response.uname,
                email: data.response.email,
                heartbeat: data.response.heartbeat,
                bid: data.response.bid,
                link: data.response.link,
                sid: data.response.sid
            }
        },

        objToParam:function (paramObj) {
            //generate url
            var str = '';
            for (var v in paramObj) {
                if (str != '') {
                    str += '&';
                }
                str += v + '=' + paramObj[v];
            }

            return str;
        },

        concatParam:function (paramObj) {
            var sortParamASC = [];

            for(var data in paramObj){
                sortParamASC.push([data, paramObj[data]]);
            }

            sortParamASC.sort();

            var concatParam = '';

            for (var i = 0; i < sortParamASC.length; i++) {
                concatParam += sortParamASC[i][1] || '';
            };

            return concatParam;
        }
        
    });

    return CloudInfo;
});