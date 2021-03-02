'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Mann Purohit         15-FEB-2021           1.0         Initial Version           

*/
'''

import logging
import traceback
import ast

from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('project_creation')

class AlgorithmDetector:

    def __init__(self, DBObject, connection):
        self.DBObject = DBObject
        self.connection = connection

    def get_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        algorithm_type = None
        model_type = None
        # This logic is used to distinguish different types of algorithms and models.

        target_shape = target_df.shape
        total_length = target_shape[0]
        unq_length = len(target_df.iloc[:,1].unique())
        threshold = int((total_length * 0.01) / 100) # Subject to change, further research.

        if threshold < unq_length:
            model_type = 'Regression'
            
            if target_shape[1] == 2:
                algorithm_type = 'Single_Target'
            elif target_shape[1] > 2:
                algorithm_type = 'Multi_Target'
            
        else:
            model_type = 'Classification'
            if unq_length == 2:
                algorithm_type = 'Binary_Classification'
            elif unq_length > 2:
                algorithm_type = 'MultiClass_Classification'
        
        return algorithm_type, model_type
    
    def show_models_list(self, algorithm_type, model_type):
        """Returns the compatible list of model on the basis of algorithm_type and model_type.

        Returns:
            list: models_list, contains list of all the ML/DL models derived from the algorithm and model type.
        """
        sql_command = "select * from mlaas.model_master_tbl where model_type='"+model_type+"'"+" and algorithm_type='"+algorithm_type+"'"
        models_list = self.DBObject.select_records(self.connection, sql_command)# Add exception
        return models_list


    def get_hyperparameters_list(self, model_id):
        """Returns the appropriate list of hyperparameters associated with the model_name argument.

        Args:
            model_name (string): name of the ML/DL model.

        Returns:
            list: list of hyperparameters of the model 'model_name'.
        """
        sql_command = "select model_parameter from mlaas.model_master_tbl where model_id='"+model_id+"'"
        hyperparameters_list = self.DBObject.select_records(self.connection, sql_command)['model_parameter'][0]# Add exception
        return hyperparameters_list