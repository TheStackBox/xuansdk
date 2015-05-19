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
    'backbone',
    'templates',
    'views/module.rule.device_explorer',
    'views/module.scene.device-setting',
    'views/scene.editor.action-list',
    'views/scene.editor.action-list-mover',
    'views/scene.editor.delay-editor',
    'views/scene.editor.icon-selector',
    'toggleswitch',
], function ($, _, Backbone, JST, DeviceExplorer, DeviceSetting, SceneActionList, SceneActionMover, SceneDelayEditor, SceneIconSelector) {
    'use strict';

    // constant for service redirect
    var SERVICES = [
        'service_mail',
        'service-twitter',
        'service-weather'
    ]

    var current_location = function() {
        return window.location.hash.split('?')[0];
    }

    // model: 'models/scene.js'
    var SceneEditorView = Backbone.View.extend({
        className: 'scene-editor-page',
        template: JST['app/scripts/templates/scene.editor.ejs'],
        header_content: JST['app/scripts/templates/scene.editor.header.ejs'],
        header_template: JST['app/scripts/common/templates/grey-header.ejs'],
        add_menu_template: JST['app/scripts/templates/scene.editor.add-menu.ejs'],
        prompt_pop_dialog_msg: JST['app/scripts/common/templates/prompt.pop.ejs'],
        item_option_menu: JST['app/scripts/templates/scene.editor.option-menu.ejs'],
        events: {
            'click .header #nav-back-btn': 'on_user_return_back',
            'click #scene-done-btn': 'on_user_save_scene',
            'click .scene-icon-edit': 'on_user_change_icon',
            'input #name_txt': 'on_user_out_of_focus_name_txtf',
        },

        initialize: function(options) {
            this.model = options.model;
        },

        destroy: function() {

            delete this.model;
            this.model = undefined;

            this.close_device_explorer();
            this.close_device_setting();
            this.close_action_mover();
            this.close_delay();
            this.action_list.destroy();

            this.$el.empty();
            this.$el.remove();
        },

        render: function() {
            this.$el.html(this.template(this.model));

            // initialise device setting first

            // password lock handler
            this.$('#lock-toggle').toggleSwitch();
        },

        navigate: function(query) {
            console.log('----- nav', query)
            // @NOTE: has being called at scene
            // Shell.hide_pop_message();

            this.$('.body').show();
            this.$('.header').show();

            var set_default_header = function() {
                this.update_header(
                    this.header_content({
                        title: (this.model.id == undefined) ? 'new_scene' : 'edit_scene',
                        desc: 'scene_editor_description',
                    })
                )
            }.bind(this)
            console.log('query.action', query)

            if (query != undefined) {
                switch (query.action) {
                    case 'add':
                    set_default_header();

                    this.close_device_explorer();
                    this.close_device_setting();
                    this.close_delay();

                    this.trigger_add_menu();
                    break;

                    case 'add-group':
                    // hide editor
                    this.$('.body').hide();
                    this.close_device_setting();

                    this.manage_device_explorer(query);
                    break;

                    case 'edit-group':
                    this.$('.body').hide();
                    this.$('.header').hide();
                    this.close_device_explorer();

                    this.manage_device_setting(query);
                    break;

                    case 'method-option':
                    if (this.model.get('execution').length > 0) {
                        // create header
                        set_default_header();

                        this.$('.body').show();
                        this.$('.header').show();

                        // close components
                        this.close_device_explorer();
                        this.close_action_mover();

                        this.prompt_method_option(query);
                    } else {
                        // empty action list
                        window.location = current_location();
                    }
                    break;

                    case 'remove-method':
                    if (query.idx != undefined && 
                        this.model.get('execution').length > 0 && 
                        this.model.get('execution').at(query.idx) != undefined) {
                        this.on_user_remove_action(query.idx);
                    } else {
                        // empty action list
                        window.location = current_location();
                    }
                    break;

                    case 'move':
                    if (this.model.get('execution').length > 0) {
                        // header
                        this.update_header(
                            this.header_content({
                                title: 'move_scene_item',
                            })
                        )

                        // begin move device
                        this.$('.body').hide();
                        this.manage_action_mover(query);
                    } else {
                        // empty action list
                        window.location = current_location();
                    }
                    break;

                    case 'delay':
                    // header
                    if (query.at == undefined) {
                        this.update_header(
                            this.header_content({
                                title: 'add_delay',
                                desc: 'add_delay_desc'
                            })
                        )
                    } else {
                        this.update_header(
                            this.header_content({
                                title: 'edit_delay',
                                desc: 'add_delay_desc'
                            })
                        )
                    }

                    this.$('.body').hide();
                    this.manage_delay(query);
                    break;

                    case 'change-icon':
                    // create header
                    set_default_header();

                    this.manage_icon_selector(query);
                    break;

                    case 'cancel':
                    window.location = current_location();
                    break;

                    default:
                    console.warn('Unknown action', query.action);
                    break;
                }
            } else {
                // navigating as summary page
                // create header
                set_default_header();

                // close everything 
                this.close_device_explorer();
                this.close_device_setting();
                this.close_action_mover();
                this.close_delay();
                this.close_icon_selector();

                // invalidate action list
                this.invalidate_actions_list();

                // validate editor form
                this.invalidate_scene_data();

                console.log('actions summary', this.model.get('execution'))
            }
        },

        trigger_add_menu: function() {
            Shell.show_pop_message(
                this.add_menu_template({
                    data: new Backbone.Collection([
                        {id: 'add-group', label: 'add_actions', desc: 'add_actions_desc'},
                        {id: 'delay', label: 'add_delay', desc: 'add_delay_desc'},
                        {id: 'cancel', label: 'btn_cancel', desc: ''},
                    ]),
                })
                , {
                    'click .pop-menu-item': function(e) {
                        window.location = current_location() +'?action='+$(e.currentTarget).data('id');
                    }.bind(this)
                },
                function() {
                    window.history.back();
                }.bind(this)
            )
        },

        manage_device_explorer: function(query) {
            var defer = function() {
                // navigate content
                var opt = {}
                var header_content_config;
                if (query.filter != undefined && query.lId != undefined || query.gId != undefined) {
                    // list based on filter and filter id
                    opt.filter = [query.filter];
                    opt.locationId = query.lId;
                    opt.parentGroupId = query.gId;
                    header_content_config = {
                        title: 'select_a_device',
                        // desc: 'select_a_device_desc'
                    }
                } else {
                    // list basic
                    opt.filter = ['locations', 'services'];
                    header_content_config = {
                        title: 'select_location',
                        // desc: 'control_a_device_desc'
                    }
                }
                this.device_explorer.navigate(opt);

                // update header
                this.update_header(this.header_content(header_content_config))
            }.bind(this);

            if (this.device_explorer === undefined) {
                // initiate device explorer
                this.device_explorer = new DeviceExplorer();
                this.device_explorer.on('select', this.on_user_select_item_in_device_explorer, this)
                this.$el.append(this.device_explorer.$el);
                this.device_explorer.render();

                defer();
            } else {
                defer();
            }
        },

        close_device_explorer: function() {
            if (this.device_explorer != undefined) {
                this.device_explorer.destroy();
                this.device_explorer = undefined;
            }
        },

        init_device_setting: function() {
            if (this.device_setting === undefined) {
                this.device_setting = new DeviceSetting({id:'device-setting'});
                this.device_setting.on('done', this.on_device_setting_completed, this);
                this.device_setting.on('cancel', this.on_user_close_device_setting, this);
                this.$el.append(this.device_setting.$el);

                // DeviceSetting doesn't render,
                // Chuck Norris is at the back of the script.
            }
        },

        manage_device_setting: function(query) {
            this.init_device_setting();

            this.device_setting.start(query.did, 'then', null, query)
        },

        close_device_setting: function() {
            if (this.device_setting != undefined) {
                this.device_setting.destroy();
                this.device_setting = undefined;

                // remove the container
                this.$('#device-setting').remove();
            }
        },

        prompt_method_option: function(query) {
            console.log('--- prompt method option', query)
            // defer function to close option menu
            var close_option_menu = function() {
                window.location = current_location();
            }.bind(this)

            // show options
            Shell.show_pop_message(this.item_option_menu({idx: query.idx}), {
                'click .option': this.on_user_select_action_item_option.bind(this),
                'click .icon-close': close_option_menu
            },
            close_option_menu)
        },

        update_header: function(html) {
            console.log('-- header html', html)
            this.$('.header').html(this.header_template({
                content: html
            }));
        },

        remove_id_attribute: function(model) {
            delete model.id;
            delete model.idAttribute;
        },

        restore_id_attribute: function(model, idAttr) {
            model.id = model.get(idAttr);
            model.idAttribute = idAttr;
        },

        invalidate_actions_list: function() {
            if (this.action_list == undefined) {
                this.action_list = new SceneActionList();
                this.action_list.render();
                this.action_list.on('option', this.on_user_select_action_item, this);
            }

            // update data view
            this.action_list.update(this.model.get('execution'));
            this.$('.actions-summary-list').html(this.action_list.$el);
        },

        invalidate_icon: function() {
            this.$('.body .icon-holder').attr('data-icon',this.model.get('icon'));
        },

        manage_action_mover: function(query) {
            if (this.mover == undefined) {
                this.mover = new SceneActionMover();
                console.log('--- test mover constructor', this.model.get('execution'))
                this.mover.model = this.model.get('execution').constructor,
                this.mover.on('done', this.on_user_confirm_item_position, this);
                this.mover.render();
                this.$el.append(this.mover.$el);

                console.log('..... test mover constructor', this.mover.model)

                _.defer(function() {

                    this.mover.invalidate(this.model.get('execution'));
                }.bind(this))
            }
        },

        close_action_mover: function() {
            if (this.mover != undefined) {
                this.mover.destroy();
                this.mover = undefined;
            }
        },

        manage_delay: function(query) {
            if (this.delay_editor == undefined) {
                this.delay_editor = new SceneDelayEditor();
                this.delay_editor.on('done', this.on_user_confirm_delay_value, this);
                this.delay_editor.render();

                this.$el.append(this.delay_editor.$el);
            }

            var delay_action;
            if (query.at != undefined) {
                delay_action = this.model.get('execution').at(query.at);
                this.delay_editor._action_idx = query.at;
            }
            this.delay_editor.invalidate(delay_action)
        },

        close_delay: function() {
            if (this.delay_editor != undefined) {
                this.delay_editor.destroy();
                this.delay_editor = undefined;
                console.warn('delay editor has being removed')
            }
        },

        manage_icon_selector: function(query) {
            if (this.icon_selector == undefined) {
                this.icon_selector = new SceneIconSelector({
                    source: 'json/scene-icon-list.json', 
                    parser: function(data) {
                        return data.icons;
                    }
                });
                this.icon_selector.on('select', this.on_user_changed_icon, this);
                this.icon_selector.on('close', this.on_user_close_icon_selector, this);
                this.icon_selector.on('init', function() {
                    // show content
                    var $content = Shell.show_pop_message(this.icon_selector.$el, undefined, this.on_user_close_icon_selector.bind(this));
                    $content.show();
                }.bind(this));
                this.icon_selector.render();
            }
        },

        close_icon_selector: function() {
            if (this.icon_selector != undefined) {
                this.icon_selector.destroy();
                this.icon_selector = undefined;
            }
        },

        // events
        on_user_select_action_item: function(idx, model, e) {
            console.log('--- arg', idx, model)
            if (idx === 'add') {
                // add new methods
                window.location = current_location() + '?action=add'; 
            } else if (model != undefined) {

                window.location = current_location() +'?action=method-option&idx='+idx;
            }
        },

        on_user_select_item_in_device_explorer: function(model, e) {
            console.log('user select item in device explorer', model)

            var acknowledged_action = function() {
                Shell.hide_pop_message();
                this.delegateEvents();
            }.bind(this)

            // validate if model has being deleted on server side
            if (model.get('deleted')) {
                var $prompt_content = Shell.show_pop_message(this.prompt_pop_dialog_msg({
                    title: '',
                    message: 'msg_rule_device_explorer_device_delete_access_denied',
                    ok_btn_label: 'btn_ok',
                    cancel_btn_label: ''
                }), {
                    'click #modal-ok-btn': acknowledged_action
                }, acknowledged_action)

                return;
            }

            // validate if model is required setup
            if (typeof model.get('extra_info').kbxService !== 'undefined' && model.get('extra_info').kbxService.isRequireSetup === true) {
                this.undelegateEvents();

                if (window.location.host.indexOf('tunnel.thexuan.com') === -1) {
                    // is in local area
                    var $prompt_content = Shell.show_pop_message(this.prompt_pop_dialog_msg({
                        title: '',
                        message: 'error_service_setup_required',
                        ok_btn_label: 'btn_ok',
                        cancel_btn_label: 'btn_cancel'
                    }), {
                        'click #modal-ok-btn': function() {
                            window.location = '/system/admin/#setup/'+SERVICES[model.get('extra_info').kbxService.serviceId];
                        }.bind(this),
                        'click #modal-ok-btn': acknowledged_action
                    }, acknowledged_action)

                } else {
                    // is on internet

                    var $prompt_content = Shell.show_pop_message(this.prompt_pop_dialog_msg({
                        title: '',
                        message: 'error_service_setup_remote_access_denied',
                        ok_btn_label: 'btn_ok',
                        cancel_btn_label: ''
                    }), {
                        'click #modal-ok-btn': acknowledged_action
                    }, acknowledged_action)

                    // ask cancel button to fuck off
                    $prompt_content.find('#modal-cancel-btn').hide();
                }
                return;
            }

            // otherwise
            if (model.get('has_child') == true) {
                var locStr = current_location() + '?action=add-group&';
                    locStr += 'gId='+model.id;

                window.location = locStr;
            } else {
                // navigate to device setting
                window.location = current_location() + '?action=edit-group&did='+model.id;
            }
        },

        on_user_return_back: function() {
            if (window.location.hash == current_location()) {
                this.trigger('close');
            } else {
                window.history.back();
            }
        },

        on_device_setting_completed: function(config) {
            // register to current model

            // clone device setting, with methods removed
            var device = config.clone();
            device.unset('methods');

            config.get('methods').each(function(method) {
                // on each actions (method), inject device for ref later

                // remove id attributes
                this.remove_id_attribute(method);

                // register to actions collection
                method.set('device', device);
                this.model.get('execution').add(method);
            }.bind(this))

            console.log('--- actions', this.model.get('execution'))

            window.location = current_location();
        },

        on_user_close_device_setting: function() {
            window.history.back();
        },

        on_user_modify_action: function(device_setting) {
            // @NOTE: new device setting generated by device setting
            
            // grab the specified method
            var id = this._config_method.get('id');
            var newConfig = device_setting.get('methods').get(id).clone();
            this.remove_id_attribute(newConfig);

            // generate device setting
            var device = device_setting.clone();
            device.unset('methods');
            newConfig.set('device', device);

            // reset data
            var idx = this.model.get('execution').indexOf(this._config_method);
            this.model.get('execution').remove(this._config_method);
            this.model.get('execution').add(newConfig, {at: idx});

            this._config_method = undefined;
            delete this._config_method;

            console.log('validate model', idx, this.model.get('execution').at(idx))

            // back to editor
            window.location = current_location();
        },

        on_user_remove_action: function(index) {
            // prompt for verification
            var pop_conf = {};
                pop_conf.ok_btn_label = 'btn_remove';
                pop_conf.cancel_btn_label = 'btn_cancel';
                pop_conf.title = 'msg_scene_remove_method';
                pop_conf.message = 'msg_scene_remove_method_msg';
            
            var closePrompt = function() {
                window.location = current_location();
            }.bind(this);

            var $pop = Shell.$('#shell-pop-content');
            console.log('$pop', $pop, $pop.prop('style'), $pop.is(':animated'), $pop.is(':hidden'))

            if ($pop.is(':animated')) {
                // halt animation immediately
                $pop.finish().show();
            }

            $pop = Shell.show_pop_message(this.prompt_pop_dialog_msg(pop_conf), {
                'click #modal-ok-btn': function() {
                    // user confirm to delete
                    var target = this.model.get('execution').at(index);
                    this.model.get('execution').remove(target)

                    // back to editor
                    window.location = current_location();
                }.bind(this),
                'click #modal-cancel-btn': closePrompt
            }, closePrompt);
        },

        on_user_select_action_item_option: function(e) {
            var $e = $(e.currentTarget);
            var idx = $e.data('idx');

            var remove_method = function() {
                window.location = current_location() + '?action=remove-method&idx='+idx;
            }

            switch ($e.data('action')) {
                case 'edit':
                // create dummy device setting, pass to device setting
                var model = this.model.get('execution').at(idx);

                if (model.get('id') == -291) {
                    // delay device
                    window.location = current_location() + '?action=delay&at='+idx;
                } else {
                    // normal device
                    // restore idAttribute
                    var method_model = model.clone();
                    this.restore_id_attribute(method_model, 'id');

                    var dump = model.get('device').clone();
                    dump.get('methods').add(method_model);
                    this._config_method = model;

                    // init device setting with dump
                    this.init_device_setting();
                    this.device_setting.options.user_device = dump;

                    // listen to method done
                    this.device_setting.once('method:done', this.on_user_modify_action, this);

                    // listen to method remove
                    this.device_setting.once('method:reset', remove_method, this)

                    // edit selected method
                    window.location = current_location() + '?action=edit-group&did='+ model.get('device').id+'&mid='+this._config_method.get('id');
                }
                
                break;

                case 'remove':
                remove_method();
                break;

                case 'move':
                window.location = current_location() + '?action=move';
                break;
            }
        },

        on_user_confirm_item_position: function(new_actions) {
            console.log('---- new actions', new_actions);
            this.model.set('execution', new_actions);
            window.location = current_location();
        },

        on_user_confirm_delay_value: function(delay_action) {
            var cfg = {};
            if (this.delay_editor._action_idx != undefined) {
                cfg.at = this.delay_editor._action_idx;
            }
            this.model.get('execution').add(delay_action, cfg);

            window.location = current_location();
        },

        on_user_change_icon: function() {
            window.location = current_location() + '?action=change-icon';
        },

        on_user_changed_icon: function(icon) {
            // update data
            this.model.set('icon', icon);

            // update view
            this.invalidate_icon();
            this.on_user_close_icon_selector();
        },

        on_user_close_icon_selector: function(icon) {
            // hide
            var $content = Shell.hide_pop_message(function() {
                // then close
                window.location = current_location();
            })
            $content.finish();
        },

        on_user_save_scene: function(e) {
            var $e = $(e.currentTarget);

            if (!$e.hasClass('disabled')) {
                this.model.set('name', this.$('.body #name_txt').val());
                this.model.save({
                    success: function() {
                        this.trigger('save');
                        this.on_user_return_back();
                    }.bind(this),
                    error: function() {}
                });
            }
        },

        invalidate_scene_data: function() {
            var validated = true;

            // text field
            if (this.$('#name_txt').val() == '') validated = false;

            // scene item
            if (this.model.get('execution').length <= 0) validated = false;

            console.log('invalidate scene data', validated)
            if (validated) {
                this.$('#scene-done-btn').removeClass('disabled');
            } else {
                this.$('#scene-done-btn').addClass('disabled');
            }
        },

        on_user_out_of_focus_name_txtf: function() {
            this.invalidate_scene_data();
        }

    });

    return SceneEditorView;
});
