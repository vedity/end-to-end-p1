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


def get_regression_models():
    sql_command = "select model_id,model_name from mlaas.model_master_tbl where model_type='Regression'"
    model_df = DBObject.select_records(connection,sql_command)
    model_dict = model_df.to_dict(orient="list")
    return model_dict


def get_model_data(user_id, project_id, dataset_id):
    #TODO Optimize this.
    scaled_split_dict = SplitData().get_scaled_split_dict(DBObject,connection,project_id, dataset_id)
    
    X_train,X_valid,X_test,y_train,y_valid,y_test = SplitData().get_split_datasets(scaled_split_dict)
    
    input_features_list, target_features_list = SplitData().get_features_list(user_id, project_id, dataset_id, DBObject, connection)
    
    return input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict

             
def linear_regression_sklearn(run_id,**kwargs):
        
        try:
            mlflow.set_tracking_uri("postgresql+psycopg2://{}:{}@{}:{}/{}?options=-csearch_path%3Ddbo,mlflow".format(user, password, host, port, database))
        
            model_id = kwargs['model_id']
            
            model_param_dict = ast.literal_eval(kwargs['dag_run'].conf['model_param_dict'])
        
            model_mode = model_param_dict['model_mode']
            project_id = int(model_param_dict['project_id'])
            dataset_id = int(model_param_dict['dataset_id'])
            user_id = int(model_param_dict['user_id'])
            experiment_name  = model_param_dict['experiment_name']
            
            input_features_list, target_features_list, X_train, X_test, X_valid, y_train, y_test, y_valid, scaled_split_dict= get_model_data(user_id, project_id, dataset_id)
            
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
                LRObject = linear_regressor.LinearRegressionClass(input_features_list, target_features_list, 
                                                                X_train, X_valid, X_test, y_train, y_valid, 
                                                                y_test, scaled_split_dict)
                LRObject.run_pipeline()
                status = "success"
        except:
            status = "failed"
            
            ## Update Experiment ########
        finally:
            upd_exp_status = ExpObject.update_experiment(experiment_id,status)
        
        print("experiment_status == ",upd_exp_status)
        
        
        

        
        


        
