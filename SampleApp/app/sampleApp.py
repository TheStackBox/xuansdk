##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Sample Application.
#
# Xuan Sample Application is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Sample Application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Sample Application.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from com.cloudMedia.theKuroBox.sdk.app.application import Application
from app.module.sampleAppModule import SampleAppModule

class SampleApp(Application):
    '''
    Sample Application for IoT
    '''
    
    def __init__(self):
        '''
        Constructor
        '''

    def on_start(self):
        '''
        Application implement their body when application on start
        '''
        self.register_module(SampleAppModule("sample_app_module", None))

    def on_stop(self):
        '''
        Application implement their body when application on stop
        '''
        pass

    def on_destroy(self):
        '''
        Application implement their body when application on destroy
        '''
        pass
    
    def on_system_connected(self):
        '''
        Application implement their body when the application is connected to the system
        Developer should put their code for dealing with system here, such as:
        - Register Event
        - Register Event Listener
        - Register Shared Method

        For System Connected timing in Module, please refer to Module.on_system_connected
        '''
        pass

    def post_system_connected(self):
        '''
        Application implement their body when the on_system_connected timing is finished
        This timing is located after on_system_connected timing in application and all modules
        '''
        pass