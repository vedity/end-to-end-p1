'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Nisha Barad         27-Feb-2021           1.0            SplitDataClass
 
*/
'''

#* Library Imports
import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from .categorical_encoding import EncodeClass as ec

#* Common Utilities
from database import *
from common.utils.logger_handler import custom_logger as cl
from common.utils.database import db

#* Logger Import
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('project_creation')

#* Initializing Objects
DBObject = db.DBClass()
ENC_OBJECT = ec()
connection,connection_string = DBObject.database_connection(database,user,password,host,port)

class SplitDataClass():
    
    def get_split_data(self, input_df, target_df, random_state, test_size, valid_size, split_method):
            """Returns train-test or train-valid-test split on the basis of split_method.

            Args:
                X (array/DataFrame): Input values.
                y (array/DataFrame): Target values.

            Returns:
                X_train, X_test, Y_train, Y_test or also returns X_valid, Y_valid: Splitted data for train and test.
            """
            try:
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
            except Exception as e:
                return str(e),None,None,None,None,None

    def check_split_exist(self,projectid):
        """This function will return status if scale and split is performed for particular project
        Args:
            projectid[Integer] : get project id

        Return:
            [flag] : flase if scale,split is not done else true.
        """

        # flag, desc = ENC_OBJECT.get_unencoded_colnames(DBObject,connection,projectid)

        # if not flag:
        #     #? Encoding of some columns are still remaining
        #     return flag, desc

        
        try:
            flag,desc = self.check_split_validation(projectid)
            if flag == False:
                return flag,desc
            sql_command = f'select "scaled_split_parameters" from mlaas.project_tbl pt where project_id  ='+str(projectid)
            df = DBObject.select_records(connection,sql_command)
            if (df.iloc[0]['scaled_split_parameters']) == None:
                flag = False
                desc = "Please complete Scale & Split operation first!"
        
            return flag,desc

        except Exception as e:
            logging.info("data preprocessing : Check Split : check_split_exist : exception"+str(e))
            return str(e)

    def get_split_activity_desc(self,project_name,activity_id):
        """This function will replace * into project name and get activity description of scale and split.

        Args:
        project_name[String]: get project name
        activity_id[Integer]: get activity id

        Returns:
            [String]: activity_description
        """
        #project_name = '"'+project_name+'"'
        sql_command = f"select replace (amt.activity_description, '*', '{project_name}') as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
        desc_df = DBObject.select_records(connection,sql_command)
        activity_description = desc_df['description'][0]

        return activity_description

    def get_missing_col_desc(self,df,col_name):
        '''
            This is a sub-function thats specifically used to get the message for 
            missing columns list. This message will be shown on the frontend.

            Args:
            ----
            df (`pd.DataFrame`): Dataframe containing unencoded column_names in a single column.
            col_name (`String`): Name of the column that contains the unencoded column names.

            Returns:
            -------
            string (`String`): Description for missing column warning.
        '''
        try:
            logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution start")

            if df.empty:
                string = "No column remaining for Missing Value Handling."
            else:    
                string = "Missing Value Handling Remaining in Columns "

                #? Adding column names
                for i,data in df.iterrows():
                    string += f"'{data[col_name]}', "
                else:
                    string = string[:-2]+"."
            
            logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution stop")

            return string
        except Exception as e:
            logging.error("data preprocessing : Check Split : get_missing_col_desc : exception"+str(e))
            return str(e)

    def check_split_validation(self,projectid):
        '''
            This function checks if we are good to go for modelling or not.
            Returns a flag & related description.

            Args:
            ----
            projectid (`Int`): Id of the project.

            Returns:
            -------
            flag (`Boolean`):
                - `True` : Modelling is possible
                - `False` :Modelling is not possible
                
            description (`String`): Description to be shown on the frontend.
        '''
        try:
            logging.info("data preprocessing : Check Split : check_split_validation : execution start")
            target_sql_command = f"select count(*) from mlaas.schema_tbl where schema_id in (select schema_id from mlaas.project_tbl where project_id = '{projectid}') and column_attribute = 'Target'"
            target_df = DBObject.select_records(connection,target_sql_command)
            if (int(target_df['count'][0])) == 0:
                flag = False
                desc = "Select target column in schema mapping!"
                logging.info("data preprocessing : Check Split : check_split_validation : execution stop")
                return flag,desc
            # else:
            #     flag = True
            #     desc = "You can now proceed to the modelling."

            missing_sql_command = f"select case when changed_column_name = '' then column_name else changed_column_name end column_name from mlaas.schema_tbl   where schema_id in (select schema_id from mlaas.project_tbl where project_id = '{projectid}') and missing_flag = 'True' and column_attribute != 'Ignore'"
            missing_val_df = DBObject.select_records(connection, missing_sql_command)
            
            if not isinstance(missing_val_df,pd.DataFrame):
                logging.info("data preprocessing : Check Split : check_split_validation : execution stop")
                return False,'function failed'

            desc = self.get_missing_col_desc(missing_val_df,'column_name')
            if not missing_val_df.empty:
                logging.info("data preprocessing : Check Split : check_split_validation : execution stop")
                return False, desc
            else:
                desc = "Continue for Scale and Split."
                return True, desc
        
        except Exception as e:
            logging.error("data preprocessing : Check Split : check_split_validation : exception"+str(e))
            return False,str(e)
