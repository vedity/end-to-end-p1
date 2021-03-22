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
        
    
    def algorithm_identifier(self,model_type,experiment_name,experiment_desc):
        
        logging.info("modeling : ModelClass : algorithm_identifier : execution start")
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        
        # It will check wheather it is supervised algorithm or not.
        if model_type == 'Regression' or model_type == 'Classification':
             # call  supervised algorithm method
            super(ModelClass,self).supervised_algorithm(self.Model_Mode,
                                                    self.user_id,self.project_id,self.dataset_id,
                                                    self.DBObject,self.connection,
                                                    experiment_name,experiment_desc,model_type)
            
        else:
            # call  unsupervised algorithm method
            super(ModelClass,self).unsupervised_algorithm(experiment_name,experiment_desc)
            
        logging.info("modeling : ModelClass : algorithm_identifier : execution end")
        

        
    def run_model(self, model_type, model_id, experiment_name, experiment_desc):
        """This function is used to run model when model mode is in manual. 
 
        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        logging.info("modeling : ModelClass : run_model : execution start")
        
        # Check Whether Model Type Is Regression Or Classification.
        if model_type == 'Regression' or model_type == 'Classification':
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_supervised_model(self.Model_Mode,
                                                    self.user_id,self.project_id,self.dataset_id,
                                                    self.DBObject,
                                                    self.connection,
                                                    model_type, model_id, experiment_name,experiment_desc)
        else:
            print("Unsupervised ML, to be impemented.")
        
        
    def store_manual_model_params(self, manual_model_params_dict):
        # dataset_split_params = manual_model_params_dict['dataset_split_params']
        # model_type = manual_model_params_dict['model_type']
        model_id = manual_model_params_dict['model_id']
        # model_name = manual_model_params_dict['model_name']
        hyperparameters = str(manual_model_params_dict['hyperparameters'])
        experiment_name = manual_model_params_dict['experiment_name']
 
        table_name = 'mlaas.manual_model_params_tbl'
        cols = 'user_id, project_id, dataset_id, exp_name, model_id, hyperparameters'
 
        row = self.user_id, self.project_id, self.dataset_id, experiment_name, model_id, hyperparameters
        row_tuples = [tuple(row)]
 
        store_manual_model_params_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        print("store_manual_model_params status ==",store_manual_model_params_status)

    

    
   

    

    

