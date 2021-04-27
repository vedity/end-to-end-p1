'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         27-Feb-2021           1.0            FeaturnScalingClass
 
*/
'''

#* Importing Libraries
import pandas as pd
import logging
import traceback
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

#* Common Utilities
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('feature_scaling')

class FeaturnScalingClass:
    
    def standard_scaling(self,dataframe):
        '''
            This function is used to scale the data using standard scaler.

            Args:
            -----
            dataframe (`pandas.DataFrame`): Unscaled Dataframe

            Returns:
            --------
            dataframe (`pandas.DataFrame`): Scaled Dataframe
        '''
        try:
            logging.info("data preprocessing : FeatureScalingClass : standard_scaling : execution start")
            scaler = StandardScaler()
            
            scaled_data = scaler.fit_transform(dataframe._get_numeric_data())
            scaled_df = pd.DataFrame(scaled_data,columns = dataframe._get_numeric_data().columns)
            for col in scaled_df.columns:
                dataframe[col] = scaled_df[col]
            
            logging.info("data preprocessing : FeatureScalingClass : standard_scaling : execution stop")
            return dataframe
        except Exception as e:
            logging.error("data preprocessing : FeatureScalingClass : standard_scaling : execution ailed : " +str(e))
            logging.error("data preprocessing : FeatureScalingClass : standard_scaling : execution ailed : " +traceback.format_exc())
            return None
    
    def min_max_scaling(self,dataframe):
        '''
            This function is used to scale the data using min-max scaler.

            Args:
            -----
            dataframe (`pandas.DataFrame`): Unscaled Dataframe

            Returns:
            --------
            dataframe (`pandas.DataFrame`): Scaled Dataframe
        '''
        
        try:
            logging.info("data preprocessing : FeatureScalingClass : min_max_scaling : execution start")
            
            scaler = MinMaxScaler()
            
            scaled_data = scaler.fit_transform(dataframe._get_numeric_data())
            scaled_df = pd.DataFrame(scaled_data,columns = dataframe._get_numeric_data().columns)
                
            for col in scaled_df.columns:
                dataframe[col] = scaled_df[col]
            
            logging.info("data preprocessing : FeatureScalingClass : min_max_scaling : execution stop")
            return dataframe
        except Exception as e:
            logging.error("data preprocessing : FeatureScalingClass : min_max_scaling : execution failed : " +str(e))
            logging.error("data preprocessing : FeatureScalingClass : min_max_scaling : execution failed : " +traceback.format_exc())
            return None
    
    
    def robust_scaling(self,dataframe):
        '''
            This function is used to scale the data using robust scaler.

            Args:
            -----
            dataframe (`pandas.DataFrame`): Unscaled Dataframe

            Returns:
            --------
            dataframe (`pandas.DataFrame`): Scaled Dataframe
        '''
        
        try:
            logging.info("data preprocessing : FeatureScalingClass : robust_scaling : execution start")
            
            scaler = RobustScaler()
            
            scaled_data = scaler.fit_transform(dataframe._get_numeric_data())
            scaled_df = pd.DataFrame(scaled_data,columns = dataframe._get_numeric_data().columns)
                
            for col in scaled_df.columns:
                dataframe[col] = scaled_df[col]
            
            logging.info("data preprocessing : FeatureScalingClass : robust_scaling : execution stop")
            return dataframe
        except Exception as e:
            logging.error("data preprocessing : FeatureScalingClass : robust_scaling : execution failed : " +str(e))
            logging.error("data preprocessing : FeatureScalingClass : robust_scaling : execution failed : " +traceback.format_exc())
            return None
    
    #! There are some bugs in this function
    # def custom_scaling(dataframe, max, min):
    #     count = dataframe.shape[1]
    #     for index in range(count):

    #         #get the dataframe column name based on the index
    #         column_name = dataframe.columns[index]

    #         #get the maximum value of the column
    #         col_max_value = dataframe[column_name].max()

    #         #get the minimum value of the column
    #         col_min_value = dataframe[column_name].min()

    #         #Looping based on columns present in the dataframe
    #         for i,val in enumerate(dataframe[column_name]):

    #             dataframe[column_name][i] = ((val- col_min_value)/(col_max_value - col_min_value))*(max - min) + min

    #     return dataframe
