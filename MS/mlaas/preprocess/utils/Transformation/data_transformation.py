'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Riddhi Pandya         20-April-2021           1.0           Created Class
 
*/
'''


#* Library Imports
import logging
import traceback
from scipy.stats import boxcox 

#* Commong Utilities
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('data_transformation')



class DataTransformationClass:
    
    def logarithmic_transformation(self,DBObject,connection,column_string,table_name):
        """
        [This function is used to make extremely skewed distributions less skewed, especially for right-skewed distributions]
        
        formula: f(x)=ln(x)
        
        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            
        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : logarithmic_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name) # change datatype to float
        
            sql_command =f'update {table_name} set "{column_string[1]}"=ln("{column_string[1]}")'
        
            logging.info("data preprocessing : DataTransformationClass : logarithmic_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : logarithmic_transformation : execution end")  
        
            return status
        
        except Exception as e:
            
            logging.error("data preprocessing : DataTransformationClass : logarithmic_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : logarithmic_transformation : " +traceback.format_exc())
            
            return 1
    
    
    def squareroot_transformation(self,DBObject,connection,column_string,table_name):
        
        """
        [This function used for reducing right-skewed distributions]
            
            formula: f(x)=√x

        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            
        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : squareroot_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name) #change datatype to float
        
            sql_command =f'update {table_name} set "{column_string[1]}"=sqrt("{column_string[1]}")' #Update table
        
            logging.info("data preprocessing : DataTransformationClass : squareroot_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : squareroot_transformation : execution end")
        
            return status
        except Exception as e:
            logging.error("data preprocessing : DataTransformationClass : squareroot_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : squareroot_transformation : " +traceback.format_exc())
            return 1
    
    def reciprocal_transformation(self,DBObject,connection,column_string,table_name):
        
        """
        [The reciprocal reverses the order among values of the same sign, so large values become smaller]

            formula:   f(X) = 1/X
        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            
        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : reciprocal_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name) #change datatype to float
        
            sql_command =f'update {table_name} set "{column_string[1]}"=1/("{column_string[1]}")'  #Update table
        
            logging.info("data preprocessing : DataTransformationClass : reciprocal_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : reciprocal_transformation : execution end")
        
            return status
        
        except Exception as e:
            logging.error("data preprocessing : DataTransformationClass : reciprocal_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : reciprocal_transformation : " +traceback.format_exc())
            return 1
        
    
    def exponential_transformation(self,DBObject,connection,column_string,table_name,value):
        """
        [This function used for to reduce left skewness.]

            formula: K(X) = exp(X)
            
        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]
            value([integer]): [user input]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            

        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : exponential_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name)
        
            sql_command =f'update {table_name} set "{column_string[1]}"=power("{column_string[1]}",{value})'
        
            logging.info("data preprocessing : DataTransformationClass : exponential_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : exponential_transformation : execution end")
        
            return status
        except Exception as e:
            logging.error("data preprocessing : DataTransformationClass : exponential_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : exponential_transformation : " +traceback.format_exc())
            return 1
        
    
    def boxcox_transformation(self,DBObject,connection,column_string,table_name):
        """
        [A box-cox transformation is a commonly used method for transforming a non-normally distributed dataset into a more normally distributed one.
        The basic idea behind this method is to find some value for λ such that the transformed data is as close to normally distributed as possible]
            
            formula:
            y(λ) = (yλ – 1) / λ  if y ≠ 0
            y(λ) = log(y)  if y = 0]

        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            

        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : boxcox_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name) #change datatype to float
        
            column_df=DBObject.get_column_df(connection,table_name,column_string[1]) #get df of specific column
        
            column_df=column_df[column_string[1]] #select specific column
        
            transformed_data, best_lambda = boxcox(column_df) #find best_lamda
        
            if best_lambda == 0:
            
                sql_command =f'update {table_name} set "{column_string[1]}"=ln("{column_string[1]}")'
            else:
            
                sql_command =f'update {table_name} set "{column_string[1]}"=(power("{column_string[1]}",{best_lambda})-1)/{best_lambda}'
        
            logging.info("data preprocessing : DataTransformationClass : boxcox_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : boxcox_transformation : execution end")
        
            return status
        except Exception as e:
            logging.error("data preprocessing : DataTransformationClass : boxcox_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : boxcox_transformation : " +traceback.format_exc())
            return 1
    
    def yeojohnson_transformation(self,DBObject,connection,column_string,table_name):
        """
        [The Yeo-Johnson transformation is an extension of the Box-Cox transformation and can be used on variables with zero and negative values]
            formula:
            
            ((x + 1)** λ - 1) /  λ ; if λ is not 0 and X >= zero
            ln(X + 1 ); if λ is zero and X >= zero; 
            -((-x + 1)**(2 - λ) - 1) / (2 - λ), if λ is not 2 and X is negative
            -ln(-X + 1); if λ is 2 and X is negative
        
        Args:
            DBObject ([object]):  [DB Class Object.]
            connection ([object]):  [Postgres Connection object]
            column_string ([list]): [list of column]
            table_name ([string]): [Name of the table]

        Returns:
            [status]: [return 0 if successfully performed the operation else return 1]
            
        """
        try:
            
            logging.info("data preprocessing : DataTransformationClass : yeojohnson_transformation : execution start")
        
            status=DBObject.change_datatype(connection,column_string[1],table_name) #change datatype to float
        
            column_df=DBObject.get_column_df(connection,table_name,column_string[1]) #get df of specific column
        
            column_df=column_df[column_string[1]] #select specific column
        
            transformed_data, best_lambda = boxcox(column_df) #find best_lamda
        
            sql_command =f'update {table_name} set "{column_string[1]}"=case when "{column_string[1]}">=0 and {best_lambda} != 0 then (power(("{column_string[1]}"+1),{best_lambda})-1)/{best_lambda} when "{column_string[1]}">=0 and {best_lambda} = 0  then ln("{column_string[1]}")+1 when "{column_string[1]}"<0 and {best_lambda} != 2 then  -(power((-("{column_string[1]}")+1),2-{best_lambda})-1)/(2-{best_lambda}) when "{column_string[1]}"<0 and {best_lambda} = 2 then -(ln(-"{column_string[1]}"+1)) end'
        
            logging.info("data preprocessing : DataTransformationClass : yeojohnson_transformation : sql command"+str(sql_command))
        
            status = DBObject.update_records(connection,sql_command)
        
            logging.info("data preprocessing : DataTransformationClass : yeojohnson_transformation : execution end")
        
            return status
        except Exception as e:
            logging.error("data preprocessing : DataTransformationClass : yeojohnson_transformation : " +str(e))
            logging.error("data preprocessing : DataTransformationClass : yeojohnson_transformation : " +traceback.format_exc())
            return 1
        

        
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        