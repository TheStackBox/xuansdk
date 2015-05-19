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
    'common/components/views/component.control.abstract',
    'templates',
    'common/components/views/component.control.option.item-renderer'
], function ($, _, AbstractControlComponent, JST, kbxOptionItemRenderer) {
    'use strict';

    var spr = AbstractControlComponent.prototype;
    var ItemRenderer = AbstractControlComponent.extend({
    	template: JST['app/scripts/common/components/templates/component.control.option.item.ejs'],
    	events: {
    		'click #item': 'on_item_selected'
    	},

    	destroy: function() {
    		this.undelegateEvents();
    		this.model = undefined;
    		
    		spr.destroy.call(this);
    	},

    	render: function(model) {
    		this.model = model;
    		this.$el.html(this.template({model: model}))
    	},

    	select: function() {
    		this.$('#item').addClass('selected')
    	},

    	deselect: function() {
    		this.$('#item').removeClass('selected')
    	},

    	on_item_selected: function(e) {
    		this.trigger('select', this, e);
    	}
    })

    return ItemRenderer;
});