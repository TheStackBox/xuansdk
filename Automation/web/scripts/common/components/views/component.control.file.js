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
    'common/components/views/component.control.abstract',
    'templates',
    'common/components/models/kbx.input-text',
    'KuroboxFilebrowser'
], function ($, _, AbstractControlComponent, JST, InputTextModel) {
    'use strict';

    var kbxTextInput = AbstractControlComponent.extend({
        template: JST['app/scripts/common/components/templates/component.control.file.ejs'],
        events: {
            'click #browse-btn':'init_filebrowser',
        },
    	render: function(model) {
            this.model = model;

            console.warn('TODO: check classname before proceed')
            console.log('className', model.className)
            console.log('model', model.attributes)

            this.maxSelect = this.model.get('extra').kbxParamMaxSize || 1;
            if (typeof this.model.get('extra').kbxParamBrowseTypes === 'string') {
                this.browseType = this.model.get('extra').kbxParamBrowseTypes;
            } else if (typeof this.model.get('extra').kbxParamBrowseTypes === 'object' && typeof this.model.get('extra').kbxParamBrowseTypes.length > 0) {
                // array
                // support the first selection
                this.browseType = this.model.get('extra').kbxParamBrowseTypes[0];
            } else {
                this.browseType = 'upnp';
            }
            this.startPath = (typeof this.model.get('extra').kbxParamBrowsePath === 'undefined') ? '' : this.model.get('extra').kbxParamBrowsePath;
            this.extFilter = (typeof this.model.get('extra').kbxParamFilters === 'undefined') ? '' : this.model.get('extra').kbxParamFilters;
            this.fileSelectionOnly = (typeof this.model.get('extra').kbxParamSelectDirectories === 'undefined') ? true : !this.model.get('extra').kbxParamSelectDirectories;

            this.selected_items = new this.model.valueLabelClass();

            if (this.model.get('value').length > 0) {
                // select value
                this.selected_items = this.model.get('value')
            } else {
                // select default value
                this.selected_items = this.model.get('default_value')
            }

            this.$el.html(this.template());

            // output to ui
            this.invalidate_selected_items();

            this.trigger(this.EVT_INIT);

            this.validate();
        },

        get_value: function() {
            if (this.validate()) {
                return this.selected_items;
            }

            return;
        },

        validate: function() {
            var valid = (this.selected_items !== undefined && this.selected_items.length > 0);
            console.log('--- validate', valid)
            if (!valid) {
                this.trigger(this.EVT_INVALID);
            } else {
                this.trigger(this.EVT_VALID);
            }
            return valid;
        },

        init_filebrowser: function() {
            $.kbx_filebrowser.set_select_limit(this.maxSelect);         
            $.kbx_filebrowser.browse(this.browseType, this.startPath, '100', '0', '', this.extFilter, this.fileSelectionOnly, function(list) {
                if (list !== undefined && list.length > 0) {
                    // got files
                    this.selected_items = new this.model.valueLabelClass();
                    _.each(list, function(file) {
                        this.selected_items.add({value: file.path, label: file.filename, isDirectory: file.isDirectory, fileType: this.browseType});
                    }.bind(this))

                    // validate selected item
                    this.invalidate_selected_items();

                } else {
                    // got no files
                }

                // throw back
                this.validate();
            }.bind(this))
        },

        invalidate_selected_items: function() {
            if (this.selected_items !== undefined && this.selected_items.length > 0) {
                var s = '';
                var len = this.selected_items.length - 1;
                this.selected_items.each(function(item, idx) {
                    console.log('item',idx, item);
                    s += item.get('label');
                    if (idx < len) {
                        s += ', ';
                    }
                }.bind(this))

                this.$('#value-txt').text(s);
                this.$('#desc-txt').text(this.model.get('extra').kbxParamDesc);
            } else {
                // show description
                this.$('#desc-txt').text(this.model.get('extra').kbxParamDesc);
            }
        }
    })

    return kbxTextInput;
});