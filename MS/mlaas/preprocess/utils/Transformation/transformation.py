'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           TransformationClass
 
*/
'''

#* Library Imports
import logging
import traceback
import pandas as pd

#* Relative Imports
from . import duplicate_data_handling as ddh
from . import feature_scaling as fs
from . import categorical_encoding as ce
from . import math_functions as mf
from . import data_transformation as dt
from . import feature_engineering as fe

#* Commong Utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.activity_timeline import activity_timeline
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from database import *
from .. import common

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('transformation')

#* Object Initialize
commonObj = common.CommonClass()

class TransformationClass(ddh.RemoveDuplicateRecordClass, fs.FeaturnScalingClass, ce.EncodeClass, mf.MathOperationsClass, fe.FeatureEngineeringClass,dt.DataTransformationClass):
    '''
        Handles orchastration of the transforamtion related Functions.
    '''
    
    def __init__(self):
        # self.op_diff = 8
        self.AT = activity_timeline.ActivityTimelineClass(database, user, password, host, port)
    
    #* SCALING
    
    def standard_scaling(self, dataframe):
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().standard_scaling(dataframe)
    
    def min_max_scaling(self, dataframe):
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().min_max_scaling(dataframe)
    
    def robust_scaling(self, dataframe):
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution start")
        
        logging.info("data preprocessing : TransformationClass : duplicate_data_removal : execution stop")
        
        return super().robust_scaling(dataframe)
    
    #* Duplicate Deletion

    def delete_duplicate_records(self,DBObject,connection,project_id,column_list,old_column_list, table_name, **kwargs):
        '''
            Function will delete the duplicate records from the table.

            Operation id: 
        '''
        operation_id = 'dp_331'
        logging.info("data preprocessing : TransformationClass : delete_duplicate_records : execution start")
        try:
            
            col_string = ''
            operation_id = 'dp_331'
            #Insert the activity for the operation
            col_name = "blank"
            activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id,col_name)
                
            for x in old_column_list:
                if x != 'index':
                    col_string += '"'+str(x)+'",'
            
            status = super().delete_duplicate_records(DBObject,connection,table_name,col_string[:-1])
            #Update the activity status for the operation performed
            if status == 0:
                status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            else:
                status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
        except Exception as exc:
            logging.error("data preprocessing : TransformationClass : delete_duplicate_records : Exception "+str(exc))
            logging.error("data preprocessing : TransformationClass : delete_duplicate_records : " +traceback.format_exc())
            
            return 1
        logging.info("data preprocessing : TransformationClass : delete_duplicate_records : execution stop")
        return status
    
    def delete_duplicate_column(self,DBObject,connection,schema_id,project_id, table_name):
        '''
            Function will delete the duplicate column from the table.

            Operation id: ?
        '''
        
        logging.info("data preprocessing : TransformationClass : delete_duplicate_column : execution start")
        try:
            operation_id = 'dp_332'
            col_name = "blank"
            activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id,col_name)
          
            status,column_list = super().delete_duplicate_column(DBObject,connection,schema_id,table_name)
            #Update the activity status for the operation performed
            if status == 0:
                status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            else:
                status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
            
            
            return status
        except Exception as exc:
            logging.error("data preprocessing : TransformationClass : delete_duplicate_column : Exception : "+str(exc))
            logging.error("data preprocessing : TransformationClass : delete_duplicate_column : " +traceback.format_exc())
            
            return 1

    def delete_low_variance_column(self,DBObject,connection,project_id,schema_id,column_list,old_column_list, table_name, **kwargs):
        '''
            Delete the column which has low variance. 
            Operation id: dp_333
        '''
        
        logging.info("data preprocessing : TransformationClass : delete_low_variance_column : execution start")
        try:
            operation_id = 'dp_333'
            #Initialize the empty list
            variance_column = []
            variance = 0.5
            status = 1
            col_name = "blank"
            activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id,col_name)
          
            for index,col_name in enumerate(old_column_list):
                
                value = commonObj.check_datatype(DBObject,connection,col_name,table_name,datatype_check = 'text')
                if value == False:
                    #Query to get Boolean value  "True" if column variance is less ten te given variance else return "False"
                    sql_command = f'''select  case when VARIANCE("{col_name}") < {str(variance)} then
                    'True' when VARIANCE("{col_name}") is null then
                    'True' else 'False' end as variance_status from {table_name}  '''
                    
                    #Execute the sql query
                    dataframe = DBObject.select_records(connection,sql_command)
                    if str(dataframe['variance_status'][0]) =='True':

                        #Append Name of column into a list variable called "variance_column"
                        variance_column.append(column_list[index])

                        #Delete the column from the table
                        status = super().delete_column(DBObject,connection,schema_id,table_name,col_name)
                        #Update the activity status for the operation performed
                else:
                    status = 0
            if status == 0:
                status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
            else:
                status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
            
        except Exception as exc:
                logging.error("data preprocessing : TransformationClass : delete_low_variance_column : Exception : "+str(exc))
                logging.error("data preprocessing : TransformationClass : delete_low_variance_column : " +traceback.format_exc())
                return 1

        logging.info("data preprocessing : TransformationClass : delete_low_variance_column : execution stop")
        return status
    
    #* Encoding 

    def label_encoding(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
            This function will update column with numeric sequence.
            Operation id: dp_261
        '''
        #Activity id for starting of label_encoding operation i.e (data preprocessing : 261)
        operation_id = 'dp_261'

        logging.info("data preprocessing : TransformationClass : label_encoding : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            try:
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().label_encoding(DBObject, connection, [index,old_cols[i]], table_name)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
                
            except Exception as exc:
                logging.info("data preprocessing : TransformationClass : label_encoding : Exception : "+str(exc))
                logging.info("data preprocessing : TransformationClass : label_encoding : " +traceback.format_exc())
                return 1

        logging.info("data preprocessing : TransformationClass : label_encoding : execution stop")
        return status

    def one_hot_encoding(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, schema_id, **kwargs):
        '''
            This function will do one hot encoding on original column and add distinct value column to table.
            Operation id: dp_271
        '''
        
        logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution start")
        index = column_list[0]

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        #Activity id for starting of label_encoding operation i.e (data preprocessing : 271)
        operation_id = 'dp_271'

        for i,col_name in enumerate(cols):
            try:

                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().one_hot_encoding(DBObject, connection, [index,old_cols[i]], table_name, schema_id)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                
                
            except Exception as exc:
                logging.info("data preprocessing : TransformationClass : one_hot_encoding : Exception : "+str(exc))
                logging.info("data preprocessing : TransformationClass : one_hot_encoding : " +traceback.format_exc())
                return 1

        logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution stop")
        return status

    # def one_hot_encoding(self, dataframe, col):
    #     '''
    #         Operation id: 28
    #     '''
        
    #     logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution start")
        
    #     cols = [dataframe.columns[i] for i in col]
        
    #     for column in cols:
    #         try:
    #             temp_df =super().one_hot_encoding(dataframe[column])
    #             dataframe.drop([column], axis=1, inplace = True)
    #             dataframe = dataframe.join(temp_df)
    #         except:
    #             continue

    #     logging.info("data preprocessing : TransformationClass : one_hot_encoding : execution stop")
    #     return dataframe
    
    #* MATH OPERATIONS
    
    def add_to_column(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: 29
        '''
        logging.info("data preprocessing : TransformationClass : add_to_column : execution start")
        
        #Operation Id to get activity details
        operation_id = 'dp_281'

        operation = '+'
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.perform_math_operation(DBObject, connection, table_name, old_cols[i], operation, value)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)


        logging.info("data preprocessing : TransformationClass : add_to_column : execution stop")
        return status
    
    def subtract_from_column(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: 30
        '''
        logging.info("data preprocessing : TransformationClass : subtract_from_column : execution start")
        #Operation Id to get activity details
        operation_id = 'dp_291'

        operation = '-'
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):

                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.perform_math_operation(DBObject, connection, table_name, old_cols[i], operation, value)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)
        
        logging.info("data preprocessing : TransformationClass : subtract_from_column : execution stop")
        return status
    
    def multiply_column(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: 31
        '''
        logging.info("data preprocessing : TransformationClass : multiply_column : execution start")
        
        operation = '*'
        #Operation Id to get activity details
        operation_id = 'dp_311'

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.perform_math_operation(DBObject, connection, table_name, old_cols[i], operation, value)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)
        logging.info("data preprocessing : TransformationClass : multiply_column : execution stop")
        return status
    
    def divide_column(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, value, **kwargs):
        '''
            Operation id: 32
        '''
        logging.info("data preprocessing : TransformationClass : divide_column : execution start")
        
        operation = '/'
        #Operation Id to get activity details
        operation_id = 'dp_301'

        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.perform_math_operation(DBObject, connection, table_name, old_cols[i], operation, value)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)

        logging.info("data preprocessing : TransformationClass : divide_column : execution stop")
        return status
    
    def split_date_column(self, DBObject, connection, project_id, column_list,old_column_list, table_name, col, schema_id, **kwargs):
        '''
        
        
        Operation id: 321
        '''
        logging.info("data preprocessing : TransformationClass : split_date_column : execution start")
    
        operation_id = 'dp_321'
        
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = self.datetime_fe(DBObject, connection, schema_id, old_cols[i], table_name)
                
                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)

    
        logging.info("data preprocessing : TransformationClass : split_date_column : execution stop")
        return status
    
   
    def logarithmic_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
        [This function is used to make extremely skewed distributions less skewed, especially for right-skewed distributions]
        
        operation_id = 'dp_251'
        
        '''
        #Operation Id to get activity details
        operation_id = 'dp_251'

        logging.info("data preprocessing : TransformationClass : logarithmic_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().logarithmic_transformation(DBObject, connection, [index,old_cols[i]], table_name)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)

        logging.info("data preprocessing : TransformationClass : logarithmic_transformation : execution stop")
        
        return status
    
    
    def squareroot_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
        [This function used for reducing right-skewed distributions]
        
        operation_id = 'dp_252'
        '''
        #Operation Id to get activity details
        operation_id = 'dp_252'

        logging.info("data preprocessing : TransformationClass : squareroot_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().squareroot_transformation(DBObject, connection, [index,old_cols[i]], table_name)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)

        logging.info("data preprocessing : TransformationClass : squareroot_transformation : execution stop")
        
        return status
    
    def reciprocal_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
        [The reciprocal reverses the order among values of the same sign, so large values become smaller]
        
        operation_id = 'dp_253'
        '''
        #Operation Id to get activity details
        operation_id = 'dp_253'

        logging.info("data preprocessing : TransformationClass : reciprocal_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().reciprocal_transformation(DBObject, connection, [index,old_cols[i]], table_name)

                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)

        logging.info("data preprocessing : TransformationClass : reciprocal_transformation : execution stop")
        
        return status
    
    
    def exponential_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col,value, **kwargs):
        '''
        [This function used for to reduce left skewness.]
        
        operation_id = 'dp_254'
        '''
        #Operation Id to get activity details
        operation_id = 'dp_254'

        logging.info("data preprocessing : TransformationClass : exponential_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):

                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().exponential_transformation(DBObject, connection, [index,old_cols[i]], table_name,value)

                
                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)
            

        logging.info("data preprocessing : TransformationClass : exponential_transformation : execution stop")
        
        return status
    
    def boxcox_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
        [A box-cox transformation is a commonly used method for transforming a non-normally distributed dataset into a more normally distributed one.
        The basic idea behind this method is to find some value for λ such that the transformed data is as close to normally distributed as possible]
        
        operation_id = 'dp_255'
        '''
        #Operation Id to get activity details
        operation_id = 'dp_255'

        logging.info("data preprocessing : TransformationClass : boxcox_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().boxcox_transformation(DBObject, connection, [index,old_cols[i]], table_name)

                
                #Update the activity status for the operation performed
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)
                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)   

        logging.info("data preprocessing : TransformationClass : boxcox_transformation : execution stop")
        
        return status
    
    def yeojohnson_transformation(self, DBObject,connection,project_id,column_list,old_column_list, table_name, col, **kwargs):
        '''
        [The Yeo-Johnson transformation is an extension of the Box-Cox transformation and can be used on variables with zero and negative values]
        
        operation_id = 'dp_256'
        
        '''
        #Operation Id to get activity details
        operation_id = 'dp_256'

        logging.info("data preprocessing : TransformationClass : yeojohnson_transformation : execution start" + str(col))

        index = column_list[0]
        cols = [column_list[i] for i in col]
        old_cols = [old_column_list[i] for i in col]
        for i,col_name in enumerate(cols):
            
                #Insert the activity for the operation
                activity_id = commonObj.operation_start(DBObject, connection, operation_id, project_id, col_name)

                status = super().yeojohnson_transformation(DBObject, connection, [index,old_cols[i]], table_name)

                #Update the activity status for the operation performed
    
                
                if status == 0:
                    status = commonObj.operation_end(DBObject, connection, activity_id, operation_id, col_name)

                else:
                    status = commonObj.operation_failed(DBObject, connection, activity_id, operation_id, col_name)
                    raise TransformationFailed(500)
            

        logging.info("data preprocessing : TransformationClass : yeojohnson_transformation : execution stop")
        
        return status
    