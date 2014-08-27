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