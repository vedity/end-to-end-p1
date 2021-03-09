'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging
import traceback

#* Relative Imports
from . import duplicate_data_handling as ddh
from . import feature_scaling as fs
from . import categorical_encoding as ce

#* Commong Utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('transformation')



class TransformationClass(ddh.RemoveDuplicateRecordClass, fs.FeaturnScalingClass, ce.EncodeClass):
    '''
        Handles orchastration of the transforamtion related Functions.
    '''
    
    #* DUPLICATE DATA REMOVAL
    
    def duplicate_data_removal(self, data_df):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        return super().remove_duplicate_records(dataframe= data_df)
    
    #* RESCALING
    
    def standard_scaling(self, dataframe):
        '''
            Operation id: 23
        '''
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().standard_scaling(dataframe)
    
    def min_max_scaling(self, dataframe):
        '''
            Operation id: 24
        '''
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().min_max_scaling(dataframe)
    
    def robust_scaling(self, dataframe):
        '''
            Operation id: 25
        '''
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().robust_scaling(dataframe)
    
    def custom_scaling(self, dataframe, max, min):
        '''
            Operation id: 26
        '''
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().custom_scaling(dataframe, max, min)
    
    #* Categorical Encoding
    
    def label_encoding(self, dataframe, col):
        '''
            Operation id: 10
        '''
        
        logging.info("data preprocessing : TransformationClass : label_encoding : execution start")
        
        cols = [dataframe.columns[i] for i in col]
        
        for column in cols:
            try:
                dataframe[column] =super().label_encoding(dataframe[column])
            except:
                continue

        logging.info("data preprocessing : TransformationClass : label_encoding : execution stop")
        return dataframe
    
    def one_hot_encoding(self, dataframe, col):
        '''
            Operation id: 10
        '''
        
        logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution start")
        
        cols = [dataframe.columns[i] for i in col]
        
        for column in cols:
            try:
                temp_df =super().one_hot_encoding(dataframe[column])
                dataframe.drop([column], axis=1, inplace = True)
                dataframe = dataframe.join(temp_df)
            except:
                continue

        logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution stop")
        return dataframe
    