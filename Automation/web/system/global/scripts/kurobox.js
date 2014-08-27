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
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['exports', 'jquery', 'underscore'], function(exports, $, _) {
            root.Kurobox = factory(root, exports, $, _);
        });
    } else if (typeof exports === 'object') {
        // CommonJS
        var $ = require('jquery');
        var _ = require('underscore');
        root.Kurobox = factory(root, exports, $, _);
    } else {
        // Browser globals
        var instance = function() {
            //this.initialize.apply(this, arguments);
        }
        root.Kurobox = factory(root, instance, root.$, root._);
    }
}(this, function (root, Kurobox, $, _) {
    'use strict'
    var API_URL = '/cgi-bin/syb_reqresp_cgi';
    var EVENT_SOURCE_URL = '/cgi-bin/syb_event_cgi';
    var generate_login_callback = function() {
        return '/system/?callback='+encodeURIComponent(root.location);
    }

    var assist_default = function(obj, def_obj) {
        for (var prop in def_obj) {
            if (obj[prop] === undefined) {
                obj[prop] = def_obj[prop];
            }
        }

        return obj;
    }
    Kurobox.host = '';

    // enabled global api error handling for ui changes
    Kurobox.global_api_error_handler = undefined;

    // global setting for auto redirect to login
    Kurobox.redirectLogin = true;

    var is_login_error = function(error_code) {
        var pIndex = _.indexOf([403, 401, 405], error_code)
        return (pIndex >= 0)
    }

    var _api_error_handling = function(err_obj, options) {
        // trigger global api error handler
        if (Kurobox.global_api_error_handler !== undefined && !options.skipGlobalError) {
            Kurobox.global_api_error_handler(err_obj, function() {
                if (is_login_error(err_obj.error.code) && options.redirectLogin === true) {
                    // assume required login
                    root.location = generate_login_callback();
                } else {
                    if (options.error) options.error(err_obj);
                }
            })
        } else {
            if (options.error) options.error(err_obj);
        }
    }

    Kurobox.api = function(method, param, options) {
        var def_options = {
            redirectLogin: Kurobox.redirectLogin,
            url: Kurobox.host+API_URL,
            httpMethod: 'POST'
        };

        options = assist_default(options, def_options);

        // var param = param || {};
        var vparam = {};
        if (Kurobox.app_id !== undefined || options.app_id !== undefined) {
            options.url += '?app_id='+(Kurobox.app_id || options.app_id);
            vparam.method = method;
        } else {
            vparam.func = method;
        }

        $.extend(vparam, param)

        console.log('api url='+options.url+'?'+$.param(vparam));

        return $.ajax({
            type: options.httpMethod,
            timeout: options.timeout || 60000,
            url: options.url,
            data: vparam,
            dataType: 'json',
            success: function(data, textStatus, jqXHR) {
                if (data.theKuroBox.returnValue === 100) {
                    if (options.success) {
                        options.success({
                            response: data.theKuroBox.response,
                            error: {
                                code: data.theKuroBox.returnValue,
                                message: data.theKuroBox.returnMessage
                            },
                            ajax: {
                                data: data,
                                textStatus: textStatus,
                                jqXHR: jqXHR
                            }
                        })
                    }
                } else {
                    
                    var err_obj = {
                        error: {
                            code: data.theKuroBox.returnValue,
                            message: data.theKuroBox.returnMessage
                        },
                        ajax: {
                            data: data,
                            textStatus: textStatus,
                            jqXHR: jqXHR
                        }
                    }

                    _api_error_handling(err_obj, options);
                }
            },
            error: function(jqXHR, textStatus, httpError) {
                var err_obj = {
                    error: {
                        code: -1,       // ajax error
                        message: httpError || textStatus,
                    },
                    ajax: {
                        textStatus: textStatus,
                        jqXHR: jqXHR,
                        httpError: httpError
                    }
                }
                
                _api_error_handling(err_obj, options);
            }
        });
    }

    var eventSource = function() {
        this.initialize.apply(this, arguments);
    }
    var event_tag = '__evt__';
    var _pending_socket_evt;
    var ping = false;
    var socket_event_handler;
    _.extend(eventSource.prototype, {
        verbose: false,
        connected: false,
        _events: {},
        initialize: function() {
            socket_event_handler = this._onSocketEvent.bind(this);
        },
        on: function(name, callback, context) {
            context = context || this;
            name = event_tag+name;
            var add_socket_evt = false;
            if (this._events[name] === undefined) {
                this._events[name] = [];
                add_socket_evt = true;
            }
            this._events[name].push({name: name, callback: callback, context: context});

            if (name.match('socket:') && add_socket_evt) {
                var sc_evt = name.replace(event_tag+'socket:', '');
                this._addSocketEvent(sc_evt);
            }
        },
        off: function(name, callback, context) {
            var removeSocketEvent = function(name) {
                if (this._es !== undefined && name.indexOf('socket:') >= 0) {
                    var type = name.replace(event_tag+'socket:', '');
                    if (this.verbose) {
                        console.log('EventSource removing eventlistener:', type)
                    }
                    this._es.removeEventListener(type, this.socket_event_handler, false);
                }
            }.bind(this);

            var removeEvent = function(name) {
                removeSocketEvent(name);
                this._events[name] = undefined;
            }.bind(this);

            name = event_tag+name;

            if (name === undefined) {
                // clear every things
                _.each(this._events, function(evt) {
                    _.each(evt, function(evt_listener) {
                        removeSocketEvent(evt_listener.name);
                    })
                })
                this._events = [];
            } else {
                if (this._events[name] !== undefined) {
                    if (callback === undefined) {
                        // remove all listener to specific event
                        removeEvent(name);
                    } else {
                        // remove particular callback
                        _.each(this._events[name], function(evt_listener, index) {
                            if (evt_listener.callback === callback && evt_listener.context === context) {

                                // remove from list
                                this._events[name].splice(index, 1);

                                if (this._events[name].length === 0) {
                                    removeEvent(name);
                                }
                                return false;
                            }
                        }.bind(this))
                    }
                }
            }
            /*
            var oname = name;
            if (name === undefined) {
                // off() remove all listeners
                _.each(this._events, function(listeners, type) {
                    type = type.replace(event_tag, '');
                    this.off(type);
                }.bind(this))
            } else {
                name = (name.indexOf(event_tag) < 0) ? event_tag+name : name;

                var evtArr = this._events[name];
                if (callback === undefined) {
                    // off('event') remove 'event' all listener
                    _.each(evtArr, function(evt, index){
                        this.off(oname, evt.callback, evt.context);
                    }.bind(this))
                    this._events[name] = undefined;
                } else {
                    // off('event', callback, this) remove  event's callback function
                    var removedEvt;
                    _.each(evtArr, function(evt, index) {
                        if (evt.callback === callback && evt.context === context) {
                            console.log('--- hitttt', index)
                            removedEvt = evtArr.splice(1, index);
                            console.log('--- removedEvt', removedEvt)
                            return false;
                        }
                    });
                    if (removedEvt !== undefined) {
                        console.log('EventSource remove listener:', name, callback == undefined, context == undefined);
                        name = name.replace(event_tag+'socket:', '');
                        this._es.removeEventListener(name, callback, context);
                    }
                }
            }*/
        },
        trigger: function(name) {
            name = event_tag+name;
            var listeners = this._events[name];
            var args = Array.prototype.slice.call(arguments, 1);
            if (listeners) {
                _.each(listeners, function(listener) {
                    listener.callback.apply(listener.context, args)
                }.bind(this))
            }
        },
        start: function() {
            if (typeof(EventSource) === "undefined") {
                throw 'EventSource support is not available in this browser!'
                return;
            }

            if (this._es === undefined) {
                this.url = Kurobox.host+EVENT_SOURCE_URL+'?app_id='+Kurobox.app_id;
                if (this.verbose) console.log('EventSource init', this.url);
                this._es = new EventSource(this.url);
                this._es.addEventListener('open', this._onEsInit.bind(this), false);
                this._es.addEventListener('error', this._onEsError.bind(this), false);
                this._es.addEventListener('ping', this._onEsPing.bind(this), false);

                if (_pending_socket_evt !== undefined) {
                    // add pending event
                    _.each(_pending_socket_evt, function(evt) {
                        this._addSocketEvent(evt);
                    }.bind(this));
                    _pending_socket_evt = undefined;
                }
                this.connected = false;
            }
        },
        stop: function() {
            // NOTE: once event source is close. all event listener will be closed too
            if (this._es !== undefined) {
                this.off();
                this._es.removeEventListener('open', this._onEsInit.bind(this), false);
                this._es.removeEventListener('error', this._onEsError.bind(this), false);
                this._es.removeEventListener('ping', this._onEsPing.bind(this), false);
                this._es.close();
                this._es = undefined;
                this.connected = false;
                if (this.verbose) console.log('EventSource disconnected')
            }
        },
        _onEsError: function(e) {
            if (this.verbose) {
                console.error('EventSource error:', e);
                this.trigger('error');
                this.stop();
            }
        },
        _onEsInit: function(e) {
            if (this.verbose) {
                console.log('EventSource connected:', this.url);
            }

            // prepare for first ping
            this.connected = false;
        },
        _onEsPing: function(e) {
            if (!this.connected) {
                this.connected = true
                this.trigger('connected');
            }

            if (this.verbose) {
                ping = !ping;
                // if (ping) {
                //     console.log('EventSource stay-alive-ping ♥')
                // } else {
                //     console.log('EventSource stay-alive-ping ♡')
                // }
            }
        },
        _onSocketEvent: function(e) {
            if (this.verbose) {
                console.log('EventSource ['+e.type+']', e.data);
            }
            var type = 'socket:'+e.type;
            this.trigger(type, JSON.parse(e.data));
        },
        _addSocketEvent: function(type) {
            if (this._es !== undefined) {
                // assume event source is init
                if (this.verbose) {
                    console.log('EventSource listening', type);
                }
                this._es.addEventListener(type, socket_event_handler, false)
            } else {
                // pending socket event
                if (_pending_socket_evt === undefined) {
                    _pending_socket_evt = [];
                }
                _pending_socket_evt.push(type);
            }
        }
    })
    Kurobox.socket = new eventSource();
    
    //Handle Native function(wrapper function)
    Kurobox.native = function(func, callback, param, defaultCallbackValue){
        var _callback = function() {
            if(callback){
                callback.apply(this, $.isArray(defaultCallbackValue) ? defaultCallbackValue : [defaultCallbackValue]);
            }
        }.bind(this)

        if(typeof NativeMethod === 'undefined'){
            _callback();
        } else {
            var vparam = [];
            if(typeof param == 'string'){
                vparam.push(param);
            }else{
                vparam = vparam.concat(param);
            }

            if(callback){
                vparam.push(callback);
            }

            if (NativeMethod[func] === undefined) {
                console.error('!! Not able to find this native function '+func);
                _callback();
                return;
            }
            return NativeMethod[func].apply(this, vparam);
        }
    };

    return Kurobox;
}));
