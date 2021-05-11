'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''
# Imports All Necessary Library.
import numpy as np
import pandas as pd
import json
import re
import logging
import traceback
import datetime
import mlflow
import mlflow.sklearn
import uuid 
import requests

# from requests.auth import HTTPBasicAuth

# Imports Common Class Files.
from common.utils.logger_handler import custom_logger as cl

# Declare Global Object And Variables.
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('model_identifier')


class RegressionClass:
    
    def regression_model(self,basic_params_dict,db_param_dict):
        
        """This function is used to run regression type model.
        """
        
        try:
        
            logging.info("modeling : RegressionClass : regression_model : execution start")
    
            if basic_params_dict['target_type'] == 'Single_Target':
                
                json_data = {'conf':'{"basic_params_dict":"'+str(basic_params_dict)+'"}'}
                
                logging.info("modeling : RegressionClass : all_regression_model : execution"+str(json_data))
                
                result = requests.post("http://airflow:8080/api/experimental/dags/auto_regression_pipeline/dag_runs",data=json.dumps(json_data),verify=False)#owner
      
            else:
                print("yet not tested")
                
            logging.info("modeling : RegressionClass : regression_model : execution end")
            
            return result
        
        except Exception as e:
            return e
    
    


    