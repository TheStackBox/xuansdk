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
(function ($)
{
    var ajaxReqURL = Kurobox.host + '/cgi-bin/syb_reqresp_cgi?app_id=2000100&module=file_browser_module&method=';

    $('head').append('<link rel="stylesheet" href="/system/global/styles/filebrowser.css"/>');

    var STATIC_OBJECT = null;
    var PREV_ARRAY = null;
    var PREV_OBJECT = null;
    var CURRENT_OBJECT = null;
    
    var $_title = 'Select File';
    
    var $_itemSelectLimit = 0;
    var $_type = null;
    var $_path = null;
    var $_limit = null;
    var $_offSet = null;
    var $_exclude = null;
    var $_fileSelectionOnly = false;
    
    var $mainLayout;
    var $fileBrowserContainer;
    var $fileEveMsgContainer;
    
    var deferredBrowse = null;
    var ajaxReq = null;
    
    // log all ajax send URL
    $(document).ajaxSend(function (evt, request, settings)
    {
        console.log('####AJAX_SEND #: ' + settings.url);
    });

    /******************************************* LOCAL METHOD *******************************************/
    
    // global ajax method 
    // param:
    //  -request: https://.../..../method=(request)
    //  -response: JSON from kurobox
    ajax = function (request, response)
    {
        ajaxReq = $.ajax(
        {
            url: ajaxReqURL + request,
            dataType: 'json',
            xhrFields: {
                withCredentials: true
            },
            error: function (jqXHR, exception)
            {
                if($el('#fileBrowser-loading').is(':visible'))
                    $el('#fileBrowser-loading').hide();
                
                console.log('----------------------');
                console.log('AJAX ERROR');
                
                var error = '';
                
                if (exception === 'abort')
                {
                	console.log(error = 'Ajax request aborted.');
                }
                else if (jqXHR.status === 0) 
                {
                    console.log(error = 'Network not connect.');
                }
                else if (jqXHR.status == 404) 
                {
                    console.log(error = 'Requested page not found [404].');
                }
                else if (jqXHR.status == 500) 
                {
                    console.log(error = 'Internal Server Error [500].');
                }
                else if (exception === 'parsererror') 
                {
                    console.log(error = 'Requested JSON parse failed.');
                }
                else if (exception === 'timeout') 
                {
                    console.log(error = 'Time out error.');
                }
                else 
                {
                    console.log(error = 'Uncaught Error. ' + jqXHR.responseText);
                }
                
                console.log('');
                
                var data = '{"theKuroBox":{"response":{"returnMessage": "'+error+'", "returnValue": 104},"returnValue":104,"returnMessage":"'+error+'","request":"'+request+'"}}';
                
                response(JSON.parse(data));
            },
            success: function (data)
            {
                if($el('#fileBrowser-loading').is(':visible'))
                    $el('#fileBrowser-loading').hide();
                
                console.log('----------------------');
                console.log('AJAX RESPONSE');
                console.log(JSON.stringify(data));
                console.log('');
                
                response(data);
            }
        });
    }
    
    // pageResizeAndClicks : type, filesLen
    // param:
    //  -type: previous,list,view
    //  -filesLen: files array object length from fileBrowser_listFile
    pageResizeAndClicks = function (type, filesLen)
    {
        var $fileBrowserListLi = $el('.fileBrowser-content-li');
        var $fileBrowserListLiContent = $el('.fileBrowser-li-article');
        var $fileBrowserListContentInfo = $el('.fileBrowser-fileInfo');
        var $fileBrowserListContentTick = $el('.fileBrowser-fileTick');
        var $fileBrowserGoBack = $el('.fileBrowserIco-prev2');
        var $fileFolderEmpty =  $el('#fileBrowser-file-message');

        // page resize
        $fileBrowserListLiContent.width(
        $fileBrowserListLi.width() - parseInt($fileBrowserListLi.css('padding-right')) - parseInt($fileBrowserListLi.css('padding-left')));

        $fileBrowserListContentInfo.width(
        $fileBrowserListLiContent.width() - $fileBrowserListContentTick.outerWidth() - parseInt($fileBrowserListContentInfo.css('padding-right')) - parseInt($fileBrowserListContentInfo.css('padding-left')) - 2);

        // on click/tap effect
        $fileBrowserListContentTick.hover(function ()
        {
            $(this).css('margin-left', '2px');
        }, function ()
        {
            $(this).css('margin-left', '0px');
        });

        // on click/tap effect if not on view page : folder clickable
        if (type !== 'view')
        {
            $fileBrowserListContentInfo.hover(function ()
            {
                $(this).css('margin-left', '2px');
            }, function ()
            {
                $(this).css('margin-left', '0px');
            });
        }

        filesLen == 0 ? $fileFolderEmpty.show() : $fileFolderEmpty.hide();
        
        // if previous object holds items, mean can go back to previous page
        PREV_ARRAY.length > 0 ? $fileBrowserGoBack.show() : $fileBrowserGoBack.hide();
        
        
        // bind click event
            // tick
            // item tap
        for (var i = 0; i < filesLen; i++)
        {
            if ($el('#tickID' + i).hasClass('fileBrowser-unticked-dim'))
            {
                $el('#tickID' + i).unbind('click')
            }
            else
            {
                $el('#tickID' + i).unbind('click').bind('click', function ()
                {
                    var selectedItemCount = parseInt($el('.fileBrowser-selectedItem').html());
                    if ($(this).hasClass('fileBrowser-ticked'))
                    {
                        $(this).removeClass('fileBrowser-ticked fileBrowserIco-tick').addClass('fileBrowser-unticked fileBrowserIco-untick');
                        $el('.fileBrowser-selectedItem').html((selectedItemCount - 1) + ' selected item(s)');
                    }
                    else
                    {
                        if(typeof($_itemSelectLimit) == 'number' && $_itemSelectLimit > 0 && selectedItemCount >= $_itemSelectLimit)
                        {
                            fileBrowser_showMessage('Maximum ' + $_itemSelectLimit + ' item(s) can be select');
                        }
                        else
                        {
                            $(this).addClass('fileBrowser-ticked fileBrowserIco-tick').removeClass('fileBrowser-unticked fileBrowserIco-untick');
                            $el('.fileBrowser-selectedItem').html((selectedItemCount + 1) + ' selected item(s)');
                        }
                    }
                });
            }

            if (type !== 'view')
            {
            	$el('#fileID' + i).unbind('click').bind('click', function ()
                {
            		if (CURRENT_OBJECT['files'][(this.id).split('ID')[1]].isDirectory === true || CURRENT_OBJECT['files'][(this.id).split('ID')[1]].isDirectory === 'true')
                    {
                        $el('#fileBrowser-loading').show();
                        var headerTitle = CURRENT_OBJECT['files'][(this.id).split('ID')[1]].filename;

                        ajax('browse_file&offset='+$_offSet+'&limit='+$_limit+'&type='+$_type+'&excludeFiles='+$_exclude+'&path='+CURRENT_OBJECT['files'][(this.id).split('ID')[1]].path,function (data){
                            if(data.theKuroBox.returnValue == '100')
                            {
                            	fileBrowser_setSelectedList(true);
                                fileBrowser_listFile('list', JSON.stringify(data.theKuroBox.response), headerTitle);
							}
                            else
                                fileBrowser_showMessage('Error : '+data.theKuroBox.returnMessage,'error',null);
                        });
                    }
                });
            }
        }
    }
    
    // fileBrowser_listFile : type, data
     // param:
     // -type: previous,list,view
     // -data: if previous: data is get from previous object
     //        if list: data is get from ajax response
     //        if view: data is get from static object (which contain list of selected item)
    
    fileBrowser_listFile = function (type, data, title)
    {
        CURRENT_OBJECT = JSON.parse(decodeURIComponent(data));
        
        var response = null;
        var files = null;
        var fileList = '';
        var fileSelectedCount = null;
        var filesLen = 0;

        response = CURRENT_OBJECT;
        files = response.files;
        fileSelectedCount = 0;

        if (type == 'view')
        {
            //view selected file
            $el('.fileBrowserIco-done').hide();
            $el('.fileBrowserIco-close').hide();
            $el('.fileBrowser-viewSelectedItem').hide();
            $el('.fileBrowser-deselectAll').show();
            $el('.fileBrowser-header-name').html('SELECTED ITEMS');
        }
        else
        {
            var displayName = title ? title : "";
            CURRENT_OBJECT['headerTitle'] = displayName;
            
            //list file or back
            $el('.fileBrowserIco-done').show();
            $el('.fileBrowserIco-close').show();
            $el('.fileBrowser-viewSelectedItem').show();
            $el('.fileBrowser-deselectAll').hide();
            $el('.fileBrowser-header-name').html(displayName || $_title);
        }

        // list file dynamically using file list template
        if (files)
        {
            filesLen = files.length;
            var fileName = '';
            var fileIcon = '';

            for (var i = 0; i < filesLen; i++)
            {
                var showFileTicked = 'fileBrowserIco-untick fileBrowser-unticked';
                var showFilePath = '';
                var showFileClick = '<div class="fileBrowserIco-next2 fileBrowser-fileOpen fileBrowser-fileOpen' + i + '"></div>';
                var filePath = files[i].path;

                if (type == 'view')
                {
                    var pathString = filePath.split('/');
                    var pathStringLen = pathString.length;
                    var minimizedPath = '';

                    // minimize path with /..
                    for (var j = 0; j < pathStringLen; j++)
                    {
                        if (j == 0)
                        {
                            minimizedPath += '/';
                        }
                        else if (j == (1) || j == (pathStringLen - 1))
                        {
                            minimizedPath += '/' + pathString[j];
                        }
                        else
                        {
                            minimizedPath += '/..';
                        }
                    }

                    showFileTicked = 'fileBrowserIco-tick fileBrowser-ticked';
                    showFilePath = '<a>' + minimizedPath + '</a>';
                    showFileClick = '';

                    fileSelectedCount = filesLen;

                    $el('.fileBrowser-selectedItem').html(fileSelectedCount + ' selected item(s)');
                }
                else if (type == 'previous')
                {
                    if (STATIC_OBJECT[filePath] === true)
                    {
                        showFileTicked = 'fileBrowserIco-tick fileBrowser-ticked';
                    }
                }

                if (((files[i].isDirectory + '') == 'true'))
                {
                    if ($_fileSelectionOnly === 'true' || $_fileSelectionOnly === true)
                    {
                        showFileTicked = 'fileBrowserIco-untick fileBrowser-unticked-dim';
                    }
                    fileIcon = 'fileBrowserIco-folder';
                }
                else
                {
                    fileIcon = 'fileBrowserIco-file';
                    showFileClick = ''
                }

                fileList += '<li class="fileBrowser-content-li"><article class="fileBrowser-li-article">' + '<div id="tickID' + i + '" class="fileBrowser-fileTick ' + showFileTicked + ' fileBrowser-fileTick' + i + '"></div>' + '<div id="fileID' + i + '" class="fileBrowser-fileInfo">' + '<div class="' + fileIcon + ' fileBrowser-fileName fileBrowser-fileName' + i + '">' + '<span>' + files[i].filename + '</span>' + showFilePath + '</div>' + showFileClick + '</div></article></li>';
            }
        }

        // file list item click and hover effect
        $el('#fileBrowser-container-content').hide('fast', function ()
        {
            $el('#fileBrowser-container-content').empty().append(fileList + '<li style="height:50px;"></li>').show(0, function ()
            {
                pageResizeAndClicks(type, filesLen);
            });
        });
    }

    // setSelectedList : trackPrevious
     // param:
     // -trackPrevious: true - save current file list to history
     //                 false - dont save file list to history
    
    // logic:
        // a static object will hold list of selected item
        // current object will hold list of current page item
        // previous object will hold array of current object(which can be previous current object)
    
        // compare current object to static object
            //if path same
                // if tick- do nothing
                // if untick- remove from static object
            //if path different
                // if tick then- add to static object
                // if untick- do nothing
    fileBrowser_setSelectedList = function (trackPrevious)
    {
        // save to history for go back function
        if (trackPrevious === true)
        {
            PREV_ARRAY.push(CURRENT_OBJECT);
        }

        var current_selected_files = [];
        var current_files = CURRENT_OBJECT['files'];

        STATIC_OBJECT['path'] = CURRENT_OBJECT['path'];
        STATIC_OBJECT['parent'] = CURRENT_OBJECT['parent'];

        for (var i in current_files)
        {
            var path = current_files[i].path;

            if ($el('#tickID' + i).hasClass('fileBrowser-ticked'))
            {
                //ticked, add to STATIC_OBJECT when path is not existed in list of selected file
                if (addOrRemove(true, path) === true)
                {
                    console.log('--add path:'+current_files[i].path);
                    current_selected_files.push(current_files[i]);
                    STATIC_OBJECT[current_files[i].path] = true;
                }
            }
            else
            {
                //un-tick, try remove from STATIC_OBJECT if previously selected
                addOrRemove(false, path);
            }
        }

        function addOrRemove(selected, token)
        {
            var toAdd = true;
            var selected_files = STATIC_OBJECT['files'];

            for (var j in selected_files)
            {
                var selectedPath = selected_files[j].path;

                if (selectedPath == token && selected === false) 
                {   
                    // remove object from selected list when path is found and un-ticked
                    STATIC_OBJECT['files'].splice(j, 1); console.log('--remove path:'+selectedPath);
                    STATIC_OBJECT[token] = false;
                    break;
                }
                else if (selectedPath == token && selected === true) 
                {
                    // cancel add object to selected list when path is found and ticked
                    toAdd = false;
                }
            }

            return (selected === true && toAdd === true) ? true : false;
        }

        STATIC_OBJECT['files'] = STATIC_OBJECT['files'].concat(current_selected_files);

        return STATIC_OBJECT;
    }

    // open: display file browser and list file
    fileBrowser_open = function ()
    {
        PREV_ARRAY = [];
        PREV_OBJECT = new Object();
        CURRENT_OBJECT = new Object();
        STATIC_OBJECT = new Object();
        STATIC_OBJECT['files'] = [];

        /*
          $('<header id="fileBrowser-container-header">' + 
                '<div class="fileBrowser-container-headerRow1">' + 
                '<span class="fileBrowserIco-prev2" style="cursor:pointer;width:15px;display:inline-block; "></span>' + 
                '<span class="fileBrowser-header-name" style="text-transform:uppercase;">Select File</span></div>' + 
                '<div class="fileBrowser-container-headerRow2" style="position:relative">' + 
                '<div class="fileBrowser-selectedItem" style="position:relative; margin-top:15px; width:130px; padding:0; height:20px;text-align:left; float:left;">0 selected items</div>' + 
                '<div class="fileBrowser-viewSelectedItem" style="cursor:pointer; position:relative;padding:0; margin-top:15px; width:40px;height:20px;text-align:left; float:left">View</div>' + 
                '<div class="fileBrowserIco-done" style="cursor:pointer; position:relative; margin-top:15px; width:10px;height:20px;text-align:center; float:right; font-size:10pt;"></div>' + 
                '<div class="fileBrowserIco-close" style="cursor:pointer; position:relative; margin-top:15px; width:10px;height:20px;text-align:center; float:right; font-size:10pt;"></div>' + 
                '<div class="fileBrowser-deselectAll" style="cursor:pointer; position:relative;padding:0; margin-top:15px; width:130px;height:20px;text-align:right; float:right">Deselect all</div>' + 
                '</div>' + 
                '</header>' + '<ul id="fileBrowser-container-content"></ul>') 
         * */
        
        
        $fileBrowserContainer.empty().append($('<header id="fileBrowser-container-header"><div class="fileBrowser-container-headerRow1"><span class="fileBrowserIco-prev2" style="cursor:pointer;width:15px;display:inline-block; "></span><span class="fileBrowser-header-name" style="text-transform:uppercase;">Select File</span></div><div class="fileBrowser-container-headerRow2" style="position:relative"><div class="fileBrowser-selectedItem" style="position:relative; margin-top:15px; width:130px; padding:0; height:20px;text-align:left; float:left;">0 selected item(s)</div><div class="fileBrowser-viewSelectedItem" style="cursor:pointer; position:relative;padding:0; margin-top:15px; width:40px;height:20px;text-align:left; float:left">View</div><div class="fileBrowserIco-done" style="cursor:pointer; position:relative; margin-top:17px;  margin-right:20px; width:10px;height:20px;text-align:center; float:right; font-size:10pt;"></div><div class="fileBrowserIco-close" style="cursor:pointer; position:relative; margin-top:17px; margin-right:8px; width:10px;height:20px;text-align:center; float:right; font-size:10pt;"></div><div class="fileBrowser-deselectAll" style="cursor:pointer; position:relative;padding:0; margin-top:17px; margin-right:8px; width:120px;height:20px;text-align:right; float:right">Deselect all</div></div></header><ul id="fileBrowser-container-content"></ul>'));

        var $fileBrowserHeader = $el('#fileBrowser-container-header');
        var $fileBrowserHeader1 = $el('.fileBrowser-container-headerRow1');
        var $fileBrowserHeader2 = $el('.fileBrowser-container-headerRow2');
        var $fileBrowserGoBack = $el('.fileBrowserIco-prev2');
        var $fileBrowserList = $el('#fileBrowser-container-content');
        var $fileBrowserDone = $el('.fileBrowserIco-done');
        var $fileBrowserClose = $el('.fileBrowserIco-close');
        var $fileBrowserView = $el('.fileBrowser-viewSelectedItem');
        var $fileBrowserDeselect = $el('.fileBrowser-deselectAll');
        
        $fileBrowserGoBack.hide();
        
        $fileBrowserGoBack.hover(function ()
        {
            $(this).css('margin-left', '2px');
        }, function ()
        {
            $(this).css('margin-left', '0px');
        });
        
        $fileBrowserDone.hover(function ()
        {
            $(this).css('color', '#8b8b8b');
        }, function ()
        {
            $(this).css('color', '#e51a5a');
        });
        
        $fileBrowserClose.hover(function ()
        {
            $(this).css('color', '#8b8b8b');
        }, function ()
        {
            $(this).css('color', '#e51a5a');
        });
        
        $fileBrowserDeselect.hover(function ()
        {
            $(this).css('color', '#8b8b8b');
        }, function ()
        {
            $(this).css('color', '#e51a5a');
        });
        
        $fileBrowserView.hover(function ()
        {
            $(this).css('color', '#8b8b8b');
        }, function ()
        {
            $(this).css('color', '#e51a5a');
        });
        
        $fileBrowserGoBack.unbind('click').bind('click', function ()
        {
            fileBrowser_setSelectedList(false);
            
            if(PREV_ARRAY.length > 0)
            {
                var prevArray = PREV_ARRAY.pop();
                fileBrowser_listFile('previous', JSON.stringify(prevArray), prevArray['headerTitle']);
            }
        });

        $fileBrowserDeselect.unbind('click').bind('click', function ()
        {
            fileBrowser_deselectAll();
        });

        $fileBrowserView.unbind('click').bind('click', function ()
        {
            var obj = fileBrowser_setSelectedList(false);

            if(obj['files'].length > 0 )
                fileBrowser_closeAndView(true); // isView true
            else
                fileBrowser_showMessage('0 selected item(s)','warning',null);
        });

        $fileBrowserClose.unbind('click').bind('click', function ()
        {
            $fileBrowserContainer.hide().empty();
            
            // cancel data
            STATIC_OBJECT['files'] = [];
            deferredBrowse.resolve();
        });

        $fileBrowserDone.unbind('click').bind('click', function ()
        {
            STATIC_OBJECT = fileBrowser_closeAndView(false); // isView false
                    
            if(STATIC_OBJECT)
            {
                $fileBrowserContainer.hide().empty();
                deferredBrowse.resolve();
            }
        });

        $fileBrowserList.css(
        {
            'height': $(window).height() - $fileBrowserHeader.height(),
            'top': $fileBrowserHeader.height()
        });

        $fileBrowserHeader.width(
        $fileBrowserContainer.width())

        $fileBrowserHeader1.width(
        $fileBrowserHeader.width());
        
        //- parseInt($fileBrowserHeader1.css('padding-right')) - parseInt($fileBrowserHeader1.css('padding-left'))

        $fileBrowserHeader2.width(
        $fileBrowserHeader1.width());

        $fileBrowserContainer.show();
        
        // ajax to browse file
        $el('#fileBrowser-loading').show();
        ajax('browse_file&offset='+$_offSet+'&limit='+$_limit+'&type='+$_type+'&excludeFiles='+$_exclude+'&path='+$_path,function (data){
            
            console.log('----------------------');
            console.log('FILE BROWSER BROWSE');
            console.log(JSON.stringify(data));
            console.log('');
            
            if(data.theKuroBox.returnValue == '100')
                fileBrowser_listFile('list', JSON.stringify(data.theKuroBox.response),null);
            else
                fileBrowser_showMessage('Error : '+data.theKuroBox.returnMessage,'error',null);
        });
    }
    
    // closeAndView: share function with close/view file with param isView
    // closeAndView(false) = set selected file list and return
    // closeAndView(true) = set selected file list and display selected file list
    fileBrowser_closeAndView = function (isView)
    {
        STATIC_OBJECT = fileBrowser_setSelectedList(isView);
        
        // is Close Browser
        if (isView === false) return STATIC_OBJECT;

        // is View file
        if(STATIC_OBJECT['files'].length > 0){
            fileBrowser_listFile('view', JSON.stringify(STATIC_OBJECT),null);
        }
        else
        {
            fileBrowser_showMessage('0 item selected','warning',null);
        }
        
        return true;
    }

    // showMessage: notify app msg eg. success, error, warning 
    fileBrowser_showMessage = function (message,type,callback)
    {
        if (type == 'success') color = '#84a403';
        else if (type == 'warning') color = '#e51a5a';
        else if (type == 'error') color = '#BF1919';
        else color = '#373725';

        if(!$fileEveMsgContainer.hasClass('animating'))
        {
		    $el('#eventMsgClose').remove();
            $fileEveMsgContainer.html(message);
			$fileEveMsgContainer.append('<span id="eventMsgClose" class="fileBrowserEventMsgIco-close" style="cursor:pointer; position:relative; width:10px; height:20px; text-align:center; margin-right:10px; float:right; font-size:10pt;"></span>')
            $fileEveMsgContainer.addClass('animating')
            $fileEveMsgContainer.css('background', color);
            $fileEveMsgContainer.css('opacity', 0.9);
            $fileEveMsgContainer.css("top", 0);
            
			$el('#eventMsgClose').unbind('click').bind('click', function ()
			{
				$fileEveMsgContainer.removeClass('animating');
				$fileEveMsgContainer.css("top", (-1 * $fileEveMsgContainer.height()));
				$fileEveMsgContainer.html('');
				if(typeof(callback) == 'function') callback();
			});

            $fileEveMsgContainer.unbind('transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd');
            $fileEveMsgContainer.bind('transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd', function ()
            {
                if($fileEveMsgContainer.hasClass('animating'))
                {
                    setTimeout(function ()
                    {
                        $fileEveMsgContainer.removeClass('animating');
                        $fileEveMsgContainer.css("top", (-1 * $fileEveMsgContainer.height()));
                    }, 2000);
                }
                else
                {
                    $fileEveMsgContainer.html('');
                    if(typeof(callback) == 'function') callback();
                }
            });
        }
        else
        {
            if(typeof(callback) == 'function') callback();
        }
    }
    
    // deselectAll: to untick all selected file from list
    fileBrowser_deselectAll = function ()
    {
        var filesLen = CURRENT_OBJECT['files'].length;
        
        for (var i = 0; i < filesLen; i++)
            $('#tickID' + i).removeClass('fileBrowser-ticked fileBrowserIco-tick').addClass('fileBrowserIco-untick');
        
        $('.fileBrowser-selectedItem').html('0 selected item(s)');
    }
    
    // maxZindex: get max z-index of html element : to make sure file-browser container show on top of it 
    fileBrowser_maxZindex = function ()
    {
        return Math.max.apply(null, $.map($('body > *'), function (e, n)
        {
            if ($(e).css('position') == 'absolute' || $(e).css('position') == 'fixed') return (parseInt($(e).css('z-index')) + 1) || 1;
        }));
    }
    
    function $el(query) {
        return $mainLayout.find(query);
    }
    
    fileBrowser_init = function ()
    {
    	$('body').append($mainLayout = $('<main style="margin:0;padding:0;top:0;bottom:0;left:0;right:0;"><div id="fileBrowser-container" class="fileBrowser-container"></div><div id="fileBrowser-event-message"></div><div id="fileBrowser-file-message">Folder is empty</div><div id="fileBrowser-loading"></div></main>'));
    	$fileBrowserContainer = $el('.fileBrowser-container');
    	$fileEveMsgContainer = $el('#fileBrowser-event-message');
    	$el('#fileBrowser-loading').append('<table height="100%" width="100%"><tr><td align="center" valign="middle"><img src="/system/global/images/filebrowser/loading.gif" alt="loading..." height="56" width="46"><br/><button id="btnAbortAjax" style="float:none;">Cancel</button></td></tr></table>')
    	$fileBrowserContainer.css("z-index", fileBrowser_maxZindex()).height("height", $(document).height()).width("width", $(document).width()).hide();
    	$fileEveMsgContainer.css("z-index", fileBrowser_maxZindex()+1).height(30);

    	$el('#btnAbortAjax').unbind('click').bind('click', function ()
        {
            if (ajaxReq !== null)
            	ajaxReq.abort();
        });
    }

    /******************************************* INITIALIZATION ***********************************/
    $(document).ready(function ()
    {
        fileBrowser_init();
    });
    
    /******************************************* GLOBAL *******************************************/
    $.kbx_filebrowser = function ()
    {
        return 'true';
    };
    
    $.kbx_filebrowser.set_title = (function (title)
    {
        $_title = title || $_title ;
    })
    
    /*Storage Type*/
    $.kbx_filebrowser.storage_type = (function (callback)
    {
        ajaxReqURL = Kurobox.host + '/cgi-bin/syb_reqresp_cgi?app_id=2000100&module=file_browser_module&method=';
        if (typeof (callback) == 'function')
        {
           ajax('get_storage_source_type',function (data){
              callback(data);
           });
        }
    })
    
    /*Get Media Info*/
    $.kbx_filebrowser.get_media_info = (function (type, path, callback)
    {
        ajaxReqURL = Kurobox.host + '/cgi-bin/syb_reqresp_cgi?app_id=2000100&module=file_browser_module&method=';
        if (typeof (callback) == 'function')
        {
           ajax('get_media_info&type='+type+'&path='+path+'',function (data){
              callback(data);
           });
        }
    })
    
    /*Browse*/
    $.kbx_filebrowser.browse = (function (type, path, limit, offSet, exclude, fileSelectionOnly, callback)
    {
        ajaxReqURL = Kurobox.host + '/cgi-bin/syb_reqresp_cgi?app_id=2000100&module=file_browser_module&method=';

       $_type = type+''; 
       $_path = path+''; 
       $_limit = limit+''; 
       $_offSet = offSet+''; 
       $_exclude = exclude+'';
       $_fileSelectionOnly = (fileSelectionOnly === 'true' || fileSelectionOnly === true);
        
       deferredBrowse = null;
       deferredBrowse = $.Deferred(),

       fileBrowser_open();

       $.when(deferredBrowse).done(function () {
           
           if (typeof (callback) == 'function')
           {
               var files = STATIC_OBJECT['files'];

               callback(files);
           }
        });
    })

    //set_select_limit : set max number of selected item
    /*
        Parameter
            -title : Integer. default:0 (no limit)
    */
    $.kbx_filebrowser.set_select_limit = (function (limit)
    {
        $_itemSelectLimit = limit;
    })

    /* 
    if (window.history && window.history.pushState) 
    {
        $(window).on('popstate', function() {
        
          var hashLocation = location.hash;
          var hashSplit = hashLocation.split("#!/");
          var hashName = hashSplit[1];
        
          if (hashName !== '')
          {
            var hash = window.location.hash;
            if (hash === '') {
              alert('Back');
            }
          }
          
        });
        
        window.history.pushState('forward', null, './demo.html');
    }*/
    
})(jQuery);
