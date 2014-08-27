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
	'underscore',
    'libs/backbone/router/kurobox-router',
    'views/shell',
    'views/device',
    'views/rule',
], function (_, KuroboxRouter, AppShell, DeviceView, RuleView) {
    

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
            'device': 'navigate_device',
            'device/:action(/:uid?:queryStr)': 'navigate_device',
            'device/:action(/:uid)': 'navigate_device'
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
    		this.navigate('#/device', {trigger: true});
    	},

    	navigate_device: function(action, uid, queryStr) {
    		action = action || 'list_device';	// default go to list_device

    		if (this.page === undefined || ((this.page !== undefined) && this.page.constructor !== DeviceView)) {
                if (this.page !== undefined) {
                    if (typeof this.page.destroy !== 'undefined') this.page.destroy();
                }
    			this.page = this.change_page(DeviceView);
    		}
            
    		this.page.navigate(action, uid, this.parse_query(queryStr));
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

    	prepare_page_param: function(extra_param) {
    		var param = KuroboxRouter.prototype.prepare_page_param.apply(this, extra_param);
    		param.nav = this.shell.nav;
    		return param;
    	}
    });

    return AutomationAppRouter;
});
