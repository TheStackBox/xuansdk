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
    'backbone',
    'templates',
    'models/rule.device',
    'views/module.rule.device-setting.method-list',
    'views/module.rule.device-setting.opt-param-list',
    'views/module.rule.device-setting.req-param-list',
    'views/module.rule.device-setting.param-component',
    'views/module.rule.device-setting.method-enabler',
    'models/kbx.toggle'
], function ($, _, Backbone, JST, RuleDevice, MethodListView, OptionalParamListView, RequiredParamListView, ComponentView, MethodEnablerView, kbxToggle) {
    'use strict';
    var ModuleRuleDeviceSettingView = Backbone.View.extend({
        destroy: function() {
            this.rule_device = undefined;
            this.close();
            if (this.method_list !== undefined) {
                this.method_list.destroy();
            }

            if (this.param_list !== undefined) {
                this.param_list.destroy();
            }

            if (this.comp_view !== undefined) {
                this.comp_view.destroy();
            }

            if (this.method_enabler !== undefined) {
                this.method_enabler.destroy();
                this.method_enabler = undefined;
            }
        },

        close: function() {
            this.rule_device = undefined;
            this.options.user_device = undefined;
            this.clear();
        },

        clear: function() {
            if (this.method_list !== undefined) {
                this.method_list.close();
            }

            if (this.param_list !== undefined) {
                this.param_list.close();
            }

            if (this.comp_view !== undefined) {
                this.comp_view.close();
            }

            if (this.method_enabler !== undefined) {
                this.method_enabler.close();
            }
        },

        initialize: function() {
            this.method_list = new MethodListView({el: this.create_new_div({id: 'methods_container'})});
            this.method_list.on('cancel', this.on_method_list_cancelled, this);

            this.comp_view = new ComponentView({el: this.create_new_div({id: 'component_container'})});
            this.comp_view.on('done', this.on_component_view_value_confirmed, this);
            this.comp_view.on('reset', this.on_component_view_value_reset, this);
            this.comp_view.on('cancel', this.on_component_view_cancel, this);

            this.method_enabler = new MethodEnablerView({el: this.create_new_div({id: 'method_enabler_container'})})
            this.method_enabler.on('done', this.on_method_enabler_value_confirmed, this);
            this.method_enabler.on('cancel', this.on_method_enabler_cancel, this);
        },

        render: function() {
            this.$el.html(this.template());
        },

        start: function(did, section, nav, query) {

            if (this.rule_device === undefined) {
                // var for determine has user setting saved
                this._has_setting_changed = false;

                // add new device
                this.rule_device = new RuleDevice.model();
                this.rule_device.set('id', did);
                this.rule_device.set('section', section);
                this.rule_device.list_methods({
                    success: function() {
                        if (this.options.user_device === undefined) {
                            console.log('------ new setting')
                            // create new
                            this.options.user_device = new RuleDevice.model({
                                section: this.rule_device.get('section'),
                                description: this.rule_device.get('description'),
                                id: this.rule_device.get('id'),
                                name: this.rule_device.get('name'),
                                status: this.rule_device.get('status'),
                                icon: this.rule_device.get('icon'),
                            })
                        } else {
                            console.log('------ exisitng setting')
                            // clone
                            this.options.user_device = this.options.user_device.clone();
                        }

                        this.render_ui(query);
                    }.bind(this),
                    error: function() {
                        // let's go back
                        window.history.back();
                    }
                });

            } else {
                // edit the device setting
                this.render_ui(query);
            }
        },

        render_ui: function(query) {
            this.clear();

            if (query.pid !== undefined) {
                // render param ui component
                console.log('component view')
                this._handling_param(query);
                
            } else if (query.mid !== undefined) {
                // render arguments of method

                // determine how many arguments
                var ui_comp = this.rule_device.get('methods').get(query.mid).get('ui_components');
                var req_param_len = ui_comp.get_total_required_parameter();
                var opt_param_len = ui_comp.get_total_optional_parameter();
                if (this.param_list !== undefined) {
                    // assume param list is available
                    
                    this.param_list.show();
                } else {
                    // param list first init
                    if (ui_comp.length === 0) {
                        // redirect to method enabler
                        window.location.replace(window.location +'&pid='+MethodEnablerView.ID);
                    } else if (req_param_len === 0) {
                        // assume there is optional param
                        this.param_list = new OptionalParamListView({el: this.create_new_div({id: 'param_container'})});
                    } else {
                        // assume there's required param
                        if (ui_comp.length === 1) {
                            // there's only one param

                            // redirect to arg display
                            window.location.replace(window.location +'&pid='+ui_comp.models[0].id);
                            return;
                        } else {
                            // there's multiple param
                            this.param_list = new RequiredParamListView({el: this.create_new_div({id: 'param_container'})});
                        }
                    }
                    this.param_list.render(query.mid, this.rule_device, this.options.user_device);
                    this.param_list.on('done', this.on_param_modified, this);
                    this.param_list.on('reset', this.on_param_reset, this)
                }

            } else if (query.did !== undefined) {
                // destroy param list
                if (this.param_list !== undefined) {
                    this.param_list.destroy();
                    this.param_list = undefined
                }

                // clear out cloned method
                this._remove_cloned_method();

                // render methods
                this.method_list.render(this.rule_device, this.options.user_device);
            }
        },

        _handling_param: function(query) {
            if (query.pid === MethodEnablerView.ID) {
                // method enabler ---------
                var activation_model;
                if (this.param_list !== undefined) {
                    // from param list
                    activation_model = this.param_list.activation_model;
                } else {
                    // from method
                    activation_model = this._prepare_activation_model(
                        this.options.user_device.get('methods').get(query.mid) !== undefined
                    )
                }
                this.method_enabler.render(query.mid, this.rule_device, this.options.user_device.get('methods'), activation_model);
            } else {
                // parameter component ----
                if (this.param_list !== undefined) {
                    // from param list
                    this.comp_view.render(query.mid, query.pid, this.rule_device, this.param_list.user_params.get(query.pid));
                } else {
                    // direct from method list
                    // mean only have 1 param in the device
                    var param;
                    if (this.options.user_device.get('methods').get(query.mid) === undefined) {
                        // user setting is NOT available
                        this._clone_method(query.mid);
                    }
                    param = this.options.user_device.get('methods').get(query.mid).get('params').get(query.pid);

                    this.comp_view.render(query.mid, query.pid, this.rule_device, param, this.rule_device.get('methods').get(query.mid))
                }
            }
        },

        _clone_method: function(method_id) {
            // cloned from device
            this.options.user_device.get('methods').add(this.rule_device.get('methods').get(method_id).clone());

            this._cloned_method_id = method_id;
        },

        _remove_cloned_method: function() {
            if (this._cloned_method_id !== undefined) {
                this._remove_user_method(this._cloned_method_id)
                this._cloned_method_id = undefined;
            }
        },

        _prepare_activation_model: function(enabled) {
            return new kbxToggle({
                label: 'Enable this method',
                name: MethodEnablerView.ID,
                value: enabled
            })
        },

        create_new_div: function(prop, target) {
            return $('<div>', prop || {}).appendTo(target || this.$el);
        },

        on_component_view_value_confirmed: function(method_id, param_id) {
            // apply value change
            if (this.param_list !== undefined) {
                // update param list
                this.param_list.update(param_id);
            } else {
                // update method view
                this._cloned_method_id = undefined;
                this.method_list.update(method_id);

                // update flag
                this._has_setting_changed = true;
            }

            window.history.back();
        },

        on_component_view_value_reset: function(method_id, param_id) {
            // reset value change
            if (this.param_list !== undefined) {
                // update param list
                this.param_list.update(param_id);
            } else {
                // update method view
                // remove newly created methods
                this._remove_user_method(method_id)
                this._cloned_method_id = undefined;

                this.method_list.update(method_id);

                // update flag
                this._has_setting_changed = true;
            }

            window.history.back();
        },

        on_component_view_cancel: function(method_id, param_id) {
            window.history.back();
        },

        _remove_user_method: function(method_id) {
            var model = this.options.user_device.get('methods').get(method_id);
            this.options.user_device.get('methods').remove(model);
        },

        on_param_modified: function(params, method_id) {
            // update user data
            if (!this.options.user_device.get('methods').get(method_id)) {
                var clone_method = this.rule_device.get('methods').get(method_id).clone();
                this.options.user_device.get('methods').add(clone_method);
            }

            this.options.user_device.get('methods').get(method_id).set('params', params)

            // update method list
            this.method_list.update(method_id);

            // update flag
            this._has_setting_changed = true;

            this.param_list.destroy();
            this.param_list = undefined

            window.history.back();
        },

        on_param_reset: function(method_id) {
            // update method list
            this.method_list.update(method_id);

            // update flag
            this._has_setting_changed = true;

            this.param_list.destroy();
            this.param_list = undefined
            
            window.history.back();
        },

        on_method_enabler_value_confirmed: function(method_id, enabled) {
            if (this.param_list !== undefined) {
                // optional param list
                this.param_list.update_method(enabled);
            } else {
                var m;
                if (enabled) {
                    // add method to user setting
                    if (this.options.user_device.get('methods').get(method_id) === undefined) {
                        m = this.rule_device.get('methods').get(method_id).clone();
                        this.options.user_device.get('methods').add(m);
                    }
                } else {
                    // remove method from user setting
                    m = this.options.user_device.get('methods').get(method_id);
                    if (m !== undefined) {
                        this.options.user_device.get('methods').remove(m);
                    }
                }
                // method list, maybe?
                this.method_list.update(method_id);
            }

            window.history.back();
        },

        on_method_enabler_cancel: function(method_id) {
            window.history.back();
        },

        on_method_list_cancelled: function() {
            this.trigger('done', this.options.user_device);
        }
    });

    return ModuleRuleDeviceSettingView;
});
