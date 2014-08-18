##############################################################################################
# Copyright 2014 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
#    Xuan Application Development SDK is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################
from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod


class WeatherService():

    @staticmethod
    def set_location(location, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set weather location
        location:String :- name of a location
        return:Dictionary :eg- {"status": "success"}
        ''' 
        pass
    
    @staticmethod  
    def get_location(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get weather location set
        return:Dictionary :eg- {"location": "london", "longitude": -0.33333000000000002, "id": 7535661, "latitude": 51.566668999999997, "country": "GB"}
        '''
        pass
    
    @staticmethod    
    def set_coordinate(latitude, longitude, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set coordinate
        latitude:Range :- latitude of a location. Range from -90 to 90
        longitude:Range :- longitude of a location. Range from -180 to 180
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod 
    def get_coordinate(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
         get coordinate
         return:Dictionary :eg- {"longitude": 100.48, "latitude": 5.2999999999999998}
        '''
        pass
    
    @staticmethod
    def get_current_weather_by_location_name(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get current weather by location name
        return:Dictionary :eg- {"currentWeather": {"weather_code": 500, "rain": {"3h": 0}, "reference_time": 1401863400, 
                                                   "sunset_time": 1401881384, "detailed_status": "light rain", "pressure": {"sea_level": null, "press": 1006}, 
                                                   "temperature": {"temp_min": 27.0, "unit": "celsius", "temp_kf": 0, "temp_max": 29.0, "temp": 27.84, "location": {"name": "", "country": "Malaysia", 
                                                   "coordinates": {"lat": 5.4199999999999999, "lon": 100.33}, "ID": 1735106}}, "humidity": 83, "sunrise_time": 1401836661, 
                                                   "status": "rain", "snow": "No snow", "weather_icon_name": "10d", "clouds": 75, "wind": {"deg": 320, "speed": 2.1000000000000001}}}
        '''
        pass
    
    @staticmethod    
    def get_snow(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get snow forecast
        return:Dictionary :eg- {"snow": "No snow"}
        '''
        pass
    
    @staticmethod    
    def get_current_temperature(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        return:Dictionary :eg- {"currentTemp": {"temp_max": 29.0, "icon": "10d", "temp_min": 28.0, "unit": "celsius", 
                                                "location": {"name": "George Town", "country": "MY", "coordinates": {"lat": 5.4100000000000001, "lon": 100.34}, 
                                                "ID": 1735106}, "temp": 28.510000000000002, "temp_kf": 0}}
        '''
        pass
    
    @staticmethod
    def get_current_weather_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current weather status
        return:Dictionary :eg- {"currentWeatherStatus": "clouds"}
        '''
        pass
    
    @staticmethod
    def get_humidity(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current weather humidity
        return:Dictionary :eg- {"humidity": 82}
        '''
        pass
    
    @staticmethod
    def get_pressure(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current sea and ground level pressure 
        return:Dictionary :eg- {"pressure": {"sea_level": null, "press": 1013}}
        '''
        pass
    
    @staticmethod    
    def get_detailed_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve detailed status of the weather
        return:Dictionary :eg- {"detailedStatus": "scattered clouds"}
        '''
        pass
    
    @staticmethod
    def get_rain(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve 3 hours rain interval
        return:Dictionary :eg- {"rain": "No rain"}
        '''
        pass
    
    @staticmethod
    def get_wind(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve current wind information
        return:Dictionary :eg- {"wind": {"gust": 1.54, "deg": 150, "speed": 0.51000000000000001}}
        '''
        pass
    
    @staticmethod
    def get_clouds(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        retrieve percentage of clouds
        return:Dictionary :eg- {"cloud": 32}
        '''
        pass
    
    @staticmethod
    def get_sunrise_time(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve sunrise time
        return:Dictionary :eg- {"sunset": "2014-06-04 00:36:14 00"}
        '''
        pass
    
    @staticmethod
    def get_sunset_time(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Retrieve sunset time
        return:Dictionary :eg- {"sunrise": "2014-06-03 09:24:17 00"}
        '''
        pass
    
    @staticmethod
    def get_current_weather_by_coordinates(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        use coordinates instead of location name
        return:Dictionary :eg- {"weatherWithCoor": {"detailed_status": "broken clouds", "reference_time": 1401872400, "wind": {"var_end": 350, "var_beg": 260, "speed": 3.1000000000000001, "deg": 300}, "weather_icon_name": "04d", 
                                                                        "status": "clouds", "pressure": {"press": 1005, "sea_level": null}, "clouds": 75, "weather_code": 803, "snow": "No snow", "rain": "No rain", "humidity": 83, 
                                                                        "sunrise_time": 1401836661, "temperature": {"temp_max": 29.0, "unit": "celsius", "temp_kf": 0, "location": {"country": "MY", "name": "Kampung Sungai Glugur", 
                                                                        "coordinates": {"lat": 5.4199999999999999, "lon": 100.33}, "ID": 1764027}, "temp": 29.0, "temp_min": 29.0}, "sunset_time": 1401881383}}
        '''
        pass
    
    @staticmethod        
    def get_matching_location_name(location, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        this method will get all location matching the location parameter. 
        return:Dictionary :eg- {"matchingLocationName": [{"id": 7535661, "longitude": -0.33333000000000002, "name": "London Borough of Harrow", 
                                                          "latitude": 51.566668999999997, "country": "GB"}, {"id": 1264773, "longitude": 77.283332999999999, 
                                                          "name": "Loni", "latitude": 28.75, "country": "IN"}]}
        '''
        pass
    
    @staticmethod
    def set_location_by_id(locationId, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set weather location by id
        locationId:Number :- locationId
        return:Dictionary :eg- {"status": "success"}
        '''
        pass
    
    @staticmethod        
    def get_daytime_is(daytime, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check daytime is sunrise or sunset
        daytime:String :- 0 =sunrise (Default), 1 =sunset 
        return:Dictionary :eg- {"value": "true"}
        '''
        pass
    
    @staticmethod  
    def get_forecast_humidity_is_above(humidity, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the humidity is above the given value
        humidity:Number :- the humidity value to check: (percentage unit)
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "true"}
        '''
        pass
    
    @staticmethod
    def get_forecast_temperature_is_below(temperature, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the temperature is below the given value
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "false"}
        '''
        pass
    
    @staticmethod  
    def get_forecast_temperature_is_above(temperature, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the humidity is above the given value
        humidity:Number :- the temperature value to check:
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "false"}
        '''
        pass
    
    @staticmethod
    def get_forecast_humidity_is_below(humidity, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the temperature is below the given value
        humidity:Number :- the temperature value to check: 
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "false"}
        '''
        pass
    
    @staticmethod  
    def get_forecast_wind_speed_is_above(speed, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the wind speed is above the given value
        speed:Number :- the wind speed value to check: (unit mph)
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "true"}
        '''
        pass
    
        
    @staticmethod
    def get_forecast_wind_speed_is_below(speed, day, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        check the wind speed is below the given value
        speed:Number :- the wind speed value to check: (unit mph)
        day:Option :- the day for check 1 = Today, 2 = tomorrow, 3 = the 3th day, 4 = the 4th day ... and so on..
        return:Dictionary :eg- {"value": "false"}
        '''
        pass
    
        
    @staticmethod
    def set_service_status(status, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        set service status
        status:Boolean :-Turn on/off the service. 0 = On, 1 = Off
        return:Dictionary :eg- {"status": 1}
        '''
        pass
    
    
    @staticmethod
    def get_service_status(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        get twitter service current status
        return:Dictionary :eg- {"status": 1}
        '''
        pass
    
    
