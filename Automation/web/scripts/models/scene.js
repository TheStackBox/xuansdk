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
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
    'common/rule/models/rule.device.method',
    'models/rule.device',
    'common/rule/models/rule.device.param',
    'models/scene.action.delay',
], function (_, KuroboxModel, KuroboxCollection, RuleDeviceMethod, RuleDevice, DeviceMethodParams, SceneDelay) {
    'use strict';

    var _retry_method_api = function(that, serId, methodIdx, options) {
        that.url = 'retry_scene_execution_result_item';
        that.dev_opt = {
            param: {
                serId: serId,
                seriIndex: methodIdx
            }
        }
        that._callApi(options)
    }

    var LogResult = KuroboxModel.extend({
        defaults: {
            status: 'error',
            error: ''
        },
    })

    var NonIDBasedRuleDeviceMethod = RuleDeviceMethod.model.extend({
        idAttribute: undefined,
        retry: function(options) {
            _retry_method_api(this, this.get('serId'), this.index, options)
        }
    })

    var ActionCollection = KuroboxCollection.extend({
        model: NonIDBasedRuleDeviceMethod,
        toObject: function() {
            var o = [];
            this.each(function(action) {
                o.push(action.toObject());
            })

            return o;
        }
    })

    var SceneModel = KuroboxModel.extend({
        fn: KuroboxModel.prototype,
    	defaults: {
            execution: new ActionCollection(),
            passcode_protected: false,
            icon: '&#xc600'
        },
        initialize: function() {
            if (arguments.length == 0) {
                this.set('execution', new ActionCollection());
            }
        },
        summary_parse: function(data) {
            return {
                id: data.sceneId,
                name: data.sceneName,
                icon: data.sceneIcon,
                passcode_protected: data.sceneProtected
            }
        },
        detail_parse: function(data) {
            var pdata = data.response;
            console.log('parse detail', data);
            var o = {
                id: pdata.sceneId,
                passcode_protected: pdata.sceneProtected,
                name: pdata.sceneName,
                icon: pdata.sceneIcon,
            }
            o.execution = new ActionCollection();

            var methodModel;
            var deviceModel;
            _.each(pdata.execution, function(item, index) {
                deviceModel = new RuleDevice.model({response: {group: item, data: []}}, {parse: true});

                switch (item.kbxMethodId) {
                    case -291:
                    methodModel = new SceneDelay(item, {parse: true});
                    break;

                    default:
                    methodModel = new o.execution.model(item, {parse: true});
                    
                    // remove methods property
                    deviceModel.unset('methods');

                    // set deviceModel to methodModel (which is the action!)
                    methodModel.set('device', deviceModel);
                    break;
                }

                methodModel.index = index;
                o.execution.add(methodModel);
            })
            return o;
        },
        log_parse: function(data) {
            var o = this.detail_parse(data);
            this.total_execution_queued = 0;
            this.total_execution_failed = 0;
            o.execution.each(function(action, index) {

                // parse log result
                action.set('serId', this.get('serId'))
                action.set('result', new LogResult({
                    status: data.response.execution[index].seriStatus,
                    error: data.response.execution[index].seriError
                }))

                switch (action.get('result').get('status')) {
                    case 'busy':
                    this.total_execution_queued += 1;
                    break;

                    case 'error':
                    this.total_execution_failed += 1;
                    break;
                }
            }.bind(this))

            return o;
        },
        parse: function(data) {
            return this.summary_parse(data);
        },

        load_detail: function(passcode, options) {
            this.url = 'get_scene';
            this.parse = this.detail_parse.bind(this);

            var param = {};
            param.sceneId = this.id;
            if (passcode != undefined) {
                param.passcode = passcode
            }

            this.dev_opt = {
                param: param,
            }
            this.fn.fetch.call(this, options)
        },

        fetch_log: function(serId, options) {
            this.url = 'get_scene_execution_result';
            this.set('serId', serId)
            this.parse = this.log_parse.bind(this);

            this.dev_opt = {
                // url: 'json/example.feedback.json',
                param: {
                    serId: serId
                }
            }
            this.fn.fetch.call(this, options);
        },

        save: function(options) {
            // aggreate
            this.url = 'set_scene';
            var param = {};

            if (this.attributes.id != undefined) param.sceneId = this.attributes.id;
            param.sceneIcon = this.attributes.icon;
            param.execution = JSON.stringify(this.attributes.execution.toObject());
            param.sceneProtected = this.attributes.passcode_protected;
            param.sceneName = this.attributes.name;
            if (this.attributes.passcode != undefined) param.passcode = this.attributes.passcode;

            this.dev_opt = {
                param: param,
                method: 'POST',
            }
            
            this.fn.save.call(this, options);
        },
        remove: function(passcode, options) {
            options = (options) ? options : {};

            this.url = 'delete_scene';
            var param = {sceneId: this.get('id')};
            if (passcode) param.passcode = passcode;

            this.dev_opt = {
                method: 'GET',
                param: param
            }

            if (options.silent) {
                var psuccess = options.sucess || function() {}
                var success = function(model, resp, options) {
                    this.trigger('destroy');
                    psuccess(model, resp, options);
                }.bind(this)

                options.success = success;
            }

            var param = this._handleParam(this.dev_opt);
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        },
        execute: function(feedbackUrl, options) {
            this.url = 'execute_scene';
            this.dev_opt = {
                param: {
                    sceneId: this.id,
                    serUrl: feedbackUrl,
                }
            }
            this._callApi(options)
        },
        retry_all_failed_methods: function(options) {
            _retry_method_api(this, this.get('serId'), undefined, options);
        },
        invalidate_execution_failed_count: function() {
            this.total_execution_failed = 0;
            this.get('execution').each(function(action) {
                if (action.get('result').get('status') == 'error') {
                    this.total_execution_failed ++;
                }
            }.bind(this))
        }
    });

    var SceneCollection = KuroboxCollection.extend({
        fn: KuroboxCollection.prototype,
    	model: SceneModel,
    	fetch: function(type, id, options) {
    		this.url = 'list_scenes';
    		this.dev_opt = {
                param: {
                    // by: type,
                    // byId: id
                }
    		}
    		this.fn.fetch.call(this, options)
    	},

    	parse: function(data) {
    		var o = [];
    		_.each(data.response.data, function(item) {
    			o.push(new this.model(item, {parse:true}))
    		}.bind(this));
    		return o;
    	}
    }, {
        model: SceneModel,
        actionCollection: ActionCollection
    })

    return SceneCollection;
});
