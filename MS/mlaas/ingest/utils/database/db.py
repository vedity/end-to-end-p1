'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule
 Jay Shukla               15-DEC-2020           1.2           Added functionality for getting single value from the database
 Vipul Prajapati          18-DEC-2020           1.3           Added functionality for create schema.
*/
'''
from MS.mlaas.ingest.utils.custom_exception.exception_handler import GetColumnNamesFailed
import psycopg2
import psycopg2.extras as extras
import pandas as pd 
from sqlalchemy import create_engine
from ..custom_exception.exception_handler import *

class DBClass:

    def read_data(self,file_path):
        """This function is used read data from server file and load into dataframe.

        Args:
            file_path ([string]): [relative path of the file of server.]

        Returns:
            [dataframe]: [it will return read csv file data in the form of dataframe.]
        """
        read_df=pd.read_csv(file_path) #  Read csv file and load data into dataframe.
        return read_df


    def database_connection(self,database,user,password,host,port):
        """This function is used to make connection with database.

        Args:
            database ([string]): [name of the database.],
            user ([string]): [user of the database.],
            password ([string]): [password of the database.],
            host ([string]): [host ip or name where database is running.],
            port ([string]): [port number in which database is running.]

        Returns:
            [object,string]: [it will return connection object well as connection string.]
        """
        try:
            connection_string = "postgresql://" + user + ":" + password + "@" + host + ":" + port + "/" + database # Make database connection string.
            connection = psycopg2.connect(database = database, user = user , password = password, host = host, port = port) #Get connection object by initializing connection to database. 
        except:
            return None,None
            
        return connection,connection_string
    #v1.3
    def create_schema(self,connection,user_name = None):
        """This function is used to create schema.

        Args:
            connection ([object]): [connection for database],
            user_name ([string]): [user name]

        Returns:
            [integer]: [status of create schema. if successfully then 0 else 1.]
        """
        if user_name == None :
            schema_name = "mlaas"
        else:
            schema_name = user_name.lower() # Get schema name.
            
        cursor = connection.cursor() # Open cursor for database.
        try:
            cursor.execute('CREATE Schema '+ schema_name +';') # Excute create schema query.
            connection.commit() # Commit the changes.
            return 0 # If successfully created.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor
            return 1 # If failed.
        
    def create_table(self,connection,table_name,schema):
        """This function is used to  create table into database.

        Args:
            connection ([object]): [object of the connection to the database.],
            table_name ([string]): [name of the table.],
            schema ([string]): [structure of the table.]

        Returns:
            [integer]: [it will return status of the table creation. if successfully the 0 else 1.]
        """
        cursor = connection.cursor() # Open cursor for database.
        try:
            cursor.execute('CREATE TABLE '+table_name+' ('+schema+');') # Excute create table query.
            connection.commit() # Commit the changes.
            return 0 # If successfully created.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor
            return 1 # If failed.
        
    
    
    def insert_records(self,connection,table_name,row_tuples,cols):
        """This function is used to insert data into database table.

        Args:
            connection ([object]): [object of the database connection.],
            table_name ([string]): [name of the table.],
            row_tuples ([list]): [list of the tuple of record.],
            cols ([string]): [column names in the form of strings.]

        Returns:
            [integer]: [it will return status of the data insertion. if successfully then 0 else 1.]
        """
        
        cols = cols # Get columns name for database insert query.
        tuples = row_tuples # Get record for database insert query.
        query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, cols) # Make query
        cursor = connection.cursor() # Open cursor for database.
        try:
            extras.execute_values(cursor, query, tuples) # Excute insert query.
            connection.commit() # Commit the changes.
            return 0 # If successfully inserted.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor.
            return 1 # If failed.

    
    def select_records(self,connection,sql_command):
        """This function is used to retrieve data from database table into dataframe.

        Args:
            connection ([object]): [object of the database connection.],
            sql_command ([string]): [select sql command.]

        Returns:
            [dataframe]: [it will return dataframe of the selected data from the database table.]
        """
        cursor = connection.cursor() # Open the cursor.
        sql_command = sql_command # Get sql command.
        try :
            data = pd.read_sql(sql_command, connection) # Read data from database table.
            return data   
        except :
            return None
        
       

    

    def delete_records(self,connection,sql_command):
        """This function is used to delete data from database table.

        Args:
            connection ([object]): [connection object of the database class.],
            sql_command ([string]): [delete sql command]

        Returns:
            [integer]: [it will return stauts of deleted record. if successfully then 0 else 1.]
        """
        cursor = connection.cursor() # Open the cursor.
        sql_command = sql_command # Get delete query
        try:
            cursor.execute(sql_command) # Execute the delete query.
            connection.commit() # Commit the changes.
            status = 0 # If Successfully.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor.
            status = 1 # If failed

        return status

    def update_records(self,connection,sql_command):
        """This function is used to update records into database.

        Args:
            connection ([object]): [connection for database],
            sql_command ([string]): [query string for update command]

        Returns:
            [integer]: [status of updated records. if successfully then 1 else 0.]
        """
        cursor = connection.cursor() # Open the cursor.
        sql_command = sql_command # Get update query
        try:
            cursor.execute(sql_command) # Execute the update query.
            connection.commit() # Commit the changes.
            status = 0 # If Successfully.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor.
            status = 1 # If failed

        return status


    def load_csv_into_db(self,connection_string,table_name,file_data_df,user_name):
        """This function is used to load csv data  into database table.

        Args:
            connection_string ([object]): [connection string of the database connection.],
            table_name ([string]): [name of the table.],
            file_data_df ([dataframe]): [dataframe of the file data.],
            user_name ([string]): [name of the user.]

        Returns:
            [integer]: [it will return status of loaded data into database table. if successfully then 0 else 1.]
        """
        engine = create_engine(connection_string) # Create database engine.
        schema_name = user_name.lower()
        try :
            file_data_df.to_sql(table_name,engine,schema=schema_name) # Load data into database with table structure.
            status = 0 # If successfully.
        except :
            status = 1 # If failed.
            
        return status

    def get_column_names(self, connection, table_name):
        '''
        Returns name of the columns from the given csv table.
        
        Args:
            connection_string ([object]): [connection string of the database connection.],
            table_name ([string]): [name of the table.]
        
        Returns:
            columns ([List of Strings]): [List of Column names]
        '''
        
        col_cursor = connection.cursor()

        # concatenate string for query to get column names
        # SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'some_table';
        sql_command = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
        sql_command += "table_name = '{}';".format( table_name )
        
        try:
            # execute the SQL string to get list with col names in a tuple
            col_cursor.execute(sql_command)

            # get the tuple element from the list
            col_names = ( col_cursor.fetchall() )

            columns = []

            # iterate list of tuples and grab first element
            for tup in col_names:

                # append the col name string to the list
                columns += [ tup[0] ]
            
            # close the cursor object to prevent memory leaks
            col_cursor.close()
        except:
            raise GetColumnNamesFailed
        
        return columns







     