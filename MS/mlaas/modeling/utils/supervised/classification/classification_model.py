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

from ...model_utils.sklearn_classification import logistic_classifier
from ...model_experiments import model_experiment
from common.utils.logger_handler import custom_logger as cl


user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('classification_model')

class ProbabilisticClass:
    
    def classification_model(self,Model_Mode, user_id, project_id, dataset_id,
                            model_type, algorithm_type,target_type,DBObject,connection,experiment_name,experiment_desc):
        
        print("This is classification type problem")
        logging.info("modeling : RegressionClass : classification_model : execution start")
        
        print("******************** IN Probilistic Class  ***************************")
        
        
        self.all_classification_model(Model_Mode, user_id, project_id, dataset_id,
                                    model_type, algorithm_type,target_type,DBObject,connection,experiment_name,experiment_desc)
            
    # This is for auto model run   
    def all_classification_model(self,Model_Mode, user_id, project_id, dataset_id,
                                model_type, algorithm_type,target_type,DBObject,connection,experiment_name,experiment_desc):
        
        
        logging.info("modeling : ClassificationClass : all_classification_model : execution start")

        if target_type == 'Single_Target':
            
            json_data = {'conf':'{"model_mode":"Auto","project_id":'+str(project_id)+',"dataset_id":'+str(dataset_id)+',"exp_name":"'+experiment_name+'","exp_desc":"'+experiment_desc+'","user_id":'+str(user_id)+'}'}
            
            logging.info("modeling : RegressionClass : all_classification_model : execution"+str(json_data))
            
            result = requests.post("http://airflow:8080/api/experimental/dags/auto_classification_pipeline/dag_runs",data=json.dumps(json_data),verify=False)#owner
            
        else:
            print("yet not tested")
            
        logging.info("modeling : ClassificationClass : all_classification_model : execution end")
        
        
    # This is for manually model run    
    def run_classification_model(self,model_id,model_name,model_type,model_parameters,Model_Mode,
                             input_features_list,target_features_list,
                             input_df,target_df,
                             project_id,dataset_id,user_id):
        
        if model_name == 'logistic classifier' :
            
            mlflow.set_tracking_uri("postgresql+psycopg2://postgres:admin@postgresql:5432/postgres?options=-csearch_path%3Ddbo,mlaas")
            
            # model_id = 1
            # model_name = 'linear regression'
            id = uuid.uuid1() 
            experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+str(dataset_id)
            
            ## Below Basic Parameter Changes Based On Model selected
            test_size = 0.20 # holdout
            random_state = 1
            cv = 5 # K-Fold Cross Validation 
            # create experiment 
            experiment_id = mlflow.create_experiment(experiment_name)
            experiment = mlflow.get_experiment(experiment_id)
            # mlflow.set_experiment(experiment_name)
            with mlflow.start_run(experiment_id=experiment_id) as run:
                ## Declare Object
                LCObject = logistic_classifier.LogisticClassifierClass(input_df,target_df,test_size,random_state,cv)
                LCObject.run_pipeline()
            
            # Create an experiment name, which must be unique and case sensitive
            run_uuid = run.info.run_id
            experiment_id = experiment.experiment_id
            # Add Experiment 
            ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode)
            experiment_status = ExpObject.add_experiments()
            print("experiment_status == ",experiment_status)
            
        else:
            
            print("yet not implemented")
        
        
        