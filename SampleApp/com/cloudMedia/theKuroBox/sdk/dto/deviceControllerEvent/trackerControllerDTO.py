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

class TrackerControllerDTO(dict):
    

    def __init__(self, trackerControllerDTO=None):
        pass

    def set_paired_device_id(self, pairedDeviceId):
        pass

    def get_paired_device_id(self):
        pass

    def set_link_loss(self, linkLoss):
        ''' 
        0 - No Alert
        1 - Mild Alert
        2 - High Alert
        '''
        pass

    def get_link_loss(self):
        pass

    def set_battery(self, battery):
        '''
        % of the battery energy left.
        '''
        pass

    def get_battery(self):
        pass

    def set_rssi(self, rssi):
        '''
        RSSI, a negative value
        '''
        pass

    def get_rssi(self):
        pass

    def set_distance(self, distance):
        '''
        Approximate distance in meter.
        '''
        pass

    def get_distance(self):
        pass

