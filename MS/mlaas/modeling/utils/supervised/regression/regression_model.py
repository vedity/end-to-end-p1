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
from ...model_utils.sklearn_regression import linear_regressor
from ...model_experiments import model_experiment
from sklearn.model_selection import train_test_split

class RegressionClass:

  
    def regression_model(self,Model_Mode,input_features_list,target_features_list, X_train, X_valid, 
                    X_test, Y_train, Y_valid, Y_test,split_data_object, DBObject, connection, connection_string,
                         project_id,dataset_id,user_id):
        
        """This function is used to run regression type model.
        """
        
        model_type = 'Regression_Model'
        
        print("******************** IN Regression Class  ***************************")
        
        # Call private method of the current class .
        self.all_regression_model(Model_Mode,input_features_list,target_features_list, project_id,dataset_id,
                user_id, X_train, X_valid, X_test, Y_train, Y_valid, Y_test, split_data_object, 
                DBObject, connection, connection_string, model_type)
    
    # This is for auto model run   
    def all_regression_model(self,Model_Mode,input_features_list,target_features_list, project_id,dataset_id,
                            user_id, X_train, X_valid, X_test, Y_train, Y_valid, Y_test, split_data_object, 
                            DBObject, connection, connection_string, model_type):
        
        """This function is used to run all regression type model.
        """
        
        
        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        mlflow.set_tracking_uri("postgresql+psycopg2://postgres:admin@postgresql:5432/postgres")
        
        # Algorithm First
        self.linear_regression_sklearn(Model_Mode,input_features_list,target_features_list,
                             project_id,dataset_id,user_id, X_train, X_valid, X_test, Y_train, Y_valid, 
                             Y_test, split_data_object, DBObject, connection, connection_string, model_type)
        
        # # Algorithm Second
        # self.linear_regression_keras(Model_Mode,input_features_list,target_features_list,
        #                      project_id,dataset_id,user_id,
        #                      X_train, X_valid, X_test, Y_train, Y_valid, Y_test,split_data_object, model_type)
        


   

    # This is for manually model run    
    def run_regression_model(self,model_id,model_name,model_type,Model_Mode,
                             input_features_list,target_features_list,
                             X_train, X_valid, X_test, Y_train, Y_valid, Y_test,split_data_object,
                             DBObject, connection, connection_string, project_id,dataset_id,user_id):
        
        """This function is used to run model directly when model mode is in manual.
           it will run model based on model name or id and model type.
        
        """

        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        if model_name == 'linear regression':
            
            mlflow.set_tracking_uri("postgresql+psycopg2://postgres:admin@postgresql:5432/postgres")
            
            # TODO : we will used parameter class will take these parameters  from users.
            # Get model id and model name and model type from the user.
            model_id = 1
            model_name = 'linear regression'
            
            # Create an experiment name, which must be unique and case sensitive
            id = uuid.uuid1() 
            experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+str(dataset_id)
            
            ## Below Basic Parameter Changes Based On Model selected
            # test_size = 0.20 # holdout
            # random_state = 1 # Get from REST API
            # cv = 5 # K-Fold Cross Validation 
            
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


    def linear_regression_sklearn(self,Model_Mode,input_features_list,target_features_list,
                             project_id,dataset_id,user_id, X_train, X_valid, X_test, Y_train, Y_valid, 
                             Y_test, split_data_object, DBObject, connection, connection_string, model_type):
        
        ## TODO : we have to get class file also based on model type. 
        # Get model id and model name based on model type.
        model_id = 1
        model_name = 'linear regression sklearn'
        # Create an experiment name, which must be unique and case sensitive
        id = uuid.uuid1() 
        experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+'_'+str(dataset_id)
         
        ## Below Basic Parameter Changes Based On Model
        # test_size = 0.20 # holdout
        # random_state = 1
        # cv = 5 # K-Fold Cross Validation 
        
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
        
        
        
        # Get experiment id and run id from the experiment set.
        run_uuid = run.info.run_id
        experiment_id = experiment.experiment_id
        
        # Add Experiment into database
        ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode, DBObject, connection, connection_string)
        experiment_status = ExpObject.add_experiments(DBObject, connection, connection_string)
        
        print("experiment_status == ",experiment_status)
    
    def linear_regression_keras(self,Model_Mode,input_features_list,target_features_list, project_id,dataset_id,
                    user_id, X_train, X_valid, X_test, Y_train, Y_valid, Y_test, split_data_object, 
                    DBObject, connection, connection_string, model_type):
        
        ## TODO : we have to get class file also based on model type. 
        # Get model id and model name based on model type.
        model_id = 2
        model_name = 'linear regression keras'
        # Create an experiment name, which must be unique and case sensitive
        id = uuid.uuid1() 
        experiment_name = "EXP_"+ str(id.time)+"_"+str(project_id)+'_'+str(dataset_id)
         
        ## Below Basic Parameter Changes Based On Model
        test_size = 0.20 # holdout
        random_state = 1
        cv = 5 # K-Fold Cross Validation 
        
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
        
        
        
        # Get experiment id and run id from the experiment set.
        run_uuid = run.info.run_id
        experiment_id = experiment.experiment_id
        
        # Add Experiment into database
        ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode, DBObject, connection, connection_string)
        experiment_status = ExpObject.add_experiments(DBObject, connection, connection_string)
        
        print("experiment_status == ",experiment_status)
                 
            
    
        