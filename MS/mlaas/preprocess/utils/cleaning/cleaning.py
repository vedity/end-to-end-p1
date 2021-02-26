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

class CleaningClass(ot.OutliersTreatmentClass, nr.RemoveNoiseClass):
    
    def rem_outliers_ext_val_analysis(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df = self.remove_outliers(data_df, column)
            
        return data_df
    
    def rem_outliers_z_score(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df = self.remove_outliers(data_df, column, detect_method= 1)
            
        return data_df
    
    def repl_outliers_med_ext_val_analysis(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df[column] = self.replace_outliers(data_df[column], operation=1)
            
        return data_df
    
    def repl_outliers_med_z_score(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df[column] = self.replace_outliers(data_df[column], operation=1, detect_method = 1)
            
        return data_df
    
    def repl_outliers_mean_ext_val_analysis(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df[column] = self.replace_outliers(data_df[column])
            
        return data_df
    
    def repl_outliers_mean_ext_val_analysis(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df[column] = self.replace_outliers(data_df[column], detect_method= 1)
            
        return data_df
    
    def apply_log_transformation(self, data_df, col):
        
        cols = [data_df.columns[i] for i in col]
        
        for column in cols:
            data_df[column] = super().apply_log_transformation(series= data_df[column])
            
        return data_df
    