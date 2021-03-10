'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         16-Feb-2021           1.0           Created Class
 
*/
'''

#* Importing Libraries
import pandas as pd
import numpy as np
from collections import Counter

#* Relative Imports
from . import missing_value_handling as mvh

#* Initializing Objects
MVH_OBJECT = mvh.MissingValueClass()

class RemoveNoiseClass:
    
    # def _check_string_col(self, series):
    #     '''
    #         This Function is used to check if given column is string column or not.
    #         It also checks if this column is cleanable or not.
    #         #!Note: This function is only produces accurate results for object dtype columns. 
        
    #         Args:
    #             Series(pandas.Series): The Column you want to check.
                
    #         Returns:
    #             is_string_col(boolean): True if the column is completely string.
    #             is_val_str_col(boolean): True if the column can be converted into numerical.
    #             is_string_minority(boolean): True is (Float or int) column has negeligible amount of string noise. 
    #     '''
        
    #     try:
    #         #? Defining required lists & booleans
    #         dtype = []
    #         valid_digit = []
    #         is_string_col = False
    #         is_val_str_col = False
    #         is_string_minority = False
            
    #         #? Getting Datatypes
    #         for data in series:
    #             dtype.append(type(data))
                
    #         #? Verifying the column type: if object column contains only one datatype then its a string column.
    #         if len(set(dtype)) == 1:
    #             is_string_col = True
                
    #             #? Checking if the whole column can be converted to string or not.
    #             for data in series:
    #                 valid_digit.append(data.isdigit())
    #             valid_digit_set = list(set(valid_digit))
    #             if len(valid_digit_set) == 1 and valid_digit_set[0] == True:
    #                 is_val_str_col = True
    #         #? If object column has more than 1 datatypes then checking if the string can be ignored or not.
    #         else:
    #             dtype_dict = Counter(dtype)
    #             if (dtype_dict.get(str)/len(series)) <= 0.33:
    #                 is_string_minority = True
                    
    #         return is_string_col,is_val_str_col,is_string_minority
    #     except:
    #         return False,False,False
        
    # def get_noisy_columns(self, data_df):
    #     '''
    #         Takes Dataframe as input.
    #         This function returns Noisy columns, Cleanable columns & Numeric_str cols for given dataframe.
            
    #         Args:
    #             data_df(pandas.DataFrame): the dataframe containing the data.
                
    #         Returns:
    #             noisy_columns(list of Strings): List containing noisy column names.
    #             cleanable_cols(list of strings): List containing columns that can be cleaned.
    #             valid_str_cols(list of Strings): List containing columns that can be converted to numerical columns.
    #     '''
        
    #     #? Defining required lists
    #     object_cols = [ col  for col, dt in data_df.dtypes.items() if dt == object]
    #     noisy_cols = []
    #     valid_str_cols = []
    #     cleanable_cols = []
        
    #     #? Only object columns contain the noise so checking for object columns
    #     for col in object_cols:
    #         is_string_col,is_val_str_col,is_string_minority = self._check_string_col(data_df[col])
            
    #         #? If object column is not a string column then it is a noisy column
    #         if not is_string_col:
    #             noisy_cols.append(col)
    #             #? Is is cleanable
    #             if is_string_minority:
    #                 cleanable_cols.append(col)
    #         else:
    #             #? Can it be converted to numerical columns
    #             if is_val_str_col:
    #                 valid_str_cols.append(col)
                    
    #     return noisy_cols, cleanable_cols, valid_str_cols
    
    # def detect_noise(self, series):
    #     '''
    #         Takes series as an input.
    #         This function returns Noisy columns, Cleanable columns & Numeric_str cols for given series.
            
    #         Args:
    #             data_df(pandas.Series): the Series containing the column data.
                
    #         Returns:
    #             noisy(boolean): Is the column noisy?
    #             cleanable(boolean): Can the column be cleaned?
    #             valid_str(boolean): Can the column be converted to numerical?
    #     '''
        
    #     #? Is the column of object dtype? if not the the column is not noisy
    #     if series.dtypes != object:
    #         return False, False, False
    #     else:
    #         noisy = False
    #         valid_str = False
    #         cleanable = False

    #         is_string_col,is_val_str_col,is_string_minority = self._check_string_col(series)
    #         #? if the column is not string column then the column is noisy
    #         if not is_string_col:
    #             noisy = True
    #             #? Is is cleanable
    #             if is_string_minority:
    #                 cleanable = True
    #         else:
    #             #? Can it be converted to numerical columns
    #             if is_val_str_col:
    #                 valid_str = True

    #         return noisy, cleanable, valid_str
        
    # def drop_noise(self, series):
    #     '''
    #         Takes in noisy series & replaces the string noise with the `np.NaN` value.
            
    #         Args:
    #         -----
    #         series (`pandas.Series`): the column data.
            
    #         Returns:
    #         -------
    #         series (`pandas.Series`): the column data with noise replaced with `np.NaN`.
    #     '''
        
    #     series = pd.to_numeric(series, errors = 'coerce')
        
    #     return series
        
    # def remove_noise(self, dataframe, column_id = None):
    #     '''
    #         Removes the rows where given columns contains noise.
            
    #         Args:
    #         -----
    #         dataframe (`pandas.DataFrame`): Whole dataframe.
    #         column_id (`List`) (default = `None`): List containing the column ids. if `None` then takes whole dataframe.
            
    #         Returns:
    #         --------
    #         dataframe (`pandas.DataFrame`): Dataframe with noise removed.
    #     '''
        
    #     if column_id:
    #         for i in column_id:
    #             dataframe.iloc[:,i] = self.drop_noise(dataframe.iloc[:,i])
    #     else:
    #         for i in dataframe.columns:
    #             dataframe.iloc[:,i] = self.drop_noise(dataframe.iloc[:,i])
        
    #     return MVH_OBJECT.discard_missing_values(dataframe= dataframe, column_id= column_id)
        
    # def replace_noise(self, series, operation_type = 0, val = np.NaN):
    #     '''
    #         This function replaces the noise by performing the operation you specified on given columns.
            
    #         Args:
    #         -----
    #         series (`pandas.Series`): the whole series.
    #         operation_type (`Intiger`): Type of the operation.
    #             - 0 : Replace with Mean.
    #             - 1 : Replace with Median.
    #             - 2 : Replace with Mode.
    #             - 3 : Replace with End of Distribution.
    #             - 4 : Replace with a random sample.
    #             - 5 : Replace with an arbitrary value. \n
    #         val (`Intiger`) (default = `numpy.NaN`): Value to be replaced in place of the noise in the case of the arbitrary value imputation.  
            
    #         Returns:
    #         --------
    #         series (`pandas.Series`): Updated series.
    #     '''
        
    #     #? Replacing noise with NaN
    #     series = self.drop_noise(series)
        
    #     if operation_type == 0:
    #         #? Handling with Mean
    #         series = MVH_OBJECT.mean_imputation(series)
        
    #     elif operation_type == 1:
    #         #? Handling with Median
    #         series = MVH_OBJECT.median_imputation(series)
        
    #     elif operation_type == 2:
    #         #? Handling with Mode
    #         series = MVH_OBJECT.mode_imputation(series)
        
    #     elif operation_type == 3:
    #         #? Handling with end of distribution
    #         series = MVH_OBJECT.end_of_distribution(series)
        
    #     elif operation_type == 4:
    #         #? Handling with random sample imputation
    #         series = MVH_OBJECT.random_sample_imputation(series)
        
    #     elif operation_type == 5:
    #         #? Handling with Arbitrary value
    #         series = MVH_OBJECT.add_missing_category(series, val)
        
    #     return series
        
    # def to_string_col(self, Series, cols):
    #     pass
    
    def detect_noise(self, DBObject, connection, table_name, column_name):
        '''
            Detects if there is removable noise present in the column.
        '''
        
        
    
    