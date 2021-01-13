'''
/*CHANGE HISTORY
--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 
*/
'''
import pandas as pd 
import logging
import json
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')

class SchemaClass:
    
    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.]
            user ([string]): [user of the database.]
            password ([string]): [password of the database.]
            host ([string]): [host ip or name where database is running.]
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number
        
    def get_schema(self):
        # Project table name
        table_name = 'mlaas.schema_tbl'
        # Columns for project table
        cols = 'dataset_id,column_name,changed_column_name,data_type,changed_data_type,column_attribute' 
        # Schema for project table.
        schema ="dataset_id bigint,"\
                "column_name  text,"\
                "changed_column_name  text,"\
                "data_type  text,"\
                "changed_data_type  text,"\
                "column_attribute  text"
                
        return table_name,cols,schema
    
    def get_dataset_schema(self,dataset_id):
        """
        this function used to get the column name and datatype of the table

        Args :
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
                [List] : [return the list of dictonery]
        """
        DBObject = db.DBClass() # create object for database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        sql_command = "SELECT dataset_name,dataset_table_name,user_name from mlaas.dataset_tbl Where dataset_id =" + str(dataset_id)
        dataset_df = DBObject.select_records(connection,sql_command)  # execute the sql query and return data if found else return None
        dataset_records = dataset_df.to_records(index=False) # convert dataframe to a NumPy record  
        dataset_name,dataset_table_name,user_name = dataset_records[0]
        dataset_name,dataset_table_name,user_name = str(dataset_name),str(dataset_table_name),str(user_name)

        table_name = dataset_table_name

        #sql query string to get the INFORMATION_SCHEMA for the table and fetch column_name and data type
        sql_command = "SELECT column_name,data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE "
        sql_command += "table_name = '{}' order by ordinal_position;".format( table_name )  
        
        data_details_df = DBObject.select_records(connection,sql_command) #execute the sql query
        column_name = data_details_df["column_name"].tolist() # covert the dataframe into list
        column_data_type = data_details_df["data_type"].tolist() # covert the dataframe into list
        
        schema_data = get_schema_format(column_name,column_data_type) #call get_schema_format to get json format data
        return schema_data
    
    def map_dataset_schema(self,DBObject,connection,user_name,dataset_id,column_name_list,column_lst,data_type_lst,column_attribute_lst,column_change_datatype):
        prev_cols_lst = []
        prev_dtype_lst = []
        
        new_cols_lst = column_lst
        new_dtype_lst = column_change_datatype
        cols_attribute_lst = column_attribute_lst

        table_name,cols,schema =self.get_schema()
        # table_name = user_name +"."+table_name
        prev_cols_lst = column_name_list
        prev_dtype_lst = data_type_lst
        
        if self.is_existing_schema(DBObject,connection,dataset_id,user_name):
            for prev_col,new_col,prev_dtype,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,new_dtype_lst,cols_attribute_lst): 
                sql_command = "update "+table_name + " SET changed_column_name = '" + new_col + "',"\
                                                           "changed_data_type = '" + new_dtype + "',"\
                                                            "column_attribute = '" + col_attr +"'"\
                              " Where column_name ='"+ prev_col +"' and data_type = '"+ prev_dtype +"'"
                logger.info("Sql_command : "+ sql_command)
                status = DBObject.update_records(connection,sql_command)
                
        else:
            for prev_col,new_col,prev_dtype,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,new_dtype_lst,cols_attribute_lst): 
                row = dataset_id,prev_col,new_col,prev_dtype,new_dtype,col_attr
                row_tuples = [tuple(row)] # Make record for project table
                status = DBObject.insert_records(connection,table_name,row_tuples,cols)
            
        return status
    
    def update_dataset_schema(self,column_name_list,column_lst,data_type_lst,column_attribute_lst,column_change_datatype,dataset_id,user_name): ###

        DBObject = db.DBClass()
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        # schema_status = DBObject.create_schema(connection,user_name)
        table_name,col,schema = self.get_schema()
        # table_name = str(user_name)+"."+str(table_name)
        create_status = DBObject.create_table(connection,table_name,schema)
        mapping_status =self.map_dataset_schema(DBObject,connection,user_name,dataset_id,column_name_list,column_lst,data_type_lst,column_attribute_lst,column_change_datatype) ###
        return mapping_status
    
    def is_existing_schema(self,DBObject,connection,dataset_id,user_name):
        """
        this function checks schema table already exist
        """
        table_name,*_ = self.get_schema()
        sql_command = "select dataset_id from "+ table_name +" where dataset_id="+dataset_id
        data=DBObject.select_records(connection,sql_command)
        if data is None:
            return False
        # data=int(data.shape[0])
        if len(data) > 0 :
            return True
        else:
            return False
        
        
       