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

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class LocationManagerService():
    
    @staticmethod
    def get_locations(zoneId=None, offset=0, limit=50, language=None):
        '''
        Get location.
        zoneId: - the specific zone for the location
        offset:Number - offset of the return list. Offset is 0.
        limit:Number - the limit of the return record for every request. Default is 50.
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"dinning_room", "description":"Dinning Room", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"living_room", "description":"Living Room", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_all_locations(language=None):
        '''
        Get location.
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"dinning_room", "description":"Dinning Room", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"living_room", "description":"Living Room", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_locations_with_devices(showEmptyDeviceLocation=True, zoneId=None, offset=0, limit=50, language=None):
        '''
        Get location with device count.
        showEmptyDeviceLocation:Boolean - indicate to show location without device.
        zoneId:Number - the specific zone for the location
        offset:Number - offset of the return list. Offset is 0.
        limit:Number - the limit of the return record for every request. Default is 50.
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"dinning_room", "description":"Dinning Room", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"living_room", "description":"Living Room", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_location_others(zoneId=None, language=None):
        '''
        Get location with device count.
        zoneId:Number - the specific zone for the location
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"dinning_room", "description":"Dinning Room", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"living_room", "description":"Living Room", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_zones(locationId=None, offset=0, limit=50, language=None):
        '''
        Get location.
        locationId:Number - the specific zone for the location
        zoneId:Number - the specific zone for the location
        offset:Number - offset of the return list. Offset is 0.
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"out_door", "description":"Out Door", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"in_door", "description":"In Door", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_zone_details(zoneId=None, language=None):
        '''
        Get zone detail info.
        zoneId:Number - the specific zone for the location
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"out_door", "description":"Out Door", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"in_door", "description":"In Door", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod    
    def get_location_details(locationId=None, language=None):
        '''
        Get location detail info.
        locationId:Number - the specific zone for the location
        language:String - language of the request
        return:Dictionary :eg- [{"id":1, "name":"out_door", "description":"Out Door", "imageURL":"icon1.ico", "modifyTime":"2015-01-30 09:44:24"}, 
                                {"id":2, "name":"in_door", "description":"In Door", "imageURL":"icon2.ico", "modifyTime":"2015-01-30 09:45:24"}]
        '''
        pass

    @staticmethod
    def get_locations_shared_method_groups(language=None):
        '''
        Get shared method group register by locations.
        language:String - language of the request
        return:Dictionary :eg- [{"2": {"parentId": 1,"otherLocation": true,"zoneName": "A place where device's location is not assigned by user","icon": "&#xe6eb","zoneDesc": "A place where device's location is not assigned by user","groupId": 4,"locationId": 2,"name": "2","zoneId": "","label": "Unknown"}},
                                {"4": {"parentId": 1,"otherLocation": true,"zoneName": "Outdoors","icon": "&#xe6eb","zoneDesc": "Outdoors","groupId": 5,"locationId": 4,"name": "4","zoneId": 3,"label": "Back Yard"}}]
        '''
        pass

    @staticmethod
    def add_location(name, description, imageURL, zoneId=None, language=None):
        '''
        add location.
        name: - location name
        description: - location description
        imageURL: - image url to present the location
        zoneId: - the specific zone for the location
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

    @staticmethod
    def add_zone(name, description, imageURL, locationName, locationDesc, locationImageURL, language=None):
        '''
        add zone.
        name: - zone name
        description: - zone description
        imageURL: - image url to present the zone
        locationName: - location name
        locationDesc: - location description
        locationImageURL: - image url to present the location
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

    @staticmethod
    def remove_location(locationId, language=None):
        '''
        remove location.
        locationId: - the target location Id to remove
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

    @staticmethod
    def remove_zone(zoneId, language=None):
        '''
        remove location.
        zoneId: - the target zone Id to remove
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

    @staticmethod
    def update_location(locationId, name="",  description="",  imageURL="",  zoneId=None, language=None):
        '''
        update location.
        locationId: - the target location Id to remove
        name: - location name
        description: - location description
        imageURL: - image url to present the location
        zoneId: - the specific zone for the location
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

    @staticmethod
    def update_zone(zoneId, name, description, imageURL, language=None):
        '''
        update location.
        zoneId: - the target location Id to remove
        name: - location name
        description: - location description
        imageURL: - image url to present the location
        language:String - language of the request
        return:Dictionary :eg- [{"rowId":13, "status":true}]
        '''
        pass

