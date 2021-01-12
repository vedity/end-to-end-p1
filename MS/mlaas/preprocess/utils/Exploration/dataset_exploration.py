'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla               25-DEC-2020           1.0           Created Class
 
*/
'''

import pandas as pd
#from ..ingest.utils.database import db
from common.utils.database import db
import numpy as np
import json

class ExploreClass:

    def get_dataset_statistics(self,DBObject,connection,table_name):
        """
            This class returns all the statistics for the given table.
            
            input: DBObject, connection object, name of the csv table
            output: dataframe containing statistics
        """
        
        sql_command = f"SELECT * FROM {table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        
        try:
            stats_df = data_df.describe(include = 'all')

            stats_df = stats_df.T
            stats_df.rename(columns = {'unique':'Unique Values'}, inplace = True)    
            stats_df["Null Values"] = len(data_df) - stats_df['count']
            stats_df.rename(columns = {'count':'Non-Null Values'}, inplace = True)    
            stats_df.rename(columns = {'mean':'Mean'}, inplace = True)    
            stats_df.rename(columns = {'std':'Std'}, inplace = True)    
            stats_df.rename(columns = {'min':'Min Value'}, inplace = True)    
            stats_df.rename(columns = {'max':'Max Value'}, inplace = True)    
            stats_df.rename(columns = {'top':'Most Frequent'}, inplace = True)    
            stats_df.rename(columns = {'freq':'Frequency'}, inplace = True)    

            try:
                stats_df = stats_df[['Mean','Std','Min Value','25%','50%','75%','Max Value','Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
            except KeyError:
                try:
                    stats_df = stats_df[['Mean','Std','Min Value','25%','50%','75%','Max Value','Null Values','Non-Null Values']]
                except KeyError:
                    stats_df = stats_df[['Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
        except AttributeError:
            stats_df = data_df.describe(include = 'all')
            return stats_df
        except TypeError:
            stats_df = data_df.describe(include = 'all')
            return stats_df
            
        return  stats_df
    
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
        # data_df = data_df.to_json(orient='records')
        # data_df = json.loads(data_df)
        
        return data_df
    

