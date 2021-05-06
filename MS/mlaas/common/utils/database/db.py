'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule
 Jay Shukla               15-DEC-2020           1.2           Added functionality for getting single value from the database
 Vipul Prajapati          18-DEC-2020           1.3           Added functionality for create schema.
*/
'''
#Python library imports
import psycopg2
import psycopg2.extras as extras
import pandas as pd 
import numpy as np
import json
import logging
import traceback
from sqlalchemy import create_engine

#database variable file import
from database import *
from ingest.utils.dataset import dataset_creation as dc

#Common utils import
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception.common.common_exception import *

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('dataset_creation')

#? Dataset Class Object
DatasetObject = dc.DatasetClass()
class DBClass:

    def read_data(self,file_path):
        """This function is used read data from server file and load into dataframe.

        Args:
            file_path ([string]): [relative path of the file of server.]

        Returns:
            [dataframe]: [it will return read csv file data in the form of dataframe.]
        """

        read_df=pd.read_csv(file_path) #  Read csv file and load data into dataframe.

        column_name_list = read_df.columns.values.tolist()
    
        column_list = []
        for name in column_name_list:
            if read_df.dtypes.to_dict()[name] == 'object':
                column_list.append(name)
        
        read_df=pd.read_csv(file_path,parse_dates=column_list) #  Read csv file and load data into dataframe.
        
        dataframe = read_df.replace(r'^\s*$', np.nan, regex=True)
        
        return dataframe
    
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

    def create_sequence(self,connection):
        cursor = connection.cursor()
        try:
            sql_command = 'CREATE SEQUENCE dataset_sequence INCREMENT 1 START 1;'
            cursor.execute(sql_command)
            connection.commit()
            cursor.close()
            return 0
        except (Exception,psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor
            return 1 # If failed.

    def get_sequence(self,connection):
        sql_command = "select nextval('dataset_sequence')"
        data = self.select_records(connection, sql_command)
        return data

    def is_exist_sequence(self,connection,seq_name):
        sql_command = "SELECT * FROM information_schema.sequences where sequence_name ='"+ seq_name +"'"
        data=self.select_records(connection,sql_command) #call select_records which return data if found else None
        if len(data) == 0: # check whether length of data is empty or not
            data = self.create_sequence(connection)
            if data == 0:
                return "True"
            else :
                return "False"
        else:
            return "True"

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
            logging.info(str(error))
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor
            return 1 # If failed.
        
    
    
    def insert_records(self,connection,table_name,row_tuples,cols,column_name=None):
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


        cursor = connection.cursor() # Open cursor for database.
        try:
            if column_name == None :
                query = "INSERT INTO %s(%s) VALUES %%s " % (table_name, cols) # Make query
                logging.info(str(table_name) + " <> table_name")
                logging.info(str(cols) + " <> columns")
                logging.info(str(query) + " <> Query")
                logging.info(str(query) + " <> tuples")
                extras.execute_values(cursor, query, tuples) # Excute insert query.
                index = 0
            else :
                query = f"INSERT INTO %s(%s) VALUES %%s RETURNING {column_name} " % (table_name, cols) # Make query
                extras.execute_values(cursor, query, tuples) # Excute insert query.
                index = [row[0] for row in cursor.fetchall()][0]
            
            status = 0
            connection.commit() # Commit the changes.
            cursor.close()
            return status,index # If successfully inserted.
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor.
            logging.error(str(error))
            return 1,None # If failed.

    
    def select_records(self,connection,sql_command):
        """This function is used to retrieve data from database table into dataframe.

        Args:
            connection ([object]): [object of the database connection.],
            sql_command ([string]): [select sql command.]

        Returns:
            [dataframe]: [it will return dataframe of the selected data from the database table.]
        """
        sql_command = str(sql_command) # Get sql command.
        try :
            
           
            data = pd.read_sql(sql_command, connection) # Read data from database table.
            self.update_records(connection,'commit')
            # connection_string = "postgresql://" + user + ":" + password + "@" + host + ":" + port + "/" + database # Make database connection string.
            # engine = create_engine(connection_string) # Create database engine.
            # data = pd.read_sql_query(sql_command, engine) #method of sqlalchemy
            # engine.dispose()
            return data   
        except(Exception, psycopg2.DatabaseError) as error:
            logging.info(str(error) + "check")
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
            logger.info(str(error) + " Error in delete record function")
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
            cursor.close() # Close the cursor.
            status = 0 # If Successfully.
            
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback() # Rollback the changes.
            cursor.close() # Close the cursor.
            status = 1 # If failed
            
            logging.error(str(error))
        return status

    def column_rename(self,file_data_df):
        """This function is used to rename column of dataframe for % , ( , ) this special characters.

        Args:
            file_data_df ([dataframe]): [dataframe of the file data.]

        Returns:
            columns [List of renamed column]: [List of unchanged column]
        """
        df_columns=file_data_df.columns.values
        df_columns_new =[]
        
        for i in df_columns: # this loop check a column name
            str1 =""
            for x in i: # this loop check each character column name
                if '%' in x:
                    str1 += x.replace('%','percent_isg') #It will replace column name when column name contains % 

                elif '(' in x:
                    str1 += x.replace('(','open_Bracket_isg') #It will replace column name when column name contains ( 

                elif ')' in x:
                    str1 += x.replace(')','close_Bracket_isg') #It will replace column name when column name contains )
                    
                else:
                    str1 += x
            df_columns_new.append(str1) # it append the renamed column name

        return df_columns_new ,df_columns # it returns list of changed and unchanged column name

    def load_df_into_db(self,connection_string,table_name,file_data_df,user_name):
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
            
            file_data_df.to_sql(table_name,engine,schema=schema_name, chunksize=10000) # Load data into database with table structure.
            
            status = 0 # If successfully.
        except Exception as e:
            logging.error("Exception: "+str(e))
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
    
    
    def get_schema_columnlist(self, connection,schema_id,type):
        col_cursor = connection.cursor()
        # sql_command = "select case when changed_column_name='' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id =1 and column_attribute!='Ignore' order by index" 
        if type=="schema":
            sql_command = "select column_name column_list  from mlaas.schema_tbl where schema_id ="+str(schema_id)+" and column_attribute!='Ignore' order by index"           
        elif type=="Select":
            sql_command = "select case when changed_column_name='' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id="+str(schema_id)+" and column_attribute='Select' order by index"    
        elif type== "all":
            sql_command = "select column_name, case when changed_column_name='' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id="+str(schema_id)+" order by index"
            
            #Execute sql query and return dataframe 
            dataframe = self.select_records(connection,sql_command)
            
            #Get the previous column name and changed column name from the schema table
            prev_col_name,current_col_name =list(dataframe['column_name']),list(dataframe['column_list']) 
            return prev_col_name,current_col_name

        else:
            sql_command = "select case when changed_column_name='' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id="+str(schema_id)+" and column_attribute!='Ignore' order by index"           
        
        logger.info(sql_command)
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
    

    
    def get_order_clause(self,connection,schema_id,table_name,sort_type,sort_index):    
        """ function used to get ORDER by clause string

        Args:
            table_name[(String)] : [Name of the table]
            sort_type[(String)] : [value of the sort type]
            sort_index[(integer)] : [index of column]
        Return : 
            [String,List] : [return the Order clause,list of column name]
        """ 
        if schema_id != None:
            columns_list=self.get_schema_columnlist(connection,schema_id,type="ab") #get the column list   
        else:
            col_table_name=table_name.partition(".")[2] #trim from the string and get the table name
            col_table_name=col_table_name[1:-1]
            columns_list=self.get_column_names(connection,col_table_name) #get the column list    
        if sort_type =="asc" and  str(sort_index) == "0":  #check if value sort_type and sort_index is empty
            order_clause=f'ORDER BY "{columns_list[0]}"'
        else:
            order_clause=f'ORDER BY "{columns_list[int(sort_index)]}" {sort_type}' #formated string for order By clause 
        return order_clause,columns_list
    
    def get_global_search_clause(self,connection,schema_id,columns,global_value):
        """ function used to create search  string for sql command

        Args:
            table_name[(String)] : [Name of the table]
            sort_type[(String)] : [value of the sort type]
            sort_index[(integer)] : [index of column]
        Return : 
            [String] : [return the search pattern string]
        """ 
        if schema_id != None:
            columns_list=self.get_schema_columnlist(connection,schema_id,type="schema") 
            columns=columns_list[1:]
        else:
            columns=columns     
        empty_string=""
        global_value=global_value.lower()
        for i in range(len(columns)):
            empty_string+="lower(cast(\""+str(columns[i])+"\" as varchar)) like '%"+str(global_value)+"%' or "   # create the string with Like operator  
        global_search_clause="("+empty_string[:len(empty_string)-3]+")" # remove the "or" string appended at last 
        return global_search_clause
    
    def get_customfilter(self,connection,customefilter):
        """ function used to get customfilter clause
        Args:
            customefilter ([type]): [dictionary]
        Returns:
            [String]: [retun the custom filter string]
        """
        dict=customefilter
        empty_string=""
        for x in dict:
            if dict[x]!="":
                dict[x]=dict[x].replace("'","''")
                dict[x]=dict[x].lower()
                empty_string+="lower(cast(\""+x+"\" as varchar)) like '%"+dict[x]+"%' or "
        customefilter="("+empty_string[:len(empty_string)-3]+")" # remove the "or" string appended at last 
        return customefilter
    
    def get_query_string(self,connection,schema_id):
        try:
            logging.info("database : DBClass : get_query_string : Execution start")

            # sql command to get details from schema table  based on  schema id 
            sql_command = "select column_name,case when changed_column_name = '' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id ="+str(schema_id)+"and column_attribute !='Ignore' order by index"
            
            #execute sql commnad if data exist then return dataframe else return None
            schema_df = self.select_records(connection,sql_command) 

            #extract the column name and column_list
            column_name,column_list = schema_df['column_name'],schema_df['column_list']

            string_query = ""
            for count in range(0,len(column_name)):
                #append string column name as alias  column list name
                string_query +='"'+column_name[count]+'" as "'+column_list[count]+'",'
            
            logging.info("database : DBClass : get_query_string : Execution stop")
            return string_query[:len(string_query)-1]
        except  Exception as exc:
            logging.error("database : DBClass : get_query_string : Exception " + str(exc))
            return str(exc)

    
    def pagination(self,connection,table_name,start_index,length,sort_type,sort_index,global_search_value,customefilter,schema_id):
        """ function used to create Sql query string

        Args:
                start_index[(Integer)] : [value of the starting index]
                length[(Integer)] :[value of length of records to be shown]
                sort_type[(String)] : [value of sort_type ascending or descending]
                sort_index[(Integer)] : [index value of the column to perform sorting]
                global_value[(String)] : [value that need be search in table]
                
        Return : 
            [String] : [return the sql query string for data]
            [String] : [return the sql query string for filter row count]
        """
        try: 
            end_index = (start_index + length)-1 #get total length
            limit_index=start_index+length #calculate limit
            order_clause,columns_list=self.get_order_clause(connection,schema_id,table_name,sort_type,sort_index) #call get_order_clause function and get order by string and column list            
            columns=columns_list[1:] #remove first column
            global_search_clause="" #initialize global_search_clause
            if global_search_value!="":
                global_search_clause=self.get_global_search_clause(connection,schema_id,columns,global_search_value)  #call get_global_search_clause function and get search query string
                global_search_clause= "where "+global_search_clause  #add where to global_search_clause
            customefilter=self.get_customfilter(connection,customefilter) #call get_customfilter value
            customefilter_clause="" #initialize customefilter_clause
            if schema_id == None:
                select_clause="*"
            else:
                query = self.get_query_string(connection,schema_id)
                # select_clause=str(columns_list[0])+","+str(query)
                select_clause=str(query)
            if customefilter!='()':
                customefilter_clause="where "+customefilter #add where to customefilter_clause 
            if str(sort_index) != "0" or global_search_value!="" or customefilter_clause!="":  
                if start_index==0:                              #checking column
                    if customefilter_clause !="":
                        sql_data = f'select * from (SELECT {str(select_clause)} From {table_name} {global_search_clause} {order_clause}) as dt {customefilter_clause} {order_clause} limit {length}'   #sql Query with customefilter_clause
                        sql_filtercount = f'select count(*) from (SELECT {str(select_clause)} From {table_name} {global_search_clause} ) as dt {customefilter_clause} ' #sql Query for filter row count                             
                    else:
                        sql_data = f'SELECT {str(select_clause)} From {table_name} {global_search_clause} {order_clause} limit {length}'  #sql Query without customefilter_clause 
                        sql_filtercount = f'SELECT count(*) From {table_name} {global_search_clause}'   #sql Query for filter row count                             
                else:
                    if customefilter_clause !="":
                        sql_data = f'select {str(select_clause)} from (SELECT * From {table_name} {global_search_clause} {order_clause} limit {limit_index} offset {start_index}) as dt {customefilter_clause} {order_clause} limit {length}'  #sql Query with customefilter_clause
                        sql_filtercount = f'select count(*) from (SELECT {str(select_clause)} From {table_name} {global_search_clause}) as dt {customefilter_clause}'#sql Query for filter row count                              
                    else:   
                        sql_data = f'select {str(select_clause)} from (SELECT * From {table_name} {global_search_clause} {order_clause} limit {limit_index} offset {start_index}) as dt limit {length}' #sql Query for filter row count  
                        sql_filtercount = f'select count(*) from (SELECT {str(select_clause)} From {table_name} {global_search_clause}) as dt'  #sql Query for filter row count                                 
            
            else:
                sql_data =  f'SELECT {str(select_clause)} From {table_name} where "{columns_list[0]}" >= {start_index} {order_clause} limit {length}' # sql Query without any filter and clause 
                sql_filtercount = f'SELECT count(*) From {table_name}' #sql Query with customefilter_clause

            logger.info("sql_data===="+str(sql_data))
            return sql_data,sql_filtercount
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
        print(str(data) + "checking")
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

        column_list=self.get_column_names(connection,dataset_table_name)


        return column_list
    

    #! The Function of the DB Class is itself taking DBObject as an input... which is unnecessary & logically wrong. 
    #TODO: We will have to remove DBObject from the function parameters. Because 'self' itself means DBObject.
    def get_dataset_detail(self,DBObject,connection,dataset_id):
        '''This function is used to get dataset table name from dataset id
        Args:
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
                [Dataframe] : [return the dataframe of dataset table ]
        '''
        # sql_command = "SELECT dataset_name,dataset_table_name,user_name,dataset_visibility,no_of_rows,dataset_desc from mlaas.dataset_tbl Where dataset_id =" + str(dataset_id)
        sql_command = "SELECT dataset_name,file_size,file_name,dataset_table_name,user_name,dataset_visibility,no_of_rows,dataset_desc from mlaas.dataset_tbl Where dataset_id =" + str(dataset_id)
        dataset_df=self.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        return dataset_df 
    
    def get_project_detail(self,connection,project_id):
        '''This function is used to get details for project table.
        Args:
                project_id[(Integer)] : [Id of the project table]
        Return : 
                [Dataframe] : [return the dataframe of project table]
        '''
        sql_command = "SELECT user_name,original_dataset_id,dataset_id,project_name,model_status,cleanup_dag_id from mlaas.project_tbl where project_id='"+str(project_id)+"'"
       
        dataset_df=self.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        return dataset_df
    
    def get_table_name(self,connection,table_name):
        """
        function used to create table name by adding unique sequence number init.
        Args :
                table_name[(String)] : [Name of old table]
        Return :
                [String] : [return the table name]
        """
        logging.info("data ingestion : SchemaClass : get_table_name : execution start")
        split_value = table_name.split('_tbl')[0].split('_')[-1] # Extract the sequence number
        table_name = table_name.split(split_value) # split with the sequence number
        seq = self.get_sequence(connection) #get the sequence number
        table_name = table_name[0]+str(seq['nextval'][0])+table_name[1] #create table name by joining sequence
        logging.info("data ingestion : SchemaClass : get_table_name : execution stop")
        return table_name
    
    def user_authentication(self,connection,user_name,password):
        """[summary]

        Args:
            connection ([String]): [connection String]
            user_name ([String]): [User Name]
            password ([String]): [password]

        Raises:
            UserAuthenticationFailed: [User authentication failed]
        Returns:
            [String]: [if user authenticated then it return True]
        """
        try:
            sql_command = "SELECT user_name from mlaas.user_auth_tbl where user_name='"+ str(user_name) +"' and password='"+ str(password) +"'"
            user_df = self.select_records(connection,sql_command)
            if user_df is None:
                raise UserAuthenticationFailed(500)          
            if len(user_df) > 0 :
                return True
            else:
                raise UserAuthenticationFailed(500)
        except UserAuthenticationFailed as exc:
            return exc.msg
  
    def get_raw_dataset_detail(self,connection,original_dataset_id):
        """
        function used to get the row dataset details based on  original dataset id where dataset name are equal but
        page name is "schema mapping".

        Args:
                original_dataset_id[(Integer)] : [Id on dataset table]
        return :
                dataset_id[Integer] : [Id of the raw dataset]
                dataset_table_name[String] : [Name of the table ] 

        """
        try:
            #sql command to get dataset_name based on original dataset id
            sql_Command = "SELECT dataset_name from mlaas.dataset_tbl where dataset_id ='"+str(original_dataset_id)+"' "

            #execute the sql command and get te dataframe if found else None
            dataframe = self.select_records(connection,sql_Command)

            #get the dataset_name
            dataset_name = dataframe['dataset_name'][0]
            
            #sql command to get Raw dataset id based on the dataset_name and page_name 
            sql_Command = "SELECT dataset_id,dataset_table_name from mlaas.dataset_tbl where dataset_name='"+str(dataset_name)+"' and page_name ='schema mapping'"
            

            #execute the sql command and get te dataframe if found else None
            dataframe = self.select_records(connection,sql_Command)
            
            #get the dataset id
            dataset_id = int(dataframe['dataset_id'][0])
            table_name = str(dataframe['dataset_table_name'][0])
           

            return dataset_id,table_name
        except Exception as exc:
            return exc,None

    def get_dataset_df(self, connection, dataset_id, schema_id = None):
        '''
            Returns a dataframe containing data of given dataset_id & schema_id.  
            If schema_id is not given then it returns whole datatable without schema changes. 
            
            Args:
                connection(Object): Postgres Connection Object.
                dataset_id(Intiger): id of the dataset.
                schema_id(Intiger) [default None]: id of the dataset in the schema table.
                
            Returns:
                data_df(pandas.DataFrame): Dataframe containing the data.
        '''
        
        try:
            logging.info("database : DBClass : get_dataset_df : execution start")
            
            #? getting the name of the dataset_tbl
            table_name,_,_ = DatasetObject.make_dataset_schema()
            
            #? Getting user_name and dataset_visibility
            sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY,DATASET_TABLE_NAME,no_of_rows FROM {table_name} WHERE dataset_id = '{dataset_id}'"
            visibility_df = self.select_records(connection,sql_command) 
            if len(visibility_df) != 0: 
                user_name,dataset_visibility = visibility_df['user_name'][0],visibility_df['dataset_visibility'][0]
            #? No entry for the given dataset_id        
            else: raise EntryNotFound(500)
            
            #? Getting CSV table name
            dataset_table_name = visibility_df['dataset_table_name'][0]
            dataset_table_name = '"'+ dataset_table_name+'"'
            
            #? changing the database schema for the public databases
            if dataset_visibility == 'public':
                user_name = 'public'
            
            #? Get Whole table
            if schema_id is None:
                sql_command = f"SELECT * FROM {user_name}.{dataset_table_name}"
            
            #? Get table with schema changes applied
            else:
                query = self.get_query_string(connection,schema_id)
                #? Getting all the data
                sql_command = f"SELECT {str(query)} FROM {user_name}.{dataset_table_name}"
                
            data_df = self.select_records(connection,sql_command)    
            data_df = data_df.replace([''],np.NaN)
            
            logging.info("database : DBClass : get_dataset_df : execution stop")

            return data_df
            
        except (EntryNotFound) as exc:
            logging.error("database : DBClass : get_dataset_df : Exception " + str(exc.msg))
            logging.error("database : DBClass : get_dataset_df : " +traceback.format_exc())
            return exc.msg
        
    def get_target_col(self, connection, schema_id):
        '''
            Returns a list containing target columns.
            
            Args:
            -----
            connection (`Object`): Postgres Connection Object.
            schema_id (`Intiger`): id of dataset in the schema table.
            
            Returns:
            -------
            target_cols (`List`): List of the Names of Target Columns.
        '''
        try:
            logging.info("database : DBClass : get_target_col : Execution Start")
            
            sql_command = f"select case when changed_column_name = '' then column_name else changed_column_name end column_name from mlaas.schema_tbl st where st.schema_id = '{schema_id}' and st.column_attribute = 'Target'"
            target_df = self.select_records(connection,sql_command)
            
            target_lst = target_df['column_name']
            
            logging.info("database : DBClass : get_target_col : Execution Stop")
            return target_lst.tolist()

        except Exception as exc:
            logging.error("database : DBClass : get_target_col : Exception " + str(exc))
            return str(exc)

    
    def get_active_table_name(self, connection, dataset_id):
        '''
            Returns the Name of the raw data table thats currently associated with the project.
            
            Args:
            -----
            connection (`Object`): Postgres Connection Object.
            dataset_id (`Intiger`): id of the dataset.
            
            Returns:
            --------
            dataset_table_name (`String`): Name of the raw data table.
        '''
        try:
            logging.info("database : DBClass : get_active_table_name : Execution Start")
            
            dataframe = self.get_dataset_detail(self,connection,dataset_id)

            #Extract the dataframe based on its column name as key
            table_name,dataset_visibility,user_name = str(dataframe['dataset_table_name'][0]),str(dataframe['dataset_visibility'][0]),str(dataframe['user_name'][0])
            
            if dataset_visibility == 'private':
                dataset_table_name = user_name+'."'+table_name+'"'
            else:
                dataset_table_name = 'public'+'."'+table_name+'"'

            logging.info("database : DBClass : get_active_table_name : Execution Stop")
            return dataset_table_name

        except Exception as exc:
            logging.error("database : DBClass : get_active_table_name : Exception " + str(exc))
            return str(exc)


    def create_score_view(self,connection):
        
        sql_command = "CREATE OR REPLACE VIEW mlaas.score_view "\
                      "AS SELECT a.experiment_id,a.project_id,"\
                      "a.run_uuid,a.cv_score,mr.value AS holdout_score "\
                      "FROM ( SELECT met.experiment_id,met.project_id,"\
                      "met.run_uuid,m.key,m.value AS cv_score "\
                      "FROM mlaas.model_experiment_tbl met left outer join mlflow.metrics m "\
                      "ON met.run_uuid = m.run_uuid AND m.key = 'cv_score') a left outer join mlflow.metrics mr "\
                      "ON a.run_uuid = mr.run_uuid AND mr.key = 'holdout_score';"
                      
        status = self.update_records(connection,sql_command)
        
        return status
    

    def get_schema_column(self,connection,schema_id):
        '''
        Function used to get the column name list from the schema table based on the schema id.
        Args :
                schema_id[(Integer)] : [Id of the schema table]
        Return :
                column_list[(List)] : [Name of the column ]

        '''
        sql_command = f"select column_name from mlaas.schema_tbl where schema_id = '{str(schema_id)}' order by index"

        data_df = self.select_records(connection,sql_command)
       
        column_list = list(data_df['column_name'])
        return column_list
    
    def change_datatype(self, connection,column_string, table_name,type='float8'):
        """[it will change data type of table]

        Args:
            column_string ([type]): [column name which we want to change type]
            table_name ([type]): [table name]

        Returns:
            [status]: [0,1]
        """
        sql_command = f'ALTER TABLE {table_name} ALTER COLUMN "{str(column_string)}" type "{type}"'
        logger.info("sql_command==="+sql_command) 
        status = self.update_records(connection,sql_command)   
        return status
           
    def get_column_df(self, connection, table_name,column_string):
        
        """[This function return specific column dataframe]

        Returns:
            [pandas df]: [specific column df]
        """
        
        sql_command = f'SELECT "{str(column_string)}" FROM {table_name} order by index'
        data_df = self.select_records(connection,sql_command)   
        return data_df 
    
    def get_tablename(self,connection,dataset_id):
        """[This function used to get table name from dataset_id]

        Args:
            connection ([object]): [[psetgres connection string]
            dataset_id ([integer]): [dataset_id]

        Raises:
            EntryNotFound: [Dataset Entry is not found]

        Returns:
            [table_name]: [it will return dataset table name]
        """
        
        #? getting the name of the dataset_tbl
        table_name,_,_ = DatasetObject.make_dataset_schema()
        
        #? Getting user_name and dataset_visibility
        sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY,DATASET_TABLE_NAME,no_of_rows FROM {table_name} WHERE dataset_id = '{dataset_id}'"
        visibility_df = self.select_records(connection,sql_command) 
        if len(visibility_df) != 0: 
            user_name,dataset_visibility = visibility_df['user_name'][0],visibility_df['dataset_visibility'][0]
        #? No entry for the given dataset_id        
        else: raise EntryNotFound(500)
        
        #? Getting CSV table name
        dataset_table_name = visibility_df['dataset_table_name'][0]
        dataset_table_name = '"'+ dataset_table_name+'"'
        
        #? changing the database schema for the public databases
        if dataset_visibility == 'public':
            user_name = 'public'
            
        dataset_table_name=user_name+"."+dataset_table_name
        return dataset_table_name
    
    
    def check_column_type(self,connection,dataset_id,prev_col_name):
        """[check the column contains positive,negative and zero]

        Args:
            dataset_id ([type]): [dataset_id]
            prev_col_name ([type]): [old column name]

        Returns:
            [is_positve_flag]: [flag True or Flaseption]
            [is_zero_flag]: [flag True or Flase]

        """
        
        tablename=self.get_tablename(connection,dataset_id)
        
        sql_command=f'select count(*) as negative_count from {tablename} where "{prev_col_name}"<0'
        
        negative_data_df = self.select_records(connection,sql_command)
        
        negative_count = negative_data_df['negative_count'].tolist()[0]
        
        if negative_count == 0:
            is_positve_flag=True
        else:
            is_positve_flag=False
        
       
        sql_command=f'select count(*) as zero_count from {tablename} where "{prev_col_name}"=0'
        
        zero_data_df = self.select_records(connection,sql_command)
        
        zero_count = zero_data_df['zero_count'].tolist()[0]
        if zero_count == 0:
            is_zero_flag=False
        else:
            is_zero_flag=True
            
        return is_positve_flag,is_zero_flag

    def get_feature_df(self, connection, dataset_id,col):
        '''
            Returns a dataframe containing data of given dataset_id & schema_id.  
            If schema_id is not given then it returns whole datatable without schema changes. 
            
            Args:
                connection(Object): Postgres Connection Object.
                dataset_id(Intiger): id of the dataset.
                schema_id(Intiger) [default None]: id of the dataset in the schema table.
                
            Returns:
                data_df(pandas.DataFrame): Dataframe containing the data.
        '''
        
        try:
            logging.info("database : DBClass : get_dataset_df : execution start")
            
            #? getting the name of the dataset_tbl
            table_name,_,_ = DatasetObject.make_dataset_schema()
            
            #? Getting user_name and dataset_visibility
            sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY,DATASET_TABLE_NAME,no_of_rows FROM {table_name} WHERE dataset_id = '{dataset_id}'"
            visibility_df = self.select_records(connection,sql_command) 
            if len(visibility_df) != 0: 
                user_name,dataset_visibility = visibility_df['user_name'][0],visibility_df['dataset_visibility'][0]
            #? No entry for the given dataset_id        
            else: raise EntryNotFound(500)
            
            #? Getting CSV table name
            dataset_table_name = visibility_df['dataset_table_name'][0]
            dataset_table_name = '"'+ dataset_table_name+'"'
            
            #? changing the database schema for the public databases
            if dataset_visibility == 'public':
                user_name = 'public'
            
            #? Get Whole table
            query_string = ""
            for i in range(len(col)):
                query_string += '"'+col[i]+'",'
            
            query_string = query_string[:len(query_string)-1]
            logging.info("+++>"+str(query_string))
            
            sql_command = f"SELECT {query_string} FROM {user_name}.{dataset_table_name}"
            logging.info("))))"+str(sql_command))
                
            data_df = self.select_records(connection,sql_command)    
            data_df = data_df.replace([''],np.NaN)
            
            logging.info("database : DBClass : get_dataset_df : execution stop")
            return data_df
            
        except (EntryNotFound) as exc:
            logging.error("database : DBClass : get_dataset_df : Exception " + str(exc.msg))
            logging.error("database : DBClass : get_dataset_df : " +traceback.format_exc())
            return exc.msg
            
