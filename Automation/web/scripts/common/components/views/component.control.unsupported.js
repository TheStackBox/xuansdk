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
    'common/components/models/kbx.input-text'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var unsupportedKbx = AbstractControlComponent.extend({
        template: JST['app/scripts/common/components/templates/component.control.abstract.error.ejs'],
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