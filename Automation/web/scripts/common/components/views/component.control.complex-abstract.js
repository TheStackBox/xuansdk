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
	'backbone',
    'common/components/views/component.control.abstract',
    'common/components/views/list/component.list',
    'common/components/views/list/component.list.param',
    'templates',
    'common/components/models/kbx.datetime'
], function (Backbone, AbstractControlComponent, ComponentListItem, ComponentParam, JST, kbxDateTime) {
    'use strict';

    // class providing listing and param holder

    var spr = AbstractControlComponent.prototype;
    var AbstractComplexControlComponent = AbstractControlComponent.extend({
    	EVT_SELECT: 'select_elem',
    	initialize: function() {
    		this.list_setting = new Backbone.Collection();
    		this.list_view = new ComponentListItem();
    		this.param_holder = new ComponentParam();
            this.param_holder.on('done', this.on_user_completed_component, this);
    		this.param_holder.on('reset', this.on_user_completed_component, this);
    	},

    	render: function(model) {
            this.model = model;
            this.list_view.render(this.list_setting);
            this.trigger(this.EVT_INIT);
    	},

    	render_component: function(model) {
    		// render component
    		this.param_holder.render(model);
    		this.$el.html(this.param_holder.$el);
    	},

    	on_user_completed_component: function(model) {
    		// update list
    		this.list_view.update(model);

    		window.history.back();
    	},

    });

    return AbstractComplexControlComponent;
});