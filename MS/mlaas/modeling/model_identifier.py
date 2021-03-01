'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''

import ast
import pandas as pd
import json
import re
import logging
import traceback
import datetime

from .algorithm_detector import AlgorithmDetector
from .utils.supervised.supervised_model import SupervisedClass as SC
from .utils.model_experiments.model_experiment import ExperimentClass as EC
from .algorithm_detector import AlgorithmDetector
# from utils.unsupervised.unsupervised_model import UnSupervisedClass as USC
from .split_data import SplitData
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')

class ModelClass(SC, SplitData):
    """This is the main class from which stores the methods for fetching data and implementing ML algorithms.

    Args:
        SC (Class): Supervised Algorithm Class, which stores all the supervised algorithms.
        SplitData ([Class]): [Stores the variables required at the time of splitting the train,test, validation data]
    """
    def __init__(self,Model_Mode=None, user_id=None, project_id=None,dataset_id=None, DBObject=None,
                 connection=None,connection_string=None):
        
        """This is used to initialise the basic input parameter for the model. 
        """
        
        self.Model_Mode = Model_Mode # Get Mode Mode
        self.user_id = user_id # Get User Id
        self.project_id = project_id # Get Project Id
        self.dataset_id = dataset_id # Get Datset Id
        self.DBObject, self.connection, self.connection_string = DBObject,connection,connection_string# Get Database Object,Connection And Connection String
        # self.input_features_list, self.target_features_list = SplitData().get_input_target_features_list(user_id, project_id, dataset_id, DBObject, connection) # Get Input and Target Features List 
    
    def algorithm_identifier(self):
        
        logging.info("modeling : ModelClass : algorithm_identifier : execution start")
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        # It will check wheather it is supervised algorithm or not.
        if len(self.target_features_list) > 0:
             # call  supervised algorithm method
            self.supervised_algorithm()
            
        else:
            # call  unsupervised algorithm method
            self.unsupervised_algorithm()
            
        logging.info("modeling : ModelClass : algorithm_identifier : execution end")
           
            
    
       
        
    def run_model(self,model_id,model_name,model_type, SplitDataObject):
        """This function is used to run model when model mode is in manual. 

        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        logging.info("modeling : ModelClass : run_model : execution start")
        # Get Scaled Data With Input And Target 
        input_df,target_df = self.get_scaled_data()
        
        # Check Whether Model Type Is Regression Or Classification.
        if model_type == 'Regression_Model':
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_regression_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       SplitDataObject,
                                                       self.DBObject, 
                                                       self.connection, 
                                                       self.connection_string,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)
            
            
        else:
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_classification_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       SplitDataObject,
                                                       self.DBObject, 
                                                       self.connection, 
                                                       self.connection_string,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)
            
        logging.info("modeling : ModelClass : run_model : execution end")

    
    def supervised_algorithm(self):
        """This function is used to call supervised algorithm.
        """
        logging.info("modeling : ModelClass : supervised_algorithm : execution start") 
        # Call The Super Class (SupervisedClass) Method's.                                                                                                                           
        super(ModelClass,self).supervised_algorithm(self.Model_Mode,
                                                    self.user_id,
                                                    self.project_id,
                                                    self.dataset_id,
                                                    self.DBObject,
                                                    self.connection)
        
        logging.info("modeling : ModelClass : supervised_algorithm : execution end")
    
    def unsupervised_algorithm(self):
        """This function is used to call unsupervised algorithm.
        """
        logging.info("modeling : ModelClass : unsupervised_algorithm : execution start")
        # Get Scaled Data With Input And Target.
        input_df,_ = self.get_scaled_data()
        logging.info("modeling : ModelClass : unsupervised_algorithm : execution end")


    def get_dataset_info(self):
        """This function returns the project_name, dataset_name and the target columns for the associated dataset.

        Returns:
            Tuple: project_name, dataset_name, target_columns:- name of target feature/s associated to the dataset.
        """
        logging.info("modeling : ModelClass : get_dataset_info : execution start")
       
        # SQL query to get the project_name
        sql_command = 'select project_name from mlaas.project_tbl where project_id=' + str(self.project_id)
        project_df = self.DBObject.select_records(self.connection, sql_command)
        project_name = project_df['project_name'][0]

        # SQL query to get the dataset_name
        sql_command = 'select dataset_name from mlaas.dataset_tbl where dataset_id=' + str(self.dataset_id)
        dataset_df = self.DBObject.select_records(self.connection, sql_command)
        dataset_name = dataset_df['dataset_name'][0]

        # SQL Query to get the target_features_list
        sql_command = 'select target_features from mlaas.cleaned_ref_tbl where project_id=2 and dataset_id=2'#.format(self.project_id, dataset_id)
        target_columns = self.DBObject.select_records(self.connection, sql_command)['target_features'].to_list()
        target_columns= ast.literal_eval(target_columns[0])
        
        logging.info("modeling : ModelClass : get_dataset_info : execution end"+str(type(target_columns)))

        return project_name, dataset_name, target_columns[1:]

    
    def get_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        
        AlgorithmDetectorObject = AlgorithmDetector(self.DBObject, self.connection)
        # Used to detect the ML algorithm and model types based on target_df
        return AlgorithmDetectorObject.get_model_types(target_df)

    def show_model_list(self):
        """Returns the compatible list of model on the basis of target_df, using which we identify
        algorithm_type and model_type.

        Returns:
            list: models_list, contains list of all the ML/DL models derived from the algorithm and model type.
        """
        target_df = self.get_scaled_data()[1]
        AlgorithmDetectorObject = AlgorithmDetector(self.DBObject, self.connection)
        # Used to detect the ML algorithm and model types based on target_df
        algorithm_type, model_type = AlgorithmDetectorObject.get_model_types(target_df)
        # Used to get all the model names compatible with the algorithm and model type
        return AlgorithmDetectorObject.show_models_list(algorithm_type, model_type)

    def get_hyperparameters_list(self, model_name):
        """Returns the appropriate list of hyperparameters associated with the model_name argument.

        Args:
            model_name (string): name of the ML/DL model.

        Returns:
            list: list of hyperparameters of the model 'model_name'.
        """
        
        AlgorithmDetectorObject = AlgorithmDetector(self.DBObject, self.connection)
        # 
        hyperparameters_list = AlgorithmDetectorObject.get_hyperparameters_list(model_name)
        print(hyperparameters_list)
        #logging.info("aaaaaaaaaaaaaaaaaaaaaaa"+hyperparameters_list)
        #return ast.List(hyperparameters_list)
        return hyperparameters_list


