define([
    'jquery',
    'underscore',
    'backbone',
    'templates',
    'models/rule.device-type',
    'models/rule.device',
    'utils/common.utils'
], function ($, _, Backbone, JST, RuleDeviceType, RuleDevice, CommonUtils) {
	'use strict';

	var SERVICES = [
		'service_mail',
		'service-twitter',
		'service-weather'
	]

	var util = new CommonUtils();

	return Backbone.View.extend({
		type_tmpl: JST['app/scripts/templates/module.rule.add.device_type_list.ejs'],
		no_devices: JST['app/scripts/templates/module.rule.add.no_device.ejs'],
		header_content: JST['app/scripts/templates/module.rule.device-explorer.header.ejs'],
        header_template: JST['app/scripts/templates/module.rule.grey-header.ejs'],
        pop_message: JST['app/scripts/templates/prompt.pop.ejs'],
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
		},
		close: function() {
			this.type_collection.destroy();
			this.device_collection.destroy();
			this.$el.hide();
		},
		list_type: function(section) {
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
		},
		list_device: function(section, group, group_name) {

			if (this.$el.is(':hidden')) this.$el.show();

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
								subtitle: 'Which %%name%%'.replace('%%name%%', this.device_collection.group.get('label')),
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
					var acknowledged_action = function() {
						Shell.hide_pop_message();
						this.delegateEvents();
					}.bind(this)

					var $prompt_content = Shell.show_pop_message(this.pop_message({
						title: '',
                        message: 'error_service_setup_remote_access_denied',
                        ok_btn_label: 'Ok',
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
			window.history.back();
		},
	});
});