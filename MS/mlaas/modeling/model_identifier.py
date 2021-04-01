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
    def __init__(self,db_param_dict):
        
        """This is used to initialise the basic input parameter for the model. 
        """
        # Get Database Object,Connection And Connection String
        self.db_param_dict = db_param_dict
    
    def algorithm_identifier(self,model_param_dict):
        
        logging.info("modeling : ModelClass : algorithm_identifier : execution start")
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        # It will check wheather it is supervised algorithm or not.
        try:
            if model_param_dict['model_type'] in ('Regression','Classification'):
                # call  supervised algorithm method
                result = super(ModelClass,self).supervised_algorithm(model_param_dict,self.db_param_dict)
                
            else:
                # call  unsupervised algorithm method
                result = super(ModelClass,self).unsupervised_algorithm(model_param_dict,self.db_param_dict)
                
            logging.info("modeling : ModelClass : algorithm_identifier : execution end")

            return result
        except Exception as e:
            return e

        
    def run_model(self,model_param_dict,model_id,model_name,model_param):
        """This function is used to run model when model mode is in manual. 
 
        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        logging.info("modeling : ModelClass : run_model : execution start")
        
        # Check Whether Model Type Is Regression Or Classification.
        if model_param_dict['model_type'] in ('Regression','Classification'):
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_supervised_model(model_param_dict,self.db_param_dict,model_id,model_name,model_param)
        else:
            print("Unsupervised ML, to be implemented.")
        
        
 
        
        
    

    

    
   

    

    

