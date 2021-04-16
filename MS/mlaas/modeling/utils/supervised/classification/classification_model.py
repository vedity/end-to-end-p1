'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


import numpy as np
import pandas as pd
import json
import mlflow
import mlflow.sklearn
import uuid
import logging
import requests


from ...model_experiments import model_experiment
from common.utils.logger_handler import custom_logger as cl


user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('classification_model')

class ProbabilisticClass:
    
    def classification_model(self,model_param_dict,db_param_dict):
        
        try:
            logging.info("modeling : RegressionClass : classification_model : execution start")
            
            if model_param_dict['target_type'] == 'Single_Target':
                
                json_data = {'conf':'{"model_param_dict":"'+str(model_param_dict)+'"}'}
                
                logging.info("modeling : RegressionClass : classification_model : execution"+str(json_data))
                
                result = requests.post("http://airflow:8080/api/experimental/dags/auto_classification_pipeline/dag_runs",data=json.dumps(json_data),verify=False)#owner
                
            else:
                print("yet not tested")
                
            logging.info("modeling : ClassificationClass : classification_model : execution end")
            logging.info("modeling : ClassificationClass : classification_model : "+str(result))
        
            return result

        except Exception as e:
            return e