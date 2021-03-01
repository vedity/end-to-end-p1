'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging
import traceback

#* Relative Imports
from . import outliers_treatment as ot
from . import noise_reduction as nr
from . import missing_value_handling as mvh

class CleaningClass(mvh.MissingValueClass, nr.RemoveNoiseClass, ot.OutliersTreatmentClass):
    '''
        Handles orchastration of the cleaning related Functions.
    '''
    
    #* MISSING VALUE HANDLING
    
    def discard_missing_values(self, data_df, col, whole = False):
        '''
            Operation id: 1
        '''
        
        if whole:
            #? Perform operation on whole dataframe.
            col = None
        
        return super().discard_missing_values(data_df, col)
    
    def mean_imputation(self, data_df, col):
        '''
            Operation id: 4
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().mean_imputation(data_df[column])
            except:
                continue

        return data_df
    
    def median_imputation(self, data_df, col):
        '''
            Operation id: 5
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().median_imputation(data_df[column])
            except:
                continue

        return data_df
    
    def mode_imputation(self, data_df, col):
        '''
            Operation id: ?
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().mode_imputation(data_df[column])
            except:
                continue

        return data_df
    
    def arbitrary_value_imputation(self, data_df, col, val):
        '''
            Operation id: 6
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().add_missing_category(data_df[column], val)
            except:
                continue

        return data_df
    
    def end_of_distribution(self, data_df, col):
        '''
            Operation id: 7
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().end_of_distribution(data_df[column])
            except:
                continue

        return data_df
    
    def frequent_category_imputation(self, data_df, col):
        '''
            Operation id: 8
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().frequent_category_imputation(data_df[column])
            except:
                continue

        return data_df
    
    def add_missing_category(self, data_df, col):
        '''
            Operation id: 9
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().add_missing_category(data_df[column])
            except:
                continue

        return data_df
    
    def random_sample_imputation(self, data_df, col):
        '''
            Operation id: 10
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().random_sample_imputation(data_df[column])
            except:
                continue

        return data_df
    
    
    
    #* NOISE HANDLING
    
    def remove_noise(self, data_df, col):
        '''
            Operation id: 11
        '''
        
        return super().remove_noise(dataframe= data_df, column_id= col)
    
    def repl_noise_mean(self, data_df, col):
        '''
            Operation id: 12
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 0)
            except:
                continue

        return data_df
    
    def repl_noise_median(self, data_df, col):
        '''
            Operation id: 13
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 1)
            except:
                continue

        return data_df
    
    def repl_noise_mode(self, data_df, col):
        '''
            Operation id: ?
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 2)
            except:
                continue

        return data_df
    
    def repl_noise_eod(self, data_df, col):
        '''
            Operation id: ?
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 3)
            except:
                continue

        return data_df
    
    def repl_noise_random_sample(self, data_df, col):
        '''
            Operation id: 14
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 4)
            except:
                continue

        return data_df
    
    def repl_noise_arbitrary_val(self, data_df, col, val):
        '''
            Operation id: 15
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_noise(data_df[column], operation_type= 5, val= val)
            except:
                continue

        return data_df
    
    
    #* OUTLIER ANALYSIS
    
    def delete_above(self, data_df, col, val):
        '''
            Operation id: 2
        '''
        
        return super().delete_above(data_df, col, val)
    
    def delete_below(self, data_df, col, val):
        '''
            Operation id: 3
        '''
        
        return super().delete_below(data_df, col, val)
    
    def rem_outliers_ext_val_analysis(self, data_df, col):
        '''
            Operation id: 16
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df = self.remove_outliers(data_df, column)
            except:
                continue

        return data_df
    
    def rem_outliers_z_score(self, data_df, col):
        '''
            Operation id: 17
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df = self.remove_outliers(data_df, column, detect_method= 1)
            except:
                continue

        return data_df
    
    def repl_outliers_mean_ext_val_analysis(self, data_df, col):
        '''
            Operation id: 18
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column])
            except:
                continue

        return data_df
    
    def repl_outliers_mean_z_score(self, data_df, col):
        '''
            Operation id: 19
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column], detect_method= 1)
            except:
                continue

        return data_df
    
    def repl_outliers_med_ext_val_analysis(self, data_df, col):
        '''
            Operation id: 20
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column], operation=1)
            except:
                continue
            
        return data_df
    
    def repl_outliers_med_z_score(self, data_df, col):
        '''
            Operation id: 21
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column], operation=1, detect_method = 1)
            except:
                continue

        return data_df
    
    def repl_outliers_mode_ext_val_analysis(self, data_df, col):
        '''
            Operation id: ?
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column], operation=2)
            except:
                continue
            
        return data_df
    
    def repl_outliers_mode_z_score(self, data_df, col):
        '''
            Operation id: ?
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = self.replace_outliers(data_df[column], operation=2, detect_method = 1)
            except:
                continue

        return data_df
    
    def apply_log_transformation(self, data_df, col):
        '''
            Operation id: 22
        '''
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            try:
                data_df[column] = super().apply_log_transformation(series= data_df[column])
            except:
                continue

        return data_df
    