'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

import pandas as pd
import numpy as np
from scipy import stats

class OutliersTreatmentClass:
    
    #* Below functions are used for detecting the outliers
    
    def extreme_value_analysis(self,series,outlier = True):
        '''
            Returns Probable & Extreme outliers. Best suitable for Non-Normal Distributions.
            
            Args:
                series[(pandas.Series)]: Column for which you want the outlier ranges.
                outlier[(boolean)]: if false than only returns ranges.
                
            Returns:
                List[(Intiger|Float)]: Output list contains following 2 lists & 4 Intigers,
                    1. List of Probable Outliers,
                    2. List of Most-Probable Outliers
                    3. Upper Limit for probable outliers
                    4. Upper Limit for Most-Probable outliers
                    5. Lower Limit for probable outliers
                    6. Lower Limit for Most-Probable outliers
        '''
        try:
            #? Finding Quartiles
            q1 = series.quantile(0.25)
            q3 = series.quantile(0.75)
            
            #? Finding Boundaries of the normal data
            iqr = q3-q1
            upper_limit = q3 + (iqr * 1.5)
            upper_limit_extreme = q3 + (iqr * 3)
            lower_limit = q1 - (iqr * 1.5)
            lower_limit_extreme = q1 - (iqr * 3)
            
            if not outlier: 
                return [upper_limit,upper_limit_extreme,lower_limit,lower_limit_extreme]
            
            #? Getting probable outliers
            outliers = series[series > upper_limit]
            outliers = outliers.append(series[series < lower_limit])
            
            #? Getting most-probable outliers
            extreme_outliers = series[series > upper_limit_extreme]
            extreme_outliers = extreme_outliers.append(series[series < lower_limit_extreme])
            
            return [outliers.tolist(),extreme_outliers.tolist(),upper_limit,upper_limit_extreme,lower_limit,lower_limit_extreme]
        
        except:
            return 1
    
    def z_score_analysis(self,series,level = 3,outlier = True):
        '''
            Returns list of the Outliers. Best suitable for Normal Distributions.
            
            Args:
                Series[(pandas.Series)]: Column for which you want the outlier ranges,
                level[(intiger|float)] (default=3)= level of the standard deviation. (Typically between 1.5 to 4).
                outlier[(boolean)]: if false than only returns z-scores.
                
            Returns:
                List[(intiger|float)] = List of the outliers for given standard deviation range & Z-scores for all values
        '''
        try:
            #? This line returns z-scores for all the values of the column
            z_score = stats.zscore(series)
            
            if not outlier:
                return z_score
            
            #? Getting the outliers
            return [[i for i in z_score if (i > level or i < -level)],z_score]
        except:
            return 1
        
    #* Below functions are used for dealing with outliers
    
    def delete_above(self,data_df,col,val,ge = False):
        '''
            Deletes rows where value of given column is greater than given value.
            
            Args:
                data_df[(pandas.Dataframe)]: Dataframe,
                col[(String)]: Name of the column
                val[(intiger|float)]: deciding value
                ge[(boolean)]: Delete values "Greater than or Eq: True" or only "Greater than: False"

            Returns:
                pandas.Dataframe: Filtered Dataframe
        '''
        try:
            if ge:
                return data_df[data_df[col] < val]
            else:
                return data_df[data_df[col] <= val]
        except:
            return 1
        
    def delete_below(self,data_df,col,val,le = False):
        '''
            Deletes rows where value of given column is lesser than given value.
            
            Args:
                data_df[(pandas.Dataframe)]: Dataframe,
                col[(String)]: Name of the column
                val[(intiger|float)]: deciding value
                ge[(boolean)]: Delete values "Less than or Eq: True" or only "Less than: False"

            Returns:
                pandas.Dataframe: Filtered Dataframe
        '''
        try:
            if le:
                return data_df[data_df[col] > val]
            else:
                return data_df[data_df[col] >= val]
        except:
            return 1
    
    def replace_outliers(self,series, operation = 0, detect_method = 0, less_probable = False, level = 3, log = False):
        '''
            Returns a series where the outliers are replaced with the given function(Mean of Median)
            
            Args:
            -----
            series[(pandas.Series)]: column,
            operation[(intiger)] (default = 0): which operation should be performed,
                - 0 : mean
                - 1 : median
                - 2 : mode \n
            detect_method[(intiger)] (default = 0): which method should be used to detect outliers,
                - 0 : Extreme Value Analysis
                - 1 : Z-score method \n
            less_probable[(boolean)] (default = False): should less probable outliers be raplaced?
            level[(intiger)] (default = 3): level of std in Z-score method.
            log[(boolean)] (default = False): Apply log transforamation before outlier detection?
                
            Returns:
            --------
            List[(intiger|float)]: Updated Column
        '''
        
        try:
            if log:
                series = self.apply_log_transformation(series)
            
            if operation == 0:
                value = np.mean(series)
            elif operation == 1:
                value = np.median(series)
            elif operation == 2:
                value = stats.mode(series.tolist())
            else:
                return 2
            
            #? Extreme Value Analysis
            if detect_method == 0:
                upper_limit,upper_limit_extreme,lower_limit,lower_limit_extreme = self.extreme_value_analysis(series,False)
                
                #? Setting upper & lower limit
                if less_probable:
                    u_limit = upper_limit
                    l_limit = lower_limit
                else:
                    u_limit = upper_limit_extreme
                    l_limit = lower_limit_extreme
                    
                #? Replacing outliers
                series = series.apply(lambda x: value if (x > u_limit or x < l_limit) else x)
            
            #? Z-Score Method
            elif detect_method == 1:
                if level < 1.5:
                    level = 1.5
                elif level > 4:
                    level = 4
                    
                z_score = self.z_score_analysis(series,level,False)
                
                #? Replacing Outliers
                series = [value if (val > level or val < -level) else series.iloc[index] for index,val in enumerate(z_score) ]
            
            #? Invalid Input
            else:
                return 3
            
            return series
        except:
            return 1
        
    def remove_outliers(self,data_df,col, detect_method = 0, less_probable = False, level = 3, log = False):
        '''
            Returns a series where the outliers are replaced with the given function(Mean of Median)
            
            Args:
                data_df[(pandas.Dataframe)]: whole dataframe,
                col[(string)]: name of the column
                detect_method[(intiger)] (default = 0): which method should be used to detect outliers,
                                                            0 => Extreme Value Analysis
                                                            1 => Z-score method
                less_probable[(boolean)] (default = False): should less probable outliers be removed?
                level[(intiger)] (default = 3): level of std in Z-score method.
                log[(boolean)] (default = False): Apply log transforamation before outlier detection?
                
            Returns:
                pandas.Dataframe: Updated Dataframe
        '''
        
        try:
            if log:
                data_df[col] = self.apply_log_transformation(data_df[col])
                
            #? Extreme Value Analysis
            if detect_method == 0:
                upper_limit,upper_limit_extreme,lower_limit,lower_limit_extreme = self.extreme_value_analysis(data_df[col],False)
                
                #? Setting upper and lower limit
                if less_probable:
                    u_limit = upper_limit
                    l_limit = lower_limit
                else:
                    u_limit = upper_limit_extreme
                    l_limit = lower_limit_extreme
                    
                data_df = data_df[data_df[col] >= l_limit]
                data_df = data_df[data_df[col] <= u_limit]
                
            #? Z-Score Method
            elif detect_method == 1:
                if level < 1.5:
                    level = 1.5
                elif level > 4:
                    level = 4
                    
                z_score = self.z_score_analysis(data_df[col],level,False)
                
                data_df['z_score'] = z_score
                data_df = data_df[data_df['z_score'] <= level]
                data_df = data_df[data_df['z_score'] >= -level]
                
            #? Invalid Input
            else:
                return 3
            
            return data_df
        except:
            return 1
        
    def apply_log_transformation(self,series):
        '''
            Apply log transformation on the given column.
            
            Args:
                series[(pandas.Series)]: column data.
                
            Returns:
                pandas.Series: transformed series.
        '''
        
        return np.log(series)