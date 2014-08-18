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
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException


class FoscamF19821wService(object):
    '''
    SDK Service for Foscam HD API
    '''
    @staticmethod
    def __validate_default_params(isSecured, host, port):
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
    def __check_is_enabled_key_valid(value):
        '''
        Check whether the value is 1 or 0 
        '''
        pass
    
    
    @staticmethod
    def __check_range(rangeValue, minValue, maxValue):
        '''
        Return the value if its in range, else raise exception
        '''
        pass
    
    
    @staticmethod
    def __check_is_in_options(optionValue, *options):
        '''
        Check whether option value in options
        '''
        pass
    
    
    @staticmethod
    def get_image_setting(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''    
        Get image setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"imageSettings": {"CGI_Result": {"hue": "50", "saturation": "45", "sharpness": "50", 
                                "denoiseLevel": "50", "result": "0", "contrast": "50", "brightness": "30"}}}
        '''
        pass
    
        
    @staticmethod
    def set_brightness(isSecured, host, port, username, password, brightnessValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set brightness
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        brightnessValue:String :- 1 - 100
        return:Dictionary :eg- {"setBrightnessStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_contrast(isSecured, host, port, username, password, constrastValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set contrast
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        constrastValue:String :- 1 - 100
        return:Dictionary :eg- {"setContrastStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_hue(isSecured, host, port, username, password, hueValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set hue
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        hueValue:String :- 1 - 100
        return:Dictionary :eg- {"setHueStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_saturation(isSecured, host, port, username, password, saturationValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set saturation
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        saturationValue:String :- 1 - 100
        return:Dictionary :eg- {"setSaturationStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_sharpness(isSecured, host, port, username, password, sharpnessValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set sharpness
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        sharpnessValue:String :- 1 - 100
        return:Dictionary :eg- {"setSharpnessStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def reset_image_setting(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Reset image setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"resetImageSettingStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_mirror_and_flip_settings(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get mirror / flip setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"mirrorAndflipSetting": {"CGI_Result": {"result": "0", "isMirror": "0", "isFlip": "0"}}}
        '''
        pass


    @staticmethod
    def mirror_video_display(isSecured, host, port, username, password, isMirror, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set mirror display enable or not
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isMirror:String :- 0 disable, 1 enable
        return:Dictionary :eg- {"mirrorVideoStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def flip_video_display(isSecured, host, port, username, password, isFlip, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set flip display enable or not
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isFlip:String :- 0 disable, 1 enable
        return:Dictionary :eg- {"flipVideoStatus": {"CGI_Result": {"result": "0"}}} 
        '''
        pass


    @staticmethod
    def set_sensor_power_frequency(isSecured, host, port, username, password, frequencyValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set sensor power frequency
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        frequencyValue:String :- 0 : 60 HZ, 1 : 50 HZ
        return:Dictionary :eg- {"setSensorPowerFrequencyStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_video_stream_parameters(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the video stream parameters
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getVideoStream": {"CGI_Result": {"GOP2": "30", "GOP3": "60", "GOP0": "30", "GOP1": "30", 
                                                                    "resolution1": "0", "resolution0": "0", "resolution3": "0", 
                                                                    "resolution2": "0", "result": "0", "frameRate1": "30", "frameRate0": "30", 
                                                                    "frameRate3": "10", "frameRate2": "30", "bitRate1": "2097152", "bitRate0": "2097152", 
                                                                    "bitRate3": "204800", "bitRate2": "2097152", "isVBR0": "1", "isVBR1": "1", 
                                                                    "isVBR2": "1", "isVBR3": "1"}}}
        '''
        pass


    @staticmethod
    def set_video_stream_parameters(isSecured, host, port, username, password, streamType, resolution, bitRate, frameRate, GOP, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set video stream parameters
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        streamType:String :- 0~3
        resolution:String :- Resolution of stream type N
        bitRate:String :- Bit rate of stream type N (20480~2097152)
        frameRate:String :- Frame rate of stream type N
        GOP:String :- P frames between I frame of stream type N The suggest value is: X * frameRate
        return:Dictionary :eg- {"setVideoStreamStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_main_video_stream_type(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get main video stream type
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getVideoStreamStatus": {"CGI_Result": {"result": "0", "streamType": "2"}}}
        '''
        pass


    @staticmethod
    def get_sub_video_stream_type(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get sub video stream type
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getSubVideoStreamStatus": {"CGI_Result": {"result": "0", "streamType": "3"}}}
        '''
        pass


    @staticmethod
    def set_main_video_stream_type(isSecured, host, port, username, password, streamType, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set main video stream type
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        streamType:String :- 0-3
        return:Dictionary :eg- {"setMainVideoStreamtypeStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_sub_video_stream_type(isSecured, host, port, username, password, videoFormat, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set sub video stream type
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        videoFormat:String :- 0:H264,  1:MotionJPEG
        return:Dictionary :eg- {"setSubVideoStreamtypeStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_motion_jpeg_stream(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get MJPEG Stream URL
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getMotionJpeg": "http://192.168.0.82:88/cgi-bin/CGIStream.fcgi?usr=admin&cmd=GetMJStream&pwd=admin"}
        '''
        pass


    @staticmethod
    def get_OSD_setting(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get OSD Setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"osdSettings": {"CGI_Result": {"result": "0", "isEnableDevName": "1", "isEnableOSDMask": "0", 
                                                "isEnableTimeStamp": "1", "dispPos": "0"}}}
        '''
        pass


    @staticmethod
    def set_OSD_setting(isSecured, host, port, username, password, isEnableTimeStamp, isEnableDevName, dispPos, isEnableOSDMask, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set OSD Setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isEnableTimeStamp:String :- 0 to disable and 1 to enable
        isEnableDevName:String :- 0 to disable and 1 to enable
        dispPos:String :- display position of camera, 0 to disable and 1 to enable
        isEnableOSDMask:String :- 0 to disable and 1 to enable
        return:Dictionary :eg- {"setOSDSettingStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_OSD_mask_area(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get OSD Mask are
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"osdMaskArea": {"CGI_Result": {"y2_3": "0", "x1_0": "100", "x1_1": "100", "x1_2": "100", 
                                                "x1_3": "0", "y2_0": "200", "y2_1": "110", "x2_1": "100", "x2_0": "200", 
                                                "y1_3": "0", "y1_2": "0", "y1_1": "100", "y1_0": "100", "x2_3": "0", 
                                                "result": "0", "y2_2": "0", "x2_2": "0"}}}
        '''
        pass


    @staticmethod
    def set_OSD_mask_area(isSecured, host, port, username, password, x1_0, y1_0, x2_0, y2_0, x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2, x1_3, y1_3, x2_3, y2_3, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set OSD Mask area
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        x1_N:String:String :- x1_N top left X position of mask N, y1_N top left y position of mask N, x2_N bottom right x position of mask, y2_N bottom right y position of mask,  
        return:Dictionary :eg- {"setOSDMaskAreaStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_motion_detection_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get motion detection configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"motionDetectionConfig": {"CGI_Result": {"area8": "0", "area9": "0", "area4": "0", 
                                                           "area5": "0", "area6": "0", "area7": "0", "area0": "1", 
                                                           "area1": "0", "area2": "2", "area3": "4", "isEnable": "1", 
                                                           "sensitivity": "3", "triggerNumbererval": "10000", "schedule5": "0", 
                                                           "schedule0": "1", "schedule1": "0", "schedule2": "2", 
                                                           "schedule3": "4", "schedule4": "0", "schedule6": "0", 
                                                           "linkage": "0", "result": "0", "snapNumbererval": "5000"}}}
        '''
        pass


    @staticmethod
    def set_motion_detection_configuration(isSecured, host, port, username, password, isEnable, linkage, snapNumbererval, sensitivity, triggerNumbererval, schedules=[], areas=[], language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set motion detection configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isEnable:String :- Is enable motion detect alarm 1:0
        linkage:String :- Motion alarm linkage ( bit3 | bit2 | bit1 | bit0 ) bit0:Ring | bit1:Send mail | bit2:Snap picture | bit3:Record
        snapNumbererval:String :- The Numbererval time to snap picture again
        sensitivity:String :- Motion detect sensitivity 0 : Low | 1: Normal | 2: High | 3: Lower | 4: Lowest
        triggerNumbererval:String :- The time of which motion detect alarm can trigger again when a motion detection has happened
        schedules:String :- The motion alarm schedule of one week
        areas:String :- The area info
        return:Dictionary :eg- {"setMotionDetectionStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_snapshot_config(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get snapshot configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"snapshotConfig": {"CGI_Result": {"result": "0", "saveLocation": "2", "snapPicQuality": "0"}}}
        '''
        pass


    @staticmethod
    def set_snapshot_config(isSecured, host, port, username, password, snapPicQuality, saveLocation, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set snapshot configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        snapPicQuality:String :- 0:Low quality 1:Normal quality 2:High quality
        saveLocation:String :- 0:Save to sd card 1:Not in use now 2:Upload to FTP
        return:Dictionary :eg- {"snapshotConfigStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def snap_picture_same_as_main_stream(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get snapshot URL 1
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"snapPicAsMainStream": "http://192.168.0.82:88/cgi-bin/CGIProxy.fcgi?usr=admin&cmd=snapPicture&pwd=admin"}
        '''
        pass


    @staticmethod
    def snap_picture_by_jpeg_format(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get snapshot URL 2
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"snapPicAsMainStream": "http://192.168.0.82:88/cgi-bin/CGIProxy.fcgi?usr=admin&cmd=snapPicture&pwd=admin"}
        '''
        pass


    @staticmethod
    def get_record_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get record list
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"recordList": {"CGI_Result": {"totalCnt": "0", "curCnt": "0", "result": "0", "record8": null, 
                                                               "record9": null, "record6": null, "record7": null, "record4": null, 
                                                               "record5": null, "record2": null, "record3": null, "record0": null, 
                                                               "record1": null}}}
        '''
        pass


    @staticmethod
    def get_alarm_record_config(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get alarm record configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"alarmRecordConfig": {"CGI_Result": {"result": "0", "preRecordSecs": "5", "alarmRecordSecs": "30", "isEnablePreRecord": "1"}}}
        '''
        pass


    @staticmethod
    def set_alarm_record_config(isSecured, host, port, username, password, isEnablePreRecord, preRecordSecs, alarmRecordSecs, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set alarm record configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isEnablePreRecord:String :- 0:Disable 1:Enable
        preRecordSecs:String :- Pre recording seconds 
        alarmRecordSecs:String :- Alarm record seconds
        return:Dictionary :eg- {"alamRecordConfigStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_io_alarm_config(isSecured, host, port, username, password, isEnable, linkage, alarmLevel, snapNumbererval, triggerNumbererval, schedules=[], language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set IO alarm configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        alarmLevel:String :- 0 : low, 1 : high
        linkage:String :- wxyz in binary bits (0 - 15), w:Ring, x:Send mail, y:Snap picture, z:Record
        snapNumbererval:String :- Numbererval to snap picture
        triggerNumbererval:String :- Numbererval to trigger alarm again
        schedules:String :- N(0-6) alarm schedule
        return:Dictionary :eg- {"alamIOConfigStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_io_alarm_config(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get IO alarm configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"ioAlarmConfig": {"CGI_Result": {"schedule0": "0", "schedule1": "0", "schedule2": "0", 
                                                   "schedule3": "0", "schedule4": "0", "schedule5": "0", "linkage": "16", 
                                                   "result": "0", "schedule6": "0", "triggerNumbererval": "5", "isEnable": "1", 
                                                   "alarmLevel": "1", "snapNumbererval": "2"}}}
        '''
        pass


    @staticmethod
    def clear_io_alarm_output(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Clear IO alarm output
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"clearIoAlarmOutputStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_multi_device_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the list of device in the multi device setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"multiDeviceList": {"CGI_Result": {"dev3": "+", "dev2": "+", "dev1": "Foscam 8910+192.168.0.10", 
                                                                    "dev0": "+", "dev7": "+", "dev6": "+", "dev5": "+", 
                                                                    "dev4": "+", "result": "0", "dev8": "+"}}}
        '''
        pass


    @staticmethod
    def get_multi_device_detail(isSecured, host, port, username, password, channelNo, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the divce information of the device in the multi device setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        channelNo:String :- Device location 
        return:Dictionary :eg- {"multiDeviceList": {"CGI_Result": {"dev3": "+", "dev2": "testing+192.168.1.3", 
                                                                    "dev1": "Foscam 8910+192.168.0.10", "dev0": "+", 
                                                                    "dev7": "+", "dev6": "+", "dev5": "+", "dev4": "+", 
                                                                    "result": "0", "dev8": "+"}}}
        '''
        pass


    @staticmethod
    def add_multiple_device(isSecured, host, port, username, password, channelNo, productType, ip, devicePort, mediaPort, userName, passWord, devName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Add a device Numbero mutli device setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        channelNo:String :- Channel number for new device
        productType:String :- Device type
        ip:String :- New device IP Address
        devicePort:String :- New device port number
        mediaPort:String :- New device media port number
        userName:String :- New device username
        passWord:String :- New device password
        devName:String :- New device name
        return:Dictionary :eg- {"newMultiDeviceStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def delete_multiple_device(isSecured, host, port, username, password, channelNo, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Remove a device from multi device setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        channelNo:String :- Channel number of device
        return:Dictionary :eg- {"deleteDeviceStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def add_new_user_account(isSecured, host, port, username, password, usrName, usrPwd, privilege, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Create a new user account
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- New username for specific user
        usrPwd:String :- New password for specific user
        privilege:String :- 0 : Visitor, 1 : Operator, 2 : Administrator
        return:Dictionary :eg- {"addNewUserStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def delete_existing_user_account(isSecured, host, port, username, password, usrName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Remove a user account
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Current username of existing user
        return:Dictionary :eg- {"deleteUserStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def change_existing_user_password(isSecured, host, port, username, password, usrName, oldPwd, newPwd, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Change password for a user account
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Current existing username
        oldPwd:String :- Current password of user
        newPwd:String :- New password for existing user
        return:Dictionary :eg- {"changeUserPasswordStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def change_existing_username(isSecured, host, port, username, password, usrName, newUsrName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Change username for a user account
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Current existing username
        newUsrName:String :- New username for existing user
        return:Dictionary :eg- {"changeUsernameStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def log_in(isSecured, host, port, username, password, usrName, ip, pwd, groupId, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Login a user account
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Current existing username
        ip:String :- User's ip address
        pwd:String :- User's password
        groupId:String :- ID to distinguish different user
        return:Dictionary :eg- {"logInStatus": {"CGI_Result": {"privilege": "2", "result": "0", "logInResult": "0"}}}
        '''
        pass


    @staticmethod
    def log_out(isSecured, host, port, username, password, usrName, ip, groupId, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Logout
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Current existing username
        ip:String :- User's ip address
        groupId:String :- ID to distinguish different user
        return:Dictionary :eg- {"logOutStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_session_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get session list
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"sessionList": {"CGI_Result": {"usr8": null, "usr1": null, "usrCnt": "0", "usr2": null, 
                                                                "result": "0", "usr3": null, "usr6": null, "usr7": null, 
                                                                "usr4": null, "usr5": null}}}
        '''
        pass


    @staticmethod
    def get_user_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get list of users
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"userList": {"CGI_Result": {"usr8": null, "usr1": "admin+2", "usrCnt": "1", "usr2": null, 
                                                             "result": "0", "usr3": null, "usr6": null, "usr7": null, 
                                                             "usr4": null, "usr5": null}}}
        '''
        pass


    @staticmethod
    def get_user_connection_with_camera(isSecured, host, port, username, password, usrName, remoteIp, groupId, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        User checks connection with camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        usrName:String :- Username of user whose connection is to be checked
        remoteIp:String :- IP Address of remote user
        groupId:String :- Group identification value
        return:Dictionary :eg- {"userConnectionStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_up(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move up the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveUp": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_down(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move down the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveDown": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_left(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move lef the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveLeft": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_right(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move right the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveRight": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_top_left(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move top left the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveTopLeft": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_top_right(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move top right the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveTopRight": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_bottom_left(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move bottom left the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveBottomLeft": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_move_bottom_right(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move bottom right the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraMoveBottomRight": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_stop(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Stop camera moving
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraStop": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_reset(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Reset camera position
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraPtzReset": {"CGI_Result": {"result": "0"}}}
        '''
        pass

    @staticmethod
    def get_camera_ptz_speed(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get camera moving speed
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraPtzSpeed": {"CGI_Result": {"result": "0", "speed": "4"}}}
        '''
        pass


    @staticmethod
    def set_camera_ptz_speed(isSecured, host, port, username, password, speedValue, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set camera moving speed
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        speedValue:String :- 0 : Very Slow ....... 4 : Very Fast
        return:Dictionary :eg- {"cameraPtzSpeedStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_camera_ptz_preset_poNumber_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get a list of camera preset position poNumber
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraPtzPresetPoNumber": {"CGI_Result": {"poNumber2": "LeftMost", "poNumber7": null, "result": "0", 
                                                                        "poNumber3": "RightMost", "poNumber6": null, "poNumber4": "preset1", 
                                                                        "poNumber5": "1", "poNumber14": null, "poNumber15": null, "poNumber12": null, 
                                                                        "poNumber13": null, "poNumber10": null, "poNumber11": null, "poNumber0": "TopMost", 
                                                                        "poNumber8": null, "poNumber9": null, "cnt": "6", "poNumber1": "BottomMost"}}}
        '''
        pass


    @staticmethod
    def add_camera_ptz_preset_poNumber(isSecured, host, port, username, password, presetName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Add current position as a preset poNumber
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        presetName:String :- Camera preset name
        return:Dictionary :eg- {"newCameraPtzPresetPoNumber": {"CGI_Result": {"poNumber2": "LeftMost", "poNumber7": null, "result": "0", 
                                                                            "poNumber11": null, "poNumber6": null, "addResult": "2", 
                                                                            "poNumber4": "preset1", "poNumber5": "1", "poNumber14": null, 
                                                                            "poNumber15": null, "poNumber12": null, "poNumber13": null, 
                                                                            "poNumber10": null, "poNumber3": "RightMost", "poNumber0": 
                                                                            "TopMost", "poNumber8": null, "poNumber9": null, "cnt": "6", 
                                                                            "poNumber1": "BottomMost"}}}
        '''
        pass


    @staticmethod
    def delete_camera_ptz_preset_poNumber(isSecured, host, port, username, password, presetName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Remove a preset poNumber
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        presetName:String :- Camera preset name
        return:Dictionary :eg- {"deleteCameraPtzPresetPoNumber": {"CGI_Result": {"poNumber2": "LeftMost", "deleteResult": "3", "poNumber7": null, 
                                                                "result": "0", "poNumber3": "RightMost", "poNumber6": null, "poNumber4": "preset1", 
                                                                "poNumber5": "1", "poNumber14": null, "poNumber15": null, "poNumber12": null, "poNumber13": null, 
                                                                "poNumber10": null, "poNumber11": null, "poNumber0": "TopMost", "poNumber8": null, "poNumber9": null, 
                                                                "cnt": "6", "poNumber1": "BottomMost"}}}
        '''
        pass


    @staticmethod
    def go_to_camera_ptz_preset_poNumber(isSecured, host, port, username, password, presetName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Move the camera to the preset poNumber
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        presetName:String :- Camera preset name
        return:Dictionary :eg- {"goToCameraPtzPresetPoNumber": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_camera_ptz_cruise_map_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get a list of camera cruise map
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"cameraPtzCruiseList": {"CGI_Result": {"cnt": "2", "map7": null, "map6": null, "result": "0", "map4": null, "map5": null, 
                                                                        "map2": null, "map3": null, "map0": "Vertical", "map1": "Horizontal"}}}
        '''
        pass


    @staticmethod
    def get_camera_ptz_cruise_detail(isSecured, host, port, username, password, cruiseName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get detail of a camera cruise map
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        cruiseName:String :- Camera cruise name
        return:Dictionary :eg- {"cameraPtzCruiseDetail": {"CGI_Result": {"poNumber4": null, "poNumber5": null, "poNumber6": null, "poNumber7": null, "poNumber0": "TopMost", 
                                                                          "poNumber1": "BottomMost", "poNumber2": null, "poNumber3": null, "result": "0", "getResult": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_start_cruise(isSecured, host, port, username, password, cruiseName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set the camera to start a cruise
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        cruiseName:String :- Camera cruise name
        return:Dictionary :eg- {"startCruise": {"CGI_Result": {"result": "0", "startResult": "0"}}}
        '''
        pass


    @staticmethod
    def camera_ptz_stop_cruise(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Stop camera cruising
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"stopCruise": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def set_camera_ptz_self_test_mode(isSecured, host, port, username, password, testmode, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set camera self test mode
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        testmode:String :- 0 : No self test, 1 : Normal self test, 2 : After normal self test, go to preset poNumber assigned
        return:Dictionary :eg- {"selfTestMode": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_camera_ptz_self_test_mode(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get camera self test mode
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getSelfTestMode": {"CGI_Result": {"result": "0", "mode": "1"}}}
        '''
        pass


    @staticmethod
    def set_ptz_prepoNumber_for_self_test(isSecured, host, port, username, password, prepoNumberName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set the preset poNumber for self test
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        prepoNumberName:String :- Name of the pre poNumber
        return:Dictionary :eg- {"ptzSelfTestMode": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_ptz_prepoNumber_for_self_test(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the preset poNumber for self test
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getPtzPrepoNumberSelfTest": {"CGI_Result": {"result": "0", "name": "TopMost"}}}
        '''
        pass


    @staticmethod
    def set_485_information(isSecured, host, port, username, password, rs485Protocol, rs485Address, rs485BaudRate, rs485DataBit, rs485StopBit, rs485Check, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set information for 485
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        rs485Protocol:String :- Protocol        
        rs485Address:String :- Address
        rs485BaudRate:String :- Baud rate
        rs485DataBit:String :- Data bit
        rs485StopBit:String :- Stop bit
        rs485Check:String :- Parity
        '''
        pass


    @staticmethod
    def  get_485_information(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get information for 485
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"get485Information": {"CGI_Result": {"rs485DataBit": "7", "rs485Addr": "1", "rs485Baud": "1200", 
                                                                      "rs485Protocol": "0", "result": "0", "rs485Check": "0", "rs485StopBit": "1"}}}
        '''
        pass


    @staticmethod
    def get_ip_information(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get IP Network information
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getIpInformation": {"CGI_Result": {"mask": "255.255.255.0", "gate": "0.0.0.0", "ip": "192.168.0.82", 
                                                                     "dns2": "0.0.0.0", "result": "0", "isDHCP": "1", "dns1": "0.0.0.0"}}}
        '''
        pass


    @staticmethod
    def set_ip_information(isSecured, host, port, username, password, isDHCP, ip, gateway, subnetMask, dns1, dns2, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set IP Network information
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isDHCP:String :- Turn on or off DHCP, 0:Disable | 1:Enable
        ip:String :- IP Address(ipv4)
        gateway:String :- Default gateway
        subnetMask:String :- Subnet mask
        dns1:String :- First dns server address
        dns2:String :- Second dns server address
        return:Dictionary :eg- {"setIpInformation": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def refresh_wifi_list(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Request the camera to refresh its WiFi list
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"refreshWifiList": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_wifi_list(isSecured, host, port, username, password, startNo, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get a list of WiFi access poNumber
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        startNo:String :-Start number of wifi connection user wants to get.
        return:Dictionary :eg- {"getWifiList": {"CGI_Result": {"ap5": null, "ap4": null, "ap7": null, "ap6": null, "ap1": "dlink @_@#+00:01:95:6A:4E:BF+7+0+0", 
                                                                "ap0": "WRT yes 300N+00:18:39:6A:E3:E2+7+1+2", "ap3": "WRT120N+00:25:9C:AF:F6:ED+2+1+4", 
                                                                "ap2": "dlink651+B8:A3:86:53:97:00+2+1+3", "result": "0", "ap9": null, "ap8": null, "curCnt": "4", 
                                                                "totalCnt": "5"}}}
        '''
        pass


    @staticmethod
    def get_wifi_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get WiFi configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getWifiConfig": {"CGI_Result": {"authMode": "2", "key4Len": "64", "key1Len": "64", "key2": null, "key3Len": "64", 
                                                                  "key2Len": "64", "isEnable": "0", "isUseWifi": "0", "psk": null, "key4": null, "isConnected": "0", 
                                                                  "key1": null, "connectedAP": null, "key3": null, "defaultKey": "1", "ssid": null, "result": "0", 
                                                                  "keyFormat": "0", "encryptType": "0"}}}
        '''
        pass


    @staticmethod
    def get_port_information(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get ports information of the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getPortInformation": {"CGI_Result": {"mediaPort": "88", "httpsPort": "443", "result": "0", 
                                                        "webPort": "88", "onvifPort": "888"}}}
        '''
        pass


    @staticmethod
    def get_upnp_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get UPNP Configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getUpnpInformation": {"CGI_Result": {"result": "0", "isEnable": "1"}}}
        '''
        pass


    @staticmethod
    def set_upnp_configuration(isSecured, host, port, username, password, isEnableUpnp, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set UPNP configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isEnableUpnp:String :- Enable or disable upnp, 0:Disable | 1:Enable
        return:Dictionary :eg- {"setUpnpStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_ddns_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get DDNS Configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getDdnsInformation": {"CGI_Result": {"password": null, "ddnsServer": "0", "factoryDDNS": "dh4434.myfoscam.org", 
                                                                        "hostName": null, "user": null, "result": "0", "isEnable": "0"}}}
        '''
        pass


    @staticmethod
    def get_ftp_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get FTP Configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getFtpInformation": {"CGI_Result": {"ftpPort": "21", "password": null, "result": "0", "userName": null, "mode": "0", "ftpAddr": null}}}
        '''
        pass


    @staticmethod
    def test_ftp_server(isSecured, host, port, username, password, ftpAddr, ftpPort, ftpMode, ftpUserName, ftpPassword, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Test a FTP Server
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        ftpMode:String :- 0 : PASV Mode, 1 : PORT Mode
        ftpAddr:String :- Ftp server address        
        ftpPort:String :- Ftp server port number
        ftpUserName:String :- Ftp server username
        ftpPassword:String :- Ftp server password
        '''
        pass


    @staticmethod
    def get_smtp_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get SMTP Configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"getSmtpConfig": {"CGI_Result": {"server": null, "reciever": null, "port": "0", "password": null, 
                                                                  "user": null, "isEnable": "1", "isNeedAuth": "1", "result": "0", "sender": null, "tls": "0"}}}
        '''
        pass


    @staticmethod
    def smtp_test(isSecured, host, port, username, password, smtpServer, portSmtp, isNeedAuthSmtp, tls, userSmtp, passwordSmtp, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Test SMTP
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        tls:String :- 0 : None, 1 : TLS, 2 : STARTTLS
        '''
        pass


    @staticmethod
    def set_system_time(isSecured, host, port, username, password, timeSource, ntpServer, dateFormat, timeFormat, timeZone, isDst, year, month, day, hour, minute, sec, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set time for the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        timeSource:String :- 0 : NTP Server, 1 : Manual
        dateFormat:String :- 0 : YYYY-MM-DD, 1 : DD/MM/YYYY, 2 : MM/DD/YYYY
        timeFormat:String :- 0 : 12 hours, 1 : 24 hours
        isDst:String :- 0 : disable, 1 : enable
        year:String :- Year eg- 2014
        month:String :- Month eg- 05
        day:String :- Day eg- 04
        hour:String :- Hour eg 13 
        minute:String :- Minute eg- 30
        sec:String :- Seconds eg- 00
        return:Dictionary :eg- {"systemTimeStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_system_time(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get system time of the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"systemTime": {"CGI_Result": {"day": "2", "isDst": "0", "ntpServer": "time.nist.gov", "timeZone": "-28800", "year": "2014", 
                                                               "timeSource": "0", "result": "0", "sec": "36", "minute": "50", "timeFormat": "0", "dateFormat": "0", 
                                                               "mon": "6", "hour": "16", "dst": "0"}}}
        '''
        pass


    @staticmethod
    def get_infrared_led_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get infrared led configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"infraredLedConfig": {"CGI_Result": {"result": "0", "mode": "1"}}}
        '''
        pass


    @staticmethod
    def set_infrared_led_configuration(isSecured, host, port, username, password, infraredMode, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set infrared led configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        infraredMode:String :- 0 : Auto, 1 : Manual
        return:Dictionary :eg- {"infraredLedStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_all_device_state(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get all device state
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"allDeviceState": {"CGI_Result": {"sdState": "0", "motionDetectAlarm": "1", "upnpState": "1", "IOAlarm": "1", 
                                                                    "ntpState": "1", "result": "0", "record": "0", "isWifiConnected": "0", "sdFreeSpace": "0k", 
                                                                    "url": "http://dh4434.myfoscam.org:88", "soundAlarm": "0", "ddnsState": "0", "wifiConnectedAP": null, 
                                                                    "sdTotalSpace": "0k", "infraLedState": "0"}}}
        '''
        pass


    @staticmethod
    def get_device_name(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"deviceName": {"CGI_Result": {"result": "0", "devName": "Foscam9821w"}}}
        '''
        pass


    @staticmethod
    def set_device_name(isSecured, host, port, username, password, devName, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"setDeviceName": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_device_information(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get device information
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"deviceInformation": {"CGI_Result": {"productName": "FI9821W V2", "day": "2", "devName": "Foscam9821wTest", "timeZone": "-28800", 
                                                                      "serialNo": null, "min": "55", "hour": "16", "result": "0", "sec": "46", "year": "2014", "mon": "6", 
                                                                      "hardwareVer": "1.4.1.8", "mac": "C4D6552FF77A", "firmwareVer": "1.11.1.18"}}}
        '''
        pass


    @staticmethod
    def restart_camera_system(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Restart the camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"restartCamera": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def restore_device_factory_setting(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Restore camera factory default setting
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        '''
        pass


    @staticmethod
    def export_camera_config(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Exports current camera configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"exportCameraConfig": {"CGI_Result": {"fileName": "configs.bin", "result": "0"}}}
        '''
        pass


    @staticmethod
    def get_firewall_configuration(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get firewall configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"firewallConfiguration": {"CGI_Result": {"ipList5": "0", "rule": "0", "ipList7": "0", "ipList6": "0", 
                                                                          "ipList1": "1660987584", "ipList0": "553691328", "ipList3": "0", 
                                                                          "ipList2": "3825248448", "isEnable": "1", "result": "0", "ipList4": "0"}}}
        '''
        pass


    @staticmethod
    def set_firewall_configuration(isSecured, host, port, username, password, isEnableFirewall, rule, ips=[], language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Set firewall configurations
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        isEnableFirewall:String :- Turn on or off firewall, 0:Disable  |  1:Enable
        rule:String :- 0 : IP List cannot access, 1 : Only allow the IP List to access
        ips:String :- IP Address to block or allow
        return:Dictionary :eg- {"firewallConfigurationStatus": {"CGI_Result": {"result": "0"}}}
        '''
        pass


    @staticmethod
    def get_camera_log(isSecured, host, port, username, password, offset, count, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get the name of camera
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        offset:String :- Starting place to get camera log
        count:String :- Amount of log to take. <20
        return:Dictionary :eg- {"cameraLog": {"CGI_Result": {"log9": null, "log8": null, "log1": "1401728621+admin+4043352256+3", 
                                                              "log0": "1401728632+admin+4043352256+5", "result": "0", "log2": "1399509555+root+16777343+0", 
                                                              "log5": null, "log4": null, "log7": null, "log6": null, "curCnt": "3", "totalCnt": "3", "log3": null}}}
        '''
        pass


    @staticmethod
    def open_infra_led(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Open infrared Led 
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"response":{"openInfraLed": {"CGI_Result": {"result": "0", "ctrlResult": "0"}}}
        '''
        pass


    @staticmethod
    def close_infra_led(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Close infrared Led 
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        return:Dictionary :eg- {"closeInfraLed": {"CGI_Result": {"result": "0", "ctrlResult": "0"}}}
        '''
        pass


    @staticmethod
    def camera_zoom_in(isSecured, host, port, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):

        '''
        Get firewall configuration
        isSecured:Boolean :- Decide whether to use HTTPS or not. Default is False
        host:String :- IP Address or host name of the camera
        port:Number :- Port number of the camera HTTP server from 0 - 65535
        username:String :- Username of camera user
        password:String :- Password of camera user
        '''
        pass

