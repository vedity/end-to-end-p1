'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Mann Purohit         10-FEB-2021           1.0         Initial Version           

*/
'''

import json
import ast 
import logging
import numpy as np

from common.utils.logger_handler import custom_logger as cl
from sklearn.model_selection import train_test_split
from common.utils.exception_handler.python_exception.common.common_exception import *

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')


class SplitData:
    # Add DBObject and connection to it's attributes in constructor.

    
    def get_scaled_split_dict(self,DBObject,connection,project_id,dataset_id):
        #TODO This command will change
        try:
            # Get the scaled_split_params from the mlaas.project_tbl
            sql_command = 'select scaled_split_parameters from mlaas.project_tbl where project_id = ' + str(project_id) + ' and dataset_id='+str(dataset_id)
            data_df = DBObject.select_records(connection, sql_command)
            if data_df is None:
                    raise DatabaseConnectionFailed(500)
            if len(data_df) == 0 :
                    raise DataNotFound(500)
            
            scaled_split_params = data_df['scaled_split_parameters'][0]# Add exception
            scaled_split_params_dict = ast.literal_eval(scaled_split_params)
            return scaled_split_params_dict

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        
        
    def get_features_list(self, user_id, project_id, dataset_id, DBObject, connection):
        #TODO sql_command will be changed in the future
        try:
            sql_command = 'select input_features,target_features from mlaas.project_tbl where  project_id={} and dataset_id={}'.format(project_id, dataset_id)
            input_target_df = DBObject.select_records(connection, sql_command)
            if input_target_df is None:
                    raise DatabaseConnectionFailed(500)
            if len(input_target_df) == 0 :
                    raise DataNotFound(500)
            input_features = input_target_df['input_features'][0]# Get the input features list
            target_features = input_target_df['target_features'][0]# Get the target features list
            
            input_features = ast.literal_eval(input_features)# Formatting   
            target_features = ast.literal_eval(target_features)# Formatting

            return input_features, target_features
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg

    def get_split_datasets(self, scaled_split_params_dict):

        path = "/opt/airflow/dags/" 
        # Load the train, test, valid datasets 
        train_X = np.load(path + scaled_split_params_dict['train_X_filename'], allow_pickle=True)
        test_X = np.load(path + scaled_split_params_dict['test_X_filename'], allow_pickle=True)
        train_y = np.load(path + scaled_split_params_dict['train_Y_filename'], allow_pickle=True)
        test_y = np.load(path + scaled_split_params_dict['test_Y_filename'], allow_pickle=True)
        if scaled_split_params_dict['split_method'] == 'train_valid_holdout':
            valid_X = np.load(path + scaled_split_params_dict['valid_X_filename'], allow_pickle=True)
            valid_y = np.load(path + scaled_split_params_dict['valid_Y_filename'], allow_pickle=True)
        else:
            # Validation data will be none in case the user selects 'cross_validation' in data spliting
            valid_X = None
            valid_y = None
        return train_X,valid_X,test_X,train_y,valid_y,test_y

    def get_scaled_data(self, scaled_split_params_dict):

        path = "./" 
        # Load the train, test, valid datasets 
        train_X = np.load(path + scaled_split_params_dict['train_X_filename'], allow_pickle=True)
        test_X = np.load(path + scaled_split_params_dict['test_X_filename'], allow_pickle=True)
        train_y = np.load(path + scaled_split_params_dict['train_Y_filename'], allow_pickle=True)
        test_y = np.load(path + scaled_split_params_dict['test_Y_filename'], allow_pickle=True)
        actual_y = np.load(path + scaled_split_params_dict['actual_Y_filename'], allow_pickle=True)
        if scaled_split_params_dict['split_method'] == 'train_valid_holdout':
            valid_X = np.load(path + scaled_split_params_dict['valid_X_filename'], allow_pickle=True)
            valid_y = np.load(path + scaled_split_params_dict['valid_Y_filename'], allow_pickle=True)
        else:
            # Validation data will be none in case the user selects 'cross_validation' in data spliting
            valid_X = None
            valid_y = None
        return train_X,valid_X,test_X,train_y,valid_y,test_y,actual_y

    
    

