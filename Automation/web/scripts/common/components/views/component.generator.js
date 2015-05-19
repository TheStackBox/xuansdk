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
define(function (require) {
    'use strict';

    // component import
    var component_store = {};
    // type backward
    component_store['kbxBoolean'] = require('common/components/views/component.control.toggle');
    component_store['kbxString'] = require('common/components/views/component.control.input-text');

    // new type
    component_store['kbxTextInput'] = component_store['kbxString'];
    component_store['kbxTextArea'] = require('common/components/views/component.control.text-area');
    component_store['kbxSlider'] = require('common/components/views/component.control.slider');
    component_store['kbxOption'] = require('common/components/views/component.control.option');
    component_store['kbxToggle'] = component_store['kbxBoolean'];
    component_store['kbxTime'] = require('common/components/views/component.control.time');
    component_store['kbxColor'] = require('common/components/views/component.control.color');
    component_store['kbxHSBColor'] = require('common/components/views/component.control.color.hsb');
    component_store['kbxFiles'] = require('common/components/views/component.control.file');
    component_store['kbxDateTime'] = require('common/components/views/component.control.datetime');
    component_store['kbxDateTimeRange'] = require('common/components/views/component.control.datetime-range');
    component_store['kbxTimeRange'] = require('common/components/views/component.control.time-range');
    component_store['kbxOption.kbxDayOfWeek'] = component_store['kbxOption'];
    component_store['kbxOption.kbxOptionWithIcon'] = require('common/components/views/component.control.icon-option');

    var create_component = function(kbxType) {
        var comp = component_store[kbxType];

        if (comp !== undefined) {
            return comp;
        }

        console.warn(' No component registered under', kbxType);
        return;
    }

    return create_component;
});
