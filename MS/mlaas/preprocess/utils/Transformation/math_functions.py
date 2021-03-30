
#* Importing Common Utilities
from common.utils.logger_handler import custom_logger as cl

#* Importing Libraries
import logging

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('math_operations')


class MathOperationsClass:
    '''
        For Maths related Operations.
    '''
    
    def perform_math_operation(self, DBObject, connection, table_name, col_name, operation, value):
        '''
            Used to perform maths operations.
            
            Args:
            -----
            DBObject(`object`): DB class object.
            connection(`object`): Postgres connection object.
            table_name(`String`): Name of the table.
            col_name(`String`): Name of the column.
            operation(`String`): Operation symbol.
            
            Returns:
            Status(`Intiger`): Status of the query execution.
        '''
        
        logging.info("Preprocess : MathOperationsClass : perform_operation : execution start")
        
        sql_command = f'update {table_name} set "{col_name}" = "{col_name}" {operation} {value}' # Get update query

        logging.info("Math Operation Command: "+ sql_command)

        status = DBObject.update_records(connection,sql_command)
        
        logging.info("Preprocess : MathOperationsClass : perform_operation : execution stop")

        return status
