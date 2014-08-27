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
    var CloudSession = KuroboxModel.extend({
        defaults: {
            uname: '',
            email: '',
            heartbeat: 3600,
            link: false,
            bid: '',
            sid: ''            
        },

        initialize: function(){
            Kurobox.cloudhost = Kurobox.cloudhost || 'https://user.thexuan.com';

            this.url = 'server_request';
            this.dev_opt = {
                method: 'GET',
                //url: 'json/example.cloud_login_success.json',
                bypassSession: true,
                param: {}
            }
        },

        //reponsible to retrieve box name,cpu id and lang 
        get_box_info:function (key, options, callback) {
            //get box name if not available
            if(_.isEmpty(this.get('boxName'))){
                var boxModel = new BoxinfoModel();
                boxModel.fetch({
                    success:function(){
                        console.log('boxName', boxModel.get('name'));
                        this.set('boxName', boxModel.get('name'));
                        this.set('cpuid', boxModel.get('cpuid'));
                        this.get_box_info(key, options, callback);
                    }.bind(this),
                    error:function(){
                        options.error();
                    }.bind(this)
                })
                return false;
            }

            //get lang
            if(_.isEmpty(this.get('lang'))){
                Kurobox.native('getLanguage', function(lang){
                    console.log('lang', lang);
                    this.set('lang', lang);      
                    callback(key, options);            
                }.bind(this), null, 'en')
                return false;
            }

            //get port if not available
            // if(_.isEmpty(this.get('http_port')) || _.isEmpty(this.get('https_port'))){
            //     var portModel = new PortModel();
            //     portModel.fetch({
            //         success:function(){
            //             this.set('http_port', portModel.get('http_port'));
            //             this.set('https_port', portModel.get('https_port'));
            //             callback(key, options);
            //         }.bind(this),
            //         error:function(){
            //             options.error();
            //         }.bind(this)
            //     })
            //     return false;
            // }

            return true;
        },

        //login
        fetch: function(key, options) {
            var success = this.get_box_info(key, options, this.fetch.bind(this));
            if(success){
                //set require arg( no need passing mac address and fwversion due server request api already prefix)
                var paramObj = key;
                paramObj.sapi='1.0';
                paramObj.boxName = this.get('boxName');
                paramObj.cid = this.get('cpuid');
                paramObj.lang = this.get('lang');

                //generate url
                var str = '';
                for (var v in paramObj) {
                    if (str != '') {
                        str += '&';
                    }
                    str += v + '=' + paramObj[v];
                }

                var concat_str = "";
                for (var i in paramObj) {
                    concat_str += paramObj[i];
                }

                //generate url
                this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/login?'+str;
                //generate sum
                this.dev_opt.param.concate = concat_str;

                console.log(this.dev_opt.param);
                //call

                var callback = {
                    success:function(target, data, sync){
                        console.log('set session to wrapper!!!');

                        // var storeData = {};
                        //     storeData.email = this.get('email');
                        //     storeData.heartbeat = this.get('heartbeat');
                        //     storeData.link = this.get('link');
                        //     storeData.bid = this.get('bid');
                        //     storeData.sid = this.get('sid');
                        //     storeData.timestamp = $.now();

                        // var session = encodeURIComponent(JSON.stringify(storeData));
                        // console.log(session);
                        //NativeMethod.setKeyWithData('session', session);
                        Kurobox.native('setTemporaryKeyWithData', null, ['session', this.get('sid')]);
                        console.log('save session:');
                        console.log(this.get('sid'));
                        if(options.success){options.success(target, data, sync)}
                    }.bind(this),
                    error:function(target, data, sync){
                        if(options.error){options.error(target, data, sync)}
                    }.bind(this)         
                }

                KuroboxModel.prototype.fetch.call(this, callback);
            }
        },

        save: function(key, options) {
            var success = this.get_box_info(key, options, this.save.bind(this));

            if(success){
                var paramObj = key;
                console.log('key.email: ', key.email);
                paramObj.sapi ='1.0';
                paramObj.boxName = this.get('boxName');
                paramObj.cid = this.get('cpuid');
                paramObj.lang = this.get('lang');

                //generate url
                var str = '';
                for (var v in paramObj) {
                    if (str != '') {
                        str += '&';
                    }
                    str += v + '=' + paramObj[v];
                }

                this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/registerUser?'+str;

                //generate sum
                var str = '';
                for (var i in paramObj) {
                    str += paramObj[i];
                }

                this.dev_opt.param.concate = str;
                console.log(this.dev_opt.param.url);
                console.log(this.dev_opt.param);

                var callback = {
                    success:function(target, data, sync){
                        console.log('set session to wrapper!!!');
                        Kurobox.native('setTemporaryKeyWithData', null, ['session', this.get('sid')]);
                        console.log('save session:');
                        console.log(this.get('sid'));
                        if(options.success){options.success(target, data, sync)}
                    }.bind(this),
                    error:function(target, data, sync){
                        if(options.error){options.error(target, data, sync)}
                    }.bind(this)         
                }

                KuroboxModel.prototype.fetch.call(this, callback);
            }
        },

        logout: function(username, options) {
            // user log out
            Kurobox.native('getLanguage', function(lang){
                this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/logout?sapi=1.0&uname='+username +'&lang='+lang;    
                this.dev_opt.param.concat = '1.0'+username+lang;
            }.bind(this), null, 'en');

            KuroboxModel.prototype.fetch.call(this, options);
        },

        linkbox: function(enable, options) {
            var success = this.get_box_info(null, options, this.fetch.bind(this));
            console.log('link box!!!');
            if(success){
                Kurobox.native('getTemporaryDataOfKey', function(session){
                    console.log('session return:');
                    console.log(session);
                    console.log('ori session return:');
                    console.log(this.get('sid'));
                    console.log('final session return:');
                    session = session || this.get('sid');
                    console.log(session);
                    if(_.isEmpty(session)){
                        var data = {error:{}};
                            data.error.code = 5002;
                            data.error.message = 'Your session is expired. Please try again.';

                        if(options.error){options.error(null, data, null)}
                    }else{
                        //set require arg( no need passing mac address and fwversion due server request api already prefix)
                        var paramObj = {};
                        if(enable){
                            paramObj.sapi='1.0';
                            paramObj.boxName = this.get('boxName');
                            paramObj.cid = this.get('cpuid');                            
                            paramObj.lang = this.get('lang');
                        }else{
                            paramObj.sapi='1.0';
                            paramObj.lang = this.get('lang');
                        }

                        //generate url
                        var str = '';
                        for (var v in paramObj) {
                            if (str != '') {
                                str += '&';
                            }
                            str += v + '=' + paramObj[v];
                        }

                        var concat_str = "";
                        for (var i in paramObj) {
                            concat_str += paramObj[i];
                        }

                        //generate url
                        if(enable){
                            this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/linkBox;jsessionid='+session+'?'+str;
                        }else{
                            this.dev_opt.param.url = Kurobox.cloudhost+'/c/client/unlinkBox;jsessionid='+session+'?'+str;
                        }
                        //generate sum
                        this.dev_opt.param.concate = concat_str;

                        console.log(this.dev_opt.param);
                        //call
                        KuroboxModel.prototype.fetch.call(this, options);
                    }
                }.bind(this), 'session');
            }
        },

        // unlinkBox: function(options) {
        //     var success = this.get_box_info(key, options, this.fetch.bind(this));

        //     if(success){
        //         Kurobox.native('getDataOfKey', function(sid){
        //             if(_.isEmpty(sid)){
        //                 var data = {error:{}};
        //                     data.error.code = 5002;
        //                     data.error.message = 'Your session is expired. Please try again.';

        //                 if(options.error){options.error(null, data, null)}
        //             }else{
        //                 //set require arg( no need passing mac address and fwversion due server request api already prefix)
        //                 var paramObj = key;
        //                 paramObj.boxName = this.get('boxName');
        //                 paramObj.cid = this.get('cpuid');
        //                 paramObj.lang = this.get('lang');
        //                 paramObj.sid = sid;

        //                 var str = "";
        //                 for (var i in paramObj) {
        //                     str += paramObj[i];
        //                 }

        //                 //generate url
        //                 this.dev_opt.param.url = CloudHost+'/davidbox/c/client/unlinkBox?sapi1.0&'+$.param(paramObj);
        //                 //generate sum
        //                 this.dev_opt.param.concate = str;

        //                 console.log(this.dev_opt.param);
        //                 //call
        //                 KuroboxModel.prototype.fetch.call(this, options);
        //             }
        //         }.bind(this), 'sid');
        //     }
        // },

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

        
    });

    return CloudSession;
});