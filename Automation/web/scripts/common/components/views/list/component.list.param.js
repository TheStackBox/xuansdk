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
define(function(require) {
	'use strict';

	var Backbone = require('backbone');
	var UnsupportedComponent = require('common/components/views/component.control.unsupported')
	var ComponentGenerator;

	console.log('... init ComponentParamHolderView')
	var ComponentParamHolderView = Backbone.View.extend({
		rule_action_button: JST['app/scripts/common/status-item/templates/action-buttons.ejs'],
		render: function(model) {
			this.model = model;
			var kbxType = model.get('type')

			if (ComponentGenerator === undefined) {
				ComponentGenerator = require('common/components/views/component.generator');
			}
			var comp = ComponentGenerator(kbxType);
			if (comp === undefined) {
				// assume there's no component registered
                comp = UnsupportedComponent;
			}

			try {
	    		this.component_view = new comp({el: this.el});
	    		if (this.component_view.EVT_SELECT === undefined) {
	                this.component_view.on(this.component_view.EVT_INVALID, this.on_component_value_invalid, this);
	                this.component_view.on(this.component_view.EVT_VALID, this.on_component_value_valid, this);
	                this.component_view.on(this.component_view.EVT_ERROR, this.on_component_error, this);
	                this.component_view.on('init', this.on_component_init, this);
			    	this.component_view.render(model);
	    		} else {
	    			this.component_view = undefined;
	    			console.error('Cannot load complex component')
	    		}
    		} catch (e) {
    			console.error('Error component view:', kbxType);
    			console.error(e.stack)
    		}

    		// render action buttons
    		var $footer = $('<div>', {id: 'abstract-comp-footer'});
    		$footer.hide();
    		this.$el.append($footer);
    		this.render_action_buttons($footer, {
                'reset-btn': 'on_user_reset',
                'done-btn': 'on_user_done'
            });
		},

		on_component_value_invalid: function() {
			// value is invalid
            // disable done button
            this.$('#abstract-comp-footer #done-btn').addClass('disabled');
		},

		on_component_value_valid: function() {
			// value is valid
            // enable done button
            this.$('#abstract-comp-footer #done-btn').removeClass('disabled');
		},

		on_component_error: function() {
			// remove action buttons
            this.$('#abstract-comp-footer').hide();
		},

		on_component_init: function() {
            // once component is rendered,
            
            _.defer(function() {
                // invalidate value in the component
                this.invalidate_done_buttons();
                this.$('#abstract-comp-footer').show();
            }.bind(this))
		},

		invalidate_done_buttons: function() {
            var $done_btn = this.$('#abstract-comp-footer #done-btn');
            var enabled = true;
            if (this.component_view === undefined) {
                // fail to init component
                enabled = false;
            } else {
                // let component get value to do the validation
                var comp_value = this.component_view.get_value()
                enabled = !(comp_value === undefined)
            }

            if (!enabled) {
                $done_btn.addClass('disabled');
            } else {
                $done_btn.removeClass('disabled');
            }
        },

		render_action_buttons: function(el, event_handlers) {
            el.append(this.rule_action_button());

            // register events
            if (this.events === undefined) this.events = {};

            _.each(event_handlers, function(callback, id) {
                this.events['click #'+el.attr('id')+' > #action-buttons > #'+id] = callback;
            }.bind(this));

            console.log('this.events', this.events)

            // re-delegate events
            this.undelegateEvents();
            this.delegateEvents();
        },

        on_user_done: function(e) {
        	// invalidate done buttons before start
            this.invalidate_done_buttons();

            var $me = $(e.currentTarget);
            var value = this.component_view.get_value();

            if (!$me.hasClass('disabled') && (value !== undefined || value !== '')) {
                // save value to method
                this.model.set('value', value);

                this.trigger('done', this.model);
            }
        },

        on_user_reset: function() {
            this.model.reset_value();

            this.trigger('reset', this.model);
        }
	})

	return ComponentParamHolderView;

});