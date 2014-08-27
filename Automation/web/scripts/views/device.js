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
    'views/module.device_list',
    'views/module.device-info',
    'views/module.add-device',
    'views/control.speaker',
    'views/control.door-lock',
    'views/control.switch',
    'views/control.hue',
    'views/control.dimmer',
    'views/control.dimmer-stepper',
    'views/control.ipcamera',
    'views/control.power-switch',
    'views/control.horn',
    'bootstrap'
], function ($, _, Backbone, JST, DeviceListModule, DeviceInfoModule, DeviceAddModule, ControlSpeaker, DoorLockControl, SwitchControl, HueControl, DimmerControl, DimmerStepperControl, IPCameraControl, PowerSwitchControl, HornControl) {
    'use strict';

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
            this.content_module.destroy();
            if(this.info_module !== undefined){
                this.info_module.destroy();
            }

            if (this.control_module !== undefined) {
                this.control_module.destroy();
                this.control_module = undefined;
            }

            if (this.content_module !== undefined) {
                this.content_module.destroy();
                this.content_module = undefined;
            }
        },

        navigate: function(action, uid, query) {
        	console.log('param', action, uid);
            console.log('query', query)
            this.uid = uid;
            this.action = action;
            var nav = {};

            if (_.isEmpty(this.content_module) && this.validateListModule(action)) {
                this.content_module = new DeviceListModule();
                this.content_module.render();
                this.content_module.on('list complete', function() {
                    this.trigger('idle');

                    // determine right nav header icons
                    if (this.content_module.collection.length <= 0) {
                        // empty list
                        this.options.nav.update_buttons(undefined, ['ADD_RULE']);
                    } else {
                        if (this.action !== 'setting') {
                            
                            this.options.nav.update_buttons(undefined, ['ADD_RULE']);
                        }
                    }
                }, this);
                $('.page-content').append(this.content_module.el);

                this.trigger('busy');
            }

            // terminate control panel
            if (action !== 'control-panel' && this.control_module !== undefined) {
                // destroy it!
                this.control_module.destroy();
                this.control_module = undefined;
            }


           // initialise header
            nav.title = 'automation';
            nav.callback = this.on_device_list_nav_updated.bind(this);
            
            switch (action) {
                case 'list_device':
                    // initialise header
                    nav.left = ['NAV_HOME'];
                    nav.right = ['ADD_RULE'];
                    nav.title = 'automation';
                    nav.callback = this.on_device_list_nav_updated.bind(this);

                    if (this.info_module !== undefined) {
                        this.info_module.close();
                    }
                    if (this.add_module !== undefined) {
                        this.add_module.hide();
                    }
                     //remove page margin
                    $('#main-container').removeClass( "container" );

                    this.content_module.show();
                    this.content_module.hide_options();
                    this.prompt_message('hide');

                    if (this.content_module.is_empty()) {
                        // renew data
                        this.content_module.retrieve_device();
                    }
                    break;

                case 'options':
                    if (this.info_module !== undefined) {
                        this.info_module.close();
                    }
                    if (this.add_module !== undefined) {
                        this.add_module.hide();
                    }
                    this.content_module.show();
                    this.content_module.trigger_action(action, uid);
                    console.log('options');
                      // initialise header
                    nav.left = ['NAV_HOME'];
                    nav.right = ['ADD_RULE'];
                    nav.title = 'automation';
                    nav.callback = this.on_device_list_nav_updated.bind(this);
                    this.prompt_message('hide');
                    break;
        
                case 'unpair':
                    // prompt!
                    this.content_module.hide_options();
                    
                    console.log('ask user wan to remove? seriously?')
                    this.prompt_message({
                        title: 'remove_device',
                        message: 'msg_remove',
                        confirm_label: 'remove',
                        confirm_callback: function() {
                            this.prompt_message('hide');
                            this.content_module.trigger_action(action, uid);
                        }.bind(this),
                        cancel_callback: this.on_everything_cancel
                    })
                    break;

                case 'setting':
                    if (_.isEmpty(this.info_module)) {
                        // initialise info module
                        this.info_module = new DeviceInfoModule();
                        this.info_module.render();
                        this.info_module.on('close', this.on_info_module_closed, this);
                    }

                    if (this.content_module !== undefined) {
                        this.content_module.hide_options();
                        this.content_module.hide();
                    }

                    if (this.add_module !== undefined) {
                        this.add_module.hide();
                    }

                    nav.left = ['BACK'];
                    nav.right = [];
                    nav.title = 'edit_device';
                    if(query){
                        if(query.action == 'change-type'){
                            nav.title = 'type';
                        }
                    }
                    nav.callback = this.on_device_info_nav_updated.bind(this);

                    var edit_cb = this.options.callback;
                    delete this.options.callback;

                    // embed it the el to page content
                    $('.page-content').append(this.info_module.el);
                    $('#main-container').addClass( "container" );
                    if (this.info_module.isOpened) {
                        this.info_module.update_action(query);
                    } else {
                        this.info_module.open(uid, {
                            'save-and-add-btn': (edit_cb !== undefined),
                            'save-btn': true,
                        }, edit_cb, query);
                    }
                    break;

                case 'control-panel':
                    if (this.content_module !== undefined) {
                        this.content_module.hide_options();
                        this.content_module.hide();
                    }

                    if (this.info_module !== undefined) {
                        this.info_module.close();
                    }

                    nav.left = ['BACK'];
                   // nav.right = ['ADVANCE'];
                    nav.right = []; 
                    nav.title = undefined;
                    // NOTE: set later in show_control_panel method
                    // nav.title = this.content_module.collection.get(uid).get('name');
                    nav.callback = this.on_device_list_nav_updated.bind(this);
                    this.show_control_panel(uid);
                    break;

                case 'advanced-control-panel':

                break;

                case 'add':
                    if (this.content_module !== undefined) {
                        this.content_module.hide_options();
                        this.content_module.hide();
                    }

                    if (this.info_module !== undefined) {
                        this.info_module.close();
                    }

                    if (this.add_module === undefined) {
                        // initialise add device module
                        this.add_module = new DeviceAddModule();
                        this.add_module.on('paired', this.on_new_device_paired, this);
                        this.add_module.render();
                    }
                    if (this.add_module.$el.is(':hidden')) {
                        $('body').scrollTop(0);
                        this.add_module.show();
                    }

                    $('.page-content').append(this.add_module.el);
                    $('#main-container').removeClass( "container" );
                    console.log('uid: ', uid);
                    
                    // setup nav
                    nav.left = ['BACK'];
                    nav.right = [];
                    nav.title = 'add_device';
                    nav.callback = this.on_device_info_nav_updated.bind(this);
                    this.add_module.navigate(uid);
                    break;

                default:
                console.error('Invalid action');
                return;
            }

            this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
            if (typeof nav.title !== 'undefined') this.options.nav.update_title(nav.title);  
        },

        set_param: function(param) {
            this.options = param;
        },

        on_device_list_nav_updated: function(item) {
            console.log('on_device_list_nav_updated!');
            console.log('nav cb', item)

            switch(item) {
                case this.options.nav.NAV_HOME:
                    window.location = '/system/myapp';
                break;

                case this.options.nav.ADD_RULE:
                // go to add device
                window.location = '#/device/add';
                break;

                case this.options.nav.ADVANCE:
                // go to advance control panel
                window.location = '#/device/advanced-control-panel/'+this.uid;
                break;

                case this.options.nav.BACK:
                window.history.back();
                break;
            }
        },

        prompt_message: function() {
            var action = 'show';
            var conf = {
                confirm_label: 'btn_ok',
                cancel_label: 'btn_cancel',
                confirm_callback: undefined,
                cancel_callback: undefined
            };

            if (typeof arguments[0] === 'string') {
                action = arguments[0];
            } else {
                _.extend(conf, arguments[0]);

                // fill in the blank
                $('#myModalLabel').text(conf.title || '');
                $('#modal-body').text(conf.message || 'msg_are_u_sure');
                $('#modal-cancel-btn').text(conf.cancel_label);
                $('#modal-ok-btn').text(conf.confirm_label);
            }

            // execute action
            $('#prompt-modal').data('confirm_cb', conf.confirm_callback);
            $('#prompt-modal').data('cancel_cb', conf.cancel_callback);
            // $('#prompt-modal').modal(action);
            
            console.log('action', action)
            if (action === 'show') {
                this.$('#confirm-dark').show();
                this.$('#prompt-modal').show();
            } else {
                this.$('#confirm-dark').hide();
                this.$('#prompt-modal').hide();
            }
        },

        on_prompt_confirm:function () {
            var func = $('#prompt-modal').data('confirm_cb');
            if (func !== undefined) func();
            this.prompt_message('hide');
        },

        on_prompt_cancel: function() {
            console.log(' on_prompt_cancel');
            var func = $('#prompt-modal').data('cancel_cb');
            if (func !== undefined) func();
            this.prompt_message('hide');
        },

        on_prompt_close: function() {
            console.log(' on_prompt_close');
            $('#device-list').attr('class', 'device-list not-blur');
            $('#prompt-modal:not(:hidden)').slideToggle();
            $('#device-list').removeClass('not-blur');
        },

        on_info_module_closed: function(saved) {

            if (saved) {
                // clear current list
                this.content_module.clear();
            }
            // info module closed
            window.location = '#/device';
        },

        on_device_info_nav_updated: function(item) {
            console.log('back!!!');
            window.history.back();
        },

        validateListModule: function(action) {
            return action === 'options' ||
            action === 'list_device' || 
            action === 'unpair' ||
            action === 'setting' || 
            action === 'control-panel' || 
            action === 'advanced-control-panel'

        },

        on_new_device_paired: function(device_model) {
            this.trigger('idle');
            this.options.callback = window.location.href;

            // mark list to reload
            this.content_module.clear();

            // navigate to edit device
            console.log('device_model id' + device_model.get('id'));
            window.location = '#/device/setting/'+device_model.get('id');
        },

        load_control_panel: function(uid) {
            var control_uri = '/'+uid+'/index.html';
            console.log('loading', control_uri);

            $('.control-panel-holder').show();
            $('#control-panel-loader').attr('src', control_uri);
        },

        unload_control_panel: function() {
            $('.control-panel-container').hide();
            $('#control-panel-container').attr('src', '');
        },

        on_everything_cancel: function() {
            location.replace('#/device');
        },

        init_nav_bar: function(){
            var nav = {};
            nav.left = ['NAV_HOME'];
            nav.right = ['ADD_RULE'];
            nav.title = 'automation';
            nav.callback = this.on_device_list_nav_updated.bind(this);
            this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
            this.options.nav.update_title(nav.title);  
        },

        show_control_panel:function(id){
            if (this.content_module.collection !== undefined && this.content_module.collection.length > 0) {

                if (this.control_module !== undefined) {
                    this.control_module.destroy();
                    this.control_module = undefined;
                }

                var model = this.content_module.collection.get(id);
                var module;
                console.log('id', id);
                console.log('type', model.attributes);

                switch (model.get('typeId')) {
                    case 1:
                    module = SwitchControl;
                    break;

                    case 2:
                    module = DoorLockControl;
                    break;

                    case 3:
                    module = DimmerControl;
                    break;

                    case 4:
                    module = PowerSwitchControl;
                    break;

                    case 5:
                    module = HueControl;
                    break;

                    case 6:
                    console.log('No control panel for sensor')
                    break;

                    case 7:
                    module = ControlSpeaker;
                    break;

                    case 8:
                    case 22:
                    case 23:
                    case 24:
                    case 25:
                    case 26:
                    module = HornControl;
                    break;

                    case 9:
                    module = IPCameraControl;
                    break;

                    case 27:
                    module = DimmerStepperControl;
                    break;

                    default:
                    console.error('unknown device type', model.get('typeId'))
                    break;
                }
                this.control_module = new module({el: this.$('#control-panel'), device: model})
                this.control_module.render();

                this.$('#control-panel').show();

                // set title
                this.options.nav.update_title(model.get('name'));
                // $('#option-dark').show();
            } else {
                // route back to home
                this.on_everything_cancel();
            }
        },

        show_mockup:function (type){
            var path='images/mockup/'+ type+'.jpg';
            console.log('path', path)
            $( "#mockup" ).show();
            $( '#imgMockup' ).attr( 'src', path);
        },

        hide_control_panel:function(){
            //$( "#mockup" ).hide();
            // $( '#imgMockup' ).attr( 'src', '');

            // $('#option-dark').hide();
        },

    });

    return DeviceView;
});
