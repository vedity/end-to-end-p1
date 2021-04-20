'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging
import traceback
import pandas as pd

#* Relative Imports
from . import outlier_sql as ot
from . import noise_reduction as nr
from . import missing_value_handling as mvh

#* Commong Utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.activity_timeline import activity_timeline
from database import *


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
    
    def __init__(self):
        self.op_diff = 8
        self.AT = activity_timeline.ActivityTimelineClass(database, user, password, host, port)
        
    
    #* MISSING VALUE HANDLING
    
    def discard_missing_values(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 1
        '''
        
        
        #Operation Id to get activity details
        operation_id = 1

        logging.info("data preprocessing : CleaningClass : discard_missing_values : execution start")

        #Extract the column name based on the column id's
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):

                status = 1
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super(CleaningClass,self).discard_missing_values(DBObject,connection, table_name,old_cols[i])
                if status ==0:
                    #Update the activity status for the operation performed
                    at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
        logging.info("data preprocessing : CleaningClass : discard_missing_values : execution stop")
        return status
    
    def mean_imputation(self, DBObject,connection,project_id,column_list,old_column_list,table_name, col,flag = False, **kwargs):
        '''
            Operation id: 6
        '''
        
        logging.info("data preprocessing : CleaningClass : mean_imputation : execution start" + str(col))

        #Operation Id to get activity details
        operation_id = 6

        #Extract the column name based on the column id's
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                sql_command = 'select AVG(cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)

                if flag == True:
                    return impute_value
                    
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mean_imputation : execution stop")
        return status
    
    def median_imputation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 7
        '''
        
        logging.info("data preprocessing : CleaningClass : median_imputation : execution start")
        
        #Operation Id to get activity details
        operation_id = 7
        
        #Extract the column name based on the column id's
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                #Update the activity status for the operation performed
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : median_imputation : execution stop")
        return status
    
    def mode_imputation(self,  DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 8
        '''
        logging.info("data preprocessing : CleaningClass : mode_imputation : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 8
        
        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select MODE() WITHIN GROUP (ORDER BY cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mode_imputation : execution stop")
        return status
    
    def end_of_distribution(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 10
        '''
        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 10

        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)


                sql_command = 'select (AVG(cast ("'+str(old_cols[i])+'" as float))+3*STDDEV(cast ("'+str(old_cols[i])+'" as float))) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution stop")
        return status

    def missing_category_imputation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col,value ,flag = False, **kwargs):
        '''
            Operation id: 12
        '''
        logging.info(" checking " +str(value))
        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        logging.info(str(cols) + " " +str(value))
        
        #Operation Id to get activity details
        if not flag:
            operation_id = 12
        else:
            operation_id = 9

        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                if not flag:
                    value = "'"+value+"'"
            
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],value)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                logging.error(str(exc))
                return exc

        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution stop")
        return status
    
   
    def frequent_category_imputation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 11
        '''
        
        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 11

        
        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select "'+str(old_cols[i])+'" as impute_value,count(*) from '+str(table_name)+' where "'+old_cols[i]+'" is not null group by "'+old_cols[i]+'" order by count desc limit 1'
                logging.info(" sql_command : frequent_category_imputation " + str(sql_command))
                dataframe = DBObject.select_records(connection,sql_command)
                if len(dataframe['impute_value'])==0:
                    impute_value = 0
                else:
                    impute_value = "'"+str(dataframe['impute_value'][0])+"'"
                
                logging.info(str(impute_value) + " impute_value ")

                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
            

        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution stop")
        return status
    
    def random_sample_imputation(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: 13
        '''
        
        logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 13
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = f'select distinct "{old_cols[i]}" as distinct_value from {table_name}'
                logging.info("Sql_command : Select query : random_sample_imputation : "+str(sql_command))

                dataframe = DBObject.select_records(connection,sql_command)
                logging.info(str(dataframe))
                list_value = list(dataframe['distinct_value'])
                impute_string = ''
                for value in list_value:
                    impute_string += '('+str(value)+'),'

                impute_string = impute_string[:len(impute_string)-1]
        
                status = super().random_sample_imputation(DBObject,connection,table_name,old_cols[i],impute_string)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                 
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
    
    def remove_noise(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 5
        '''
        
        logging.info("data preprocessing : CleaningClass : remove_noise : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 5
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : remove_noise : execution stop")
        return status
    
    def discard_noise(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 2
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 2
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.discard_missing_values(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_mean(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 14
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 14
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.mean_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_median(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 15
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 15
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.median_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution stop")
        return status
    
    def repl_noise_mode(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 16
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 16
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.mode_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution stop")
        return status
    
    def repl_noise_eod(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 17
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 17
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.end_of_distribution(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution stop")
        return status
    
    def repl_noise_random_sample(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 18
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 18
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.random_sample_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution stop")
        return status
    
    def repl_noise_arbitrary_val(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: 19
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 19
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.missing_category_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col, value)

        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution stop")
        return status
    
    
    #* OUTLIER ANALYSIS
    
    def delete_above(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col,val, **kwargs):
        '''
            Operation id: 3
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 3
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().delete_above(DBObject,connection,table_name,old_cols[i],val)
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def delete_below(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col,val, **kwargs):
        '''
            Operation id: 4
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 4
        
        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().delete_below(DBObject,connection,table_name,old_cols[i],val)
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def rem_outliers_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: 20
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 20
        
        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.remove_outliers(DBObject,connection,dataset_table_name,old_cols[i], detect_method = 0)
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution stop")
        return status
    
    def rem_outliers_z_score(self,DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: 21
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 21
        
        for i,col_name in enumerate(cols):
            try:
                
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.remove_outliers(DBObject,connection,dataset_table_name,old_cols[i], detect_method = 1)
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution stop")
        return status

    
    def repl_outliers_mean_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: 22
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 22
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                logging.info(str(sql_command) + " sql_command")
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)                
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mean_z_score(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 23
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution start")
        

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 23
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution stop")
        return status
    
    def repl_outliers_med_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: 24
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution start")

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 24
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_med_z_score(self,DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: 25
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 25
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution stop")
        return status
    
    def repl_outliers_mode_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 7
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select MODE() WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)
                logging.info(str(status))

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mode_z_score(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 7
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution stop")
        return status
    
    def apply_log_transformation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: 26
        '''
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            #Operation Id to get activity details
            operation_id = 26
            
            
        
            for i,col_name in enumerate(cols):

                #Insert the activity for the operation
                activity_id = self.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().apply_log_transformation(DBObject,connection,table_name,old_cols[i])

                #Update the activity status for the operation performed
                at_status = self.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution stop")
        return status
    
    def delete_duplicate_records(self,DBObject,connection,project_id,column_list,old_column_list, table_name, **kwargs):
        '''
            Operation id: ?
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_duplicate_records : execution start")
        try:
            
            col_string = ''
            # operation_id = 7
            for x in column_list:
                col_string += '"'+str(x)+'",'
    
            status = super().delete_duplicate_records(DBObject,connection,table_name,col_string[:-1])
                
        except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_duplicate_records : execution stop")
        return status


    #* ACTIVITY TIMELINE FUNCTIONS
    
    def get_act_desc(self, DBObject, connection, operation_id, col_name, code = 1):
        '''
            Used to get preprocess activity description from the activity master table.
        
            Returns:
            --------
            description (`String`): Description for the activity.
        '''
        logging.info("data preprocessing : CleaningClass : get_activity_desc : execution start")
        
        #? Getting Description
        sql_command = f"select replace (amt.activity_name || ' ' || amt.activity_description, '*', '{col_name}') as description from mlaas.activity_master_tbl amt where amt.activity_id = '{operation_id}' and amt.code = '{code}'"
        
        
        desc_df = DBObject.select_records(connection,sql_command)
        if not isinstance(desc_df, pd.DataFrame):
            return "Failed to Extract Activity Description."
        
        #? Fatching the description
        description = desc_df['description'].tolist()[0]
        
        logging.info("data preprocessing : CleaningClass : get_activity_desc : execution stop")
        
        return description
            
    def operation_start(self, DBObject, connection, operation_id, project_id, col_name):
        '''
            Used to Insert Activity in the Activity Timeline Table.
            
            Returns:
            --------
            activity_id (`Intiger`): index of the activity in the activity transection table.
        '''
        logging.info("data preprocessing : CleaningClass : operation_start : execution start")
            
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        operation_id += self.op_diff
        
        #? Getting Activity Description
        desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 1)
        
        #? Getting Dataset_id & User_Name
        sql_command = f"select pt.dataset_id,pt.user_name from mlaas.project_tbl pt where pt.project_id = '{project_id}'"
        details_df = DBObject.select_records(connection,sql_command) 
        dataset_id,user_name = int(details_df['dataset_id'][0]),details_df['user_name'][0]

        #? Inserting the activity in the activity_detail_table
        _,activity_id = self.AT.insert_user_activity(operation_id,user_name,project_id,dataset_id,desc,column_id =col_name)
        
        logging.info("data preprocessing : CleaningClass : operation_start : execution stop")
        
        return activity_id
    
    def operation_end(self, DBObject, connection, activity_id, operation_id, col_name):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        
        logging.info("data preprocessing : CleaningClass : operation_end : execution start")
        
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        operation_id += self.op_diff
        
        #? Getting Activity Description
        desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 2)
        
        #? Changing the activity description in the activity detail table 
        status = self.AT.update_activity(activity_id,desc)
        
        logging.info("data preprocessing : CleaningClass : operation_end : execution stop")
        
        return status
    
    def operation_failed(self, DBObject, connection, activity_id, operation_id, col_name):
        '''
            Used to update Activity description when the Activity ends.
            
            Returns:
            --------
            status (`Intiger`): Status of the updation.
        '''
        
        logging.info("data preprocessing : CleaningClass : operation_end : execution start")
        
        #? Transforming the operation_id to the operation id stored in the activity timeline table. 
        operation_id += self.op_diff
        
        #? Getting Activity Description
        desc = self.get_act_desc(DBObject, connection, operation_id, col_name, code = 0)
        
        #? Changing the activity description in the activity detail table 
        status = self.AT.update_activity(activity_id,desc)
        
        logging.info("data preprocessing : CleaningClass : operation_end : execution stop")
        
        return status
    