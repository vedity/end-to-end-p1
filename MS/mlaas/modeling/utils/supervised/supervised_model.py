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
from modeling.algorithm_detector import AlgorithmDetector
from modeling.split_data import SplitData

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')

class SupervisedClass(RC,PC):
   
    def supervised_algorithm(self, Model_Mode, user_id, project_id, dataset_id, 
                             DBObject, connection,experiment_name,experiment_desc,model_type):
        
        """This function is used to call supervised algorithm.
        """
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution start")

        AlgorithmDetectorObject = AlgorithmDetector(DBObject, connection)
        
        model_type_dict = AlgorithmDetectorObject.get_model_type(project_id,dataset_id)
        
        algorithm_type = model_type_dict['algorithm_type']
        target_type = model_type_dict['target_type']

        if model_type == "Regression" :
            # Call Regression Class's method
            super(SupervisedClass,self).regression_model(Model_Mode, user_id, project_id, dataset_id,
                                                        model_type, algorithm_type,target_type,DBObject,connection,experiment_name,experiment_desc)
                
                                                
        elif model_type == "Classification" :
            # Call Probabilistic Class's method
            super(SupervisedClass,self).classification_model(Model_Mode,
                                                             DBObject,connection,connection_string,
                                                             project_id,dataset_id,user_id,
                                                             experiment_name,experiment_desc)
        
        else:
            print("please select appropriate target")
            
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution end")
        
        
        
        
    def run_supervised_model(self, Model_Mode,user_id,project_id,dataset_id,DBObject,connection,model_type, 
                            model_id, experiment_name,experiment_desc):
        
        logging.info("modeling : SupervisedClass : run_regression_model : execution start") 
        # Call the super class method.
        if model_type == 'Regression':
            
            super(SupervisedClass, self).run_regression_model(Model_Mode,user_id,project_id,dataset_id,
                                        DBObject,connection,model_id, experiment_name,experiment_desc)
        else:
            print("Classification is to be implemented")
        
        logging.info("modeling : SupervisedClass : run_regression_model : execution end") 


         
        
        
        
   
    