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
    'views/module.rule-creator',
    'views/module.rule-list',
    'bootstrap'

], function ($, _, Backbone, JST, RuleCreator, RuleListModule) {
    'use strict';

    /*var NAV_HOME = 'nav-circle-home nav-icon-home';
    var ADD_RULE = 'nav-circle-add nav-icon-add';
    var EDIT_RULE = 'nav-circle-edit nav-icon-edit';
    var EXIT_EDIT_RULE = 'nav-circle-done nav-icon-done';
    var SAVE_RULE = 'nav-circle-done nav-icon-done';
    var BACK = 'nav-icon-back';*/

    var DeviceView = Backbone.View.extend({
        template: JST['app/scripts/templates/device.ejs'],
        events: {
            // modal click event
            'click #confirm-dark': 'on_everything_cancel',
            'click #modal-ok-btn': 'on_prompt_confirm',
            'click #modal-cancel-btn': 'on_prompt_cancel'
        },
        render: function() {
            $(this.el).html(this.template());
            this.trigger('page.rendered', this);
            this.init_nav_bar();
        	return this;
        },

        destroy: function() {
            if (this.content_module !== undefined) {
                this.content_module.destroy();
                this.content_module = undefined;
            }
        },
 
        navigate: function(action, uid, query) {
            console.log('rule navigate', action, uid, query);
            this.uid = uid;
            var nav = {};

            // show navigation first
            this.options.nav.show();

            if (_.isEmpty(this.content_module)) {
                this.content_module = new RuleListModule();
                this.content_module.render();
                this.content_module.on('list_retrieved', function() {
                    this.trigger('idle');
                }, this);
                this.content_module.on('execute', function(rule_config) {
                    
                    window.location = '#/rule/execute/'+rule_config.get('id');
                }.bind(this))
                this.content_module.on('edit', function(rule_config) {
                    window.location = '#/rule/edit/'+rule_config.get('id');
                })
                $('.page-content').append(this.content_module.el);
            }
            
            switch (action) {
                case 'add':
                case 'edit':
                    // hide navigation
                    this.options.nav.hide();

                    this.content_module.hide();
                    
                    // navigation configuration is set inside RuleCreator class
                    nav = undefined;

                    // initialise module
                    if (this.rule_creator === undefined) {
                        var render_creator = function() {
                            this.rule_creator.render();
                            $('.page-content').append(this.rule_creator.el);
                        }.bind(this);

                        this.rule_creator = new RuleCreator({nav: this.options.nav, parent: this, mode: action});
                        this.rule_creator.on('busy', function() {
                            this.trigger('page.busy');
                        }.bind(this));
                        this.rule_creator.on('idle', function() {
                            this.trigger('page.idle');
                        }.bind(this));
                        this.rule_creator.on('inited', function() {
                            this.rule_creator.navigate(uid, query);
                        }.bind(this));
                        this.rule_creator.on('saved', function() {
                            // refresh list
                            this.content_module.destroy();

                            window.location.replace('#/rule');
                        }.bind(this))

                        if (uid !== undefined) {
                            console.log('edit rule', uid);
                            this.rule_creator.create_rule_config();
                            this.rule_creator.rule_config.set('id', uid);
                            this.rule_creator.rule_config.fetch({
                                success: function() {
                                    render_creator();
                                }.bind(this),
                                error: function() {
                                    console.error('Unable to get detailed rule', uid);
                                }
                            })
                        } else {
                           render_creator();
                        }
                    } else {
                        this.rule_creator.navigate(uid, query)
                    }
                break;
                case 'options':
                    // show content list
                    console.log('this.content_module.is_empty()', this.content_module.is_empty())
                    if (this.content_module.is_empty()) {
                        this.content_module.retrieve_rule();
                    }
                    this.content_module.show();
                    this.content_module.trigger_action(action, uid);

                    if (this.rule_creator !== undefined && this.rule_creator.$el.is(':visible')) {
                        console.log('hide rule creator')
                        this.rule_creator.destroy();
                        this.rule_creator = undefined;
                    }

                    console.log('options');
                      // initialise header
                    nav.left = ['NAV_HOME'];
                    nav.right = ['ADD_RULE'];
                    nav.title = 'automation';
                    nav.callback = this.on_rule_list_nav_updated.bind(this);
                    this.prompt_message('hide');
                    break;
                case 'remove':
                case 'execute':
                case 'disable':
                case 'enable':
                    if (this.content_module.collection !== undefined) {
                        this.content_module.hide_options();

                        nav.left = ['NAV_HOME'];
                        nav.right = ['ADD_RULE'];
                        nav.title = 'automation';
                        nav.callback = this.on_rule_list_nav_updated.bind(this);

                        var o = {
                            confirm_callback: function() {
                                this.prompt_message('hide');
                                this.content_module.trigger_action(action, uid);
                                window.location.replace('#/rule');
                            }.bind(this),
                            cancel_callback: function() {
                                window.location = '#/rule';
                            }
                        };
                    
                        switch (action) {
                            case 'remove':
                            o.title = 'remove_rule';
                            o.message = 'msg_confirm_remove_rule';
                            o.confirm_label = 'btn_remove';
                            break;

                            case 'execute':
                            o.title = 'execute_rule';
                            o.message = 'msg_confirm_execute_rule'
                            o.confirm_label = 'btn_execute';
                            break;

                            case 'disable':
                            o.title = 'disable_rule';
                            o.message = 'msg_confirm_disable_rule'
                            o.confirm_label = 'disable';
                            break;

                            case 'enable':
                            o.title = 'enable_rule';
                            o.message = 'msg_confirm_enable_rule'
                            o.confirm_label = 'enable';
                            break;
                        }
                        this.prompt_message(o);
                    } else {
                        window.location = '#/rule';
                    }
                    break;
                break;
                default:
                     // initialise header
                    nav.left = ['NAV_HOME'];

                    // remove rule creator
                    if (this.rule_creator !== undefined && this.rule_creator.$el.is(':visible')) {
                        console.log('hide rule creator')
                        this.rule_creator.destroy();
                        this.rule_creator = undefined;
                    }
   
                    nav.right = ['ADD_RULE'];
                    nav.title = 'automation';
                    nav.callback = this.on_rule_list_nav_updated.bind(this);

                    console.log('show content')
                    this.content_module.show();

                    this.prompt_message('hide');
                    this.content_module.hide_options();

                    if (this.content_module.is_empty()) {
                        this.content_module.retrieve_rule();
                    }
                    this.content_module.show();

                    // remove rule editor
                    if (this.rule_creator !== undefined) {
                        this.rule_creator.destroy();
                        this.rule_creator = undefined;
                    }
                break;
            };

            if (nav !== undefined) {
                // for add action will be update by its module
                this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
                this.options.nav.update_title(nav.title);
            }
        },

        on_rule_list_nav_updated: function(item, nav) {
            console.log('nav cb', item)

            switch(item) {
                case nav.NAV_HOME:
                    window.location = '/system/myapp';
                break;
                case 'nav-circle-add nav-icon-add':
                    // go to add rule
                    window.location = '#/rule/add';
                break;
            }
        },

        set_param: function(param) {
        },

        on_nav_update: function(item) {
           window.history.back();
        },

        prompt_message: function() {
            var action = 'show';
            var conf = {
                confirm_label: 'Ok',
                cancel_label: 'Cancel',
                confirm_callback: undefined,
                cancel_callback: undefined
            };

            if (typeof arguments[0] === 'string') {
                action = arguments[0];
            } else {
                _.extend(conf, arguments[0]);

                // fill in the blank
                $('#myModalLabel').text(conf.title || '');
                $('#modal-body').text(conf.message || 'Are you sure?');
                $('#modal-cancel-btn').text(conf.cancel_label);
                $('#modal-ok-btn').text(conf.confirm_label);
            }

            // execute action
            $('#prompt-modal').data('confirm_cb', conf.confirm_callback);
            $('#prompt-modal').data('cancel_cb', conf.cancel_callback);
            // $('#prompt-modal').modal(action);

            if (action === 'show') {
                console.log('show confirm dark!!!!!!!!!!!!!');
                $('#confirm-dark').show();
                $('#prompt-modal').show();
            } else {
                $('#confirm-dark').hide();
                $('#prompt-modal').hide();

            }            
        },

        on_prompt_confirm:function () {
            var func = $('#prompt-modal').data('confirm_cb');
            if (func !== undefined) func();
        },

        on_prompt_cancel: function() {
            console.log(' on_prompt_cancel');
            var func = $('#prompt-modal').data('cancel_cb');
            if (func !== undefined) func();
        },

        on_prompt_close: function() {

        },

        on_info_module_closed: function() {

        },

        validateListModule: function(action) {
        },

        on_new_device_paired: function(device_model) {
        },

        on_new_device_pairing: function() {
        },

        on_new_device_pair_failed: function() {
        },

        load_control_panel: function(uid) {

        },

        unload_control_panel: function() {

        },

        on_everything_cancel: function() {
            //location.replace('#/rule');
           this.on_prompt_cancel();
        },

        init_nav_bar: function(){
            console.log("init_nav_bar")
            var nav = {};
            nav.right = ['ADD_RULE'];
            this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
        }

    });

    return DeviceView;
});
