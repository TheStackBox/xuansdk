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

import re

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod
from com.cloudMedia.theKuroBox.sdk.ex.systemException import SystemException


class FoscamFI8910wService(object):
    '''
    Foscam FI8910W
    '''
    
    @staticmethod
    def __validate_default_params(hostAddress, hostPort):
        '''
        Validate the default parameters and return in tupple
        '''
        pass


    @staticmethod
    def __check_is_enabled_key_valid(value):
        '''
        Check whether the value is 1 or 0 
        '''
        pass

 
    @staticmethod
    def __validate_result(result):
        '''
        Validate the result returned
        '''
        pass


    @staticmethod
    def check_user(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Check user list
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"userLoginDetail": {"pwd": "admin", "pri": "3", "user": "admin"}}
        '''
        pass


    @staticmethod
    def get_snapshot(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get snapshot link
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"snapshot": "http://192.168.0.10/snapshot.cgi?user=admin&pwd=admin"}
        '''
        pass


    @staticmethod
    def get_jpeg_video_stream(hostAddress, hostPort, username, password, videoStreamResolution, videoStreamRate, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get MJPEG Stream URL
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        videoStreamResolution:String :- 8 : 320x240, 32 : 640x480
        videoStreamRate:String :- 0 :full speed, 1 : 20 fps, 3 : 15 fps, 6 : 10 fps, 11 :5 fps, 12 : 4 fps, 13 : 3 fps, 14 : 2 fps, 15 : 1 fps, 17 : 1 fp/2s, 19 : 1 fp/3s, 21 : 1 fp/4s, 23 : 1 fp/5s
        return:Dictionary :eg- {"jpegVideoStream": "http://192.168.0.10/videostream.cgi?user=admin&pwd=admin&rate=0&resolution=32"}
        '''
        pass


    @staticmethod
    def get_asf_video_stream(hostAddress, hostPort, username, password, videoStreamResolution, videoStreamRate, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get ASF video stream URL
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        videoStreamResolution:String :- 8 : 320x240, 32 : 640x480
        videoStreamRate:String :- 0 :full speed, 1 : 20 fps, 3 : 15 fps, 6 : 10 fps, 11 :5 fps, 12 : 4 fps, 13 : 3 fps, 14 : 2 fps, 15 : 1 fps, 17 : 1 fp/2s, 19 : 1 fp/3s, 21 : 1 fp/4s, 23 : 1 fp/5s
        return:Dictionary :eg- {"jpegVideoStream": "http://192.168.0.10/videostream.asf?user=admin&pwd=admin&rate=0&resolution=32"}
        '''
        pass


    @staticmethod
    def get_device_status(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get the status of device
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"deviceStatus": {"upnp_status": "1", "now": "1401765438", "id": "00626E4641CB", "tridro_error": "", 
                                                  "alias": "Foscam8910", "p2p_local_port": "22097", "wifi_status": "0", "alarm_status": "0", 
                                                  "msn_status": "0", "app_ver": "2.0.10.3", "oray_type": "0", "ddns_host": "", "sys_ver": "11.37.2.49", 
                                                  "humidity": "0", "ddns_status": "0", "p2p_status": "0", "tz": "-28800", "temperature": "0.0"}} 
        '''
        pass


    @staticmethod
    def get_camera_parameters(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get camera's parameters
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraParameters": {"resolution": "32", "flip": "1", "contrast": "3", "mode": "1", "fps": "0", "brightness": "30"}} 
        '''
        pass


    @staticmethod
    def camera_ptz_turn_up(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move camera up
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraTurnUp": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_turn_down(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move camera down
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraTurnDown": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_turn_left(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move camera left
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraTurnLeft": "ok."}
        '''

        pass


    @staticmethod
    def camera_ptz_turn_right(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move camera right
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraTurnRight": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_go_center(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move camera to go center
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraCenter": "ok."}
        '''

        pass


    @staticmethod
    def camera_ptz_patrol_up_down(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the camera to patrol vertically
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"patrolUpDown": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_patrol_left_right(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the camera to patrol horizontally
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg-  {"patrolLeftRight": "ok."}
        '''

        pass


    @staticmethod
    def camera_ptz_stop_patrol_left_right(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop camera from patroling horizontally
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"stopPatrolLeftRight": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_stop_patrol_up_down(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Stop camera from patroling vertically
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"stopPatrolUpDown": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_move_upper_left(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera top left
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"moveUpperLeft": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_move_upper_right(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera top right
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"moveUpperRight": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_move_down_left(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera bottom left
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"moveDownLeft": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_move_down_right(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Move the camera bottom right
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"moveDownRight": "ok."}
        '''

        pass



    @staticmethod
    def camera_ptz_motor_test(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the camera to test its motor
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"motorTest": "ok."}
        '''

        pass




    @staticmethod
    def set_camera_resolution(hostAddress, hostPort, username, password, resolutionValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera resoltion value
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        resolutionValue:String :- 2 : qqvga, 8 : qvga, 32 : vga
        return:Dictionary :eg- {"resolutionStatus": "ok."} 
        '''

        pass


    @staticmethod
    def set_camera_brightness(hostAddress, hostPort, username, password, brightnessValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera brightness value 
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        brightnessValue:String :- 0 - 255
        return:Dictionary :eg- {"brightnessStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_camera_contrast(hostAddress, hostPort, username, password, contrastValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera contrast value
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        contrastValue:String :- 0 -6 
        return:Dictionary :eg- {"contrastStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_camera_mode(hostAddress, hostPort, username, password, modeValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera mode
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        modeValue:String :- 0 : 50hz, 1 : 60hz, 2 : outdoor
        return:Dictionary :eg- {"modetStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_camera_patrol(hostAddress, hostPort, username, password, patrolValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set patrol behaviour 
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        patrolValue:String :- 0 : initial, 1 : vertical patrol, 2 : horizontal patrol, 3 : vertical patrol + horizontal patrol
        return:Dictionary :eg- {"patrolStatus": "ok."}
        '''

        pass


    @staticmethod
    def reboot_camera(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reboot the camera
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"rebootStatus": "ok."}
        '''

        pass


    @staticmethod
    def factory_restore_camera(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Reset camera setting to factory default
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"factoryRestoreStatus": "ok."}
        '''

        pass


    @staticmethod
    def get_device_setting_parameters(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Get a list of camera setting parameters
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"deviceSettingParameter": {"dev3_host": "", "user1_name": "admin", "mail_user": ""}}
        '''

        pass


    @staticmethod
    def set_camera_alias_name(hostAddress, hostPort, username, password, aliasName, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set the name of camera
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        aliasName:String :- New name for the camera
        return:Dictionary :eg- {"aliasNameStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_camera_date_time(hostAddress, hostPort, username, password, now, timezoneValue, ntp_enable, daylight_saving_time, ntp_svr, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set camera date time setting
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        now:String :- The lost seconds during the period from 1970-1-1 0:0:0 to the specified time , e.g. attach the parameter,then the device proofread the time according to this time.
        timezoneValue:String :- the seconds deviate from the standard GMT eg. for gmt-8 : -28800
        ntp_enable:String :- 0 : disable ntp proofread time, 1 : enable
        daylight_saving_time:String :- Set the different seconds between daylight saving time and the standard time
        ntp_svr:String :- Ntp server length <= 64
        return:Dictionary :eg- {"dateTimeStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_upnp_setting(hostAddress, hostPort, username, password, isEnableUpnp, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set whether to enable UPNP or not
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        isEnableUpnp:String :- 0 : disable, 1 : enable
        return:Dictionary :eg- {"upnpSettingStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_alarm(hostAddress, hostPort, username, password, motionArmed, motionSensitivity, motionCompensation, inputArmed, soundDetectArmed, soundDetectSensitivity, sendmail, uploadInterval, isEnableSchedule, scheduleSun0, scheduleSun1, scheduleSun2, scheduleMon0, scheduleMon1, scheduleMon2, scheduleTue0, scheduleTue1, scheduleTue2, scheduleWed0, scheduleWed1, scheduleWed2, scheduleThu0, scheduleThu1, scheduleThu2, scheduleFri0, scheduleFri1, scheduleFri2, scheduleSat0, scheduleSat1, scheduleSat2, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Set alarm setting
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        motion_armed 0:String  :- motion detection unarmed; 1 :armed
        motion_sensitivity:String :- 0-9 : high-low
        motion_compensation:String  :- Enable alarm motion compensation or not when the light changes suddently:0=No, 1=yes
        input_armed:String :- 0:input_unarmed  1:input_armed
        sounddetect_armed:String :- 0:sounddetect_unarmed, 1:armed
        sounddetect_sensitivity:String :- 0-9 : high-low
        mail:String :- 0:disable sending mail on alarm  1:enable
        upload_interval:String :- alarm_upload_interval(seconds)0-65535
        schedule_enable:String :- schedule_enable or not 1:enable or 0:disable
        schedule_sun_0:String :- Sunday arm plan.24hours/day. Divided 24hours to 96 time district,each district for 15 munites. bit0-95
        return:Dictionary :eg- {"alarmStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_forbidden(hostAddress, hostPort, username, password, isEnableSchedule, scheduleSun0, scheduleSun1, scheduleSun2, scheduleMon0, scheduleMon1, scheduleMon2, scheduleTue0, scheduleTue1, scheduleTue2, scheduleWed0, scheduleWed1, scheduleWed2, scheduleThu0, scheduleThu1, scheduleThu2, scheduleFri0, scheduleFri1, scheduleFri2, scheduleSat0, scheduleSat1, scheduleSat2, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        schedule_enable:String :- schedule_enable or not 1:enable or 0:disable
        schedule_sun_0:String :- Sunday arm plan.24hours/day. Divided 24hours to 96 time district,each district for 15 munites. bit0-95
        return:Dictionary :eg- {"forbiddenStatus": "ok."}
        '''
        
        pass


    @staticmethod
    def get_forbidden(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"forbiddenSchedule": {"schedule_thu_0": "1", "schedule_thu_1": "1", "schedule_thu_2": "1", "schedule_sat_1": "1", 
                                                       "schedule_sat_0": "1", "schedule_sat_2": "1", "schedule_mon_2": "1", "schedule_mon_1": "1", 
                                                       "schedule_mon_0": "1", "schedule_fri_0": "1", "schedule_fri_1": "1", "schedule_fri_2": "1", 
                                                       "schedule_enable": "1", "schedule_tue_2": "1", "schedule_tue_1": "1", "schedule_tue_0": "1", 
                                                       "schedule_wed_1": "1", "schedule_wed_0": "1", "schedule_wed_2": "1", "schedule_sun_2": "1", 
                                                       "schedule_sun_1": "1", "schedule_sun_0": "1"}}
        '''

        pass


    @staticmethod
    def set_LED_mode(hostAddress, hostPort, username, password, ledValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account.
        ledValue:String :- 0:mode1, 1:mode2, 2:shut off the led
        return:Dictionary :eg- {"ledModeStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_center_on_start(hostAddress, hostPort, username, password, onStartValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        onStartValue:String :- 0:Disable or :Enable
        return:Dictionary :eg- {"centerOnStart": "ok."}
        '''

        pass


    @staticmethod
    def set_patrol_horizontal_round(hostAddress, hostPort, username, password, hRoundValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        hRoundValue:String :- 0 to infinity
        return:Dictionary :eg- {"patrolHorizontalRoundStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_patrol_vertical_round(hostAddress, hostPort, username, password, vRoundValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        vRoundValue:String :- 0 to infinity
        return:Dictionary :eg- {"patrolVerticalRoundStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_patrol_speed(hostAddress, hostPort, username, password, patrolRate, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        patrolRate:String :- 0-100 >fast
        return:Dictionary :eg- {"patrolSpeedStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_disable_preset(hostAddress, hostPort, username, password, isEnablePreset, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        isEnablePreset:String :- 0 : disable, 1 :enable
        return:Dictionary :eg- {"disablePresetStatus": "ok."}
        '''

        pass


    @staticmethod
    def set_preset_on_start(hostAddress, hostPort, username, password, isEnablePresetOnStart, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        isEnablePresetOnStart:String :- 0: disable, 1 : enable
        return:Dictionary :eg- {"presetOnStartStatus": "ok."}
        '''

        pass


    @staticmethod
    def get_camera_parameter(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"cameraParameter": {"ptz_patrol_up_rate": "6", "ptz_auto_patrol_interval": "0", "ptz_patrol_right_rate": "6", 
                                                     "ptz_patrol_h_rounds": "10", "ptz_preset_onstart": "1", "led_mode": "1", "ptz_disable_preset": "1", 
                                                     "ptz_patrol_v_rounds": "10", "ptz_patrol_down_rate": "6", "ptz_auto_patrol_type": "0", "ptz_patrol_rate": "15", 
                                                     "ptz_center_onstart": "1", "ptz_patrol_left_rate": "6"}}
        '''

        pass


    @staticmethod
    def set_camera_decoder(hostAddress, hostPort, username, password, baudValue, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        baudValue:String :- 9:B1200, 11:B2400, 12:B4800, 13:B9600, 14:B19200, 15:B38400, 4097:B57600, 4098:B115200
        return:Dictionary :eg- {"decoderStatus": "ok."}
        '''

        pass


    @staticmethod
    def wifi_scan(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"wifiScanStatus": "ok."}
        '''

        pass


    @staticmethod
    def get_wifi_scan_result(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"wifiScanResult": {"ap_ssid": "new Array()", "ap_bssid": "new Array()", "ap_mode": "new Array()", 
                                                    "ap_number": "10", "ap_security": "new Array()"}}
        '''

        pass


    @staticmethod
    def get_camera_log(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"logResult": {"log_text": "aaa"}}
        '''

        pass


    @staticmethod
    def set_camera_mac_address(hostAddress, hostPort, username, password, macAddress, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        macAddress:String :- MAC Address without any separator. e.g.: 0006DC970533
        return:Dictionary :eg- {"macAddressStatus": "ok."}
        '''

        pass
    

    @staticmethod
    def reset_factory_ddns_setting(hostAddress, hostPort, username, password, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        hostAddress:String :- IP Address or host name for the camera
        hostPort:String :- Port 0 - 65535
        username:String :- Username of the user account
        password:String :- Password of the user account
        return:Dictionary :eg- {"factoryDdnsSetting": "ok."}
        '''

        pass


        