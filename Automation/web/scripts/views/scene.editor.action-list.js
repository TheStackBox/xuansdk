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
    'views/scene.editor.action-item-generator'
], function ($, _, Backbone, JST, ActionItemLabelGenerator) {
    'use strict';


    var SceneActionListView = Backbone.View.extend({
    	tagName: 'ul',
        add_item_template: JST['app/scripts/templates/scene.editor.add-action.ejs'],
        events: {
            'click .option-btn': 'on_user_trigger_action_item_option',
            'click #add-scene-item-btn': 'on_user_trigger_action_item_option',
        },
        destroy: function() {
            this.$el.remove();
            this.collection = undefined;
        },
    	update: function(collection) {
    		this.$el.empty();
            this.undelegateEvents();

            // before hand, add add button!
            this.$el.append(this.add_item_template());

            if (this.label_gen == undefined) {
                this.label_gen = new ActionItemLabelGenerator();
            }

    		var render_tmpl;
            console.warn('TODO: translation please')
            collection.each(function(action, index) {
                render_tmpl = this.label_gen.generate_item_label(action, index);

                // print them
                this.$el.append(render_tmpl);
            }.bind(this))
            
            this.collection = collection;

            _.defer(function() {
                this.delegateEvents();
            }.bind(this))
    	},

        on_user_trigger_action_item_option: function(e) {
            var $e = $(e.currentTarget);
            console.log('---- user trigger action item', $e.data('idx'))
            var model = this.collection.at($e.data('idx'));
            this.trigger('option', $e.data('idx'), model, e)
        }
    })

    return SceneActionListView;
});