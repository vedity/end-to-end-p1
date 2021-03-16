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
from . import outlier_sql as ot
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
    
    def discard_missing_values(self,DBObject,connection,column_list, table_name, col):
        '''
            Operation id: 1
        '''
        
        logging.info("data preprocessing : CleaningClass : discard_missing_values : execution start")
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for column in cols:
                status = super().discard_missing_values(DBObject,connection, table_name,column)
        logging.info("data preprocessing : CleaningClass : discard_missing_values : execution stop")
        return status
    
    def mean_imputation(self, DBObject,connection,column_list, table_name, col,flag = False):
        '''
            Operation id: 6
        '''
        
        logging.info("data preprocessing : CleaningClass : mean_imputation : execution start" + str(col))

        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select AVG(cast ("'+str(col_name)+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)

                if flag == True:
                    return impute_value
                    
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,impute_value)
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mean_imputation : execution stop")
        return status
    
    def median_imputation(self, DBObject,connection,column_list, table_name, col):
        '''
            Operation id: 5
        '''
        
        logging.info("data preprocessing : CleaningClass : median_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cast ("'+str(col_name)+'" as float)) AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,impute_value)
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : median_imputation : execution stop")
        return status
    
    def mode_imputation(self,  DBObject,connection,column_list, table_name, col):
        '''
            Operation id: ?
        '''
        logging.info("data preprocessing : CleaningClass : mode_imputation : execution start")
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select MODE() WITHIN GROUP (ORDER BY cast ("'+str(col_name)+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,impute_value)
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mode_imputation : execution stop")
        return status
    
    def end_of_distribution(self,DBObject,connection,column_list, table_name, col):
        '''
            Operation id: ?
        '''
        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution start")
        cols = [column_list[i] for i in col]
        
        for col_name in cols:
            try:
                sql_command = 'select (AVG(cast ("'+str(col_name)+'" as float))+3*STDDEV(cast ("'+str(col_name)+'" as float))) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,impute_value)
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution stop")
        return status

    def missing_category_imputation(self,DBObject,connection,column_list, table_name, col,value ,flag = False):
        '''
            Operation id: 8
        '''
        logging.info(" checking " +str(value))
        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols) + " " +str(value))
        for i,col_name in enumerate(cols):
            try:
                if not flag:
                    value = "'"+value[i]+"'"
            
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,value)
            except Exception as exc:
                logging.error(str(exc))
                return exc

        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution stop")
        return status
    
    
    def frequent_category_imputation(self,DBObject,connection,column_list, table_name, col):
        '''
            Operation id: 8
        '''
        
        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select "'+str(col_name)+'" as impute_value,count(*) from '+str(table_name)+' group by "'+col_name+'" order by count desc limit 1'
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = "'"+str(dataframe['impute_value'][0])+"'"

                status = self.perform_missing_value_imputation(DBObject,connection, table_name,col_name,impute_value)
            
            except Exception as exc:
                return exc
            

        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution stop")
        return status
    
    def random_sample_imputation(self, DBObject,connection,column_list, table_name,col):
        '''
            Operation id: 10
        '''
        
        logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = f'select distinct "{col_name}" as distinct_value from {table_name}'
                logging.info("Sql_command : Select query : random_sample_imputation : "+str(sql_command))

                dataframe = DBObject.select_records(connection,sql_command)
                logging.info(str(dataframe))
                list_value = list(dataframe['distinct_value'])
                impute_string = ''
                for value in list_value:
                    impute_string += '('+str(value)+'),'

                impute_string = impute_string[:len(impute_string)-1]
        
                status = super().random_sample_imputation(DBObject,connection,table_name,col_name,impute_string)
                 
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution stop")
        return status
    
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
    
    #* NOISE HANDLING
    
    def remove_noise(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: 11
        '''
        
        logging.info("data preprocessing : CleaningClass : remove_noise : execution start")
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : remove_noise : execution stop")
        return status
    
    def discard_noise(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: 12
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.discard_missing_values(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_mean(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: 12
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.mean_imputation(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_median(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: 13
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.median_imputation(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution stop")
        return status
    
    def repl_noise_mode(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.mode_imputation(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution stop")
        return status
    
    def repl_noise_eod(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.end_of_distribution(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution stop")
        return status
    
    def repl_noise_random_sample(self, DBObject,connection, column_list, table_name, col):
        '''
            Operation id: 14
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.random_sample_imputation(DBObject, connection, column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution stop")
        return status
    
    def repl_noise_arbitrary_val(self, DBObject,connection, column_list, table_name, col, value):
        '''
            Operation id: 15
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution start")
        
        cols = [column_list[i] for i in col]
        for col_name in cols:
            try:
                status = self.rmv_noise(DBObject, connection, col_name, table_name)
            except Exception as exc:
                return exc
        if status == 0:
            status = self.missing_category_imputation(DBObject, connection, column_list, table_name, col, value)

        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution stop")
        return status
    
    
    #* OUTLIER ANALYSIS
    
    def delete_above(self, DBObject,connection,column_list, table_name,col,val):
        '''
            Operation id: 2
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for i,col_name in enumerate(cols):
            try:

                status = super().delete_above(DBObject,connection,table_name,col_name,val[i])
                logging.info(str(status))
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def delete_below(self, DBObject,connection,column_list, table_name,col,val):
        '''
            Operation id: 3
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for i,col_name in enumerate(cols):
            try:

                status = super().delete_below(DBObject,connection,table_name,col_name,val[i])
                logging.info(str(status))
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def rem_outliers_ext_val_analysis(self, DBObject,connection,column_list, dataset_table_name,col):
        '''
            Operation id: 16
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:

                status = self.remove_outliers(DBObject,connection,dataset_table_name,col_name, detect_method = 0)
                logging.info(str(status))
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution stop")
        return status
    
    def rem_outliers_z_score(self,DBObject,connection,column_list, dataset_table_name,col):
        '''
            Operation id: 17
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                
                status = self.remove_outliers(DBObject,connection,dataset_table_name,col_name, detect_method = 1)
                logging.info(str(status))

            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution stop")
        return status

    
    def repl_outliers_mean_ext_val_analysis(self, DBObject,connection,column_list, table_name,col):
        '''
            Operation id: 18
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select AVG("'+col_name+'") AS impute_value from '+str(table_name)
                logging.info(str(sql_command) + " sql_command")
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value, 0)
                logging.info(str(status))
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mean_z_score(self, DBObject,connection,column_list, table_name, col):
        '''
            Operation id: 19
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution start")
        

        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select AVG("'+col_name+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value,1)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution stop")
        return status
    
    def repl_outliers_med_ext_val_analysis(self, DBObject,connection,column_list, table_name,col):
        '''
            Operation id: 20
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution start")

        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(col_name)+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value, 0)
                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_med_z_score(self,DBObject,connection,column_list, table_name,col):
        '''
            Operation id: 21
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution start")
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(col_name)+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value,1)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution stop")
        return status
    
    def repl_outliers_mode_ext_val_analysis(self, DBObject,connection,column_list, table_name,col):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select MODE() WITHIN GROUP (ORDER BY "'+str(col_name)+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value, 0)
                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mode_z_score(self, DBObject,connection,column_list, table_name,col):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        logging.info(str(cols))
        for col_name in cols:
            try:
                sql_command = 'select AVG("'+col_name+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,col_name,impute_value,1)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution stop")
        return status
    
    def apply_log_transformation(self,DBObject,connection,column_list, table_name, col):
        '''
            Operation id: 22
        '''
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution start")
        try:
            
            cols = [column_list[i] for i in col]
            logging.info(str(cols))
            for col_name in cols:
                
                status = super().apply_log_transformation(DBObject,connection,table_name,col_name)
                
        except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution stop")
        return status
    
    def delete_duplicate_records(self,DBObject,connection,column_list, table_name):
        logging.info("data preprocessing : CleaningClass : delete_duplicate_records : execution start")
        try:
            
            col_string = ''
            for x in column_list:
                col_string += '"'+str(x)+'",'

            status = super().delete_duplicate_records(DBObject,connection,table_name,col_string[:-1])
                
        except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_duplicate_records : execution stop")
        return status
