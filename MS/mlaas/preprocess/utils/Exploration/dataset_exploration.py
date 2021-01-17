'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla               25-DEC-2020           1.0           Created Class
 
*/
'''

import pandas as pd
import numpy as np
from scipy import stats
import math

from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from ingest.utils.dataset import dataset_creation as dc
from common.utils.database import db

class ExploreClass:

    def get_dataset_statistics(self,DBObject,connection,dataset_id):
        """
            This class returns all the statistics for the given dataset.
            
            Args:
                DBObject ([object]): [object of database class.],
                connection ([object]): [connection object of database class.],
                dataset-id ([intiger]): [id of the dataset.]
            
            Returns:
                stats_df ([pandas.Dataframe]): [Dataframe containing all the statistics.]
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
            
            #? Getting Categorical & Continuous Columns
            cols = data_df.columns
            num_cols = data_df._get_numeric_data().columns
            numerical_columns = list(num_cols)

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
            stats_df['Plot Values'] = 0
            stats_df['Plot Values'] = stats_df['Plot Values'].astype('object')
            data_df = data_df.dropna()

            #? Merging the Column Names
            i = 0
            for col in data_df.columns:
                stats_df.iloc[i,-2] = col
                stats_df.iloc[i,-1] = self.get_values(data_df[col],numerical_columns,col)
                i += 1

            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['Plot Values','Column Name','Mean','Std','Min Value','25%','50%','75%','Max Value','Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['Plot Values','Column Name','Mean','Std','Min Value','25%','50%','75%','Max Value','Null Values','Non-Null Values']]
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['Plot Values','Column Name','Most Frequent','Frequency','Unique Values','Null Values','Non-Null Values']]
        except:
            return 2
        
        return stats_df
    
    def return_columns(self,DBObject, connection, table_name,*args):
        '''
            Returns data to be shown in the Visualization.
            
            input: DBObject, connection object, name of the csv table, columns.
            output: dataframe. 
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

    def iqr(self,arr):
        '''
            Returns Interquartile range of values in the given array.
            #! Array must be in a sorted form.
            
            Args: 
                List[(Intiger|Float)]: Array containing all the values.
                
            Returns:
                (Intiger|Float): Inter Quartile Range.
        '''
        
        #? Get Interquartile Range
        i_q_r = stats.iqr(arr, interpolation = 'midpoint') 
        return i_q_r

    def get_bin_size_width(self,arr,sort = False):
        '''
            Returns Optimal Number of Bins for the histogram.
            
            Arguments:
                List[(Intiger|Float)]: Array containing all the values.
                sort[(Boolean)] (Default: False): Do you want to sort the array or not?
                
            Returns:
                (Intiger): Number of Bins.
        '''
        
        if sort: arr.sort()
        #minimum = arr[0]
        #maximum = arr[-1]
        i_q_r = self.iqr(arr)
        n = len(arr)
        
        #? Getting optimal number of bins
        number_of_bins = (2*(i_q_r/(n**(1/3))))
        number_of_bins = math.ceil(number_of_bins)
        if number_of_bins < 2: number_of_bins = 3
        #? Getting optimal bin width
        #bin_width = ((maximum-minimum)/number_of_bins)
        #bin_width = math.ceil(bin_width)
        
        return number_of_bins  #, bin_width 
    
    def get_histogram_values(self,arr):
        '''
            Returns the List Containing 2 Lists,  
                1) Bin Edge values (for X-axis).
                2) Histogram values for bins (For Y-axis).
                
            Arguments:
                List[(Intiger|Float)]: Array containing all the values.
                
            Returns:
                List[(Intiger|Float)]: List of 2 Lists containing bin_edges & histogram values.

        '''
        try:
            #? Sorting the array
            arr.sort()
            #? Getting the optimal number of bins
            number_of_bins = self.get_bin_size_width(arr)
            #? Limiting the number of bins in a diagram to 20
            if number_of_bins > 20: number_of_bins = 20
            #? Getting histogram values & bin_edges
            hist, bin_edges = np.histogram(arr, number_of_bins)
            
            return [bin_edges[:-1],hist]
        
        except (Exception) as exc:
            return exc
        
    def get_count_plot(self,arr):
        '''
            Returns values for the count plot. This function will be used when the
            column is categorical.
            
            Args:
                List(pandas.Series): Takes Categorical data as pandas.Series object.
                
            Returns:
                List[(String|Intiger)]: Retruns List of 2 lists containing,
                    1) Classes: For X-axis
                    2) Values: For Y-axis
        '''
        unique_values = arr.value_counts()
        classes = list(unique_values.index)
        values = unique_values.tolist()
        
        return [classes, values]
    
    def get_values(self,arr,numerical,col_name):
        '''
            This function handles plot values for Categorical & Continuous Data.
            
            Args:
                arr[(Intiger|Float|String)]: Takes pandas.Series object as input.
                numerical[List(String)]: Names of numerical columns.
                col_name[String]: Name of the current column.
                
            Returns:
                List[(Intiger|Float|String)]: Returns Values.
        '''
        
        if col_name in numerical:
            return self.get_histogram_values(arr.tolist())
        else:
            return self.get_count_plot(arr)
        
        
        
        