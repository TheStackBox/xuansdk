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
    'common/components/views/component.control.option',
    'common/components/views/component.control.icon-option.item-renderer',
    'common/components/views/component.control.icon-option.select-all-item-renderer',
    'templates',
    'common/components/utils/fontloader'
], function ($, _, OptionListComponent, kbxIconOptionItemRenderer, kbxIconOptionSelectAllItemRenderer, JST) {
    'use strict';

    //model: kbx.icon-option
    var IconOptionListComponent = OptionListComponent.extend({
        fn: OptionListComponent.prototype,
        item_renderer: kbxIconOptionItemRenderer,
        select_all_item_renderer: kbxIconOptionSelectAllItemRenderer,
        template: JST['app/scripts/common/components/templates/component.control.icon-option.ejs'],
        render: function(model) {

            // get font parameter
            var settings = {};
            model.get('list').each(function(item) {
                settings[JSON.stringify(item.get('font').attributes)] = item.get('font');
            });

            // load fonts
            _.each(settings, function(value, key) {
                KbxFontLoader.load(value.get('family'), value.get('srcs'), value.get('style'));
            });

            this.fn.render.call(this, model);

        }
    });

    return IconOptionListComponent;

});
