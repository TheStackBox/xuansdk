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
    'backbone',
    'libs/backbone/models/kurobox-model',
    'libs/backbone/models/kurobox-core'
], function (_, Backbone, KuroboxModel, Core) {
    'use strict';
    var t = {
        model: KuroboxModel
    };

    // extends with core
    _.extend(t, Core.prototype);

    // extends backbone collection
    return Backbone.Collection.extend(t);
});
