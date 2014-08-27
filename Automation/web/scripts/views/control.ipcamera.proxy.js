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
    'Kurobox',
], function (_, AbstractCtrl) {
    'use strict';

    var MODULE = 'device_manager.ip_camera_controller';
    var SUCCESS_CALLBACK = 'apiSuccessedWithRequestIdAndData';
    var ERROR_CALLBACK = 'apiFailedWithRequestIdAndData';

    if (typeof window.IPCameraProxy === 'undefined') {
        console.log('-- writing proxy')
        var IPCameraProxy = window.IPCameraProxy = function() {};

        var api = function(method, jsonParam, requestId) {
            if (typeof IPCameraProxy.paired_device_id === 'undefined') {
                console.log('paired device id not found')
                throw 'No paired device id assigned to IPCameraProxy';
            }

            // parse param
            var param = JSON.parse(jsonParam);
            if (param === undefined) {
                console.error('unable to parse parameter object')
                throw 'Unable to parse parameter';
            }
            // insert module
            param.module = MODULE;
            param.pairedDeviceId = IPCameraProxy.paired_device_id;

            console.log('param json = '+ JSON.stringify(param));
            console.log('method ='+ method)
            console.log('requestID ='+requestId)
            
            Kurobox.api(method, param, {
                httpMethod:'GET',
                success: function(resp) {
                    Kurobox.native(SUCCESS_CALLBACK, undefined, [requestId, JSON.stringify(resp.response)]);
                },
                error: function(resp) {
                    Kurobox.native(ERROR_CALLBACK, undefined, [requestId, JSON.stringify({
                        is_ajax: error === -1,
                        code: resp.error.code,
                        message: resp.error.message
                    })]);
                }
            })
        }

        IPCameraProxy.api = api;
    }
});