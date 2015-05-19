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
	'underscore',
	'jquery',
    'templates',
], function (_, $, JST) {
    'use strict';
    var ComponentFactory = {};

    var tmplStore = {};
    tmplStore['default'] = JST['app/scripts/templates/scene.editor.component.default.ejs']
    tmplStore['kbxHSBColor'] = JST['app/scripts/templates/scene.editor.component.color.ejs']
    tmplStore['kbxColor'] = JST['app/scripts/templates/scene.editor.component.color.ejs']
    tmplStore['kbxOption.kbxOptionWithIcon'] = function(opt) {
    	var _tmpl = JST['app/scripts/templates/scene.editor.component.icon-option.ejs'];
    	var _icon_tmpl = JST['app/scripts/templates/scene.editor.component.icon-option.item.ejs'];
    	var $t = $($.parseHTML(_tmpl(opt)));
    	var $_value_container = $t.find('.icon-option-value-container');

    	opt.model.get('value').each(function(value, index) {
    		// add comma
    		if ($_value_container.html() != '') $_value_container.append(', ');

    		// write
    		$_value_container.append(_icon_tmpl({model: value}));
    	}.bind(this))

    	return $t;
    }

    var renderComponent = function(comp) {
    	var tmpl = tmplStore[comp.get('type')];
    	if (tmpl == undefined) {
    		console.warn('Component type',comp.get('type'),'has no template')
    		tmpl = tmplStore['default'];
    	}
    	return tmpl({model: comp});
    }

    // action model: scene.js [NonIDBasedRuleDeviceMethod]
	ComponentFactory.render = function($el, action) {
		// header
		var $header = $('<span>', {className:'action-item-header'});
		var $components = $('<span>', {className: 'action-components'});

		$header.text('['+action.get('device').get('name')+'] '+action.get('label') + ' - ');

		if (action.get('ui_components').length >= 1) {
            // more than one user parameters
            // cf.action_desc = 'Set '+action.get('label') + ' in ' +action.get('device').get('name');
            action.get('ui_components').each(function(component, index) {
            	if (component.toDisplayValue() != undefined) {
            		// give a comma first
            		if ($components.text() != '') {
            			$components.append(', ');
            		}

            		$components.append(renderComponent(component));
            	}
            })
        } else if (action.get('ui_components').length == 0) {
            // Chuck Norris fill them all
            $components.text(' Enabled '+action.get('label'));
        }

        $el.append($header);
        $el.append($components);
	}
	
	return ComponentFactory;
})