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
    'moment',
    'knob'
], function (_, moment) {
	'use strict';

	// handle arc drawing and playback

	var DurationController = function() {
		this.initialize.apply(this, arguments);
	}

	_.extend(DurationController.prototype, {
		initialize: function($arcEl, $playTime, model) {
			
			this.$arcEl = $arcEl;
			this.$playTime = $playTime;
			this.model = model;
			this._is_playhead_scrubbing = false;

			// begin knob
			console.log('model', model)
			this.$arcEl.knob({
				'min': 0,
				'max': this.model.get('totalTime'),
				'displayInput': false,
				'release': this.on_knob_release.bind(this),
				'change': this.on_knob_scroll.bind(this),
			})
			this.$arcEl.val(this.model.get('currentTime')).trigger('change')

			// fill in total time and current time in play time
			this.isHourAvail = this.model.get('totalTime') > 3600;
			this.updateDurationInfo();

			// display time display
			console.log('status', this.model.get('status'))
			if (this.model.get('status') === 'STOPPED') {
				this._hide_time_display();
			} else {
				this._show_time_display();
			}

			this.prevTotal = this.model.get('totalTime');
		},

		buffer_init: function() {
			this.bufferLoc = 0;
			this.playbackReady = false;
		},

		buffer_start: function() {
			window.setTimeout(function(){
				if( this.playbackReady==false )
				{
					var max = 150
					var speed = 2;
					this.$arcEl.trigger('configure', {
						max: max,
						cursor: 4
					});

					this.bufferLoc = this.bufferLoc + speed;
					if( this.bufferLoc > max )
						this.bufferLoc = this.bufferLoc - max;

					this.$arcEl.val(this.bufferLoc).trigger('change');
	                this.buffer_start();
	            }
            }.bind(this),150);
		},

		buffer_stop: function() {
			this.playbackReady = true;
			this.$arcEl.trigger('configure', {
				max: 0,
				cursor: 0
			})
		},

		updateDurationInfo: function() {
			this.$playTime.find('#curr-play-time').text(
				this.formatToHMS(this.model.get('currentTime'), this.printDurationFormat())
			);
			this.$playTime.find('#total-time').text(
				this.formatToHMS(this.model.get('totalTime'), this.printDurationFormat())
			);
		},

		formatToHMS: function(inSecond, format) {
			var m = moment({hour: 0, minute: 0, second:0}).second(inSecond);
			return m.format(format);
		},

		printDurationFormat: function() {
			return this.isHourAvail ? 'hh:mm:ss' : 'mm:ss';
		},

		update: function(_resetTimer) {
			_resetTimer = _resetTimer || true;

			var current = this.model.get('currentTime');
			var total = this.model.get('totalTime');

			// updatee total time
			if (current <= total) {
				if (total !== this.prevTotal) {
					this.$arcEl.trigger('configure', {
						max: total,
						cursor: 0
					})
					this.prevTotal = total;
				}

				// update playhead
				if (!this._is_playhead_scrubbing) {
					this.$arcEl.val(current).trigger('change');
				}

				// update duration info
				this.updateDurationInfo();

				// reset timer
				if (_resetTimer) {
					this._stop_interval();
					this._start_interval();
				}

				// force show playtime
				this._show_time_display();
			}
		},

		_update_stepper: function() {
			var current = this.model.get('currentTime');
			this.model.set('currentTime', ++current);
			this.update(false);
		},

		_stop_interval: function() {
			clearInterval(this.intv);
			this.intv = undefined;
		},

		_start_interval: function() {
			this.intv = setInterval(this._update_stepper.bind(this), 1000);
		},

		_hide_time_display: function() {
			this.$playTime.hide();
		},

		_show_time_display:function() {
			this.$playTime.show();
		},

		start: function() {
			this._start_interval();
			this.update();
			this._show_time_display();
		},

		stop: function() {
			this._stop_interval();
			if (this.model.get('status') === 'STOPPED') {
				this._hide_time_display();
			}
		},

		on_knob_release: function(target_time) {
			this.model.set('currentTime', target_time);
			this._is_playhead_scrubbing = false;

			if (this._isRunning) {
				this._start_interval();
				this._isRunning = false;
			}
		},

		on_knob_scroll: function() {
			this._is_playhead_scrubbing = true;

			// stop timer
			if (this.intv !== undefined) {
				this._isRunning = true;
				this._stop_interval();
			}
		}

	})

	return DurationController;
});
