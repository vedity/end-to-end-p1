
#* Importing Libraries
import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split

#* Common utilities
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('project_creation')

class ModelType():
    def get_model_type(self, target_df):   
        """Returns the list of all algorithm using the model_type and algorithm_type.

         Args:
             target_df ([DataFrame]): [Target values of the target features.]

         Returns:
             [string, string]: [algorithm type, model type]
        """
        try:
            target_df=np.array(target_df)
            target_shape = target_df.shape
            total_length = target_shape[0]
            unq_length = len(np.unique(target_df[:,-1]))
            threshold = int((total_length * 0.01) / 100) # Subject to change, further research.
            target_type = ""
            if threshold < unq_length:
                model_type = 'Regression'
            else:
                model_type = 'Classification'
            
            if unq_length == 2:
                algorithm_type = 'Binary'
            elif unq_length > 2:
                algorithm_type = 'MultiClass'   
                
            if target_shape[1] == 2:
                target_type = 'Single_Target'
            elif target_shape[1] > 2:
                target_type = 'Multi_Target'
       
            return model_type,algorithm_type,target_type
        except Exception as e:
            logging.error("data preprocessing : ModelType : get_model_type : " +str(e))
            logging.error("data preprocessing : ModelType : get_model_type : " +traceback.format_exc())
            return None,None,None

