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
define([
    'Kurobox',
	'underscore'
], function (Kurobox, _) {
    var _xhr_store = {};
    var gen_id = function() {
        return new Date().getTime();
    }
    var clazz = function() {
        this.initialize.apply(this, arguments)
    }
	_.extend(clazz.prototype, {
		dev_opt: null,
        get_xhr: function(id) {
            return _xhr_store[id];
        },

        fetch: function(options) {
            // inject parsing script
            options = options || {};
            var successCb;
            if (options.success) {
                successCb = options.success;
            }; 

            options.success = function(model, kurobox, options) {
                // parse data
                this.set(this.parse(kurobox), {silent: (successCb !== null)});

                // run callback
                if (successCb) successCb(model, kurobox, options);
            }.bind(this);

            this._callApi(options);
        },

        save: function (key, val, options) {
            var attrs, api_param;

            // Handle both `"key", value` and `{key: value}` -style arguments.
            if (typeof key === 'object') {
                if (!key.success && !key.error) {
                    attrs = key;
                    options = (val) ? val : {};
                } else {
                    options = key;
                }
            } else {
                (attrs = {})[key] = val;
                options || (options = {});
            }


            if (key !== undefined) {
                // save to server
                // Run validation.
                if (!this._validate(attrs, options)) return false;

                // set local
                if (typeof key === 'object' && !options.success && !options.error) {
                    this.set(attrs, options);
                } else {
                    this.set(attrs, val, options);
                }
            }

            this._callApi(options);
        },

        _callApi: function(options) {
             // customize param
            var api_param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, this.url, api_param, options, this.dev_opt);
        },

        _handleParam: function(opt_param) {
            var api_param;
            if (opt_param !== null) {
                // customize param
                if (typeof opt_param.param_attr !== 'undefined') {
                    api_param = {};
                    _.each(opt_param.param_attr, function(attr, prop) {
                        api_param[prop] = this.attributes[attr];
                    }.bind(this));
                } else {
                    if (typeof opt_param.param !== 'undefined') {
                        api_param = {};
                    } else {
                        api_param = this.attributes;
                    }
                }

                // combine static param
                if (typeof this.dev_opt.param !== 'undefined') {
                    _.extend(api_param, opt_param.param);
                }
            }
            return api_param;
        },

		_triggerKuroboxApi: function(model, method, param, options, dev_opt) {
            /*Kurobox.api(method, param, function(success, data, returnValue) {
                if (success) {
                    if (options.success) options.success(model, data, options);
                } else {
                    if (options.error) options.error(model ,data, options);
                }
            }, dev_opt);*/
            console.log(method, param)
            var skipGlobalError = false;
            if (options) {
                skipGlobalError = options.skipGlobalError || false;
            } else if (dev_opt) {
                skipGlobalError = dev_opt.skipGlobalError || false;
            }
            
            var api_opt = {
                url: dev_opt.url || undefined,
                httpMethod: dev_opt.method || undefined,
                app_id: dev_opt.app_id || undefined,
                redirectLogin: dev_opt.redirectLogin,
                skipGlobalError: skipGlobalError,
                query_param: dev_opt.query_param,
                success: function(resp) {
                    if (!_.isEmpty(options) && _.isFunction(options.success)){
                        options.success(model, resp, options);
                    }
                },
                error: function(resp) {
                        if (resp.ajax.textStatus !== 'abort') {
                            if (!_.isEmpty(options) && _.isFunction(options.error)) options.error(model, resp, options);
                        } else {
                            console.warn(method, 'call has being aborted');
                        }
                },
            }

            var id = gen_id();
            _xhr_store[id] = Kurobox.api(method, param, api_opt).complete(function() {
                delete _xhr_store[id];
            });
            return id;
        },

        destroy: function() {
            _.each(_xhr_store, function(xhr) {
                xhr.abort();
            })
        }
	}) 

	return clazz;
})
