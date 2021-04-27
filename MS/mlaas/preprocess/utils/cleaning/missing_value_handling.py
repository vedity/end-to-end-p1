import pandas as pd
import numpy as np
import logging
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('missing_value_handling')


class MissingValueClass:

    def discard_missing_values(self, DBObject,connection, table_name,col_name, condition = "is null"):
        '''
            Returns a dataframe where all the rows where given columns have null values are removed.
            
            Args:
            -----
            dataframe (`pandas.Dataframe`): Whole Dataframe.
            column_id (`List`) (default = `None`): List of Columns. If `None` then considers whole dataframe.

            Returns:
            -------
            dataframe (`pandas.Dataframe`): Dataframe with all the missing data removed.
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
            return 1
    
    def perform_missing_value_imputation(self,DBObject,connection, table_name,col_name,impute_value, condition = "is null"):
        """
        Function will replace column NaN value with its column mean value
        
        Args:
                series[(pandas.Series)] : [the Series containing the column data]
        Return:
                series[(pandas.Series)] : [return the updated series]  

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
            return 1

    

    def random_sample_imputation(self,DBObject,connection,table_name,col_name,impute_value):
        '''
            This function will impute the missing values with the values of some random values from the column.

            Args:
            -----
            table_name (`String`)
            col_name (`String`)
            impute_value (`Integer`)
        '''
        try:
            logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution start")
            
            sql_command = f'update {table_name} t1 set "{col_name}" = (select "{col_name}" col from {table_name} t2 where t2."{col_name}" is not null and t1."{col_name}" is null order by random() limit 1) where t1."{col_name}" is null'

            #sql_command = f'update {table_name} c set "{col_name}" =(select  random_value from (values {impute_value}) v(random_value) where C."{col_name}" <> v.random_value order by random() limit 1) where C."{col_name}" is null'
            logging.info("Sql_command : Update query : random_sample_imputation : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution stop")
            return status
        except Exception as e:
            logging.error(f"Preprocess : MissingValueClass : random_sample_imputation : execution failed : {str(e)}")
            return 1

    
    def detect_missing_values(self, DBObject, connection, table_name, col_name):
        '''
            Returns True if there are any missing values in the column, else returns False.
            
            Args:
            -----
            DBObject (`object`): DB Class Object.
            connection (`object`): Postgres Connection object.
            table_name (`String`): Name of the table. (Ex. `public.demo_tbl`)
            col_name (`String`): Name of the Column.
            
            Returns:
            --------
            `boolean`: `True` if missing value exists else `False`.
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
            return False
    
        
