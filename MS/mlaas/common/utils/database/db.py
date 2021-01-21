'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule
 Jay Shukla               15-DEC-2020           1.2           Added functionality for getting single value from the database
 Vipul Prajapati          18-DEC-2020           1.3           Added functionality for create schema.
*/
'''
import psycopg2
import psycopg2.extras as extras
import pandas as pd 
from sqlalchemy import create_engine
import json
import logging
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('dataset_creation')

class DBClass:

    def read_data(self,file_path):
        """This function is used read data from server file and load into dataframe.

        Args:
            file_path ([string]): [relative path of the file of server.]

        Returns:
            [dataframe]: [it will return read csv file data in the form of dataframe.]
        """
        read_df=pd.read_csv(file_path, na_filter= False) #  Read csv file and load data into dataframe.
        # column_list = read_df.select_dtypes(include=['object'])
        # logging.info("Test tyoe: "+str(df_num))
        
        # column_list=[*range(0, len(read_df.columns), 1)] 
        # read_df=pd.read_csv(file_path,na_filter= False,parse_dates=column_list) #  Read csv file and load data into dataframe.
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
        except(Exception, psycopg2.DatabaseError) as error:
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
            file_data_df.to_sql(table_name,engine,schema=schema_name,) # Load data into database with table structure.
            status = 0 # If successfully.
        except Exception as e:
            logging.info("Exception: "+str(e))
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
        sql_command += "table_name = '{}' order by ordinal_position;".format( table_name )
        
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
    
    
    def get_order_clause(self,connection,table_name,sort_type,sort_index):    
        """ function used to get ORDER by clause string

        Args:
            table_name[(String)] : [Name of the table]
            sort_type[(String)] : [value of the sort type]
            sort_index[(integer)] : [index of column]
        Return : 
            [String,List] : [return the Order clause,list of column name]
        """ 
        
        col_table_name=table_name.partition(".")[2] #trim from the string and get the table name
        columns_list=self.get_column_names(connection,col_table_name) #get the column list    
        if sort_type =="asc" and  str(sort_index) == "0":  #check if value sort_type and sort_index is empty
            order_clause=f'ORDER BY "{columns_list[0]}"'
        else:
            order_clause=f'ORDER BY "{columns_list[int(sort_index)]}" {sort_type}' #formated string for order By clause 
        return order_clause,columns_list
    
    def get_global_search_clause(self,columns,global_value):
        """ function used to create search  string for sql command

        Args:
            table_name[(String)] : [Name of the table]
            sort_type[(String)] : [value of the sort type]
            sort_index[(integer)] : [index of column]
        Return : 
            [String] : [return the search pattern string]
        """ 
        
        empty_string=""
        for i in range(len(columns)):
            empty_string+="cast(\""+str(columns[i])+"\" as varchar) like '%"+str(global_value)+"%' or "   # create the string with Like operator  
        global_search_clause="("+empty_string[:len(empty_string)-3]+")" # remove the "or" string appended at last 
        return global_search_clause
    
    def get_customfilter(self,customefilter):
        dict=customefilter[0]
        empty_string=""
        for x in dict:
            if dict[x]!="":
                dict[x]=dict[x].replace("'","''")
                empty_string+="cast(\""+x+"\" as varchar) like '%"+dict[x]+"%' or "
        customefilter="("+empty_string[:len(empty_string)-3]+")" # remove the "or" string appended at last 
        return customefilter
    
    
    def pagination(self,connection,table_name,start_index,length,sort_type,sort_index,global_search_value,customefilter):
        """ function used to create Sql query string

        Args:
                start_index[(Integer)] : [value of the starting index]
                length[(Integer)] :[value of length of records to be shown]
                sort_type[(String)] : [value of sort_type ascending or descending]
                sort_index[(Integer)] : [index value of the column to perform sorting]
                global_value[(String)] : [value that need be search in table]
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
            [String] : [return the sql query string]
        """
        try: 
            end_index = (start_index + length)-1 #get total length
            limit_index=start_index+length
            order_clause,columns_list=self.get_order_clause(connection,table_name,sort_type,sort_index) #call get_order_clause function and get order by string and column list            
            order_clause,columns_list=self.get_order_clause(connection,table_name,sort_type,sort_index) #call get_order_clause function and get order by string and column list            
            columns=columns_list[1:]
            global_search_clause=""
            if global_search_value!="":
                global_search_clause=self.get_global_search_clause(columns,global_search_value)  #call get_global_search_clause function and get search query string
                global_search_clause= "where "+global_search_clause  
            customefilter=self.get_customfilter(customefilter)
            customefilter_clause=""
            if customefilter!='()':
                customefilter_clause="where "+customefilter
                # if global_search_value=="":
                #     customefilter_clause="where "+customefilter_clause  
            logging.info("customefilter_clause: "+customefilter_clause)         
            
            if str(sort_index) != "0" or global_search_value!="" or customefilter_clause!="":  
                if start_index==0:
                    if customefilter_clause !="":
                       sql_command = f'select * from (SELECT * From {table_name} {global_search_clause} {order_clause}) as dt {customefilter_clause} {order_clause} limit {length}'                  
                    else:
                        sql_command = f'SELECT * From {table_name} {global_search_clause} {order_clause} limit {length}'                 
                else:
                    if customefilter_clause !="":
                        sql_command = f'select * from (SELECT * From {table_name} {global_search_clause} {order_clause} limit {limit_index} offset {start_index}) as dt {customefilter_clause} {order_clause} limit {length}'                 
                    else:   
                        sql_command = f'select * from (SELECT * From {table_name} {global_search_clause} {order_clause} limit {limit_index} offset {start_index}) as dt limit {length}'                 
                logger.info("sql_command1: "+sql_command)
            
            else:
                sql_command = f'SELECT * From {table_name} where "{columns_list[0]}" between {start_index} and {end_index}  {order_clause}'
                logger.info("sql_command2: "+sql_command)            
            return sql_command
        except Exception as exc:
            return str(exc) 

    def is_existing_table(self,connection,table_name,schema):
        """ function used to check the table is Exists or Not in database

        Args:
                table_name[(String)] : [Name of the table]
                schema[String] : [Name of the Schema]
        Return : 
            [String] : [return the True if record found else False]
        """
        sql_command = "SELECT 1 FROM information_schema.tables WHERE table_schema ='"+schema+"' AND table_name = '"+table_name+"'"
        data=self.select_records(connection,sql_command) #call select_records which return data if found else None
        if len(data) == 0: # check whether length of data is empty or not
            self.create_schema(connection)
            return "False"
        else:
            return "True"
    
    def get_row_count(self,connection,dataset_id):
        """ function used to get the row count of the table

        Args:
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
            [Interger] : [return the row count]
        """
        sql_command = "SELECT no_of_rows FROM mlaas.dataset_tbl WHERE dataset_id ="+str(dataset_id)
        row_data=self.select_records(connection,sql_command) #get the record for specific dataset id
        no_of_rows=row_data["no_of_rows"] # get the row count
        return no_of_rows
    
    def get_column_list(self,connection,dataset_id):
        """ function used to get the column name list of the table

        Args:
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
            [List] : [return the list of column name]
        """
        
        sql_command = 'SELECT dataset_table_name,dataset_visibility,user_name FROM mlaas.dataset_tbl  Where dataset_id='+ str(dataset_id)
        dataset_df = self.select_records(connection,sql_command) #get the dataframe for that perticular dataset id if present ortherwise None 
        if len(dataset_df) == 0 or dataset_df is None:
            return None
        
        dataset_records = dataset_df.to_records(index=False) # convert dataframe to a NumPy record  
        
        dataset_table_name,dataset_visibility,user_name = dataset_records[0]  #get 0 index records
        dataset_table_name,dataset_visibility,user_name = str(dataset_table_name),str(dataset_visibility),str(user_name) #convert variable  type into string
         
        if dataset_visibility.lower() == 'public':
            user_name = 'public'
    
        sql_command = 'SELECT * FROM '+ user_name +'.' + dataset_table_name 
        data_details_df = self.select_records(connection,sql_command)
        data_details_df=data_details_df.to_json(orient='records') # transform dataframe based on record
        data_details_df = json.loads(data_details_df)  #convert data_details_df into dictonery
        return data_details_df


        







     