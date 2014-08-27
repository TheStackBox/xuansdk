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
    'templates'
], function ($, _, Backbone, JST) {
    'use strict';

    var ModuleAddDeviceProtocolSelectorView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.add-device.protocol-selector.ejs'],
        events: {
        	'click .protocol-item': 'on_user_select_protocol'
        },

        initialize: function() {
        	if (this.options.list === undefined) {
        		console.error('Undefined protocol list');
        		return;
        	}

        	this.render();
        },

        reset: function() {
            $('.protocol-pane').find('div').each(function() {
                $(this).removeClass('protocol-status');
                $(this).children( 'span' ).removeClass('protocol-itm-select');
                $(this).children( 'div' ).removeClass('arrow-up');
            });
        },

        render: function() {
        	$(this.el).html(this.template(this.options));
        },

        update: function(status, protocol_id) {
            console.log('=--- updating protocol status', protocol_id, status)
            var protocol = this.options.list.get(protocol_id);
            var $protocol_el = this.$('.protocol-item[data-protocol-id="'+protocol_id+'"]');
            protocol.set('enabled', status);

            if (status) {
                $protocol_el.removeClass('disable');
            } else {
                $protocol_el.addClass('disable');
            }
        },

        on_user_select_protocol: function(evt) {
        	var protocol_id = $(evt.currentTarget).data('protocol-id');
            // for loop to remove all on class
            $('.protocol-pane').find('div').each(function() {
                $(this).removeClass('protocol-status');
                $(this).children( 'span' ).removeClass('protocol-itm-select');
                $(this).children( 'div' ).removeClass('arrow-up');
            });
            // apply current selected status on UI
            $(evt.currentTarget).children( 'span' ).addClass('protocol-itm-select');
            $(evt.currentTarget).children( 'div' ).addClass('arrow-up');
            $(evt.currentTarget).addClass('protocol-status');
            
        	this.trigger('select', protocol_id);
        }
    });

    return ModuleAddDeviceProtocolSelectorView;
});
