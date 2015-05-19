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

from automationApp.core.database import Database


class APIController:
    
    
    def __init__(self):
        self.__db = Database.instance()
        
    def has_kbx_method(self, kbxMethodId):
        '''
        Check if a given kbxMethodId is in use by scenes or rules.
        Database table involved: kbx_method
        '''
        result = self.__db.execute_and_fetch_one('SELECT "kbxMethodId" FROM "kbx_method" WHERE "kbxMethodId"=? LIMIT 1', (kbxMethodId,))
        return result is not None
    
    def has_kbx_group(self, kbxGroupId):
        '''
        Check if a given kbxGroupId is in use by scenes or rules.
        Database table involved: kbx_group
        '''
        result = self.__db.execute_and_fetch_one('SELECT "kbxGroupId" FROM "kbx_group" WHERE "kbxGroupId"=? LIMIT 1', (kbxGroupId,))
        return result is not None
        
        