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
    'views/control.abstract',
    'templates',
    'Kurobox',
    'models/control.thermostat'
], function (_, AbstractCtrl, JST, Kurobox, Model) {
    'use strict';

    var spr = AbstractCtrl.prototype;
    var SwitchControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.thermostat.ejs'],
        template_options: JST['app/scripts/templates/module.thermostat.options.ejs'],
        model_class: Model,
        events: {
            'click #temp-mode-btn': 'on_tab_mode',
            'click #fan-mode-btn': 'on_tab_mode',
            'click #temp-mode-view li': 'on_tab_temp_mode',
            'click #fan-mode-view li': 'on_tab_fan_mode',
            'click #target-temp-up-btn': 'on_taget_temp_up',
            'click #target-temp-dw-btn': 'on_taget_temp_dw',
        },

        destroy: function() {
            spr.destroy.call(this);
            Kurobox.socket.stop();
        },

        init: function() {
            spr.init.call(this);
            this.initialize_thermostat();
        },

        initialize_thermostat:function (e) {
            this.model.get_status({
                success:function(){
                    this.invalidate_thermostat_status();
                    Kurobox.socket.verbose = true;
                    Kurobox.socket.on('socket:THERMOSTAT_TEMPERATURE_CHANGED', this.on_thermostat_temperature_changed, this)
                    
                    Kurobox.socket.start();
                }.bind(this)
            })
        },

        navigate:function (param) {
            var param = param ? param : {};
            if(param.page == 'temp-mode'){
                this.$('#temperature-view').hide();
                this.$('#temp-mode-view').show();
                this.$('#fan-mode-view').hide();
                this.$('#temp-mode-view li').removeClass('selected');
                this.$('#temp-mode-view li[data-id='+this.model.get('mode')+']').addClass('selected');
            }else if(param.page == 'fan-mode'){
                this.$('#temperature-view').hide();     
                this.$('#fan-mode-view').show();
                this.$('#temp-mode-view').hide();
                this.$('#fan-mode-view li').removeClass('selected');
                this.$('#fan-mode-view li[data-id='+this.model.get('fanMode')+']').addClass('selected');                
            }else{
                this.$('#temperature-view').show();     
                this.$('#fan-mode-view').hide();     
                this.$('#temp-mode-view').hide();    
            }
        },

        on_thermostat_temperature_changed:function (data) {
            // if (data.response.pairedDeviceId == this.options.device.get('id')) {
                //this.mode.set('currentTermperature', 'new temperature 123456')
                //this.$('#temperature').text(this.model.get('currentTermperature'));
            // }
        },

        on_tab_mode:function (e) {
            if(this.$(e.currentTarget).attr('id') == 'temp-mode-btn'){
                window.location = window.location.hash+'?page=temp-mode';
            }else if(this.$(e.currentTarget).attr('id') == 'fan-mode-btn'){
                window.location = window.location.hash+'?page=fan-mode';
            }
        },

        on_tab_temp_mode:function (e) {
            this.$('#temp-mode-view').hide();
            this.model.temp_mode(this.$(e.currentTarget).data('id'));
            var selectedMode = this.model.get('tempModeList').get(this.model.get('mode'));
            if(selectedMode.attributes.targetEnable == 'false'){
                this.$('#target-temperature-view').hide();   
            }else{
                this.$('#target-temperature-view').show();   
            }            
            this.$('#temp-mode').text(selectedMode.attributes.name);
            window.history.back();
        },

        on_tab_fan_mode:function (e) {
            this.$('#fan-mode-view').hide();
            this.model.fan_mode(this.$(e.currentTarget).data('id'));
            this.$('#fan-mode').text(this.model.get('fanModeList').get(this.model.get('fanMode')).attributes.name);
            window.history.back();                       
        },

        on_taget_temp_up: function(e) {
            this.model.temperature(this.model.get('targetTermperature')+1, this.model.get('mode'));
            this.$('#target-temperature').text(this.model.get('targetTermperature'));                       

        },

        on_taget_temp_dw: function(e) {
            this.model.temperature(this.model.get('targetTermperature')-1, this.model.get('mode'));
            this.$('#target-temperature').text(this.model.get('targetTermperature'));
        },

        on_state_changed: function(data) {
            if (data.response.pairedDeviceId == this.options.device.get('id')) {
                this.model.set('switch_status', data.response.switch);
                this.invalidate_switch_status(this.model.get('switch_status'));
            }
        },

        invalidate_thermostat_status: function(status) {
            this.$('#temperature').html(this.model.get('currentTermperature'));
            this.$('#temperature-unit').html(this.model.get('unit'));
            this.$('#target-temperature').html(this.model.get('targetTermperature'));
            this.$('#temp-mode').text(this.model.get('tempModeList').get(this.model.get('mode')).attributes.name);
            this.$('#fan-mode').text(this.model.get('fanModeList').get(this.model.get('fanMode')).attributes.name);
            if(this.model.get('showTargetTermperature')){
                this.$('#target-temperature-view').show();
            }else{
                this.$('#target-temperature-view').hide();
            }

            console.log('------', this.model.get('tempModeList'))
            console.log('---- got it!!!', this.model.get('tempModeList').get('1').attributes.name);
            this.$('#temp-mode-view').html(this.template_options({collection:this.model.get('tempModeList'), selected:this.model.get('mode')}));
            this.$('#fan-mode-view').html(this.template_options({collection:this.model.get('fanModeList'), selected:this.model.get('fanMode')}));
        }
    });

    return SwitchControl;
});
