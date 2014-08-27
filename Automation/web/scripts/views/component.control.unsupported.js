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
    'models/kbx.input-text'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var unsupportedKbx = AbstractControlComponent.extend({
        template: JST['app/scripts/templates/component.control.abstract.error.ejs'],
    	render: function(model) {
            this.model = model;

            this.$el.html(this.template({
                message: 'Sorry, '+ this.model.get('type')+' is yet to be supported.'
            }))

            // throw error instead init
            this.trigger(this.EVT_ERROR)
        },
    })

    return unsupportedKbx;
});