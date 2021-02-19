import numpy as np
import pandas as pd
import json
import mlflow
import mlflow.sklearn
import uuid 

from .linear_regressor_keras import LinearRegressorKerasClass 
from .linear_regressor_sklearn import LinearRegressorSklearnClass
from .model_experiment import ExperimentClass

def start_pipeline(**kwargs):
    mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow")
    print(" pipeline start ")
    
def linear_regression_sklearn(**kwargs):
    
    input_features_list = ['seq_id','house_size','bedrooms','bathrooms']
    target_features_list = ['seq_id','price']   
    
    
    scaled_df = pd.read_csv('./dags/src/models/house_prediction.csv')
    # scaled_df = pd.read_csv('student_results_prediction.csv')

    input_df= scaled_df[input_features_list]  # by using self.input_features_list. must include unique seq id
    target_df = scaled_df[target_features_list] 

    project_id = 1
    dataset_id = 1
    user_id = 1
    
    model_id = 1
    model_name = 'linear regression with sklearn'
    
    # Create an experiment name, which must be unique and case sensitive
    id = uuid.uuid1() 
    experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+str(dataset_id)
    
    ## Below Basic Parameter Changes Based On Model selected
    test_size = 0.20 # holdout
    random_state = 1
    cv = 5 # K-Fold Cross Validation 
    
    # create experiment 
    experiment_id = mlflow.create_experiment(experiment_name)
    # experiment = mlflow.get_experiment(experiment_id)
    
        # mlflow set_experiment and run the model.
    with mlflow.start_run(experiment_id=experiment_id) as run:
        ## Declare Object
        LRObject = LinearRegressorSklearnClass(input_df,target_df,test_size,random_state,cv)
        LRObject.run_pipeline()
    
    
    run_uuid = run.info.run_id
    experiment_id = experiment_id
    # Add Experiment 
    Model_Mode = 'auto'
    ExpObject = ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode)
    experiment_status = ExpObject.add_experiments()
    
    print("experiment_status == ",experiment_status)
    
   
    
def linear_regression_keras(**kwargs):
    
    input_features_list = ['seq_id','house_size','bedrooms','bathrooms']
    target_features_list = ['seq_id','price']   
    
    
    scaled_df = pd.read_csv('./dags/src/models/house_prediction.csv')
    # scaled_df = pd.read_csv('student_results_prediction.csv')

    input_df= scaled_df[input_features_list]  # by using self.input_features_list. must include unique seq id
    target_df = scaled_df[target_features_list] 

    project_id = 1
    dataset_id = 1
    user_id = 1
    
    model_id = 2
    model_name = 'linear regression with keras'
    
    # Create an experiment name, which must be unique and case sensitive
    id = uuid.uuid1() 
    experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+str(dataset_id)
    
    ## Below Basic Parameter Changes Based On Model selected
    test_size = 0.20 # holdout
    random_state = 1
    cv = 5 # K-Fold Cross Validation 
    
    # create experiment 
    experiment_id = mlflow.create_experiment(experiment_name)
    # experiment = mlflow.get_experiment(experiment_id)
    
        # mlflow set_experiment and run the model.
    with mlflow.start_run(experiment_id=experiment_id) as run:
        ## Declare Object
        LRObject = LinearRegressorKerasClass(input_df,target_df,test_size,random_state,cv)
        LRObject.run_pipeline()
    
    
    run_uuid = run.info.run_id
    experiment_id = experiment_id
    # Add Experiment 
    ExpObject = ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode)
    experiment_status = ExpObject.add_experiments()
    
    print("experiment_status == ",experiment_status)