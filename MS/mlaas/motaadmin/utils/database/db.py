'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Intial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/

*/
'''
import psycopg2
import psycopg2.extras as extras
import pandas as pd 
from sqlalchemy import create_engine

class DBClass:

    def read_data(self,file_name):
        """
        This function is used read data from uploaded file and load into dataframe.
        It will take input parameter as file name.
        And it will return schema.

        Input : csv file name
        Output : dataframe
        """
        read_df=pd.read_csv(file_name) #  Read csv file and load data into dataframe.
        return read_df


    def database_connection(self,database,user,password,host,port):
        """
        This function is used to make connection with database..
        It will take input parameter as database,user,password,host,port
        And it will return connection object.

        Input : database,user,password,host,port
        Output : connection object
        """
        conection_string = "postgresql://" + user + ":" + password + "@" + host + ":" + port + "/" + database # Make database connection string.
        connection = psycopg2.connect(database = database, user = user , password = password, host = host, port = port) #Get connection object by initializing connection to database.
        return connection,conection_string

    def create_table(self,connection,table_name,schema):
        """
        This function is used to  create table into database.
        It will take input parameter as connection object,table name,table schema
        And it will return status of table creation.

        Input : connection,table_name,schema
        Output : status
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
        
    
    
    def insert_reocrds(self,connection,table_name,row_tuples,cols):
        """
        This function is used to insert data into database table.
        It will take input parameter as connection object,table name,records. 
        And it will return status of insertion.

        Input : connection,table_name,row_tuples
        Output : status
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
        """
        This function is used to retrieve data from database table into dataframe.
        It will take input parameter as connection object,sql_command.
        And it will return dataframe of retrieval data.

        Input : connection,sql_command
        Output : dataframe
        """
        cursor = connection.cursor() # Open the cursor.
        sql_command = sql_command # Get sql command.
        data = pd.read_sql(sql_command, connection) # Read data from database table.
        return data

    def delete_records(self,connection,sql_command):
        """
        This function is used to delete data from database table.
        It will take input parameter as connection object,sql_command.
        And it will return status of deletion of  data.

        Input : connection,sql_command.
        Output : status.
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


    def load_csv_into_db(self,conection_string,table_name,file_data_df):
        """
        This function is used to load csv data  into database table.
        It will take input parameter as connection string,table_name and file data.
        And it will return status of loaded data.

        Input : conection_string,table_name,file_data_df
        Output : status
        """
        engine = create_engine(conection_string) # Create database engine.
        try :
            file_data_df.to_sql(table_name, engine) # Load data into database with table structure.
            status = 0 # If successfully.
        except :
            status = 1 # If failed.
            
        return status



DBObject=DBClass()

    









     