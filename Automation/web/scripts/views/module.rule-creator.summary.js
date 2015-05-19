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
    'utils/common.utils'
], function ($, _, Backbone, JST, Utils) {
    'use strict';

    var spr = Backbone.View.prototype;
    var SummaryView = Backbone.View.extend({
    	summary_header_item: JST['app/scripts/templates/module.rule.device-rule-header.ejs'],
    	summary_item: JST['app/scripts/templates/module.rule.device-rule-item.ejs'],
    	initialize: function() {
    		this.utils = new Utils();

    		spr.initialize.apply(this, arguments)
    	},
    	render: function(data, uid, edit_mode) {
            if (this.$el.is(':empty')) {
                // empty...
        		if (data.length > 0) {

        			// clear all first
        			this.clear();

    	    		this.uid = uid || undefined;
    	    		this.collection = data;

    	    		// begin render template
    	    		var $container, $device_content, delete_device_url, delete_method_url, args, arg, desc;
    	    		this.collection.each(function(device) {

                        console.log('--- device', device);
    	    			// prepare container
    	    			$container = $('<div>', {id: device.get('id')}).appendTo(this.$el);

    	    			// header
    	    			delete_device_url = this.get_navigation_url()+'?section='+this.options.section+'&action=delete&id='+device.get('id');

    	    			$container.append(this.summary_header_item({
    	    				icon: device.get('icon'),
    	    				label: device.get('name'),
    	    				delete_url: delete_device_url,
                            is_error: (device.get('status') > 0),
                            edit_mode: edit_mode
    	    			}));

    	    			// content
    	    			$device_content = $('<div>', {'class': 'rule-action-container'}).appendTo($container);

                        if (device.get('status') !== 1) {
                            // assume device is still available
                            // determine if device stil enable
                            device.get('methods').each(function(method, index) {

                                args = method.get('ui_components');
                                if (args.length > 1) {
                                    var data = {};
                                    args.each(function(_arg) {
                                        if (_arg.get('value_label') !== undefined) {
                                            data[_arg.get('name')] = _arg.get('value_label');
                                        } else {
                                            data[_arg.get('name')] = this.parse_value(_arg);
                                        }
                                    });
                                    desc = method.get('label');
                                    if (method.get('editor_value_display') !== undefined) {
                                        desc += '<br><br>'+label_rendering(method.get('editor_value_display'), data);
                                    }
                                } else if (args.length === 0) {
                                    desc = method.get('label');
                                } else {
                                    arg = args.models[0];
                                    desc = method.get('label') + ': ';
                                    desc += arg.toDisplayValue();
                                }

                                delete_method_url = this.get_navigation_url()+'?section='+this.options.section+'&action=delete&id='+device.get('id')+'&aid='+method.id;

                                $device_content.append(this.summary_item({
                                    method_id: method.id,
                                    delete_url: delete_method_url,
                                    desc: desc,
                                    is_error: (method.get('status') > 0),
                                    edit_mode: edit_mode
                                }));
                            }.bind(this));
                        } else {
                            // assume device has being remove/unpaired
                            $device_content.append('<div style="width:50px; height:24px"></div>')
                        }
                        
    	    		}.bind(this));
        		}
            }
    	},

    	destroy: function() {
    		this.clear();
    	},

    	clear: function() {
    		this.$el.empty();
    	},

    	get_navigation_url: function() {
    		var url = '#/rule/'+this.options.mode;
			if (this.uid !== undefined) {
				url += '/'+this.uid
			}
			return url;
    	},

    	label_rendering: function(label, data, reg) {
            reg = reg || '%(\\w+)%';
            var preg = new RegExp(reg, 'i');
            var greg = new RegExp(reg, 'gi');
            if (label !== null && label !== undefined) {
                var o = label;
                var matcher, datapick;
                _.each(label.match(greg), function(a, idx) {
                    console.log('o', o)
                    matcher = o.match(preg);
                    datapick = data[matcher[1]];
                    if (datapick !== undefined) {
                        o = o.replace(matcher[0], datapick);
                    } else {
                        console.warn('matcher', matcher[0], 'contains unknown property or not value set?')
                        o = o.replace(matcher[0], 'N/A');
                    }
                });

                var html = '';
                _.each(o.split('\n'), function(v) {
                    html += '<div class="action-gp-item">'+v+'</div>';
                });

                if (html === '') html = o;
            }

            return html;
        },

        parse_value: function(arg) {
        	var value = arg.get('value');
        	switch (arg.get('component_type')) {
        		case 'kbxDateTimeRange':
        		var del = arg.get('component_config').kbxParamDelimiter;
        		var tmp = arg.get('value').split(del);
        		tmp[0] = this.utils.unixToDateString(tmp[0], 'MMM DD, YYYY hh:mm A')
        		tmp[1] = this.utils.unixToDateString(tmp[1], 'MMM DD, YYYY hh:mm A')
        		value = tmp[0] + ' ' +del +' '+ tmp[1];
        		break;
        	}
        	return value;
        }

    })

    return SummaryView;
});
