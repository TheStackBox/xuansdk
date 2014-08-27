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
    'views/component.control.input-text',
    'templates',
    'models/kbx.text-area'
], function ($, _, ComponentInputText, JST, Model) {
    'use strict';

    var spr = ComponentInputText.prototype;
    var kbxTextArea = ComponentInputText.extend({
    	template: JST['app/scripts/templates/component.control.text-area.ejs'],
    	render: function(model) {
    		this.model = model;

    		console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            this.$el.html(this.template({type: this.type, model: model}));

            this.trigger(this.EVT_INIT);
    	},

        validate: function(e) {
            var state = spr.validate.call(this, e);
            
            var $target = this.$('#textinput');
            var result = $target.prop('value');

            if (!state) {
                if (result.length > 0 && result.length < parseInt(this.model.get('extra').kbxParamMinLength)) {
                    // not within min char requirement
                    $target.removeClass('error-msg');
                    $target.addClass('error-data');
                } else {
                    $target.addClass('error-msg');
                    $target.removeClass('error-data');
                }
            } else {
                $target.removeClass('error-data');
            }

            return state;
        }
    })

    return kbxTextArea;
});