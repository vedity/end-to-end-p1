'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0         Initial Version 
 Mann Purohit         02-FEB-2021           1.1         

*/
'''

import pandas as pd
import numpy as np
import json
import ast 
import logging
import mlflow
import mlflow.sklearn
import uuid 
import logging
import sys
import os
from database import *
from common.utils.database import db

from sklearn.model_selection import train_test_split
from modeling.utils.model_utils.sklearn_classification import logistic_classifier
from modeling.utils.model_experiments import model_experiment
from modeling.split_data import SplitData
from common.utils.logger_handler import custom_logger as cl


# Global Variables And Objects
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('all_classfier')


DBObject=db.DBClass()     
connection,connection_string=DBObject.database_connection(database,user,password,host,port) 


def get_classification_models():
    sql_command = "select model_id,model_name from mlaas.model_master_tbl where model_type='Classification'"
    model_df = DBObject.select_records(connection,sql_command)
    model_dict = model_df.to_dict(orient="list")
    return model_dict



def get_model_data(user_id, project_id, dataset_id):
    #TODO Optimize this.
    scaled_split_dict = SplitData().get_scaled_split_dict(DBObject,connection,project_id, dataset_id)
    
    X_train,X_valid,X_test,y_train,y_valid,y_test = SplitData().get_split_datasets(scaled_split_dict)
    
    input_features_list, target_features_list = SplitData().get_features_list(user_id, project_id, dataset_id, DBObject, connection)
    
    return input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict



######################################## Regression Pipeline Code ###################################################

def start_pipeline(dag,run_id,execution_date,ds,**kwargs):
    print("regressor pipeline start")

    model_mode = kwargs['dag_run'].conf['model_mode']
    dag_id = dag.dag_id
    project_id = int(kwargs['dag_run'].conf['project_id'])
    dataset_id = int(kwargs['dag_run'].conf['dataset_id'])
    user_id = int(kwargs['dag_run'].conf['user_id'])
    exp_name  = kwargs['dag_run'].conf['exp_name']
    
    table_name='mlaas.model_dags_tbl'
    cols = 'dag_id,exp_name,run_id,execution_date,project_id,dataset_id,user_id,model_mode' 
        
    row = dag_id,exp_name ,run_id,execution_date,project_id,dataset_id,user_id,model_mode    
    row_tuples = [tuple(row)]
    
    dag_status = DBObject.insert_records(connection,table_name,row_tuples,cols)
    print("dag status ==",dag_status)
    


             
def logistic_regression_sklearn(run_id,**kwargs):
        
        mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow?options=-csearch_path%3Ddbo,mlaas")
       
        #TODO Later On model id may be changed
     
        model_mode = kwargs['model_mode']
        model_id = kwargs['model_id']
        if model_mode == 'Auto':
            project_id = int(kwargs['dag_run'].conf['project_id'])
            dataset_id = int(kwargs['dag_run'].conf['dataset_id'])
            user_id = int(kwargs['dag_run'].conf['user_id'])
            experiment_name = kwargs['dag_run'].conf['exp_name']
 
        else:
            project_id = kwargs['project_id']
            dataset_id = kwargs['dataset_id']
            user_id = kwargs['user_id']
            experiment_name = kwargs['exp_name']
        
        input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict= get_model_data(user_id, project_id, dataset_id)
           
        # TODO : experiment name and experiment_desc coming from frontend.
        
        # Create an experiment name, which must be unique and case sensitive
        # experiment_name = kwargs['dag_run'].conf['exp_name']
        ExpObject = model_experiment.ExperimentClass(DBObject, connection, connection_string)
        experiment, experiment_id = ExpObject.get_mlflow_experiment(experiment_name)
        # mlflow set_experiment and run the model.
        with mlflow.start_run(experiment_id=experiment_id) as run:
            # Get experiment id and run id from the experiment set.
            run_uuid = run.info.run_id
            experiment_id = experiment.experiment_id
            dag_run_id = run_id
            ################### Add Experiment ################################
            
            add_exp_status = ExpObject.add_experiments(experiment_id,experiment_name,run_uuid,
                                                          project_id,dataset_id,user_id,
                                                          model_id,model_mode,dag_run_id)
            
            try:
                ## Declare Object
                LCObject = logistic_classifier.LogisticClassifierClass(input_features_list, target_features_list, X_train, X_test, X_valid,
                                                        y_train, y_test, y_valid, scaled_split_dict)
                LCObject.run_pipeline()
                status = "success"
            except:
                status = "failed"
                
            ## Update Experiment ########
            upd_exp_status = ExpObject.update_experiment(experiment_id,status)
        
        print("experiment_status == ",upd_exp_status)
        
        

def manual_algorithm_identifier(run_id, **kwargs):
    
    model_name = kwargs['dag_run'].conf['model_name']
    model_mode = kwargs['model_mode']
    project_id = int(kwargs['dag_run'].conf['project_id'])
    dataset_id = int(kwargs['dag_run'].conf['dataset_id'])
    user_id = int(kwargs['dag_run'].conf['user_id'])
    exp_name = kwargs['dag_run'].conf['exp_name']
    model_id = int(kwargs['dag_run'].conf['model_id'])
 
    if model_id == 4:
        logistic_regression_sklearn(run_id, user_id=user_id, project_id=project_id, dataset_id=dataset_id, exp_name=exp_name, 
                            model_mode=model_mode, model_id=model_id)
        
        


        
