'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version. 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule.
 Jay Shukla               15-DEC-2020           1.2           Added Deletion Functionality.
 Vipul Prajapati          05-JAN-2021           1.3           no_of_rows field added into dataset tbl.           
*/
'''

# Python library imports
import os
import pandas as pd
import logging
import traceback

# Common file imports
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.logger_handler import custom_logger as cl
#from common.utils.database.db import DBClass
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('dataset_creation')


class DatasetClass:
   
    def make_dataset_schema(self):
        """ This function is used to make schema for creating dataset table.

        Returns:
            [string]: [it will return name of the table, structure of the table and columns of the table.]
        """
        logging.info("data ingestion : DatasetClass : make_dataset_schema : execution start")
        # Dataset table name
        table_name = 'mlaas.dataset_tbl' 
        # Columns for dataset table.
        cols = 'dataset_name,file_name,file_size,dataset_table_name,dataset_visibility,user_name,dataset_desc,page_name' 
        #v1.3
        # Schema for dataset table.
        schema = "dataset_id bigserial,"\
                 "dataset_name text,"\
                 "file_name text,"\
                 "file_size text,"\
                 "no_of_rows integer NOT NULL DEFAULT 0,"\
                 "dataset_table_name  text,"\
                 "dataset_visibility text,"\
                 "user_name text,"\
                 "dataset_desc text,"\
                 "page_name text,"\
                 "created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()" 
                 
        logging.info("data ingestion : DatasetClass : make_dataset_schema : execution end")          
        return table_name,schema,cols

    def  make_dataset_records(self,dataset_name,file_name,dataset_visibility,user_name,dataset_desc,page_name):
        """This function is used to make records for inserting data into table based on input dataframe.
           E.g. column_name_1,column_name_2 .......,column_name_n.

        Args:
            dataset_name ([string]): [name of the dataset.],
            file_name ([string]): [name of the file.],
            dataset_visibility ([string]): [visibility of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [tuple]: [it will return records in the form of tuple.]
        """
        logging.info("data ingestion : DatasetClass : make_dataset_records : execution start")
        
        file_path = self.get_file_path(file_name,dataset_visibility,user_name)
        file_size = self.get_file_size(file_path)# Get size of uploaded file.
        dataset_table_name = self.get_dataset_table_name(file_name) # Make table name for loaded csv.
        row=dataset_name,file_name,file_size,dataset_table_name,dataset_visibility,user_name,dataset_desc,page_name # Make record for dataset table.
        logging.info("row error"+str(row))
        row_tuples = [tuple(row)] # Convert row record into list of tuple.
        logging.info("row tuples error"+str(row_tuples))
        logging.info("data ingestion : DatasetClass : make_dataset_records : execution end")
        return row_tuples
    
    def get_file_path(self,file_name,dataset_visibility,user_name):
        """This function is used to get server file path.

        Args:
            file_name ([string]): [name of the file.],
            dataset_visibility ([string]): [visibility of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [string]: [it will return path of the file.]
        """
        logging.info("data ingestion : DatasetClass : get_file_path : execution start")
        if dataset_visibility.lower() == "public" :
            file_path = './static/server/' + dataset_visibility + "/" + file_name
        else:
            file_path = './static/server/' + user_name + "/" + file_name 
        
        logging.info("data ingestion : DatasetClass : get_file_path : execution end")
        return file_path
    
    def get_file_size(self,file_path):
        """This function is used to get size of the file.

        Args:
            file_path ([string]): [relative path of the file.]

        Returns:
            [string]: [it will return size of the file. in GB or MB or KB.]
        """
            
        logging.info("data ingestion : DatasetClass : get_file_size : execution start")
        file_size = os.path.getsize(file_path)
        max_size = 512000
        if file_size < max_size:
            value = round(file_size/1000, 2)
            ext = ' kb'
        elif file_size < max_size * 1000:
            value = round(file_size/1000000, 2)
            ext = ' Mb'
        else:
            value = round(file_size/1000000000, 2)
            ext = ' Gb' 
            
        logging.info("data ingestion : DatasetClass : get_file_size : execution end")
        return str(value)+ext
    
    def get_dataset_table_name(self,file_name):
        """This function is used to get dataset table name.

        Args:
            file_name ([string]): [name of the file.]

        Returns:
            [string]: [it will return name of the table.]
        """
        logging.info("data ingestion : DatasetClass : get_dataset_table_name : execution start")
        table_name = ("di_" + file_name.replace(".csv","") + "_" + "tbl").lower()
        logging.info("data ingestion : DatasetClass : get_dataset_table_name : execution end")
        return table_name
        
 

    def make_dataset(self,DBObject,connection,connection_string,dataset_name,file_name,dataset_visibility,user_name,dataset_desc,page_name,flag=True,row_creation_flag=True):
        """This function is used to main dataset table and also load main dataset details into database table.
           E.g. dataset details : dataset_name,file_name,file_size,dataset_table_name,user_name.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            dataset_name ([string]): [name of the dataset.],
            file_name ([string]): [name of the file.],
            dataset_visibility ([string]): [visibility of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [string,integer]: [it will return status of dataset creation. if successfully created then 1 else 0.
                                and also return dataset id of created dataset.]
        """
        logging.info("data ingestion : DatasetClass : make_dataset : execution start")
        
        schema_status = DBObject.create_schema(connection)
        table_name,schema,cols = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        original_dataset_id = 0
        if flag == True:
            #? Checking if the same dataset is there for the same user in the dataset table? If yes, then it will not insert a new row in the table
            dataset_exist = self.dataset_exists(DBObject,connection,table_name,dataset_visibility,dataset_name,user_name)
            if dataset_exist == False: pass #? No dataset with same name exists so creating the new one
            else: return 2,dataset_exist,None #? dataset_exists() function returns id of the dataset if dataset with same name exists
        
        create_status = DBObject.create_table(connection,table_name,schema) # Get status about dataset tableis created or not.if created then 0 else 1.
        row_tuples = self.make_dataset_records(dataset_name,file_name,dataset_visibility,user_name,dataset_desc,page_name) # Get record for dataset table.
        insert_status,_ = DBObject.insert_records(connection,table_name,row_tuples,cols) # Get status about inserting records into dataset table. if successful then 0 else 1.


        # Condition will check dataset table created and data is successfully stored into project table or not.if both successful then 0 else 1. 
        if schema_status in [0,1] and create_status in [0,1] and insert_status == 0 :
            if flag == True:
                original_dataset_id = self.get_dataset_id(DBObject,connection,row_tuples,user_name,flag)
                
            else:
                raw_dataset_id = self.get_dataset_id(DBObject,connection,row_tuples,user_name,flag)

            status = 0 # If Successfully.
            if row_creation_flag == True:
                load_data_status,no_of_rows = self.load_dataset(DBObject,connection,connection_string,file_name,dataset_visibility,user_name)
            else:
                # raw_no_of_rows = DBObject.get_row_count(connection , oid)
                # logging.info("========>"+str(raw_no_of_rows))
                load_data_status = self.insert_raw_dataset(DBObject,connection,raw_dataset_id,user_name,file_name,dataset_visibility)
            
    
            if load_data_status == 1:
                return 1,None,None
            else:
                if row_creation_flag == True:
                    sql_command = "UPDATE "+str(table_name)+" set no_of_rows="+str(no_of_rows)+" where dataset_id="+str(original_dataset_id)
                    update_status = DBObject.update_records(connection,sql_command)
            
                
            if flag == True:
                if row_creation_flag == True:
                    page_name='schema mapping'
                
                    status,_,raw_dataset_id=self.make_dataset(DBObject,connection,connection_string,dataset_name,file_name,dataset_visibility,user_name,dataset_desc,page_name,flag=False,row_creation_flag=False)
                    
        else :
            status = 1 # If Failed.
            original_dataset_id = None
            raw_dataset_id = None

        logging.info("data ingestion : DatasetClass : make_dataset : execution end")
        return status,original_dataset_id,raw_dataset_id
    
    def load_dataset(self,DBObject,connection,connection_string,file_name,dataset_visibility,user_name):
        """This function is used to load csv file data into database table.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            connection_string ([string]): [connection string of the database.],
            file_name ([string]): [name of the file.],
            dataset_visibility ([string]): [visibility of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [type]: [it will return status about loaded data.if successfully then 1 else 0.]
        """
        logging.info("data ingestion : DatasetClass : load_dataset : execution start")
        # Get file relative file path.
        file_path = self.get_file_path(file_name,dataset_visibility,user_name)
        # Get dataframe of the file data.
        
        file_data_df = DBObject.read_data(file_path)
        logging.info("---->"+str(file_data_df))
        # Get number of rows.
        no_of_rows = file_data_df.shape[0]
        logger.info("no_of_rows:===="+str(no_of_rows))
        # Get table name.
        
        table_name = self.get_dataset_table_name(file_name)
        
            
        if dataset_visibility.lower() == "public" :
            user_name = "public"
        else:
            user_name = user_name
        # Get schema status.if successfully then 0 else 1.
        schema_status = DBObject.create_schema(connection,user_name)
        # Get load dataset status. if successfully then 0 else 1.
        load_dataset_status = DBObject.load_df_into_db(connection_string,table_name,file_data_df,user_name)
        
        logging.info("data ingestion : DatasetClass : load_dataset : execution end")
        return load_dataset_status,no_of_rows
    
    def get_dataset_id(self,DBObject,connection,row_tuples,user_name,page_name=True):
        """This function is used to get dataset id of the created dataset.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            row_tuples ([list]): [list of the tuple of dataset record.],
            user_name ([string]): [name of the user.]

        Returns:
            [integer]: [it will return dataset id of the created dataset.]
        """
        logging.info("data ingestion : DatasetClass : get_dataset_id : execution start")
        # Get table name.
        table_name,*_ = self.make_dataset_schema()
        # Get dataset name.
        logging.info("index of list",str(row_tuples))
        dataset_name,*_ = row_tuples[0]

        logging.debug("data ingestion : DatasetClass : get_dataset_id : this will excute select query on table name : "+table_name +" based on dataset name : "+dataset_name + " user name : "+user_name)
        
        # Prepare select sql command to fetch dataset id from dataset table for particular user.
        dataset_name=str(dataset_name).replace("'","''")
        if page_name == False:
            sql_command = "SELECT dataset_id from "+ table_name + " Where dataset_name ='" + dataset_name + "' and user_name = '"+ user_name + "' and page_name='schema mapping'"
            logging.info(str(sql_command) + "command")
        else:
            sql_command = "SELECT dataset_id from "+ table_name + " Where dataset_name ='" + dataset_name + "' and user_name = '"+ user_name + "' "
            logging.info(str(sql_command) + "command")
        # Get dataframe of dataset id. 
        dataset_df = DBObject.select_records(connection,sql_command)

        # Get dataset id.
        dataset_id = int(dataset_df['dataset_id'][0])
        
        logging.info("data ingestion : DatasetClass : get_dataset_id : execution end")
        return dataset_id

    def show_dataset_details(self,DBObject,connection,user_name):
        """This function is used to show details about all created datasets by user.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataset details in the form of dataframe.]
        """
        logging.info("data ingestion : DatasetClass : show_dataset_details : execution start")
        table_name,_,cols = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        
        logging.debug("data ingestion : DatasetClass : show_dataset_details : this will excute select query on table name : "+str(table_name) +" based on user name : "+str(user_name))
        
        # This command is used to get dataset details from dataset table of database.
        sql_command = "SELECT * FROM "+ table_name + " WHERE (USER_NAME ='"+ user_name +"' OR dataset_visibility='public') and page_name in ('Create dataset','Create Project','schema save') and no_of_rows != 0"
        
        data=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        logging.info("data ingestion : DatasetClass : show_dataset_details : execution end")
        return data

    def show_data_details(self,DBObject,connection,dataset_id,start_index,length,sort_type,sort_index,global_value,customefilter,schema_id):
        """This function is used to show details about loaded dataset.
 
        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            table_name ([string]): [name of the table.]
 
        Returns:
            [dataframe]: [it will return loaded csv data in the form of dataframe.]
        """
        logging.info("data ingestion : DatasetClass : show_data_details : execution start")
       
        table_name,*_ = self.make_dataset_schema()
        
        logging.debug("data ingestion : DatasetClass : show_data_details : this will excute select query on table name : "+table_name +" based on dataset id : "+str(dataset_id))
        
        sql_command = 'SELECT dataset_table_name,dataset_visibility,user_name FROM ' + table_name + ' Where dataset_id='+ str(dataset_id)
        # Get dataframe of loaded csv.
        dataset_df = DBObject.select_records(connection,sql_command) 
        if len(dataset_df) == 0 or dataset_df is None:
            return None
        
        dataset_records = dataset_df.to_records(index=False)
        
        dataset_table_name,dataset_visibility,user_name = dataset_records[0]
        dataset_table_name,dataset_visibility,user_name = str(dataset_table_name),str(dataset_visibility),str(user_name)
         
        if dataset_visibility.lower() == 'public':
            user_name = 'public'
        # This command is used to get data details (i.e. loaded csv file data) from database.
        
        logging.debug("data ingestion : DatasetClass : show_data_details : this will excute select query on table name : "+ user_name +'.' + dataset_table_name )
        dataset_table_name=user_name +'."' + dataset_table_name +'"'
        sql_data,sql_filtercount=DBObject.pagination(connection,dataset_table_name,start_index,length,sort_type,sort_index,global_value,customefilter,schema_id)
        # Get dataframe of loaded csv.
        data_details_df = DBObject.select_records(connection,sql_data) 
        data_details_count_df = DBObject.select_records(connection,sql_filtercount) 
        
        logging.info(str(data_details_count_df) + "check")

        filtercount= data_details_count_df["count"]
        logging.info("data ingestion : DatasetClass : show_data_details : execution end")
        return data_details_df,filtercount

    #* Version 1.2
    def delete_dataset_details(self,DBObject,connection,dataset_id,user_name,skip_check = False):
        """This function is used to delete dataset entry from the dataset table.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            dataset_id ([integer]): [dataset id for the delete dataset record.],
            user_name ([string]): [name of the user.],
            skip_check ([boolean]): [Make this true if you don't want to check how many projects are using this dataset.], Defaults to False.

        Returns:
            [integer]: [it will return status of the dataset deletion. if successfully then 0 else 1.]
        """

        logging.info("data ingestion : DatasetClass : delete_dataset_details : execution start")

        table_name,_,_ = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        
        logging.debug("data ingestion  :  DatasetClass  :  delete_dataset_details  :  Trying to get user_name & dataset_visibility from dataset_tbl")
        sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY FROM {table_name} WHERE dataset_id = '{dataset_id}'"
        user_name_df = DBObject.select_records(connection,sql_command) 
        if  len(user_name_df) == 0:
            logging.debug(f"data ingestion  :  DatasetClass  :  delete_dataset_details  :  No entry found for the giver dataset_id = {dataset_id}")
            return 5,_
        
        user_name_from_table,dataset_visibility = user_name_df['user_name'][0],user_name_df['dataset_visibility'][0]
        logging.debug(f"data ingestion  :  DatasetClass  :  delete_dataset_details  :  Authenticating user {user_name} for the request of [dataset_id = {dataset_id}]'s deletion")
        if user_name == user_name_from_table:    
            #? This condition will be false when called form delete_project_details function,
            #? because that function has already checked that this dataset is used nowhere
            if not skip_check:   
                # ProjectObject = project_creation.ProjectClass() # Get dataset class object

                # project_table_name,_,_ = ProjectObject.make_project_schema()
                project_table_name = 'mlaas.project_tbl'
                sql_command = f"SELECT PROJECT_ID FROM {project_table_name} WHERE original_dataset_id = '{dataset_id}'"
                dataset_ids_df = DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
                
                #? No project table
                if dataset_ids_df is None:
                    id_count = 0
                else:
                    id_count = len(dataset_ids_df)
            else:
                id_count = 0
                
            if id_count == 0: #? Number of projects that use this dataset
                
                #? Getting csv table name
                logging.debug(f"data ingestion  :  DatasetClass  :  delete_dataset_details  :  getting data_table_name for the dataset_id = {dataset_id}")
                sql_command = "SELECT DATASET_TABLE_NAME,dataset_name FROM "+ table_name + " WHERE dataset_id ='"+ dataset_id +"'"
                dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
                
                if len(dataset_df) == 0:
                    return 5,_
                

                row_dataset_status = self.delete_row_dataset(DBObject,connection,dataset_id,dataset_visibility,user_name)

                if row_dataset_status==1:
                    return 6,_

                dataset_table_name = dataset_df['dataset_table_name'][0] 
                #v 1.4
                dataset_name = dataset_df['dataset_name'][0]
                sql_command = f"DELETE FROM {table_name} WHERE dataset_id = '{dataset_id}'"
                
                dataset_status = DBObject.delete_records(connection,sql_command)
                if dataset_status == 1: return 1,_
                
                #? Deleting the CSV Table
                if dataset_visibility == 'public':
                    user_name = 'public'
                
                dataset_table_name = dataset_table_name.lower()
                
                table_name = dataset_table_name
                user_name = user_name.lower()
                
                

                logging.debug(f"data ingestion  :  DatasetClass  :  delete_dataset_details  :  Dataset_tbl entry deleted, Now dropping {user_name}.{dataset_table_name} table")
                data_status = self.delete_data_details(DBObject,connection,table_name,user_name)
                
                logging.info("data ingestion : DatasetClass : delete_dataset_details : execution end")
                
                if dataset_status == 0 and data_status == 0: 
                    return 0,dataset_name
                elif data_status == 1: 
                    return 2,_
                else: 
                    return 1,_
                
            else:
                #? Some project is using this dataset, can't delete it.   
                return 3,_
        else:
            return 4,_
        
    #* Version 1.2
    def delete_data_details(self,DBObject,connection,table_name,user_name):
        """
        This function is used to delete the whole table which was created from 
        user input file.
        
        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            table_name ([string]): [Name of the table that you want to delete.],
            user_name ([string]): [Name of the user.]

        Returns:
            [integer]: [it will return status of the dataset deletion. if successfully then 0 else 1.]
        """
        logging.info("data ingestion : DatasetClass : delete_data_details : execution start")
        logging.info("####>"+str(table_name))
        #? Creating Sql Query
        sql_command = 'DROP TABLE '+ user_name +'."'+table_name+'"'
        logging.info(str(sql_command)+ " delete")
        status = DBObject.delete_records(connection,sql_command)
        logging.debug(f"data ingestion  :  DatasetClass  :  delete_data_details  :  Dropped {user_name}.{table_name} table")
        
        logging.info("data ingestion : DatasetClass : delete_data_details : execution end")
        
        return status

    def dataset_exists(self,DBObject,connection,table_name,dataset_visibility,dataset_name,user_name):
        """This function is used to check existing dataset name.

        Args:
            DBObject ([object]): [object of the database class.],
            connection ([object]): [object of the database connection.],
            table_name ([string]): [name of the table.],
            dataset_name ([string]): [name of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean | integer]: [it will return False if no dataset with same name does not exists,
                                    or else it will return the id of the existing dataset]
        """
        
        logging.info("data ingestion : DatasetClass : dataset_exists : execution start")
        
        #? Checking if the same dataset is there for the same user in the dataset table? If yes, then it will not insert a new row in the table
        try:
            dataset_name=str(dataset_name).replace("'","''")
            #? There can't be 2 public datasets with same name, because that will create ambiguity in Dropdown list
            #? But there can be 2 private datasets with same name, if users are different
            dataset_name=str(dataset_name).replace("'","''")
            if dataset_visibility == 'public':
                #? Is there any(public & private) dataset with same name?
                sql_command = f"SELECT dataset_id FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' and page_name in ('Create dataset','Create Project','schema save')"
                logging.info(str(sql_command) + "check file")
                #! Possible Security Issue: User will get to know that some other user has private dataset with same name
            else:
                #? Is there any public dataset with same name?
                sql_command = f"SELECT dataset_id FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND DATASET_VISIBILITY = 'public' and page_name in ('Create dataset','Create Project','schema save')"
                logging.info(str(sql_command) + "check file")
                data_df=DBObject.select_records(connection,sql_command)
                data=len(data_df)

                if data == 0:
                    #? No public dataset with same name
                    #? Is there any private dataset from you with same name?
                    sql_command = f"SELECT dataset_id FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND USER_NAME = '{user_name}' and page_name in ('Create dataset','Create Project','schema save')"
                    logging.info(str(sql_command) + "check file")
                else:
                    #! There is a public dataset with your name
                    logging.debug(f"data ingestion  :  DatasetClass  :  dataset_exist  :  A public dataset with the same dataset_name exists at dataset_id = {int(data_df['dataset_id'][0])}")
                    return int(data_df['dataset_id'][0])
            data_df=DBObject.select_records(connection,sql_command)
            data=len(data_df)
            
            logging.info("data ingestion : DatasetClass : dataset_exists : execution end")
        
            if data == 0: return False
            else: 
                logging.debug(f"data ingestion  :  DatasetClass  :  dataset_exist  :  A dataset with the same dataset_name = '{dataset_name}' exists ")
                return int(data_df['dataset_id'][0])
            #else: return True
        except:
            return False
        
    def show_dataset_names(self,DBObject,connection,user_name):
        """Show all the existing datasets created by user.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the selected columns from dataset details.]
        """
        logging.info("data ingestion : DatasetClass : show_dataset_names : execution start")
        table_name,_,_ = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        # This command is used to get dataset id and names from dataset table of database.
        logging.debug("data ingestion : DatasetClass : show_dataset_names : this will excute select query on table name : "+ table_name +" based on user name :" + user_name + " and dataset visibility : public" )
        
        sql_command = "SELECT dataset_id,dataset_name FROM "+ table_name + " WHERE USER_NAME ='"+ user_name +"' or dataset_visibility='public'"
        dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        logging.info("data ingestion : DatasetClass : show_dataset_names : execution end")
        return dataset_df

    def delete_row_dataset(self,DBObject,connection,dataset_id,dataset_visibility,user_name):
        """
        function used to delete the raw dataset record from the dataset table.

        Args :
                dataset_id[(Integer)] : [Id of the dataset table]
                dataset_visibility[(String)] : [Name of the visibility(Private, public)]
                user_name[(String)] : [Name of the user]
        Return:
                [Integer] : [return 0 if successfully deleted else return 1 ]
        """
        try:
            # Get table name,schema and columns from dataset class.
            table_name,_,_ = self.make_dataset_schema() 

            #get the  dataset id and table name of the raw dataset
            raw_dataset_id,raw_dataset_table = DBObject.get_raw_dataset_detail(connection,dataset_id)
            
            #sql query to delete raw dataset for given dataset id
            sql_command = f"DELETE FROM {table_name} WHERE dataset_id = '{raw_dataset_id}'"


            #execute the sql query
            dataset_status = DBObject.delete_records(connection,sql_command)

            #? Deleting the CSV Table
            if dataset_visibility == 'public':
                user_name = 'public'

            #delete the raw dataset table 
            raw_dataset_status = self.delete_data_details(DBObject,connection,str(raw_dataset_table),str(user_name))

            return raw_dataset_status
        except Exception as exc:
            return exc
    
    def insert_raw_dataset(self,DBObject,connection,dataset_id,user_name,file_name,dataset_visibility):
        try:
            #get the formated table name of the actual dataset
            original_table_name = self.get_dataset_table_name(file_name)
            
            #get the updated table name for te raw dataset
            raw_table_name = DBObject.get_table_name(connection,original_table_name)
           
            #check the visibility 
            if dataset_visibility=='private':

                sql_command = 'CREATE TABLE '+str(user_name)+'."'+str(raw_table_name)+'" AS SELECT * FROM '+str(user_name)+'."'+str(original_table_name)+'"'
                logging.info(str(sql_command)+ " private")
            else:
                sql_command = 'CREATE TABLE public."'+str(raw_table_name)+'" AS SELECT * FROM public."'+str(original_table_name)+'"'
                logging.info(str(sql_command)+ " public")
            
            #form the new table based on te existing table 
            create_status = DBObject.update_records(connection,sql_command)

            ################
            if create_status == 0:
                if dataset_visibility == 'private':
                    table_name = user_name+'."'+str(raw_table_name)+'"'
                else:
                    table_name = 'public."'+str(raw_table_name)+'"'
                
                sql_command = "SELECT count(*) from "+str(table_name)
                logging.info(str(sql_command) + "  check")
                dataframe = DBObject.select_records(connection,sql_command)
                no_of_rows = int(dataframe['count'][0])
                logging.info("----->"+str(no_of_rows))
            #update the dataset table name of the raw dataset
            sql_command = "UPDATE mlaas.dataset_tbl SET dataset_table_name='"+str(raw_table_name)+"',no_of_rows = '"+str(no_of_rows)+"' where dataset_id ='"+str(dataset_id)+"'"
            create_status = DBObject.update_records(connection,sql_command)
            
            return create_status
        except Exception as exc:
            return exc



