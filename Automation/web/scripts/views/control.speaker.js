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
    'models/control.speaker',
    'models/device.api',
    'views/control.speaker.duration_controller',
    'views/component.tab',
    'Kurobox',
    'libs/utils/browser',
    'KuroboxFilebrowser',
], function (_, AbstractCtrl, JST, SpeakerControlModel, DeviceAPIModel, DurationController, TabView, Kurobox) {
    'use strict';
    var spr = AbstractCtrl.prototype;
    var SpeakerControl = AbstractCtrl.extend({
        template: JST['app/scripts/templates/control.speaker.ejs'],
        events: {
            'click #power-btn': 'set_power',
            'mousedown #play-pause-btn': 'set_pause_play',
            'click #enlarge-btn': 'enlarge_control',
            // 'change #volume-control': 'adjust_volume',
            // 'touchend #volume-control': 'volume_up',
            'input #volume-control': 'invalidate_volume_view',
            'click #mute-btn': 'set_mute',
            'click #repeat': 'set_repeat',
            'click #source-btn': 'browse_some_good_song'
        },
        initialize: function() {
            if (BrowserUtil.isMobile()) {
                this.events['touchend #volume-control'] = 'adjust_volume';
            } else {
                this.events['change #volume-control'] = 'adjust_volume';
            }
            spr.initialize.apply(this, arguments);
        },
        render: function() {
            if (this.options.device === undefined) throw 'Undefined paired device';
            this.extended = true;
            this.model = new SpeakerControlModel( this.options.device.get('id') );
            this.model.playback.init_device(
            {
                success: function() {
                    this.methods = new DeviceAPIModel.collection();
                    // check supported api
                    this.methods.fetch('speaker_controller', this.options.device.get('id'), {
                        parse: true,
                        success: function() {
                            // get all playback info
                            this.model.fetch({
                                success: function(){
                                    console.log("result: " + this.model.playback.get('currentTime'));
                                    console.log("result: " + this.model.playback.get('totalTime'));
                                    console.log("result: " + this.model.playback.get('status'));
                                    console.log("result: " + this.model.playback.get('artist'));
                                    console.log("result: " + this.model.playback.get('album'));
                                    console.log("result: " + this.model.volume.get('mute'));
                                    console.log("result: " + this.model.volume.get('volume'));
                                    this._invalidate_ui();
                                }.bind(this),
                                error: function() {
                                    console.log('Error in fetching');
                                }.bind(this)
                            });                           
                        }.bind(this),
                        error: function() {
                            console.log('Unfortunately, getting there seems impossible');
                            this._invalidate_ui();
                        }.bind(this)
                    });        
                }.bind(this),
                error: function(resp) {
                    console.error('Oh well... Can\'t get speaker control profile', resp)
                    console.error('But let it run!')
                    this._invalidate_ui();
                }.bind(this)
            });  
        },

        _invalidate_ui: function() {
            // remove shell global preloading
            Shell.removePreloadingEvents();
            
            // listen to socket
            this.prepareSocketEventHandler();

            // start render view
            this.$el.html(this.template({methods: this.methods, model: this.model, device: this.options.device}));
            _.defer(function() {
                // register playback controller
                this.duration_control = new DurationController(this.$('#play-arc'), this.$('.playtime'), this.model.playback);

                // determine if the playback is playing
                if (this.model.playback.get('status') === 'PLAYING') {
                    // start duration controller
                    this.duration_control.start();
                }
                this.update_pause_play_view(this.model.playback.get('status'))

                // define initial value from API
                this.invalidate_song_info();

                // define initial value from API
                this.volRangeBarWidth = this.$('#range').width();
                console.log('this.volRangeBarWidth', this.volRangeBarWidth);
                console.log('vol', this.model.volume)
                this.update_volume_range(this.model.volume.get('volume'));

                // invalidate mute status
                this.invalidate_mute_status();

                // initialise tab
                this.tab = new TabView({el: this.$('#option-tab'), data: [
                    {label: 'Control', value: 'control', icon: 'control'},
                    {label: 'Queue list', value: 'queue', icon: 'queue'}
                ],
                selected: 0});
                this.tab.on('selected', this.on_user_selected_tab, this);
                this.tab.render();
               
                spr.init.call(this);
            }.bind(this));
        },
        
        destroy: function() {
            // model destroy in superclass
            if (typeof this.methods !== 'undefined') {
                this.methods.destroy();
                this.methods = undefined;
            }

            // stop duration_control
            if (this.duration_control !== undefined) {
                this.duration_control.stop();
            }

            // terminate socket
            Kurobox.socket.stop();
            AbstractCtrl.prototype.destroy.call(this);
        },

        set_power: function() {
            console.log('switch off/on');
            this.is_on = !this.is_on;
            // set api
            // this.model.playback.set_power(this.is_on);
        },

        set_pause_play: function(e) {
            console.log('set_pause_play='+this.model.playback.get('status'))
            try {
                var status;
                switch (this.model.playback.get('status')) {
                    case 'STOPPED':
                    var url = this.model.playback.get('url');
                    if (url === undefined || url === '') {

                        // user choose the song,
                        // grab id3 info
                        this.browse_some_good_song();
                    } else {
                        this.model.playback.play(url);
                        status = 'PLAYING';
                    }
                    break;

                    case 'PAUSED':
                    this.model.playback.resume();
                    status = 'PLAYING';
                    break;

                    case 'PLAYING':
                    this.model.playback.pause();
                    status = 'PAUSED';
                    break;
                }

                this.update_pause_play_view(status);
               } catch (e) {
                console.log('!! '+e);
            }
            
        },

        update_pause_play_view: function(state) {
            console.log('update pause play view='+state)
            switch (state) {
                case 'STOPPED':
                case 'PAUSED':
                this.$('#play-pause-btn').removeClass('play');
                this.$('#play-pause-btn').addClass('pause');
                // this.$('#play-pause-btn').html('&#xe674;');
                break;

                case 'PLAYING':
                this.$('#play-pause-btn').removeClass('pause');
                this.$('#play-pause-btn').addClass('play');
                // this.$('#play-pause-btn').html('&#xe670;');
                break;
            }
        },

        invalidate_song_info: function() {
            console.log('--- song info:')
            console.log('name = '+this.model.playback.get('name'));
            console.log('artist = '+this.model.playback.get('artist'));
            console.log('albumArtURI = '+this.model.playback.get('albumArtURI'));
            console.log('albumArtData=', String(this.model.playback.get('albumArtData')).substring(0, 30))
            console.log('--- [end] song info:')

            this.$('#title').text(this.model.playback.get('name'));
            this.$('#artist').text(this.model.playback.get('artist'));

            if (this.model.playback.get('albumArtData') !== undefined && this.model.playback.get('albumArtData') !== null && this.model.playback.get('albumArtData') !== '') {
                this.$('.cover-art').empty();               
                this.$('.cover-art').css('background-image', 'url(' + this.model.playback.get('albumArtData') + ')');
            } 
            else if (this.model.playback.get('albumArtURI') !== undefined && this.model.playback.get('albumArtURI') !== null && this.model.playback.get('albumArtURI') !== '') {
                this.$('.cover-art').empty();               
                this.$('.cover-art').css('background-image', 'url(' + this.model.playback.get('albumArtURI') + ')');
            }else {
                console.log('Default')
                this.$('.cover-art').html('&#xe6a8');
                this.$('.cover-art').removeAttr('style');
            }
        },

        enlarge_control: function() {
            console.log('max/min control pane');
            var $c = this.$('#song-art');
            this.extended = !this.extended;
            if (this.extended) {
                $c.addClass('control-extended');
                this.$('#enlarge-btn').html('&#xe67a');
            } else {
                $c.removeClass('control-extended');
                this.$('#enlarge-btn').html('&#xe671');
            }
            //$('#song-art').$(this).animate({'height': '250px'});
        },

        adjust_volume: function(e) {
            var $e = $(e.currentTarget);
            console.log('adjust volume ------ ' + $e.prop('value'));
            this.model.volume.save($e.prop('value'));
        },

        volume_up: function(e) {
            var $e = $(e.currentTarget);
            console.log('hand up!', $e.prop('value'));
        },

        invalidate_volume_view: function(e) {
            var $e = $(e.currentTarget);
            this.update_volume_range($e.prop('value'));
        },

        update_volume_range: function(vol) {
            var percentage = (vol / 100) * this.volRangeBarWidth;
            this.$('#range').css('width',percentage);
        },

        set_mute: function() {
            this.model.volume.mute();
            this.invalidate_mute_status();
        },

        invalidate_mute_status: function() {
            console.log('mute', this.model.volume.get('mute'))

            // update mute status
            if (this.model.volume.get('mute')) {
                this.$('#mute-btn').removeClass('disabled');
            } else {
                this.$('#mute-btn').addClass('disabled');
            }
        },

        set_repeat: function() {
            if (this.model.playback.get('repeat') === this.model.playback.REPEAT_NONE) {
                // let's party with one song
                this.model.playback.repeat(this.model.playback.REPEAT_ONE);
            } else {
                // don't brainwash me with the song!
                this.model.playback.repeat(this.model.playback.REPEAT_NONE);
            }

            this.invalidate_repeat();
        },

        invalidate_repeat: function() {
            if (this.model.playback.get('repeat') === this.model.playback.REPEAT_NONE) {
                // let's party with one song
                this.$('#repeat').removeClass('disabled');
            } else {
                // don't brainwash me with the song!
                this.$('#repeat').addClass('disabled');
            }
        },

        browse_some_good_song: function() {
            $('#main-container').hide();
            $.kbx_filebrowser.set_select_limit(1);
            $.kbx_filebrowser.browse('upnp', '', '100', '0', '', true, function(list) {
                console.log('--- list', list)

                if (list !== undefined && list.length === 1) {
                    // got files
                    // get playback info
                    var id3_info = {};
                    var media_path = list[0].path;
                    $.kbx_filebrowser.get_media_info('upnp', media_path, function(info) {
                        console.log('media info', info)
                        if (info.theKuroBox.returnValue === 100) {
                            id3_info.name = info.theKuroBox.response.title;
                            id3_info.artist = info.theKuroBox.response.artist;
                            id3_info.album = info.theKuroBox.response.album;
                            id3_info.albumArtURI = info.theKuroBox.response.albumArt.uri;
                            id3_info.albumArtData = info.theKuroBox.response.albumArt.data;

                            this.model.playback.play(info.theKuroBox.response.path, id3_info);
                            this.update_pause_play_view('PLAYING');
                            // invalidate playback audio info
                            this.invalidate_song_info();

                        } else {
                            console.error('Unable to get media info');
                            // straight play the file
                        }

                        $('#main-container').show();
                    }.bind(this));
                } else {
                    // got no files
                    $('#main-container').show();
                }
            }.bind(this))
        },

        prepareSocketEventHandler: function() {
            Kurobox.socket.verbose = true;
            Kurobox.socket.on('socket:SPEAKER_CONTROLLER_PLAYBACK_INFO_UPDATED', this.on_playback_info, this);
            if (!Kurobox.socket.connected) {
                Kurobox.socket.start();
            }
        },

        on_playback_info: function(resp) {
            //console.log('response', resp.response.pairedDeviceId)
            console.log('[CHECK] ', this.model.playback.get('status'), '|', resp.response.state, '[RESP]', resp.response.pairedDeviceId, '[CURR]', this.options.device.get('id'));
            if (resp.response.pairedDeviceId === this.options.device.get('id') ) {
                //console.log('****resp='+JSON.stringify(resp));
                if( resp.response.state=='BUFFERING' )
                {
                    this.model.playback.set('status', 'STOPPED');
                    this.model.playback.set('currentTime', 0); 
                    this.model.playback.set('totalTime', 0);  
                    this.duration_control.update();
                    this.duration_control.stop();
                    this.duration_control.buffer_init();
                    this.duration_control.buffer_start();
                }
                else if( resp.response.state=='STOPPED' )
                {
                    this.duration_control.buffer_stop();
                    this.on_playback_state_changed(resp);
                }
                else if( this.model.playback.get('status')=='STOPPED' && resp.response.state=='PLAYING' )
                {
                    this.duration_control.buffer_stop();
                    this.on_playback_started(resp);
                    this.on_playback_state_changed(resp);
                    this.on_playback_duration_changed(resp);
                    this.on_volume_changed(resp);
                    this.on_volume_mute_changed(resp);
                }
                else if( this.model.playback.get('status')!=resp.response.state )
                {
                    this.on_playback_state_changed(resp);
                    this.on_playback_duration_changed(resp);
                }
                else if( this.model.volume.get('mute')!=resp.response.mute )
                {
                    this.on_volume_mute_changed(resp);
                }
                else if( this.model.volume.get('volume')!=resp.response.volume )
                {
                    this.on_volume_changed(resp);
                }
                else
                {
                    this.on_playback_duration_changed(resp);
                }
            }
        },

        on_playback_started: function(resp) {
            console.warn('TODO: update new song info to playback model');
            console.log('-- playback started')
            console.log('resp='+JSON.stringify(resp));
            // update playback state
            this.model.playback.set('status', 'PLAYING');
            this.update_pause_play_view('PLAYING');

            console.log('-----------------------------------------');
            console.log('Check on Playback data');
            console.log('current data');
            console.log(this.model.playback.get('url'));
            console.log(this.model.playback.get('name'));
            console.log(this.model.playback.get('album'));
            console.log(this.model.playback.get('albumArtURI'));
            console.log(this.model.playback.get('albumArtData'));
            console.log(this.model.playback.get('artist'));
            console.log('updated data');
            console.log(resp.response.trackURL);
            console.log(resp.response.name);
            console.log(resp.response.album);
            console.log(resp.response.albumArt.uri);
            console.log(resp.response.albumArt.data);
            console.log(resp.response.artist);
            console.log('-----------------------------------------');
            
            //on change if they are differences
            if(
                this.model.playback.get('url')!==resp.response.trackURL ||
                this.model.playback.get('name')!==resp.response.name || 
                this.model.playback.get('album')!==resp.response.album ||
                this.model.playback.get('albumArtURI')!==resp.response.albumArt.uri ||
                this.model.playback.get('albumArtData')!==resp.response.albumArt.data ||
                this.model.playback.get('artist')!==resp.response.artist
              )
            {
                console.log(resp.response.name);
                console.log(resp.response.album);
                console.log(resp.response.albumArt.uri);
                console.log(resp.response.albumArt.data);
                console.log(resp.response.artist);

                this.model.playback.set('name', resp.response.name);
                this.model.playback.set('album', resp.response.album);
                this.model.playback.set('albumArtURI', resp.response.albumArt.uri);
                this.model.playback.set('albumArtData', resp.response.albumArt.data);
                this.model.playback.set('artist', resp.response.artist);
                this.model.playback.set('url', resp.response.trackURL);
                this.invalidate_song_info();
            }

            if (resp.response.totalTime !== undefined) {
                this.model.playback.set('totalTime', resp.response.totalTime);
            } else {
                this.model.playback.set('totalTime', 0);
                console.warn('totalTime is undefined. So duration count is not started');
            }

            this.duration_control.start();
        },

        on_playback_state_changed: function(response) {
            console.log('-- playback state changed')
            console.log('resp='+JSON.stringify(response));
            this.model.playback.set('status', response.response.state);

            if (response.response.state === 'STOPPED' || response.response.state === 'PAUSED') {
                if (response.response.state === 'STOPPED') {
                    // reset currentTime
                    this.model.playback.set('currentTime', 0);
                }
                console.log("[VIEW] call stop");
                console.log("[VIEW] test" );
                this.duration_control.update();
                this.duration_control.stop();
            } else {
                // wait for first duration update
                // clean up current time and total time
                this.model.playback.set('currentTime', 0);
                this.model.playback.set('totalTime', 0);
                console.log("[VIEW] test" );
                this.duration_control.update();
            }

            // update playback state
            this.update_pause_play_view(response.response.state);
        },

        on_playback_duration_changed: function(resp) {
            console.log('-- playback duration changed')
            //console.log('resp='+JSON.stringify(resp));

            if (this.model.playback.get('status') === 'PLAYING') {
                if (this.model.playback.get('totalTime') !== resp.response.totalTime) {
                    // recorrect total time
                    this.model.playback.set('totalTime', resp.response.totalTime);
                }

                if (this.model.playback.get('currentTime') !== resp.response.currentTime) {
                    // current time is diff

                    if (resp.response.currentTime < this.model.playback.get('totalTime')) {
                        this.model.playback.set('currentTime', resp.response.currentTime);
                    } else {
                        this.model.playback.set('currentTime', this.model.playback.get('totalTime'));
                    }
                    console.log("[VIEW] test" );
                    this.duration_control.update();
                }
            }
        },

        on_volume_changed: function(resp) {
            // console.log('volume changed', resp)
             console.log('-- volume changed')
            console.log('resp='+JSON.stringify(resp));

            this.model.volume.set('volume', resp.response.volume);
            var vol = this.model.volume.get('volume');

            // update volume head
            this.$('#volume-control').val(vol);

            // update volume range
            this.update_volume_range(vol);
        },

        on_volume_mute_changed: function(resp) {
            console.log('--- mute changed');
            console.log('resp='+JSON.stringify(resp));
            this.model.volume.set('mute', resp.response.mute);

            // update mute component
            this.invalidate_mute_status();
        }

    });

    return SpeakerControl;
});
