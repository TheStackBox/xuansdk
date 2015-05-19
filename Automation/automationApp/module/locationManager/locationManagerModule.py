##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Automation Application.
#
# Xuan Automation Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Automation Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxBoolean import KBXBoolean
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxNumber import KBXNumber
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.service.manager.locationManagerService import LocationManagerService
from com.cloudMedia.theKuroBox.sys import Sys


class LocationManagerModule(Module):

    def __init__(self, kbxModuleName, parentPath):
        super().__init__(kbxModuleName, parentPath)
        self.__pyapi = KBXString(kbxParamName="pyapi", kbxParamIsRequired=False)
        self.__offset = KBXNumber(kbxParamName="offset", kbxParamIsRequired=False)
        self.__limit = KBXNumber(kbxParamName="limit", kbxParamIsRequired=False)
        
        
        self.register_method(kbxMethodName="get_locations",
                             kbxMethodFunc=self.get_locations,
                             kbxMethodParams=[self.__pyapi,
                                              self.__offset,
                                              self.__limit,
                                              KBXNumber(kbxParamName="zoneId", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="get_all_locations",
                             kbxMethodFunc=self.get_all_locations,
                             kbxMethodParams=[self.__pyapi,
                                              self.__offset,
                                              self.__limit])
        
        self.register_method(kbxMethodName="get_locations_with_devices",
                             kbxMethodFunc=self.get_locations_with_devices,
                             kbxMethodParams=[self.__pyapi,
                                              self.__offset,
                                              self.__limit,
                                              KBXBoolean(kbxParamName="showEmptyDeviceLocation", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="zoneId", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="get_location_others",
                             kbxMethodFunc=self.get_location_others,
                             kbxMethodParams=[self.__pyapi,
                                              KBXNumber(kbxParamName="zoneId")])
        
        self.register_method(kbxMethodName="get_zones",
                             kbxMethodFunc=self.get_zones,
                             kbxMethodParams=[self.__pyapi,
                                              self.__offset,
                                              self.__limit,
                                              KBXNumber(kbxParamName="locationId", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="get_zone_details",
                             kbxMethodFunc=self.get_zone_details,
                             kbxMethodParams=[self.__pyapi,
                                              self.__offset,
                                              self.__limit,
                                              KBXNumber(kbxParamName="zoneId")])
        
        self.register_method(kbxMethodName="add_location",
                             kbxMethodFunc=self.add_location,
                             kbxMethodParams=[self.__pyapi,
                                              KBXString(kbxParamName="name"),
                                              KBXString(kbxParamName="description", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="imageURL", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="zoneId", kbxParamIsRequired=False)])
    
        self.register_method(kbxMethodName="add_zone",
                             kbxMethodFunc=self.add_zone,
                             kbxMethodParams=[self.__pyapi,
                                              KBXString(kbxParamName="name"),
                                              KBXString(kbxParamName="description", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="imageURL", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="locationName"),
                                              KBXString(kbxParamName="locationDesc", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="locationImageURL", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="remove_location",
                             kbxMethodFunc=self.remove_location,
                             kbxMethodParams=[self.__pyapi,
                                              KBXNumber(kbxParamName="locationId")])
        
        self.register_method(kbxMethodName="remove_zone",
                             kbxMethodFunc=self.remove_zone,
                             kbxMethodParams=[self.__pyapi,
                                              KBXNumber(kbxParamName="zoneId")])
        
        self.register_method(kbxMethodName="update_location",
                             kbxMethodFunc=self.update_location,
                             kbxMethodParams=[self.__pyapi,
                                              KBXNumber(kbxParamName="locationId"),
                                              KBXString(kbxParamName="name", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="description", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="imageURL", kbxParamIsRequired=False),
                                              KBXNumber(kbxParamName="zoneId", kbxParamIsRequired=False)])
        
        self.register_method(kbxMethodName="update_zone",
                             kbxMethodFunc=self.update_zone,
                             kbxMethodParams=[self.__pyapi,
                                              KBXNumber(kbxParamName="zoneId"),
                                              KBXString(kbxParamName="name", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="description", kbxParamIsRequired=False),
                                              KBXString(kbxParamName="imageURL", kbxParamIsRequired=False)])
     
    def on_system_connected(self):
        super().on_system_connected()
        
        
    def get_locations(self, request):
        try:
            offset = request.get_value("offset")
            limit = request.get_value("limit")
            zoneId = request.get_value("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            locations = LocationManagerService.get_locations(zoneId=zoneId, offset=offset, limit=limit, language=language)
            self.send_response(locations, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def get_all_locations(self, request):
        try:
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            locations = LocationManagerService.get_all_locations(language=language)
            self.send_response(locations, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
            
     
    def get_locations_with_devices(self, request):
        try:
            offset = request.get_value("offset")
            limit = request.get_value("limit")
            zoneId = request.get_value("zoneId")
            showEmptyDeviceLoc = request.get_value("showEmptyDeviceLocation")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            locations = LocationManagerService.get_locations_with_devices(showEmptyDeviceLocation=showEmptyDeviceLoc, zoneId=zoneId, offset=offset, limit=limit, language=language)
            self.send_response(locations, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def get_location_others(self, request):
        try:
            zoneId = request.get_value("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            locations = LocationManagerService.get_location_others(zoneId=zoneId, language=language)
            self.send_response(locations, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def get_zones(self, request):
        try:
            offset = request.get_value("offset")
            limit = request.get_value("limit")
            locationId = request.get_value("locationId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            zones = LocationManagerService.get_zones(locationId=locationId, offset=offset, limit=limit, language=language)
            self.send_response({"zones": zones.get("zones", []), "total":zones.get("total")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def get_zone_details(self, request):
        try:
            zoneId = request.get_value("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            zone = LocationManagerService.get_zone_details(zoneId=zoneId, language=language)
            self.send_response(zone, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    def add_location(self, request):
        try:
            name = request.get_arg("name")
            description = request.get_arg("description")
            imageURL = request.get_arg("imageURL")
            zoneId = request.get_arg("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = self.__add_location(name, description, imageURL, zoneId, language)
            self.send_response({"locationId":result.get("rowId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception as e:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def add_zone(self, request):
        try:
            name = request.get_value("name")
            description = request.get_value("description")
            imageURL = request.get_value("imageURL")
            locationName = request.get_value("locationName")
            locationDesc = request.get_value("locationDesc")
            locationImageURL = request.get_value("locationImageURL")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = LocationManagerService.add_zone(name, description, imageURL, locationName, locationDesc, locationImageURL, language=language)
            self.send_response({"zoneId":result.get("zoneId"), "locationId":result.get("locationId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def remove_location(self, request):
        try:
            locationId = request.get_value("locationId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = LocationManagerService.remove_location(locationId, language=language)
            self.send_response({"locationId":result.get("rowId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def remove_zone(self, request):
        try:
            zoneId = request.get_value("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = LocationManagerService.remove_zone(zoneId, language=language)
            self.send_response({"zoneId":result.get("rowId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def update_location(self, request):
        try:
            locationId = request.get_value("locationId")
            name = request.get_value("name")
            description = request.get_value("description")
            imageURL = request.get_value("imageURL")
            zoneId = request.get_value("zoneId")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = LocationManagerService.update_location(locationId, name, description, imageURL, zoneId, language=language)
            self.send_response({"locationId":result.get("rowId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))

    
    def update_zone(self, request):
        try:
            zoneId = request.get_value("zoneId")
            name = request.get_value("name")
            description = request.get_value("description")
            imageURL = request.get_value("imageURL")
            language = request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE)
            result = LocationManagerService.update_zone(zoneId, name, description, imageURL, language=language)
            self.send_response({"zoneId":result.get("rowId"), "status":result.get("status")}, request.requestId)
        except SystemException as se:
            self.send_response({}, request.requestId, se.value["returnValue"], Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), se.value["returnValue"], se.value["returnMessage"]))
        except Exception:
            self.send_response({}, request.requestId, 1001, Sys.get_message(request.get_arg(AppInfo.REQUEST_KEY_LANGUAGE), 1001, "Unexpected Error Occur"))
    
    
    def __add_location(self, name, description="", imageURL=None, zoneId=None, language=None):
        try:
            return LocationManagerService.add_location(name, description, imageURL, zoneId, language=language)
        except Exception as e:
            raise e
        
        
