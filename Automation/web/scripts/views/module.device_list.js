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
    'Kurobox',
    'models/device',
    'views/module.unpairing.generic',
    'views/module.unpairing.zwave',
    'infinitescroll'
], function ($, _, Backbone, JST, Kurobox, Device, GenericUnpairModule, ZWaveUnpairModule) {
    'use strict';
    var hashTag = '#/device';
    var itemSize = 30;
    var listSpacer = '<div id="list-spacer" class="clear" style="height:50px;"></div>';
    var ModuleDeviceListView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.device_list.ejs'],
        list_template: JST['app/scripts/templates/module.device_list.devices_tmpl.ejs'],
        list_error_msg: JST['app/scripts/templates/module.device_list.error.ejs'],
        empty_device_tmpl: JST['app/scripts/templates/module.device_list.empty.ejs'],
        prompt_pop_msg: JST['app/scripts/templates/prompt.pop.ejs'],
        events: {
            'click .device-empty button': 'on_device_start',
            'click #device-list-error #retry-btn': 'retrieve_device',
            'click #option-button': 'on_device_action',
            'click #option-dark': 'on_option_closed',
            'click #dark-empty': 'on_cancel_start',
            'click #exit-options': 'on_option_closed',
            'click #nav-add': 'on_add_device',
            'click #device-control': 'on_user_select_device',
            //'click .device-itm': 'on_user_select_device',
            // 'click #mockup': 'hide_control_panel',
        },

        initialize: function() {
            this.collection = new Device.collection();
            this.firstBatchData = true;
        },

        clear: function() {
            if (this.unpair_module !== undefined) {
                this.unpair_module.stop();
                this.unpair_module.destory();
            }
            // destroy current infinite scroll
            $('#device-list').infinitescroll('destroy');

            // destroy html display
            $('#device-list').empty();

            // clear collection
            this.collection = new Device.collection();
        },

        is_empty: function() {
            return this.collection === undefined || this.collection.length === 0;
        },

        destroy: function() {
            if (this.unpair_module !== undefined) {
                this.unpair_module.destroy();
                this.unpair_module = undefined;
            }

            this.clear();
        },

        show: function() {
            this.$('#device-list').infinitescroll('resume')
            $(this.el).show();
        },

        hide: function() {
            this.$('#device-list').infinitescroll('pause')
            $(this.el).hide();
        },

        render: function() {
            $(this.el).html(this.template());
            $(this.el).attr('class', 'device-wrapper centerFlex');
             //remove page margin
            $('#main-container').removeClass( "container" );
            //$(this.el).addClass('centerFlex');
            return this;
        },

        retrieve_device: function(pageNum) {
            if (this.is_empty()) {
                pageNum = pageNum || 0;
                this.$('#device-list').infinitescroll('destroy');
                this.$('#device-list').data('infinitescroll', null);
                this.$('#device-list').empty();
            }
            this.begin_scroller();
            $('#device-list').infinitescroll('retrieve', pageNum);
            $('#device-list').infinitescroll('resume');
            
        },

        get_model: function(uid) {
            return this.collection.get(uid);
        },

        trigger_action: function(action, uid) {
            console.log('trigger action', action, uid)
            switch(action) {
                case 'unpair':
                this.unpair_device(uid);
                break;

                case 'options':
                this.trigger_options(uid)
                break;
            }
        },

        on_device_action: function(evt) {
            var did = $(evt.currentTarget).parent().data('ref_id');
            var act = $(evt.currentTarget).data('action'); 

            switch (act) {
                case 'unpair':
                case 'setting':
                case 'control-panel':
                location.replace(hashTag+'/'+act+'/' + did);
                break;

                default:
                console.error('No such action:', act);
                break;
            }
        },

        on_option_closed: function() {
            console.log('closed')
            window.location = hashTag;
        },

        trigger_options:function(did) {

            // bind id to option modal
            $('#device-option-modal #option-buttons').data('ref_id', did);

            // show hide element
            $('#option-dark').show();
            $('#device-list').attr('class', 'device-list');
            $('#device-option-modal:hidden').slideToggle();
        },

        hide_options: function() {
            $('#option-dark').hide();
            $('#device-list').attr('class', 'device-list');
            $('#device-option-modal:not(:hidden)').slideToggle();
            //$('#device-list').removeClass('not-blur');
        },

        unpair_device: function(uid) {
            // call unpair device api
            var model = this.collection.get(uid);
            var unpair_mod;
            console.log('unpair protocol:', model.get('protocolId'))
            switch (model.get('protocolId')) {
                // case 4:
                // // zwave unpair
                // unpair_mod = ZWaveUnpairModule;
                // break;

                default:
                // generic unpair
                unpair_mod = GenericUnpairModule;
                break;
            }

            this.unpair_module = new unpair_mod(this.$el.find('#module-content'), model, this.collection);
            this.unpair_module.on('unpair', this.unpair_device_complete, this); 
            this.unpair_module.on('cancel', this.unpair_device_cancel, this);
            this.unpair_module.render();
        },

        unpair_device_complete: function(model) {
            this.unpair_module.destroy();
            this.unpair_module = undefined;

            if (this.collection.length > 0) {
                // remove from item
                var itemEl =  $('#device-control[data-id="' + model.get('id') + '"]');
                itemEl.parent().remove();

                // centeralizing the components
                this.invalidateCenterFlex();

                // check if item at the bottom is empty
                this.invalidateViewElement($('#next'));
            } else {
                // collection is empty
                this.show_empty_list();
            }

            // replace history
            window.location.replace(hashTag);
        },

        unpair_device_cancel: function() {
            this.unpair_module.destroy();
            this.unpair_module = undefined;

            console.log('unpair cancelled')
            location.replace('#/device');
        },

        begin_scroller: function() {
            console.log('begin data scroller')
            $('#device-list').infinitescroll({
                navSelector     : 'a#next:last',
                nextSelector    : 'a#next:last',
                itemSelector    : '#device-list',
                debug           : false,
                maxPage         : 2,
                dataType        : 'json',
                appendCallback  : false,
                state           : {currPage:-1, isDestroyed: false, isDone:false},
                loading: {
                    finishedMsg: '',
                    img: "data:image/gif;base64,R0lGODlhAQABAHAAACH5BAUAAAAALAAAAAABAAEAAAICRAEAOw==",
                    msgText: '',
                    finished: function() {
                        console.log('--- finish scroll', $(this).infinitescroll())
                    }
                },
                errorCallback   : function () {
                   this.$('#device-list').infinitescroll('pause');
                   this.show_list_error();
                }.bind(this),
                path: function(pageNum) {
                    // in the meanwhile, centralize loading bar
                    $('#infscr-loading').css('text-align', 'center');
                    $('#infscr-loading').css('height', '0px');

                    var param = {
                        app_id: Kurobox.app_id,
                        method: 'get_paired_device_list',
                        module: 'device_manager',
                        limit: itemSize,
                        offset: (pageNum*itemSize)
                    };

                    // make a copy reference for rendering later
                    this.api_param = param;

                    return Kurobox.host+'/cgi-bin/syb_reqresp_cgi?'+$.param(param);
                    // return 'json/device_list.json?'+$.param(param);
                }.bind(this)
            }, function(response, options){ //callback
                if (response.theKuroBox.returnValue === 100) {
                    // remove previous spacer
                    $('#device-list > #list-spacer').remove();

                    this.collection.add(response.theKuroBox, {parse:true});

                    if (this.collection.models.length <= 0 && this.firstBatchData) {
                        // assume there's not device paired
                       this.show_empty_list();

                        this.trigger('list empty')
                    } else {
                         // $('.nav-icon-edit').addClass('icon-off');
                         //$('#device-list').html(this.empty_device_tmpl());
                        $('#device-list').append(this.list_template({
                            collection: this.collection, 
                            offset: this.api_param.offset,
                            limit: this.api_param.limit,
                            total: response.theKuroBox.response.totalItem,
                        }));
                        console.log('test termination', this.collection.length, response.theKuroBox.response.totalItem)
                        if (this.collection.length >= response.theKuroBox.response.totalItem) {
                            // stop data request
                            $('#device-list').infinitescroll('destroy');
                        }
                        // handle if only one item do not align center
                        this.invalidateCenterFlex();
                    }

                    $('#device-list').append(listSpacer);

                    // check if item at the bottom is empty
                    this.invalidateViewElement($('#next'));

                    this.firstBatchData = false;
                    this.trigger('list complete')
                } else {
                    $('.device-list').infinitescroll('destroy');

                    // show error
                    this.show_list_error(response.theKuroBox.returnMessage+' ['+response.theKuroBox.returnValue+']');

                    //TODO: show some error message
                    console.error('API error', response.theKuroBox.returnValue, response.theKuroBox.returnMessage);
                }

            }.bind(this));
        },

        show_list_error: function(error_ref) {
            this.$('#device-list').html(this.list_error_msg({
                reference: error_ref || ''
            }));
        },

        invalidateCenterFlex: function() {
            if(this.collection.length === 1){
                this.$el.removeClass('centerFlex');
            } else {
                this.$el.addClass('centerFlex');
            }
        },

        show_empty_list: function() {
             // show tutorial
            $('#device-list').html(this.empty_device_tmpl());

            $('#device-list').infinitescroll('destroy');
            // disable edit icon
            $('.nav-icon-edit').addClass('icon-off');
        },

        invalidateViewElement:function (elem)
        {
            var docViewTop = $(window).scrollTop();
            var docViewBottom = docViewTop + $(window).height();

            var elemTop = $(elem).offset().top;
            var elemBottom = elemTop + $(elem).height();

            return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
        },

        on_device_start:function (){
            console.log('on_device_start');
            $('.dark-layer-70').show();
            $('.device-empty-start').show();
            $('body').scrollTop(0);
        },

        on_cancel_start: function(){
            $('.dark-layer-70').hide();
            $('.device-empty-start').hide();
        },

        on_add_device:function (){
            window.location = '#/device/add';
        },

        on_user_select_device: function(e) {
            var $e = $(e.currentTarget);
            // var $e = $(e.currentTarget).parent();
            var model = this.collection.get($e.data('id'));
            console.log(model)
            if (model.get('isControllable') && model.get('enabled')) {
                // redirect to control panel
                window.location = '#/device/control-panel/'+$e.data('id');
            } else {
                // nothing to be controlled btw
                var $pop_content = Shell.show_pop_message(this.prompt_pop_msg({
                    title: 'error_unsupported_control_panel',
                    message: 'msg_unsupported_control_panel'
                }), {
                    // event function
                    'click #modal-ok-btn': this._on_user_acknowledge_error.bind(this)
                },
                this._on_user_acknowledge_error.bind(this));

                $pop_content.find('#modal-cancel-btn').hide();
                console.warn('TODO: redirect to advanced setting');
            }
        },

        _on_user_acknowledge_error: function() {
            Shell.hide_pop_message();
        }

    });

    return ModuleDeviceListView;
});
