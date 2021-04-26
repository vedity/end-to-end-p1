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
from . import common
commonObj = common.CommonClass()


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
    
    def discard_missing_values(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_1
        '''
        
        try:
            #Operation Id to get activity details
            operation_id = 'dp_1'

            logging.info("data preprocessing : CleaningClass : discard_missing_values : execution start")

            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
            
            for i,col_name in enumerate(cols):

                    status = 1
                    #Insert the activity for the operation
                    activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                    status = super(CleaningClass,self).discard_missing_values(DBObject,connection, table_name,old_cols[i])
                    if status ==0:
                        #Update the activity status for the operation performed
                        at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                    
            logging.info("data preprocessing : CleaningClass : discard_missing_values : execution stop")
            return status
        except Exception as exc:
            logging.info("data preprocessing : CleaningClass : discard_missing_values : Exception :"+str(exc))
            return str(exc)
        
    
    def mean_imputation(self, DBObject,connection,project_id,column_list,old_column_list,table_name, col,flag = False, **kwargs):
        '''
            Operation id: dp_51
        '''
        
        logging.info("data preprocessing : CleaningClass : mean_imputation : execution start" + str(col))

        #Operation Id to get activity details
        operation_id = 'dp_51'

        #Extract the column name based on the column id's
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            try:
                status = 1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                sql_command = 'select AVG(cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)

                if flag == True:
                    return impute_value
            
                status = commonObj.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mean_imputation : execution stop")
        return status
    
    def median_imputation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_61
        '''
        
        logging.info("data preprocessing : CleaningClass : median_imputation : execution start")
        
        #Operation Id to get activity details
        operation_id = 'dp_61'
        
        #Extract the column name based on the column id's
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                #Update the activity status for the operation performed
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)
                
                if status == 0:
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            
            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : median_imputation : execution stop")
        return status
    
    def mode_imputation(self,  DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_71
        '''
        logging.info("data preprocessing : CleaningClass : mode_imputation : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_71'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select MODE() WITHIN GROUP (ORDER BY cast ("'+str(old_cols[i])+'" as float)) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)
                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : mode_imputation : execution stop")
        return status
    
    def end_of_distribution(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_91
        '''
        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_91'

        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)


                sql_command = 'select (AVG(cast ("'+str(old_cols[i])+'" as float))+3*STDDEV(cast ("'+str(old_cols[i])+'" as float))) AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : end_of_distribution : execution stop")
        return status

    def missing_category_imputation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col,value ,flag = False, **kwargs):
        '''
            Operation id: dp_81
        '''
        logging.info(" checking " +str(value))
        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        logging.info(str(cols) + " " +str(value))
        
        #Operation Id to get activity details
        if not flag:
            operation_id = 'dp_111'
        else:
            operation_id = 'dp_81'

        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                if not flag:
                    value = "'"+value+"'"
            
                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],value)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                logging.error(str(exc))
                return exc

        logging.info("data preprocessing : CleaningClass : missing_category_imputation : execution stop")
        return status
    
   
    def frequent_category_imputation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_101
        '''
        
        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_101'

        
        for i,col_name in enumerate(cols):
            try:
                
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select "'+str(old_cols[i])+'" as impute_value,count(*) from '+str(table_name)+' where "'+old_cols[i]+'" is not null group by "'+old_cols[i]+'" order by count desc limit 1'
                logging.info(" sql_command : frequent_category_imputation " + str(sql_command))
                dataframe = DBObject.select_records(connection,sql_command)
                if len(dataframe['impute_value'])==0:
                    impute_value = 0
                else:
                    impute_value = "'"+str(dataframe['impute_value'][0])+"'"
                
                logging.info(str(impute_value) + " impute_value ")

                status = self.perform_missing_value_imputation(DBObject,connection, table_name,old_cols[i],impute_value)
                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
            

        logging.info("data preprocessing : CleaningClass : frequent_category_imputation : execution stop")
        return status
    
    def random_sample_imputation(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_121
        '''
        
        logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_121'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

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
                
                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                 
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : random_sample_imputation : execution stop")
        return status
    
    
    
    def remove_noise(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_41
        '''
        
        logging.info("data preprocessing : CleaningClass : remove_noise : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_41'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)
                
                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc

        logging.info("data preprocessing : CleaningClass : remove_noise : execution stop")
        return status
    
    def discard_noise(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_11
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_11'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.discard_missing_values(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_mean(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_131
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_131'
        
        for i,col_name in enumerate(cols):
            try:

                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.mean_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mean : execution stop")
        return status
    
    def repl_noise_median(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_141
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_141'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.median_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_median : execution stop")
        return status
    
    def repl_noise_mode(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_151
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_151'
        
        for i,col_name in enumerate(cols):
            try:

                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.mode_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_mode : execution stop")
        return status
    
    def repl_noise_eod(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_161
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_161'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.end_of_distribution(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_eod : execution stop")
        return status
    
    def repl_noise_random_sample(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_171
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_171'
        
        for i,col_name in enumerate(cols):
            try:
                status=1
                
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.random_sample_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col)

        logging.info("data preprocessing : CleaningClass : repl_noise_random_sample : execution stop")
        return status
    
    def repl_noise_arbitrary_val(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: dp_181
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_181'
        
        for i,col_name in enumerate(cols):
            try:

                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.rmv_noise(DBObject, connection, old_cols[i], table_name)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return exc
        if status == 0:
            status = self.missing_category_imputation(DBObject, connection,project_id,column_list,old_column_list, table_name, col, value)

        logging.info("data preprocessing : CleaningClass : repl_noise_arbitrary_val : execution stop")
        return status
    
    
    #* OUTLIER ANALYSIS
    
    def delete_above(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col,val, **kwargs):
        '''
            Operation id: dp_21
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_21'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().delete_above(DBObject,connection,table_name,old_cols[i],val)
                logging.info(str(status))
                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def delete_below(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col,val, **kwargs):
        '''
            Operation id: dp_31
        '''
        
        logging.info("data preprocessing : CleaningClass : delete_below : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_31'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().delete_below(DBObject,connection,table_name,old_cols[i],val)
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : delete_below : execution stop")
        return status
    
    def rem_outliers_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_191
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_191'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.remove_outliers(DBObject,connection,dataset_table_name,old_cols[i], detect_method = 0)
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_ext_val_analysis : execution stop")
        return status
    
    def rem_outliers_z_score(self,DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_201
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_201'
        
        for i,col_name in enumerate(cols):
            try:
                
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.remove_outliers(DBObject,connection,dataset_table_name,old_cols[i], detect_method = 1)
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : rem_outliers_z_score : execution stop")
        return status
    
    def rem_outliers_lof(self, DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_202
        '''
        
        logging.info("data preprocessing : CleaningClass : rem_outliers_lof : execution start")

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_202'
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                status = self.remove_outliers(DBObject,connection,dataset_table_name,old_cols[i], detect_method = 2)

                if status == 0:
                    #Update the activity status for the operation performed
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    
                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : rem_outliers_lof : execution stop")
        return status

    
    def repl_outliers_mean_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_211
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_211'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                logging.info(str(sql_command) + " sql_command")
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)                
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mean_z_score(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_221
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution start")
        

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_221'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_z_score : execution stop")
        return status
    
    def repl_outliers_med_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_231
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution start")

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_231'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_med_z_score(self,DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_241
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution start")
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_241'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_med_z_score : execution stop")
        return status
    
    def repl_outliers_mode_ext_val_analysis(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_7
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_7'
        
        for i,col_name in enumerate(cols):
            try:

                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select MODE() WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value, 0)
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_ext_val_analysis : execution stop")
        return status
    
    def repl_outliers_mode_z_score(self, DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: dp_7
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_7'
        
        for i,col_name in enumerate(cols):
            try:
                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(table_name)
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                status = self.replace_outliers(DBObject,connection,table_name,old_cols[i],impute_value,1)

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mode_z_score : execution stop")
        return status
    

    def repl_outliers_mean_lof(self, DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_242
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_lof : execution start")
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_242'
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select AVG("'+old_cols[i]+'") AS impute_value from '+str(dataset_table_name)
                logging.info(str(sql_command) + " sql_command")
                dataframe = DBObject.select_records(connection,sql_command)
                impute_value = round(dataframe['impute_value'][0],5)
                
                #Detect method Number to be called in replace outlier function 
                detect_method = 3

                status = self.replace_outliers(DBObject,connection,dataset_table_name,old_cols[i],impute_value, detect_method,method_type = 0)                
                logging.info(str(status))

                if status == 0:
                    #Update the activity status for the operation performed
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
            except Exception as exc:
                return str(exc)

        logging.info("data preprocessing : CleaningClass : repl_outliers_mean_lof : execution stop")
        return status
    
    def repl_outliers_median_lof(self, DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_243
        '''
        
        logging.info("data preprocessing : CleaningClass : repl_outliers_median_lof : execution start")

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Operation Id to get activity details
        operation_id = 'dp_243'
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                sql_command = 'select PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "'+str(old_cols[i])+'") AS impute_value from '+str(dataset_table_name)
                logging.info(sql_command)
                dataframe = DBObject.select_records(connection,sql_command)

                impute_value = round(dataframe['impute_value'][0],5)
                
                #Detect method Number to be called in replace outlier function 
                detect_method = 3
                status = self.replace_outliers(DBObject,connection,dataset_table_name,old_cols[i],impute_value, detect_method,method_type = 0)

                if status == 0:
                    #Update the activity status for the operation performed
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
                logging.info(str(status))
            except Exception as exc:
                return str(exc)
            
        logging.info("data preprocessing : CleaningClass : repl_outliers_median_lof : execution stop")
        return status




    def repl_outliers_iqr_proximity(self,DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_244
        '''
        logging.info("data preprocessing : CleaningClass : repl_outliers_iqr_proximity : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            #Operation Id to get activity details
            operation_id ='dp_244'
            
            for i,col_name in enumerate(cols):

                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                status = super().replace_outliers(DBObject,connection,dataset_table_name,old_cols[i],impute_value = None , detect_method = 2,method_type = 'iqr_proximity')
                
                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                logging.info("data preprocessing : CleaningClass : repl_outliers_iqr_proximity : Exception : "+str(exc))
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_iqr_proximity : execution stop")
        return status
    

    def repl_outliers_Gaussian_approx(self,DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: dp_245
        '''
        logging.info("data preprocessing : CleaningClass : repl_outliers_Gaussian_approx : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            #Operation Id to get activity details
            operation_id = 'dp_245'
            
            for i,col_name in enumerate(cols):

                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                status = super().replace_outliers(DBObject,connection,dataset_table_name,old_cols[i],impute_value = None , detect_method = 2,method_type = 'Gaussian_approx')
                
                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                logging.info("data preprocessing : CleaningClass : repl_outliers_Gaussian_approx : Exception : "+str(exc))
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_Gaussian_approx : execution stop")
        return status
    
    def repl_outliers_quantiles(self,DBObject,connection,project_id,column_list,old_column_list, dataset_table_name,col, **kwargs):
        '''
            Operation id: ?
        '''
        logging.info("data preprocessing : CleaningClass : repl_outliers_quantiles : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            # #Operation Id to get activity details
            # operation_id = ?
            
            for i,col_name in enumerate(cols):

                # #Insert the activity for the operation
                # activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                lower_limit,upper_limit = super().get_upper_lower_limit(DBObject,connection,col_name,dataset_table_name,method_type = 'quantiles' ,quantile_1=0.25,quantile_2=0.75)
                status = super().update_outliers(DBObject,connection,lower_limit,upper_limit,old_cols[i],dataset_table_name)
                
                #Update the activity status for the operation performed
                # if status == 0:
                #     status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                # else:
                #     status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                logging.info("data preprocessing : CleaningClass : repl_outliers_quantiles : Exception : "+str(exc))
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_quantiles : execution stop")
        return status
    
    def repl_outliers_arbitrarily(self,DBObject,connection,project_id,column_list,old_column_list, table_name,col, **kwargs):
        '''
            Operation id: ?
        '''
        logging.info("data preprocessing : CleaningClass : repl_outliers_arbitrarily : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            # #Operation Id to get activity details
            # operation_id = ?
            
            for i,col_name in enumerate(cols):

                # #Insert the activity for the operation
                # activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)
                
                lower_limit = 10
                upper_limit = 90
                status = super().update_outliers(DBObject,connection,lower_limit,upper_limit,old_cols[i],table_name)
                
                # #Update the activity status for the operation performed
                # at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                logging.info("data preprocessing : CleaningClass : repl_outliers_arbitrarily : Exception : "+str(exc))
                return str(exc)
        logging.info("data preprocessing : CleaningClass : repl_outliers_arbitrarily : execution stop")
        return status


        
    def apply_log_transformation(self,DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            Operation id: dp_251
        '''
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution start")
        try:
            
            #Extract the column name based on the column id's
            cols = [column_list[i] for i in col]
            old_cols = [old_column_list[i] for i in col]
        
            #Operation Id to get activity details
            operation_id = 'dp_251'
            
            
        
            for i,col_name in enumerate(cols):

                status =1
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().apply_log_transformation(DBObject,connection,table_name,old_cols[i])

                if status == 0:
                    #Update the activity status for the operation performed
                    at_status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
                return str(exc)
        logging.info("data preprocessing : CleaningClass : apply_log_transformation : execution stop")
        return status
    



    
