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
    'underscore',
    'backbone',
    'templates',
], function (_, Backbone, JST) {
    'use strict';

    var OptionPaneView = Backbone.View.extend({
    	template: JST['app/scripts/common/templates/option-pane.ejs'],
    	item_template: JST['app/scripts/common/templates/option-pane.item.ejs'],
        events: {
            'click #exit-options': 'on_initial_close',
        },
    	render: function(config) {
    		this.$el.html(this.template(config));

    		if (config != undefined && config.items != undefined) {
    			if (config.items.length > 0) {
                    _.each(config.items, function(item) {
    				    this.$('#item-list').append(this.item_template(item));
                    }.bind(this));
    			}
    		}

            this.delegateEvents();
    		return this;
    	},

        destroy: function() {
            this.close();
        },

        open: function() {
            this.$el.show();
        },

        close: function() {
            this.$el.empty();
            this.undelegateEvents();
        },

        on_initial_close: function() {
            this.trigger('close');
        },
    })

    return OptionPaneView;
});