'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Exceptions
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
from .model_type import ModelType
# from modeling.split_data import SplitData as sd
#from model_type import ModelType

#* Library Imports
import os
import logging
import traceback
import numpy as np
import pandas as pd
import uuid
from sklearn.model_selection import train_test_split

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('preprocessing')

#* Object Definition
dc = dataset_creation.DatasetClass()

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
    
    def save_schema_data(self,schema_data,project_id,dataset_id,schema_id):
        try:
            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")

            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            status = super(PreprocessingClass,self).save_schema(DBObject,connection,schema_data,project_id,dataset_id,schema_id)

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
        
    def get_col_names(self, schema_id, json = False):
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
                
            sql_command = f"select case when changed_column_name = '' then column_name else changed_column_name end column_list,case when 'True' in( missing_flag, noise_flag) then 'True' else 'False' end flag from mlaas.schema_tbl where schema_id ='{str(schema_id)}' and column_attribute !='Ignore' order by index"
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
            logging.info("AAAAAAAAAAAAAAAAAAAA" + str(json_data))
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
                
            sql_command = f"select amt.activity_id,amt.activity_name,amt.user_input,pat.parent_activity_name,ptt.tab_name from mlaas.activity_master_tbl amt , mlaas.parent_activity_tbl pat, mlaas.preprocess_tab_tbl ptt where amt.code = '0' and amt.parent_activity_id = pat.parent_activity_id and ptt.tab_id = pat.tab_id order by amt.activity_id"
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
                is_missing_value = series.isnull().any()
                missing_value_status.append(is_missing_value)
                
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
            
    # def get_possible_operations(self, dataset_id, schema_id, column_ids):
    #     '''
    #         This function returns all possible operations for given columns.
            
    #         Args:
    #             schema_id(int): Id of the dataset's schema.
    #             column_ids(list of intigers): Selected columns.
                
    #         Returns:
    #             operations[List]: List of possible operations.
    #     '''
    #     try:
    #         logging.info("data preprocessing : PreprocessingClass : get_possible_operations : execution start")
            
    #         #TODO: THIS NEEDS TO BE REMOVED LATER BECAUSE IT TAKES MORE TIME TO GET WHOLE DATAFRAME
            
    #         #? Getting Dataframe
    #         data_df = self.get_data_df(dataset_id,schema_id)
    #         if isinstance(data_df, str):
    #             raise GetDataDfFailed(500)
            
    #         #TODO: Remove Until HERE
            
    #         #? Getting DB object & connection object
    #         DBObject,connection,connection_string = self.get_db_connection()
    #         if connection == None :
    #             raise DatabaseConnectionFailed(500)

    #         num_cols = [data_df.columns.get_loc(i) for i in data_df._get_numeric_data().columns]
    #         data_types, missing_val_list, noise_list = self.retrive_preprocess_cache(DBObject,connection,schema_id)
    #         data_types = data_types[1:]
    #         missing_val_list = missing_val_list[1:]
    #         noise_list = noise_list[1:]
            
    #         missing_val_list = [bool(i) for i in missing_val_list]
    #         noise_list = [bool(i) for i in noise_list]
            
    #         #? Logical function starts
    #         try:
    #             all_col_operations = []

    #             for id in column_ids:
    #                 operations = [1,2,3,6,10]

    #                 #? Column is both numerical & categorical
    #                 if (id in num_cols) and (data_types[id].startswith('c') and data_types[id].endswith('l')):
    #                     col_type = 0
    #                 #? Column is Numerical
    #                 elif id in num_cols:
    #                     col_type = 1
    #                 #? Column is categorical
    #                 elif data_types[id].startswith('c') and data_types[id].endswith('l'):
    #                     col_type = 2
    #                 else:
    #                     col_type = 3

    #                 #? Column is text column
    #                 if col_type == 3:
    #                     all_col_operations.append(operations)
    #                     continue
                    
    #                 #? Adding Missing Value Operations
    #                 if col_type == 0:
    #                     operations += [4,5,7,8,9]
    #                 elif col_type == 1:
    #                     operations += [4,5,7]
    #                 elif col_type == 2:
    #                     operations += [8,9]
                    
    #                 #? Adding Noise Reduction Operations
    #                 if not missing_val_list[id]:
    #                     operations += [11,14,15]
    #                     if col_type == 0 or col_type == 1:
    #                         operations += [12,13]
                    
    #                 #? Outlier Removal & Scaling Operations for numeric; Encoding ops for Categorical
    #                 if not missing_val_list[id] and not noise_list[id]:
    #                     if col_type == 0 or col_type == 1:
    #                         operations += [16,17,18,19,20,21,22,23,24,25,26]
    #                     if col_type == 0 or col_type == 2:
    #                         operations += [27,28,29]
                        
    #                 #? Math operations
    #                 if not noise_list[id]:
    #                     if col_type == 0 or col_type == 1:
    #                         operations += [30,31,32,33]
                            
    #                 all_col_operations.append(operations)
                
    #             #? Getting Final Common Operation List
    #             final_op_list = []
    #             for ops in all_col_operations:
    #                 for op in ops:
    #                     flag = True
    #                     for other_ops in all_col_operations:
    #                         if op not in other_ops:
    #                             flag = False
    #                             break
    #                     if flag == True:
    #                         final_op_list.append(op)
    #             final_op_list = list(set(final_op_list))
    #             final_op_list.sort()
                
    #             logging.info("data preprocessing : PreprocessingClass : get_possible_operations : execution End")
                
    #             return [i+8 for i in final_op_list]    
            
    #         except Exception as exc:
    #             logging.info(f"data preprocessing : PreprocessingClass : get_possible_operations : Function failed : {str(exc)}")
    #             return exc
            
    #     except (DatabaseConnectionFailed,GetDataDfFailed) as exc:
    #         logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
    #         logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
    #         return exc.msg
        
        
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
            
            #? Logical function starts
            try:
                #? Logical function starts
                all_col_operations = []

                for id in column_ids:
                    col = data_df.columns[id]
                    series = data_df[col]
                    operations = [3,4]

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

                    missing_values = data_df[col].isnull().any()
                    noise_status = self.dtct_noise(DBObject, connection, col, table_name= table_name)
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
                        if col_type == 0 or col_type == 1:
                            operations += [5,14,15,16,17,18,19]
                    
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
            This function accepts list of operations sent by front end &
            returns a optimized reordered dictionary.
            
            Input data format:
            [
                {
                column_id: [1]
                selected_handling: [12,16,17]
                values: [15,'',33]
                },
                {
                column_id: [1,2]
                selected_handling: [10,14,17]
                values: ['','','']
                }
            ]
            
            Output dictionary:
            {
                10: [1,2],
                12: [1],
                14: [1,2],
                16: [1],
                17: [1,2]
            }
            
            args:
                data[List of Dictionaries]: Data sent by frontend.
            
            Returns:
                final_dict[Dictionary]: Operation Order optimized dictionary;
                    final_dict = {
                        operation: [column(s)]
                    }
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : reorder_operations : execution start")
            
            #? Getting operations in a cleaned format
            operation_dict = {}
            for dicts in data:
                for ids in dicts['column_id']:
                    operation_dict[ids] = list(set(operation_dict.get(ids,[]) + [i-self.op_diff for i in dicts['selected_handling']]))
                    #? Important: Above line also handles the renumbering of the operation numbers
        
            #? Getting all the operation in the sorted order
            operations = list(operation_dict.values())
            all_operations = []
            for ops in operations:
                all_operations += ops

            #? Getting all operations   
            all_operations = list(set(all_operations))
            #? Sorting Operations
            all_operations.sort()
            #? Rearranging the operation numbering such that they start from 1
            
            #? Getting final reordered dictionary
            final_dict = {}
            for op in all_operations: 
                cols = []
                for i,val in operation_dict.items():
                    if op in val:
                        cols.append(i)

                final_dict[op] = cols
                i+=1
            
            logging.info("data preprocessing : PreprocessingClass : reorder_operations : execution end")
            
            return final_dict
        
        except Exception as exc:
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc))
            return OperationOrderingFailed(500).msg
        
        
    def master_executor(self, project_id,dataset_id, schema_id,request, save_as = False,value = None):
        '''
            It takes the request from the frontend and executes the cleanup operations.
            
            Args:
            -----
            dataset_id (`Intiger`): Id of the dataset.
            schema_id (`Intiger`): Id of the dataset in the schema_tbl.
            request (`Dict`): Request coming from the frontend.
            save_as (`Boolean`) (default = `False`): Has the user chosen save_as option?
            
            Returns:
            --------
            Positive or Negative responce.
        '''
        
        try:
            logging.info("data preprocessing : PreprocessingClass : master_executor : execution start")
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)
            #? Getting Dataframe
            
            #Get the dataframe of dataset detail based on the dataset id
            dataframe = DBObject.get_dataset_detail(DBObject,connection,dataset_id)

            #Extract the dataframe based on its column name as key
            table_name,dataset_visibility,user_name = str(dataframe['dataset_table_name'][0]),str(dataframe['dataset_visibility'][0]),str(dataframe['user_name'][0])
            
            if dataset_visibility == 'private':
                dataset_table_name = user_name+'."'+table_name+'"'
            else:
                dataset_table_name = 'public'+'."'+table_name+'"'

            #get the Column list
            column_list = self.get_col_names(schema_id)
            logging.info(str(column_list) + " column_list")

            #? Getting operations in the ordered format
            operation_ordering = self.reorder_operations(request)
            
            operations = operation_ordering.keys()
            for op in operations:
                status = 1
                flag = False
                
                #? Getting Columns
                col = operation_ordering[op]
                temp_col = [column_list[i] for i in col]
                temp_col = str(temp_col)
                temp_col = temp_col[1:-1]
                temp_col = temp_col.replace('"',"'")
                
                activity_id = self.operation_start(DBObject, connection, op, user_name, project_id, dataset_id, temp_col)
                
                if op == 1:
                    status = self.discard_missing_values(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True
                # elif op == 3:
                #     data_df = self.delete_above(data_df, col, val)
                # elif op == 4:
                #     data_df = self.delete_below(data_df, col, val)
                elif op == 6:
                    status = self.mean_imputation(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True
                elif op == 7:
                    status = self.median_imputation(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True
                # elif op == 6:
                #     data_df = self.arbitrary_value_imputation(data_df, col, val)
                elif op == 10:
                    status = self.end_of_distribution(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True
                elif op == 11:
                    status = self.frequent_category_imputation(DBObject,connection,column_list, dataset_table_name, col,value)
                    flag = True
                elif op == 12:
                    status = self.missing_category_imputation(DBObject,connection,column_list, dataset_table_name, col,value)
                    flag = True
                elif op == 13:
                    status = self.random_sample_imputation(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                # elif op == 11:
                #     data_df = self.get_data_df(dataset_id,schema_id)
                #     if isinstance(data_df, str):
                #         raise GetDataDfFailed(500)
                #     data_df = self.remove_noise(data_df, col)
                # elif op == 12:
                #     data_df = self.get_data_df(dataset_id,schema_id)
                #     if isinstance(data_df, str):
                #         raise GetDataDfFailed(500)
                #     data_df = self.repl_noise_mean(data_df, col)
                # elif op == 13:
                #     data_df = self.get_data_df(dataset_id,schema_id)
                #     if isinstance(data_df, str):
                #         raise GetDataDfFailed(500)
                #     data_df = self.repl_noise_median(data_df, col)
                # elif op == 14:
                #     data_df = self.get_data_df(dataset_id,schema_id)
                #     if isinstance(data_df, str):
                #         raise GetDataDfFailed(500)
                #     data_df = self.repl_noise_random_sample(data_df, col)
                # # elif op == 15:
                # #     data_df = self.repl_noise_arbitrary_val(data_df, col, val)
                elif op == 20:
                    status = self.rem_outliers_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 21:
                    status = self.rem_outliers_z_score(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 22:
                    status = self.repl_outliers_mean_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 23:
                    status = self.repl_outliers_mean_z_score(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 24:
                    status = self.repl_outliers_med_ext_val_analysis(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 25:
                    status = self.repl_outliers_med_z_score(DBObject,connection,column_list, dataset_table_name,col)
                    flag = True

                elif op == 26:
                    status = self.apply_log_transformation(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True

                elif op == 27:
                    status = self.label_encoding(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True

                elif op == 28:
                    status = self.one_hot_encoding(DBObject,connection,column_list, dataset_table_name, col)
                    flag = True
                elif op == 29:
                    status = self.add_to_column(DBObject,connection,column_list, dataset_table_name, col, value)
                    flag = True

                elif op == 30:
                    status = self.subtract_from_column(DBObject,connection,column_list, dataset_table_name, col, value)
                    flag = True

                elif op == 31:
                    status = self.multiply_column(DBObject,connection,column_list, dataset_table_name, col, value)
                    flag = True

                elif op == 32:
                    status = self.divide_column(DBObject,connection,column_list, dataset_table_name, col, value)
                    flag = True
                

                if status == 1:
                    if flag:
                        #? Sql function Failed
                        raise SavingFailed(500)
                    
                    data_df.drop(data_df.columns[0],axis=1, inplace = True)

                    updated_table_name = DBObject.get_table_name(connection,table_name)
                    
                    if dataset_visibility == 'public':
                        user_name='public'
        
                    status = DBObject.load_df_into_db(connection_string,updated_table_name,data_df,user_name)
    
                    sql_command = "update mlaas.dataset_tbl set dataset_table_name='"+str(updated_table_name)+"' where dataset_id='"+str(dataset_id)+"'"
                    logging.info(str(sql_command))
                    update_status = DBObject.update_records(connection,sql_command)
                    status = update_status
                    if status == 1:
                        raise SavingFailed(500)
                    else:
                        sql_command = f"drop table {dataset_table_name}"
                        update_status = DBObject.update_records(connection,sql_command)
                        status = update_status
                        activity_status = self.operation_end(DBObject, connection, activity_id, op, temp_col)
                else:
                    activity_status = self.operation_end(DBObject, connection, activity_id, op, temp_col)
                    
                    
            logging.info("data preprocessing : PreprocessingClass : master_executor : execution stop")
            return status

        except (DatabaseConnectionFailed,GetDataDfFailed,SavingFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
            logging.error(str(exc) +" Error")
            return exc.msg
            
    def handover(self, dataset_id, schema_id, project_id, user_name,split_parameters,scaling_type = 0, val = None):
        '''
            This function is used to store the scaled numpy file into the scaled dataset folder.
            
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
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            #? Getting Dataframe
            data_df = self.get_data_df(dataset_id,schema_id)
            if isinstance(data_df, str):
                raise GetDataDfFailed(500)
            
            if scaling_type == 0:
                data_df[:,1:] = self.standard_scaling(data_df[:,1:])
            elif scaling_type == 1:
                data_df[:,1:] = self.min_max_scaling(data_df[:,1:])
            elif scaling_type == 2:
                data_df[:,1:] = self.robust_scaling(data_df[:,1:])
                    
            feature_cols = list(data_df.columns)
            tg_cols = DBObject.get_target_col(connection, schema_id)
            for col in tg_cols:
                feature_cols.remove(col)
            target_cols = [data_df.columns[0]]
            target_cols += tg_cols
            
            input_features_df = data_df[feature_cols] #input_features_df
            target_features_df=data_df[target_cols] #target_features_df
            mt = ModelType()
            problem_type = mt.get_model_type(target_features_df)
            model_type = problem_type[0]
            algorithm_type = problem_type[1]
            target_type = problem_type[2]
            problem_type_dict = '{"model_type": "'+str(model_type)+'","algorithm_type": "'+str(algorithm_type)+'","target_type": "'+str(target_type)+'"}'
            
            feature_cols = str(feature_cols) #input feature_cols
            target_cols = str(target_cols) #target feature_cols
            feature_cols = feature_cols.replace("'",'"')
            target_cols = target_cols.replace("'",'"')


            # #splitting parameters
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
            X_train, X_valid, X_test, Y_train, Y_valid, Y_test=mt.get_split_data(input_features_df,target_features_df, int(random_state),float(test_ratio), valid_ratio, str(split_method))
            if split_method != 'cross_validation':
                Y_valid_count= Y_valid.shape[0]
                valid_X_filename = scale_dir+"/scaled_valid_X_data_" + unique_id #genrate valid_X file path     
                valid_Y_filename = scale_dir+"/scaled_valid_Y_data_" + unique_id #genrate valid_Y file path     
                np.save(valid_X_filename,X_valid.to_numpy()) #sa
                np.save(valid_Y_filename,Y_valid.to_numpy())    
            Y_train_count=Y_train.shape[0]
            Y_test_count =Y_test.shape[0]        
            np.save(train_X_filename,X_train.to_numpy())
            np.save(train_Y_filename,Y_train.to_numpy())
            np.save(test_X_filename,X_test.to_numpy())
            np.save(test_Y_filename,Y_test.to_numpy())
        
            scaled_split_parameters = '{"split_method":"'+str(split_method)+'" ,"cv":'+ str(cv)+',"valid_ratio":'+ str(valid_ratio)+', "test_ratio":'+ str(test_ratio)+',"random_state":'+ str(random_state)+',"valid_size":'+str(Y_valid_count)+',"train_size":'+str(Y_train_count)+',"test_size":'+str(Y_test_count)+',"train_X_filename":"'+train_X_filename+".npy"+'","train_Y_filename":"'+train_Y_filename+".npy"+'","test_X_filename":"'+test_X_filename+".npy"+'","test_Y_filename":"'+test_Y_filename+".npy"+'","valid_X_filename":"'+valid_X_filename+".npy"+'","valid_Y_filename":"'+valid_Y_filename+".npy"+'"}'
            logger.info("scaled_split_parameters=="+scaled_split_parameters)
            sql_command = f"update mlaas.project_tbl set target_features= '{target_cols}' ,input_features='{feature_cols}',scaled_split_parameters = '{scaled_split_parameters}',problem_type = '{problem_type_dict}' where dataset_id = '{dataset_id}' and project_id = '{project_id}' and user_name= '{user_name}'"
            status = DBObject.update_records(connection, sql_command)
            return status
            
        except (DatabaseConnectionFailed,GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : handover : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : handover : " +traceback.format_exc())
            return exc.msg
        
    def get_activity_desc(self, DBObject, connection, operation_id, col_name, code = 1):
        '''
            Used to get preprocess activity description from the activity master table.
        
            Returns:
            --------
            description (`String`): Description for the activity.
        '''
        logging.info("data preprocessing : PreprocessingClass : get_activity_desc : execution start")
        
        #? Getting Description
        sql_command = f"select replace (amt.activity_name || ' ' || amt.activity_description, '*', {col_name}) as description from mlaas.activity_master_tbl amt where amt.activity_id = '{operation_id}' and amt.code = '{code}'"
        
        desc_df = DBObject.select_records(connection,sql_command)
        if not isinstance(desc_df, pd.DataFrame):
            return "Failed to Extract Activity Description."
        
        #? Fatching the description
        description = desc_df['description'].tolist()[0]
        
        logging.info("data preprocessing : PreprocessingClass : get_activity_desc : execution stop")
        
        return description
            
    def operation_start(self, DBObject, connection, operation_id, user_name, project_id, dataset_id, col_name):
        '''
            Used to Insert Activity in the Activity Timeline Table.
            
            Returns:
            --------
            activity_id (`Intiger`): index of the activity in the activity transection table.
        '''
        logging.info("data preprocessing : PreprocessingClass : operation_start : execution start")
            
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        operation_id += self.op_diff
        
        #? Getting Activity Description
        desc = self.get_activity_desc(DBObject, connection, operation_id, col_name, code = 1)
        
        #? Inserting the activity in the activity_detail_table
        _,activity_id = self.AT.insert_user_activity(operation_id,user_name,project_id,dataset_id,desc,column_id =col_name)
        
        logging.info("data preprocessing : PreprocessingClass : operation_start : execution stop")
        
        return activity_id
    
    def operation_end(self, DBObject, connection, activity_id, operation_id, col_name):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        
        logging.info("data preprocessing : PreprocessingClass : operation_end : execution start")
        
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        operation_id += self.op_diff
        
        #? Getting Activity Description
        desc = self.get_activity_desc(DBObject, connection, operation_id, col_name, code = 2)
        
        #? Changing the activity description in the activity detail table 
        status = self.AT.update_activity(activity_id,desc)
        
        logging.info("data preprocessing : PreprocessingClass : operation_end : execution stop")
        
        return status



