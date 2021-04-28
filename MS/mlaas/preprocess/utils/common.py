'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
  Abhishek Negi         26-04-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging
import traceback
import pandas as pd


#* Relative Imports
from common.utils.logger_handler import custom_logger as cl
from common.utils.activity_timeline import activity_timeline
from database import *

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('Common_Cleanup_operation')


class CommonClass:
        
    def __init__(self):
        #* ACTIVITY TIMELINE OBJECT
        self.AT = activity_timeline.ActivityTimelineClass(database, user, password, host, port)
        
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

    def operation_start(self, DBObject, connection, operation_id, project_id, col_name):
        '''
            Used to Insert Activity in the Activity Timeline Table.
            
            Returns:
            --------
            activity_id (`Intiger`): index of the activity in the activity transection table.
        '''
        try:
            logging.info("data preprocessing : CleaningClass : operation_start : execution start")
                
            #? Transforming the operation_id to the operation id stored in the activity timeline table. 
            # operation_id += self.op_diff
            
            #? Getting Activity Description
            desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 1)
            
            #? Getting Dataset_id & User_Name
            sql_command = f"select pt.dataset_id,pt.user_name from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
            details_df = DBObject.select_records(connection,sql_command) 
            dataset_id,user_name = int(details_df['dataset_id'][0]),details_df['user_name'][0]

            #? Inserting the activity in the activity_detail_table
            _,activity_id = self.AT.insert_user_activity(operation_id,user_name,project_id,dataset_id,desc,column_id =col_name)
            
            logging.info("data preprocessing : CleaningClass : operation_start : execution stop")
            
            return activity_id
        except Exception as e:
            logging.error(f"data preprocessing : CleaningClass : operation_start : execution failed : {str(e)}")
            return -1
    
    def operation_end(self, DBObject, connection, activity_id, operation_id, col_name):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        try:
            logging.info("data preprocessing : CleaningClass : operation_end : execution start")
            
            #? Transforming the operation_id to the operation id stored in the activity timeline table. 
            # operation_id += self.op_diff
            
            if activity_id == -1:
                #? Activity insertion was failed
                raise RuntimeError

            #? Getting Activity Description
            desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 2)
            
            #? Changing the activity description in the activity detail table 
            status = self.AT.update_activity(activity_id,desc)
            
            logging.info("data preprocessing : CleaningClass : operation_end : execution stop")
            
            return status
        except Exception as e:
            logging.error(f"data preprocessing : CleaningClass : operation_end : execution failed : {str(e)}")
            return 1
    
    def operation_failed(self, DBObject, connection, activity_id, operation_id, col_name):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        try:
            logging.info("data preprocessing : CleaningClass : operation_failed : execution start")
            
            #? Transforming the operation_id to the operation id stored in the activity timeline table. 
            # operation_id += self.op_diff
            
            #? Getting Activity Description
            desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 0)
            
            #? Changing the activity description in the activity detail table 
            status = self.AT.update_activity(activity_id,desc)
            
            logging.info("data preprocessing : CleaningClass : operation_failed : execution stop")
            
            return status
        except Exception as e:
            logging.error(f"data preprocessing : CleaningClass : operation_failed : execution failed : {str(e)}")
            return 1
