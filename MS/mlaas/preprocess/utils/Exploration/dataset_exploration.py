'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla               25-DEC-2020           1.0           Created Class
 
*/
'''

import pandas as pd
from ..database import db
import numpy as np

class ExploreClass:
  
    def get_dataset_statistics(self,DBObject,connection,table_name):
        """
            This class returns all the statistics for the given table.
            
            input: DBObject, connection object, name of the csv table
            output: dataframe containing statistics
        """
        
        sql_command = f"SELECT * FROM {table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        
        unique_list= []
        null_list = []
        
        for cols in data_df.columns:
            unique_list.append(len(data_df[cols].unique()))
            null_list.append(len(data_df[data_df[cols] == np.NaN]))
        
        stats_df = data_df.describe()
        
        stats_df["Unique Values"] = unique_list
        stats_df["Null Values"] = null_list
        
        return stats_df
    
    def return_columns(self,DBObject, connection, table_name,*args):
        '''
            Returns data to be shown in the boxplot
            
            input: DBObject, connection object, name of the csv table, columns
            output: dataframe 
        '''
        
        cols = ''
        for i in args:
            cols += str(i)
            cols += ' '
        
        cols = cols.strip()
        cols = cols.replace(" ",",")
        
        sql_command = f"SELECT {cols} FROM {table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        
        return data_df