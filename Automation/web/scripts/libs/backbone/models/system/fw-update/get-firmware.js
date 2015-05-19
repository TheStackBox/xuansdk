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
    'backbone',
    'libs/backbone/models/system/info/firmware_version',
    'libs/backbone/models/system/fw-update/call-external-api',
    'libs/backbone/models/system/network/check_internet'
], function ($, _, Backbone, FirmwareVer, CallExtUrl, CheckInternet) {
    'use strict';
    var FirmwareUpdateModel = Backbone.Model.extend({
        fetch:function(options) {
            console.log('Check Internet connection...');
            var checkInternet = new CheckInternet();
                checkInternet.fetch({
                    success:function(){
                        console.log('Box is connected to internet!');
                       //get firmware version
                        var firmwareVer = new FirmwareVer();
                            firmwareVer.fetch({
                                success:function(){
                                    this.set('version', firmwareVer.get('version'));
                                    //check any updated firmware for the board
                                    var get_firmware_url = 'http://myibox.net/firmware/update_xml.jsp?UserAgent=Syabas/'+this.get('version');
                                    //var get_firmware_url = 'http://myibox.net/firmware/update_xml.jsp?UserAgent=Syabas/01-01-150714-02-POP-899-800';

                                    var callExtUrl = new CallExtUrl();
                                        callExtUrl.fetch(get_firmware_url, {
                                            success:function(target, data, sync){
                                                console.log('get firmware success!!!');
                                                var xml =  $($.parseXML(callExtUrl.get('data')));
                                                    this.set('updateAvailable', xml.find('updateAvailable').text());
                                                    this.set('copyright', xml.find('copyright').text());
                                                    this.set('priority', xml.find('priority').text());
                                                    this.set('disclaimer', xml.find('text').text());
                                                    this.set('changes', xml.find('changes').text());
                                                    this.set('releaseDate', xml.find('releaseDate').text());
                                                    this.set('latestRelease', xml.find('latestRelease').text());
                                                    this.set('url', xml.find('url').text());

                                                console.log('Update available: ');
                                                console.log(xml.find('updateAvailable').text());
                                                
                                                if(xml.find('updateAvailable').text() != null){
                                                    if(options.success) options.success(target, data, sync);
                                                }else{
                                                    if(options.error) options.error(target, data, sync);
                                                }
                                            }.bind(this),
                                            error:function(target, data, sync){
                                                console.log('get firmware failed!!!');
                                                if(options.error) options.error(target, data, sync);
                                            }.bind(this)
                                        })
                                }.bind(this),
                                error:function(target, data, sync){
                                    console.log('get firmware version error!!!');
                                    if(options.error){options.error(target, data, sync)}
                                }.bind(this)                   
                            })
                    }.bind(this),
                    error:function(target, data, sync){
                        console.log('Box is not connected to internet!');
                        if(options.error){options.error(target, data, sync)}
                    }.bind(this)                    
                })
        }
    });

    return FirmwareUpdateModel;

});
