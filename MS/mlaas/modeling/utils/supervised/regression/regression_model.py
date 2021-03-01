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
    """Regression Class, stores the implementation of all the regression model.
    """
  
    def regression_model(self,Model_Mode, user_id, project_id,dataset_id, model_type, algorithm_type,
                        DBObject, connection):
        
        """This function is used to run regression type model.
        """
        logging.info("modeling : RegressionClass : regression_model : execution start")

        # Call private method of the current class .
        self.all_regression_model(Model_Mode, user_id,project_id,dataset_id, model_type, algorithm_type,
                                DBObject, connection)
        
        logging.info("modeling : RegressionClass : regression_model : execution end")
    
    # This is for auto model run   
    def all_regression_model(self,Model_Mode, user_id, project_id, dataset_id, model_type, algorithm_type,
                            DBObject, connection):
        
        """This function is used to run all regression type model.
        """
        logging.info("modeling : RegressionClass : all_regression_model : execution start")
        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        #TODO we will remove this condition and pass variable to rest api
        if algorithm_type == 'Single_Target':
            
            json_data = {'conf':'{"model_mode":"Auto","project_id":'+str(project_id)+',"dataset_id":'+str(dataset_id)+',"user_id":'+str(user_id)+'}'}
            
            logging.info("modeling : RegressionClass : all_regression_model : execution"+str(json_data))
            
            result = requests.post("http://airflow:8080/api/experimental/dags/auto_regressor_pipeline/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
        else:
            print("yet not tested")
            
        
        logging.info("modeling : RegressionClass : all_regression_model : execution end")
        
        
    # This is for manually model run    
    def run_regression_model(self,model_id,model_name,model_type,Model_Mode,
                             input_features_list,target_features_list,
                             X_train, X_valid, X_test, Y_train, Y_valid, Y_test,split_data_object,
                             DBObject, connection, connection_string, project_id,dataset_id,user_id):
        
        """This function is used to run model directly when model mode is in manual.
           it will run model based on model name or id and model type.
        
        """
        logging.info("modeling : RegressionClass : run_regression_model : execution start")

        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        if model_id == 1:
            
            mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow?options=-csearch_path%3Ddbo,mlaas")
            
            # TODO : we will used parameter class will take these parameters  from users.
            # Get model id and model name and model type from the user.
            model_id = 1
            model_name = 'linear regression'
            
            # Create an experiment name, which must be unique and case sensitive
            id = uuid.uuid1() 
            experiment_name = Model_Mode.upper() + "_" + "EXPERIMENT_"+ str(id.time)
            
            # create experiment 
            experiment_id = mlflow.create_experiment(experiment_name)
            experiment = mlflow.get_experiment(experiment_id)
            
             # mlflow set_experiment and run the model.
            with mlflow.start_run(experiment_id=experiment_id) as run:
                ## Declare Object
                LRObject = linear_regressor.LinearRegressionClass(input_features_list, target_features_list, 
                                                            X_train, X_valid, X_test, Y_train, Y_valid, 
                                                            Y_test, split_data_object) 
                LRObject.run_pipeline()
            
            
            run_uuid = run.info.run_id
            experiment_id = experiment.experiment_id
            # Add Experiment 
            ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode, DBObject, connection, connection_string)
            experiment_status = ExpObject.add_experiments(DBObject, connection, connection_string)
            
            print("experiment_status == ",experiment_status)
            

        else:
            print("yet not implemented")
            
        logging.info("modeling : RegressionClass : run_regression_model : execution end")


    