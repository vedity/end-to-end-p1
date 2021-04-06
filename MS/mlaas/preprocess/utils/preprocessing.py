'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Exceptions
from common.utils import dynamic_dag
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils.activity_timeline import activity_timeline

#* Common utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

#* Class Imports
from ingest.utils.dataset import dataset_creation
from .Exploration import dataset_exploration as de
from .schema import schema_creation as sc
from .cleaning import noise_reduction as nr
from .cleaning import cleaning
from .Transformation import transformation as trs
from .Transformation import split_data 
from .Transformation.model_type_identifier import ModelType

#* Library Imports
import os
import logging
import traceback
import numpy as np
import pandas as pd
import uuid
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import requests
import uuid
import json
import time
import datetime


user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('preprocessing')

#* Object Definition
dc = dataset_creation.DatasetClass()
sp = split_data.Split_Data()
le = LabelEncoder()
class PreprocessingClass(sc.SchemaClass, de.ExploreClass, cleaning.CleaningClass, trs.TransformationClass):
    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.],
            user ([string]): [user of the database.],
            password ([string]): [password of the database.],
            host ([string]): [host ip or name where database is running.],
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number
        self.AT = activity_timeline.ActivityTimelineClass(database, user, password, host, port)
        self.op_diff = 8 #difference between database_operation ids & universal operation ids
        
    def get_db_connection(self):
        """This function is used to initialize database connection.
        
        Returns:
            [object,string]: [it will return database object as well as connection string.]
        """
        logging.info("data preprocessing : PreprocessingClass : get_db_connection : execution start")
        DBObject = db.DBClass() # Get database object from database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port) # Initialize connection with database and get connection string , connection object.
        
        logging.info("data preprocessing : PreprocessingClass : get_db_connection : execution end")
        return DBObject,connection,connection_string
    
    def get_data_df(self, dataset_id, schema_id = None):
        '''
            Returns pandas DataFrame containing data of given dataset_id for given schema_id.  
            If schema_id is None then it returns raw table without schema changes. 
            
            Args:
                dataset_id(Intiger): id of the dataset.
                schema_id(Intiger) [default None]: id of the dataset in the schema table.
                
            Returns:
                data_df(pandas.DataFrame): Dataframe containing the data.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : get_data_df : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            data_df = DBObject.get_dataset_df(connection, dataset_id, schema_id)
            if isinstance(data_df, str):
                raise EntryNotFound(500)
            
            logging.info("data preprocessing : PreprocessingClass : get_data_df : execution stop")
            
            return data_df
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_data_df : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_data_df : " +traceback.format_exc())
            return exc.msg
        
    def get_exploration_data(self,dataset_id,schema_id):
        """
            This class returns all the statistics for the given dataset.
            
            Args:
                dataset_id ([intiger]): [id of the dataset.]
            
            Returns:
                stats_df ([pandas.Dataframe]): [Dataframe containing all the statistics.]
        """
        try:
            logging.info("data preprocessing : PreprocessingClass : get_exploration_data : execution start")
            
            data_df = self.get_data_df(dataset_id, schema_id)
            logging.error(str(data_df) + "  chaclking")
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            stats_df = super(PreprocessingClass,self).get_dataset_statistics(data_df)
            if isinstance(stats_df, int):
                if stats_df == 1:
                    raise EntryNotFound(500)
                elif stats_df == 2:
                    raise StatisticsError(500)
            
        except (Exception,EntryNotFound,StatisticsError,GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_exploration_data : Exception " + str(exc))
            logging.error("data preprocessing : PreprocessingClass : get_exploration_data : " +traceback.format_exc())
            return str(exc)
            
        logging.info("data preprocessing : PreprocessingClass : get_exploration_data : execution end")
        return stats_df
    
    def save_schema_data(self,schema_data,project_id,dataset_id,schema_id,user_name):
        try:
            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")

            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            status = super(PreprocessingClass,self).save_schema(DBObject,connection,schema_data,project_id,dataset_id,schema_id,user_name)

            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")
            return status
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : " +traceback.format_exc())
            return exc.msg

    def get_schema_details(self,schema_id):
        try:
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution start")
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            status = super(PreprocessingClass,self).get_schema_data(DBObject,connection,schema_id)
            
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution stop")
            return status
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : " +traceback.format_exc())
            return exc.msg
        
    def get_col_names(self, schema_id, json = False,original = False):
        '''
            It is used to get the column names.
            
            Args:
                schema_id (Intiger): schema id of the associated dataset.
                json (Boolean) (default: False): Returns json dict if True else returns List of Column Names. 
                
            Returns:
                column_names(List of Strings): List of Name of the columns.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : get_col_names : execution start")
        
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            if not original:
                sql_command = f"select case when changed_column_name = '' then column_name else changed_column_name end column_list,case when 'True' in( missing_flag, noise_flag) then 'True' else 'False' end flag from mlaas.schema_tbl where schema_id ='{str(schema_id)}' and column_attribute !='Ignore' order by index"
            else:
                sql_command = f"select column_name as column_list,case when 'True' in( missing_flag, noise_flag) then 'True' else 'False' end flag from mlaas.schema_tbl where schema_id ='{str(schema_id)}' and column_attribute !='Ignore' order by index"
                logging.info(str(sql_command) + " command ")
            col_df = DBObject.select_records(connection,sql_command) 
            
            if col_df is None:
                raise EntryNotFound(500)
            
            column_name,flag_value = list(col_df['column_list']),list(col_df['flag'])
            
            
            
            #? Returning column names if user doesn't want json
            if not json:
                logging.info("data preprocessing : PreprocessingClass : get_col_names : execution stop")
                return column_name
            
            #? For FrontEnd 
            json_data = [{"column_id": count, "col_name": column_name[count],"is_missing":flag_value[count]} for count in range(1,len(column_name))]
            
            logging.info("data preprocessing : PreprocessingClass : get_col_names : execution stop")
            
            return json_data
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_col_names : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_col_names : " +traceback.format_exc())
            return exc.msg
        
        
    def get_all_operations(self):
        '''
            This function returns all operations. It is used by the data cleanup as master api responce when the data_cleanup page is called.
            
            Args:
                None
                
            Returns:
                all_operations[List]: List of dictionaries containing all operations.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : get_all_operations : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
                
            sql_command = f"select amt.activity_id,amt.activity_name,amt.user_input,amt.check_type,pat.parent_activity_name,ptt.tab_name from mlaas.activity_master_tbl amt , mlaas.parent_activity_tbl pat, mlaas.preprocess_tab_tbl ptt where amt.code = '0' and amt.parent_activity_id = pat.parent_activity_id and ptt.tab_id = pat.tab_id order by amt.activity_id"
            operations_df = DBObject.select_records(connection,sql_command) 
            
            if operations_df is None:
                raise TableNotFound(500)
            
            #? Logical Function Starts
            try:
                #? To store dictionaries
                master_response = []

                #? For ids
                k = 1
                for tabs in operations_df.groupby('tab_name'):
                    
                    #? To store operation classes which will be shown in the tab
                    tab_dict = {}
                    
                    #? To store operation classes
                    operation_classes = []
                    i = 1
                    for dfs in tabs[1].groupby('parent_activity_name'):
                        
                        #? To store each individual operations
                        operation_class_dict = {}
                        handlers = []
                        
                        #? Storing each individual operations
                        j = 1
                        for index,data in dfs[1].iterrows():
                            operation_dict = {}
                            operation_dict['id'] = j
                            operation_dict['name'] = data['activity_name']
                            operation_dict['operation_id'] = data['activity_id']
                            operation_dict['user_input'] = data['user_input']
                            operation_dict['check_type'] = data['check_type']
                            handlers.append(operation_dict)
                            j += 1
                        
                        #? Adding the operations to the class
                        operation_class_dict['id'] = i
                        operation_class_dict['title'] = dfs[0]
                        operation_class_dict['operations'] = handlers
                        operation_classes.append(operation_class_dict)
                        i+=1
                        
                    #? Adding classes to the tab
                    tab_dict['tab_id'] = k
                    tab_dict['tab_name'] = tabs[0]
                    tab_dict['operation_classes'] = operation_classes
                    master_response.append(tab_dict)
                    k += 1
    
                logging.info("data preprocessing : PreprocessingClass : get_all_operations : execution stop")
                return master_response
            
            except Exception as exc:
                logging.info(f"data preprocessing : PreprocessingClass : get_all_operations : Function failed : {str(exc)}")
                return exc
            
        except (DatabaseConnectionFailed,TableNotFound) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : " +traceback.format_exc())
            return exc.msg
            
        
    def get_preprocess_cache(self, dataset_id):
        '''
            This function is used to return Missing value & Noise status for all the columns.
            This will be stored in the schema_tbl.
            
            Args:
                dataset_id(Intiger): id of the dataset.
                
            Returns:
                missing_value_status(List of Booleans): List containing missing value statuses for all the columns.
                noise_status(List of Booleans): List containing noise statuses for all the columns.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_preprocess_cache : execution start")
            
            data_df = self.get_data_df(dataset_id)
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            #? Getting DB object & connection object
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            #? Getting Table Name
            table_name = DBObject.get_active_table_name(connection, dataset_id)
            
            missing_value_status = []
            noise_status = []
            for col in data_df.columns:
                series = data_df[col]
                
                #? Checking if there are missing values in the column
                # is_missing_value = series.isnull().any()
                # missing_value_status.append(is_missing_value)
                missing_value_status.append(self.detect_missing_values(DBObject, connection, table_name, col))
                
                #? Checking if there is noise in the column
                noise = self.dtct_noise(DBObject, connection, col, table_name= table_name)
                if noise == 1:
                    noise = True
                else: noise = False
                noise_status.append(noise)
            
            logging.info("data preprocessing : PreprocessingClass : get_preprocess_cache : execution stop")
            return missing_value_status,noise_status
            
        except (DatabaseConnectionFailed,EntryNotFound,GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_preprocess_cache : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_preprocess_cache : " +traceback.format_exc())
            return exc.msg
        
    def retrive_preprocess_cache(self, DBObject, connection, schema_id):
        '''
            This function is used to retrive preprocess cache from the schema table.
            
            Args:
                DBObject(Object): Instance of DB Class. 
                schema_id(Intiger): Schema_id of the table.
                connection(Object): Postgres connection object.
                
            Returns:
                data_types(List of Strings): Predicted Datatypes of every column.
                missing_value_status(List of booleans): State of missing values for each columns. 
                noise_status(List of booleans): State of noise for each columns. 
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : retrive_preprocess_cache : execution start")
            
            sql_command = f'''
                select 
                    st.data_type, st.missing_flag, st.noise_flag 
                from 
                    mlaas.schema_tbl st 
                where
                    st.schema_id = '{schema_id}' 
                and
                    st.column_attribute <> 'Ignore'
                order by 
                    st."index" asc ;
            '''
            cache_df = DBObject.select_records(connection,sql_command) 
            
            data_types, missing_status, noise_status = cache_df['data_type'],cache_df['missing_flag'],cache_df['noise_flag']
            
            logging.info("data preprocessing : PreprocessingClass : retrive_preprocess_cache : execution stop")
            return data_types.tolist(),missing_status.tolist(), noise_status.tolist()
            
        except Exception as exc:
            logging.info(f"data preprocessing : PreprocessingClass : retrive_preprocess_cache : function failed : {str(exc)}")
            return str(exc)
            
    def get_possible_operations(self, dataset_id, schema_id, column_ids):
        '''
            This function returns all possible operations for given columns.
            
            Args:
                dataset_id(int): Id of the dataset.
                schema_id(int): Id of the dataset's schema.
                column_ids(list of intigers): Selected columns.
                
            Returns:
                operations[List]: List of possible operations.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_possible_operations : execution start")
            
            #? Getting Dataframe
            data_df = self.get_data_df(dataset_id,schema_id)
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            #? Getting DB object & connection object
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            #? Getting Table Name
            table_name = DBObject.get_active_table_name(connection, dataset_id)
            
            num_cols = data_df._get_numeric_data().columns.tolist()
            
            predicted_datatypes = self.get_attrbt_datatype(data_df,data_df.columns,len(data_df))
            
            old_col_list = self.get_col_names(schema_id,json = False,original = True)
            
            #? Logical function starts
            try:
                #? Logical function starts
                all_col_operations = []
                
                for id in column_ids:
                    prev_col_name = old_col_list[id]
                    col = data_df.columns[id]
                    
                    series = data_df[col]
                    operations = []

                    #? Column is both numerical & categorical
                    if (col in num_cols) and (predicted_datatypes[id].startswith('Ca')):
                        col_type = 0
                    #? Column is Numerical
                    elif col in num_cols:
                        col_type = 1
                    #? Column is categorical
                    elif predicted_datatypes[id].startswith('Ca'):
                        col_type = 2
                    else:
                        col_type = 3

                    missing_values = self.detect_missing_values(DBObject, connection, table_name, prev_col_name)
                    noise_status = self.dtct_noise(DBObject, connection, prev_col_name, table_name= table_name)
                    if noise_status == 1:
                        noise_status = True
                    else: noise_status = False
                    
                    if missing_values:
                        #? Adding Missing Value Operations
                        if col_type == 0:
                            operations += [1,6,7,8,9,10,11,13]
                        elif col_type == 1:
                            operations += [1,6,7,8,9,10,13]
                        elif col_type == 2 or col_type == 3:
                            operations += [1,11,12]
                    
                    if noise_status:
                        operations += [2,5,14,15,16,17,18,19]
                    
                    #? Outlier Removal & Scaling Operations for numeric; Encoding ops for Categorical
                    if not missing_values and not noise_status:
                        if col_type == 0 or col_type == 1:
                            operations += [3,4,20,21,22,23,24,25,26]
                        if col_type == 2 or col_type == 3:
                            operations += [27,28]
                        if col_type == 0:
                            operations += [28]
                        
                    #? Math operations
                    if not noise_status:
                        if col_type == 0 or col_type == 1:
                            operations += [29,30,31,32]
                            
                    all_col_operations.append(operations)
                
                #? Getting Final Common Operation List
                final_op_list = []
                for ops in all_col_operations:
                    for op in ops:
                        flag = True
                        for other_ops in all_col_operations:
                            if op not in other_ops:
                                flag = False
                                break
                        if flag == True:
                            final_op_list.append(op)
                final_op_list = list(set(final_op_list))
                final_op_list.sort()
                
                logging.info("data preprocessing : PreprocessingClass : get_possible_operations : execution End")
                
                return [i+self.op_diff for i in final_op_list]    
            
            except Exception as exc:
                logging.info(f"data preprocessing : PreprocessingClass : get_possible_operations : Function failed : {str(exc)}")
                return exc
                
        except (DatabaseConnectionFailed,EntryNotFound,GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
            return exc.msg
        
    def reorder_operations(self, data):
        '''
            This function accepts list of operations & list of values sent by front end &
            returns a optimized reordered dictionary of operations & values.
            
            Input data format:
            ------------------
            [
                {
                    'column_id': [1],
                    'selected_handling': [44,9,33],
                    'values': [15,'','']
                },
                {
                    'column_id': [2],
                    'selected_handling': [25,44],
                    'values': ['',300]
                },
                {
                    'column_id': [3],
                    'selected_handling': [34,23,15],
                    'values': ['','','']
                }
            ]
            
            Output dictionaries:
            ------------------
            - First Dictionary has operations as keys & columns as values.
            - Second dictionary has operations as keys and user inputs as values.  
            
            {
                1: [1], 
                7: [3], 
                15: [3], 
                17: [2], 
                25: [1], 
                26: [3], 
                36: [1, 2]
            },
            {
                1: [''], 
                7: [''], 
                15: [''], 
                17: [''], 
                25: [''], 
                26: [''], 
                36: [15, 300]
            }
            
            Args:
            -----
            data[List of Dictionaries]: Data sent by frontend.
            
            Returns:
            --------
            operation_dict [`Dictionary`]: Operation Order optimized dictionary;
            -   operation_dict = {
                    operation: [column(s)]
                }
                
            value_dict [`Dictionary`]: Dictionary containing user inputs.
            -   value_dict = {
                    operation: [user_input(s)]
                }

        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : reorder_operations : execution start")
            
            #? Getting operations in a cleaned format
            operation_dict = {}
            for dic in data:
                for op in dic['selected_handling']:
                    operation_dict[op-self.op_diff] = operation_dict.get(op-self.op_diff,[]) + dic['column_id']
            
            #? Getting Values in a cleaned formate
            value_dict = {}
            for dic in data:
                for i,op in enumerate(dic['selected_handling']):
                    value_dict[op-self.op_diff] = value_dict.get(op-self.op_diff,[]) + [dic['values'][i]]
            
            #? Sorting both dictionaries
            operation_dict = {k: v for k, v in sorted(operation_dict.items(), key=lambda item: item[0])}
            value_dict = {k: v for k, v in sorted(value_dict.items(), key=lambda item: item[0])}
            
            logging.info(f"data preprocessing : PreprocessingClass : reorder_operations : Operation_dict : {operation_dict}")
            logging.info(f"data preprocessing : PreprocessingClass : reorder_operations : Values_dict : {value_dict}")
            logging.info("data preprocessing : PreprocessingClass : reorder_operations : execution end")
            
            return operation_dict,value_dict

        except Exception as exc:
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc))
            return OperationOrderingFailed(500).msg
        
        
    # def master_executor(self, project_id,dataset_id, schema_id,request, flag ,selected_visibility,dataset_name ,dataset_desc):
    #     '''
    #         It takes the request from the frontend and executes the cleanup operations.
            
    #         Args:
    #         -----
    #         dataset_id (`Intiger`): Id of the dataset.
    #         schema_id (`Intiger`): Id of the dataset in the schema_tbl.
    #         request (`Dict`): Request coming from the frontend.
    #         save_as (`Boolean`) (default = `False`): Has the user chosen save_as option?
            
    #         Returns:
    #         --------
    #         Positive or Negative responce.
    #     '''
        
    #     try:
    #         logging.info("data preprocessing : PreprocessingClass : master_executor : execution start" + str(type(flag))+ str(flag))
    #         DBObject,connection,connection_string = self.get_db_connection()
    #         if connection == None :
    #             raise DatabaseConnectionFailed(500)
    #         #? Getting Dataframe
            
    #         #Get the dataframe of dataset detail based on the dataset id
    #         dataframe = DBObject.get_dataset_detail(DBObject,connection,dataset_id)

    #         #Extract the dataframe based on its column name as key
    #         table_name,dataset_visibility,user_name = str(dataframe['dataset_table_name'][0]),str(dataframe['dataset_visibility'][0]),str(dataframe['user_name'][0])
            
    #         if dataset_visibility == 'private':
    #             dataset_table_name = user_name+'."'+table_name+'"'
    #         else:
    #             dataset_table_name = 'public'+'."'+table_name+'"'

    #         #get the Column list
    #         column_list = DBObject.get_column_names( connection, table_name)
    #         # column_list = self.get_col_names(schema_id)
    #         logging.info(str(column_list) + " column_list")

    #         #? Getting operations in the ordered format
    #         op_dict, val_dict = self.reorder_operations(request)
            
    #         operations = op_dict.keys()
    #         for op in operations:
    #             status = 1
                
    #             #? Getting Columns
    #             col = op_dict[op]
    #             temp_cols = [str(column_list[i]) for i in col]
    #             # temp_col = str(temp_col)
    #             # temp_col = temp_col[1:-1]
    #             # temp_col = temp_col.replace('"',"'")
                
    #             #? Getting Values
    #             value = val_dict[op]
                
    #             #? Making Entry in the Activity Table
    #             activity_ids = []
    #             for temp_col_names in temp_cols:
    #                 activity_ids.append(self.operation_start(DBObject, connection, op, user_name, project_id, dataset_id, temp_col_names))
                
    #             col_names = [column_list[i] for i in col]
    #             try:
    #                 if op == 1:
    #                     status = self.discard_missing_values(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 2:
    #                     status = self.discard_noise(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 3:
    #                     status = self.delete_above(DBObject,connection,column_list, dataset_table_name, col, value)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 4:
    #                     status = self.delete_below(DBObject,connection,column_list, dataset_table_name, col, value)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 5:
    #                     status = self.remove_noise(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name, "True")
                        
    #                 elif op == 6:
    #                     status = self.mean_imputation(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 7:
    #                     status = self.median_imputation(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 8:
    #                     status = self.mode_imputation(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 9:
                        
    #                     #? Reusing the missing category imputation function for the arbitrary value imputation
    #                     status = self.missing_category_imputation(DBObject,connection,column_list, dataset_table_name,col, value,flag = True)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 10:
    #                     status = self.end_of_distribution(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 11:
    #                     status = self.frequent_category_imputation(DBObject,connection,column_list, dataset_table_name, col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 12:
    #                     status = self.missing_category_imputation(DBObject,connection,column_list, dataset_table_name, col,value)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 13:
    #                     status = self.random_sample_imputation(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 14:
    #                     status = self.repl_noise_mean(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 15:
    #                     status = self.repl_noise_median(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 16:
    #                     status = self.repl_noise_mode(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 17:
    #                     status = self.repl_noise_eod(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 18:
    #                     status = self.repl_noise_random_sample(DBObject,connection,column_list, dataset_table_name,col)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 19:
    #                     status = self.repl_noise_arbitrary_val(DBObject,connection,column_list, dataset_table_name,col, value)
    #                     if status == 0:
    #                         for col_name in col_names:
    #                             sts = self.update_schema_tbl_missing_flag(DBObject,connection, schema_id, col_name)
    #                             sts = self.update_schema_tbl_noise_flag(DBObject,connection, schema_id, col_name)
                        
    #                 elif op == 20:
    #                     status = self.rem_outliers_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 21:
    #                     status = self.rem_outliers_z_score(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 22:
    #                     status = self.repl_outliers_mean_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 23:
    #                     status = self.repl_outliers_mean_z_score(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 24:
    #                     status = self.repl_outliers_med_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 25:
    #                     status = self.repl_outliers_med_z_score(DBObject,connection,column_list, dataset_table_name,col)
                        
    #                 elif op == 26:
    #                     status = self.apply_log_transformation(DBObject,connection,column_list, dataset_table_name, col)
                        
    #                 elif op == 27:
    #                     status = self.label_encoding(DBObject,connection,column_list, dataset_table_name, col)
                        
    #                 elif op == 28:
    #                     status = self.one_hot_encoding(DBObject,connection,column_list, dataset_table_name, col, schema_id)
                        
    #                 elif op == 29:
    #                     status = self.add_to_column(DBObject,connection,column_list, dataset_table_name, col, value)
                        
    #                 elif op == 30:
    #                     status = self.subtract_from_column(DBObject,connection,column_list, dataset_table_name, col, value)
                        
    #                 elif op == 31:
    #                     status = self.divide_column(DBObject,connection,column_list, dataset_table_name, col, value)
                        
    #                 elif op == 32:
    #                     status = self.multiply_column(DBObject,connection,column_list, dataset_table_name, col, value)
                        
    #                 if status != 0:
    #                     #? Sql function Failed
    #                     raise SavingFailed(500)
                        
    #                     #? Saving the dataframe into the database
    #                     # data_df.drop(data_df.columns[0],axis=1, inplace = True)

    #                     # updated_table_name = DBObject.get_table_name(connection,table_name)
                        
    #                     # if dataset_visibility == 'public':
    #                     #     user_name='public'
            
    #                     # status = DBObject.load_df_into_db(connection_string,updated_table_name,data_df,user_name)
        
    #                     # sql_command = "update mlaas.dataset_tbl set dataset_table_name='"+str(updated_table_name)+"' where dataset_id='"+str(dataset_id)+"'"
    #                     # logging.info(str(sql_command))
    #                     # update_status = DBObject.update_records(connection,sql_command)
    #                     # status = update_status
    #                     # if status == 1:
    #                     #     raise SavingFailed(500)
    #                     # else:
    #                     #     sql_command = f"drop table {dataset_table_name}"
    #                     #     update_status = DBObject.update_records(connection,sql_command)
    #                     #     status = update_status
    #                     #     activity_status = self.operation_end(DBObject, connection, activity_id, op, temp_col)
    #                 else:

    #                     #Update all the status flag's based on the schema id
    #                     status = self.update_schema_flag_status(DBObject,connection,schema_id,dataset_id,column_list)
                        
    #                     if status ==0:  
    #                         #? Updating the Activity table
    #                         for i,temp_col_names in enumerate(temp_cols):
    #                             activity_status = self.operation_end(DBObject, connection, activity_ids[i], op, temp_col_names)

    #                         if flag == 'True':
    #                             logging.info(" call <>")
    #                             save_as_status = self.SaveAs(DBObject,connection,project_id,table_name,user_name,dataset_visibility,dataset_name,selected_visibility,dataset_desc)
    #                             return save_as_status
    #                     else:
                            
    #                         return status
    #             except Exception as exc :
    #                 continue
                    
    #         logging.info("data preprocessing : PreprocessingClass : master_executor : execution stop")
    #         return status

    #     except (DatabaseConnectionFailed,GetDataDfFailed,SavingFailed) as exc:
    #         logging.error(str(exc) +" Error")
    #         logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
    #         logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
    #         return exc.msg
            
    def handover(self, dataset_id, schema_id, project_id, user_name,split_parameters,scaling_type = 0):
        """[This function is used to scaled data and store numpy file into the scaled dataset folder.]

        Args:
            dataset_id ([type]): [to get the dataframe for scaling and split]
            schema_id ([type]): [to get column name]
            project_id ([type]): [to update the entry in project_tble]
            user_name ([type]): [to update the entry in project_tble]
            split_parameters ([type]): [for spliling]
            scaling_type (int, optional): [get scaling type]. Defaults to 0.

        Raises:
            DatabaseConnectionFailed: [description]
            GetDataDfFailed: [description]
            ProjectUpdateFailed: [description]

        Returns:
            status (`Intiger`): Status of the upload.
        """
        '''
            This function is used to scaled data and store numpy file into the scaled dataset folder.
            
            Args:
            -----
            data_df (`pandas.DataFrame`) = whole dataframe.
            scaling_type (`Intiger`) (default = `0`): Type of the rescaling operation.
                - 0 : Standard Scaling
                - 1 : Min-max Scaling
                - 2 : Robust Scaling
                - 3 : Custom Scaling
                
            Returns:
            -------
            status (`Intiger`): Status of the upload.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : handover : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection() #get db connection
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            #? Getting Dataframe
            data_df = self.get_data_df(dataset_id,schema_id) #get dataframe
            
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            tg_cols = DBObject.get_target_col(connection, schema_id) #get list of the target columns
            target_cols = [data_df.columns[0]]
            target_cols += tg_cols           
            target_actual_features_df=data_df[target_cols]
        
            
            if scaling_type == 0:
                data_df.iloc[:,1:] = self.standard_scaling(data_df.iloc[:,1:]) #standard_scaling
            elif scaling_type == 1:
                data_df.iloc[:,1:] = self.min_max_scaling(data_df.iloc[:,1:]) #min_max_scaling
            elif scaling_type == 2:
                data_df.iloc[:,1:] = self.robust_scaling(data_df.iloc[:,1:]) #robust_scaling
             
            feature_cols = list(data_df.columns) #get list of the column
            for col in feature_cols[1:]:
                if data_df[col].dtype == 'O':
                    data_df[col] = le.fit_transform(data_df[col])  
            for col in tg_cols:
                feature_cols.remove(col) #remove target columns from list

            
            # target_cols = [data_df.columns[0]]
            # target_cols += tg_cols #add index column from target columns list
            
            input_features_df = data_df[feature_cols] #input_features_df
            target_features_df=data_df[target_cols] #target_features_df
            mt = ModelType()
            problem_type = mt.get_model_type(target_features_df) #call get_model_type
            model_type = problem_type[0] #model_type
            algorithm_type = problem_type[1] #algorithm type
            target_type = problem_type[2] #target type
            problem_type_dict = '{"model_type": "'+str(model_type)+'","algorithm_type": "'+str(algorithm_type)+'","target_type": "'+str(target_type)+'"}' #create problem type dict
            
            feature_cols = str(feature_cols) #input feature_cols
            target_cols = str(target_cols) #target feature_cols
            feature_cols = feature_cols.replace("'",'"')
            target_cols = target_cols.replace("'",'"')

            #splitting parameters
            split_method =split_parameters['split_method'] #get split_method
            cv = split_parameters['cv'] #get cv
            if len(cv) == 0:
                cv = 0
            random_state = split_parameters['random_state'] #get random_state
            test_ratio = split_parameters['test_ratio'] #get test_size
            valid_ratio = split_parameters['valid_ratio'] #get valid_size
            if len(valid_ratio) == 0:
                valid_ratio= 0
            else:
                valid_ratio=float(valid_ratio)
            unique_id = str(uuid.uuid1().time) #genrate unique_id
            scale_dir = "scaled_dataset/scaled_data_" + unique_id  #genrate directory
            CHECK_FOLDER = os.path.isdir(scale_dir) #check directory already exists or not
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(scale_dir) #create directory
                logger.info("Directory  Created")
            else:
                logger.info("Directory  already exists")
            train_X_filename = scale_dir+"/scaled_train_X_data_" + unique_id #genrate train_X file path
            train_Y_filename = scale_dir+"/scaled_train_Y_data_" + unique_id #genrate train_Y file path
            test_X_filename =  scale_dir+"/scaled_test_X_data_" + unique_id  #genrate test_X file path  
            test_Y_filename =  scale_dir+"/scaled_test_Y_data_" + unique_id  #genrate test_Y file path     
            valid_X_filename = "None"
            valid_Y_filename = "None"
            Y_valid_count= None
            X_train, X_valid, X_test, Y_train, Y_valid, Y_test=sp.get_split_data(input_features_df,target_features_df, int(random_state),float(test_ratio), valid_ratio, str(split_method))
            if split_method != 'cross_validation':
                Y_valid_count= Y_valid.shape[0]
                valid_X_filename = scale_dir+"/scaled_valid_X_data_" + unique_id #genrate valid_X file path     
                valid_Y_filename = scale_dir+"/scaled_valid_Y_data_" + unique_id #genrate valid_Y file path     
                np.save(valid_X_filename,X_valid.to_numpy()) #save X_valid
                np.save(valid_Y_filename,Y_valid.to_numpy()) #save Y_valid   
            Y_train_count=Y_train.shape[0] #train count
            Y_test_count =Y_test.shape[0]  #test count
            actual_Y_filename =  scale_dir+"/Unscaled_actual_Y_data_" + unique_id  #genrate test_Y file path           
            np.save(train_X_filename,X_train.to_numpy()) #save X_train
            np.save(train_Y_filename,Y_train.to_numpy()) #save Y_train
            np.save(test_X_filename,X_test.to_numpy()) #save X_test
            np.save(test_Y_filename,Y_test.to_numpy()) #save Y_test
            np.save(actual_Y_filename,target_actual_features_df.to_numpy()) #save Y_actual
        
            scaled_split_parameters = '{"split_method":"'+str(split_method)+'" ,"cv":'+ str(cv)+',"valid_ratio":'+ str(valid_ratio)+', "test_ratio":'+ str(test_ratio)+',"random_state":'+ str(random_state)+',"valid_size":'+str(Y_valid_count)+',"train_size":'+str(Y_train_count)+',"test_size":'+str(Y_test_count)+',"train_X_filename":"'+train_X_filename+".npy"+'","train_Y_filename":"'+train_Y_filename+".npy"+'","test_X_filename":"'+test_X_filename+".npy"+'","test_Y_filename":"'+test_Y_filename+".npy"+'","valid_X_filename":"'+valid_X_filename+".npy"+'","valid_Y_filename":"'+valid_Y_filename+".npy"+'","actual_Y_filename":"'+actual_Y_filename+".npy"+'"}' #genrate scaled split parameters
            logger.info("scaled_split_parameters=="+scaled_split_parameters)
            sql_command = f"update mlaas.project_tbl set target_features= '{target_cols}' ,input_features='{feature_cols}',scaled_split_parameters = '{scaled_split_parameters}',problem_type = '{problem_type_dict}' where dataset_id = '{dataset_id}' and project_id = '{project_id}' and user_name= '{user_name}'"
            status = DBObject.update_records(connection, sql_command)
            if status==1:
                raise ProjectUpdateFailed(500)
            return status
            
        except (DatabaseConnectionFailed,GetDataDfFailed,ProjectUpdateFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : handover : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : handover : " +traceback.format_exc())
            return exc.msg
        
    
    def update_schema_tbl_missing_flag(self, DBObject, connection, schema_id, column_name, flag = "False"):
        
        logging.info("data preprocessing : PreprocessingClass : update_schema_tbl_missing_flag : execution start")
        
        index = '"index"'
        sql_command = f"update mlaas.schema_tbl set missing_flag = '{flag}' where {index} in (select {index} from mlaas.schema_tbl st where st.schema_id = '{schema_id}' and (st.changed_column_name = '{column_name}' or st.column_name = '{column_name}'))"
        logging.info("Sql_command : update_schema_tbl_missing_flag : "+str(sql_command))
        
        status = DBObject.update_records(connection,sql_command)
        logging.info("data preprocessing : PreprocessingClass : update_schema_tbl_missing_flag : execution stop")
        
        return status
    
    def update_schema_tbl_noise_flag(self, DBObject, connection, schema_id, column_name, flag = "False"):
        
        logging.info("data preprocessing : PreprocessingClass : update_schema_tbl_noise_flag : execution start")
        
        index = '"index"'
        sql_command = f"update mlaas.schema_tbl set noise_flag = '{flag}' where {index} in (select {index} from mlaas.schema_tbl st where st.schema_id = '{schema_id}' and (st.changed_column_name = '{column_name}' or st.column_name = '{column_name}'))"
        logging.info("Sql_command : update_schema_tbl_noise_flag : "+str(sql_command))
        
        status = DBObject.update_records(connection,sql_command)
        logging.info("data preprocessing : PreprocessingClass : update_schema_tbl_noise_flag : execution stop")
        
        return status
    
    def update_schema_flag_status(self,DBObject,connection,schema_id,dataset_id,column_list, **kwargs):
        try:
            logging.info("data preprocessing : PreprocessingClass : update_schema_flag_status : execution start")
            
            missing_flag,noise_flag = self.get_preprocess_cache(dataset_id)

            
            for noise_flag,missing_flag,col_name in zip(missing_flag,noise_flag,column_list): 

                #sql command for updating change_column_name and column_attribute column  based on index column value
                sql_command = "update mlaas.schema_tbl SET missing_flag = '" + str(missing_flag) + "',"\
                                "noise_flag = '" +str(noise_flag) +"'"\
                                " Where schema_id ='"+str(schema_id)+"' and column_name = '"+str(col_name)+"'"

                logging.info("Sql_command : update_schema_flag_status : "+str(sql_command))
                #execute sql query command
                status = DBObject.update_records(connection,sql_command) 

                if status ==1:
                    raise SchemaUpdateFailed(500)
            
                status = DBObject.update_records(connection,sql_command)
                logging.info("data preprocessing : PreprocessingClass : update_schema_flag_status : execution stop")
            
            return status
        except (SchemaUpdateFailed) as exc:
            return exc.msg

    def get_cleanup_dag_name(self):
        '''
            This Function is used to get the unique cleanup dag name for the project_tbl entry.

            Args:
            -----
            None

            Returns:
            --------
            dag_id (`String`): the Cleanup dag id.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_cleanup_dag_name : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection() #get db connection
            if connection == None :
                raise DatabaseConnectionFailed(500)  

            id = uuid.uuid1().time
            dag_id='Cleanup_dag_'+str(id)

            template = "cleanup_dag.template"
            namespace = "Cleanup_Dags"

            #? Inserting into Dag_Status Table
            col = "dag_id,status"
            row_data = [tuple((dag_id,'0'))]
            table_name = "mlaas.cleanup_dag_status"
            insert_status,_ = DBObject.insert_records(connection,table_name,row_data,col)
            
            master_dict = {'active': 0}
            
            json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
            
            result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

            logging.info("data preprocessing : PreprocessingClass : get_cleanup_dag_name : execution stop")
            
            return dag_id
        
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_cleanup_dag_name : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_cleanup_dag_name : " +traceback.format_exc())
            return exc.msg
            
    
    def dag_executor(self,project_id, dataset_id, schema_id, request, flag ,selected_visibility,dataset_name ,dataset_desc,user_name):
        '''
            This Function is used to trigger the dag at the save time.

            Args:
            -----
            project_id (`Integer`): Id of the project.
            dataset_id (`Integer`): Id of the dataset.
            schema_id (`Integer`): Id of the schema.
            request (`Dictionary`): Request from the frontend.
            flag (`Boolean`): Is it save or save_as?
            selected_visibility (`String`): public or private.
            dataset_name (`String`): Name of the new dataset.
            dataset_desc (`String`): Description for the dataset.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : dag_executor : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)
                
            
            sql_command = f"select pt.cleanup_dag_id from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
            dag_id_df = DBObject.select_records(connection,sql_command) 
            if not isinstance(dag_id_df,pd.DataFrame): return 1
            dag_id = dag_id_df['cleanup_dag_id'][0]
            
            #? Setting the dag as busy
            sql_command = f"update mlaas.cleanup_dag_status set status = (case when status = '1' then '0' else '1' end) where dag_id = '{dag_id}'"
            update_status = DBObject.update_records(connection,sql_command)

            op_dict, val_dict = self.reorder_operations(request)
            
            template = "cleanup_dag.template"
            namespace = "Cleanup_Dags"
            file_name = dag_id + ".py"

            master_dict = {
            'active': 1,
            "operation_dict": op_dict,
            "values_dict": val_dict,
            "schema_id": schema_id,
            "dataset_id": dataset_id,
            "project_id": project_id,
            "save_as": flag,
            "visibility": selected_visibility,
            "dataset_name": dataset_name,
            "dataset_desc": dataset_desc,
            "user_name": user_name
            }
            
            # json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
            # result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

            status = self.dag_updater(master_dict, file_name, namespace)
            if not isinstance(status,int):
                logging.error(f"Dag Updation Failed : Error : {str(status)}")
                raise DagUpdateFailed(500)

            activity_id = 51
            activity_status = self.get_cleanup_startend_desc(DBObject,connection,dataset_id,project_id,activity_id,user_name)

            json_data = {}
            result = requests.post(f"http://airflow:8080/api/experimental/dags/{dag_id}/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
            logging.info("DAG RUN RESULT: "+str(result))
            
            logging.info("data preprocessing : PreprocessingClass : dag_executor : execution stop")
                
            return 0
        
        except (DatabaseConnectionFailed,DagUpdateFailed) as exc:
            
            #? Resetting the dag status, else if will be in running state always
            if update_status == 0:
                sql_command = f"update mlaas.cleanup_dag_status set status = (case when status = '1' then '0' else '1' end) where dag_id = '{dag_id}'"
                update_status = DBObject.update_records(connection,sql_command)

            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
            return exc.msg
        

    def dag_updater(self, dic, file, namespace = '.'):
        '''
            Updates the dag.

            Args:
            -----
            dic (`dictionary`): Python dictionary that you want to place in the file.
            file (`string`): Name of the file.
            namespace (`string`): Name of the folder inside of the dynamic_dags directory.

            Returns:
            --------
            status (`integer | Exception`): `0` if updation was successful else error.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : dag_updater : execution start")
            
            #? Reading the file
            with open(f"dynamic_dags/{namespace}/{file}","r") as ro:
                content = ro.read()
        
            new_dic = str(dic)

            point = content.find("master")
            bracket_start = content.find("{",point) 
            
            def bracket_end_finder(string, length = 0):
                '''
                    A Subfunction to find the ending bracket.
                '''
                
                opening_count = 0
                length -= 1
                flag = False
                
                for i in string:
                    if i == '{':
                        opening_count += 1
                        flag = True
                    elif i == '}':
                        opening_count -= 1
                    length += 1
                        
                    if flag:
                        if opening_count == 0:
                            return length
                else:
                    #? Closing bracket not found
                    return -1    
            
            bracket_end = bracket_end_finder(content[bracket_start:],bracket_start)

            new_str = content[:bracket_start] + new_dic + content[bracket_end + 1:]
        
            #? Writing into the file
            with open(f"dynamic_dags/{namespace}/{file}", 'w') as wo:
                wo.write(new_str)

            logging.info("data preprocessing : PreprocessingClass : dag_updater : execution stop")
            
            return 0

        except Exception as e:
            return e

    def SaveAs(self,DBObject,connection,project_id,table_name,user_name,dataset_visibility,dataset_name,selected_visibility,dataset_desc, **kwargs):
        '''
        Function used to create a new table with updated changes and insert a new record into dataset table and update the dataset_id into the project_tbl
        '''
        try:
            #? Safety measure in case if DAG calls this method with None parameters
            if dataset_name is None:
                return 1

            # Get table name,schema and columns from dataset class.
            tbl_name,schema,cols = dc.make_dataset_schema() 
            file_name = None
            file_size = None
            page_name = 'Cleanup'

            # Make record for dataset table.
            row = dataset_name,file_name,file_size,table_name,selected_visibility,user_name,dataset_desc,page_name 
                                
            # Convert row record into list of tuple.
            row_tuples = [tuple(row)] 

            logging.info("row tuples error"+str(row_tuples))

            # Insert the records into table and return status and dataset_id of the inserted values
            insert_status,dataset_id = DBObject.insert_records(connection,tbl_name,row_tuples,cols,column_name = 'dataset_id')
                                
            if insert_status == 0:
                                    
                table_name = table_name.replace('di_',"").replace('_tbl',"")

                # Create the new table based on the existing table and return status 0 if successfull else 1 
                dataset_insert_status = dc.insert_raw_dataset(DBObject,connection,dataset_id,user_name,table_name,dataset_visibility,selected_visibility)
                                   
                if dataset_insert_status == 0:

                    # Command will update the dataset id  in the project table
                    sql_command = f'update mlaas.project_tbl set dataset_id={str(dataset_id)} where project_id={str(project_id)}'
                                        
                    # Execute the sql query
                    update_status = DBObject.update_records(connection,sql_command)

                    return update_status
                else:
                    return dataset_insert_status

            else:
                return insert_status
        except Exception as exc:
            return str(exc)

    def get_dag_status(self, project_id):
        '''
            Used to get the dag status
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)
            
            #? Getting Dag id
            sql_command = f"select pt.cleanup_dag_id from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
            dag_id_df = DBObject.select_records(connection,sql_command) 
            dag_id = dag_id_df['cleanup_dag_id'][0]

            #? Getting Dag Status
            sql_command = f"select cds.status from mlaas.cleanup_dag_status cds where cds.dag_id = '{dag_id}';"
            status_df = DBObject.select_records(connection,sql_command) 
            status = status_df['status'][0]
            
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")

            if status == '1':
                return True
            else:
                return False
        
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : " +traceback.format_exc())
            return exc.msg
        

    def get_cleanup_startend_desc(self,DBObject,connection,dataset_id,project_id,activity_id,user_name):
        """This function will replace * into project name and get activity description of scale and split.
 
        Args:
        project_name[String]: get project name
        activity_id[Integer]: get activity id
 
        Returns:
            [String]: activity_description
        """
        activity_df = self.AT.get_activity(activity_id,"US")
        datasetnm_df = DBObject.get_dataset_detail(DBObject,connection,dataset_id)
        projectnm_df = DBObject.get_project_detail(DBObject,connection,project_id)
        dataset_name = datasetnm_df['dataset_name'][0]
        project_name = projectnm_df['project_name'][0]

        sql_command = f"select amt.activity_description as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
        desc_df = DBObject.select_records(connection,sql_command)
        activity_description = desc_df['description'][0]
        activity_description = activity_description.replace('*',dataset_name)
        activity_description = activity_description.replace('&',project_name)
    
        end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        activity_status,index = self.AT.insert_user_activity(activity_id,user_name,project_id,dataset_id,activity_description,end_time)

        return activity_status
