'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Abhishek Negi         17-Jan-2021           1.0           Created Class
 
*/
'''
#* Library Imports
import logging
import numpy as np
import traceback

#* Relative Imports
from sklearn.neighbors import LocalOutlierFactor
from common.utils.logger_handler import custom_logger as cl
from .. import common
#Object Initialize
commonObj = common.CommonClass()

#* Defining Logger
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('outlier')


class OutliersTreatmentClass:
    
    
    def extreme_value_analysis(self,DBObject,connection,col_name,table_name,impute_value = None,discard_missing = False):
        '''
            Find the extream outlier and update/delete the outliers Best suitable for Non-Normal Distributions.
            
            Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]   : [Name of the column]
                table_name[(String)] : [Name of the table]
                impute_value[(Integer|Decimal)] : [It will have Mean or Median value of the column ]
                discard_missing([Integer]) :
                                        False : User want's to replace the outlier 
                                        True : User want's to Remove outliers
                
            Returns:
                [(intiger)]: [Return 0 if successfully function executed else return 1] 
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : extreme_value_analysis : execution start")
            
            
            # #? Finding lower limit and upper limit  based on the Quartiles
            lower_limit,upper_limit =self.get_upper_lower_limit(DBObject,connection,col_name,table_name,method_type = 'extreme_value_analysis')
            if lower_limit == upper_limit == None:
                return 1

            if discard_missing == True:

                # Delete the records from the table based on the upper limit and lower limit 
                sql_command = f'delete from {table_name} where "{col_name}" < {str(lower_limit)} or "{col_name}" > {str(upper_limit)}'
                logging.info("Sql_command : Delete record using  : extreme_value_analysis : "+str(sql_command))

            else:
                # Replace the with mean/median/mode of the column
                sql_command = f'Update {table_name} set "{col_name}"={impute_value} where "{col_name}" < {str(lower_limit)} or "{col_name}" > {str(upper_limit)}' # Get update query
                logging.info("Sql_command : update record using  : extreme_value_analysis : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            logging.info("data preprocessing : OutliersTreatmentClass : extreme_value_analysis : execution end")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : extreme_value_analysis : Exception : "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : extreme_value_analysis : " +traceback.format_exc())
            return 1
    
    def z_score_analysis(self,DBObject,connection,table_name,col_name,impute_value = None,discard_missing = False):
        '''
            Find the extream outlier and update/delete the outliers using the Z Score Analysis method.
            
            Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]   : [Name of the column]
                table_name[(String)] : [Name of the table]
                impute_value[(Integer|Decimal)] : [It will have Mean or Median value of the column ]
                discard_missing([Integer]) :
                                        False : User want's to replace the outlier 
                                        True : User want's to Remove outliers
                
                
            Returns:
                [(intiger)]: [Return 0 if successfully function executed else return 1] 
        '''
        
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : z_score_analysis : execution start")

            dataframe = self.get_column_statistics(DBObject,connection,col_name,table_name)
            if len(dataframe)==0 or dataframe is None:
                return 1
            else:
                avg_value,stddev_value =  round(dataframe['avg'][0],4),round(dataframe['stddev'][0],4)
            logging.info("Averag value : "+str(avg_value)+" : standard deviation : "+str(stddev_value))

            if discard_missing == True:

                #Delete the records if the compute value of the column based on formula is not between -3 and 3
                sql_command = f'delete from {table_name} where ("{col_name}"-'+str(avg_value)+')/'+str(stddev_value)+ ' not between -3 and 3'
                logging.info("Sql_command : Delete query: z_score_analysis : "+str(sql_command))
            else:
                sql_command = f'Update {table_name} set "{col_name}"={impute_value} where ("{col_name}"-'+str(avg_value)+')/'+str(stddev_value)+ ' not between -3 and 3' # Get update query
                logging.info("Sql_command : update query : z_score_analysis : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : z_score_analysis : execution stop")

            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : z_score_analysis :Exception :"+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : z_score_analysis : " +traceback.format_exc())
            return 1
        
    
    def delete_above(self,DBObject,connection,table_name,col_name,val):
        '''
            Deletes rows where value of given column is greater than given value.
            
            Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]      : [Name of the column]
                table_name[(string)]    : [Name of the dataset table]
                val[(intiger|float)]    : [deciding value]
                
            Returns:
                [(intiger)]: [Return 0 if successfully function executed else return 1] 
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : delete_above : execution stop")

            #Delete records where column value less then the given value
            sql_command = 'delete from '+str(table_name)+' where "'+str(col_name)+'" >'+str(val)
            logging.info("Sql_command : Delete query : delete_above : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : delete_above : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : delete_above :Exception "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : delete_above : " +traceback.format_exc())
            return 1
        
    def delete_below(self,DBObject,connection,table_name,col_name,val):
        '''
            Deletes rows where value of given column is lesser than given value.
            
            Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]      : [Name of the column]
                table_name[(string)]    : [Name of the dataset table]
                val[(intiger|float)]    : [deciding value]
                
            Returns:
                [(intiger)]: [Return 0 if successfully function executed else return 1] 
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : delete_below : execution start")

            #Delete records where column value greater then the given value
            sql_command = f'delete from {str(table_name)} where "{str(col_name)}" < {str(val)}'
            logging.info("Sql_command : Delete query : delete_below : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            logging.info("data preprocessing : OutliersTreatmentClass : delete_below : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : delete_below : Exception "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : delete_below : " +traceback.format_exc())
            return 1
    
    def replace_outliers(self,DBObject,connection,table_name,col_name,impute_value, detect_method,method_type = None, log = False):
        '''
            
            Function will replace the the outlier with impute value(Mean/median) and the method select by user.
            
            Args:
            -----
            DBObject [(Object)]     : [DB Class Object.]
            connection [(Object)]   : [Postgres Connection object]
            col_name[(String)]      : [Name of the column]
            table_name[(string)]    : [Name of the table]
            impute value [(intiger)] (default = 0): which operation should be performed [ mean| median | mode ]
            detect_method[(intiger)] : which method should be used to detect outliers,
                - 0 : Extreme Value Analysis
                - 1 : Z-score method 
                - 2 : Censoring
                - 3 : Local factor outlier Method
            Method_type[(Integer)] : which operation to be performed.
                0 : Replace with the outlier with impute value
                1 : Delete the outlier  
                
            Returns:
            --------
            [(intiger)]: [Return 0 if successfully function executed else return 1] 
        '''
        
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : replace_outliers : execution start")
            if log:
                status = self.apply_log_transformation(DBObject,connection,table_name,col_name)
            
            #? Extreme Value Analysis
            if detect_method == 0:

                status = self.extreme_value_analysis(DBObject,connection,col_name,table_name,impute_value)
            
            #? Z-Score Method
            elif detect_method == 1:
                
                status = self.z_score_analysis(DBObject,connection,table_name,col_name,impute_value)
            
            #Censoring 
            elif detect_method == 2:

                lower_limit,upper_limit = self.get_upper_lower_limit(DBObject,connection,col_name,table_name,method_type )

                status = self.update_outliers(DBObject,connection,lower_limit,upper_limit,col_name,table_name)
            
            #Local factor outlier Method
            elif detect_method == 3:
                
                status = self.local_factor_outlier(DBObject,connection,col_name,table_name,impute_value,method_type)
            
            #? Invalid Input
            else:
                return 1
            logging.info("data preprocessing : OutliersTreatmentClass : replace_outliers : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : replace_outliers : Exception "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : replace_outliers : " +traceback.format_exc())
            return 1
        
    def remove_outliers(self,DBObject,connection,table_name,col_name, detect_method = 0, log = False):
        '''
            Function will replace the the outlier with impute value(Mean/median) and the method select by user.
            
            Args:
            -----
            DBObject [(Object)]     : [DB Class Object.]
            connection [(Object)]   : [Postgres Connection object]
            col_name[(String)]      : [Name of the column]
            table_name[(string)]    : [Name of the table]
            impute value [(intiger)] (default = 0): which operation should be performed [ mean| median | mode ]
            detect_method[(intiger)] : which method should be used to detect outliers,
                - 0 : Extreme Value Analysis
                - 1 : Z-score method 
                - 2 : Local factor outlier Method  
                
            Returns:
            --------
            [(intiger)]: [Return 0 if successfully function executed else return 1]
        '''
        
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : remove_outliers : execution start")
            if log:
                status = self.apply_log_transformation(DBObject,connection,table_name,col_name,)
                
            #? Extreme Value Analysis
            if detect_method == 0:
                status= self.extreme_value_analysis(DBObject,connection,col_name,table_name,discard_missing = True)
                
            #? Z-Score Method
            elif detect_method == 1:
                    
                status = self.z_score_analysis(DBObject,connection,table_name,col_name,discard_missing = True)
            
            #Local factor outlier Method
            elif detect_method == 2:
                
                status = self.local_factor_outlier(DBObject,connection,col_name,table_name,method_type =1)
                
            #? Invalid Input
            else:
                status = 1

            logging.info("data preprocessing : OutliersTreatmentClass : remove_outliers : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : remove_outliers : Exception "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : remove_outliers : " +traceback.format_exc())
            return 1
        
    def apply_log_transformation(self,DBObject,connection,table_name,col_name):
        '''
            Apply log transformation on the given column.
            
            Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]      : [Name of the column]
                table_name[(string)]    : [Name of the table]
                
            Returns:
                [(intiger)]: [Return 0 if successfully function executed else return 1]
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : apply_log_transformation : execution start")
            
            sql_command = f'Update {table_name} set "{col_name}"= log("{col_name}")' # Get update query
            logging.info("Sql_command : Update query : apply_log_transformation : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : apply_log_transformation : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : apply_log_transformation : Exception "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : apply_log_transformation : " +traceback.format_exc())
            return 1

    def get_upper_lower_limit(self,DBObject,connection,col_name,table_name,method_type ,quantile_1=0.25,quantile_2=0.75):
        """
        Function will find out the minimum and maximum limit based on the method type selected by user.
        Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]     : [Name of the column]
                table_name[(String)]   : [Name of the table]
                method_type[(String)]  : [Method name selected by user]
                                        1)extreme_value_analysis
                                        2)iqr_proximity
                                        3)Gaussian_approx
                                        4)quantiles
                quantile_1[(Integer)]   : [By default will be 0.25 else depends on user input]
                quantile_1[(Integer)]   : [By default will be 0.75 else depends on user input]
            
        Return:

                upper_limit[integer] : [return maximum limit of the column ]
                lower_limit[integer] : [return minimum limit of the column ]
        """
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : get_upper_lower_limit : execution start")
            sql_command = f'select PERCENTILE_CONT({str(quantile_1)}) WITHIN GROUP (ORDER BY "{str(col_name)}") AS quartile_1,PERCENTILE_CONT({str(quantile_2)}) WITHIN GROUP (ORDER BY "{str(col_name)}") AS quartile_2 from {table_name}'
            logging.info("Sql_command : get_upper_lower_limit( PERCENTILE_COUNTS) : "+str(sql_command))

            
            dataframe = DBObject.select_records(connection,sql_command)
            q1,q3 = float(dataframe['quartile_1'][0]),float(dataframe['quartile_2'][0])

            # #? Finding Boundaries of the normal data
            iqr = q3-q1
            if method_type == 'extreme_value_analysis' or method_type == 'iqr_proximity' :
                
                lower_limit = q1 - (iqr * 1.5)
                upper_limit = q3 + (iqr * 1.5)

            elif method_type == 'Gaussian_approx':
                
                dataframe = self.get_column_statistics(DBObject,connection,col_name,table_name)
                avg_value,stddev_value =  round(dataframe['avg'][0],4),round(dataframe['stddev'][0],4)
                
                lower_limit = avg_value - 3 * stddev_value
                upper_limit = avg_value + 3 * stddev_value

            elif method_type == 'quantiles':
                lower_limit = q1
                upper_limit = q3

            logging.info(f"get_upper_lower_limit : method : {method_type} : lower_limit : {str(lower_limit)} : upper_limit : {str(upper_limit)}")
            logging.info("data preprocessing : OutliersTreatmentClass : get_upper_lower_limit : execution ends")
            return lower_limit,upper_limit

        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : get_upper_lower_limit : Exception : "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : get_upper_lower_limit : " +traceback.format_exc())
            return None,None
    
        

    def get_column_statistics(self,DBObject,connection,col_name,table_name):
        """
        Find Average and standard deviation of the column.

        Args:
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]   : [Name of the column]
                table_name[(String)] : [Name of the table]
        Return:
                [dataframe |integer] : [return dataframe if successfully retrived else return 1 any exception occurred]
        """
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : get_column_statistics : execution start")
            
            #query will get  average and standard deviation of the given column name
            sql_command = f'select avg("{str(col_name)}"),STDDEV("{str(col_name)}") from {table_name}'
            logging.info("Sql_command : get_column_statistics : "+str(sql_command))

            #Execute the sql query
            dataframe = DBObject.select_records(connection,sql_command)

            logging.info("data preprocessing : OutliersTreatmentClass : get_column_statistics : execution end")
            return dataframe
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : get_column_statistics : Exception : "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : get_column_statistics : " +traceback.format_exc())
            return None
    
    def local_factor_outlier(self,DBObject,connection,col_name,table_name,impute_value = None,method_type = None):
        """
        Function will find out the outlier and get the index value of that outlier  delete or Replace the with impute method
        is selected.

        Args : 
                DBObject [(Object)]     : [DB Class Object.]
                connection [(Object)]   : [Postgres Connection object]
                col_name[(String)]   : [Name of the column]
                table_name[(String)] : [Name of the table]
                impute_value[(Integer|Decimal)] : [It will have Mean or Median value of the column ]
                method_type[(Integer)] : 
                                        0 : User want's to replace the outlier with the impute value 
                                        1 : User want's to delete outliers
        Return:
                [Integer] : [Return 0 if successfully operation performed else 1 if failed]

        """
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : local_factor_outlier : execution start")
            
            #Get the column data from table
            sql_command = f'''select "{str(col_name)}" from {table_name} ''' # Get update query
            logging.info("Sql_command :  local_factor_outlier : Get column values: "+str(sql_command))

            #Get the dataframe from execute table
            dataframe = DBObject.select_records(connection,sql_command)

            # Convert into numpy array
            numpy_data  = dataframe.to_numpy()

            #initialize the object
            lof_obj = LocalOutlierFactor(n_neighbors=20,contamination=0.1)

            #Fit and predict outliers
            trained_data = lof_obj.fit_predict(numpy_data)


            #?outlier_data variable will have True or False boolean value
            #? where trained_data  variable having -1 value
            outlier_data = trained_data ==-1
            
            #?check with the corresponding row index of original dataframe
            #Get the index from dataframe where row is False (-1) means outlier 
            index_list = list(dataframe[outlier_data].index)

            logging.info('local_factor_outlier : index list : outliers : '+str(index_list))

            #Form a query string with comma seperated index value
            in_query =",".join(str(x) for x in index_list)

            if method_type == 0:
                sql_command = f''' UPDATE {table_name} SET "{str(col_name)}"=
                                CASE  WHEN (SELECT DATA_TYPE  FROM INFORMATION_SCHEMA.COLUMNS WHERE 
                                TABLE_NAME = '{str(table_name.split('.')[-1][1:-1])}' AND COLUMN_NAME = '{col_name}') IN ('bigint') THEN CAST({impute_value} as BIGINT) ELSE {str(impute_value)} END 
                                WHERE INDEX IN ({in_query}) '''
                logging.info("Sql_command :  local_factor_outlier : Replace outlier: "+str(sql_command))
            else:
                sql_command = f''' Delete from  {table_name} where index in ({in_query}) '''
                logging.info("Sql_command :  local_factor_outlier : Remove outlier: "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : local_factor_outlier : execution end")
            return status

        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : local_factor_outlier : Exception : "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : local_factor_outlier : " +traceback.format_exc())
            return 1
    
    def update_outliers(self,DBObject,connection,lower_limit,upper_limit,col_name,table_name):
        """
        Function will replace the outliers with the given upper and lower limit

        Args:
            DBObject [(Object)]     : [DB Class Object.]
            connection [(Object)]   : [Postgres Connection object]
            lower_limit[(Integer)]  : [minimum distribution limit]
            upper_limit[(Integer)]  : [maximum distribution limit]
            col_name[(String)]      : [Name of the column]
            table_name[(string)]    : [Name of the table]

        Return : 
                [Integer] : [return 0 if successfull else 1]
        """
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : update_outliers : execution start")
            
            value = commonObj.check_datatype(DBObject,connection,col_name,table_name)
            if value == True:
                lower_limit,upper_limit = int(lower_limit),int(upper_limit)
                
            sql_command = f'''Update {table_name} set "{col_name}"= case when  "{col_name}" < {str(lower_limit)} then {str(lower_limit)} when "{col_name}" > {str(upper_limit)} then {str(upper_limit)} else "{col_name}" end ''' # Get update query
            
            logging.info("Sql_command :  update_outliers with lower_limit : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            logging.info("data preprocessing : OutliersTreatmentClass : update_outliers : execution end")
            return status
        except Exception as exc:
            logging.error("data preprocessing : OutliersTreatmentClass : update_outliers : Exception : "+str(exc))
            logging.error("data preprocessing : OutliersTreatmentClass : update_outliers : " +traceback.format_exc())
            return 1
    
    
    

    
    
