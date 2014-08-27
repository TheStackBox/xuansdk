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
'use strict';

require.config({
    shim: {
        underscore: {
            exports: '_'
        },
        backbone: {
            deps: [
                'underscore',
                'jquery'
            ],
            exports: 'Backbone'
        },
        bootstrap: {
            deps: ['jquery'],
            exports: 'jquery'
        },
        Kurobox: {
            deps: ['jquery', 'underscore'],
            exports: 'Kurobox'
        },
        KuroboxFilebrowser: {
            deps: ['jquery', 'Kurobox'],
            exports: 'KuroboxFilebrowser'
        },
        infinitescroll: {
            deps: ['jquery'],
            exports: 'jquery'
        },
        toggleswitch: {
            deps: ['jquery'],
            exports: 'toggleswitch'
        },
        moment: {
            exports: 'momment'
        },
         lang: {
            deps: ['jquery'],
            exports: 'lang'
        },
        farbtastic: {
            deps: ['jquery'],
            exports: 'farbtastic'
        },
        mobiscroll: {
            deps: [
                'jquery',
                'mobiscroll_core',
                'mobiscroll_widget',
                'mobiscroll_scroller',

                'mobiscroll_datetime',
                // 'mobiscroll_select',

                // 'mobiscroll_widget_android_holo',
                // 'mobiscroll_widget_android',
                // 'mobiscroll_widget_ios',
                // 'mobiscroll_widget_ios7',
                // 'mobiscroll_widget_jqm',
                // 'mobiscroll_widget_senseui',
                // 'mobiscroll_widget_wp',
            ],
            exports: 'mobiscroll'
        }
    },
    paths: {
        jquery: '../bower_components/jquery/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/underscore/underscore',
        bootstrap: '../bower_components/sass-bootstrap/dist/js/bootstrap',
        infinitescroll: '../bower_components/infinite-scroll/jquery.infinitescroll',
        toggleswitch: 'libs/jquery/jquery.toggleswitch',
        Kurobox: '/system/global/scripts/kurobox',
        KuroboxFilebrowser: '/system/global/scripts/filebrowser',
        eventsource: '../bower_components/EventSource/eventsource',
        knob: '../bower_components/jquery-knob/js/jquery.knob',
        moment: '../bower_components/momentjs/min/moment.min',
        lang: '../bower_components/jquery-lang-js/js/jquery-lang',
        farbtastic: '../bower_components/farbtastic-color-picker/farbtastic',

        mobiscroll_core: '../bower_components/mobiscroll/js/mobiscroll.core',
        mobiscroll_datetime: '../bower_components/mobiscroll/js/mobiscroll.datetime',
        mobiscroll_list: '../bower_components/mobiscroll/js/mobiscroll.list',
        mobiscroll_scroller: '../bower_components/mobiscroll/js/mobiscroll.scroller',
        mobiscroll_select: '../bower_components/mobiscroll/js/mobiscroll.select',
        mobiscroll_widget: '../bower_components/mobiscroll/js/mobiscroll.widget',
        mobiscroll: '../bower_components/mobiscroll/js/mobiscroll.select',
    }
});

require([
    'backbone', 'router', 'lang', 'Kurobox'
], function (Backbone, AppRouter) {
    // setup Kurobox
    Kurobox.app_id = '2000300';

    // setup host name (for development)
    if (typeof PRODUCTION === 'undefined') {
        Kurobox.host = 'https://192.168.0.93';//19'//72';
    }

    var init_app = function() {
        // prepare router
        var router = new AppRouter();
        window.AppRouter = router;
        
        Backbone.history.start();
    }

    console.warn('TODO: read time format')

    console.log('getting language...')
    Kurobox.native('getLanguage', function(currLang){
        console.log('get language!!!!!!!!!!!!!!!!!!!!!!!');
        console.log(currLang);
        var currLang = currLang;

        var mylang = new Lang('df');
            mylang.dynamic(currLang, 'json/language/'+currLang+'.json');
            mylang.attrList.push('data');
            mylang.attrList.push('data-match');
            mylang.loadPack(currLang, function(error){
                if(error){
                    if(currLang == 'en'){
                        init_app();
                    }else{
                        mylang.dynamic('en', 'json/language/en.json');
                        mylang.loadPack('en', function(){
                            init_app();
                            mylang.change('en');
                        }.bind(this))
                    }
                }else{
                    init_app();
                    console.log('no error!!!');
                    mylang.change(currLang);
                }
           }.bind(this))
    }, undefined, 'en')
   // Backbone.history.start();
});
