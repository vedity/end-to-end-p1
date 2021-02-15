'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''


import pandas as pd
import json
import re
import logging
import traceback
import datetime
from .utils.supervised.supervised_model import SupervisedClass as SC
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
    
    def __init__(self,Model_Mode = None,input_features_list=None,target_features_list=None,
                 project_id = None,dataset_id = None, user_id = None, DBObject=None,
                 connection=None,connection_string=None):
        
        """This is used to initialise the basic input parameter for the model. 
        """
        
        self.Model_Mode = Model_Mode # Get Mode Mode
        self.input_features_list = input_features_list # Get Input Features List
        self.target_features_list = target_features_list # Get Target Features List
        self.project_id = project_id # Get Project Id
        self.dataset_id = dataset_id # Get Datset Id
        self.user_id = user_id # Get User Id
        # Get Database Object,Connection And Connection String
        self.DBObject, self.connection, self.connection_string = DBObject,connection,connection_string
        self.algorithm_type, self.model_type = self.get_model_type(self.get_scaled_data()[1])


    def algorithm_identifier(self,split_data_object):
        
        logging.info("modeling : ModelClass : algorithm_identifier : execution start")
        
        """This function is used to identify the algorithm based on target selected.
            if target is selected then call superived algorithm.
            else call the unsupervised algorithm. 
        """
        # It will check wheather it is supervised algorithm or not.
        if len(self.target_features_list) > 0:
             # call  supervised algorithm method
            self.supervised_algorithm(split_data_object)
            
        else:
            # call  unsupervised algorithm method
            self.unsupervised_algorithm()
            
        logging.info("modeling : ModelClass : algorithm_identifier : execution end")
           
            
    
       
        
    def run_model(self,model_id,model_name,model_type, split_data_object):
        """This function is used to run model when model mode is in manual. 

        Args:
            model_id ([integer]): [unique id of the model.]
            model_name ([string]): [unique name of the model.]
            model_type ([string]): [type of the model.]
            split_data_object ([Object of Class SplitData]): [Train-Test splitting parameters for the model.]
        """
        logging.info("modeling : ModelClass : run_model : execution start")
        # Get Scaled Data With Input And Target 
        input_df,target_df = self.get_scaled_data()
        
        # Check Whether Model Type Is Regression Or Classification.
        if model_type == 'Regression_Model':
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_regression_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       split_data_object,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)
            
            
        else:
            # Call The Super Class (SupervisedClass) Method's. 
            super(ModelClass,self).run_classification_model(model_id,
                                                       model_name,
                                                       model_type,
                                                       self.Model_Mode,
                                                       self.input_features_list,
                                                       self.target_features_list,
                                                       input_df,
                                                       target_df,
                                                       split_data_object,
                                                       self.project_id,
                                                       self.dataset_id,
                                                       self.user_id)
            
        logging.info("modeling : ModelClass : run_model : execution end")

    
    def supervised_algorithm(self,split_data_object):
        """This function is used to call supervised algorithm.
        """
        logging.info("modeling : ModelClass : supervised_algorithm : execution start")
        # Get Scaled Data With Input And Target
        input_df,target_df = self.get_scaled_data()
        # Call The Super Class (SupervisedClass) Method's.                                                                                                                           
        super(ModelClass,self).supervised_algorithm(self.Model_Mode,
                                                    self.input_features_list,
                                                    self.target_features_list,
                                                    input_df,
                                                    target_df,
                                                    split_data_object,
                                                    self.project_id,
                                                    self.dataset_id,
                                                    self.user_id)
        
        logging.info("modeling : ModelClass : supervised_algorithm : execution end")
        
        
    
    def unsupervised_algorithm(self):
        """This function is used to call unsupervised algorithm.
        """
        logging.info("modeling : ModelClass : unsupervised_algorithm : execution start")
        # Get Scaled Data With Input And Target.
        input_df,_ = self.get_scaled_data()
        logging.info("modeling : ModelClass : unsupervised_algorithm : execution end")
        
    
    
    def split_dataset(self, basic_split_parameters):
        '''
        Input: split_dataset, a dictionary which contains key value pairs where keys are the train,test,
        validation ratios, split_method and cv value.
            
        This function creates an object of the Class SplitData and returns this object.
        '''
        logging.info("modeling : ModelClass : split_dataset : execution start")
        # Get Split Data Object
        split_data_object = SplitData(basic_split_parameters) 
        logging.info("modeling : ModelClass : split_dataset : execution end")
        return split_data_object


    def get_dataset_info(self):
        
        logging.info("modeling : ModelClass : get_dataset_info : execution start")
       

        sql_command = 'select project_name from mlaas.project_tbl where project_id = ' + str(self.project_id)
        project_df = self.DBObject.select_records(self.connection, sql_command)
        project_name = project_df['project_name'][0]

        sql_command = 'select dataset_name from mlaas.dataset_tbl where dataset_id = ' + str(self.dataset_id)
        dataset_df = self.DBObject.select_records(self.connection, sql_command)
        dataset_name = dataset_df['dataset_name'][0]

        target_columns = self.target_features_list
        
        logging.info("modeling : ModelClass : get_dataset_info : execution end")

        return project_name, dataset_name, target_columns[1:]


    def get_scaled_data(self):
        logging.info("modeling : ModelClass : get_scaled_data : execution start")
        # DBObject, connection, _ = self.get_db_connection()
        dataset_name_command = 'select scaled_data_table from mlaas.cleaned_ref_tbl where dataset_id = ' + str(self.dataset_id)
        dataset_table_name = self.DBObject.select_records(self.connection, dataset_name_command)['scaled_data_table'][0]

        scaled_df_get_command = 'select * from ' +'mlaas.' + dataset_table_name# doubt 
        scaled_df = self.DBObject.select_records(self.connection, scaled_df_get_command)

        input_features_df= scaled_df[self.input_features_list]  # by using self.input_features_list. must include unique seq id
        target_features_df = scaled_df[self.target_features_list]  # by using self.target_features_list .must include unique seq id
        logging.info("modeling : ModelClass : get_scaled_data : execution end")
        return input_features_df,target_features_df

    
    def get_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        logging.info("modeling : ModelClass : get_model_type : execution start")
        algorithm_type = None
        model_type = None
        if len(target_df) == 0: 
            algorithm_type = 'unsupervised'
            return algorithm_type, model_type
        else:
            target_shape = target_df.shape
            if target_shape[1] == 2:
                algorithm_type = 'Single_target'
            elif target_shape[1] > 2:
                algorithm_type = 'Multi_target'
            total_length = target_shape[0]
            unq_length = len(target_df.iloc[:,1].unique())

            threshold = int((total_length * 20) / 100)

            if threshold < unq_length :
                model_type = 'Regression'
            else:
                if unq_length == 2:
                    model_type = 'Binary_Classification'
                elif unq_length > 2:
                    model_type = 'MultiClass_Classification'
                    
            logging.info("modeling : ModelClass : get_model_type : execution end")
            return algorithm_type, model_type

    def show_model_list(self):
        logging.info("modeling : ModelClass : show_model_list : execution start")
        DBObject, connection, _ = self.get_db_connection()
        sql_command = 'select * from model_master where model_type='+self.model_type+' and algorithm_type='+self.algorithm_type
        logging.info("modeling : ModelClass : show_model_list : execution end")
        return DBObject.select_records(connection, sql_command)





