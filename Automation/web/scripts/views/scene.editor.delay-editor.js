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
    'templates',
    'views/scene.editor.delay-editor.delay-input',
    'models/scene.action.delay',
    'moment'
], function ($, _, Backbone, JST, TimeComponent, SceneDelayMethod) {
    'use strict';

    var SceneDelayEditor = Backbone.View.extend({
        id: 'scene-delay-editor',
        template: JST['app/scripts/templates/scene.editor.delay-editor.ejs'],
        events: {
            'click #done-btn': 'on_user_confirm_delay'
        },

        destroy: function() {
            this.time_comp.destroy();
            delete this.time_comp;
            this.time_comp = undefined;

            this.action.destroy();
            this.action = undefined;

            this.$el.empty();
            this.$el.remove();
        },

        render: function() {
            this.$el.html(this.template());

            // init time component
            this.time_comp = new TimeComponent({el: this.$('#time-container')});
            this.time_comp.on(this.time_comp.EVT_INVALID, this.time_value_invalid, this);
            this.time_comp.on(this.time_comp.EVT_ERROR, this.time_comp_error, this);
            this.time_comp.on('init', this.on_component_init, this);
        },

        invalidate: function(action) {
            if (action == undefined) {
                console.log('--- create new delay action')
                action = new SceneDelayMethod();
            }
            this.action = action;

            console.log('------ delay action', action.get('params').get('delayInSec'))
            this.time_comp.render(action.get('params').get('delayInSec'));
        },

        on_user_confirm_delay: function() {
            this.action.get('params').get('delayInSec').set('value', this.time_comp.get_value());
            this.trigger('done', this.action);
        }
    })

    return SceneDelayEditor;

});