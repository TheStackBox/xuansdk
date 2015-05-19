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
    'views/scene.list',
    'models/scene',
    'common/views/option-pane',
    'views/scene.list.filter',
    'views/scene.editor',
    'views/scene.feedback',
], function ($, _, Backbone, JST, SceneItemListFactory, SceneData, OptionPane, SceneListFilterOptionView, SceneEditor, SceneFeedback) {
    'use strict';

    var SceneMainView = Backbone.View.extend({
    	template: JST['app/scripts/templates/scene.ejs'],
        list_item_template: JST['app/scripts/templates/scene.item.list.ejs'],
        empty_list_template: JST['app/scripts/templates/scene.item.list.empty.ejs'],
        error_list_template: JST['app/scripts/templates/scene.item.list.error.ejs'],
        prompt_template: JST['app/scripts/common/templates/prompt.pop.ejs'],
        events: {
            'click #filter-option-btn': 'trigger_filter_list',
            // 'click #add-btn': 'navigate_scene_editor',
            'click .empty-list #retry-btn': 'refresh_list'
        },

    	initialize: function() {
    		// init list view
            this.option_pane = new OptionPane();
    	},

    	destroy: function() {
            if (this.list_view != undefined) this.list_view.destroy();
    		if (this.filter_list != undefined) this.filter_list.destroy();
            if (this.option_pane != undefined) this.option_pane.destroy();

            this.destroy_feedback();
            this.destroy_editor();
            this.disable_item_update_socket();

    		this.undelegateEvents();
    		this.$el.empty();
    	},

    	render: function() {

    		// templating
    		$(this.el).html(this.template());
            
            this.invalidate_nav_bar({
            	left: ['NAV_HOME'],
            	title: lang.translate('scene')
            });

        	// registering element
        	this.list_view = new SceneItemListFactory({el: this.$('#scene-list')});

            // prepare option pane
            this.option_pane.close();
            this.option_pane.on('close', this.on_option_pane_closed, this);

            // prepare filter view
            this.filter_list = new SceneListFilterOptionView({el: this.$('#filter-option')}) ;
            this.filter_list.on('open', this.on_filter_open, this);
            this.filter_list.on('close', this.on_filter_close, this);
            this.filter_list.on('select', this.on_filter_item_select, this);

            // remove container class in #main-container
            if ($('#main-container').hasClass('container')) {
                $('#main-container').removeClass('container');
            }

            this.trigger('page.rendered', this);

        	return this;
    	},

    	navigate: function(section, uid, action, queryObj) {
            // reset popup
            if (!Shell.$('#shell-pop-content').is(':empty') && 
                action != 'delete') {
                this._returnBlackShade = function() {};
                if (section === 'item') {
                    // navigate to item
                    // @NOTE: return shell dark if there's API CALLING
                    // as error message required shell dark!
                    this._returnBlackShade = function() {
                        if (!Shell.$('#shell-dark-content').is(':empty') || !Shell.$('#shell-pop-content').is(':empty')) {
                            Shell.$('#shell-dark').show();
                        }
                    }.bind(this);
                }
                Shell.hide_pop_message(this._returnBlackShade);
            }

    		if (section === undefined) {
    			// redirect to favourite if not sorting is avail
    			window.location = '#/scene/location/all'
                return;
    		}

            var nav_setting = {};
            nav_setting.right = [];
            nav_setting.callback = function() {};

            this.section = section;

    		switch (section) {
    			case 'location':
                // show scene list page
                // destroy editor page
                this.destroy_editor();

                // destroy feedback
                this.destroy_feedback();

                    // restore back nav bar
                    nav_setting.title = 'my_scene';
                    nav_setting.left = ['NAV_HOME'];
                    nav_setting.right = ['ADD_RULE'];
                    nav_setting.callback = this.on_user_interact_scene_list_nav.bind(this)

                // enable socket
                this.enable_item_update_socket();

                this.$('.scene-list-page').show();

                if (this.list_view.data == undefined) {
                    
                    // render filter list
                    // this.filter_list.render();

                    this.list_view.render(this.list_item_template.bind(this), this.empty_list_template);
                    this.list_view.on('option', this.on_user_want_to_do_something, this);
                    this.list_view.on('data_error', this.on_list_failed, this);
	    		}	
                
    			if (this.list_view.data == undefined || this._locationId != uid) {
                    this._locationId = uid;

                    var options = {};

                    // getting list from api
                    var type = 'location';
                    var id = uid

                    if (id == 'all') {
                        type = undefined;
                        id = undefined;
                    }
                    options.list_params = [type, id];
                    this.list_view.list(new SceneData(), options);
                }
    			break;

                case 'item':
                this.disable_item_update_socket();
                    this.destroy_feedback();

                if (uid != "new" && action != "edit") {
                    if (this.list_view.data != undefined) {
                        // assume data is available
                        this.determine_scene_action(action, uid, queryObj);
                    } else {
                        window.location = "#/scene/location/all";
                    }
                } else {
                    // create new scene
                    this.determine_scene_action(action, uid, queryObj);

                    // update nav config
                    nav_setting.title = 'add_scene';
                }
                break;
                    this.destroy_editor();

                case 'feedback':
                this.disable_item_update_socket();
                this.destroy_editor();

                // remove option pane
                this.option_pane.close();

                nav_setting.title = 'scene_feedback';
                nav_setting.left = ['BACK'];
                // query.serId will be used, instead of uid
                this.manage_feedback(queryObj);
                break;

    			default:
    			console.log('Unknown section', section);
    			break;
    		}

    		this.invalidate_nav_bar(nav_setting);
    	},

    	invalidate_nav_bar: function(nav){
    		// update buttons and its callback
    		if (nav.left !== undefined || nav.right !== undefined || nav.callback !== undefined) {
            	this.options.nav.update_buttons(nav.left, nav.right, nav.callback);
    		}
    		// update title
            if (nav.title !== undefined) this.options.nav.update_title(nav.title);
        },

        on_list_failed: function(error) {
            if (this.list_view.data.length == 0) {
                var o = {reference: ''};
                if (error.error.code != -1) {
                    o.reference = error.error.code+' ['+error.error.message+']'
                }
                this.list_view.$el.html(this.error_list_template(o));
            }
        },

        refresh_list: function(e) {
            var lid = this._locationId;
            this._locationId = undefined;

            var hash = window.location.hash.split('/');
            this.navigate('location', hash[2], lid);
        },

        on_user_want_to_do_something: function(e) {
        	// trigger options
            var $e = $(e.currentTarget);
            this.determine_scene_action('option', $e.data('id'));
        },

        determine_scene_action: function(action, uid, query) {
            console.log('param', action, uid)
            var item;
            if (uid != 'new') {
                if (this.list_view == undefined || this.list_view.data == undefined) {
                    window.location.href = '#/scene/location/all';
                    return;
                }
                item = this.list_view.data.get(uid);
            }

            switch (action) {
                case 'execute':
                // get user confirmation
                this.on_execute_item(item);
                break;

                case 'option':
                // trigger options pane
                this.on_option_pane_open(item);
                break;

                case 'edit':
                // going editor
                if (this.scene_editor != undefined) {
                    console.log('---- nav scene editor')
                    // editor is initialise
                    this.scene_editor.navigate(query);
                    console.log('navigating scene editor', query);
                } else {
                    var begin_init_editor = function(scene_model) {
                        // hide scene list
                        this.$('.scene-list-page').hide();

                        this.initialize_editor(scene_model, query);

                        _.defer(function() {
                            this.trigger('page.idle');
                        }.bind(this))
                    }.bind(this)

                    if (item != undefined) {
                        // edit scene
                        console.warn('TODO: get scene info')
                        console.warn('TODO: pass navigation query')

                        item.load_detail(null, {
                            success: function() {
                                // override return shell dark
                                this._returnBlackShade = function() {}

                                begin_init_editor(item);
                            }.bind(this),
                            error: function() {
                                // fallback
                                window.history.back();
                            }.bind(this)
                        });
                    } else {
                        // create scene
                        begin_init_editor(new SceneData.model());
                        this.scene_editor.navigate(query);
                    }
                }
                break;

                case 'delete':
                if (item != undefined) {
                    // prompt user for confirmation
                    this.on_user_delete_scene_item(item);
                } else {
                    // assume the item is not available
                    window.history.back();
                }
                break;

                default:
                console.warn('Unregistered action',action);
                break;
            }
        },

        on_execute_item: function(item) {
            // direct execute
            item.execute(window.location.pathname+'#/scene/feedback');
            // revert back
            window.history.back();
        },

        on_option_pane_open: function(item) {
            this.option_pane.render({
                    items: [
                        {
                            icon: 'edit',
                            title: 'edit',
                            url: '#/scene/item/'+item.id+'/edit'
                        },
                        {
                            icon: 'delete',
                            title: 'remove',
                            url: '#/scene/item/'+item.id+'/delete'
                        }
                    ]
                })
                // this.option_pane.open();
                var $shell = Shell.show_pop_message(
                    this.option_pane.el,
                    null,
                    this.on_option_pane_closed.bind(this)
                )
                
                // escape animation
                $shell.finish();
        },

        on_option_pane_closed: function() {
            this.option_pane.close();
            Shell.hide_pop_message();
        },

        trigger_filter_list: function() {
            this.filter_list.trigger_view()
        },

        on_filter_open: function() {
            console.log('this.filter option label', this.$('#filter-option-btn#indicator'))
            this.$('#filter-option-btn #indicator').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        },

        on_filter_close: function() {
            this.$('#filter-option-btn #indicator').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
        },

        on_filter_item_select: function(item, id) {
            window.location = '#/scene/location/'+id;
            this.filter_list.trigger_view()
        },

        navigate_scene_editor: function() {
            this._back_history = window.location.href;
            window.location = '#/scene/item/new/edit';
        },

        initialize_editor: function(scene_data, query) {
            console.error('---- init editor')
            Shell.nav.hide();

            this.scene_editor = new SceneEditor({model: scene_data});
            this.scene_editor.on('close', this.on_user_close_editor, this);
            this.scene_editor.on('save', this.on_user_save_scene, this);
            this.scene_editor.render();
            this.$el.append(this.scene_editor.$el);

            this.scene_editor.navigate(query);
        },

        destroy_editor: function() {
            if (this.scene_editor != undefined) {
                this.scene_editor.destroy();
                this.scene_editor = undefined;

                // bring back header
                Shell.nav.show();
            }
        },

        on_user_close_editor: function() {
            if (this._back_history != undefined) {
                window.location.href = this._back_history;
            } else {
                window.location = '#/scene';
            }
            this._back_history = undefined;
        },

        on_user_save_scene: function() {
            // scene has being saved, update list
            this._locationId = undefined;
        },

        on_user_delete_scene_item: function(item) {
            // prompt for confirmation
            var events = {
                'click #modal-cancel-btn': function() {
                    // revert back
                    window.history.back();
                }.bind(this),
                'click #modal-ok-btn': function() {
                    // invalidate passcode
                    // execute
                    item.remove();
                    window.history.back();
                }.bind(this)
            }
            Shell.show_pop_message(this.prompt_template({
                title: 'msg_scene_delete_title',
                message: 'msg_scene_delete',
                ok_btn: 'btn_remove'
            }),
            events, events['click #modal-cancel-btn']
            )
        },

        manage_feedback: function(queryObj) {
            if (this.scene_feedback == undefined) {
                this.scene_feedback = new SceneFeedback();
                this.scene_feedback.nav = this.options.nav;
                this.scene_feedback.on('init', this.on_feedback_init);
                this.scene_feedback.render();

                this.$el.append(this.scene_feedback.$el);
            }

            // clear other dom
            if (!this.$('.scene-list-page').is(':hidden')) this.$('.scene-list-page').hide();

            this.scene_feedback.navigate(queryObj);
        },

        destroy_feedback: function() {
            if (this.scene_feedback != undefined) {
                this.scene_feedback.destroy();
                this.scene_feedback = undefined;
            }
        },

        on_feedback_init: function() {
            this.$('.scene-list-page').hide()
        },

        enable_item_update_socket: function() {
            Kurobox.socket.on('socket:AUTOMATION_SCENE_DELETED', this.on_socket_item_deleted, this);
        },

        disable_item_update_socket: function() {
            Kurobox.socket.off('socket:AUTOMATION_SCENE_DELETED', this.on_socket_item_deleted, this);
        },

        on_socket_item_deleted: function(data) {
            this.list_view.data.each(function(scene_item, index) {
                if (scene_item.get('id') == data.sceneId) {
                    this.list_view.data.remove(scene_item, {silent: true});
                    this.list_view.reset();
                    this.list_view.invalidate();
                    return false;
                }
            }.bind(this))
        },

        on_user_interact_scene_list_nav: function(mode, nav) {
            switch (mode) {
                case nav.ADD_RULE:
                this.navigate_scene_editor();
                break;

                case nav.NAV_HOME:
                window.location = '/system/myapp';
                break;
            }
        }
    })

    return SceneMainView;

});
