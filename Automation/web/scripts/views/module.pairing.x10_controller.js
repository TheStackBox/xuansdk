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

    var ModulePairingX10ControllerView = Backbone.View.extend({
        template: JST['app/scripts/templates/module.pairing.x10_controller.ejs'],
        events: {
            'click #unit': 'show_options_list',
            'click #house': 'show_options_list',
            'click #x10-opt-list li':'close_options_list',
        },

        show_options_list: function(e){
        	$('#protocol-select').hide();
        	$('#x10-controller').hide();
        	$('#x10-opt-list').show();
        }

        close_options_list: function(e){
        
        	window.history.back();
        }
    });

    return ModulePairingX10ControllerView;
});
