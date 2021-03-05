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

#* Commong Utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('cleaning')



class CleaningClass(mvh.MissingValueClass, nr.RemoveNoiseClass, ot.OutliersTreatmentClass):
    '''
        Handles orchastration of the cleaning related Functions.
    '''
    
    #* MISSING VALUE HANDLING
    
    # def discard_missing_values(self, data_df, col, whole = False):
    #     '''
    #         Operation id: 1
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : discard_missing_values : execution start")
        
    #     if whole:
    #         #? Perform operation on whole dataframe.
    #         col = None
        
    #     logging.info("data preprocessing : CleaningClass : discard_missing_values : execution stop")
    #     return super().discard_missing_values(DBObject,connection, table_name,col_name)
    
    def imputation(self,DBObject,connection,column_list, table_name, col, operation):
        
        logging.info("data preprocessing : CleaningClass : mean_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for column in cols:
            try:
                impute_value = self.get_impute_value(DBObject,connection,table_name,column,operation)
                status = super().missing_value_imputation(DBObject,connection, table_name,column,impute_value)

            except Exception as exc:
                logging.info(str(exc) + " error ")
                status =1
                continue

        logging.info("data preprocessing : CleaningClass : mean_imputation : execution stop")
        return status
    
    def get_impute_value(self,DBObject,connection,table_name,column_name,operation):

        if operation == 4:
            sql_command = 'select AVG("'+column_name+'") AS mean from '+str(table_name)
            logging.info(str(sql_command))
            dataframe = DBObject.select_records(connection,sql_command)
            impute_value = float(dataframe['mean'][0])
            
        elif operation == 5:
            sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(column_name)+'") AS median from '+str(table_name)
            logging.info(str(sql_command))
            dataframe = DBObject.select_records(connection,sql_command)
            impute_value = int(dataframe['median'][0])

        elif operation == 6:
            sql_command = 'select MODE() WITHIN GROUP (ORDER BY "'+str(column_name)+'") AS mode from '+str(table_name)
            logging.info(str(sql_command))
            dataframe = DBObject.select_records(connection,sql_command)
            impute_value = int(dataframe['mode'][0])
        
        elif operation == 7:
            sql_command = 'select ((select AVG("'+column_name+'") AS mean from '+str(table_name)+')+3*(select STDEV("'+column_name+'") AS mean from '+str(table_name)+')) as value'
            logging.info(str(sql_command))
            dataframe = DBObject.select_records(connection,sql_command)
            impute_value = int(dataframe['value'][0])

        return impute_value       
    
   
    
    # def arbitrary_value_imputation(self, data_df, col, val):
    #     '''
    #         Operation id: 6
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : arbitrary_value_imputation : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().add_missing_category(data_df[column], val)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : arbitrary_value_imputation : execution stop")
    #     return data_df
    
    # def end_of_distribution(self, data_df, col):
    #     '''
    #         Operation id: 7
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : end_of_distribution : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().end_of_distribution(data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : end_of_distribution : execution stop")
    #     return data_df
    
    # def frequent_category_imputation(self, data_df, col):
    #     '''
    #         Operation id: 8
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().frequent_category_imputation(data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution stop")
    #     return data_df
    
    # def add_missing_category(self, data_df, col):
    #     '''
    #         Operation id: 9
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : add_missing_category : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().add_missing_category(data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : add_missing_category : execution stop")
    #     return data_df
    
    # def random_sample_imputation(self, data_df, col):
    #     '''
    #         Operation id: 10
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().random_sample_imputation(data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution stop")
    #     return data_df
    
    
    
    # #* NOISE HANDLING
    
    # def remove_noise(self, data_df, col):
    #     '''
    #         Operation id: 11
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : remove_noise : execution start")
        
    #     logging.info("data preprocessing : CleaningClass : remove_noise : execution stop")
    #     return super().remove_noise(dataframe= data_df, column_id= col)
    
    # def repl_noise_mean(self, data_df, col):
    #     '''
    #         Operation id: 12
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 0)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
    #     return data_df
    
    # def repl_noise_median(self, data_df, col):
    #     '''
    #         Operation id: 13
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_median : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 1)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_median : execution stop")
    #     return data_df
    
    # def repl_noise_mode(self, data_df, col):
    #     '''
    #         Operation id: ?
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 2)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution stop")
    #     return data_df
    
    # def repl_noise_eod(self, data_df, col):
    #     '''
    #         Operation id: ?
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 3)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution stop")
    #     return data_df
    
    # def repl_noise_random_sample(self, data_df, col):
    #     '''
    #         Operation id: 14
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 4)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution stop")
    #     return data_df
    
    # def repl_noise_arbitrary_val(self, data_df, col, val):
    #     '''
    #         Operation id: 15
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_noise(data_df[column], operation_type= 5, val= val)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution stop")
    #     return data_df
    
    
    # #* OUTLIER ANALYSIS
    
    # def delete_above(self, data_df, col, val):
    #     '''
    #         Operation id: 2
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : delete_above : execution start")
        
    #     logging.info("data preprocessing : CleaningClass : delete_above : execution stop")
    #     return super().delete_above(data_df, col, val)
    
    # def delete_below(self, data_df, col, val):
    #     '''
    #         Operation id: 3
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        
    #     logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
    #     return super().delete_below(data_df, col, val)
    
    # def rem_outliers_ext_val_analysis(self, data_df, col):
    #     '''
    #         Operation id: 16
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df = self.remove_outliers(data_df, column)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution stop")
    #     return data_df
    
    # def rem_outliers_z_score(self, data_df, col):
    #     '''
    #         Operation id: 17
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df = self.remove_outliers(data_df, column, detect_method= 1)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution stop")
    #     return data_df
    
    # def repl_outliers_mean_ext_val_analysis(self, data_df, col):
    #     '''
    #         Operation id: 18
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution stop")
    #     return data_df
    
    # def repl_outliers_mean_z_score(self, data_df, col):
    #     '''
    #         Operation id: 19
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column], detect_method= 1)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution stop")
    #     return data_df
    
    # def repl_outliers_med_ext_val_analysis(self, data_df, col):
    #     '''
    #         Operation id: 20
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column], operation=1)
    #         except:
    #             continue
            
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution stop")
    #     return data_df
    
    # def repl_outliers_med_z_score(self, data_df, col):
    #     '''
    #         Operation id: 21
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column], operation=1, detect_method = 1)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution stop")
    #     return data_df
    
    # def repl_outliers_mode_ext_val_analysis(self, data_df, col):
    #     '''
    #         Operation id: ?
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column], operation=2)
    #         except:
    #             continue
            
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution stop")
    #     return data_df
    
    # def repl_outliers_mode_z_score(self, data_df, col):
    #     '''
    #         Operation id: ?
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = self.replace_outliers(data_df[column], operation=2, detect_method = 1)
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution stop")
    #     return data_df
    
    # def apply_log_transformation(self, data_df, col):
    #     '''
    #         Operation id: 22
    #     '''
        
    #     logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution start")
        
    #     cols = [data_df.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             data_df[column] = super().apply_log_transformation(series= data_df[column])
    #         except:
    #             continue

    #     logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution stop")
    #     return data_df
    