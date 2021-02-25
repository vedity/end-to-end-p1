'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''

import pandas as pd
import numpy as np
import json
import ast 
import mlflow
import mlflow.sklearn
import uuid 
import logging
from database import *
from common.utils.database import db
from sklearn.model_selection import train_test_split
from modeling.utils.model_utils.sklearn_regression import linear_regressor
from modeling.utils.model_experiments import model_experiment
## Get Database Connection


# Get data dataset info
def get_dataset_ids(**kwargs):
    DBObject=db.DBClass()     
    connection,connection_string=DBObject.database_connection(database,user,password,host,port) 

    # get dataset,project,user ids
    sql_command = "select * from mlaas.model_dataset_tbl"

    model_dataset_df=DBObject.select_records(connection,sql_command)
    model_dataset_records=model_dataset_df.to_records(index=False)

    project_id,dataset_id,user_id = model_dataset_records[0]
    
    sql_command = "select scaled_data_table,input_features,target_features from mlaas.cleaned_ref_tbl where project_id =" + str(project_id) +" and dataset_id =" + str(dataset_id) + " and user_id =" + str(user_id)
    dataset_info_df=DBObject.select_records(connection,sql_command)
    dataset_info_records=dataset_info_df.to_records(index=False)
    
    scaled_data_table,input_features,target_features = dataset_info_records[0]
    input_features_list = ast.literal_eval(input_features)
    target_features_list = ast.literal_eval(target_features)
    
    print("scaled_data_table ",scaled_data_table)
    print("input_features ",input_features_list)
    print("target_features ",target_features_list)
    
    ############## Get Scaled Data ##############
    sql_command = "select * from mlaas."+scaled_data_table
    scaled_df=DBObject.select_records(connection,sql_command)
    print("scaled_df ==",type(scaled_df))
    input_df = scaled_df[input_features_list]
    target_df = scaled_df[target_features_list]
    
    print("input df shape ==",input_df.shape)
    print("output df shape ==",target_df.shape)
    
    ################## Get Basic Split Parameter ##########
    sql_command = "select * from mlaas.auto_model_split_param_tbl"
    split_data_df=DBObject.select_records(connection,sql_command)
    split_param = split_data_df['split_param'][0]
    
    split_param_dict = ast.literal_eval(split_param)
    
    print("dataset split param ==",split_param_dict)
    print("param type ==",type(split_param_dict))
    # print(kwargs['conf'])
    
    ################### Split Dataset #########################
    X_train, X_test, y_train, y_test = train_test_split(input_df, target_df, test_size=split_param_dict['test_size'],
                                                                random_state=split_param_dict['random_state'])
    
    
    print("X train shape ==",X_train.shape)
    print("X test shape ==",X_test.shape)
    print("y train shape ==",y_train.shape)
    print("y test shape ==",y_test.shape)
    
    
    ################## #############################################
    
################### Regression Pipeline Code
def start_pipeline(**kwargs):
    print("regressor pipeline start")
        
def linear_regression_sklearn(**kwargs):
        
        mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow?options=-csearch_path%3Ddbo,mlaas")
        # mlflow.set_tracking_uri("./")
        #TODO Later On model id may be changed
        model_id = kwargs['model_id']
        model_mode = kwargs['model_mode']
        
        input_features_list,target_features_list = kwargs['input_features_list'],kwargs['target_features_list']
        
        project_id,dataset_id,user_id = int(kwargs['project_id']),int(kwargs['dataset_id']),int(kwargs['user_id'])
        
        X_train, X_valid, X_test = kwargs['X_train'],kwargs['X_valid'],kwargs['X_test']
        y_train, y_valid, y_test = kwargs['y_train'],kwargs['y_valid'],kwargs['y_test']
        SplitDataObject = kwargs['SplitDataObject']
        DBObject = kwargs['DBObject']
        connection, connection_string = kwargs['connection'],kwargs['connection_string']
        
        
        # Create an experiment name, which must be unique and case sensitive
        experiment_name = "house_prediction"
        
        print(model_id)
        print(model_mode)
        print(input_features_list,target_features_list)
        print(project_id,dataset_id,user_id)
        print(X_train, X_valid, X_test)
        print(y_train, y_valid, y_test)
        print(SplitDataObject)
        print(DBObject)
        print(connection, connection_string)
        
        # Get from database
        sql_command = "select experiment_id from mlaas.experiments order by experiment_id desc limit 1"
        counter = DBObject.select_records(connection, sql_command)
        print("counter==",counter)
        if counter is None:
            counter = 1
        else:
            counter = counter['experiment_id'][0]
            counter += 1
        
        print("c=",counter)
        id = uuid.uuid1().time 
        
        experiment_name = model_mode.upper() + "_" + experiment_name.upper() + "_" + str(id)
        # create experiment 
        experiment_id = mlflow.create_experiment(experiment_name)
        experiment = mlflow.get_experiment(experiment_id)
        
        # mlflow set_experiment and run the model.
        with mlflow.start_run(experiment_id=experiment_id) as run:
            ## Declare Object
            LRObject = linear_regressor.LinearRegressionClass(input_features_list, target_features_list, 
                                                            X_train, X_valid, X_test, y_train, y_valid, 
                                                            y_test, SplitDataObject)
            LRObject.run_pipeline()
        
        
        
        # Get experiment id and run id from the experiment set.
        run_uuid = run.info.run_id
        experiment_id = experiment.experiment_id

        # Add Experiment into database
        ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,model_mode)
        # print(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,model_mode)
        # print(type(experiment_id),type(experiment_name),type(run_uuid),type(int(project_id)),type(int(dataset_id)),type(int(user_id)),type(model_id),type(model_mode))
        experiment_status = ExpObject.add_experiments(DBObject, connection, connection_string)
        print("experiment_status == ",experiment_status)
        
        
############# Delete Below Code ################################
def get_auto_model_param():
    
    DBObject=db.DBClass()     
    connection,connection_string=DBObject.database_connection(database,user,password,host,port) 

    # get dataset,project,user ids
    sql_command = "select * from mlaas.model_dataset_tbl"

    model_dataset_df=DBObject.select_records(connection,sql_command)
    model_dataset_records=model_dataset_df.to_records(index=False)

    project_id,dataset_id,user_id = model_dataset_records[0]
    
    sql_command = "select scaled_data_table,input_features,target_features from mlaas.cleaned_ref_tbl where project_id =" + str(project_id) +" and dataset_id =" + str(dataset_id) + " and user_id =" + str(user_id)
    dataset_info_df=DBObject.select_records(connection,sql_command)
    dataset_info_records=dataset_info_df.to_records(index=False)
    
    scaled_data_table,input_features,target_features = dataset_info_records[0]
    input_features_list = ast.literal_eval(input_features)
    target_features_list = ast.literal_eval(target_features)
    ############## Get Scaled Data ##############
    sql_command = "select * from mlaas."+scaled_data_table
    scaled_df=DBObject.select_records(connection,sql_command)
    
    input_df = scaled_df[input_features_list]
    target_df = scaled_df[target_features_list]
    ################## Get Basic Split Parameter ##########
    sql_command = "select * from mlaas.auto_model_split_param_tbl"
    split_data_df=DBObject.select_records(connection,sql_command)
    split_param = split_data_df['split_param'][0]
    
    split_param_dict = ast.literal_eval(split_param)
    
    ################### Split Dataset #########################
    X_train, X_test, y_train, y_test = train_test_split(input_df, target_df, test_size=split_param_dict['test_size'],
                                                                random_state=split_param_dict['random_state'])
    
    
    
    
    return input_features_list,target_features_list,project_id,dataset_id,user_id,X_train,X_test, y_train, y_test,DBObject,connection,connection_string





