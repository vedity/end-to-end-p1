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

#* Library Imports
import logging
import traceback

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('preprocessing')

dc = dataset_creation.DatasetClass()

class PreprocessingClass(sc.SchemaClass,de.ExploreClass,nr.RemoveNoiseClass):
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
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            stats_df = super(PreprocessingClass,self).get_dataset_statistics(DBObject,connection,dataset_id,schema_id)
            if isinstance(stats_df, int):
                if stats_df == 1:
                    raise EntryNotFound(500)
                elif stats_df == 2:
                    raise StatisticsError(500)
            
        except (Exception,EntryNotFound,StatisticsError) as exc:
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
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_all_operations : " +traceback.format_exc())
            return exc.msg
            
        
    def get_preprocess_cache(self, dataset_id):
        '''
            This function is used to return Missing value & Noise status for all the columns
            
            Args:
                dataset_id(Intiger): id of the dataset.
                
            Returns:
                missing_value_status(List of Booleans): List containing missing value statuses for all the columns.
                noise_status(List of Booleans): List containing noise statuses for all the columns.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : get_preprocess_cache : execution start")
            
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
            
            #? Getting all the data
            sql_command = f"SELECT * FROM {user_name}.{dataset_table_name}"
            data_df = DBObject.select_records(connection,sql_command)    
            
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
            
        except (DatabaseConnectionFailed,EntryNotFound) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_preprocess_cache : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_preprocess_cache : " +traceback.format_exc())
            return exc.msg
        
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
            
            num_cols = data_df._get_numeric_data().columns
            numerical_columns = list(num_cols)
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
                    if (col in numerical_columns) and (predicted_datatypes[id].startswith('Ca')):
                        col_type = 0
                    #? Column is Numerical
                    elif col in numerical_columns:
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
                
                return final_op_list    
            
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
                    operation_dict[ids] = list(set(operation_dict.get(ids,[]) + dicts['selected_handling']))
        
            #? Getting all the operation in the sorted order
            operations = list(operation_dict.values())
            all_operations = []
            for ops in operations:
                all_operations += ops

            #? Getting all operations   
            all_operations = list(set(all_operations))
            #? Sorting Operations
            all_operations.sort()
            
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
    





