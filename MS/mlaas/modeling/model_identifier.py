'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           Initial Version 

*/
'''
# import Necessary Library.
import ast
import pandas as pd
import json
import re
import logging
import traceback
import datetime

# Import Common Class Files.
from .algorithm_detector import AlgorithmDetector
from .utils.supervised.supervised_model import SupervisedClass as SC
from .utils.model_experiments.model_experiment import ExperimentClass as EC
from .algorithm_detector import AlgorithmDetector
# from utils.unsupervised.unsupervised_model import UnSupervisedClass as USC
from .split_data import SplitData
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

# Declare Global Object And Variable.
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')

class ModelClass(SC):
    """This is the main class from which stores the methods for fetching data and implementing ML algorithms.

    Args:
        SC (Class): Supervised Algorithm Class, which stores all the supervised algorithms.
    """
    def __init__(self,db_param_dict):
        
        """This is used to initialise the basic input parameter for the model. 
        """
        # Get Database Object,Connection And Connection String
        self.db_param_dict = db_param_dict
    
    def algorithm_identifier(self,basic_params_dict):
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        # It will check wheather it is supervised algorithm or not.
        logging.info("modeling : ModelClass : algorithm_identifier : execution start")
        try:
            if basic_params_dict['model_type'] in ('Regression','Classification'):
                # call  supervised algorithm method
                result = super(ModelClass,self).supervised_algorithm(basic_params_dict,self.db_param_dict)
                
            else:
                # call  unsupervised algorithm method
                result = super(ModelClass,self).unsupervised_algorithm(basic_params_dict,self.db_param_dict)
                
            logging.info("modeling : ModelClass : algorithm_identifier : execution end"+str(result))

            self.set_experiment_state(basic_params_dict, result.status_code)

            return result
        except Exception as e:
            return e

        
    def run_model(self,basic_params_dict,model_id,model_name,model_hyperparams):
        
        """This function is used to run model when model mode is in manual. 
 
        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        logging.info("modeling : ModelClass : run_model : execution start")
        
        # Check Whether Model Type Is Regression Or Classification.
        if basic_params_dict['model_type'] in ('Regression','Classification'):
            # Call The Super Class (SupervisedClass) Method's. 
            result = super(ModelClass,self).run_supervised_model(basic_params_dict,self.db_param_dict,model_id,model_name,model_hyperparams)

            self.set_experiment_state(basic_params_dict, result.status_code)
        else:
            print("Unsupervised ML, to be implemented.")
            
        return result

    def set_experiment_state(self, basic_params_dict, status_code):
        """This function sets the state of the experiment.

        Args:
            basic_params_dict (dict): contains neccessary variables.
        """
        if status_code == 200:
            state = 'running'
                
            exp_name = basic_params_dict['experiment_name']
            project_id = int(basic_params_dict['project_id'])
            user_id = int(basic_params_dict['user_id'])
            dataset_id = int(basic_params_dict['dataset_id'])
            model_mode = basic_params_dict['model_mode']

            table_name='mlaas.model_dags_tbl'
            cols = 'exp_name,project_id,dataset_id,user_id,model_mode,state' 

            row = exp_name,project_id,dataset_id,user_id,model_mode,state  
            row_tuples = [tuple(row)]
            
            # Insert current running dag information into external model_dag_tbl.
            DBObject = self.db_param_dict['DBObject']
            connection = self.db_param_dict['connection']
            dag_status = DBObject.insert_records(connection,table_name,row_tuples,cols)

        
        
 
        
        
    

    

    
   

    

    

