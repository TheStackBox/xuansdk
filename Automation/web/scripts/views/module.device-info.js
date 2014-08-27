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
    'models/device',
    'models/device-type',
    'views/module.icon-chooser'
], function ($, _, Backbone, JST, Device, DeviceType, IconChooser) {
    'use strict';

    var ModuleDeviceInfoView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.device-info.ejs'],
        info_tmpl: JST['app/scripts/templates/module.device-info.info.ejs'],
        type_list_tmpl: JST['app/scripts/templates/module.device-info.type.ejs'],
        isOpened: false,
        events: {
        	'click #edit-icon': 'user_change_icon',
            'click #exit-options': 'user_has_changed_icon',
            'click #icon-picker-dark': 'user_has_changed_icon',
            'click #edit-type': 'user_change_type',
            'click #save-and-add-btn': 'save_and_add',
            'click #save-btn': 'save_and_close',
            'click #test-device-btn': 'test_device',
            'click .device-type-item': 'user_select_type',
            'click .section': 'toggle_desc',
            'blur #edit-name': 'user_change_name',
            'focus #edit-name': 'user_begin_change_name',
            'keyup #edit-name': 'validate_save_btn'
        },
        render: function() {
        	$(this.el).html(this.template());
        	$(this.el).hide();
            $('#main-container').addClass( "container" );
        	return this;
        },

        destroy:function () {
        },

        open: function(uid, button_config, callback, query) {
            console.log('query')
            this.callback = callback;
    
        	// config buttons
        	if (button_config !== undefined) {
                var totalBtn=0;
        		_.each(button_config, function(value, prop) {
        			prop = '#'+prop;
        			if (value === true) {
        				$(prop).show();
                        totalBtn++;
                       
        			} else {
        				$(prop).hide();
        			}
        		});


                // calulate total btn to assign a proper btn css
                $('#action-btn').addClass('btn-'+totalBtn+'-stretch');
        	}

        	// retrieve more detail
        	this.model = new Device.model();
        	this.model.fetch(uid, {
        		success: function() {
                    console.log('device data', this.model.attributes);
        			$('#info-container').html(this.info_tmpl(this.model.attributes));
        			$(this.el).show();
                    this.isOpened = true;
        		}.bind(this),
        		error: function(model, resp, options) {
        			console.error('failed', resp);
        		}.bind(this)
        	})
        },
        update_action: function(query) {
            if (query !== null && query !== undefined) {
                if (query.action !== null && query.action !== undefined) {
                    switch (query.action) {
                        case 'select-icon':
                        // show prompt
                        if (this.icon_chooser === undefined) {
                            this.icon_chooser = new IconChooser({data_url:'json/icon-list.json'});
                            this.icon_chooser.on('select', this.user_has_changed_icon, this);
                            this.icon_chooser.render();
                            console.log('user_change_icon');
                            $('#icon-picker').append(this.icon_chooser.el);
                        }

                        $('#icon-picker-dark').show();
                        $('.icon-picker-pane:hidden').slideToggle();
                        break;
                    }
                }
                
            } else {
                // assume no query
                if (this.icon_chooser !== undefined) {
                    $('#icon-picker-dark').hide();
                    $('.icon-picker-pane:not(:hidden)').slideToggle();
                }
                $('#type-list-container').hide();
                $('#info-page').show();                         
            }
        },
        close: function() {
            delete this.model;
        	$(this.el).hide();
        	$('#info-container').empty();
            this.isOpened = false;
        },

        save_and_close: function() {
            if(this.$('#save-btn').hasClass('disabled')){
                console.log('Not allow to save');
            }else{
                this.model.save({success: function() {
                    this.trigger('close', true);
                }.bind(this),
                error: function(m,r,o) {
                    console.error('Failed to save device', r);
                    this.trigger('close', false);
                }.bind(this)});
            }
        },
        save_and_add: function() {
            if(this.$('#save-and-add-btn').hasClass('disabled')){
                console.log('Not allow to save');
            }else{
            	this.model.save({success: function() {
                    if (typeof this.callback === 'function') {
                        this.callback();
                    } else {
                        //window.location = this.callback;
                        //location.replace(this.callback);
                        window.history.back();
                    }
            	}.bind(this)});
            }
        },
        test_device: function() {
        	this.model.test();
        },
        user_change_type: function(evt) {
            window.location += '?action=change-type';
            // retrieve type list
            this.type_list = new DeviceType.collection();
            this.type_list.fetch(this.model.get('protocolId'), {success: function() {
                $('body').scrollTop(0);
                $('#type-list-container').html(this.type_list_tmpl({collection: this.type_list, selected:$('#label-type').text()}));
                $('#type-list-container').show();
                $('#info-page').hide();
            }.bind(this),
            error: function(scope, resp, options) {
                console.error('error', resp.error);
            }});

        },
        user_select_type: function(evt) {
            // update model
            var $e = $(evt.currentTarget);
            this.model.set('typeId', $e.data('id'));

            $('#label-type').text($e.text());
            $('body').scrollTop(0);
            window.history.back();
        },
        user_begin_change_name: function() {
            this._pname = $('#edit-name').val();
            this.validate_save_btn();
        },
        user_change_name: function() {
            if (this._pname !== $('#edit-name').val()) {
                this.model.set('name', $('#edit-name').val());
            }
            this.validate_save_btn();
        },

        user_change_icon: function() {
            window.location += '?action=select-icon'
        },

        user_has_changed_icon: function(iconId) {
            if (typeof iconId === 'string') {
                // update model
                this.model.set('icon', iconId);
                // update view
                $('#preview-icon').attr('data-icon', iconId);
            }

            window.history.back();
        },

        validate_save_btn: function(){
            if($('#edit-name').val().length <= 0 ){
                $('#save-btn').addClass('disabled');
                $('#save-and-add-btn').addClass('disabled');
            }else{

                $('#save-btn').removeClass('disabled');
                $('#save-and-add-btn').removeClass('disabled');
            }
        },

        toggle_desc:function(){
            if(this.$('#desc').hasClass( "desc2" )){
                this.$('#desc').attr( "class", 'desc2-extend' );
            }else{
                 this.$('#desc').attr( "class", 'desc2' );
            }
            
        }

    });

    return ModuleDeviceInfoView;
});
