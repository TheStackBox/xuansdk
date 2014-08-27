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
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-collection',
], function (_, KuroboxModel, KuroboxCollection) {
    'use strict';

    // to validate model id
    var validate = function(model) {
        if (model.get('id') === undefined) throw 'Undefined device ID';
    }
    var defaultParam = {
        module: 'device_manager.speaker_controller',
    }

    var _playback = KuroboxModel.extend({
        REPEAT_NONE: 0,
        REPEAT_ONE: 1,
        REPEAT_ALL: 2,

        defaults: {
            currentTime: 0,
            totalTime: 0,
            status: 'STOPPED'
        },

        init_device: function(options) {
            validate(this);
            this.url = "set_init";
            this.dev_opt = {
                param: _.defaults({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        fetch: function(options) {
            validate(this);
            this.parse = this.parse_playback_data;
            this.url = 'get_status';
            this.dev_opt = {
                // url: 'json/example.get_current_playback.json',
                param: _.defaults({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            KuroboxModel.prototype.fetch.call(this, options);
        },

        play: function(url, id3_nfo, options) {
            console.warn('TOOD: api to implement id3 nfo together')
            validate(this);
            if (url === undefined) {
                if (this.get('url') === undefined) {
                    throw 'No playback to play. Define your music';
                } else {
                    // play previous music
                    url = this.get('url');
                }
            }

            if (id3_nfo === undefined) {
                // self-generated
                id3_nfo = {
                    artist: this.get('artist'),
                    album: this.get('album'),
                    albumArtURI: this.get('albumArtURI'),
                    albumArtData: this.get('albumArtData'),
                    name: this.get('name')
                }
            }

            // merge data to self
            this.set('url', url);
            _.each(id3_nfo, function(value, key) {
                this.set(key, value);
            }.bind(this))

            // merge id3 info with url and pairedDeviceId
            // as api parameter
            // _.extend(id3_nfo, {url: url, pairedDeviceId: this.get('id')});
            var albumArtStr = '{\"uri\":\"' + id3_nfo.albumArtURI + '\", \"data\":\"' + id3_nfo.albumArtData + '\"}';
            id3_nfo = {url: url, pairedDeviceId: this.get('id'), name: id3_nfo.name, album: id3_nfo.album, artist: id3_nfo.artist, albumArt: albumArtStr};

            this.url = "set_start";
            this.dev_opt = {
                param: _.defaults(id3_nfo, defaultParam),
                method: 'GET'
            }
            this._plainAPICall(options);
        },

        pause: function(options) {
            validate(this);
            this.url = "set_pause";
            this.dev_opt = {
                param: _.defaults({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                method: 'GET'
            }
            this._plainAPICall(options);
        },

        resume: function(options) {
            validate(this);
            this.url = "set_start";
            this.dev_opt = {
                param: _.defaults({
                    pairedDeviceId: this.get('id')
                },defaultParam),
                method: 'GET'
            }
            this._plainAPICall(options);
        },

        parse: function(data) {
            return data.response;
        },

        parse_playback_data: function(data) {
            this.set('currentTime', data.response.status.currentTime);
            this.set('totalTime', data.response.status.totalTime);
            this.set('state', data.response.status.state);
            this.set('artist', data.response.status.artist);
            this.set('album', data.response.status.album);
            this.set('albumArtURI', data.response.status.albumArt.uri);
            this.set('albumArtData', data.response.status.albumArt.data);
            this.set('name', data.response.status.name);


            return{
                currentTime: data.response.status.currentTime,
                totalTime: data.response.status.totalTime,
                status: data.response.status.state,
                artist: data.response.status.artist,
                album: data.response.status.album,
                albumArtURI: data.response.status.albumArt.uri,
                albumArtData: data.response.status.albumArt.data,
                name: data.response.status.name
            }
        },

        repeat: function(repeatType, options) {
            this.set('repeat', repeatType);

            this.url = 'set_repeat';
            this.dev_opt = {
                param: _.defaults({
                    pairedDeviceId: this.get('id'),
                    repeatOption: this.get('repeat')
                }, defaultParam),
                method: 'GET'
            }

            // call the server man
            this._plainAPICall(options);
        },

        _plainAPICall: function(options) {
            // set custom param by developer
            var param = this._handleParam(this.dev_opt);

            console.log('api call plain stylo: ', this.url, param);
             // call the server
            this._triggerKuroboxApi(this, this.url, param, options, this.dev_opt);
        }

    })

    var _volume = KuroboxModel.extend({
        defaults: {
            volume: 50,
            mute: false
        },
        mute: function(is_mute, options) {
            if (is_mute === undefined) is_mute = !this.attributes.mute;

            this.set('mute', is_mute);

            this.url = 'set_mute_status';
            this.dev_opt = {
                param: _.defaults({
                    pairedDeviceId: this.get('id')
                }, defaultParam),
                param_attr: {
                    mute: 'mute'
                },
                method: 'GET'
            }

            KuroboxModel.prototype.save.call(this, {mute: is_mute}, options)
        },

        save: function(volume, options) {
            validate(this);
            this.set('volume', volume);

            this.url = "set_volume";
            this.dev_opt = {
                param: _.defaults({
                  pairedDeviceId: this.get('id'),
                }, defaultParam),
                param_attr: {
                  volume: 'volume'
                },
                method: 'GET'
            }
            KuroboxModel.prototype.save.call(this, volume, options)
        },

        parse: function(data) {
            this.set('volume', data.response.status.volume);
            this.set('mute', data.response.status.mute);
            return {
                volume: data.response.status.volume,
                mute: data.response.status.mute
            }
        },
    })

    var speaker = function(id, options) {
        this.initialize.apply(this, arguments)
    }

    _.extend(speaker.prototype, {
        initialize: function(id, options) {
            this.playback = new _playback({id: id});
            this.volume = new _volume({id: id});
        },

        fetch: function( options ) {
             this.playback.fetch({
                success: function(m, resp) { 
                    this.volume.parse(resp);
                    if (options !== undefined && options.success !== undefined) options.success();
                }.bind(this),
                error: function(m, resp) {
                    console.error('Failed to fetch playback info');
                    if (options !== undefined && options.success !== undefined) options.error(resp);
                }.bind(this)
            })
        },

        destroy: function() {
            this.playback.destroy();
            this.volume.destroy();
            this.playback = undefined;
            this.volume = undefined;
        }
    });


    return speaker;
});
