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
], function ($, _, Backbone, JST) {
    'use strict';

    var SceneIconSelector = Backbone.View.extend({
        id: 'scene-icon-selector',
        template: JST['app/scripts/templates/scene.editor.icon-selector.ejs'],
        item_renderer: JST['app/scripts/templates/scene.editor.icon-selector.item.ejs'],
        events: {
            'click .icon-picker-item': 'on_user_selected_icon',
            'click #exit-options': 'on_user_close_this',
        },

        initialize: function(options) {
            this.source = options.source;
            this.parser = options.parser;
        },

        render: function() {
            if (this.source == undefined) {
                console.error('No source has being defined');
                return;
            }

            this.$el.html(this.template());

            if (this.source.constructor == String) {
                // read json file
                $.ajax({
                    url: this.source,
                    dataType: 'json',
                    success: function(data, status, xhr) {
                         console.log('success render')
                        
                        // render it out
                        if (this.parser == undefined) {
                            console.warn('No parser found. Using original data.')
                            this.data = data;
                        } else {
                            this.data = this.parser(data);
                        }

                        console.log('this.data ===', this.data);

                        _.each(this.data, function(item) {
                            this.$('#icon-picker').append(this.item_renderer({id: item}));
                        }.bind(this));

                        _.defer(function() {
                            this.trigger('init');
                        }.bind(this))

                    }.bind(this),
                    error: function(xhr, status, httpErr) {
                        // throw error
                        var err = 'Unable to read icon data file'
                        console.error(err, xhr)
                        this.trigger('error', 'Unable to read icon data file', xhr);
                    }.bind(this)

                })
            } else if (this.source.constructor == Array) {
                console.warn('TODO: use array as data source')
            } else {
                console.error('Unsupported source type')
                this.$el.html('');
            }
        },

        on_user_selected_icon: function(e) {
            var $e = $(e.currentTarget);
            this.trigger('select', $e.data('id'));
        },

        on_user_close_this: function(e) {
            this.trigger('close');
        },

        destroy: function() {
            this.data = undefined;
            this.source = undefined;
            this.parser = undefined;

            this.undelegateEvents();
            this.$el.remove();
        }
    })

    return SceneIconSelector;
});