import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from common.utils.logger_handler import custom_logger as cl
from common.utils.database import db
from database import *
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('project_creation')
DBObject = db.DBClass()
connection,connection_string = DBObject.database_connection(database,user,password,host,port)
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

    def check_split_exist(self,projectid):

        sql_command = f'select "scaled_split_parameters" from mlaas.project_tbl pt where project_id  ='+projectid
        df = DBObject.select_records(connection,sql_command)
        if (df.iloc[0]['scaled_split_parameters']) == None:
            flag = False
        else:
            flag = True
    
        return flag

    def get_split_activity_desc(self,project_name,activity_id):
        #project_name = '"'+project_name+'"'
        sql_command = f"select replace (amt.activity_description, '*', '{project_name}') as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
        desc_df = DBObject.select_records(connection,sql_command)
        activity_description = desc_df['description'][0]

        return activity_description