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

        sql_command = f"delete from {table_name}  where {col_name} is null" # Get update query
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

        sql_command = f"Update {table_name} set {col_name}={impute_value} where {col_name} is null" # Get update query
        logging.info(str(sql_command))

        status = DBObject.update_records(connection,sql_command)

        logging.info("Preprocess : MissingValueClass : mean_imputation : execution stop")
        return status

    def imputation(self,DBObject,connection,column_list, table_name, col, operation,value = None):
        
        logging.info("data preprocessing : CleaningClass : mean_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for column in cols:
            try:
                if value is None and operation ==9:
                    impute_value = 'Missing'

                elif value is not None:
                    impute_value = str(value)

                else:
                    impute_value = self.get_impute_value(DBObject,connection,table_name,column,operation)

                status = self.perform_missing_value_imputation(DBObject,connection, table_name,column,impute_value)

            except Exception as exc:
                logging.info(str(exc) + " error ")
                status = 1
                continue

        logging.info("data preprocessing : CleaningClass : mean_imputation : execution stop")
        return status
    
    def get_impute_value(self,DBObject,connection,table_name,column_name,operation):

        if operation == 4:
            sql_command = 'select AVG("'+column_name+'") AS impute_value from '+str(table_name)
            logging.info(str(sql_command))
            
            
        elif operation == 5:
            sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(column_name)+'") AS impute_value from '+str(table_name)
            logging.info(str(sql_command))

            
        elif operation == 6:
            sql_command = 'select MODE() WITHIN GROUP (ORDER BY "'+str(column_name)+'") AS impute_value from '+str(table_name)
            logging.info(str(sql_command))
            

        elif operation == 7:
            sql_command = 'select (AVG("'+str(column_name)+'")+3*STDDEV("'+str(column_name)+'")) AS impute_value from '+str(table_name)
            logging.info(str(sql_command))
            
        dataframe = DBObject.select_records(connection,sql_command)
        impute_value = round(dataframe['impute_value'][0],5)
        logging.info(str(impute_value))
        
        return impute_value 
    
