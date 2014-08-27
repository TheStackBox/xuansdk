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
    'views/module.pairing.abstract',
    'templates',
    'Kurobox'
], function ($, _, Abstract, JST) {
    'use strict';
    var s = Abstract.prototype;

    var OptionModel = Backbone.Model.extend({
        defaults:{
            label: '',
            value: ''
        },
        idAttribute: 'value'
    })

    var OptionCollection = Backbone.Collection.extend({model: OptionModel})

    var unitList = new OptionCollection([
        {label: '-', value: 0},
    	{label: '1', value: 1},
    	{label: '2', value: 2},
    	{label: '3', value: 3},
    	{label: '4', value: 4},
    	{label: '5', value: 5},
    	{label: '6', value: 6},
    	{label: '7', value: 7},
    	{label: '8', value: 8},
    	{label: '9', value: 9},
    	{label: '10', value: 10},
    	{label: '11', value: 11},
    	{label: '12', value: 12},
    	{label: '13', value: 13},
    	{label: '14', value: 14},
    	{label: '15', value: 15},
    	{label: '16', value: 16},
    ]);

    var houseList = new OptionCollection([
    	{label: 'A', value: 'A'},
    	{label: 'B', value: 'B'},
    	{label: 'C', value: 'C'},
    	{label: 'D', value: 'D'},
    	{label: 'E', value: 'E'},
    	{label: 'F', value: 'F'},
    	{label: 'G', value: 'G'},
    	{label: 'H', value: 'H'},
    	{label: 'I', value: 'I'},
    	{label: 'J', value: 'J'},
    	{label: 'K', value: 'K'},
    	{label: 'L', value: 'L'},
    	{label: 'M', value: 'M'},
    	{label: 'O', value: 'O'},
    	{label: 'P', value: 'P'},
    ]);
    return Abstract.extend({
    	template: JST['app/scripts/templates/module.pairing.x10.manual.ejs'],
        disable_template: JST['app/scripts/templates/module.pairing.x10.disable.ejs'],
    	option_tmpl: JST['app/scripts/templates/module.rule.options.ejs'],
        busy_msg: JST['app/scripts/templates/module.pairing.busy.ejs'],
    	events: {
    		'click #unit': 'on_user_select_unit',
    		'click #house': 'on_user_select_unit',
    		'click #pair-btn': 'register_device',
    		'click #option-label': 'user_select_option',
    		'click #exit-options': 'on_user_close_prompt',
    	},
    	initialize: function() {
            console.warn('TODO: add history.back to cancel option list');
    		Kurobox.socket.verbose = true;

    		s.initialize.call(this);
    		this.paired_device = new this.collection.model({protocolId: this.options.protocol});

            Kurobox.socket.on('socket:PAIR_DEVICE', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    // the device has being paired with system

                    // hide please wait
                    this.options.parent.hide_dark();

                    var res = data.response;
                    this.paired_device.set('id', res.pairedDeviceId);

                    this.clear_socket_events();

                    this.trigger('paired')
                }
            }, this);
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_UNKNOWN', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    console.error('pair device socket error', data);

                    // hide please wait
                    this.options.parent.hide_dark();

                    // scroll to top
                    $('body').scrollTop(0);

                    this.show_generic_error();
                }
            }, this);
            Kurobox.socket.on('socket:PAIR_DEVICE_ERROR_EXIST', function(data) {
                if (data.parameter.protocolId == this.options.protocol) {
                    this.$('#x10-exist').fadeIn('fast');
                    this.$('#dark-x10').show();

                    // hide please wait
                    this.options.parent.hide_dark();

                    // scroll to top
                    $('body').scrollTop(0);

                    this.clear_socket_events();
                }
            }, this);
    	},

        destroy: function() {
            this.clear_socket_events();
            s.destroy.call(this);
        },

    	device_model: function() {
    		return this.paired_device;
    	},

    	on_user_select_unit: function(e) {
    		var $e = $(e.currentTarget);
            var title = this.$( '#title-'+$e.prop('id') ).text();
    		this.$('.x10-instruction').hide();
    		this.selected_option = $e.prop('id');
    		this.generate_options_list(this.$('#x10-opt-list'), eval($e.prop('id')+'List'), $e.data('value'), title);

            // scroll to top
            $('body').scrollTop(0);
    	},

    	generate_options_list: function($el_li, list, selected_value, title) {
            this._overriding_nav(title);

    		$el_li.html(this.option_tmpl({options: list, selected_option: selected_value}));
    		$el_li.show();
    	},

    	user_select_option: function(e) {
            var $e = $(e.currentTarget);
            var $ui_update = this.$('#'+this.selected_option);
            var label = $e.text();
            $ui_update.text(label);
            $ui_update.data('value', $e.data('value'));

            this.close_option_list();
        },

        close_option_list: function() {
            this.$('#x10-opt-list').empty().hide();
            this.$('.x10-instruction').show();

            // restore nav config
            this._restore_nav();
        },

        register_device: function(e) {
            // show message
            this.options.parent.show_dark(this.busy_msg({no_ok_btn:true}));

            // scroll to top
            $('body').scrollTop(0);

            this.pair_config_device();
        },

        pair_config_device: function() {
            var unit = this.$('#unit').data('value');
            if (unit == '0') {
                unit = '1';
            }
            this.paired_device.pair({
                error: function(model, resp) {
                    console.error('Unable to set pair device', resp)
                    this.show_generic_error();
                }.bind(this)
            }, this.$('#house').data('value')+unit)
        },

        show_generic_error: function() {
        	this.$('#x10-pair-failed').fadeIn('fast');
        	this.$('#dark-x10').show();
        	this.clear_socket_events();
        },

        on_user_close_prompt: function() {
            this.$('#x10-pair-failed').hide();
        	this.$('#x10-exist').hide();
        	this.$('#dark-x10').fadeOut('fast');
        },

        clear_socket_events: function() {
            Kurobox.socket.off('socket:PAIR_DEVICE');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_UNKNOWN');
            Kurobox.socket.off('socket:PAIR_DEVICE_ERROR_EXIST');
        },

        _overriding_nav: function(title) {
            // save previous setting
            this.ori_nav_config = {};
            this.ori_nav_config.callback = Shell.nav.callback;
            this.ori_nav_config.title = Shell.nav.$('#nav-title').text();

            Shell.nav.callback = this._on_nav_callback.bind(this);
            Shell.nav.update_title(title);
        },

        _restore_nav: function() {
            Shell.nav.callback = this.ori_nav_config.callback;
            Shell.nav.update_title(this.ori_nav_config.title);
        },

        _on_nav_callback: function(value, nav) {
            switch (value) {
                case nav.BACK:
                    this.close_option_list();
                    break;
            }
        }
    })
});