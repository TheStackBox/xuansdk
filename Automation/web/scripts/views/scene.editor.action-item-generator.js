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
    'views/scene.editor.action-item-generator.component-factory'
], function (_, $, JST, ComponentFactory) {
    'use strict';
    var Generator = function() {
    	if (this.initialize != undefined) this.initialize.call(this, arguments)
    }

    _.extend(Generator.prototype, {
	    delay_item_template: JST['app/scripts/templates/scene.editor.action-list-item.delay.ejs'],
	    item_template: JST['app/scripts/templates/scene.editor.action-list-item.ejs'],
		generate_item_label: function(action, index) {
			var tmpl;
	    	var cf = {
	            icon: action.get('device').get('icon'),
	            location: action.get('device').get('location') || '',
	            // location: action.get('device').get('location'),
	            idx: index,
	            is_error: false,
	        }
	        var $result;
	        var $r = function(selector) {
	        	console.log('-- looking for ', selector, $result.find(selector))
	        	return $result.find(selector)
	        }

	        if (action.get('status') != 0) {
	        	cf.is_error = true;
	        }

	        console.log('---> tracking action', action)

	        switch (action.get('id')) {
	            case -291:
	            cf.action_desc = lang.translate('delay_scene_desc').replace('%VALUE%', action.get('ui_components').models[0].toDisplayValue());
	            tmpl = this.delay_item_template;
	            // cf.action_desc = '['+action.get('device').get('name')+'] '+action.get('label')+ ' : '+action.get('ui_components').models[0].toDisplayValue();
	            break;

	            default: 
	            tmpl = this.item_template;
	            $result = $(tmpl(cf));
	            console.log('result', $result)

	            ComponentFactory.render($r('.action-desc'), action);
	            break;
	        }

	        if ($result == undefined) {
	        	return tmpl(cf);
	        } else {
	        	return $result;
	        }
	    }
    })
	
    return Generator;
});