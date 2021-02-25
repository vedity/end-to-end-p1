'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''
import pandas as pd
import json
import re
import logging
import traceback
import datetime
from .regression.regression_model import RegressionClass as RC
from .classification.classification_model import ProbabilisticClass as PC
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')

class SupervisedClass(RC,PC):
    

    def supervised_algorithm(self,Model_Mode,input_features_list,target_features_list,
                             input_df,target_df, SplitDataObject, model_type, algorithm_type, DBObject, connection, 
                             connection_string, project_id,dataset_id,user_id):
        
        """This function is used to call supervised algorithm.
        """
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution start")
    
        # reg_type = 0
        # cls_type = 0
        
        # for i in range(1,len(target_df.columns)):
        #     Total_Length = len(target_df.iloc[:,i])
        #     Unq_Length = len(target_df.iloc[:,i].unique())
            
        #     Thresh_Hold = int((Total_Length * 10) / 100)
            
        #     if Thresh_Hold < Unq_Length :
        #         reg_type = 1
        #     else:
        #         cls_type = 1

        # It will check whether target is regressor or classifier.
        X_train, X_valid, X_test, y_train, y_valid, y_test = SplitDataObject.get_split_data(input_df, target_df)
        
        if model_type == "Regression" :
            # Call Regression Class's method
            super(SupervisedClass,self).regression_model(Model_Mode,
                                                        input_features_list,
                                                        target_features_list,
                                                        X_train, 
                                                        X_valid,
                                                        X_test, 
                                                        y_train, 
                                                        y_valid, 
                                                        y_test,
                                                        SplitDataObject,
                                                        model_type,
                                                        algorithm_type,
                                                        DBObject, 
                                                        connection, 
                                                        connection_string,
                                                        project_id,
                                                        dataset_id,
                                                        user_id)
                
                                                
        elif model_type == "Classification" :
            
            # Call Probabilistic Class's method
            super(SupervisedClass,self).classification_model(Model_Mode,
                                                         input_features_list,
                                                         target_features_list,
                                                         X_train, 
                                                         X_valid,
                                                         X_test, 
                                                         y_train, 
                                                         y_valid, 
                                                         y_test,
                                                         SplitDataObject, 
                                                         DBObject, 
                                                         connection, 
                                                         connection_string,
                                                         project_id,
                                                         dataset_id,
                                                         user_id)
        
        else:
            print("please select appropriate target")
            
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution end")
        
        
    def run_regression_model(self,model_id,model_name,model_type,Model_Mode, input_features_list,
                target_features_list,input_df,target_df,split_data_object, DBObject, connection, 
                connection_string,project_id,dataset_id,user_id):
        
        """This function is used to run model when it is in manual mode.

        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            model_parameters ([dict]): [parameters for the model.]
            Model_Mode ([type]): [mode of the model.]
            input_features_list ([list]): [input features list]
            target_features_list ([list]): [target features list]
            input_df ([dataframe]): [input features dataframe.]
            target_df ([dataframe]): [target features dataframe.]
            project_id ([integer]): [unique id of the project.]
            dataset_id ([integer]): [unique id of the dataset.]
            user_id ([integer]): [unique id of the user.]
        """
        logging.info("modeling : SupervisedClass : run_regression_model : execution start") 
        # Call the super class method.
        X_train, X_valid, X_test, Y_train, Y_valid, Y_test = split_data_object.get_split_data(input_df, target_df)
        super(SupervisedClass,self).run_regression_model(model_id,model_name,model_type,
                                                        Model_Mode, input_features_list, target_features_list, 
                                                        X_train, X_valid, X_test, Y_train, Y_valid, Y_test, split_data_object,
                                                        project_id,dataset_id,user_id)
        
        logging.info("modeling : SupervisedClass : run_regression_model : execution end") 
         
         
        
    def run_classification_model(self,model_id,model_name,model_type,Model_Mode,input_features_list,
                target_features_list,input_df,target_df,split_data_object,DBObject, connection, 
                connection_string,project_id,dataset_id,user_id):
        
        """This function is used to run model when it is in manual mode.

        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            model_parameters ([dict]): [parameters for the model.]
            Model_Mode ([type]): [mode of the model.]
            input_features_list ([list]): [input features list]
            target_features_list ([list]): [target features list]
            input_df ([dataframe]): [input features dataframe.]
            target_df ([dataframe]): [target features dataframe.]
            project_id ([integer]): [unique id of the project.]
            dataset_id ([integer]): [unique id of the dataset.]
            user_id ([integer]): [unique id of the user.]
        """
        logging.info("modeling : SupervisedClass : run_classification_model : execution start") 
        # Call super class's method.
        X_train, X_valid, X_test, Y_train, Y_valid, Y_test = split_data_object.get_split_data(input_df, target_df)
        super(SupervisedClass,self).run_classification_model(model_id,model_name,model_type,split_data_object,
                                                          Model_Mode,input_features_list,target_features_list,
                                                          X_train, X_valid, X_test, Y_train, Y_valid, Y_test,
                                                          project_id,dataset_id,user_id)
        
        logging.info("modeling : SupervisedClass : run_classification_model : execution end") 
         
         
        
        
        
   
    