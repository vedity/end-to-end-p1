import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('project_creation')


class Split_Data():
    
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
                X_train_valid, X_test, Y_train_valid, Y_test = train_test_split(input_df, target_df, test_size=test_size,
                                                                            random_state=random_state)

                X_train, X_valid, Y_train, Y_valid = train_test_split(X_train_valid, Y_train_valid, test_size=valid_size,
                                                                random_state=random_state)

                return X_train, X_valid, X_test, Y_train, Y_valid, Y_test
