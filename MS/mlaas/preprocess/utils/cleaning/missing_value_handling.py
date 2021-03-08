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

    def discard_missing_values(self, DBObject,connection, table_name,col_name):
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
        logging.info("Preprocess : MissingValueClass : mean_imputation : execution start")

        sql_command = f'delete from {table_name}  where "{col_name}" is null' # Get update query
        logging.info(str(sql_command))

        status = DBObject.update_records(connection,sql_command)

        logging.info("Preprocess : MissingValueClass : mean_imputation : execution stop")
        return status
    
    def perform_missing_value_imputation(self,DBObject,connection, table_name,col_name,impute_value):
        """
        Function will replace column NaN value with its column mean value
        
        Args:
                series[(pandas.Series)] : [the Series containing the column data]
        Return:
                series[(pandas.Series)] : [return the updated series]  

        """
        logging.info("Preprocess : MissingValueClass : mean_imputation : execution start")

        sql_command = f'Update {table_name} set "{col_name}"={impute_value} where "{col_name}" is null' # Get update query
        logging.info(str(sql_command))

        status = DBObject.update_records(connection,sql_command)

        logging.info("Preprocess : MissingValueClass : mean_imputation : execution stop")
        return status
