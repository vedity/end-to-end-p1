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
  
    def regression_model(self,Model_Mode,input_features_list,target_features_list, X_train, X_valid, X_test, y_train, y_valid, y_test,
                    SplitDataObject, model_type, algorithm_type, DBObject, connection, connection_string, project_id,dataset_id,user_id):
        
        """This function is used to run regression type model.
        """
        logging.info("modeling : RegressionClass : regression_model : execution start")

        # Call private method of the current class .
        self.all_regression_model(Model_Mode,input_features_list,target_features_list,
                                  project_id,dataset_id,user_id,
                                  X_train, X_valid, X_test, y_train, y_valid, y_test, SplitDataObject, 
                                  model_type, algorithm_type, DBObject, connection, connection_string)
        
        logging.info("modeling : RegressionClass : regression_model : execution end")
    
    # This is for auto model run   
    def all_regression_model(self,Model_Mode,input_features_list,target_features_list, project_id,dataset_id,
                            user_id, X_train, X_valid, X_test, y_train, y_valid, y_test, SplitDataObject, model_type, algorithm_type, 
                            DBObject, connection, connection_string):
        
        """This function is used to run all regression type model.
        """
        logging.info("modeling : RegressionClass : all_regression_model : execution start")
        # it will set mlflow tracking uri where all the parameters and matrices gets stored experiment wise.
        mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow")
        
        # First Algorithm
        if algorithm_type == 'Single_Target':
            self.linear_regression_sklearn(Model_Mode,input_features_list,target_features_list,
                                project_id,dataset_id,user_id, X_train, X_valid, X_test, y_train, y_valid, y_test, 
                                SplitDataObject, DBObject, connection, connection_string)
        
        logging.info("modeling : RegressionClass : all_regression_model : execution end")
        
        # # Algorithm Second
        
        
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
            
            mlflow.set_tracking_uri("postgresql+psycopg2://airflow:airflow@postgresql:5432/airflow")
            
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


    def linear_regression_sklearn(self,Model_Mode,input_features_list,target_features_list,
                             project_id,dataset_id,user_id, X_train, X_valid, X_test, y_train, y_valid, y_test, SplitDataObject, 
                             DBObject, connection, connection_string):
        
        logging.info("modeling : RegressionClass : linear_regression_sklearn : execution start")
        ## TODO : we have to get class file also based on model type. 
        # Get model id and model name based on model type.
        model_id = 1
        # model_name = 'Linear_Regression_With_Sklearn'


        # split_data_object = SplitData(basic_split_parameters, model_id, DBObject, connection)
        # X_train, X_valid, X_test, Y_train, Y_valid, Y_test = split_data_object.get_split_data(input_df, target_df)

        # Create an experiment name, which must be unique and case sensitive
        exp_name = "my first"
        # Get from database
        sql_command = "select experiment_id from experiments order by experiment_id desc limit 1"
        # we use counter to associate a uniqueness to the experiment name.
        counter = DBObject.select_records(connection, sql_command).iloc[0, 0]
        if counter is None: # This is called when the user runs the model(clicks on start) for the first time.
            counter = 0
        else: # this is called when the user has already called the start model atleast once before.
            counter += 1
        
        id = uuid.uuid1() 
        # Used to assign a unique experiment name on the basis of model_mode, exp_name and counter.
        experiment_name = SplitDataObject.model_mode.upper()+"_"+exp_name.upper() + "_" + str(counter)
        
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
                                                            X_train, X_valid, X_test, y_train, y_valid, 
                                                            y_test, SplitDataObject)
            LRObject.run_pipeline() # Runs the Machine Learning pipeline, which trains the data.
        
        
        
        # Get experiment id and run id from the experiment set.
        run_uuid = run.info.run_id
        experiment_id = experiment.experiment_id
        
        # Add Experiment into database
        ExpObject = model_experiment.ExperimentClass(experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,Model_Mode, DBObject, connection, connection_string)
        experiment_status = ExpObject.add_experiments(DBObject, connection, connection_string)
        
        logging.info("modeling : RegressionClass : linear_regression_sklearn : execution end")
        
    
       
        print("experiment_status == ",experiment_status)


    def linear_regression_keras(self,Model_Mode,input_features_list,target_features_list, project_id,dataset_id,
                    user_id, X_train, X_valid, X_test, Y_train, Y_valid, Y_test, split_data_object, 
                    DBObject, connection, connection_string, model_type):
        
        ## TODO : we have to get class file also based on model type. 
        # Get model id and model name based on model type.
        model_id = 2
        # model_name = 'linear regression keras'
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
                 
            
    
    