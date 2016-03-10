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

from com.cloudMedia.theKuroBox.sdk.app.kbxLang import KBXLang


class AutomationException(Exception):
    '''
    All exceptions raised by automation are recorded here.
    
    11000 - 11099: Module Errors
    11500 - 11599: Trigger Related Errors
    11600 - 11699: API Service Errors
    11700 - 11799: Rule Service Errors
    11800 - 11899: Timer Module Errors
    11900 - 11999: Scene Service Errors
    12000 - 12999: Scene Execution Result Service Errors
    '''
    
    
    __all_exceptions = {
        11097: "11097_invalid_parameter",
        11099: "11099_unexpected_exception",
        
        11501: "11501_invalid_timer_type",
        11502: "11502_invalid_timer_value",
        
        11601: "11601_unexpected_system_behavior",
        11602: "11602_kbx_method_not_in_use",
        11603: "11603_kbx_group_not_in_use",

        11702: "11702_rule_not_found",
        11703: "11703_rule_update_in_progress",
        11704: "11704_rule_creation_or_update_failed",
        11705: "11705_rule_set_items_too_many",
        11706: "11706_rule_set_rules_too_many",
        
        11800: "11800_timer_condition_not_fulfilled",
                
        11901: "11901_scene_execution_in_progress",
        11902: "11902_scene_not_found",
        11903: "11903_scene_update_in_progress",
        11904: "11904_scene_creation_or_update_failed",
        11905: "11905_no_execution_in_progress",
        11906: "11906_scene_deletion_failed",
        11907: "11907_scene_set_items_too_many",
        11908: "11908_scene_set_scenes_too_many",
        
        12000: "12000_ser_not_found",
        12001: "12001_seri_not_found",
        12002: "12002_ser_no_retry_item",
        12003: "12003_seri_not_error",
        12004: "12004_ser_retry_in_progress",
        
        13000: "13000_favorited_scene_not_found",
        13001: "13001_favorited_scene_creation_or_update_failed",
        13002: "13002_favorited_scene_deletion_failed"
    }
    

    def __init__(self, exCode, exDebug=None, exFunc=None):
        try:
            exCode = int(exCode)
            exMessage = AutomationException.__all_exceptions[exCode]
            super().__init__(exMessage)
        except Exception:
            super().__init__("invalid exception code")
            exCode = 99999
            self.__exDebug = "exCode: " + str(exCode) + ", exDebug:" + str(exDebug)
        
        self.__exCode = exCode
        self.__exDebug = str(exDebug)
        self.__exFunc = exFunc

    def err_to_dict(self):
        return {"returnValue":self.__exCode,
                "returnMessage":self.get_error_message(),
                "debugMessage":self.__exDebug}

    def get_error_code(self):
        return self.__exCode

    def get_error_message(self):
        return "invalid exception code" \
                if self.__exCode == 99999 \
                else KBXLang(AutomationException.__all_exceptions[self.__exCode], self.__exFunc)

    def get_debug_message(self):
        return self.__exDebug

