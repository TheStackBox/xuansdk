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

class SqliteDataAccess():
    
    SQL3COL_NULL = "NULL"
    SQL3COL_INTEGER = "INTEGER"
    SQL3COL_REAL = "REAL"
    SQL3COL_TEXT = "TEXT"
    SQL3COL_BLOB = "BLOB"
    
    def __init__(self):
        pass

    def create_table(self, table, columns):
        '''
        Function : Create a table.
        @param table:String                  - The name of the table
        @param colums:List<String>           - The list of columns properties.
        
        @note: The SQL query formed will be: CREATE TABLE $table ($columns[0], $columns[1], $columns[2], ... $columns[n])
        
        @return A dictionary with the following structure
        { "returnValue":100, "returnMessage":success }
        
        '''
        pass

    def drop_table(self, table):
        
        '''
        Function : Remove a table
        @param table:String                   - The name of the table
        
        @return A dictionary with the following structure
        { "returnValue":100, "returnMessage":success }
        '''
        pass

    def select(self, table, fields=["*"], keyValues={}, order=[], asc=True, limit=50, offset=0, groupBy=[]):
        '''
        Function : Select a list of data
        @param table:String                  - The name of the table
        @param fields:List<String>           - A list of columns to be selected
        @param keyValues:Dictionary          - A dictionary containing the select conditions
        @param order:List<String>            - A list of columns to be ordered
        @param asc:Boolean                   - Whether to sort it in ascending. False to sort in descending
        @param limit:Number                  - The total number of data to be returned
        @param offset:Number                 - The starting index to return the data
        @param groupBy:List<String>          - A list of Group By clause
        
        @return A list of data
        '''
        pass

    def insert(self, table, keyValues):
        '''
        Function : Insert a data into the table
        @param table:String                    - The name of the table
        @param keyValues:Dictionary            - A dictionary for column data to be inserted
        
        @return: A dictionary of the following structure
        1. data:Dictionary                     - A dictionary with the following attributes
                                                       a. lastRowId         - The Last Row ID after insert
        '''
        pass

    def update(self, table, setValues, condValues={}):
        '''
        Function : Update the data in a table
        @param table:String                    - The name of the table
        @param setValues:Dictionary            - A dictionary containing the value to be set
        @param condValues:Dictionary           - A dictionary containing the condition for the update
        
        @return: A dictionary with the following structure
        { "returnValue":100, "returnMessage":success }
        '''
        pass

    def delete(self, table, keyValues={}):
        '''
        Function : Remove data from tables
        @param table:String                        - The name of the table
        @param keyValues:Dictionary                - A dictionary containing the condition for removal
        
        @return: A tuple containing the following
        [0] The row count deleted
        [1] The cursor object  
        '''
        pass

    def close_conn(self):
        '''
        Function : Close the connection
        '''
        pass

    def execute(self, sql, keyValues={}):
        '''
        Function : Execute a SQL query
        @param sql:String                          - The SQL query
        @param keyValues:Dictionary / Tuple        - The parameters to be replaced into the query
        
        @note: For further detail, please refer to https://docs.python.org/3.3/library/sqlite3.html#sqlite3.Cursor.execute
        
        @return: The cursor object after execution
        '''
        pass

    def executescript(self, sqlscript):
        '''
        Function : Execute a SQL script
        @param sqlscript:String                    - The SQL script
        
        @return: The result of the execution
        '''
        pass

