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
    'common/components/views/component.control.icon-option.item-renderer',
    'common/models/label_value',
    'templates'
], function (kbxIconOptionItemRenderer, ValueLabel, JST) {
    'use strict';

    var SelectAllItemRenderer = kbxIconOptionItemRenderer.extend({
        fn: kbxIconOptionItemRenderer.prototype,
        template: JST['app/scripts/common/components/templates/component.control.icon-option.select-all-item.ejs'],
    	render: function() {
            var m = new ValueLabel.model({value: '_select_all_', label: lang.translate('select_all')});
            this.fn.render.call(this, m);
    	}
    })

    return SelectAllItemRenderer;
});