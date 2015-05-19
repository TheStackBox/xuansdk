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
    'common/components/views/component.control.option.item-renderer',
    'common/models/label_value'
], function (kbxOptionItemRenderer, ValueLabel) {
    'use strict';

    var spr = kbxOptionItemRenderer.prototype;
    var SelectAllItemRenderer = kbxOptionItemRenderer.extend({
    	render: function() {
            var m = new ValueLabel.model({value: '_select_all_', label: lang.translate('select_all')});
            spr.render.call(this, m);
    	},

    	select: function() {
    		spr.select.call(this);
            this.$('#item').text(lang.translate('deselect_all'));
        },

        deselect: function() {
            spr.deselect.call(this);
            this.$('#item').text(lang.translate('select_all'));
    	},
    })

    return SelectAllItemRenderer;
});