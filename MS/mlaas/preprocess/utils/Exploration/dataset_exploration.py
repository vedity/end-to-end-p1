'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla               25-DEC-2020           1.0           Created Class
 
*/
'''

import pandas as pd
import numpy as np

from ingest.utils.dataset import dataset_creation as dc
from common.utils.database import db

class ExploreClass:

    def get_dataset_statistics(self,DBObject,connection,dataset_id):
        """
            This class returns all the statistics for the given dataset.
            
            input: DBObject, connection object, id of the dataset
            output: dataframe containing statistics
        """
        
        #? getting the name of the dataset_tbl
        table_name,_,_ = dc.make_dataset_schema()
        
        #? Getting user_name and dataset_vaisibility
        sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
        visibility_df = DBObject.select_records(connection,sql_command) 

        if len(visibility_df) != 0: 
            user_name,dataset_visibility = visibility_df['user_name'][0],visibility_df['dataset_visibility'][0]
        #? No entry for the given dataset_id        
        else: return 1
        
        #? Getting CSV table name
        sql_command = "SELECT DATASET_TABLE_NAME FROM "+ table_name + " WHERE DATASET_ID ='"+ dataset_id +"'"
        dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        dataset_table_name = dataset_df['dataset_table_name'][0] 
        
        #? changing the database schema for the public databases
        if dataset_visibility == 'public':
            user_name = 'public'
        
        #? Getting all the data
        sql_command = f"SELECT * FROM {user_name}.{dataset_table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        
        try:
            #? Getting Statistics
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

            stats_df['Column Name'] = 0
        
            #? Merging the Column Names
            i = 0
            for col in data_df.columns:
                stats_df.iloc[i,-1] = col
                i += 1
            
            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['Column Name','Mean','Std','Min Value','25%','50%','75%','Max Value','Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['Column Name','Mean','Std','Min Value','25%','50%','75%','Max Value','Null Values','Non-Null Values']]
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['Column Name','Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
        except AttributeError:
            stats_df = data_df.describe(include = 'all')
            return stats_df
        except TypeError:
            stats_df = data_df.describe(include = 'all')
            return stats_df
    
        return stats_df
    
    def return_columns(self,DBObject, connection, table_name,*args):
        '''
            Returns data to be shown in the Visualization
            
            input: DBObject, connection object, name of the csv table, columns
            output: dataframe 
        '''
        
        cols = ''
        for i in args:
            cols += str(i)
            cols += ' '
        
        cols = cols.strip()
        cols = cols.replace(" ",",")
        
        #? Get Data Of the Column
        sql_command = f"SELECT {cols} FROM {table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        
        return data_df
    
    