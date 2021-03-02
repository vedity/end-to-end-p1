import pandas as pd
import logging
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler


from common.utils.logger_handler import custom_logger as cl
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('feature_scaling')

class FeaturnScalingClass:
    def standard_scaling(self,dataframe):
        
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(dataframe)
        scaled_df = pd.DataFrame(scaled_data,columns = dataframe.columns)
        return scaled_df

    def min_max_scaling(self,dataframe):
        min_max = MinMaxScaler()
        min_max_data = min_max.fit_transform(dataframe)
        scaled_df = pd.DataFrame(min_max_data,columns = dataframe.columns)
        return scaled_df
    
    def robust_scaling(self,dataframe):
        robust_scaler = RobustScaler()
        robust_data = robust_scaler.fit_transform(dataframe)
        scaled_df = pd.DataFrame(robust_data,columns = dataframe.columns)
        return scaled_df
    
    def custom_scaling(dataframe, max, min):
        count = dataframe.shape[1]
        for index in range(count):

            #get the dataframe column name based on the index
            column_name = dataframe.columns[index]

            #get the maximum value of the column
            col_max_value = dataframe[column_name].max()

            #get the minimum value of the column
            col_min_value = dataframe[column_name].min()

            #Looping based on columns present in the dataframe
            for i,val in enumerate(dataframe[column_name]):

                dataframe[column_name][i] = ((val- col_min_value)/(col_max_value - col_min_value))*(max - min) + min

        return dataframe
