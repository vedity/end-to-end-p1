'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Exceptions
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

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

#* Library Imports
import logging
import traceback
import numpy as np
import pandas as pd
import uuid

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
        
    def get_col_names(self, schema_id):
        '''
            It is used to get the column names.
            
            Args:
                schema_id(Intiger): schema id of the associated dataset.
                
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

            json_data = [{"column_id": count, "col_name": column_name[count],"is_missing":flag_value[count]} for count in range(len(column_name))]
            logging.info(str(json_data) + " json data")
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
                
            sql_command = f"select amt.activity_id,amt.activity_name,pat.parent_activity_name from mlaas.activity_master_tbl amt , mlaas.parent_activity_tbl pat where amt.code = '0' and amt.parent_activity_id = pat.parent_activity_id"
            operations_df = DBObject.select_records(connection,sql_command) 
            
            if operations_df is None:
                raise TableNotFound(500)
            
            #? Logical Function Starts
            try:
                master_response = []
                i = 1
                
                #? Getting all operations based on the parent activities
                for dfs in operations_df.groupby('parent_activity_name'):
                    
                    #? Dictionary to store different operation classes
                    operation_class_dict = {}
                    operation_class_dict['id'] = i
                    i+=1
                    #? Name of Parent Activity
                    operation_class_dict['title'] = dfs[0]
                    
                    #? Adding all the operations that comes under the Parent activity
                    handlers = []
                    j = 1
                    for index,data in dfs[1].iterrows():
                        #? Dictionary for each operations
                        operation_dict = {}
                        operation_dict['id'] = j
                        operation_dict['name'] = data['activity_name']
                        operation_dict['operation_id'] = index
                        handlers.append(operation_dict)
                        j += 1
                    
                    #? All possible operations within the class
                    operation_class_dict['operations'] = handlers
                    master_response.append(operation_class_dict)
                    
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
            
            missing_value_status = []
            noise_status = []
            for col in data_df.columns:
                series = data_df[col]
                
                #? Checking if there are missing values in the column
                is_missing_value = series.isnull().any()
                missing_value_status.append(is_missing_value)
                
                #? Checking if there is noise in the column
                noisy,_,_ = self.detect_noise(series)
                noise_status.append(noisy)
            
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
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
                
            #? getting the name of the dataset_tbl
            table_name,_,_ = dc.make_dataset_schema()
            
            #? Getting user_name and dataset_visibility
            sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY,DATASET_TABLE_NAME,no_of_rows FROM {table_name} WHERE dataset_id = '{dataset_id}'"
            visibility_df = DBObject.select_records(connection,sql_command) 
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
            
            query = DBObject.get_query_string(connection,schema_id)
            #? Getting all the data
            sql_command = f"SELECT {str(query)} FROM {user_name}.{dataset_table_name}"
            data_df = DBObject.select_records(connection,sql_command)    
            
            num_cols = data_df._get_numeric_data().columns.tolist()
            predicted_datatypes = self.get_attrbt_datatype(data_df,data_df.columns,len(data_df))
            
            #? Logical function starts
            try:
                #? Logical function starts
                all_col_operations = []

                for id in column_ids:
                    col = data_df.columns[id]
                    series = data_df[col]
                    operations = [1,2,3,6,10]

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

                    #? Column is text column
                    if col_type == 3:
                        all_col_operations.append(operations)
                        continue
                    
                    #? Adding Missing Value Operations
                    if col_type == 0:
                        operations += [4,5,7,8,9]
                    elif col_type == 1:
                        operations += [4,5,7]
                    elif col_type == 2:
                        operations += [8,9]
                    
                    missing_values = data_df[col].isnull().any()
                    if missing_values == False:
                        noisy,_,_ = self.detect_noise(series)
                    
                    #? Adding Noise Reduction Operations
                    if not missing_values:
                        operations += [11,14,15]
                        if col_type == 0 or col_type == 1:
                            operations += [12,13]
                    
                    #? Outlier Removal & Scaling Operations for numeric; Encoding ops for Categorical
                    if not missing_values and not noisy:
                        if col_type == 0 or col_type == 1:
                            operations += [16,17,18,19,20,21,22,23,24,25,26]
                        if col_type == 0 or col_type == 2:
                            operations += [27,28,29]
                        
                    #? Math operations
                    if not noisy:
                        if col_type == 0 or col_type == 1:
                            operations += [30,31,32,33]
                            
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
                
                return [i+8 for i in final_op_list]    
            
            except Exception as exc:
                logging.info(f"data preprocessing : PreprocessingClass : get_possible_operations : Function failed : {str(exc)}")
                return exc
                
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
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
                },
                {
                column_id: [1,2]
                selected_handling: [10,14,17]
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
                    operation_dict[ids] = list(set(operation_dict.get(ids,[]) + [i-8 for i in dicts['selected_handling']]))
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
        
        
    def master_executor(self, dataset_id, schema_id,request, save_as = False):
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
            column_list = DBObject.get_column_list(connection,dataset_id)

            #? Getting operations in the ordered format
            operation_ordering = self.reorder_operations(request)
            
            operations = operation_ordering.keys()
            
            for op in operations:
                
                #? Getting Columns
                col = operation_ordering[op]

                if op == 1:
                    data_df = self.discard_missing_values(data_df, col)
                # elif op == 2:
                    # data_df = self.delete_above(data_df, col, val)
                # elif op == 3:
                    # data_df = self.delete_below(data_df, col, val)
                elif op == 5:
                    status = self.imputation(DBObject, connection, column_list, dataset_table_name, col,op)
                # elif op == 6:
                #     data_df = self.arbitrary_value_imputation(data_df, col, val)
                elif op == 7:
                    data_df = self.end_of_distribution(data_df, col)
                elif op == 8:
                    data_df = self.frequent_category_imputation(data_df, col)
                elif op == 9:
                    data_df = self.add_missing_category(data_df, col)
                elif op == 10:
                    data_df = self.random_sample_imputation(data_df, col)
                elif op == 11:
                    data_df = self.remove_noise(data_df, col)
                elif op == 12:
                    data_df = self.repl_noise_mean(data_df, col)
                elif op == 13:
                    data_df = self.repl_noise_median(data_df, col)
                elif op == 14:
                    data_df = self.repl_noise_random_sample(data_df, col)
                # elif op == 15:
                #     data_df = self.repl_noise_arbitrary_val(data_df, col, val)
                elif op == 16:
                    data_df = self.rem_outliers_ext_val_analysis(data_df, col)
                elif op == 17:
                    data_df = self.rem_outliers_z_score(data_df, col)
                elif op == 18:
                    data_df = self.repl_outliers_mean_ext_val_analysis(data_df, col)
                elif op == 19:
                    data_df = self.repl_outliers_mean_z_score(data_df, col)
                elif op == 20:
                    data_df = self.repl_outliers_med_ext_val_analysis(data_df, col)
                elif op == 21:
                    data_df = self.repl_outliers_med_z_score(data_df, col)
                elif op == 22:
                    data_df = self.apply_log_transformation(data_df, col)
                

            logging.info("data preprocessing : PreprocessingClass : master_executor : execution stop")
            return status

        except (GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_possible_operations : " +traceback.format_exc())
            return exc.msg
            
    def handover(self, dataset_id, schema_id, project_id, user_name, scaling_type = 0, val = None):
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
                data_df[:,1:] = self.standard_scaling(data_df[:,1:]._get_numeric_data())
            elif scaling_type == 1:
                data_df[:,1:] = self.min_max_scaling(data_df[:,1:]._get_numeric_data())
            elif scaling_type == 2:
                data_df[:,1:] = self.robust_scaling(data_df[:,1:]._get_numeric_data())
                    
            feature_cols = list(data_df.columns)
            tg_cols = DBObject.get_target_col(connection, schema_id)
            for col in tg_cols:
                feature_cols.remove(col)
            
            target_cols = [data_df.columns[0]]
            target_cols += tg_cols
            
            final_cols = feature_cols+tg_cols
            
            data_df = data_df[final_cols]
            
            feature_cols = str(feature_cols)
            target_cols = str(target_cols)
            feature_cols = feature_cols.replace("'",'"')
            target_cols = target_cols.replace("'",'"')
            filename = "scaled_dataset/scaled_data_" + str(uuid.uuid1().time)
            
            # sql_command = f"select * from mlaas.cleaned_ref_tbl crt where crt.dataset_id = '{dataset_id}' and crt.project_id = '{project_id}' and crt.user_id = '{user_id}'"
            # data=DBObject.select_records(connection,sql_command)
            
            np.save(filename,data_df.to_numpy())
            
            # if len(data) == 0:
            #     row = project_id,dataset_id,user_name,feature_cols,target_cols,filename
            #     row_tuples = [tuple(row)]
            #     col_names = "project_id,dataset_id,user_id,input_features,target_features,scaled_data_table"
                
            #     status = DBObject.insert_records(connection,"mlaas.cleaned_ref_tbl",row_tuples, col_names)
            #     logging.info("data preprocessing : PreprocessingClass : handover : execution stop")
                
            # else:
            sql_command = f"update mlaas.project_tbl set target_features= '{target_cols}' ,input_features='{feature_cols}',scaled_data_path = '{filename}' where dataset_id = '{dataset_id}' and project_id = '{project_id}' and user_name  = '{user_name}'"
            status = DBObject.update_records(connection, sql_command)
            
            return status
            
        except (DatabaseConnectionFailed,GetDataDfFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : handover : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : handover : " +traceback.format_exc())
            return exc.msg
            




