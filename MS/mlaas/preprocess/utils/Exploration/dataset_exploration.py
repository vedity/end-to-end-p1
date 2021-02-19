'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla               25-DEC-2020           1.0           Created Class
 
*/
'''

from scipy import stats
import logging
import math
import pandas as pd
import numpy as np
import json

from ingest.utils.dataset import dataset_creation
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from ingest.utils.dataset import dataset_creation

dc = dataset_creation.DatasetClass()

class ExploreClass:

    def get_attrbt_datatype(self,csv_data,column_name_list,no_of_rows):
        """
        this function used to get proper attribute type for the column in csv file.

        Args : 
            [(csv_data)] : [Pandas.DataFrame containing the data],
            [(column_name_list)] : [List of the column name],
            [(no_of_rows)] : [No of rows in csv data].

        Return :
            [List] : [List of the predicted type attribute for columns]

        """
        
        attribute_type = [] #empty list to append attribute type
        for column_name in column_name_list: #iterate column name list 
            column_data = csv_data[column_name].tolist() #get the specified column data convert into list
            unique_values = list(set(column_data)) #get the set of unique values convert into list
            if (len(unique_values)/no_of_rows) < 0.2 :
                if "," in str(column_data[1]): #check if the comma value present
                    value = "categorical list"
                else :
                    value = "Categorical"
            else:
                value =  "false" #check condition if condition true then set as categorical else false
            if value =="false": 
                datatype_value = csv_data.dtypes.to_dict()[column_name] #get datatype specified for perticular column name
                if datatype_value in ['float64','float32','int32','int64']: #check if int,float,double present then set it "numerical"
                    value = "Continuous"
                elif datatype_value in ['datetime64[ns]']: #check if datetime value present then set it "timestamp"
                    value = "Timestamp"
                elif datatype_value in ['object']:  #check if object type value present then set it "text"
                        value = "Text"
            attribute_type.append(value) #append type attribute value into list 
        
        logging.info("data preprocessing : ExploreClass : get_attribute_datatype : execution stop")    
        return attribute_type
    
    def get_dataset_statistics(self,DBObject,connection,dataset_id,schema_id):
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
        
        #? Getting user_name and dataset_visibility
        sql_command = f"SELECT USER_NAME,DATASET_VISIBILITY,DATASET_TABLE_NAME,no_of_rows FROM {table_name} WHERE dataset_id = '{dataset_id}'"
        visibility_df = DBObject.select_records(connection,sql_command) 
        if len(visibility_df) != 0: 
            user_name,dataset_visibility = visibility_df['user_name'][0],visibility_df['dataset_visibility'][0]
        #? No entry for the given dataset_id        
        else: return 1
        
        #? Getting CSV table name
        dataset_table_name = visibility_df['dataset_table_name'][0]
        dataset_table_name = '"'+ dataset_table_name+'"'
        
        #? changing the database schema for the public databases
        if dataset_visibility == 'public':
            user_name = 'public'
        

        query = DBObject.get_query_string(connection,schema_id)
        #? Getting all the data
        sql_command = f"SELECT {str(query)} FROM {user_name}.{dataset_table_name}"
        data_df = DBObject.select_records(connection,sql_command)    
        #? Logical Code Begins
        try:
            #? Getting Statistics
            stats_df = data_df.describe(include = 'all')
            
            #? Getting Categorical & Continuous Columns
            num_cols = data_df._get_numeric_data().columns
            numerical_columns = list(num_cols)
            predicted_datatypes = self.get_attrbt_datatype(data_df,data_df.columns,len(data_df))
            for i,col in enumerate(data_df.columns):
                if (col in numerical_columns) and (predicted_datatypes[i].startswith('Ca')):
                    numerical_columns.remove(col)
            stats_df = stats_df.T
            
            #? Changing The Column Names
            stats_df.rename(columns = {'unique':'Unique Values'}, inplace = True)    
            stats_df.rename(columns = {'count':'Non-Null Values'}, inplace = True)  
            stats_df.rename(columns = {'mean':'Mean'}, inplace = True)
            stats_df.rename(columns = {'std':'Std'}, inplace = True)    
            stats_df.rename(columns = {'min':'Min Value'}, inplace = True)    
            stats_df.rename(columns = {'max':'Max Value'}, inplace = True)    
            stats_df.rename(columns = {'top':'Most Frequent'}, inplace = True) 
            stats_df.rename(columns = {'freq':'Most Frequency'}, inplace = True)    

            #? Changing Column Datatypes
            stats_df['Mean'] = stats_df['Mean'].astype(float)
            stats_df['Std'] = stats_df['Std'].astype(float)
            stats_df['Min Value'] = stats_df['Min Value'].astype(float)
            stats_df['Max Value'] = stats_df['Max Value'].astype(float)
            stats_df['25%'] = stats_df['25%'].astype(float)
            stats_df['50%'] = stats_df['50%'].astype(float)
            stats_df['75%'] = stats_df['75%'].astype(float)
            
            #? Defining All the Columns that are not in the DataFrame.describe() method but are needed for the exploration page
            stats_df["Null Values"] = len(data_df) - stats_df['Non-Null Values']
            stats_df["Null Values"] = stats_df['Null Values'].astype(int)
            stats_df["Non-Null Values"] = stats_df['Non-Null Values'].astype(int)
            stats_df["DataCount"] = len(data_df)
            stats_df['Least Frequency'] = np.NAN
            stats_df['Least Frequent'] = np.NAN
            stats_df['Column Name'] = 0
            stats_df['Plot Values'] = 0
            stats_df['Plot Values'] = stats_df['Plot Values'].astype('object')
            stats_df['Right Outlier Values'] = 0
            stats_df['Right Outlier Values'] = stats_df['Right Outlier Values'].astype('object')
            stats_df['Left Outlier Values'] = 0
            stats_df['Left Outlier Values'] = stats_df['Left Outlier Values'].astype('object')
            stats_df['Outliers'] = 0
            stats_df['Outliers'] = stats_df['Outliers'].astype('object')
            data_df = data_df.dropna()
            
            #? Getting Column Names, Plotting Values of the histogram & Lest Frequent Values
            i = 0
            axislist =[]
            
            for col in data_df.columns:
                #? Merging Column Names
                stats_df.iloc[i,-5] = col
                #? Getting Histogram/CountPlot Values
                axislist.append(self.get_values(data_df[col],numerical_columns,col))
        
                #? Getting Least Frequent Values & Count, only for the categorical columns
                if self.get_datatype(numerical_columns,col).startswith("Ca"):
                    try:
                        value_count = data_df[col].value_counts()
                        stats_df.iloc[i,2] = value_count.index[0]
                        stats_df.iloc[i,3] = value_count.iloc[0]
                        stats_df.iloc[i,-6] = value_count.index[-1]
                        stats_df.iloc[i,-7] = value_count.iloc[-1]
                    except:
                        stats_df.iloc[i,2] = np.NaN
                        stats_df.iloc[i,3] = np.NaN
                        stats_df.iloc[i,-6] = np.NaN
                        stats_df.iloc[i,-7] = np.NaN
                i += 1

            stats_df['Plot Values'] = axislist
            stats_df['Datatype'] = predicted_datatypes
            
            IQR = stats_df['75%']-stats_df['25%']
            stats_df['open'] = stats_df['25%']-1.5 * IQR
            stats_df['close'] = stats_df['75%']+1.5 * IQR
            
            stats_df['open'] = stats_df['open'].astype(float)
            stats_df['close'] = stats_df['close'].astype(float)
            
            #? Getting Outlier Values
            i = 0
            outliers_list = []
            lower_outliers_list = []
            upper_outliers_list = []
            updated_plot_list = []
            unique_list = []
        
            for col in data_df.columns:
                #? Getting Lower & Upper Limits for the Histogram
                lower_limit = stats_df.iloc[i]['open']
                upper_limit = stats_df.iloc[i]['close']
                #? Getting Edges of the Bins and Values of Each Bins
                bin_edges, hists = stats_df.iloc[i]['Plot Values']
                #? Getting Arrays of the Outliers to be plotted
                lower_outliers, upper_outliers, lower_clip, upper_clip = self.get_outlier_hist(hists, bin_edges, upper_limit, lower_limit)
                #? Getting All the outlier values
                outliers_list.append(self.get_outliers(data_df,col,upper_limit,lower_limit))
                
                #? Pulling plot values
                data  = stats_df.iloc[i]['Plot Values']
                x_axis_values = data[0]
                y_axis_values = data[1]
                if col in numerical_columns:
                    #? Adjusting plot values only for the continuous values, because outlier bins will only be seen in the continuous columns
                    try:
                        #? Removing outlier bins from the plot bins
                        if upper_clip != 0:
                            x_axis_values = x_axis_values[lower_clip:-upper_clip]
                            y_axis_values = y_axis_values[lower_clip:-upper_clip]
                        else:
                            x_axis_values = x_axis_values[lower_clip:]
                            y_axis_values = y_axis_values[lower_clip:]
                    except:
                        #? NaN values of lower clip & upper clip will raise exceptions
                        pass 
                    lower_outliers_list.append(lower_outliers)
                    upper_outliers_list.append(upper_outliers)
                    unique_list.append(np.NaN)
                else:
                    #? Count plots of the categorical columns does not need the outlier bins
                    lower_outliers_list.append([[],[]])
                    upper_outliers_list.append([[],[]])
                    unique_list.append(len(data_df[col].unique()))

                updated_plot_list.append([x_axis_values,y_axis_values])
                i += 1 
            
            #? Storing the Values in the dataframe, so that tey can be sent
            stats_df['Right Outlier Values'] = upper_outliers_list
            stats_df['Left Outlier Values'] = lower_outliers_list
            stats_df['Outliers'] = outliers_list
            stats_df['Plot Values'] = updated_plot_list
            stats_df['Unique Values'] = unique_list
            
            #? Adding a column needed for the frontend
            stats_df['IsinContinuous'] = [True if stats_df.loc[i,'Datatype'] == 'Continuous' else False for i in stats_df.index]
            
            #? Dataset Contains both Categorical & Continuous Data
            try:
                stats_df = stats_df[['Plot Values','Left Outlier Values','Right Outlier Values','Outliers','IsinContinuous','Column Name','Datatype','DataCount','Mean','Std','Min Value','25%','50%','75%','Max Value','Most Frequent','Most Frequency','Least Frequent','Least Frequency','Unique Values','Null Values','Non-Null Values','open','close']]
            
            except KeyError:
                try:
                    #? Dataset Contains only Continuous Data
                    stats_df = stats_df[['Plot Values','Left Outlier Values','Right Outlier Values','Outliers','IsinContinuous','Column Name','Datatype','DataCount','Mean','Std','Min Value','25%','50%','75%','Max Value','Null Values','Non-Null Values','open','close']]
                except KeyError:
                    #? Dataset Contains only Categorical Data
                    stats_df = stats_df[['Plot Values','Left Outlier Values','Right Outlier Values','Outliers','IsinContinuous','Column Name','Datatype','DataCount','Most Frequent','Most Frequency','Least Frequent','Least Frequency','Unique Values','Null Values','Non-Null Values']]
        except:
            return 2
        
        return stats_df.round(2)    
    
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
        if number_of_bins < 10: number_of_bins = 10
        
        return number_of_bins
    
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
            elif number_of_bins < 2: number_of_bins = 2
            #? Getting histogram values & bin_edges
            hist, bin_edges = np.histogram(a=arr, bins=number_of_bins)
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
        
        #? If there are more than 50 bins than the count plot is not suitable
        #? Resizing the countplot
        if len(values) > 50:
            stepsize = int(np.ceil(len(values)/50))
            classes = classes[::stepsize]
            values = values[::stepsize]
        
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
            check = self.get_histogram_values(arr.tolist()) 
            return check
        else:
            return self.get_count_plot(arr)
        
        
    def get_datatype(self,numerical,col_name):
        '''This function bifurcate Continuous or Categorical Datatype
        Args:
                arr[(Intiger|Float|String)]: Takes pandas.Series object as input.
                numerical[List(String)]: Names of numerical columns.
                col_name[String]: Name of the current column.
                
            Returns:
                datatype[String] : Continuous/Categorical
        '''
        
        if col_name in numerical:
            datatype = "Continuous"
            return datatype
        else:
            datatype = "Categorical"
            return datatype
        

    def get_outlier_hist(self,hist,bin_edges,upper_limit,lower_limit):
        '''
            This Function returns the values for Outlier Bins to be plotted in the
            Histogram.
            
            Args:
                hist[(List of Intigers)]: Y-axis values for each bins,
                bin_edges[(List of Intigers)]: X-axis values for each bins,
                upper_limit[(Intiger)]: Upper limit for the Normal Values, 
                lower_limit[(Intiger)]: Lower limit for the Normal Values.
            
            Returns:
                lower_outliers[(List of Lists)]: Histogram Values for Lower Outliers.
                upper_outliers[(List of Lists)]: Histogram Values for Upper Outliers.
                lower_edges_length[(Intiger)]: How many left side outlier bins (lower outlier bins) are there in the histogram.
                upper_edges_length[(Intiger)]: How many right side outlier bins (upper outlier bins) are there in the histogram.
        '''
        try:
            lower_edges = list(filter(lambda x: x<lower_limit,bin_edges))
            lower_hist = hist[:len(lower_edges)]
            upper_edges = list(filter(lambda x: x>upper_limit,bin_edges))
            if len(upper_edges) == 0:
                upper_hist = []
            else:
                upper_hist = hist[-len(upper_edges):]

            upper_outliers = [upper_edges,upper_hist]
            lower_outliers = [lower_edges,lower_hist]

            return lower_outliers, upper_outliers, len(lower_edges), len(upper_edges)
        except:
            return [[],[]],[[],[]], np.NaN, np.NaN
        
    def get_outliers(self,df,col,upper_limit,lower_limit):
        '''
            This Function Returns the Values of all the Outliers.
            This function is used to get outlier values for the Box-Plot.
            
            Args:
                df[(pandas.DataFrame)]: DataFrame Containing the Dataset which is to be explored.
                col[(String)]: Columns name
                upper_limit[(Intiger)]: Upper Limit of the Normal Values
                lower_limit[(Intiger)]: Lower Limit of the Normal Values
                
            ReturnsL
                List[(List of Intigers)]: List containing the outliers to be plotted in the box plot.
        '''
        try:
            partial_list_1 = df[df[col] < lower_limit][col]
            partial_list_2 = df[df[col] > upper_limit][col]
            return list(set(partial_list_1.tolist() + partial_list_2.tolist()))
        except:
            return []
