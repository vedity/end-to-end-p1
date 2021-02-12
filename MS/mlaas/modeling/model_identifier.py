'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''


import pandas as pd
import json
import re
import logging
import traceback
import datetime
from .utils.supervised.supervised_model import SupervisedClass as SC
from .utils.model_experiments.model_experiment import ExperimentClass as EC
# from utils.unsupervised.unsupervised_model import UnSupervisedClass as USC
from .split_data import SplitData
from common.utils.database import db
from .algorithm_detector import AlgorithmDetector

class ModelClass(SC, EC, SplitData):
    
    def __init__(self,Model_Mode = None,input_features_list=None,target_features_list=None,
                 project_id = None,dataset_id = None, user_id = None, DBObject=None,
                 connection=None,connection_string=None):
        
        """This is used to initialise the basic input parameter for the model. 
        """
        print('ModelClass:- ', input_features_list)
        self.Model_Mode = Model_Mode
        self.input_features_list = input_features_list
        self.target_features_list = target_features_list
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.user_id = user_id
        # self.split_data_object 
        self.DBObject, self.connection, self.connection_string = DBObject,connection,connection_string
        # self.algorithm_type, self.model_type = self.get_model_type(self.get_scaled_data()[1])
        self.algorithm_detector = AlgorithmDetector(self.get_scaled_data()[1], self.DBObject, self.connection)


    def algorithm_identifier(self,split_data_object):
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        if len(self.target_features_list) > 0:
             # call  supervised class
            self.supervised_algorithm(split_data_object)
            
        else:
            # call  unsupervised class
            self.unsupervised_algorithm()
           
            
    
        # Get Model Id,Model Name and Model Hyper Parameter
        
    def run_model(self,model_id,model_name,model_type, split_data_object):
        """This function is used to run model when model mode is in manual. 

        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        
        # Get scaled data
        input_df,target_df = self.get_scaled_data()
        
        # check whether model type is regression or classification.
        if model_type == 'Regression_Model':
            # call the super class (SupervisedClass) method's. 
            super(ModelClass,self).run_regression_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       split_data_object,
                                                       self.DBObject, 
                                                       self.connection, 
                                                       self.connection_string,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)
            
            
        else:
            # call the super class (SupervisedClass) method's. 
            super(ModelClass,self).run_classification_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       split_data_object,
                                                       self.DBObject, 
                                                       self.connection, 
                                                       self.connection_string,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)

    
    def supervised_algorithm(self,split_data_object):
        """This function is used to call supervised algorithm.
        """
        
        # Get scaled data
        input_df,target_df = self.get_scaled_data()
         
        print("******************** IN Model Identifier Class ***************************") 
        
        # call the super class (SupervisedClass) method's.                                                                                                                            
        super(ModelClass,self).supervised_algorithm(self.Model_Mode,
                                                    self.input_features_list,
                                                    self.target_features_list,
                                                    input_df,
                                                    target_df,
                                                    split_data_object,
                                                    self.DBObject, 
                                                    self.connection, 
                                                    self.connection_string,
                                                    self.project_id,
                                                    self.dataset_id,
                                                    self.user_id)
        
        
    
    def unsupervised_algorithm(self):
        """This function is used to call unsupervised algorithm.
        """
        # Get Scaled Data
        input_df,_ = self.get_scaled_data()
        print("yet not implemented")
    
    
    def split_dataset(self, basic_split_parameters):
        '''
        Input: split_dataset, a dictionary which contains key value pairs where keys are the train,test,
        validation ratios, split_method and cv value.
            
        This function creates an object of the Class SplitData and returns this object.
        '''
        split_data_object = SplitData(basic_split_parameters) 
        return split_data_object


    def get_dataset_info(self):
       

        sql_command = 'select project_name from mlaas.project_tbl where project_id = ' + str(self.project_id)
        project_df = self.DBObject.select_records(self.connection, sql_command)
        project_name = project_df['project_name'][0]

        sql_command = 'select dataset_name from mlaas.dataset_tbl where dataset_id = ' + str(self.dataset_id)
        dataset_df = self.DBObject.select_records(self.connection, sql_command)
        dataset_name = dataset_df['dataset_name'][0]

        target_columns = self.target_features_list

        return project_name, dataset_name, target_columns[1:]


    def get_scaled_data(self):
        dataset_name_command = 'select scaled_data_table from mlaas.cleaned_ref_tbl where dataset_id = ' + str(self.dataset_id)
        dataset_table_name = self.DBObject.select_records(self.connection, dataset_name_command)['scaled_data_table'][0]

        scaled_df_get_command = 'select * from ' +'mlaas.' + dataset_table_name# doubt 
        scaled_df = self.DBObject.select_records(self.connection, scaled_df_get_command)
        print('get_scaled_data:- ', self.target_features_list)
        input_features_df= scaled_df[self.input_features_list]  # by using self.input_features_list. must include unique seq id
        target_features_df = scaled_df[self.target_features_list]  # by using self.target_features_list .must include unique seq id
        return input_features_df,target_features_df

    
    def get_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        # algorithm_type = None
        # model_type = None
        # if len(target_df) == 0: 
        #     algorithm_type = 'unsupervised'
        #     return algorithm_type, model_type
        # else:
        #     target_shape = target_df.shape
        #     if target_shape[1] == 2:
        #         algorithm_type = 'Single_target'
        #     elif target_shape[1] > 2:
        #         algorithm_type = 'Multi_target'
        #     total_length = target_shape[0]
        #     unq_length = len(target_df.iloc[:,1].unique())

        #     threshold = int((total_length * 20) / 100)

        #     if threshold < unq_length :
        #         model_type = 'Regression'
        #     else:
        #         if unq_length == 2:
        #             model_type = 'Binary_Classification'
        #         elif unq_length > 2:
        #             model_type = 'MultiClass_Classification'
        #     return algorithm_type, model_type
        return self.algorithm_detector.get_model_types()

    def show_model_list(self):
        # DBObject, connection, _ = self.get_db_connection()
        # sql_command = 'select * from model_master where model_type='+self.model_type+' and algorithm_type='+self.algorithm_type
        # return DBObject.select_records(connection, sql_command)
        models_list = self.algorithm_detector.show_models_list()
        return models_list

    def get_hyperparameters_list(self, model_name):
        hyperparameters_list = self.algorithm_detector.get_hyperparameters_list(model_name)
        return hyperparameters_list





# Basic Parameters

# Model_Mode = 'Auto' # 'Manual'

# input_features_list = ['seq_id','house_size','bedrooms','bathrooms']
# target_features_list = ['seq_id','price']   

# # input_features_list = ['seq_id','attendence','assignment','marks']
# # target_features_list = ['seq_id','results']   

# project_id = 2
# dataset_id = 2
# user_id = 1


# # Call The Model Class
# ModelObject = ModelClass(Model_Mode,
#                             input_features_list,
#                             target_features_list,
#                             project_id,
#                             dataset_id, 
#                             user_id)


# # If Manual Mode Then Give Below Details #########

# if Model_Mode == 'Auto':

#     basic_split_parameters = {'model_mode': 'auto'}

#     split_data_object = ModelObject.get_split_data_object(basic_split_parameters)
#     ModelObject.algorithm_identifier(split_data_object)
# else:
#     model_id = 1
#     model_name = 'linear regression'
#     model_type = 'Regression_Model'
#     model_parameters = {None}

#     basic_split_parameters = {'model_mode': 'manual', 'split_method': 'cross_validation',
#     'cv': 5, 'valid_size': None, 'test_size': 0.2, 'random_state': 0}

    # split_data_object = ModelObject.get_split_data_object(basic_split_parameters)
    
#     ModelObject.run_model(model_id, model_name, model_type, split_data_object)







    # ASK ABOUT RANDOM_STATE.

    # ADD RANDOM_STATE IN UI, AND ASK THE REST PEOPLE TO GET IT'S VALUE.
    
    # ModelObject-> MO

    # MO(constructor)
    # split_data_object = MO.split_data_object(split_dictionary)
    # MO.run_model(...., split_data_object)
    # MO.get_dataset_info()