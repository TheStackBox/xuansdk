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

define(["underscore","backbone"], function(_, Backbone) {
    
  // A simple module to replace `Backbone.sync` with *localStorage*-based
  // persistence. Models are given GUIDS, and saved into a JSON object. Simple
  // as that.

  // Hold reference to Underscore.js and Backbone.js in the closure in order
  // to make things work even if they are removed from the global namespace

  // Generate four random hex digits.
  function S4() {
     return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
  };

  // Generate a pseudo-GUID by concatenating random hexadecimal.
  function guid() {
     return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
  };

  Backbone.Kurobox = function() {

  }

  _.extend(Backbone.Kurobox.prototype, {
    
  });

  Backbone.Kurobox.sync = function(method, model, options) {

  }

  return Backbone.Kurobox;

  // ====================
  

  Backbone.LocalStorage = window.Store = function(name) {
    if( !this.localStorage ) {
      throw "Backbone.localStorage: Environment does not support localStorage."
    }
    this.name = name;
    var store = this.localStorage().getItem(this.name);
    this.records = (store && store.split(",")) || [];
  };

  _.extend(Backbone.LocalStorage.prototype, {

    // Save the current state of the **Store** to *localStorage*.
    save: function() {
      this.localStorage().setItem(this.name, this.records.join(","));
    },

    // Add a model, giving it a (hopefully)-unique GUID, if it doesn't already
    // have an id of it's own.
    create: function(model) {
      if (!model.id) {
        model.id = guid();
        model.set(model.idAttribute, model.id);
      }
      this.localStorage().setItem(this.name+"-"+model.id, JSON.stringify(model));
      this.records.push(model.id.toString());
      this.save();
      return this.find(model);
    },

    // Update a model by replacing its copy in `this.data`.
    update: function(model) {
      this.localStorage().setItem(this.name+"-"+model.id, JSON.stringify(model));
      if (!_.include(this.records, model.id.toString()))
        this.records.push(model.id.toString()); this.save();
      return this.find(model);
    },

    // Retrieve a model from `this.data` by id.
    find: function(model) {
      return this.jsonData(this.localStorage().getItem(this.name+"-"+model.id));
    },

    // Return the array of all models currently in storage.
    findAll: function() {
      // Lodash removed _#chain in v1.0.0-rc.1
      return (_.chain || _)(this.records)
        .map(function(id){
          return this.jsonData(this.localStorage().getItem(this.name+"-"+id));
        }, this)
        .compact()
        .value();
    },

    // Delete a model from `this.data`, returning it.
    destroy: function(model) {
      if (model.isNew())
        return false
      this.localStorage().removeItem(this.name+"-"+model.id);
      this.records = _.reject(this.records, function(id){
        return id === model.id.toString();
      });
      this.save();
      return model;
    },

    localStorage: function() {
      return localStorage;
    },

    // fix for "illegal access" error on Android when JSON.parse is passed null
    jsonData: function (data) {
        return data && JSON.parse(data);
    },

    // Clear localStorage for specific collection.
    _clear: function() {
      var local = this.localStorage(),
        itemRe = new RegExp("^" + this.name + "-");

      // Remove id-tracking item (e.g., "foo").
      local.removeItem(this.name);

      // Lodash removed _#chain in v1.0.0-rc.1
      // Match all data items (e.g., "foo-ID") and remove.
      (_.chain || _)(local).keys()
        .filter(function (k) { return itemRe.test(k); })
        .each(function (k) { local.removeItem(k); });

      this.records.length = 0;
    },

    // Size of localStorage.
    _storageSize: function() {
      return this.localStorage().length;
    }

  });

  // localSync delegate to the model or collection's
  // *localStorage* property, which should be an instance of `Store`.
  // window.Store.sync and Backbone.localSync is deprecated, use Backbone.LocalStorage.sync instead
  Backbone.LocalStorage.sync = window.Store.sync = Backbone.localSync = function(method, model, options) {
    var store = model.localStorage || model.collection.localStorage;

    var resp, errorMessage,
      // If $ and $ is having Deferred - use it.
      syncDfd = Backbone.$ && Backbone.$.Deferred && Backbone.$.Deferred();

    try {

      switch (method) {
        case "read":
          resp = model.id != undefined ? store.find(model) : store.findAll();
          break;
        case "create":
          resp = store.create(model);
          break;
        case "update":
          resp = store.update(model);
          break;
        case "delete":
          resp = store.destroy(model);
          break;
      }

    } catch(error) {
        errorMessage = error.message;
    }

    if (resp) {
      if (options && options.success) {
        if (Backbone.VERSION === "0.9.10") {
          options.success(model, resp, options);
        } else {
          options.success(resp);
        }
      }
      if (syncDfd) {
        syncDfd.resolve(resp);
      }

    } else {
      errorMessage = errorMessage ? errorMessage
                                  : "Record Not Found";

      if (options && options.error)
        if (Backbone.VERSION === "0.9.10") {
          options.error(model, errorMessage, options);
        } else {
          options.error(errorMessage);
        }

      if (syncDfd)
        syncDfd.reject(errorMessage);
    }

    // add compatibility with $.ajax
    // always execute callback for success and error
    if (options && options.complete) options.complete(resp);

    return syncDfd && syncDfd.promise();
  };

  Backbone.ajaxSync = Backbone.sync;

  Backbone.getSyncMethod = function(model) {
    if(model.localStorage || (model.collection && model.collection.localStorage)) {
      return Backbone.localSync;
    }

    return Backbone.ajaxSync;
  };

  // Override 'Backbone.sync' to default to localSync,
  // the original 'Backbone.sync' is still available in 'Backbone.ajaxSync'
  Backbone.sync = function(method, model, options) {
    return Backbone.getSyncMethod(model).apply(this, [method, model, options]);
  };

  return Backbone.LocalStorage;
}));