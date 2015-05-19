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
    'views/scene.list',
    'models/scene',
    'libs/spin/spin'
], function ($, _, Backbone, JST, ListView, Model, Spinner) {
    'use strict';

    var _spinner_store = {};
    var generate_spinner = function(id) {
        var opts = {
            lines: 11, // The number of lines to draw
            length: 2, // The length of each line
            width: 2, // The line thickness
            radius: 3, // The radius of the inner circle
            corners: 1, // Corner roundness (0..1)
            rotate: 0, // The rotation offset
            direction: 1, // 1: clockwise, -1: counterclockwise
            color: '#000', // #rgb or #rrggbb or array of colors
            speed: 1, // Rounds per second
            trail: 33, // Afterglow percentage
            shadow: false, // Whether to render a shadow
            hwaccel: true, // Whether to use hardware acceleration
            className: 'spinner', // The CSS class to assign to the spinner
            zIndex: 'inherit', // The z-index (defaults to 2000000000)
            top: 'auto', // Top position relative to parent in px
            left: 'auto' // Left position relative to parent in px
        }
        spinner = new Spinner(opts);
        spinner.spin();

        _spinner_store[id] = spinner;

        return spinner;
    }

    var get_spinner = function(id) {
        return _spinner_store[id];
    }

    var destroy_all_spinners = function() {
        _.each(_spinner_store, function(spinner, key) {
            spinner.stop();
            _spinner_store[key] = undefined;
            delete _spinner_store[key];
        })

        _spinner_store = {};
    }

    // model: 'models/scene.js'
    var SceneFeedbackView = Backbone.View.extend({
        className: 'scene-feedback-page',
        template: JST['app/scripts/templates/scene.feedback.ejs'],
        empty_list: JST['app/scripts/templates/scene.feedback.empty.ejs'],
        dialog_prompt_tmpl: JST['app/scripts/common/templates/prompt.dialog.ejs'],
        events: {
            'click #scene-feedback-retry-faulty': 'on_user_retry_all',
            'click #scene-feedback-close': 'on_user_close'
        },
        initialize: function() {
            
        },

        destroy: function() {
            if (this.list_view.data != undefined) {
                this.list_view.data.destroy();
            }
            this.list_view.destroy();

            this.undelegateEvents();
            this.$el.remove();

            destroy_all_spinners();

            // listening to socket
            Kurobox.socket.off('socket:AUTOMATION_SCENE_EXECUTION_RESULT_REMOVED', this.on_feedback_closed, this);
            Kurobox.socket.off('socket:AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_STARTED', this.on_item_retry_started, this);
            Kurobox.socket.off('socket:AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_ENDED', this.on_item_retry_ended, this);
        },

        render: function() {
            this.$el.html(this.template());

            this.list_view = new ListView({
                className: 'row action-item-list',
                tagName: 'ul'
            });
            this.list_view.on('retry', this.on_user_retry_item, this);
            this.list_view.render(this.render_log_item.bind(this), this.empty_list);

            this.$('.body').html(this.list_view.$el);

            this.$el.hide();

            // invalidate navigation bar
            this.invalidate_nav_bar();

            // listening to socket
            Kurobox.socket.on('socket:AUTOMATION_SCENE_EXECUTION_RESULT_REMOVED', this.on_feedback_closed, this);
            Kurobox.socket.on('socket:AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_STARTED', this.on_item_retry_started, this);
            Kurobox.socket.on('socket:AUTOMATION_SCENE_EXECUTION_RESULT_ITEM_RETRY_ENDED', this.on_item_retry_ended, this);
        },

        navigate: function(queryObj) {
            if (this.list_view == undefined) {
                console.error('Run render first!');
                return;
            }

            if (this.scene_data != undefined && this.scene_data.get('id') != queryObj.serId) {
                if (this.list_view != undefined) {
                    console.log('-- refreshing feedback scene')
                    this.list_view.reset();
                    this.list_view.data= undefined;
                }
            }

            if (this.list_view.data == undefined) {
                if (queryObj.serId == undefined) {
                    console.error('No feedback ID')
                    return;
                }

                console.log('-----', queryObj.serId)
                this.scene_data = new Model.model({id: queryObj.serId});
                this.scene_data.fetch_log(queryObj.serId, {
                    success: function() {
                        this.list_view.data = this.scene_data.get('execution');
                        this.list_view.invalidate();

                        this.$el.show();

                        this._invalidate_button_avail();

                        // invalidate navigation bar
                        this.invalidate_nav_bar();
                    }.bind(this),
                    error: function() {
                        window.history.back();
                    }.bind(this)
                })
            } else {

            }
        },

        invalidate_nav_bar: function() {
            if (this.nav != undefined) {
                this.nav.update_buttons(['BACK'], undefined, this.on_user_tap_nav_buttons.bind(this));
                if (this.scene_data != undefined) {
                    this.nav.update_title(this.scene_data.get('name') || 'scene_feedback');
                } else {
                    this.nav.update_title('scene_feedback');
                }
            }
        },

        render_log_item: function(obj) {
            var tmpl = JST['app/scripts/templates/scene.feedback.item.ejs'];

            console.log('obj >>', obj.item)

            var conf = {};
            if (obj.item.get('result').get('status') != 'busy') {
                conf.status = obj.item.get('result').get('status');
            }
            conf.item_idx = obj.options.index;
            conf.idx = obj.options.index;
            conf.label = '['+obj.item.get('device').get('name')+'] ';

            if (obj.item.get('ui_components').length > 1) {
                // more than one user parameters
                conf.label += obj.item.get('label')+' ';
                var length = obj.item.get('ui_components').length;
                obj.item.get('ui_components').each(function(component, index) {
                    conf.label += component.get('label')+' : '+component.toDisplayValue();
                    if (index < length) {
                        conf.label += '; ';
                    }
                })
            } else if (obj.item.get('ui_components').length == 0) {
                // Chuck Norris fill them all
                conf.label += 'Enabled '+obj.item.get('label');
            } else {
                // one parameter only
                conf.label += obj.item.get('label')+ ' : '+obj.item.get('ui_components').models[0].toDisplayValue();
            }

            var $output = $(tmpl(conf));
            if (obj.item.get('result').get('status') == 'busy') {
                this.set_item_spinner(obj.item.index, $output);
            }

            return $output;
        },

        set_item_spinner: function(idx, $item_el) {
            var spinner = get_spinner(idx);
            if (spinner == undefined) spinner = generate_spinner(idx);
            if ($item_el == undefined) $item_el = this.list_view.$('.action-item[data-idx="'+idx+'"]');

            $item_el.find('.status').html(spinner.el).addClass('busy');
            $item_el.find('.label').addClass('fix-busy-status')
        },

        update_item_view: function(idx) {
            var $item_el = this.list_view.$('.action-item[data-idx="'+idx+'"]');

            var $output = this.render_log_item({
                item: this.scene_data.get('execution').at(idx),
                options: {
                    index: idx
                }
            }).first();

            $item_el.html($output.html());
        },

        on_user_retry_item: function(e) {
            var $e = $(e.currentTarget);
            var item = this.list_view.data.at($e.data('method-idx'));

            console.log('-- retrying item index', $e.data('method-idx'), item);
            item.retry();
        },

        on_user_retry_all: function(e) {
            console.log('-- retry all item');
            this.scene_data.retry_all_failed_methods();
        },

        on_user_close: function(e) {
            window.history.back();
        },

        on_user_tap_nav_buttons: function(item, nav) {
            this.on_user_close();
        },

        on_feedback_closed: function(data) {

            if (this._is_socket_data_belong_to_me(data)) {
                console.log('feedback has being removed')

                var okCallback = function() {
                    Shell.hide_message();
                    this.on_user_close();
                }.bind(this)

                Shell.show_message(this.dialog_prompt_tmpl({
                    title: 'feedback_removed',
                    message: 'feedback_removed_msg',
                    icon: 'error'
                }), {
                    'click #ok-btn': okCallback
                },
                okCallback
                )
            }
        },

        on_item_retry_started: function(data) {
            if (this._is_socket_data_belong_to_me(data)) {
                
                var affectedItems = data.seriIndexes;
                console.log('-- feedback item retry started', affectedItems);
                
                // set busy status
                _.each(affectedItems, function(idx) {
                    this.scene_data.get('execution').at(idx).get('result').set('status', 'busy');

                    // invalidate view
                    this.update_item_view(idx);
                }.bind(this))

                // update total execution queued
                this.scene_data.total_execution_queued = affectedItems.length;

                this._invalidate_button_avail();
            }
        },

        on_item_retry_ended: function(data) {
            if (this._is_socket_data_belong_to_me(data)) {
                console.log('-- feedback item retry stopped', data.seriIndex);

                // update item
                this.scene_data.get('execution').at(data.seriIndex).get('result').set('status', data.seriStatus);
                this.scene_data.get('execution').at(data.seriIndex).get('result').set('error', data.seriError);

                this.scene_data.total_execution_queued -= 1;
                console.log('-- total queue left', this.scene_data.total_execution_queued)

                this.scene_data.invalidate_execution_failed_count();
                console.log('-- total error', this.scene_data.total_execution_failed)

                // invalidate view
                this.update_item_view(data.seriIndex);
                this._invalidate_button_avail();
            }
        },

        on_user_acknowledge_prompt_message: function() {
            Shell.hide_message();
        },

        _is_socket_data_belong_to_me: function(data) {
            return (data != undefined && data.serId == this.scene_data.get('serId'))
        },

        _invalidate_button_avail: function() {
            console.log('---> invalidate buttons availablitiliy:', this.scene_data.total_execution_queued, this.scene_data.total_execution_failed)
            if (this.scene_data.total_execution_queued == 0 && this.scene_data.total_execution_failed > 0) {
                this.$('#scene-feedback-retry-faulty').removeAttr('disabled');
                this.$('.retry-btn').removeClass('disabled');
                this.$('.retry-btn').data('event', 'retry');
            } else {
                this.$('#scene-feedback-retry-faulty').attr('disabled', 'disabled');
                this.$('.retry-btn').addClass('disabled');
                this.$('.retry-btn').data('event', '');
            }
        }

    });

    return SceneFeedbackView;
});
