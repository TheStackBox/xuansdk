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
    'libs/backbone/models/kurobox-collection',
    'views/scene.editor.action-item-generator',
    'gridster'
], function ($, _, Backbone, JST, KuroboxCollection, ActionItemLabelGenerator) {
    'use strict';

    var WIDGET_HEIGHT = 120;
    var HOLD_DURATION = 200;
    var isTouch = !!('ontouchstart' in window)
    var SceneActionItemsMover = Backbone.View.extend({
    	id: 'scene-action-item-mover',
    	template: JST['app/scripts/templates/scene.editor.action-list-mover.ejs'],
        events: {
            'touchstart li': 'on_user_touched_item',
            'mousedown li': 'on_user_touched_item',
            'touchleave li': 'on_user_leave_item',
            'mouseup li': 'on_user_leave_item',
            'touchmove': 'on_user_scroll',
            'mousemove': 'on_user_scroll',
            'click #move-done-btn': 'on_user_confirm_position'
        },
        model: KuroboxCollection,
    	destroy: function() {
            // de-reference actions
    		this.actions = undefined;

            // destroy gridster
            this.grid_control.destroy();
            this.grid_control = undefined;

            this.undelegateEvents();

            // clear up dom
    		this.$el.remove();
    	},

    	render: function() {
    		this.$el.html(this.template());
    	},

    	invalidate: function(actions) {
            if (this.grid_control != undefined) {
                this.grid_control.destroy();
                this.grid_control = undefined;
            }
    		this.actions = actions;

            if (this.label_gen == undefined) {
                this.label_gen = new ActionItemLabelGenerator();
                this.label_gen.delay_item_template = JST['app/scripts/templates/scene.editor.action-list-mover.delay.ejs'];
                this.label_gen.item_template = JST['app/scripts/templates/scene.editor.action-list-mover.item.ejs'];
            }

            var item_tmpl;
    		this.actions.each(function(action, index){
    			item_tmpl = this.label_gen.generate_item_label(action, index)

    			this.$('.scene-move-list').append(item_tmpl);
    		}.bind(this))


            _.defer(function() {
        		this.grid_control = this.$('.scene-move-list').gridster({
                    // grid config
                    min_row: this.actions.length,
                    max_row: this.actions.length,
                    widget_selector: 'li',
                    widget_base_dimensions: [this.$el.width(), WIDGET_HEIGHT],
                    widget_margins:[0,0],
                    collision: {
                        overlapping_region: 'all'
                    },
                    draggable: {
                        hold: 3,
                        start: function(jqEvent, draggable) {
                            var $target = $(jqEvent.target);
                            console.log('#####> start drag', $target.hasClass('description'), $target)

                            // some webkit cant detect width and height
                            if (draggable.$player.data('coords').coords.width === 0 || draggable.$player.data('coords').coords.height === 0) {
                                // reset coords properties
                                draggable.$player.data('coords').set();

                                // update preview holder's width height
                                this.$('.preview-holder').css({
                                    width: draggable.$player.data('coords').coords.width,
                                    height: draggable.$player.data('coords').coords.height,
                                })
                            }
                        }.bind(this)
                    }
                }).data('gridster');
                
                // remove drag start
                var pointer_events = this.grid_control.drag_api.pointer_events;
                this.grid_control.drag_api.$container.off(pointer_events.start);

                // listen drag end
                this.grid_control.drag_api.$document.on(pointer_events.end, this.on_user_leave_item.bind(this))
                
                // this.grid_control.disable();

            }.bind(this))
    	},

        on_user_touched_item: function(e) {
            e.stopPropagation();
            // prevent script execution when mouse down event in mobile/touch screen
            if (isTouch && e.which != 0) return;

            var $currentTarget = $(e.currentTarget);

            var exec_function = function() {
                $currentTarget.removeClass('hold');
                this.grid_control.drag_api.drag_handler(e)

                this.$el.addClass('dragging');
                $currentTarget.addClass('player');

                delete this.hold_timeout;
                this.hold_timeout = undefined;
            }.bind(this);

            if ($(e.target).is('.icon-mover')) {
                exec_function();
            } else {
                $currentTarget.addClass('hold')
                this.hold_timeout = setTimeout(exec_function, HOLD_DURATION)
            }

        },

        on_user_leave_item: function(e) {
            var $currentTarget = this.$('li.hold');
            $currentTarget.removeClass('hold')

            clearTimeout(this.hold_timeout);
            delete this.hold_timeout;
            this.hold_timeout = undefined;

            if (this.$el.hasClass('dragging')) {
                this.$el.removeClass('dragging');
                this.$('li.player').removeClass('player');
            }
        },

        on_user_scroll: function(e) {
            if (this.hold_timeout != undefined) {
                this.on_user_leave_item(e);
            }
        },

        get_serialized_actions: function() {
            if (this.grid_control == undefined) {
                if (this.actions == undefined) return;

                return this.actions;
            }

            var serialized_data = this.grid_control.serialize();

            var new_changes = [];

            _.each(serialized_data, function(data, index) {
                new_changes[data.row-1] = this.actions.at(index);
            }.bind(this))

            return new this.model(new_changes);
        },

        on_user_confirm_position: function() {
            this.trigger('done', this.get_serialized_actions());
        }
    })

    return SceneActionItemsMover;
});