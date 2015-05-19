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
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class NotificationManagerService():

    @staticmethod
    def dispatch_notification(text=None, title=None, tag=None, data=None, link=None, linkLabel=None, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Function : Fetch a list of notification stored
        @param text:String        - The text to be shown. (Optional)
        @param title:String       - The title of the notification (Optional)
        @param tag:String         - The tag of the notification (Optional)
        @param data:Object        - Extra information to be sent (Optional)
        @param link:String        - The link to redirect when click on the notification
        @param linkLabel:String   - The display label for link button (? or click-able label)
        
        @return: A object with the following structure:
        1. success:boolean        - Whether the notification is successfully stored.
        '''
        pass

