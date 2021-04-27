'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         23-April-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging
import traceback

#* Commong Utilities
from common.utils.logger_handler import custom_logger as cl

#* Relative Imports
from ..schema import schema_creation

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('feature_extraction')

#* Defining Objects
sc = schema_creation.SchemaClass()

class FeatureEngineeringClass:
    
    #* DATETIME FEATURE ENGINEERING
    def datetime_fe(self, DBObject, connection, schema_id, column_name, table_name):
        '''
            It takes a datetime column and creates below features(columns) from it,
                - Date
                - Month
                - Year
                - Day of the Week
                - Week of the year
                - AM/PM
                - Hour
                - Minute
                - Second
                
            Args:
            ----
            DBObject (`object`): DBClass object
            connection (`pycopg2.conn`): Postgres connection object
            column_name (`String`): Name of the column
            table_name (`String`): Name of the table
            
            Returns:
            --------
            status (`Int`): Status of the operation (`0` or `1`)
        '''
        
        try:
            logging.info("Preprocess : FeatureEngineeringClass : datetime_fe : execution start")
            
            #* Altering the table to create new columns 
            #? Getting Names
            Array = ['Date','Month','Year','Day','Week_Num','AM_PM','Hour','Minute','Second']
            col_names = [column_name+'_'+i for i in Array]

            #? Generating the Alter sql command
            sql_command = f'ALTER TABLE {table_name} '
            for name in col_names:
                sql_command += f'add "{name}" INT,'
            else:
                sql_command = sql_command[:-1] #Removing the ','
            logging.info("Datetime Feature Creation Command =>" + sql_command)

            update_status = DBObject.update_records(connection, sql_command)
            if update_status != 0:
                raise RuntimeError
            
            #* Filling the newly generated columns with appropriate data
            #? Generating query
            sql_command = f'''
            update {table_name} 
            set "{column_name}_Date" = EXTRACT (day FROM "{column_name}"),
            "{column_name}_Month" = EXTRACT (month FROM "{column_name}"),
            "{column_name}_Year" = EXTRACT (year FROM "{column_name}"),
            "{column_name}_Day" = EXTRACT (DOW FROM "{column_name}"),
            "{column_name}_Week_Num" = EXTRACT (week FROM "{column_name}"),
            "{column_name}_AM_PM" = case when EXTRACT (hour FROM "{column_name}") >12 then 1 else 0 end ,
            "{column_name}_Hour" = EXTRACT (hour FROM "{column_name}"),
            "{column_name}_Minute" = EXTRACT (minute FROM "{column_name}"),
            "{column_name}_Second" = EXTRACT (second FROM "{column_name}")
            '''
            logging.info("Datetime Feature Extraction Command =>" + sql_command)

            #? Filling data
            update_status = DBObject.update_records(connection, sql_command)
            
            if update_status != 0:
                raise RuntimeError

            #? Updating the schema_tbl
            length = len(col_names)
            missing_lst = ['False']*length
            noise_lst = ['False']*length
            dtype_lst = ['numerical']*length

            schema_update = sc.update_dataset_schema(DBObject,connection,schema_id,col_names,dtype_lst,missing_flag=missing_lst,noise_flag=noise_lst,flag = True)
            
            logging.info("Preprocess : FeatureEngineeringClass : datetime_fe : execution stop")
            return schema_update
            
        except Exception as e:
            logging.error(f"Preprocess : FeatureEngineeringClass : datetime_fe : execution failed : error => {str(e)}")
            logging.error(f"Preprocess : FeatureEngineeringClass : datetime_fe : execution failed : traceback => {traceback.format_exc()}")
            return 1
