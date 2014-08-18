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
import json

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException


class PanasonicIPCameraService(object):
    '''
    Panasonic IP Camera Service SDK class
    '''
    
    @staticmethod
    def __validate_default_params(isSecured, hostAddress, hostPort):
        '''
        Validate the default parameters and return in tupple
        '''
        pass
    
         
    @staticmethod
    def __validate_result(result):
        '''
        Validate the result returned
        '''
        pass
    
    @staticmethod
    def get_Camera_Name(isSecured, hostAddress, hostPort, username="", password="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraName": {"Data": "CloudMediaPana"}}
        '''
        pass
        

    @staticmethod
    def set_Camera_Name(isSecured, hostAddress, hostPort, username, password, newDeviceName="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        newDeviceName:String :- New name for the device
        return:Dictionary :eg- {"response":{"cameraName": {"Return": "0"}}}
        '''
        pass
    

    @staticmethod
    def get_Camera_White_Balance(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the white balance setting of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraWhiteBalance": {"Data": "32"}}
        '''
        pass
    

    @staticmethod
    def set_Camera_White_Balance(isSecured, hostAddress, hostPort, username, password, whiteBalanceValue='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the white balance setting of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        whiteBalanceValue:String :- 0: Auto, 32: Indoor, 64: Fluorescent light (Day light)
        return:Dictionary :eg- {"cameraWhiteBalance": {"Return": "0"}}
        '''
        pass
    

    @staticmethod
    def get_Camera_Return_Position_And_Time(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the return position and time of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"retPosAndTime": {"RetTime": "0", "RetPos": "0"}}
        '''
        pass
    

    @staticmethod
    def set_Camera_Return_Position_And_Time(isSecured, hostAddress, hostPort, username, password, returnTime, returnPos, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the return position and time of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        returnTime:String :- 0: Do not specify  600: 10 minutes  1800: 30 minutes  3600: 1 hour
        returnPos:String :- 0: Home position 1: Preset 1, 2: Preset 2, 3: Preset 3, 4: Preset 4, 5: Preset 5, 6: Preset 6, 7: Preset 7, 8: Preset 8, 9: Alarm 1, 10: Alarm 2
        return:Dictionary :eg- {"setRetTimeAndPosStatus": {"Return": "0"}}
        '''
        pass
    

    @staticmethod
    def get_Clock_Time(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the clock time of the device
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"currentCamClockTime": {"Data": "201406021115830000"}}
        '''
        pass
    

    @staticmethod
    def set_Clock_Time(isSecured, hostAddress, hostPort, username, password, yearMonthDayHourMinutes='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the clock time of the device
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user       
        yearMonthDayHourMinutes:String :- Date and time in format of yyyymmddHHii
        return:Dictionary :eg- {"setClockTimeStatus": {"Return": "0"}}
        '''
        pass
    

    @staticmethod
    def set_Admin_settings(isSecured, hostAddress, hostPort, username, password, Mode, ID, Password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set Admin settings
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        Mode:String :- Authorization setting. 1: Allow guest users, 3: Do not allow guest users
        ID:String :- Administrator ID (6-15 characters)
        Pass:String :- Administrator password (6-15 characters)
        return:Dictionary :eg- {"adminSettingStatus": {"Return": "0"}}
        '''
        
        pass
    

    @staticmethod
    def get_Preset_information(isSecured, hostAddress, hostPort, username, password, presetKind='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the preset poNumber information
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        presetKind:String :- Preset Number
        return:Dictionary :eg- {"presetInformation": {"Data": "HomePosition"}}
        '''
        pass
    

    @staticmethod
    def restart_Camera(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Restart the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        '''
        pass
    

    @staticmethod
    def camera_Zoom_Control(isSecured, hostAddress, hostPort, username, password, zoomKind='', zoomMode='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the zoom control for the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        zoomKind:String :- 0: General users authorized to control Zoom  1: Administrator
        zoomMode:String :- Zoom Control Mode. 4: ZoomTele, 6: ZoomWide
        return:Dictionary :eg- {"zoomCtrlStatus":{"Return": "0"}}
        '''
        pass
    

    @staticmethod
    def get_network_setting(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE): 
        '''
        Get the network setting
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"zoomCtrlStatus":{"networkSetting": {"Mode": "0", "ConnectType": "1", "Bandwidth": "2147483647"}}}
        '''
        pass
    

    @staticmethod
    def get_camera_model_information(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the model information of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"camModelInfo": {"UserAgent": "Python-urllib/3.3", "fVer": "1.46", 
                                                    "AplFirm": "1.46", "ModelName": "BL-VT164", "Function": "1c02020000",
                                                    "ModelType": "227b001c01020000"}} 
        '''
        pass
    

    @staticmethod
    def create_user(isSecured, hostAddress, hostPort, username, password, newUserNo='', newUserName="", newUserPassword="", newUserLevel='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Create a user account
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        newUserNo:String :- Note 1 General user registration no. 1-50 (However, user registration no. 1: guest user)
        newUserName:String :- User name Note: 6-15 one-byte characters
        newUserPassword:String :- Password Note: 6-15 one-byte characters
        newUserLevel:String :- Access level  1: Level 1 (Camera viewing only)   2: Level 2 (Camera viewing and preset control)   3: Level 3 (Camera viewing and all controls) (Default setting)
        return:Dictionary :eg- {"newUser": {"Return": "0"}}
        '''
        pass
    

    @staticmethod
    def modify_current_user(isSecured, hostAddress, hostPort, username, password, currentUserNo='', modifyUserName="", modifyUserLevel="", modifyUserPassword="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Modify information of a user
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        currentUserNo:String :- User number
        modifyUserName:String :- new user name
        modifyUserLevel:String :- new user level
        modifyUserPassword:String :- new user password
        '''
        pass
    

    @staticmethod
    def delete_current_user(isSecured, hostAddress, hostPort, username, password, currentUserNo='', currentUserName="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Delete an user account
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        currentUserNo:String :- User number
        currentUserName:String :- Existing username
        return:Dictionary :eg- {"deleteUserStatus": {"Return": "0"}} 
        '''
        pass
    

    @staticmethod
    def get_current_user_information(isSecured, hostAddress, hostPort, username, password, currentUserName="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the information fo a user
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        currentUserName:String :- Existing username
        return:Dictionary :eg- {"currentUserInfo": {"UserID": "testing"}}
        '''
        pass
    

    @staticmethod
    def camera_pan_left(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera left
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"panRight": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_pan_right(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera right
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"panRight": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_tilt_up(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera up
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"tiltUp": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_tilt_down(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera down
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"tiltDown": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_home_position(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera to its home position
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"homePosition": {}}
        '''
        pass
    

    @staticmethod
    def camera_reduce_brightness(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reduce brightness level of the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"reduceBrightness": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_default_brightness(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the brightness value of the camera to default value
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"defaultBrightness": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def camera_increase_brightness(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Increase the brightness value of the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"theKuroBox":{"response":{"increaseBrightness": {}},"returnValue":100,"returnMessage":"Ok"}}
        '''
        pass
    

    @staticmethod
    def get_motion_picture(isSecured, hostAddress, hostPort, username, password, pictureResolution="", pictureQuality="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the MJPEG link
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        pictureResolution: 160x120  320x240  640x480
        pictureQuality: Motion (Favor motion)       Standard (Standard quality)      Clarity (Favor clarity)
        return:Dictionary :eg- {"motionPicture": "http://192.168.0.10:80/nphMotionJpeg?Resolution=None&Quality=None"}
        '''
        pass
    

    @staticmethod
    def get_snapshot_picture(isSecured, hostAddress, hostPort, username, password, pictureResolution="", pictureQuality="", language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the link of the snapshot
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        pictureResolution: 160x120  320x240  640x480
        pictureQuality: Motion (Favor motion)       Standard (Standard quality)      Clarity (Favor clarity)
        return:Dictionary :eg- {"snapshot": "http://192.168.0.10:80/SnapshotJPEG?Resolution=None&Quality=None"}
        '''
        pass


    @staticmethod
    def camera_factory_setting(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reset the camera to factory setting
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"factorySetting": {"Return": "0"}}
        '''
        pass
    
    
    @staticmethod
    def set_ntp_server_setting(isSecured, hostAddress, hostPort, username, password, ntpEnable='', ntpServer="", timezone='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the NTP Server
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        NtpEnable:String :- Automatic clock adjustment by NTP server 1: Enable, 0: Disable
        NtpServer:String :- NTP server address or host name
        TimeZone:String :- Note 1 Time zone  -24: GMT-12:00 -23: GMT-11:30  -22: GMT-11:00  -21: GMT-10:30  -20: GMT-10:00 Hawaii  -19: GMT-09:30 -18: GMT-09:00 Alaska  -17: GMT-08:30  -16: GMT-08:00 Pacific Standard Time  -15: GMT-07:30  -14: GMT-07:00 Mountain Standard Time -13: GMT-06:30 -12: GMT-06:00 Central Standard Time  -11: GMT-05:30  -10: GMT-05:00 Eastern Standard Time  -9: GMT-04:30 -8: GMT-04:00  -7: GMT-03:30  -6: GMT-03:00  -5: GMT-02:30 -4: GMT-02:00  -3: GMT-01:30  -2: GMT-01:00  -1: GMT-00:30 0: GMT 00:00 Greenwich Mean Time  1: GMT+00:30  2: GMT+01:00 Central Europe  3: GMT+01:30  4: GMT+02:00 Eastern Europe  5: GMT+02:30 6: GMT+03:00 Baghdad  7: GMT+03:30  8: GMT+04:00  9: GMT+04:30  10: GMT+05:00  11: GMT+05:30  12: GMT+06:00  13: GMT+06:30 14: GMT+07:00  15: GMT+07:30  16: GMT+08:00 China, Western Australia  17: GMT+08:30  18: GMT+09:00 Japan  19: GMT+09:30 Central Australia 20: GMT+10:00 Eastern Australia  21: GMT+10:30  22: GMT+11:00   23: GMT+11:30  24: GMT+12:00
        return:Dictionary :eg- {"ntpServerStatus": {"Return": "0"}}
        '''
        pass
    
    
    @staticmethod
    def get_ntp_server_setting(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the NTP Setting
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"ntpServerSetting": {"NtpEnable": "1", "TimeZone": "16", "NtpServer": "asia.pool.ntp.org"}}
        '''
        pass
    
    
    @staticmethod
    def set_color_night_vision(isSecured, hostAddress, hostPort, username, password, nightVisionEnable='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set whether to ena2ble or disable night vision
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        nightVisionEnable:Number :- 0 (disable) or 1 (enable)
        return:Dictionary :eg- {"nightVisionState": {"Return": "0"}}
        '''
        pass
    
    
    @staticmethod
    def get_color_night_vision(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get night vision setting
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"nightVisionState": {"Data": "1"}}
        '''
        pass
    
    
    @staticmethod
    def get_preset_name(isSecured, hostAddress, hostPort, username, password, presetID='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the preset name
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        presetID:String :- ID of the preset poNumber
        return: Dictionary :eg- {"presetName": {"Return": "HomePosition"}}
        '''
        pass
    
    
    @staticmethod
    def set_image_timestamp_format(isSecured, hostAddress, hostPort, username, password, timestampFormat='', language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        timestampFormat:String :-  0: Do not display, 16: 12 hour time (AM/PM), 32: 24 hour time (Military time)
        return:Dictionary :eg- {"timestampStatus": {"Return": "0"}}
        '''
        pass
    
    
    @staticmethod
    def get_image_timestamp_format(isSecured, hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not
        hostAddress:String :- IP Address or host name of the camera
        hostPort:Number :- Port number of the camera http server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"timestampFormat": {"Data": "16"}}
        '''
        pass
    
    