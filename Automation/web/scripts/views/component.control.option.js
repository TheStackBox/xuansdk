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
    'views/component.control.abstract',
    'templates',
    'models/kbx.option',
    'views/component.control.option.item-renderer'
], function ($, _, AbstractControlComponent, JST, Model, kbxOptionItemRenderer) {
    'use strict';

    var spr = AbstractControlComponent.prototype;
    var kbxOption = AbstractControlComponent.extend({
        ERROR_EMPTY_LIST: 'empty_list',
    	template: JST['app/scripts/templates/component.control.option.ejs'],
    	item_renderer: kbxOptionItemRenderer,
    	destroy: function() {
    		// destroy item renderer
    		_.each(this.list_item, function(item) {
    			if (item.destroy) item.destroy();
    		});

    		// destroy the rest
    		spr.destroy.apply(this, arguments);

    		// undefining vars
    		this.model = undefined;
    		this.selected_item = undefined;

    	},
    	render: function(model) {
    		this.model = model;

            // validate data structure
            if (this.model.get('list').length <= 0) {
                // no list to display
                this.show_error('There\'s nothing to be selected.', this.ERROR_EMPTY_LIST);
                return;
            }

            this.max = this.model.get('extra').kbxParamMaxSize || undefined;
            this.min = this.model.get('extra').kbxParamMinSize || undefined;
            this.multiple = false;
            if (this.model.get('extra').kbxParamMultiSelect !== undefined) {
                this.multiple = this.model.get('extra').kbxParamMultiSelect;
            } else if (this.max === undefined) {
                // no max is defined
                this.multiple = true;
            } else if (this.min !== undefined && this.max !== undefined) {
                // if min is 1 and max is 1
                this.multiple = (this.min > 1 && this.max > 1);
            }

            // default value
    		this.selected_item = [];

    		console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            // render list template
            this.$el.html(this.template());

            // render item
            this.list_item = [];
            var itm,
                valueToBeSet;

            if (this.model.get('value').length > 0) {
                // select value
                valueToBeSet = this.model.get('value')
            } else {
                // select default value
                valueToBeSet = this.model.get('default_value')
            }

            this.model.get('list').each(function(item) {
            	itm = this.render_item(item);
            	this.list_item.push(itm);

                // pushing default value
                if (valueToBeSet.get(item.get('value')) !== undefined) {
                    this.selected_item.push(itm)
                    itm.select();
                }

            	this.$('#list-container').append(itm.el);
            }.bind(this))

            this.trigger(this.EVT_INIT);
    	},

    	render_item: function(item_model, container) {
    		var itm = new this.item_renderer();
    		itm.on('select', this.on_user_trigger_item, this);
    		itm.render(item_model);

    		return itm;
    	},

    	on_user_trigger_item: function(item_renderer, event) {
    		if (this.multiple) {
                // multiple select
                
    			var search_idx;
    			var search_item = _.find(this.selected_item, function(item, index) {
    				search_idx = index;
    				return item.model.get('value') === item_renderer.model.get('value')	
    			});

    			if (!search_item) {
    				// select the item
                    if (this.max !== undefined && this.selected_item.length +1 > this.max) {
                        // break away;
                        return ;
                    }
    				this.selected_item.push(item_renderer);
    				item_renderer.select();
    			} else {
    				// deselect item
    				search_item.deselect();
    				this.selected_item.splice(search_idx, 1);
    			}
    		} else {
    			// deselect previous item renderer
    			if (this.selected_item[0] !== undefined) this.selected_item[0].deselect();
    			this.selected_item[0] = item_renderer;
    			item_renderer.select();
    		}

            this.validate();
    	},

    	get_value: function() {
            if (this.validate()) {
        		var o = new this.model.valueLabelClass();
        		_.each(this.selected_item, function(item) {
        			o.add(item.model);
        		})
        		return o;
            }
            return;
    	},

        validate: function() {
            if (this.multiple) {
                // multiple item
                if (this.min !== undefined && this.selected_item.length < this.min) {
                    // too little
                    this.trigger(this.EVT_INVALID)
                    return false;
                } else if (this.max !== undefined && this.selected_item.length > this.max) {
                    // too much
                    this.trigger(this.EVT_INVALID)
                    return false;
                }
            } else {
                if (this.selected_item.length !== 1) {
                    this.trigger(this.EVT_INVALID)
                    return false;
                }
            }

            this.trigger(this.EVT_VALID)
            return true
        }
    });

    return kbxOption;

});
