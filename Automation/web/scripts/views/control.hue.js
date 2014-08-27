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
    'views/control.abstract',
    'templates',
    'Kurobox',
    'models/control.hue',
    'views/component.tab',
    'farbtastic',
    'libs/utils/color',
    'libs/utils/browser'
], function (_, AbstractCtrl, JST, Kurobox, Model, Tab) {
    'use strict';

	var COLOR_TAB = 0;
	var SCENE_TAB = 1;

    var spr = AbstractCtrl.prototype;
    var HueControl = AbstractCtrl.extend({
    	template: JST['app/scripts/templates/control.hue.ejs'],
        model_class: Model,
    	events: {
    		'click #power-btn': 'on_user_turn_power_on_off',
            'click .icon-reset': 'on_user_reset_hue'
            // 'touchend #picker': 'on_user_confirm_color',
            // 'mouseup #picker': 'on_user_confirm_color'
    	},

        initialize: function() {
            spr.initialize.call(this);

            if (BrowserUtil.isMobile()) {
                this.events['touchend #picker'] = 'on_user_confirm_color';
            } else {
                this.events['mouseup #picker'] = 'on_user_confirm_color';
            }
        },

    	destroy: function() {
    		spr.destroy.call(this);

            // stop event
            Kurobox.socket.stop();
    	},

        init: function(data) {
            console.log(data.response.status);
            spr.init.call(this);

            // initialize picker
            this.farbtastic = $.farbtastic('#picker', this.on_user_pick_color.bind(this));
            this.farbtastic.radius = 93;
            this.farbtastic.square = 0;
            this.farbtastic.width = 250;
            this.farbtastic.setColor('#FF0000');

            // disable inner square marker
            // added a div to display color output
            $('.color').before( '<div id="output"></div>' );
            $('.sl-marker').css('display', 'none');

            this.hue = data.response.status.hue;
            this.colorTemperature = data.response.status.colorTemperature;
            this.saturation = data.response.status.saturation;
            this.brightness = data.response.status.brightness;
            this.rgb = data.response.status.rgb;

            this.colorHex = ColorUtil.rgb2hex(this.rgb.r, this.rgb.g, this.rgb.b);
            // this.colorHex = '#FF0000'

            console.log('rgb***',this.rgb);
            console.log('hex***',this.colorHex);
            
            this.invalidate_power_status(this.hue);

            this.farbtastic.setColor(this.colorHex);
            this.farbtastic.updateDisplay();

            // update color output
            _.defer(function() {
                this.$("#output").css("background-color", this.colorHex);
            }.bind(this));
            // initialise tab
     /*this.tab = new Tab({el: this.$('#option-tab'),
                data: [
                    {label: 'Color', value: COLOR_TAB, icon: 'color'},
                    {label: 'Scene', value: SCENE_TAB, icon: 'scene'}
                ]
            });
            this.tab.on('selected', this.on_user_select_tab);
            this.tab.render();*/

            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:HUE_CONTROLLER_STATE_CHANGED', this.on_status_changed, this);
            Kurobox.socket.start();
        },

    	on_user_select_tab: function(value) {
    		switch (value) {
    			case COLOR_TAB:
    			this.$('#color-control').show();
    			this.$('#scene-control').hide();
    			break;

    			case SCENE_TAB:
    			this.$('#scene-control').show();
    			this.$('#color-control').hide();
    			break;
    		}
    	},

    	on_user_pick_color: function(code) {
    		console.log('code', code)
            this.$("#output").css("background-color", code);

            this.colorHex = code;
    	},

    	on_user_confirm_color: function(e) {
    		// save and send
            var rgb = ColorUtil.hex2rgb(this.colorHex);
            console.log('rgb', rgb);
    		this.model.set_color_rgb(rgb);
    	},

    	on_user_turn_power_on_off: function(e) {
    		var $e = $(e.currentTarget)
    		// true is on
    		if (this.hue=='ON') {
    			// turn it off
    			this.model.power_off();
                this.hue='OFF';
    		} else {
    			// turn it on
    			this.model.power_on();
                this.hue='ON';
    		}
    		
    		// assume when action is execute, power parameter is modified
    		this.invalidate_power_status(this.hue);
    	},

    	invalidate_power_status: function(powered) {
    		if (powered=='ON') {
                this.$('#power-btn').removeClass('disabled')
            } else {
                this.$('#power-btn').addClass('disabled')
    		}
    	},

        on_status_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.hue=data.response.hue;
                this.invalidate_power_status(this.hue);

                this.rgb = data.response.rgb;
                this.colorHex = ColorUtil.rgb2hex(this.rgb.r, this.rgb.g, this.rgb.b);
                //this.farbtastic.setColor(this.colorHex);
                console.log('erm..', data);
            }
        },

        on_user_reset_hue: function() {
            this.colorHex = '#ffff00'
            this.farbtastic.setColor(this.colorHex);
            this.farbtastic.updateDisplay();
            this.$("#output").css("background-color", this.colorHex);

            this.on_user_confirm_color();
        }
    })

    return HueControl;
});