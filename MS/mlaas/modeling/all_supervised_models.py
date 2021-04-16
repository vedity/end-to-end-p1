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


# Regression Class File Imports
from modeling.utils.model_utils.sklearn_regression.linear_regression import *
from modeling.utils.model_utils.sklearn_regression.ridge_regression import *
from modeling.utils.model_utils.sklearn_regression.lasso_regression import *
from modeling.utils.model_utils.sklearn_regression.elasticnet_regression import *
from modeling.utils.model_utils.keras_regression.linear_regression_keras import *
from modeling.utils.model_utils.sklearn_regression.kneighbors_regression import *
from modeling.utils.model_utils.sklearn_regression.decisiontree_regression import *
from modeling.utils.model_utils.sklearn_regression.randomforest_regression import *
from modeling.utils.model_utils.sklearn_regression.gradientboost_regression import *
from modeling.utils.model_utils.sklearn_regression.xgboost_regression import *


# Classification Class File Imports
from modeling.utils.model_utils.sklearn_classification.logistic_regression import *
from modeling.utils.model_utils.sklearn_classification.kneighbors_classification import *
from modeling.utils.model_utils.sklearn_classification.svm_classification import *
from modeling.utils.model_utils.sklearn_classification.decisiontree_classification import *
from modeling.utils.model_utils.sklearn_classification.naive_bayes_classification import *
from modeling.utils.model_utils.sklearn_classification.randomforest_classification import *
from modeling.utils.model_utils.sklearn_classification.gradientboost_classification import *
from modeling.utils.model_utils.sklearn_classification.xgboost_classification import *
from modeling.utils.model_utils.keras_classification.logistic_regression_keras import *



# Common Class File Imports
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


def get_supervised_models(model_type):
    
    sql_command = "select mmt.model_id,mmt.model_name,mmt.model_class_name,amp.hyperparam,mmt.algorithm_type from mlaas.model_master_tbl mmt,mlaas.auto_model_params amp "\
                  "where mmt.model_id=amp.model_id and mmt.model_type='"+ model_type +"' order by model_id"
                  
    model_df = DBObject.select_records(connection,sql_command)
    model_dict = model_df.to_dict(orient="list")

    return model_dict



def get_model_data(user_id, project_id, dataset_id):
    #TODO Optimize this.
    scaled_split_dict = SplitData().get_scaled_split_dict(DBObject,connection,project_id, dataset_id)
    
    X_train,X_valid,X_test,y_train,y_valid,y_test = SplitData().get_split_datasets(scaled_split_dict)
    
    input_features_list, target_features_list = SplitData().get_features_list(user_id, project_id, dataset_id, DBObject, connection)
    
    return input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict


def run_model(model_type, algorithm_type, y_train):

    if model_type == 'Classification':
        n_labels = len(np.unique(y_train[:, -1]))
        print("N_LABELS-----------", n_labels)
        if n_labels == 2:
            return 1
        elif n_labels > 2:
            if algorithm_type == 'Binary':
                print("ALGO TYPE BINARY")
                return 0
            elif algorithm_type == 'Multi':
                print("ALGO TYPE MULTIIIIIIIi")
                return 1

    elif model_type == 'Regression':
        print("MODEL TYPE MULTIIIIIIIi")
        return 1



def supervised_models(run_id,**kwargs):
        
    try:
        mlflow.set_tracking_uri("postgresql+psycopg2://{}:{}@{}:{}/{}?options=-csearch_path%3Ddbo,mlflow".format(user, password, host, port, database))
        
        model_param_dict = ast.literal_eval(kwargs['dag_run'].conf['model_param_dict'])
        project_id = int(model_param_dict['project_id'])
        dataset_id = int(model_param_dict['dataset_id'])
        user_id = int(model_param_dict['user_id'])

        input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict= get_model_data(user_id, project_id, dataset_id)
        
        if kwargs['model_mode'].lower() == 'manual':
            run_model_flag = 1
        else:
            run_model_flag = run_model(kwargs['model_type'], kwargs['algorithm_type'], y_train)

        if run_model_flag == 1:
            
            model_mode = model_param_dict['model_mode']
            
            model_id = kwargs['model_id']
            model_name = kwargs['model_name']
            model_class_name = kwargs['model_class_name']

            if model_mode.lower() == 'auto':
                hyperparameters = ast.literal_eval(kwargs['model_hyperparams'])
            else:
                hyperparameters = kwargs['model_hyperparams']
            
            experiment_name  = model_param_dict['experiment_name']
            
            # Create an experiment name, which must be unique and case sensitive
            ExpObject = model_experiment.ExperimentClass(DBObject, connection, connection_string)
            experiment, experiment_id = ExpObject.get_mlflow_experiment(experiment_name)
            # mlflow set_experiment and run the model.
            with mlflow.start_run(experiment_id=experiment_id) as run:
                # Get experiment id and run id from the experiment set.
                run_uuid = run.info.run_id
                experiment_id = experiment.experiment_id
                dag_run_id = run_id
                # Add experiment
                add_exp_status = ExpObject.add_experiments(experiment_id,experiment_name,run_uuid,
                                                            project_id,dataset_id,user_id,
                                                            model_id,model_mode,dag_run_id)
                
                
                
                # Declare Object
                LRObject = eval(model_class_name)(input_features_list, target_features_list, 
                                                                X_train, X_valid, X_test, y_train, y_valid, 
                                                                y_test, scaled_split_dict,hyperparameters)
                
                LRObject.run_pipeline()
                status = "success"
    except:
        status = "failed"
        
        ## Update Experiment ########
    finally:
        upd_exp_status = ExpObject.update_experiment(experiment_id,status)
        
        print("experiment_status == ",upd_exp_status)