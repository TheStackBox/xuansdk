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
    'sly'
], function ($, _, Backbone) {console.log();
    'use strict';

  var index;
  var total;
  var container;
  var list;
  var mask;

  var ScrollListView = Backbone.View.extend({
    initialize: function(arguments) {
      console.log('ScrollListView init!!!!!'+arguments);
      
      this.index     = 0;
      
      this.mask      = '#smart';
      this.container = arguments.container;
    },

    start: function() {
      console.log('start!!!!!!!!!!!!19');
      var that   = this;
      this.total = this.list.length;
      $(this.mask).css({height: 50*this.total+this.total});
      $.each(this.list, function( index, value ) {
          // var doc = $(that.item);
          // $(doc).text(value);
          // $(that.container).append(doc);;
          that.create(index);
      });

      this.scroller();
    },

    scroller: function() {
      console.log('scroller!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
      var mask = $(this.mask);
      var that = this;

      mask.sly({
        itemNav: 'basic',
        smart: 0,
        activateOn: 'click',
        mouseDragging: 0,
        touchDragging: 0,
        releaseSwing: 1,
        startAt: 0,
        scrollBy: 1,
        activatePageOn: 'click',
        speed: 300,
        elasticBounds: 1,
        dragHandle: 1,
        dynamicHandle: 1,
        clickBar: 1
        },{
          load: function () {console.log('loaded!!');},
          active: that.onActive.bind(that)
        }
      );

       var item_list = $(this.container).children();
       item_list.on('click', function(){that.onClick('click', item_list.index(this))});
    },

    onActive: function(eventName, itemIndex) {
    },

    onClick: function(eventName, itemIndex) {
    },

    create: function(itemIndex){
    },

    getIndex: function(target){
      mask.sly.index();
      return $(this.container).children().index(target);
    }

  });

  return ScrollListView;
});