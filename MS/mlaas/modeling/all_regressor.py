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
from modeling.utils.model_utils.sklearn_regression import linear_regressor
from modeling.utils.model_experiments import model_experiment
from modeling.split_data import SplitData
from common.utils.logger_handler import custom_logger as cl


# Global Variables And Objects
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')


DBObject=db.DBClass()     
connection,connection_string=DBObject.database_connection(database,user,password,host,port) 


def get_auto_model_param(user_id, project_id, dataset_id, dataset_split_dict):
    
    path="/usr/local/airflow/dags/scaled_dataset/my_data_num.npy"
    
    # scaled_path = SplitData().get_scaled_path(DBObject,connection,project_id)
    
    input_df, target_df = SplitData().get_scaled_data(path)
    
    input_features_list, target_features_list = SplitData().get_input_target_features_list(user_id, project_id, dataset_id, DBObject, connection)
    
    ################### Split Dataset #########################
    X_train,X_valid,X_test,y_train,y_valid,y_test = SplitData().get_split_data(input_df, target_df, random_state=dataset_split_dict['random_state'], 
                                            test_size=dataset_split_dict['test_size'], valid_size=dataset_split_dict['valid_size'], 
                                            split_method=dataset_split_dict['split_method'])
    
    return input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid

    
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
    
   
    

             
def linear_regression_sklearn(run_id,**kwargs):
        
        mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow?options=-csearch_path%3Ddbo,mlaas")
       
        #TODO Later On model id may be changed
       
        model_id = kwargs['model_id']
        model_mode = kwargs['dag_run'].conf['model_mode']
        project_id = int(kwargs['dag_run'].conf['project_id'])
        dataset_id = int(kwargs['dag_run'].conf['dataset_id'])
        user_id = int(kwargs['dag_run'].conf['user_id'])
        
        dataset_split_parameters = {"model_mode":model_mode}
        dataset_split_dict = SplitData().get_dataset_split_dict(dataset_split_parameters)
        input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid= get_auto_model_param(user_id, project_id, dataset_id, dataset_split_dict)
           
        # TODO : experiment name and experiment_desc coming from frontend.
        
        # Create an experiment name, which must be unique and case sensitive
        experiment_name = kwargs['dag_run'].conf['exp_name']
        
        
        # Get from database
        sql_command = "select nextval('unq_num_seq') as ids"
        counter = DBObject.select_records(connection, sql_command)
        print("counter==",counter)
        counter = counter['ids'][0]

        print("updated counter =",counter)
        
        id = uuid.uuid1().time 
        experiment_name = experiment_name.upper() + "_" + str(counter)
        
        # create experiment 
        experiment_id = mlflow.create_experiment(experiment_name)
        experiment = mlflow.get_experiment(experiment_id)
        # mlflow set_experiment and run the model.
        with mlflow.start_run(experiment_id=experiment_id) as run:
            # Get experiment id and run id from the experiment set.
            run_uuid = run.info.run_id
            experiment_id = experiment.experiment_id
            dag_run_id = run_id
            ################### Add Experiment ################################
            ExpObject = model_experiment.ExperimentClass(DBObject, connection, connection_string)
            add_exp_status = ExpObject.add_experiments(experiment_id,experiment_name,run_uuid,
                                                          project_id,dataset_id,user_id,
                                                          model_id,model_mode,dag_run_id)
            
            try:
                ## Declare Object
                LRObject = linear_regressor.LinearRegressionClass(input_features_list, target_features_list, 
                                                                X_train, X_valid, X_test, y_train, y_valid, 
                                                                y_test, dataset_split_dict)
                LRObject.run_pipeline()
                status = "success"
            except:
                status = "failed"
            
            ## Update Experiment ########
            upd_exp_status = ExpObject.update_experiment(experiment_id,status)
        
        print("experiment_status == ",upd_exp_status)
        
        
