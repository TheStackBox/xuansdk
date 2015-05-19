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
define([
    'jquery',
    'underscore',
    'backbone',
    'templates',
    'models/categories',
    'models/rule.device-type',
    'models/rule.device',
    'utils/common.utils',
], function ($, _, Backbone, JST, CategoriesModel, RuleDeviceType, RuleDevice, CommonUtils) {
	'use strict';

	var SERVICES = [
		'service_mail',
		'service-twitter',
		'service-weather'
	]

	var util = new CommonUtils();

	return Backbone.View.extend({
		id: 'device_explorer',
		className: 'container',
		item_renderer: JST['app/scripts/templates/module.rule.device_explorer.item.ejs'],

		type_tmpl: JST['app/scripts/templates/module.rule.add.device_type_list.ejs'],
		no_devices: JST['app/scripts/templates/module.rule.add.no_device.ejs'],
		header_content: JST['app/scripts/templates/module.rule.device-explorer.header.ejs'],
        header_template: JST['app/scripts/common/templates/grey-header.ejs'],
        pop_message: JST['app/scripts/common/templates/prompt.pop.ejs'],
		events: {
			'click .rule-type-item': 'user_select_type',
			'click .rule-device-item': 'user_select_device',
			// 'click #exit-options': 'user_close_this',
			// 'click .nav-icon-back': 'user_navigate_back',
			'click #header #nav-back-btn': 'user_navigate_back'
		},
		initialize: function() {
			this.el = $(this.options.el);
			this.type_collection = new RuleDeviceType.collection();
			this.device_collection = new RuleDevice.collection();

			// listen to group events
			/*
			"AUTOMATION_GROUP_ADDED" - {"kbxGroupId":2, "kbxGroupParentId":1, "enabled":true}
			"AUTOMATION_GROUP_DELETED" - {"kbxGroupId":2, "kbxGroupParentId":1}
			"AUTOMATION_GROUP_UPDATED" - {"kbxGroupId":2, "kbxGroupParentId":1, "enabled":false}
			*/
			Kurobox.socket.verbose = true;
			Kurobox.socket.on('socket:AUTOMATION_GROUP_ADDED', this.on_device_added, this);
			Kurobox.socket.on('socket:AUTOMATION_GROUP_DELETED', this.on_device_deleted, this);
			// Kurobox.socket.on('socket:AUTOMATION_GROUP_UPDATED', this.on_device_updated, this);
			if (!Kurobox.socket.connected) {
				Kurobox.socket.start();
			}
		},
		render: function() {
			// @NOTE: render will cause existing events reset
			// used this class as item renderer and data retriever
			this.events = {
				'click .device-explorer': 'user_select_item',
			}
			this.undelegateEvents();
			this.delegateEvents();
		},
		destroy: function() {
			this.close();

			// close group event
			Kurobox.socket.off('socket:AUTOMATION_GROUP_ADDED', this.on_device_added, this);
			Kurobox.socket.off('socket:AUTOMATION_GROUP_DELETED', this.on_device_deleted, this);
			// Kurobox.socket.off('socket:AUTOMATION_GROUP_UPDATED', this.on_device_updated, this);
			// Kurobox.socket.stop();
			
			this.$el.remove();
		},
		close: function() {
			this.type_collection.destroy();
			this.device_collection.destroy();
			this.$el.hide();

		},
		navigate: function(options) {
			console.log('navigating...', options);
			if (this.$el.is(':hidden')) this.$el.show();

			if (this.collection == undefined) {
				// this.collection = new CategoriesModel();
				this.collection = new RuleDevice.collection();
			}
			// var locationId = options.locationId, 
				// parentGroupId = options.parentGroupId

			// assume to retrieve
			this.collection.fetch(options.section || 'then', options.parentGroupId || undefined, {
			// this.collection.fetch(options.filter, locationId, parentGroupId, {
				success: function() {
					// render view

					this.render_list(this.collection, options.filter);
					// this.$('#content').html(this.type_tmpl({collection: this.collection, type:'device'}));

				}.bind(this),
				error: function() {
					window.history.back();
				}.bind(this)
			})
		},

		render_list: function(collection, filters) {
			
			this.$el.empty();

			collection.each(function(model) {
				switch (model.constructor) {
					case RuleDevice.model:
					this.$el.append(this.item_renderer({
						id: model.id,
						type: 'device',
						icon: model.get('icon'),
						label: model.get('name'),
						desc: model.get('extra_info').zoneName || model.get('description')
					}))
					break;
				}
			}.bind(this))
		},

		user_select_item: function(e) {
			var $e = $(e.currentTarget);
			var model = this.collection.get($e.data('id'))
			this.trigger('select', model, e);
		},

		// =============================================================
			// deplicating methods
		// =============================================================
		list_type: function(section) {
			console.warn('deplicated!!!!')

			this.parent_id = undefined;

			if (this.$el.is(':hidden')) this.$el.show();

			// clear content
			this.el.find('#content').empty();

			this.section = section;
			this.trigger('busy');
			if (this.el.is(':hidden')) this.el.slideToggle();

			this.el.find('#title').text((this.section === 'if') ? 'if_dot' : 'then_dot');
			this.el.find('#caption').text('choose_type');

			switch (this.section) {
				case 'if':
				case 'then':
				// retriving device type that support IF statement
				this.type_collection.fetch(this.section, {
					success: function() {
						// add header
						var subtitle = (this.section === 'if') ?
							'rule_if_device_explorer_instruction' :
							'rule_then_device_explorer_instruction';
						var desc = (this.section === 'if') ?
							'rule_if_device_explorer_instruction_desc' :
							'rule_then_device_explorer_instruction_desc';

							console.log(subtitle)
						this.el.find('#header').html(this.header_template({
							content: this.header_content({
								title: this.section.toUpperCase(),
								subtitle: subtitle,
								description: desc
							})
						}))

						// add spacer
						// this.el.find('#content').append(util.render_spacer(this.el.find('#header .top-bar-thick')));

						if (this.type_collection.length > 0) {
							// templating over the ui
							this.el.find('#content').append(this.type_tmpl({
								collection: this.type_collection, 
								type: 'type'
							}));
						} else {
							this.el.find('#content').append(this.no_devices());
						}
						this.trigger('idle');
					}.bind(this),
					error: function() {
						throw 'Unable to fetch device type list';
						this.trigger('idle');
					}.bind(this)
				});
				break;
			}

			this._return_function = function() {
				window.location = this.options.base_url;
			}.bind(this);
		},
		list_device: function(section, group, group_name) {

			if (section !== undefined) {
				this._section = section;
			} else {
				section = this._section;
			}
			if (group !== undefined) {
				this._group = group;
			} else {
				group = this._group;
			}

			if (group_name !== undefined) {
				this._group_name = group_name;	
			} else {
				group_name = this._group_name;
			}

			this.parent_id = group;

			if (this.$el.is(':hidden')) this.$el.show();

			// save top
			var _top = $('body').scrollTop();
			console.log('_top', _top);

			// clear content
			this.el.find('#content').empty();
			
			this.section = section;
			this.trigger('busy');
			if (this.el.is(':hidden')) this.el.slideToggle();

			this.el.find('#title').text(group_name.toUpperCase());
			this.el.find('#caption').text('choose_device');

			switch(this.section) {
				case 'if':
				case 'then':
				this.device_collection.fetch(this.section, group, {
					success: function() {
						// render header
						this.el.find('#header').html(this.header_template({
							content: this.header_content({
								title: this.section.toUpperCase(),
								subtitle: 'select_a_device',
								description: this.device_collection.group.get('description') || '',
							})
						}))

						// add spacer
						// this.el.find('#content').append(util.render_spacer(this.el.find('#header')));

						if (this.device_collection.length > 0) {
							// templating over the ui
							this.el.find('#content').html(this.type_tmpl({collection: this.device_collection, type:'device'}));
						} else {
							this.el.find('#content').html(this.no_devices());
						}

						_.defer(function() {
							$('body').scrollTop(_top);
						}.bind(this))
						// templating over the ui
						this.trigger('idle');
					}.bind(this),
					error: function() {
						throw 'Unable to fetch device list';
						this.trigger('idle');
					}.bind(this)
				});
				break;
			}

			this._return_function = function() {
				window.history.back();
			}
		},
		retrieve_device: function(did) {
			this.device_collection = new RuleDevice.collection();
			var device = RuleDevice.model();
			device.fetch({
				
			})
		},
		user_select_type: function(e) {
			var $e = $(e.currentTarget);
			window.location=this.options.base_url+'?section='+this.section+'&action=list-devices&group='+$e.data('id')+'&name='+$(e.currentTarget).find('#item-label').text();
		},
		user_select_device: function(e) {
			var $e = $(e.currentTarget);
			var device = this.device_collection.get($e.data('id'));

			var acknowledged_action = function() {
				Shell.hide_pop_message();
				this.delegateEvents();
			}.bind(this)

			// deleted?
			if (device.get('deleted')) {
				var $prompt_content = Shell.show_pop_message(this.pop_message({
					title: '',
                    message: 'msg_rule_device_explorer_device_delete_access_denied',
                    ok_btn_label: 'btn_ok',
                    cancel_btn_label: ''
				}), {
					'click #modal-ok-btn': acknowledged_action
				}, acknowledged_action)

				// ask cancel button to fuck off
				$prompt_content.find('#modal-cancel-btn').hide();
				return;
			}

			if (typeof device.get('extra_info').kbxService !== 'undefined' && device.get('extra_info').kbxService.isRequireSetup === true) {
				this.undelegateEvents();

				if (window.location.host.indexOf('tunnel.thexuan.com') === -1) {
					// is in local area
					this.options.prompt_message(
						{
							message: 'error_service_setup_required',
							confirm_callback: function() {
								window.location = '/system/admin/#setup/'+SERVICES[device.get('extra_info').kbxService.serviceId];
							}.bind(this),
							cancel_callback: function() {
								this.options.prompt_message('hide');
								this.delegateEvents();
							}.bind(this)
						}
					);

				} else {
					// is on internet

					var $prompt_content = Shell.show_pop_message(this.pop_message({
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
			window.location = this.options.base_url+'?section='+this.section+'&action=select&did='+$e.data('id');

		},
		user_close_this: function(e) {
			window.location = this.options.base_url;
		},

		user_navigate_back: function(e) {
			this._return_function();
			// window.history.back();
		},

		on_device_added: function(data) {
			console.log('!!! device added', data)
			if (this.$('.rule-device-item').length > 0 && !this.el.is(':hidden')) {
				// update data
				//"AUTOMATION_GROUP_ADDED" - {"kbxGroupId":2, "kbxGroupParentId":1, "enabled":true}
				if (this.parent_id == data.kbxGroupParentId) {
					// prompt to refresh
					Shell.show_pop_message(this.pop_message({
						title: 'msg_rule_device_explorer_device_update_title',
                        message: 'msg_rule_device_explorer_device_add',
                        ok_btn_label: 'btn_ok',
                        cancel_btn_label: 'btn_cancel'
					}), {
						'click #modal-ok-btn': function() {
							// update the list

							// refetch data
							this.list_device();
							Shell.hide_pop_message();

						}.bind(this),
						'click #modal-cancel-btn': function() {
							// do nothing
							Shell.hide_pop_message();
						}.bind(this)
					})
				}
			}
		},

		on_device_deleted: function(data) {
			console.log('!!! device deleted', data)
			if (this.$('.rule-device-item').length > 0 && !this.el.is(':hidden')) {
				// update data
				//"AUTOMATION_GROUP_ADDED" - {"kbxGroupId":2, "kbxGroupParentId":1, "enabled":true}
				if (this.parent_id == data.kbxGroupParentId) {
					// prompt to refresh
					Shell.show_pop_message(this.pop_message({
						title: 'msg_rule_device_explorer_device_update_title',
                        message: 'msg_rule_device_explorer_device_deleted',
                        ok_btn_label: 'btn_ok',
                        cancel_btn_label: 'btn_cancel'
					}), {
						'click #modal-ok-btn': function() {
							// update the list

							// refetch data
							this.list_device();
							Shell.hide_pop_message();

						}.bind(this),
						'click #modal-cancel-btn': function() {
							// do nothing
							Shell.hide_pop_message();

							// exclaim the device
							this.$('.rule-device-item[data-id="'+data.kbxGroupId+'"] #item-label').addClass('error');

							// set deleted flag in data model
							this.device_collection.get(data.kbxGroupId).set('deleted', true);
						}.bind(this)
					})
				}
			}
		},

		on_device_updated: function(data) {
			console.log('!!! device updated', data)
			if (this.$('.rule-device-item').length > 0) {
				// check for data
				//"AUTOMATION_GROUP_UPDATED" - {"kbxGroupId":2, "kbxGroupParentId":1, "enabled":false}
				if (this.parent_id == data.kbxGroupParentId) {
					var dev = this.device_collection.get(data.kbxGroupId);
					if (dev) {
						// update data
						dev.set('enabled', data.enabled);
					}
				}
			}
		}
	});
});