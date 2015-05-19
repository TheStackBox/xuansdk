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
    'Kurobox',
    'models/rule',
    'infinitescroll'
], function ($, _, Backbone, JST, Kurobox, Device) {
    'use strict';
    var hashTag = '#/rule';
    var itemSize = 20;
    var listSpacer = '<div id="list-spacer" class="clear tab-spacer"></div>';
    var ModuleRuleListView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.rule-list.ejs'],
        item_template: JST['app/scripts/templates/module.rule-list.tmpl.ejs'],
        empty_device_tmpl: JST['app/scripts/templates/module.rule-list.empty.ejs'],
        list_error_msg: JST['app/scripts/templates/module.rule-list.error.ejs'],
        events: {
            'click .device-empty button': 'on_device_start',
            'click #device-list-error #retry-btn': 'on_user_error_retry',
        	'click .device-option': 'on_device_option',
            'click #option-button': 'on_device_action',
            'click #option-dark': 'on_option_closed',
            'click #exit-options': 'on_option_closed',
            'click .rule-row': 'user_execute_rule'
        },

        initialize: function() {
            this.firstBatchData = true;

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:AUTOMATION_RULE_UPDATE_STARTED', this._on_rule_item_updating, this);
            Kurobox.socket.on('socket:AUTOMATION_RULE_UPDATED', this._on_rule_item_updated, this);
            Kurobox.socket.start();
        },

        start: function() {
            console.log('start!!!!!!!!!!!!!!!!!!!!');
        },

        destroy: function() {
            // clear collection
            delete this.collection;
            $('.device-list').infinitescroll('destroy');
            this.$el.find('.device-list').empty()
        },

        destroy_sockets: function() {
            // clear socket
            Kurobox.socket.off('socket:AUTOMATION_RULE_UPDATE_STARTED', this._on_rule_item_updating, this);
            Kurobox.socket.off('socket:AUTOMATION_RULE_UPDATED', this._on_rule_item_updated, this);
        },

        show: function() {
            $(this.el).show();
        },

        hide: function() {
            $(this.el).hide();
        },

        is_empty: function() {
            return this.$el.find('.device-list').text() === '';
        },

        is_list_empty: function() {
            if (this.collection !== undefined) {
                return this.collection.length === 0;
            }
            return;
        },

        is_item_disabled: function(id) {
            var $e = this.$('.rule-itm[data-id="'+id+'"]');
            return $e.hasClass('disabled');
        },

        render: function() {
            this.$el.hide();
        	$(this.el).html(this.template());
            $('#main-container').addClass('container');
           // $(this.el).addClass('centerFlex');
        	return this;
        },

        on_user_error_retry: function() {
            this.$('.device-list').text('');
            this.retrieve_rule();
        },

        retrieve_rule: function(startIdx, total) {
            console.log('retrieve_rule');
            if (this.is_empty()) {
                this.$('#device-list').infinitescroll('destroy');
                this.$('#device-list').data('infinitescroll', null);
                this.$('#device-list').empty();
            }
            this.begin_scroller();
            $('#device-list').infinitescroll('retrieve');
        },

        get_model: function(uid) {
        },

        trigger_action: function(action, uid) {
            switch(action) {
                case 'remove':
                this.remove_rule(uid);
                break;
                case 'enable':
                case 'disable':
                this.change_rule_status(action, uid);
                break;
                case 'options':
                this.trigger_options(uid)
                break;

                case 'execute':
                this.collection.get(uid).execute();
                break;
            }
        },

        on_device_option:function(evt) {
            var did = $(evt.currentTarget).parent().parent().data('id');
            window.location = hashTag+'/options/'+did;
        },

        on_device_action: function(evt) {
            var did = $(evt.currentTarget).parent().data('ref_id');
            var act = $(evt.currentTarget).data('action'); 

            switch (act) {
                case 'status':
                    var model = this.collection.get(did);

                    if(model.get('enabled')){
                        window.location = hashTag+'/disable/'+did;
                    } else {
                        window.location = hashTag+'/enable/'+did;
                    }
                break;
                case 'edit':
                case 'enable':
                case 'remove':
                    window.location = (hashTag+'/'+act+'/' + did);
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
            if (this.collection !== undefined) {

                var model = this.collection.get(did);
                console.log('pointing @', did, model);
                //switch icon and label
                var optionBtn = $('#option-button[data-action=status]');
                if(model.get('enabled') == true){
                    optionBtn.attr('class', 'icon-option-disable');
                    optionBtn.find('p').text('disable');
                }else{
                    optionBtn.attr('class', 'icon-option-enable');
                    optionBtn.find('p').text('enable');
                }
                $('#device-option-modal #option-buttons').data('ref_id', did);

                // show hide element
                $('#option-dark').show();
                //$('#device-list').attr('class', 'device-list blur');
                $('#device-list').attr('class', 'device-list');
                $('#device-option-modal:hidden').slideToggle();
            } else {
                window.location.replace('#/rule');
            }
        },

        hide_options: function() {
            console.log('hide_options')
            $('#option-dark').hide();
            //$('#device-list').attr('class', 'device-list not-blur');
            $('#device-list').attr('class', 'device-list');
            $('#device-option-modal:not(:hidden)').slideToggle();
            //$('#device-list').removeClass('not-blur');
        },

        change_rule_status: function(status, uid) {
            console.log('change_rule_status', status, uid);
            
            var model = this.collection.get(uid);

            // change status of item 
            var itemEl =  this.$('.rule-itm[data-id="' + uid + '"]');

            model.set_enable(status === 'enable')
            
            console.log('----<>', itemEl)
            if(status === 'disable'){
                itemEl.addClass('disabled');
            } else {
                itemEl.removeClass('disabled');
            }
        },

        remove_rule: function(uid) {
            // call unpair device api
            var model = this.collection.get(uid);
            this.collection.remove(model);

            if (this.collection.length === 0) {
                // no more rules to show
                
                // show empty template
                this.show_empty_template();

                // reset edit button
            } else {
                // remove from item
                var itemEl =  $('.rule-itm[data-id="' + uid + '"]');
                itemEl.remove();

                // check if item at the bottom is empty
                this.invalidateViewElement($('#next'));
            }


            // replace history
            location.replace(hashTag);
        },

        begin_scroller: function() {
            $('#device-list').infinitescroll({
                navSelector     : 'a#next:last',
                nextSelector    : 'a#next:last',
                itemSelector    : '#device-list',
                debug           : false,
                maxPage         : undefined,
                dataType        : 'json',
                appendCallback  : false,
                state           : {currPage:-1, isDestroyed: false, isDone:false},
                loading: {
                    finishedMsg: '',
                    img: "data:image/gif;base64,R0lGODlhAQABAHAAACH5BAUAAAAALAAAAAABAAEAAAICRAEAOw==",
                    msgText: '',
                },
                errorCallback   : function () {
                   this.collection = new Device.collection();

                   console.log('-- error callback!!!!', this.arguments)
                   
                   this.terminate_scroller();

                   // global error
                   Shell.handle_global_error({
                        error: {
                            code: -1
                        },
                        ajax: {
                            textStatus: '',
                            jqXHR: {responseText: ''}
                        }
                   })

                   this.show_list_error();

                   this._ignore_socket_event = false;
                }.bind(this),
                path: function(pageNum) {
                    // ignore socket event
                    this._ignore_socket_event = true;

                    // in the meanwhile, fix loader in center
                    $('#infscr-loading').css('text-align', 'center');
                    $('#infscr-loading').css('height', '0px');
                    
                    console.log('pageNum: '+pageNum);
                    var param = {
                        app_id: Kurobox.app_id,
                        method: 'list_rules',
                        limit: itemSize,
                        offset: (pageNum*itemSize)
                    };

                    console.log('request list', Kurobox.host+'/cgi-bin/syb_reqresp_cgi?'+$.param(param))
                    return Kurobox.host+'/cgi-bin/syb_reqresp_cgi?'+$.param(param);
                }.bind(this)
            }, function(response, options){ //callback
                if (this.collection === undefined) {
                    this.collection = new Device.collection();
                }

                if (response.theKuroBox.returnValue === 100) {

                    var outputCollection = new Device.collection();
                    outputCollection.add(outputCollection.parse(response.theKuroBox.response.data));

                    // remove previous spacer
                    $('#device-list > #list-spacer').remove();

                    if (outputCollection.length <= 0) {
                        this.terminate_scroller();

                        this.dataLength = 0;

                        if (this.collection.length <= 0) {
                            this.show_empty_template();
                        }
                    } else {
                        this.collection.add(outputCollection.models);

                        outputCollection.each(function(model){
                            this._create_new_item(model);
                        }.bind(this))

                        this.dataLength = response.theKuroBox.response.totalCount;
                        
                        console.log('-- test length', this.collection.length, response.theKuroBox.response.totalCount)
                        if (this.collection.length >= response.theKuroBox.response.totalCount) {
                            this.terminate_scroller();
                        } else {
                            // resume back
                            if (options.state.isPaused) {
                                this.$('#device-list').infinitescroll('resume');
                            }
                        }

                    }

                    $('#device-list').append(listSpacer);
                } else {
                    this.$('#device-list').infinitescroll('pause');

                    // global error
                    Shell.handle_global_error({
                        error: {
                            code: response.theKuroBox.returnValue,
                            message: response.theKuroBox.returnMessage
                        },
                        ajax: {
                            textStatus: '',
                        }
                    }, function() {
                        switch (response.theKuroBox.returnValue) {
                            case 401:
                            case 403:
                            case 405:
                                // login expired; redirect to login
                                window.location = '/system/?callback='+encodeURIComponent('/system/myapp');
                                break;
                        }
                    })

                    console.log('--- api error')

                    // show error
                    this.show_list_error(response.theKuroBox.returnMessage+' ['+response.theKuroBox.returnValue+']');
                }

                this._ignore_socket_event = false;
                this.trigger('list_retrieved');
            }.bind(this));
        },

        show_list_error: function(error_ref) {
            this.$('#device-list').html(this.list_error_msg({
                reference: error_ref || ''
            }));
        },

        terminate_scroller: function() {
            $('#device-list').infinitescroll('pause');
            // $.removeData(this.$('#device-list'));
        },

        _create_new_item: function(model) {
            var attr_obj = {
                'data-id': model.id,
                'class': 'rule-itm',
                'touch':'true'
            }

            if (!model.get('enabled')) {
                // assume it's not enabled
                attr_obj.class += ' disabled';
            }

            $('.device-list').append($('<div>', attr_obj).html(
                this.item_template({
                    model: model, 
                })
            ));
        },

        show_empty_template: function() {
            // assume there's not device paired
            // show tutorial
            $('.device-list').html(this.empty_device_tmpl());
            // $('.device-list').infinitescroll('destroy');
        },

        user_execute_rule: function(e) {
            var $e = $(e.currentTarget);
            var $parent = $e.parent();
            if (!$parent.hasClass('disabled')) {
                this.trigger('execute', this.collection.get($parent.data('id')))
            }
        },

        invalidateViewElement:function (elem)
        {
            var docViewTop = $(window).scrollTop();
            var docViewBottom = docViewTop + $(window).height();

            var elemTop = $(elem).offset().top;
            var elemBottom = elemTop + $(elem).height();

            return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
        },

        _on_rule_item_updating: function(data) {
            if (!this._ignore_socket_event) {
                try {
                    var $itm_el = this.$('.rule-itm[data-id="'+data.ruleId+'"]');
                    $itm_el.find('.rule-row').unbind('click');
                    $itm_el.addClass('disabled update');
                } catch (e) {
                    // assume it's creating a new one
                    // console.error('updating error', e)
                }

            }
        },

        _on_rule_item_updated: function(data) {
            if (!this._ignore_socket_event) {
                if (this.collection.length === 0) {
                    // remove no rule message
                    this.$('#device-list').html('');
                }
                var m = new Device.model({response:data}, {parse:true});
                if (this.collection.get(data.ruleId) === undefined) {
                    if (this.$('#device-list').data('infinitescroll').options.state.isPaused) {
                        console.log('-- added new rule')
                        // assume the scroller has being killed

                        // new rule
                        this.collection.add(m);

                        // remove previous spacer
                        this.$('#device-list > #list-spacer').remove();

                        // add to ui
                        this._create_new_item(this.collection.get(data.ruleId));

                        // add back spacer
                        this.$('#device-list').append(listSpacer);
                    }

                } else {
                    // update rule
                    this.collection.add(m, {merge: true, remove: false});
                    
                    var $itm_el = this.$('.rule-itm[data-id="'+data.ruleId+'"]');

                    // remove update class
                    $itm_el.removeClass('disabled update');

                    // add back status
                    if (!m.get('enabled')) {
                        // assume its not active
                        $itm_el.addClass('disabled');
                    }

                    // update ui
                    $itm_el.html(this.item_template({
                        model: this.collection.get(data.ruleId),
                    }));
                    // bind back mouse event
                    $itm_el.bind('click', this.user_execute_rule.bind(this));
                }

            }
        },
    });

    return ModuleRuleListView;
});
