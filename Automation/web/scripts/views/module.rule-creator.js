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
    'views/module.rule.device_explorer',
    'views/module.rule.device-setting',
    'models/rule',
    'views/module.rule-creator.summary'
], function ($, _, Backbone, JST, RuleDeviceExplorer, RuleDeviceSetting, RuleConfig, RuleSettingSummary) {
    'use strict';

    var OptionModel = Backbone.Model.extend({
        defaults:{
            label: '',
            value: ''
        },
        idAttribute: 'value'
    })

    var OptionCollection = Backbone.Collection.extend({model: OptionModel})

    var non_event_trigger_options = new OptionCollection([
        {label: 'Interval', value: 2},
        {label: 'Time', value: 1},
    ])

    var interval_options = new OptionCollection([
        {label: '5 min', value: 300},
        {label: '10 min', value: 600},
        {label: '15 min', value: 900},
        {label: '30 min', value: 1800},
        {label: '1 hour', value: 3600},
        {label: '3 hour', value: 10800},
        {label: '6 hour', value: 21600},
        {label: '12 hour', value: 43200},
        {label: '24 hour', value: 86400},
        {label: '1 min', value: 60}
    ])

    var search_collection = function(collection, search_value) {
        var result;
        collection.each(function(model) {
            if (model.get('value') === search_value) {
                result = model.get('label');
                return false;
            }
        });
        return result;
    }

    var ModuleRuleCreatorView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.rule-creator.ejs'],
        rule_item_tmpl: JST['app/scripts/templates/module.rule.device-rule-item.ejs'],
        option_tmpl: JST['app/scripts/templates/module.rule.options.ejs'],
        header_content: JST['app/scripts/templates/module.rule-creator.header.ejs'],
        header_template: JST['app/scripts/templates/module.rule.grey-header.ejs'],
        prompt_pop_dialog_msg: JST['app/scripts/templates/prompt.pop.ejs'],
        events: {
            'click .nav-circle-outline.nav-icon-edit': 'edit_devices',
            'click #header-rule-creator #nav-back-btn': 'user_close_this',
            'click .opt-value': 'user_select_trigger_stuff',
            'click #option-label': 'user_select_option',
            'click .device #label': 'user_edit_device_config',
            // 'click #rule-action-desc': 'user_toggle_desc_mode',
            'blur #edit-name':'check_input_validity',
            'keyup #edit-name':'check_input_validity',
            'focus #edit-name':'on_input_focus',
            'click #rule-done-btn': 'save_rule'
        },
        destroy: function() {
            this.device_rule_setting.destroy();
            this.device_rule_setting = undefined;
            
            this.device_explorer = undefined;
            this.rule_config = undefined;
            this.options = undefined;
            $(this.el).empty();
            $(this.el).hide();
        },
		render: function() {
            if (this.rule_config === undefined) {
                this.create_rule_config();
            }

            // flag for changes
            this.has_changes = false;

            $(this.el).html(this.template({
                config: this.rule_config, 
                mode: this.options.mode
            }));

            // modified href for 'select event' & 'select action'
            var _base_url;
            if (this.options.mode === 'edit') {
                _base_url = '#/rule/'+this.options.mode+'/'+this.rule_config.id;
            } else {
                _base_url = '#/rule/'+this.options.mode;
            }
            var if_href = this.$('#if-content').attr('href');
            var then_href = this.$('#then-content').attr('href');
            this.$('#if-content').attr('href',_base_url+if_href);
            this.$('#then-content').attr('href', _base_url+then_href);

            // initialise device lister
            _.defer(function() {

                // render header
                this.$('#header-rule-creator').html(this.header_template({
                    content: this.header_content({
                        mode: this.options.mode,
                        config: this.rule_config,
                        search_collection:search_collection,
                        trigger_options: non_event_trigger_options,
                        interval_options: interval_options,
                    })
                }))

	            this.device_explorer = new RuleDeviceExplorer({el: $('#device-explorer'), prompt_message: this.options.parent.prompt_message, base_url: _base_url});
	            this.device_explorer.on('busy', function() { this.trigger('busy') }.bind(this));
	            this.device_explorer.on('idle', function() { this.trigger('idle') }.bind(this));

	            this.device_rule_setting = new RuleDeviceSetting({el: $('#device-setting')});
	            this.device_rule_setting.on('done', function(setting_config) {
                    if (setting_config.get('methods').length > 0) {
                        // empty element to force summary to refresh
                        if (this.section === 'if') {
                            this.condition_summary.$el.empty();
                        } else {
                            this.execution_summary.$el.empty();
                        }

                        // update data
                        console.log('setting saved', setting_config);
                        var section = (this.section === 'if') ? 'condition' : 'execution';
                        this.rule_config.get(section).add(setting_config, {merge: true});

                        // flag for changes
                        this.has_changes = true;

                        // update ui
                        this.update_trigger();
                    }

                    this.go_main();
                    // action set compiled
                    // hide add interface
                    /*this.device_rule_setting.close();

                    // save configuration on member
                    var model_prop = (this.section === 'if') ? 'condition' : 'execution';
                    if (mode === 'add') {
                        this.rule_config.get(model_prop).add(setting_config, {merge: true});
                    } else {
                        this.rule_config.get(model_prop).set(setting_config);
                    }

                    // determine if event based action inside the configuration
                    this.update_trigger();
        
                    this.go_main();
                    $('#main-container').addClass('container');*/
                }.bind(this));

                // summary for condition
                this.condition_summary = new RuleSettingSummary({el: this.$('#if-container #if'), mode: this.options.mode, section: 'if'});
                this.execution_summary = new RuleSettingSummary({el: this.$('#then-container #then'), mode: this.options.mode, section: 'then'});

                // check content validity?
                // this.check_content_validity();

	            this.trigger('inited');

            }.bind(this));
            return this;
        },
        navigate: function(uid, query) {
			console.log('query', query)
            this.uid = uid;

            if (query === null) query = undefined;
            // reset prompt mesage
            if (this.options.parent !== undefined) this.options.parent.prompt_message('hide');

			// reset rule-content
			if ($('#rule-content').is(':hidden')) $('#rule-content').show();
             
			// setup nav
			var nav = {};
            nav.left = ['BACK'];
            nav.right = ['EDIT_RULE', 'SAVE_RULE'];
            // nav.right = ['SAVE_RULE'];
            if (this.options.mode === 'edit') {
                nav.title = 'edit_rule';
            } else {
                nav.title = 'add_rule';
            }
            nav.callback = this.on_add_rule_nav_updated.bind(this);

            // render trigger value renderer
            switch ($('#trigger-setting').data('value')) {
                case 0:
                    $('#option-interval').hide();
                    $('#trigger-time').hide();
                    break;

                case 1:
                    $('#option-interval').hide();
                    $('#trigger-time').show();
                    break;

                case 2:
                    $('#option-interval').show();
                    $('#trigger-time').hide();
                    break;
            }

            // reset variable
            this.action = undefined;
            this.section = undefined;
            this.selected_option = undefined;

            // restore global preloading events
            Shell.restorePreloadingEvents();
            
            if (!_.isEmpty(query)) {
                if (typeof query.action !== 'undefined' && query.action !== '') {
                    // add back container by default
                    $('#main-container').addClass('container');

                    this.section = query.section;
                    this.action = query.action;
                    switch (query.action) {
                        case 'list-types':
                        // disable global preloading events
                        // Shell.removePreloadingEvents();
                        this.$('#rule-content').hide();

                        // get the list
                        this.device_explorer.list_type(this.section);

                        if (this.device_rule_setting.$el.is(':visible')) {
                            this.device_rule_setting.close();
                        }
                        break;

                        case 'list-devices':
                        // disable global preloading events
                        // Shell.removePreloadingEvents();
                        this.$('#rule-content').hide();

                        // get the list
                        this.device_explorer.list_device(this.section, query.group, query.name);
                        if (this.device_rule_setting.$el.is(':visible')) {
                            this.device_rule_setting.close();
                        }
                        break;

                        default:
                            // meiai wanted to have rule setting to have
                            // full grey colour panel in argument pane
                            $('#main-container').removeClass('container');
                            // if (this.device_explorer.device_collection.length <= 0) {
                            //     // retrieve device and store back to device_explorer
                            //     this.go_main();
                            // } else {
                            if (typeof query.did !== 'undefined' && query.did !== '') {

                                if (this.device_explorer.el.is(':visible')) {
                                    this.device_explorer.close();
                                }

                                $('#rule-content').hide();

                                // navigation configuration setup in RuleSetting class
                                nav = undefined;
                                
                                // begin device setting
                                if (this.device_rule_setting.$el.is(':hidden')) {
                                    this.device_rule_setting.$el.show();
                                }
                                this.device_rule_setting.start(query.did, this.section, this.options.nav, query);
                            } else {
                                throw 'No DID is defined!'
                            }
                        // }
                        break;

                        case 'delete':
                        // prompt user
                        this.options.parent.prompt_message({
                            confirm_callback: function() {
                                this.delete_device(query.id, query.aid);
                                this.update_trigger();
                                this.go_main();
                            }.bind(this),
                            cancel_callback: function() {
                                this.go_main();
                            }.bind(this)
                        })
                        break;
                    }
                } else if (!_.isEmpty(query.option)) {
                    this.selected_option = query.option;
                    var selected_value;

                    nav.right = [];
                    switch(this.selected_option) {
                        case 'trigger':
                        nav.title = $('#trigger-setting').parent().find('.opt-label').text();
                        selected_value = $('#trigger-setting').data('value');
                        break;

                        case 'interval':
                        nav.title = $('#option-interval .opt-label').text();
                        selected_value = $('#on-interval').data('value');
                        break;
                    }

                    this.render_options(query.option, selected_value);
                }
            } else {
                // add back container
                if (!$('#main-container').hasClass('container')) $('#main-container').addClass('container');
                
                if (this.device_explorer.el.is(':visible') && 
                    query === undefined) {
                    this.device_explorer.close();
                }
                if (this.device_rule_setting.$el.is(':visible') && query === undefined) {
                    this.device_rule_setting.close();
                }
                if ($('#rule-options').is(':visible')) {
                    $('#rule-options').hide();
                }
            }

            if (nav !== undefined) {
            	this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
                this.options.nav.update_title(nav.title); 

                //if (this.action === undefined && this.selected_option === undefined) {
                    // assume it's in the rule creator's summary
                    this.check_content_validity();
                //}
            }
        },

        check_content_validity:function(){
             // only do bellow action when condition or action got data then show the action gp

             if (this.rule_config.get('condition').length > 0){
                this.$('#if-container').show();
                this.$('.dialog-box').hide();
                this.update_device_rule_list();
             }else{
                this.$('#if-container').hide();
                this.$('.dialog-box').show();
             }

             if (this.rule_config.get('execution').length > 0){
                this.$('#then-container').show();
                this.update_device_rule_list();

             }else{
                 this.$('#then-container').hide();
             }

            

              // validate edit button
             if (this.rule_config.get('condition').length > 0 || this.rule_config.get('execution').length > 0){
                 $('.nav-icon-edit').removeClass('icon-off');
             }else{
                 $('.nav-icon-edit').addClass('icon-off');
             }

            /*if (this.rule_config.get('condition').length > 0 || this.rule_config.get('execution').length > 0){
                $('#action-gp').show();
                $('.dialog-box').hide();

                this.update_device_rule_list();
            }else{
                $('.dialog-box').show();
            }*/

            // validate edit button
           /* if (this.rule_config.get('execution').length > 0) {
                $('.nav-icon-edit').removeClass('icon-off');
            } else {
                $('.nav-icon-edit').addClass('icon-off');
            }*/

            // validate save button
            this.validate_save_btn();
        },

        validate_save_btn:function() {
            if($('#edit-name').val().length <= 0 || this.rule_config.get('execution').length <= 0  || this.rule_config.get('condition').length <= 0 ){
                 console.log('disabled btn');
                $('#rule-done-btn').addClass('disabled');
            }else{
                 console.log('enabled btn');
                $('#rule-done-btn').removeClass('disabled');
            }
        },

        create_rule_config: function() {
            this.rule_config = new RuleConfig.model();
        },
        update_device_rule_list: function() {
            this.condition_summary.render(this.rule_config.get('condition'), this.uid)
            this.execution_summary.render(this.rule_config.get('execution'), this.uid)
        },

        render_options: function(option, selected_option) {
            var options_value;
            switch (option) {
                case 'trigger':
                // TODO: detect if is there any event based condition
                options_value = non_event_trigger_options;
                break;

                case 'interval':
                options_value = interval_options;
                break;
            }

            if (options_value !== undefined) {
                $('#rule-content').hide();

                $('#rule-options').show();
                $('#rule-options').html(this.option_tmpl({options: options_value, selected_option: selected_option}));
            }
        },

        delete_device: function(device_id, func) {
            var $deviceEl = $('#'+this.section+' #'+device_id);
            var $actionContEl = $deviceEl.find('.rule-action-container');
            var $actionEl;
            var devices = this.rule_config.get((this.section === 'if') ? 'condition': 'execution');
            var device = devices.get(device_id);

            if (func !== undefined) {
                $actionEl = $actionContEl.find('#'+func);
                $actionEl.remove();

                if ($actionContEl.children().length === 0) {
                    // empty action
                    $deviceEl.remove();
                    devices.remove(device);
                } else {
                    var actions = device.get('methods');
                    actions.remove(actions.get(func));
                }
            } else {
                // asking to delete device
                $deviceEl.remove();
                devices.remove(device);
            }
        },

        save_rule: function(e) {
            if(this.$('#rule-done-btn').hasClass('disabled')){
                console.log('Not allow to save');
            }else{
                // call to save config
                // grab ui value
                var prop = {
                    name: this.$el.find('#edit-name').prop('value'),
                    trigger: {
                        type: this.$el.find('#trigger-setting').data('value')
                    }
                }

                switch (prop.trigger.type) {
                    case 1:
                    prop.trigger.value = this.$el.find('#trigger-time input').prop('value');
                    break;

                    case 2:
                    prop.trigger.value = this.$el.find('#on-interval').data('value');
                    break;
                }

                console.log('prop', prop)
                this.rule_config.save(prop, {success: function() {
                        // navigate back to list
                        this.trigger('saved');
                    }.bind(this),
                    error: function(model, resp) {
                        console.error('Unable to save rule', resp)
                    }.bind(this)
                });
            }
            
        },

        edit_devices: function(e) {
            var $target = (e) ? $(e.currentTarget) : this.$('.nav-circle-outline.nav-icon-edit');

            if (!$target.hasClass('icon-off')) {
                // show dustbin
                var $if_devices = this.$('#if-container').find('.delete-device');
                var $if_methods = this.$('#if-container').find('.delete-action');
                var $then_devices = this.$('#then-container').find('.delete-device');
                var $then_methods = this.$('#then-container').find('.delete-action');

                // console.log('test hidden', $device_els.is('hidden'))
                $if_devices.toggle();
                $if_methods.toggle();
                $then_devices.toggle();
                $then_methods.toggle();
            }
        },

        go_back: function(e) {

        },

        on_add_rule_nav_updated:function (item, nav) {
            console.log('nav cb', item)
            switch(item) {
                case nav.BACK:
                    // go back to rule list
                    if (this.action === undefined && this.selected_option === undefined) {
                        window.location = '#/rule';
                    } else {
                        window.history.back();
                    }
                break;

                case nav.EDIT_RULE:
                    
                break;

                case nav.SAVE_RULE:
                    
                break;
            }
        },

        invalidate_event_based_method: function() {
            var condition = this.rule_config.get('condition');
            var hasEvent = false;
            if (condition.length > 0) {
                condition.each(function(device) {
                    // each device
                    device.get('methods').each(function(method) {
                        // each method
                        if (method.get('hasEvent')) {
                            hasEvent = true;
                            return false;
                        }
                    })

                    if (hasEvent) {
                        return false;
                    }
                }.bind(this))
                return hasEvent;
            }
            return hasEvent;
        },

        update_trigger: function() {
            var $trigger = this.$el.find('#trigger-setting');
            var hasEvent = this.invalidate_event_based_method();
            if (hasEvent) {
                if ($trigger.data('value') !== 'event') {
                    // change Trigger on
                    $trigger.data('value', 0);
                    $trigger.text('Event');
                }
            } else {
                if ($trigger.data('value') === 'event') {
                    // change Trigger on
                    $trigger.data('value', 1);
                    $trigger.text(non_event_trigger_options.get(1).get('label'));
                }
            }
        },

        user_close_this: function(e) {
            $('#rule-dark').hide();

            if (this.has_changes) {
                // prompt user for discard changes
                this.prompt_user_discard();
            } else {
                window.location = '#/rule';
            }
        },

        user_select_trigger_stuff: function(e) {
            var $e = $(e.currentTarget);
            switch ($e.prop('id')) {
                case 'trigger-setting':
                if ($e.data('value') !== 0) {
                    this.go_main({option: 'trigger'});
                }
                break;

                case 'on-interval':
                this.go_main({option: 'interval'});
                break;
            }
        },

        user_select_option: function(e) {
            var $e = $(e.currentTarget);
            var $ui_update, label;
            label = $e.text();
            switch(this.selected_option) {
                case 'trigger':
                    $ui_update = $('#trigger-setting');
                    break;

                case 'interval':
                    $ui_update = $('#on-interval');
                    break;
            }

            $ui_update.text(label);
            $ui_update.data('value', $e.data('value'));

            this.go_main();
        },

        user_edit_device_config: function(e) {
            var $e = $(e.currentTarget);
            var did = $e.parent().parent().prop('id');
            var section = $e.parent().parent().parent().prop('id');

            // set config to rule setting
            // this.device_rule_setting.options.config = this.rule_config.get((section === 'if') ? 'condition' : 'execution').get(did);
            this.device_rule_setting.options.user_device = this.rule_config.get((section === 'if') ? 'condition' : 'execution').get(did);

            this.go_main({
                section: section,
                action: 'select',
                did: did
            })
        },

        go_main: function(param) {
            console.log('test url', '#/rule/'+this.options.mode+(this.uid !== undefined ? '/'+this.uid : '')+(param !== undefined ? '?'+$.param(param) : ''))
            window.location = '#/rule/'+this.options.mode+(this.uid !== undefined ? '/'+this.uid : '')+(param !== undefined ? '?'+$.param(param) : '');
        },

        user_toggle_desc_mode: function(e){
             var $e = $(e.currentTarget);
             
             if($e.hasClass( 'itm-chop' ))
             {
                 $e.attr('class', 'item_expend');
             }
             else{
                 $e.attr('class', 'itm-chop');
             }
        },

        check_input_validity: function(e) {
            $('body').scrollTop(0);
            //$('body').removeClass('fixfixed');
            // check validity when input not empty
            if( $(e.currentTarget).val()!=''){
                console.log('call not focus');
                // check pattern validity
                $(e.currentTarget).addClass( 'notfocussed' );
                $(e.currentTarget).removeClass( 'error-msg' );
                $(e.currentTarget).removeClass( 'error-border' );
            }
            else
            {
                 console.log('call focus');
                $(e.currentTarget).removeClass( 'notfocussed' );
            }

            this.validate_save_btn();

            // flag the changes
            this.has_changes = true;
        },

        on_input_focus: function(){
            //$('body').scrollTop(0);
            //$('body').addClass('fixfixed');
        },

        prompt_user_discard: function() {
            Shell.show_pop_message(
                this.prompt_pop_dialog_msg({
                    title: 'There are some changes',
                    message: 'Are you sure you want to discard changes?',
                    ok_btn_label: 'Discard',
                    cancel_btn_label: 'Cancel'
                }),
                {
                    'click #modal-ok-btn': this.discard_changes.bind(this),
                    'click #modal-cancel-btn': this.on_user_acknowledge_prompt_message.bind(this)
                },
                this.on_user_acknowledge_prompt_message.bind(this)
            )
        },

        on_user_acknowledge_prompt_message: function() {
            // close pop message
            Shell.hide_pop_message();
        },

        discard_changes: function() {
            this.on_user_acknowledge_prompt_message();

            // and go back
            window.location = '#/rule';
        }
    });

    return ModuleRuleCreatorView;
});
