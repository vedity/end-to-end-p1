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

from ...model_utils.sklearn_classification import logistic_classifier
from ...model_experiments import model_experiment

class ProbabilisticClass:
    
    def classification_model(self,Model_Mode,
                         input_features_list,
                         target_features_list,
                         input_df,
                         target_df,
                         project_id,
                         dataset_id,
                         user_id):
        
        model_type = 'Classification Model'
        
        print("This is classification type problem")
        
        print("******************** IN Probilistic Class  ***************************")
        
        
        print("model mode ==",Model_Mode)
        print("input features  ==",input_features_list) 
        print("target features  ==",target_features_list) 
        print(" project id ==",project_id)
        print("dataset id ==",dataset_id)
        print("user id ==",user_id)
        print("input df ==",input_df.head())
        print("target df  ==",target_df.head())
        print("model type ==",model_type)
        
        
        self.all_classification_model(Model_Mode,
                                    input_features_list,
                                    target_features_list,
                                    project_id,
                                    dataset_id,
                                    user_id,
                                    input_df,
                                    target_df,
                                    model_type)
            
    # This is for auto model run   
    def all_classification_model(self,Model_Mode,
                             input_features_list,
                             target_features_list,
                             project_id,
                             dataset_id,
                             user_id,
                             input_df,
                             target_df,
                             model_type):
        
        print("Model Running in auto mode ")
        mlflow.set_tracking_uri("postgresql+psycopg2://postgres:admin@postgresql:5432/postgres")
        
        model_id = 2
        model_name = 'logistic classifier'
        
        id = uuid.uuid1() 
        experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+str(dataset_id)
         
        ## Below Basic Parameter Changes Based On Model
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
        
        
    # This is for manually model run    
    def run_classification_model(self,model_id,model_name,model_type,model_parameters,Model_Mode,
                             input_features_list,target_features_list,
                             input_df,target_df,
                             project_id,dataset_id,user_id):
        
        if model_name == 'logistic classifier' :
            
            mlflow.set_tracking_uri("postgresql+psycopg2://postgres:admin@postgresql:5432/postgres")
            
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
        
        
        