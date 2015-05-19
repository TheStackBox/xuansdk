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
    'libs/backbone/router/kurobox-router',
    'common/views/shell',
    'views/rule',
    'views/scene',
    'routefilter'
], function (_, KuroboxRouter, AppShell, RuleView, SceneView) {
    

    var spr = KuroboxRouter.prototype;
    var AutomationAppRouter = KuroboxRouter.extend({

    	// sample route map: /#/{section}/{action}/{unique_id}
    	routes: {
    		'': 'welcome',
            'rule': 'navigate_rule',
            'rule(/:action?:queryStr)': 'navigate_rule_proxy',
            'rule(/:action)': 'navigate_rule',
            'rule/:action(/:uid?:queryStr)': 'navigate_rule',
            'rule/:action(/:uid)': 'navigate_rule',
            'scene/:section/:uid/:action?:queryStr': 'navigate_scene', 
            'scene/:section/:uid(/:action)': 'navigate_scene', 
            'scene/:section?:queryStr': 'navigate_scene_with_section_and_query',
            'scene/:section(/:uid)': 'navigate_scene',
            'scene': 'navigate_scene',
    	},

        after: function(route) {
            // patching white space issue
            _.defer(function() {
                // detect screen out of range
                var content_height = $('body').prop('offsetHeight');
                var screen_pos = $('body').scrollTop();
                var range_pos = content_height - $(window).height();

                if (screen_pos >= range_pos) {
                    console.log('!!!!! update scroll !!!!!')
                    $('body').scrollTop(range_pos);
                }
            })
        },

    	initialize: function() {
    		// call super
    		this.shell = new AppShell({el: $('body')});
    		this.shell.render();


            // register global error ui handling from shell
            Kurobox.global_api_error_handler = this.shell.handle_global_error.bind(this.shell);

            // assign shell to global
            window.Shell = this.shell;

            _.defer(function() {
                
                // show busy
                this.shell.addPreloadingPage();
            }.bind(this))
        },

        welcome: function() {
    		console.log('welcome')
    		this.navigate('#/scene', {trigger: true});
    	},

    	navigate_rule: function(action, uid, queryStr) {
            if (this.page === undefined || ((this.page !== undefined) && this.page.constructor !== RuleView)) {
                if (this.page !== undefined) {
                    if (typeof this.page.destroy !== 'undefined') this.page.destroy();
                }
                this.page = this.change_page(RuleView);
            }
            console.log('action: ', action);
            console.log('uid: ', uid);
            console.log('queryStr: ', queryStr);
            this.page.navigate(action, uid, this.parse_query(queryStr));
    	},

        navigate_rule_proxy: function(action, queryStr) {
            this.navigate_rule(action, undefined, queryStr);
        },

        navigate_scene: function(section, uid, action, queryStr) {
            if (this.page === undefined || ((this.page !== undefined) && this.page.constructor !== SceneView)) {
                if (this.page !== undefined) {
                    if (typeof this.page.destroy !== 'undefined') this.page.destroy();
                }
                this.page = this.change_page(SceneView);
            }

            // #/scene/favourite = favourite list
            // #/scene/all = show all
            
            // #/scene/{location} = show location
            // #/scene/item/{id}/{action} = showing action
            // #/scene/add
            this.page.navigate(section, uid, action, this.parse_query(queryStr));
        },

        navigate_scene_with_section_and_query: function(section, queryStr) {
            this.navigate_scene(section, undefined, undefined, queryStr);
        },

    	prepare_page_param: function(extra_param) {
    		var param = KuroboxRouter.prototype.prepare_page_param.apply(this, extra_param);
    		param.nav = this.shell.nav;
    		return param;
    	}
    });

    return AutomationAppRouter;
});
