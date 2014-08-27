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
    'Kurobox',
    'models/control.ipcamera',
    'views/control.ipcamera.proxy',
], function (_, AbstractCtrl, Kurobox, Model) {
    'use strict';

    var TRIGGER_CAMERA_METHOD = 'showPluginForPluginWithPluginParameter';

    var spr = AbstractCtrl.prototype;
    var IPCameraControl = AbstractCtrl.extend({
    	destroy: function() {
            console.log('-- ip camera destroy')
    		
            spr.destroy.call(this);
        },

    	render: function() {
            // bootstrap the damn camera
            IPCameraProxy.paired_device_id = this.options.device.get('id');

            // model
            this.model = new Model({id: this.options.device.get('id')});
            this.model.fetch({
                success: function() {

                    console.log('initialise native camera')
                    // prepare ip camera proxy

                    // ip camera proxy
                    IPCameraProxy.onClose = this.on_camera_terminated.bind(this);

                    // initialise camera
                    var extra_info = {
                        device: this.model.get('stream_config'),
                        pluginCallbackClass: 'window.IPCameraProxy'
                    }
                    Kurobox.native(TRIGGER_CAMERA_METHOD, undefined, ['foscam', JSON.stringify(extra_info)]);

                    _.defer(function() {
                        spr.init.call(this);
                    })
                }.bind(this),
                error: function() {
                    console.error('Unable to get camera configuration');
                }.bind(this)
            });
    	},

    	on_camera_terminated: function() {
            console.log('-- camera closed')
    		// do something
    		window.history.back();
    	}
    });

    return IPCameraControl;

});
