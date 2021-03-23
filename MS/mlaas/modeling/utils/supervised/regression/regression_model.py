'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''

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

from ...model_utils.sklearn_regression import linear_regressor
from ...model_experiments import model_experiment
from sklearn.model_selection import train_test_split

# from ....split_data import SplitData
from common.utils.logger_handler import custom_logger as cl



user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')




class RegressionClass:
    
    def regression_model(self,Model_Mode, user_id, project_id,dataset_id,model_type,algorithm_type,target_type,
                        DBObject, connection,experiment_name,experiment_desc):
        
        """This function is used to run regression type model.
        """
        logging.info("modeling : RegressionClass : regression_model : execution start")

        #TODO we will remove this condition and pass variable to rest api
        
        if target_type == 'Single_Target':
            
            json_data = {'conf':'{"model_mode":"Auto","project_id":'+str(project_id)+',"dataset_id":'+str(dataset_id)+',"exp_name":"'+experiment_name+'","exp_desc":"'+experiment_desc+'","user_id":'+str(user_id)+'}'}
            
            logging.info("modeling : RegressionClass : all_regression_model : execution"+str(json_data))
            
            result = requests.post("http://airflow:8080/api/experimental/dags/auto_regressor_pipeline/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
        else:
            print("yet not tested")
            
        logging.info("modeling : RegressionClass : regression_model : execution end")
        
    
    # This is for manually model run    
    def run_regression_model(self, Model_Mode,user_id,project_id,dataset_id,DBObject,connection,model_id,
                            experiment_name,experiment_desc):
        
        """This function is used to run model directly when model mode is in manual.
           it will run model based on model name or id and model type.
        
        """
        logging.info("modeling : RegressionClass : run_regression_model : execution start")
 
        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        model_name = 'linear_regression_sklearn'
        json_data = {'conf':'{"model_mode":"Manual","model_id":'+str(model_id)+', "model_name":"'+model_name+'", "project_id":'+str(project_id)+',"dataset_id":'+str(dataset_id)+',"exp_name":"'+experiment_name+'","exp_desc":"'+experiment_desc+'","user_id":'+str(user_id)+'}'}
        # json_data = {'conf':'{"model_mode":"Auto","project_id":'+str(project_id)+',"dataset_id":'+str(dataset_id)+',"exp_name":"'+experiment_name+'","exp_desc":"'+experiment_desc+'","user_id":'+str(user_id)+'}'}
        logging.info("modeling : RegressionClass : all_regression_model : execution"+str(json_data))
        
        result = requests.post("http://airflow:8080/api/experimental/dags/manual_regression_dag/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
        logging.info("modeling : RegressionClass : run_regression_model : execution end")


    