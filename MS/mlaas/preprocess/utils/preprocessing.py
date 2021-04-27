'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Exceptions
from MS.mlaas.common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import ScalingFailed
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

#* Common utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.activity_timeline import activity_timeline
from common.utils.activity_timeline import activity_timeline
from common.utils import dynamic_dag

#* Class Imports
from ingest.utils.dataset import dataset_creation
from .Exploration import dataset_exploration as de
from .schema import schema_creation as sc
from .cleaning import noise_reduction as nr
from .cleaning import cleaning
from .Transformation import transformation as trs
from .Transformation import split_data 
from .Transformation.model_type_identifier import ModelType
from database import *

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

#* Defining Logger
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
    
    def get_data_df(self, DBObject, connection ,dataset_id, schema_id = None):
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
            
            data_df = DBObject.get_dataset_df(connection, dataset_id, schema_id)
            
            if isinstance(data_df, str):
                raise EntryNotFound(500)
            # connection.close()
            logging.info("data preprocessing : PreprocessingClass : get_data_df : execution stop")
            
            return data_df
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_data_df : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_data_df : " +traceback.format_exc())
            return exc.msg
        
    def get_exploration_data(self,DBObject, connection ,dataset_id,schema_id):
        """
            This class returns all the statistics for the given dataset.
            
            Args:
                dataset_id ([intiger]): [id of the dataset.]
            
            Returns:
                stats_df ([pandas.Dataframe]): [Dataframe containing all the statistics.]
        """
        try:
            logging.info("data preprocessing : PreprocessingClass : get_exploration_data : execution start")
            
            data_df = self.get_data_df(DBObject, connection ,dataset_id, schema_id)
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
    
    def save_schema_data(self,DBObject,connection,schema_data,project_id,dataset_id,schema_id,user_name):
        try:
            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")

            status = super(PreprocessingClass,self).save_schema(DBObject,connection,schema_data,project_id,dataset_id,schema_id,user_name)
            # connection.close()
            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")
            return status
        except Exception as exc:
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : Exception " + str(exc))
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : " +traceback.format_exc())
            return str(exc)

    def get_schema_details(self,DBObject,connection,schema_id):
        try:
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution start")

            status = super(PreprocessingClass,self).get_schema_data(DBObject,connection,schema_id)
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution stop")
            return status
        except (Exception) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : Exception " + str(exc))
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : " +traceback.format_exc())
            return exc
        
    def get_col_names(self, DBObject, connection ,schema_id, json = False,original = False):
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
            # connection.close()
            return json_data
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_col_names : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_col_names : " +traceback.format_exc())
            return exc.msg
        
        
    def get_all_operations(self, DBObject, connection):
        '''
            This function returns all operations. It is used by the data cleanup as master api responce when the data_cleanup page is called.
            
            Args:
                None
                
            Returns:
                all_operations[List]: List of dictionaries containing all operations.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : get_all_operations : execution start")
            
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
                            operation_dict['operation_id'] = int(data['activity_id'][3:]) #? Converting String operation_id to integer operation_id
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
                # connection.close()
                logging.info("data preprocessing : PreprocessingClass : get_all_operations : execution stop")
                return master_response
            
            except Exception as exc:
                # connection.close()
                logging.info(f"data preprocessing : PreprocessingClass : get_all_operations : Function failed : {str(exc)}")
                return exc
            
        except (DatabaseConnectionFailed,TableNotFound) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : " +traceback.format_exc())
            return exc.msg
            
        
    def get_preprocess_cache(self, DBObject, connection ,dataset_id):
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
            
            data_df = self.get_data_df(DBObject, connection ,dataset_id)
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            #? Getting columns
            # sql_command = f"select st.column_name from mlaas.schema_tbl st where st.schema_id = '{schema_id}' order by index asc "
            # col_df = DBObject.select_records(connection, sql_command)
            # cols = col_df['column_name'].tolist()
            
            #? Getting Table Name
            table_name = DBObject.get_active_table_name(connection, dataset_id)
            
            missing_value_status = []
            noise_status = []
            for col in data_df.columns:
                
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
            # connection.close()
            logging.info("data preprocessing : PreprocessingClass : get_preprocess_cache : execution stop")
            return missing_value_status,noise_status
            
        except (DatabaseConnectionFailed,EntryNotFound,GetDataDfFailed) as exc:
            # connection.close()
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
                col_names(List of Strings): Column names
                data_types(List of Strings): Predicted Datatypes of every column.
                missing_value_status(List of booleans): State of missing values for each columns. 
                noise_status(List of booleans): State of noise for each columns. 
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : retrive_preprocess_cache : execution start")
            
            sql_command = f'''
                select 
                    st.column_name ,st.data_type, st.missing_flag, st.noise_flag 
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
            if not isinstance(cache_df,pd.DataFrame):
                raise ValueError
            
            col_names, data_types, missing_status, noise_status = cache_df['column_name'],cache_df['data_type'],cache_df['missing_flag'],cache_df['noise_flag']
            
            logging.info("data preprocessing : PreprocessingClass : retrive_preprocess_cache : execution stop")
            return col_names.tolist(), data_types.tolist(),missing_status.tolist(), noise_status.tolist()
            
        except Exception as exc:
            logging.info(f"data preprocessing : PreprocessingClass : retrive_preprocess_cache : function failed : {str(exc)}")
            return str(exc)
            
    def get_possible_operations(self, DBObject, connection ,dataset_id, schema_id, column_ids):
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
            data_df = self.get_data_df(DBObject, connection ,dataset_id,schema_id)
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            #? Getting Table Name
            table_name = DBObject.get_active_table_name(connection, dataset_id)
            
            num_cols = data_df._get_numeric_data().columns.tolist()
            
            try:
                # predicted_datatypes = self.get_attrbt_datatype(data_df,data_df.columns,len(data_df))
                #? Getting preprocess Cache from schema table
                col_names,predicted_dtypes,missing_flags_original,noise_flags_original = self.retrive_preprocess_cache(DBObject, connection, schema_id)
            except:
                raise NullValue(500)
            
            old_col_list = self.get_col_names(DBObject, connection ,schema_id,json = False,original = True)
            
            #? Serializing that data, arranging it according to the columns sent to the frontend
            predicted_datatypes = []
            missing_flags = []
            noise_flags = []
            for i in range(len(col_names)):
                if col_names[i] in old_col_list: #? Is the column being sent to front end?
                    predicted_datatypes.append(predicted_dtypes[i])
                    missing_flags.append(missing_flags_original[i])
                    noise_flags.append(noise_flags_original[i])
            
            #? Logical function starts
            try:
                #? Logical function starts
                all_col_operations = []
                
                for id in column_ids:
                    
                    #? Getting metadata for selected column
                    prev_col_name = old_col_list[id]
                    col = data_df.columns[id]
                    missing_flag = missing_flags[id]
                    noise_flag = noise_flags[id]
                    predicted_datatype = predicted_datatypes[id]
                    
                    #? Array to store the operations
                    operations = []

                    #? Column is both numerical & categorical
                    if (col in num_cols) and (predicted_datatype.startswith('ca')):
                        col_type = 0
                    #? Column is Numerical
                    elif col in num_cols:
                        col_type = 1
                    #? Column is categorical
                    elif predicted_datatype.startswith('ca'): #Categorical column
                        col_type = 2
                    elif predicted_datatype.startswith('t'): #Timestamp column
                        col_type = 4
                    else:
                        col_type = 3

                    # missing_values = self.detect_missing_values(DBObject, connection, table_name, prev_col_name)
                    # noise_status = self.dtct_noise(DBObject, connection, prev_col_name, table_name= table_name)
                    # if noise_status == 1:
                    #     noise_status = True
                    # else: noise_status = False
                    
                    #? Is there any missing value in the column?
                    if missing_flag == 'True':
                        #? Adding Missing Value Operations
                        if col_type == 0:
                            operations += [1,51,61,71,81,91,101,121]
                        elif col_type == 1:
                            operations += [1,51,61,71,81,91,121]
                        elif col_type == 2 or col_type == 3:
                            operations += [1,101,111]
                        
                    
                    #? Is there any noise in the column?
                    if noise_flag == 'True':
                        operations += [11,41,131,141,151,161,171,181]
                    
                    #? Outlier Removal & Scaling Operations for numeric; Encoding ops for Categorical
                    if missing_flag == 'False' and noise_flag == 'False':
                        if col_type == 0 or col_type == 1:
                            operations += [21,31,191,201,202,211,221,231,241,242,243,244,245]
                        if col_type == 2 or col_type == 3:
                            operations += [261,271]
                        if col_type == 0:
                            operations += [271]
                        
                    #? Math operations
                    if noise_flag == 'False':
                        if col_type == 0 or col_type == 1:
                            operations += [281,291,301,311]
                            is_positve_flag,is_zero_flag=DBObject.check_column_type(connection,dataset_id,prev_col_name)
                            logger.info("is_zero_flag"+str(is_zero_flag)+"==is_positve_flag"+str(is_positve_flag))
                            operations+=[256,254]
                            if is_positve_flag ==True:
                                operations += [252,255] 
                            if is_zero_flag == False:
                                operations += [253]  
                            if is_zero_flag == False and is_positve_flag == True:
                                operations += [251]  
                            
                    #? Adding Feature Engineering Operation
                    if col_type == 4:
                        operations += [321]
                            
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
                # connection.close()
                # return [i+self.op_diff for i in final_op_list]    
                return final_op_list
            
            except Exception as exc:
                # connection.close()
                logging.info(f"data preprocessing : PreprocessingClass : get_possible_operations : Function failed : {str(exc)}")
                return exc
                
        except (DatabaseConnectionFailed,EntryNotFound,GetDataDfFailed,NullValue) as exc:
            # connection.close()
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
                    operation_dict[op] = operation_dict.get(op,[]) + dic['column_id']
            
            #? Getting Values in a cleaned formate
            value_dict = {}
            for dic in data:
                for i,op in enumerate(dic['selected_handling']):
                    value_dict[op] = value_dict.get(op,[]) + [dic['values'][i]]
            
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
        
        
            
    def handover(self,DBObject, connection , dataset_id, schema_id, project_id, user_name,split_parameters,scaling_type = 0):        
        """[ This class is used to scale and split and save numpy files.]

        Args:
            DBObject ([type]): [DBclass Object]
            connection ([type]): [Connection Object]
            dataset_id ([type]): [dataset id of the dataset.]
            schema_id ([type]): [schema id of the dataset.]
            project_id ([type]): [project_id of the dataset.]
            user_name ([type]): [user name of dataset]
            split_parameters ([type]): [Dict of split_parameters]
            scaling_type (int, optional): [selected  split_method]. Defaults to 0.

        Returns:
            [Integer] : [return 0 if successfull else 1]
        """
        
        logging.info("data preprocessing : PreprocessingClass : handover : execution start")
        try:    
            
            unique_id = str(uuid.uuid1().time) #genrate unique_id
            scale_dir = "scaled_dataset/scaled_data_" + unique_id  #genrate scale_dir path
            CHECK_FOLDER = os.path.isdir(scale_dir) #check directory already exists or not
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(scale_dir) #create directory
                logger.info("data preprocessing : PreprocessingClass : handover : Directory Created")
            else:
                logger.info("data preprocessing : PreprocessingClass : handover :Directory  already exists")
            
            actual_Y_filename =  scale_dir+"/Unscaled_actual_Y_data_" + unique_id  #genrate file path for actual data
            #? Getting Dataframe
            data_df = self.get_data_df(DBObject, connection ,dataset_id,schema_id) #get dataframe
            
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            

            tg_cols = DBObject.get_target_col(connection, schema_id) #get list of the target columns
            target_cols = [data_df.columns[0]] #select first column
            target_cols += tg_cols     #list target_cols
            target_actual_features_df=data_df[target_cols] #get actual data of target column
            encoded_target_df=target_actual_features_df #assign to encoded df
            np.save(actual_Y_filename,target_actual_features_df.to_numpy()) #save Y_actual
            #encode if target column is string
            for col in target_cols[1:]:
                if encoded_target_df[col].dtype == 'O':
                    encoded_target_df[col] = le.fit_transform(encoded_target_df[col])  
                    
            encoded_target_df=encoded_target_df[target_cols] #encoded_target_df
            feature_cols = list(data_df.columns) #get list of the column
            
            for col in tg_cols:
                feature_cols.remove(col) #remove target columns from list
                    
            input_feature_df=data_df[feature_cols] #select input fetures dataframe
            #if there is string value the encode it
            for col in feature_cols[1:]:
                if input_feature_df[col].dtype == 'O':
                    input_feature_df[col] = le.fit_transform(input_feature_df[col]) 
            
            try:
                #scale the dataframe    
                if int(scaling_type) == 0:
                    input_feature_df.iloc[:,1:] = super().standard_scaling(input_feature_df.iloc[:,1:]) #standard_scaling
                elif int(scaling_type) == 1:
                    input_feature_df.iloc[:,1:] = super().min_max_scaling(input_feature_df.iloc[:,1:]) #min_max_scaling
                elif int(scaling_type) == 2:
                    input_feature_df.iloc[:,1:] = super().robust_scaling(input_feature_df.iloc[:,1:]) #robust_scaling
            except:
                raise ScalingFailed(500)

            
            input_features_df = input_feature_df #input_features_df
            target_features_df=encoded_target_df #target_features_df           
            mt = ModelType()
            problem_type = mt.get_model_type(target_features_df) #call get_model_type
            if problem_type == None:
                raise ModelIdentificationFailed(500)
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
            train_X_filename = scale_dir+"/scaled_train_X_data_" + unique_id #genrate train_X file path
            train_Y_filename = scale_dir+"/scaled_train_Y_data_" + unique_id #genrate train_Y file path
            test_X_filename =  scale_dir+"/scaled_test_X_data_" + unique_id  #genrate test_X file path  
            test_Y_filename =  scale_dir+"/scaled_test_Y_data_" + unique_id  #genrate test_Y file path     
            valid_X_filename = "None"
            valid_Y_filename = "None"
            Y_valid_count= None
            X_train, X_valid, X_test, Y_train, Y_valid, Y_test=sp.get_split_data(input_features_df,target_features_df, int(random_state),float(test_ratio), valid_ratio, str(split_method))
            if isinstance(X_train,str):
                return X_train

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
            
        
            scaled_split_parameters = '{"split_method":"'+str(split_method)+'" ,"cv":'+ str(cv)+',"valid_ratio":'+ str(valid_ratio)+', "test_ratio":'+ str(test_ratio)+',"random_state":'+ str(random_state)+',"valid_size":'+str(Y_valid_count)+',"train_size":'+str(Y_train_count)+',"test_size":'+str(Y_test_count)+',"train_X_filename":"'+train_X_filename+".npy"+'","train_Y_filename":"'+train_Y_filename+".npy"+'","test_X_filename":"'+test_X_filename+".npy"+'","test_Y_filename":"'+test_Y_filename+".npy"+'","valid_X_filename":"'+valid_X_filename+".npy"+'","valid_Y_filename":"'+valid_Y_filename+".npy"+'","actual_Y_filename":"'+actual_Y_filename+".npy"+'"}' #genrate scaled split parameters
            logger.info("scaled_split_parameters=="+scaled_split_parameters)
            sql_command = f"update mlaas.project_tbl set target_features= '{target_cols}' ,input_features='{feature_cols}',scaled_split_parameters = '{scaled_split_parameters}',problem_type = '{problem_type_dict}' where dataset_id = '{dataset_id}' and project_id = '{project_id}' and user_name= '{user_name}'"
            status = DBObject.update_records(connection, sql_command)
            if status==1:
                raise ProjectUpdateFailed(500)
            # connection.close()
            return status
            
        except (DatabaseConnectionFailed,GetDataDfFailed,ProjectUpdateFailed,SplitFailed,ModelIdentificationFailed,ScalingFailed) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : handover : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : handover : " +traceback.format_exc())
            return exc.msg
        
    def update_schema_flag_status(self,DBObject,connection,schema_id,dataset_id,column_list, **kwargs):
        """
        Function used to update the status for the Noise and Missing flag.
        
        Args : 
            DBObject ([type]): [DBClass Object]
            connection ([type]): [Connection Object]
            dataset_id ([type]): [dataset id of the dataset.]
            schema_id ([type]): [schema id of the dataset.]
            column_list ([List]): [List of column name] 
        Return : 
            [Integer] : [return 0 if successfully updated else return 1]      
        """
        try:
            logging.info("data preprocessing : PreprocessingClass : update_schema_flag_status : execution start")
            
            missing_flag,noise_flag = self.get_preprocess_cache(DBObject, connection ,dataset_id)

            
            for missing_flag,noise_flag,col_name in zip(missing_flag,noise_flag,column_list): 

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
            
            id = uuid.uuid1().time
            dag_id='Cleanup_dag_'+str(id)

            template = "cleanup_dag.template"
            namespace = "cleanup_dags"

            # #? Inserting into Dag_Status Table
            # col = "dag_id,status"
            # row_data = [tuple((dag_id,'0'))]
            # table_name = "mlaas.cleanup_dag_status"
            # insert_status,_ = DBObject.insert_records(connection,table_name,row_data,col)
            
            master_dict = {'active': 0}
            
            json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
            
            result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

            logging.info("data preprocessing : PreprocessingClass : get_cleanup_dag_name : execution stop")
            # connection.close()
            return dag_id
        
        except (DatabaseConnectionFailed) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_cleanup_dag_name : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_cleanup_dag_name : " +traceback.format_exc())
            return exc.msg
            
    
    def dag_executor(self,DBObject, connection ,project_id, dataset_id, schema_id, request, flag ,selected_visibility,dataset_name ,dataset_desc,user_name):
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
            
            sql_command = f"select pt.cleanup_dag_id from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
            dag_id_df = DBObject.select_records(connection,sql_command) 
            if not isinstance(dag_id_df,pd.DataFrame): return 1
            dag_id = dag_id_df['cleanup_dag_id'][0]
            
            # #? Setting the dag as busy
            # sql_command = f"update mlaas.cleanup_dag_status set status ='1' where dag_id = '{dag_id}'"
            # update_status = DBObject.update_records(connection,sql_command)

            op_dict, val_dict = self.reorder_operations(request)
            
            template = "cleanup_dag.template"
            namespace = "cleanup_dags"
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

            activity_id = 'cl_1'
            activity_status = self.get_cleanup_startend_desc(DBObject,connection,dataset_id,project_id,activity_id,user_name,dataset_name,flag='True')

            json_data = {}
            result = requests.post(f"http://airflow:8080/api/experimental/dags/{dag_id}/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
            logging.info("DAG RUN RESULT: "+str(result))
            
            logging.info("data preprocessing : PreprocessingClass : dag_executor : execution stop")
            # connection.close()   
            return 0
        
        except (DatabaseConnectionFailed,DagUpdateFailed) as exc:
            
            # connection.close()
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
            with open(f"project_dags/{namespace}/{file}","r") as ro:
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
            with open(f"project_dags/{namespace}/{file}", 'w') as wo:
                wo.write(new_str)

            logging.info("data preprocessing : PreprocessingClass : dag_updater : execution stop")
            
            return 0

        except Exception as e:
            return e

    def SaveAs(self,DBObject,connection,project_id,schema_id,table_name,user_name,dataset_visibility,dataset_name,selected_visibility,dataset_desc,cleanup_flag=None, **kwargs):
        '''
        Function used to create a new table with updated changes and insert a new record into dataset table and 
        update the dataset_id into the project_tbl

        Args :
            DBObject ([type]): [DBClass Object]
            connection ([type]): [Connection Object]
            dataset_id ([type]): [dataset id of the dataset.]
            project_id ([type]): [project id of the project table.]
            schema_id ([type]): [schema id of the dataset.]
            table_name ([String]): [Name of the dataset table]
            dataset_visibility[(String)] : [ Visibility of the dataset selected]
            dataset_name[(String)] : [dataset name input by user]
            selected_visibility[(String)] : [visibility input by user]
            dataset_desc[(String)] : [description input by user]
        Return :
            [Integer] : [return 0 if success else return 1 for failed]

        '''
        try:
            #? Safety measure in case if DAG calls this method with None parameters
            if dataset_name is None:
                return 1

            # Get table name,schema and columns from dataset class.
            tbl_name,schema,cols = dc.make_dataset_schema() 
            file_name = None
            file_size = '-'
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
                dataset_insert_status = dc.insert_raw_dataset(DBObject,connection,dataset_id,schema_id,user_name,table_name,dataset_visibility,cleanup_flag,selected_visibility)
                
                if dataset_insert_status == 0:

                    schema_update = self.update_schema(DBObject,connection,schema_id)
                    if schema_update == 0:
                        # Command will update the dataset id  in the project table
                        sql_command = f'update mlaas.project_tbl set dataset_id={str(dataset_id)} where project_id={str(project_id)}'
                                        
                        # Execute the sql query
                        update_status = DBObject.update_records(connection,sql_command)

                        return update_status
                    else:
                        return schema_update   
                    
                else:
                    return dataset_insert_status

            else:
                return insert_status
        except Exception as exc:
            return str(exc)

    def get_dag_status(self, DBObject, connection ,project_id):
        '''
            Used to get the dag status
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")
            
            #? Getting Dag id
            sql_command = f"select pt.cleanup_dag_id from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
            dag_id_df = DBObject.select_records(connection,sql_command) 
            if not isinstance(dag_id_df,pd.DataFrame): #! Failed to get dag status
                raise NullValue(500)
            dag_id = dag_id_df['cleanup_dag_id'][0]

            #? Getting Dag Status
            # sql_command = f"select cds.status from mlaas.cleanup_dag_status cds where cds.dag_id = '{dag_id}';"
            sql_command = f"select dr.state from public.dag_run dr where dr.dag_id = '{dag_id}' order by id desc limit 1"
            logging.info(sql_command)
            status_df = DBObject.select_records(connection,sql_command) 
            if not isinstance(status_df,pd.DataFrame): #! Failed to get dag status
                raise NullValue(500)

            if len(status_df) == 0:
                #? Dag hasn't run yet, so sending dag status as available
                return False
            
            status = status_df['state'][0]
            
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")
            # connection.close()
            if status == 'running':
                return True
            else:
                return False      
        except (DatabaseConnectionFailed, NullValue) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : " +traceback.format_exc())
            return exc.msg
        
    def get_modelling_status(self, DBObject, connection ,project_id):
        '''
            Used to get the dag status
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")
            
            sql_command = "SELECT model_status from mlaas.project_tbl where project_id='"+str(project_id)+"'"
            model_status_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
            status = model_status_df['model_status'][0]
            logging.info("------+++"+str(status))
            logging.info("data preprocessing : PreprocessingClass : get_dag_status : execution stop")
            # connection.close()
            if status == 0:
                return True
            else:
                return False
        except (DatabaseConnectionFailed,NullValue) as exc:
            # connection.close()
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_dag_status : " +traceback.format_exc())
            return exc.msg

    def get_cleanup_startend_desc(self,DBObject,connection,dataset_id,project_id,activity_id,user_name,new_dataset_name,flag=None):
        """This function will replace * into project name and get activity description of scale and split.
 
        Args:
        project_name[String]: get project name
        activity_id[Integer]: get activity id
 
        Returns:
            [String]: activity_description
        """
        try:
            logging.info("data preprocessing : PreprocessingClass : get_cleanup_startend_desc : execution start")
            
            activity_df = self.AT.get_activity(activity_id,"US")
            
            datasetnm_df = DBObject.get_dataset_detail(DBObject,connection,dataset_id)
            dataset_name = datasetnm_df['dataset_name'][0]
            
            projectnm_df = DBObject.get_project_detail(DBObject,connection,project_id)
            project_name = projectnm_df['project_name'][0]

            # if new_dataset_name == None:
            #     new_dataset_name = dataset_name

            sql_command = f"select amt.activity_description as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
            desc_df = DBObject.select_records(connection,sql_command)
            activity_description = desc_df['description'][0]
            activity_description = activity_description.replace('*',dataset_name)
            activity_description = activity_description.replace('&',project_name)
        
            end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            activity_status,index = self.AT.insert_user_activity(activity_id,user_name,project_id,dataset_id,activity_description,end_time)
            
            if new_dataset_name != None and flag != 'True': 
                activity_id='cl_3'
                sql_command = f"select amt.activity_description as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
                desc_df = DBObject.select_records(connection,sql_command)
                activity_description = desc_df['description'][0]
                activity_description = activity_description.replace('*',new_dataset_name)
                logger.info("activity_description"+activity_description)
                activity_status,index = self.AT.insert_user_activity(activity_id,user_name,project_id,dataset_id,activity_description,end_time)
            
            logging.info("data preprocessing : PreprocessingClass : get_cleanup_startend_desc : execution stop")
            
            return activity_status
        except Exception as e:
            logging.error(f"data preprocessing : PreprocessingClass : get_cleanup_startend_desc : execution failed : {str(e)}")
            return 1
        
    def direct_save_as(self, DBObject, connection ,project_id,dataset_id,schema_id,user_name,dataset_name,selected_visibility,dataset_desc):
        '''
            This function is executed when the save as button is clicked without selecting
            any operation.
            
            Args:
            ----
            project_id (`Int`): Id of the project.  
            dataset_id (`Int`): Id of the dataset.  
            user_name (`String`): Name of the user.
            dataset_name (`String`): Name of the new dataset, Entered by user.
            selected_visibility (`String`) (`public | private`): visibility of the new dataset, selected by user.   
            dataset_desc (`String`): Description of the new dataset.
            
            Returns:
            -------
            status (`Int`): Status of Save as.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : direct_save_as : execution start")
            
            #Get the dataframe of dataset detail based on the dataset id
            dataframe = DBObject.get_dataset_detail(DBObject,connection,dataset_id)
 
            #Extract the dataframe based on its column name as key
            table_name,dataset_visibility,user_name = str(dataframe['dataset_table_name'][0]),str(dataframe['dataset_visibility'][0]),str(dataframe['user_name'][0])
            
            if dataset_visibility == 'private':
                dataset_table_name = user_name+'."'+table_name+'"'
            else:
                dataset_table_name = 'public'+'."'+table_name+'"'
                
            status = self.SaveAs(DBObject,connection, project_id,schema_id
                                 ,table_name,user_name,dataset_visibility,
                                 dataset_name,selected_visibility,dataset_desc,cleanup_flag=True)
            if status ==0: 
                activity_id='cl_3'
                sql_command = f"select amt.activity_description as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
                desc_df = DBObject.select_records(connection,sql_command)
                activity_description = desc_df['description'][0]
                activity_description = activity_description.replace('*',dataset_name)
                logger.info("activity_description"+activity_description)
                end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                activity_status,index = self.AT.insert_user_activity(activity_id,user_name,project_id,dataset_id,activity_description,end_time)
            # connection.close()
        
            logging.info("data preprocessing : PreprocessingClass : direct_save_as : execution stop")
        
            return status
        
        except (DatabaseConnectionFailed) as exc:
            return str(exc)
    
    def update_schema(self,DBObject,connection,schema_id):
        """
        function used to update schema for new dataset according to schema mapping page.
        Args:
            DBObject ([type]): [DBClass Object]
            connection ([type]): [Connection Object]
            schema_id[(schema_id)] : [Selected Id of the schema table]

        Return:
            [Integer] : [retrun 0 if successfully update/delete or both else return 1 if any of them failed ]
        """
        try:
            try:

                prev_col_name,current_col_name = DBObject.get_schema_columnlist(connection,schema_id, type ='all')
                
                for prev_col,current_col in zip(prev_col_name,current_col_name):
                    
                    #Query will update the column name based on the new column name for that particular schema_id
                    sql_command = f'''update mlaas.schema_tbl set column_name = '{str(current_col)}',changed_column_name = ''  where schema_id = '{str(schema_id)}' and column_name ='{str(prev_col)}' '''      
                    
                    #Execute the sql query
                    update_status = DBObject.update_records(connection,sql_command)
                    
                    if update_status != 0:
                        raise SchemaColumnUpdate(500)

                if update_status == 0:
                    #query will delete the columns which has "column attribute" - Ignore
                    sql_command =f'''delete from mlaas.schema_tbl where schema_id='{str(schema_id)}' and column_attribute = 'Ignore' '''
                    
                    #Execute the sql query 
                    update_status = DBObject.update_records(connection,sql_command)
                    
                    if update_status !=0:
                        return SchemaColumnDeleteion(500)
                    
                return update_status
            except (SchemaColumnDeleteion,SchemaColumnUpdate) as exc:
                return exc.msg
                
        except Exception as exc:
            return str(exc)
        
    def operation_failed(self, DBObject,connection,dataset_id,project_id,new_user_name,col_name,failed_op):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        
        logging.info("data preprocessing : CleaningClass : operation_failed : execution start")
        
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        # operation_id += self.op_diff
        
        #? Getting Activity Description
        try:
            # failed_op += self.op_diff
            logging.info("data preprocessing : CleaningClass : operation_failed : execution start")
            activity_description = self.get_act_desc(DBObject, connection, failed_op, col_name, code = 0)
            logging.info(" failed description : "+str(activity_description))
            
            activity_id = failed_op
            end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            status,index = self.AT.insert_user_activity(activity_id,new_user_name,project_id,dataset_id,activity_description,end_time,column_id =col_name)
            
            logging.info("data preprocessing : CleaningClass : operation_failed : execution stop")
            return status
        except Exception as exc:
            logging.error(f"data preprocessing : CleaningClass : operation_failed :  Exception : {str(exc)} ")
            return 1

    
    def check_failed_col(self,DBObject, connection,dataset_id,project_id,new_user_name,col_list, dag_id):
        '''
            This class checks for the failed operations and enters appropriate activity in the 
            activity timeline.

            Args:
            -----
            dataset_id
            project_id
            new_user_name (`String`): Name of th user.
            col_list (`List of integers`): Failed column list
            dag_id (`String`): Id of the dag

            Returns:
            -------
            status (`Int`): Status of operation insertion
        '''
        
        logging.info("data preprocessing : CleaningClass : check_failed_col : execution start")
        try:
            sql_command = f"select ti.task_id as task_name from public.task_instance ti where ti.dag_id = '{dag_id}' and ti.state = 'failed' "
            failed_df = DBObject.select_records(connection,sql_command)

            logging.info(" dataframe for failed task id name : "+ str(failed_df['task_name']))
            
            for failed_str in failed_df.iloc[:,0]:
                params = failed_str.split('_')
                logging.info(" split parameters : "+ str(params))
                if len(params) != 3:
                    failed_op,failed_col = int(params[1]),int(params[3])
                    logging.info(f" failed operation name : {failed_op} <[]> failed_col : {failed_col} ")

                col_name = col_list[failed_col] 
                logging.info(f"column name based on failed col ID :  {col_name}")

                status = self.operation_failed(DBObject,connection,dataset_id,project_id,new_user_name,col_name,failed_op)

                if status !=0:
                    break

            logging.info("data preprocessing : CleaningClass  : check_failed_col : execution stop")
            return  status
        except Exception as exc:
            logging.error(f"data preprocessing : CleaningClass : check_failed_col :  Exception : {str(exc)} ")
            return 1
    
    def get_act_desc(self, DBObject, connection, operation_id, col_name, code = 1):
        '''
            Used to get preprocess activity description from the activity master table.
        
            Returns:
            --------
            description (`String`): Description for the activity.
        '''
        try:
            logging.info("data preprocessing : CleaningClass : get_activity_desc : execution start")
            
            #? Getting Description
            sql_command = f"select replace (amt.activity_name || ' ' || amt.activity_description, '*', '{col_name}') as description from mlaas.activity_master_tbl amt where amt.activity_id = '{operation_id}' and amt.code = '{code}'"
            logging.info(f"sql_command : {sql_command}" )

            desc_df = DBObject.select_records(connection,sql_command)
            if not isinstance(desc_df, pd.DataFrame):
                return "Failed to Extract Activity Description."
            
            #? Fatching the description
            description = desc_df['description'].tolist()[0]
            
            logging.info("data preprocessing : CleaningClass : get_activity_desc : execution stop")
            
            return description
        except Exception as e:
            logging.error(f"data preprocessing : CleaningClass : get_activity_desc : execution failed : {str(e)}")
            return str(e)
