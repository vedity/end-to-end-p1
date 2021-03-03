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


user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')


class SplitData:
    
    def get_dataset_split_dict(self, dataset_split_parameters):
        """ Returns the splitting dataset parameters.
        Args:
        dataset_split_parameters (dictionary): [Contains the model_mode, and if required, other necessary parameters.]

        Returns:
            [tuple]: [dataset splitting method, and parameters required to split it.]
        """
        if dataset_split_parameters['model_mode'] == 'Manual':

            split_method = dataset_split_parameters['split_method']
            random_state = dataset_split_parameters['random_state']
            test_size = dataset_split_parameters['test_size']
            train_size = 1 - test_size
            
            if split_method == 'cross_validation':    
                cv = dataset_split_parameters['cv']
                valid_size = None
            else:
                valid_size = dataset_split_parameters['valid_size']
                cv = None

        elif dataset_split_parameters['model_mode'] == 'Auto':

            # config_path ="./basic_dataset_split_config.json"
            # json_data=open(config_path,'r') 
            # dataset_split = json_data.read()
            # dataset_split_param_dict = ast.literal_eval(dataset_split) 
            
            ############# 
            dataset_split_param_dict ={"split_method" : "cross_validation",
                                       "train_size" : 0.8, "test_size" : 0.2, 
                                       "random_state" : 0, "cv" : 5,
                                       "valid_size" : None}
            
            # dataset_split_param_dict = json.load(config_path)
            split_method = dataset_split_param_dict['split_method']
            random_state = dataset_split_param_dict['random_state']
            test_size = dataset_split_param_dict['test_size'] 
            train_size = dataset_split_param_dict['train_size']
            cv =  dataset_split_param_dict['cv']
            valid_size = dataset_split_param_dict['valid_size']

        dataset_split_dict = {'split_method': split_method, 'random_state': random_state, 'test_size': test_size,
                             'train_size': train_size, 'cv': cv, 'valid_size': valid_size}
        return dataset_split_dict


    def get_split_data(self, input_df, target_df, random_state, test_size, valid_size, split_method):
        """Returns train-test or train-valid-test split on the basis of split_method.

        Args:
            X (array/DataFrame): Input values.
            y (array/DataFrame): Target values.

        Returns:
            X_train, X_test, Y_train, Y_test or also returns X_valid, Y_valid: Splitted data for train and test.
        """
        if split_method == 'cross_validation':
            X_train, X_test, Y_train, Y_test = train_test_split(input_df, target_df, test_size=test_size,
                                                                random_state=random_state)

            return X_train, None, X_test, Y_train, None, Y_test
        else:
            X_train_valid, X_test, Y_train_valid, Y_test = train_test_split(X, y, test_size=self.test_size,
                                                                        random_state=self.random_state)

            X_train, X_valid, Y_train, Y_valid = train_test_split(X_train_valid, Y_train_valid, test_size=valid_size,
                                                            random_state=random_state)

            return X_train, X_valid, X_test, Y_train, Y_valid, Y_test

    
    def get_scaled_path(self,DBObject,connection,project_id):
        
        sql_command = 'select scaled_data_path from mlaas.cleaned_ref_tbl where project_id = ' + str(project_id)
        data_df = DBObject.select_records(connection, sql_command)

        path = dataset_df['scaled_data_path'][0]# Add exception
        
        return path
    
    def get_scaled_data(self,path):
        """Returns the data that will be preprocessed by the user in the preprocessing stage.

        Returns:
            [Dataframes]: [input_features_df:- the df used to predict target features, target_features_df:- the target/dependent data]
        """
        logging.info("modeling : ModelClass : get_scaled_data : execution start")
        #TODO, this will change in future as there will be multiple users,projects and datasets.
        # Read Scaled Data From Numpy File    
         
        scaled_df = np.load(path)
        
        input_features_df = scaled_df[:,0:-1]
        
        index=scaled_df[:,0].reshape(len(scaled_df[:,0]),1) 
        target=scaled_df[:,-1].reshape(len(scaled_df[:,-1]),1)
        
        target_features_df =np.concatenate((index,target),axis=1) 
        
        logging.info("modeling : ModelClass : get_scaled_data : execution end")
        return input_features_df,target_features_df 


    
    def get_input_target_features_list(self, user_id, project_id, dataset_id, DBObject, connection):
        #TODO sql_command will be changed in the future
        sql_command = 'select input_features,target_features from mlaas.cleaned_ref_tbl where user_id={} and project_id={} and dataset_id={}'.format(user_id, project_id, dataset_id)
        input_target_df = DBObject.select_records(connection, sql_command)
        #TODO Add Exception
        input_features = input_target_df['input_features'][0]# Get the input features list
        target_features = input_target_df['target_features'][0]# Get the target features list
        
        input_features = ast.literal_eval(input_features)
        target_features = ast.literal_eval(target_features)

        return input_features, target_features

