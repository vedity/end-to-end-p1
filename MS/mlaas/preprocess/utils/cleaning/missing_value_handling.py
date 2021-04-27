'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
  Abhishek Negi      17-Jan-2021           1.0           Created Class
 
*/
'''
#* Library Imports
import pandas as pd
import numpy as np
import logging
import traceback

#* Relative Imports
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('missing_value_handling')


class MissingValueClass:

    def discard_missing_values(self, DBObject,connection, table_name,col_name, condition = "is null"):
        '''
            Function will remove the rows where given columns have null values.
            
            Args:
            
                DBObject [(`object`)]   : [DB Class Object.]
                connection [(`object`)] : [Postgres Connection object.]
                table_name [(`String`)] : Name of the table. (Ex. `public.demo_tbl`)
                col_name [(`String`)]   : Name of the Column.
                condition[(String)] : [the condition need to be satisfied in sql query]

            Returns:
            
                [(intiger)]: [Return 0 if successfully function executed else return 1]
        '''
        try:
            logging.info("Preprocess : MissingValueClass : discard_missing_values : execution start")

            sql_command = f'delete from {table_name}  where "{col_name}" {condition}' # Get update query
            logging.info(str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            logging.info("Preprocess : MissingValueClass : discard_missing_values : execution stop")
            return status
        except Exception as e:
            logging.error(f"Preprocess : MissingValueClass : discard_missing_values : execution failed : {str(e)}")
            logging.error("Preprocess : MissingValueClass : discard_missing_values : : " +traceback.format_exc())
            return 1
    
    def perform_missing_value_imputation(self,DBObject,connection, table_name,col_name,impute_value, condition = "is null"):
        """
        Function will replace column NaN value with its column mean value
        
        Args:
                DBObject [(`object`)]   : [DB Class Object.]
                connection [(`object`)] : [Postgres Connection object.]
                table_name [(`String`)] : Name of the table. (Ex. `public.demo_tbl`)
                col_name [(`String`)]   : Name of the Column.
                impute_value[(Integer|decimal)] : [Value that will replace with Null]
                condition[(String)] : [the condition need to be satisfied in sql query]
        Return:
                [(intiger)]: [Return 0 if successfully function executed else return 1]  

        """
        try:
            logging.info("Preprocess : MissingValueClass : perform_missing_value_imputation : execution start")

            sql_command = f'Update {table_name} set "{col_name}"={impute_value} where "{col_name}" {condition}' # Get update query
            logging.info(str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            

            logging.info("Preprocess : MissingValueClass : perform_missing_value_imputation : execution stop")
            return status
        except Exception as exc:
            logging.error(f"Preprocess : MissingValueClass : perform_missing_value_imputation : execution failed : {str(exc)}")
            logging.error("Preprocess : MissingValueClass : perform_missing_value_imputation  : " +traceback.format_exc())
            return 1

    

    def random_sample_imputation(self,DBObject,connection,table_name,col_name,impute_value):
        '''
            This function will impute the missing values with the random values selected  from the column.

            Args:
            -----
                DBObject [(`object`)]   : [DB Class Object.]
                connection [(`object`)] : [Postgres Connection object.]
                table_name [(`String`)] : [Name of the table. (Ex. `public.demo_tbl`)]
                col_name [(`String`)]   : [Name of the Column.]
            Return:
                [(intiger)]: [Return 0 if successfully function executed else return 1]
        '''
        try:
            logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution start")
            
            sql_command = f'update {table_name} t1 set "{col_name}" = (select "{col_name}" col from {table_name} t2 where t2."{col_name}" is not null and t1."{col_name}" is null order by random() limit 1) where t1."{col_name}" is null'

            #sql_command = f'update {table_name} c set "{col_name}" =(select  random_value from (values {impute_value}) v(random_value) where C."{col_name}" <> v.random_value order by random() limit 1) where C."{col_name}" is null'
            logging.info("Sql_command : Update query : random_sample_imputation : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution stop")
            return status
        except Exception as exc:
            logging.error(f"Preprocess : MissingValueClass : random_sample_imputation : execution failed : {str(exc)}")
            logging.error("Preprocess : MissingValueClass : random_sample_imputation : " +traceback.format_exc())
            return 1

    
    def detect_missing_values(self, DBObject, connection, table_name, col_name):
        '''
            Function will detect the missing values in the column
            
            Args:
            -----
            DBObject [(`object`)]   : [DB Class Object.]
            connection [(`object`)] : [Postgres Connection object.]
            table_name [(`String`)] : [Name of the table. (Ex. `public.demo_tbl`)]
            col_name [(`String`)]   : [Name of the Column.]
            
            Returns:
            --------
            [(boolean)]: [`True` if missing value exists else `False`]
        '''
        try:
            logging.info("Preprocess : MissingValueClass : detect_missing_values : execution start")
            
            sql_command = f'select count(*) as missing_value from {table_name} where "{col_name}" is null;'
            
            noise_df = DBObject.select_records(connection,sql_command)

            logging.info("Preprocess : MissingValueClass : detect_missing_values : execution stop")
            
            if int(noise_df['missing_value'][0]) > 0:
                
                return True
            else:
                
                return False
        except Exception as e:
            logging.error(f"Preprocess : MissingValueClass : detect_missing_values : execution failed : {str(e)}")
            logging.error("Preprocess : MissingValueClass : detect_missing_values : " +traceback.format_exc())
            return False
    
        
