from scipy import stats
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils.database import db
from common.utils.database.db import DBClass
from ingest.utils.dataset import dataset_creation
from .exploration import dataset_exploration as de
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from dateutil.parser import parse
import logging
import math
import pandas as pd
import numpy as np
import json

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')
DBObject = db.DBClass() # create object for database class
dc = dataset_creation.DatasetClass()

class VisualizationClass:
    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.]
            user ([string]): [user of the database.]
            password ([string]): [password of the database.]
            host ([string]): [host ip or name where database is running.]
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number
    
    def get_hist_visualization(self,DBObject,connection,datasetid,column_name):
        dataset_id = datasetid
        table_name,_,_ = dc.make_dataset_schema()
        
        #? Getting user_name and dataset_vaisibility
        sql_command = f"SELECT DATASET_TABLE_NAME FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
        visibility_df = DBObject.select_records(connection,sql_command) 
        dataset_table_name = visibility_df['dataset_table_name'][0]
        sql_command = f"select {column_name} from {dataset_table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        try:
            #? Getting Statistics
            stats_df = data_df.describe(include = 'all')
            
        
            #? Getting Categorical & Continuous Columns
            cols = data_df.columns
            num_cols = data_df._get_numeric_data().columns
            numerical_columns = list(num_cols)
            stats_df = stats_df.T
            
            stats_df['Plot Values'] = 0
            stats_df['Plot Values'] = stats_df['Plot Values'].astype('object')
            data_df = data_df.dropna()
            #? Merging the Column Names
            i = 0
            axislist =[]
            
            for col in data_df.columns:
                stats_df.iloc[i,-2] = col
                axislist.append(self.get_values_hist(data_df[col],numerical_columns,col))     
                i += 1
            stats_df['Plot Values'] = axislist
            
            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['Plot Values']]
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['Plot Values']]
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['Plot Values']]
        except:
            return 2
        logging.info("loop end"+str(stats_df)) 
        return stats_df   


    def get_countplot_visualization(self,DBObject,connection,datasetid,column_name):
        dataset_id = datasetid
        table_name,_,_ = dc.make_dataset_schema()
        columnname = column_name
        #? Getting user_name and dataset_vaisibility
        sql_command = f"SELECT DATASET_TABLE_NAME FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
        visibility_df = DBObject.select_records(connection,sql_command) 
        dataset_table_name = visibility_df['dataset_table_name'][0]
        sql_command = f"select {columnname} from {dataset_table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        try:
            #? Getting Statistics
            stats_df = data_df.describe(include = 'all')
            
        
            #? Getting Categorical & Continuous Columns
            cols = data_df.columns
            num_cols = data_df._get_numeric_data().columns
            numerical_columns = list(num_cols)
            stats_df = stats_df.T
            stats_df['Column Name'] = 0
            stats_df['Plot Values'] = 0
            stats_df['Plot Values'] = stats_df['Plot Values'].astype('object')
            data_df = data_df.dropna()
            #? Merging the Column Names
            i = 0
            axislist =[]
            
            for col in data_df.columns:
                stats_df.iloc[i,-2] = col
                axislist.append(self.get_values_countplot(data_df[col],numerical_columns,col))     
                i += 1
            stats_df['Plot Values'] = axislist
            
            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['Column Name','Plot Values']]
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['Column Name','Plot Values']]
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['Column Name','Plot Values']]
        except:
            return 2
        logging.info("loop end"+str(stats_df)) 
        return stats_df.T 

    def get_boxplot_visualization(self,DBObject,connection,datasetid,column_name):
        dataset_id = datasetid
        table_name,_,_ = dc.make_dataset_schema()
        
        #? Getting user_name and dataset_vaisibility
        sql_command = f"SELECT DATASET_TABLE_NAME FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
        visibility_df = DBObject.select_records(connection,sql_command) 
        dataset_table_name = visibility_df['dataset_table_name'][0]
        sql_command = f"select {column_name} from {dataset_table_name}"
        data_df = DBObject.select_records(connection,sql_command)
        select_col_data = f"select * from {column_name}"
        coldata_df = DBObject.select_records(connection,sql_command)
        try:
            #? Getting Statistics
            stats_df = data_df.describe(include = 'all')
            logger.info(stats_df)
        
            #? Getting Categorical & Continuous Columns
            cols = data_df.columns
            stats_df = stats_df.T
            
            stats_df.rename(columns = {'max':'Max Value'}, inplace = True)    
            stats_df['Column Name'] = 0
            IQR = stats_df['75%']-stats_df['25%']
            stats_df['min'] = stats_df['25%']-(1.5 * IQR)
            stats_df['max'] = stats_df['75%']+(1.5 * IQR)
            minval = int(stats_df['min'])
            maxvalue = int(stats_df['max'])
            outlier = []
    
            data_df = data_df.dropna()
            #? Merging the Column Names
            i = 0

            for col in data_df.columns:
                stats_df.iloc[i,-2] = col
                i += 1
            for col in coldata_df[column_name]:
                if col < minval or col > maxvalue:
                    outlier.append(col)
                

            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['25%','75%','min','max']]
                
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['25%','75%','min','max']]
                    
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['25%','75%','min','max']]
        except:
            return 2
        logging.info("loop end"+str(stats_df)) 
        return stats_df.T,outlier
    
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
        i_q_r = self.iqr(arr)
        n = len(arr)
        
        #? Getting optimal number of bins
        number_of_bins = (2*(i_q_r/(n**(1/3))))
        number_of_bins = math.ceil(number_of_bins)
        if number_of_bins < 2: number_of_bins = 3
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
            elif number_of_bins <= 2: number_of_bins = 3
            #? Getting histogram values & bin_edges
            hist, bin_edges = np.histogram(a=arr, bins=number_of_bins)
            logging.info("np.hist finished")
            return [bin_edges[:-1].tolist(),hist.tolist()]
        
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
    
    def get_values_hist(self,arr,numerical,col_name):
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
            check = self.get_histogram_values(arr.tolist()) 
            return check
        else:
            return str("Categorical data!!")

    def get_values_countplot(self,arr,numerical,col_name):
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
            return str("Continious data!!")
        else:
            return self.get_count_plot(arr)
        
    def get_values_boxplot(self,arr,numerical,col_name):
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
            check = self.get_histogram_values(arr.tolist()) 
            return check
        else:
            return str("Categorical data!!")    
        
    
