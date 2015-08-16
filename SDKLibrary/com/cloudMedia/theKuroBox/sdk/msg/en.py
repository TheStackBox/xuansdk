##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

class EN():
    '''
    English Messages.
    '''

    '''
    returnValue_100: OK or success
    returnValue_[101-199]: Firmware General
    returnValue_[401-449]: Firmware WebServer
    returnValue_[450-499]: Firmware Player

    returnValue_[1011-1099]:  Python System
    returnValue_[1201-1399]: Driver and Device
    returnValue_[1401-1499]: Service
    returnValue_[1501-1599]: KBX Param Type
    returnValue_[1601-1699]: Shared Method Manager
    returnValue_[1701-1799]: Database
    returnValue_[1801-1899]: Application Manager
    returnValue_[1901-1999]: File Browser Module
    
    returnValue_[2201-2299]: Virtual Remote Control
    returnValue_[2301-2399]: Notification Manager
    returnValue_[2401-2499]: Event Log Manager
    
    returnValue_[5001-5999]:  theKuroBox User Server
    '''

    returnMsg = {
           "100":"Ok",

           "101":"Pending",
           "102":"Busy",
           "103":"Timeout",
           "104":"Error",
           "105":"Maximum applications reached",
           "106":"Application already running",
           "107":"Application not started",
           "108":"Application not installed",
           "109":"Invalid parameter",
           "110":"Invalid password",
           "111":"Invalid username",
           "112":"Database error",
           "114":"Sandbox error",

           "401":"Session expired",
           "402":"Invalid argument",
           "403":"Invalid login",
           "404":"Maximum users reached",
           "405":"Invalid cookie",
           "406":"Maximum failed login reached\nPlease wait for 30 minutes before retrying",

           "450":"Playback not started",
           
           "501":"Horn is running",
           "502":"Horn not yet run",
           "503":"Dim or Bright are running",
           "504":"X10 security address not yet reset",
           
           "0":"Success",
           "1001":"Unexpected Error Occurred",
           "1002":"Invalid Parameter",
           "1003":"Network Error",
           "1004":"Driver not available",
           
           "1010":"Module not found",
           "1011":"Method not found",
           
           "1030":"Unable to call function",
           "1031":"Missing function",
           "1032":"Function not found",
           "1033":"Target application id not registered",
           "1034":"Event already registered",
           "1035":"Event not found",
           "1036":"Event does not belong to provided application id",
           "1037":"Keep-alive connection found for provided application id",
           "1038":"Unknown source application id",
           "1040":"Event listener registered previously",
           "1041":"Event listener not found",

           "1201":"Fail to pair device",
           "1202":"Device exist",
           "1203":"Device authentication fail",
           "1204":"Pair device abort",
           "1205":"Scan device exist",
           "1206":"Fail to scan device",
           "1207":"Scan device timeout",
           "1208":"Fail to remove device",
           
           "1221":"Connected to another speaker.",
           "1222":"Connecting to another speaker.",
           "1223":"Failed to connect to speaker.",
           "1224":"Failed to disconnect from speaker.",
           "1225":"Switched to another speaker.",

           "1301":"Protocol exist",
           "1302":"Protocol not exist",
           "1303":"Protocol device scanning is started",
           "1304":"Protocol device scanning not started",
           "1305":"Protocol device pairing is running",
           "1306":"Protocol device pairing not started",
           "1307":"Protocol device remove is running",
           "1308":"Protocol device remove not started",
           
           "1351":"Device Controller exist",
           "1352":"Device Controller not exist",
           "1353":"Advance Device Controller exist",
           "1354":"Advance Device Controller not exist",
           
           "1370":"Condition is not fulfilled", # Generic automation condition response

           "1401":"Failed to Register Service.",
           "1404":"Object Not Found",
           "1405":"Operation Failed",
           "1406":"Invalid Parameter",
           "1407":"No Sender Found",
           "1408":"Only one instance is allowed to run at the same time",
           "1409":"Parameter values must be stringified",
           "1410":"Target Recipient Not Found.",

           "1411":"Location Not Found",
           "1412":"Invalid Latitude",
           "1413":"Invalid Longitude",
           "1414":"Invalid Temperature Unit",
           "1415":"No Matched Location Found",
           "1416":"Not a Supported Unit.",
           "1417":"Coordinate must be in earth-like bounds of: Longitude:-180 to 180, Latitude=-90 to 90",
           "1418":"Invalid Location",
           "1419":"Failed To Get Weather",

           "1420":"Failed To Get Twitter Callback URL",
           "1421":"Failed To Add Twitter Sender",
           "1422":"Failed To Send Twitter Notification",
           "1423":"Invalid callback URL.",
           "1424":"Failed To Get Twitter Followers List.",
           "1425":"Failed To Get Twitter Followers Ids",
           "1426":"Server is busy.Please try again later.",
           "1427":"Your Twitter account is suspended and is not permitted to access this feature.",
           "1428":"Failed To Get Rate Limit.",

           "1431":"Service is not available or may be turned off by another user.",
           "1432":"Service Request Timeout",
           "1433":"Target Invalid Response",

           "1440":"Failed To Get Sina Weibo Callback URL",
           "1441":"Failed To Add Sina Weibo Recipient",
           "1442":"Failed To Send Sina Weibo Notification",
           "1443":"Failed To get Sina Weibo user status",
           "1444":"Failed To update status",
           "1445":"Failed To add comment",
           "1446":"Failed To get timeline",
           "1447":"Failed to set Sina Weibo private token",

           "1501":"Invalid data type",
           "1502":"Invalid timestamp",
           "1503":"Invalid value",
           "1504":"Invalid value range",
           "1505":"Invalid value length",
           "1506":"Invalid size of object",
           "1507":"Invalid string format",
           "1508":"Invalid character in string",
           "1509":"Index out of bound or invalid object key",
           "1510":"Duplicated value is not allowed",
           "1511":"Value is required",
           "1512":"Operation failed",

           "1601":"Method Deleted",
           "1602":"Method Inactive",
           "1603":"Invalid Parameter",
           "1604":"Unable to contact system app server",
           "1605":"Unknown error occurred",
           "1606":"Permission denied",
           "1607":"Unable to stringify extra params",
           "1608":"Method not found",
           "1609":"Group not found",
           "1610":"Group is registered",

           "1701":"Failed to store data.",
           "1702":"Database connection failed.",
           "1703":"Failed to version upgrade.",
           "1704":"Failed to create column index.",
           "1705":"Failed to drop column index.",
           "1706":"Failed to create database table.",
           "1707":"Failed to drop database table.",
           "1708":"Execute query failed.",
           "1709":"Failed to update data.",
           "1710":"Failed to get data.",
           "1711":"Failed to delete data.",
           "1712":"Failed to list table from database.",
           "1713":"Failed to update the database setting.",
           "1714":"Operation failed. Either data is exist or invalid parameter value.",
           "1715":"Failed to create triggers.",
           "1716":"Failed to drop triggers.",
           "1717":"Failed to get triggers.",
           "1718":"Failed to enable recursive triggers.",

           "1801":"Application ID not found.",
           "1802":"Unable to read application list.",

           "1901":"Invalid path",
           "1902":"Invalid storage type",
           "1903":"Unable to process file",
           "1904":"Unable to retrieve directory content",
           "1905":"Unable to retrieve file info",

           "2001":"Insteon hub authentication failed.",
           "2002":"Insteon hub access timeout.",
           "2003":"Failed to scan Insteon devices.",
           
           "2100":"Failed to cast to type.",
           "2101":"Section/Option error.",
           
           "2201":"Key recording process is running. Please try again later.",
           "2202":"Unable to add key entry.",
           "2203":"Unable to start record process.",
           
           "2301":"Invalid registration key.",
           "2302":"Maximum listener reached, please try again later.",
 
           "2401":"Archive is disabled",
           "2402":"Archive not available",
           "2403":"Duration is too long. Please specify a external path to store the logs",
           
           "2501":"Invalid pass code.",
           "2502":"Pass code recover email has been set.",
           "2503":"Invalid access token.",
           "2504":"Application is not authorise.",
           "2505":"Exceed api call limit.",
           "2506":"Pass code recover email is not set.",
           "2507":"Old email address is not match.",
           "2508":"Pass code has been set.",
           "2509":"Pass code is not set.",
           "2510":"Invalid Application Id.",
           "2511":"Method is not allow to access by this application.",
           "2512":"Invalid PIN.",
           "2513":"Maximum attempt reached.",
           "2514":"Invalid change request token.",
           
           "2601":"This location already exist in the provided zone.",
           "2602":"This zone already exist."
           }
