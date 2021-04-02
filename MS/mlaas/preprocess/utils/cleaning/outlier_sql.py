'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

import logging
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('outlier')

class OutliersTreatmentClass:
    
    #* Below functions are used for detecting the outliers
    
    def extreme_value_analysis(self,DBObject,connection,col_name,table_name,impute_value = None,discard_missing = False):
        '''
            Returns Probable & Extreme outliers. Best suitable for Non-Normal Distributions.
            
            Args:
                series[(pandas.Series)]: Column for which you want the outlier ranges.
                outlier[(boolean)]: if false than only returns ranges.
                
            Returns:
                List[(Intiger|Float)]: Output list contains following 2 lists & 4 Intigers,
                    1. List of Probable Outliers,
                    2. List of Most-Probable Outliers
                    3. Upper Limit for probable outliers
                    4. Upper Limit for Most-Probable outliers
                    5. Lower Limit for probable outliers
                    6. Lower Limit for Most-Probable outliers
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : extreme_value_analysis : execution start")
            # #? Finding Quartiles
            sql_command = 'select PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "'+str(col_name)+'") AS quartile_25,PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "'+str(col_name)+'") AS quartile_75 from '+str(table_name)
            dataframe = DBObject.select_records(connection,sql_command)
            
            q1,q3 = float(dataframe['quartile_25'][0]),float(dataframe['quartile_75'][0])

            # #? Finding Boundaries of the normal data
            iqr = q3-q1
            upper_limit = q3 + (iqr * 1.5)
            # upper_limit_extreme = q3 + (iqr * 3)
            lower_limit = q1 - (iqr * 1.5)
            # lower_limit_extreme = q1 - (iqr * 3)

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
        except:
            return 1
    
    def z_score_analysis(self,DBObject,connection,table_name,col_name,impute_value = None,discard_missing = False):
        '''
            Returns list of the Outliers. Best suitable for Normal Distributions.
            
            Args:
                Series[(pandas.Series)]: Column for which you want the outlier ranges,
                level[(intiger|float)] (default=3)= level of the standard deviation. (Typically between 1.5 to 4).
                outlier[(boolean)]: if false than only returns z-scores.
                
            Returns:
                List[(intiger|float)] = List of the outliers for given standard deviation range & Z-scores for all values
        '''
        
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : z_score_analysis : execution start")

            #Find Average and standard deviation of the column
            sql_command = f'select avg("{str(col_name)}"),STDDEV("{str(col_name)}") from {table_name}'
            logging.info("Sql_command : z_score_analysis : "+str(sql_command))

            dataframe = DBObject.select_records(connection,sql_command)

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
            logging.error(str(exc))
            return str(exc)
        
    #* Below functions are used for dealing with outliers
    
    def delete_above(self,DBObject,connection,table_name,col_name,val):
        '''
            Deletes rows where value of given column is greater than given value.
            
            Args:
                data_df[(pandas.Dataframe)]: Dataframe,
                col[(String)]: Name of the column
                val[(intiger|float)]: deciding value
                ge[(boolean)]: Delete values "Greater than or Eq: True" or only "Greater than: False"

            Returns:
                pandas.Dataframe: Filtered Dataframe
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : delete_above : execution stop")

            #Delete records where column value less then the given value
            sql_command = 'delete from '+str(table_name)+' where "'+str(col_name)+'" >'+str(val)
            logging.info("Sql_command : Delete query : delete_above : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : delete_above : execution stop")
            return status
        except:
            return 1
        
    def delete_below(self,DBObject,connection,table_name,col_name,val,le = False):
        '''
            Deletes rows where value of given column is lesser than given value.
            
            Args:
                data_df[(pandas.Dataframe)]: Dataframe,
                col[(String)]: Name of the column
                val[(intiger|float)]: deciding value
                ge[(boolean)]: Delete values "Less than or Eq: True" or only "Less than: False"

            Returns:
                pandas.Dataframe: Filtered Dataframe
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : delete_below : execution start")

            #Delete records where column value greater then the given value
            sql_command = f'delete from {str(table_name)} where "{str(col_name)}" < {str(val)}'
            logging.info("Sql_command : Delete query : delete_below : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            logging.info("data preprocessing : OutliersTreatmentClass : delete_below : execution stop")
            return status
        except:
            return 1
    
    def replace_outliers(self,DBObject,connection,table_name,col_name,impute_value, detect_method, log = False):
        '''
            Returns a series where the outliers are replaced with the given function(Mean of Median)
            
            Args:
            -----
            series[(pandas.Series)]: column,
            operation[(intiger)] (default = 0): which operation should be performed,
                - 0 : mean
                - 1 : median
                - 2 : mode \n
            detect_method[(intiger)] (default = 0): which method should be used to detect outliers,
                - 0 : Extreme Value Analysis
                - 1 : Z-score method \n
            less_probable[(boolean)] (default = False): should less probable outliers be raplaced?
            level[(intiger)] (default = 3): level of std in Z-score method.
            log[(boolean)] (default = False): Apply log transforamation before outlier detection?
                
            Returns:
            --------
            List[(intiger|float)]: Updated Column
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
            
            #? Invalid Input
            else:
                return 3
            logging.info("data preprocessing : OutliersTreatmentClass : replace_outliers : execution stop")
            return status
        except Exception as exc:
            return str(exc)
        
    def remove_outliers(self,DBObject,connection,table_name,col_name, detect_method = 0, log = False):
        '''
            Returns a series where the outliers are replaced with the given function(Mean of Median)
            
            Args:
                data_df[(pandas.Dataframe)]: whole dataframe,
                col[(string)]: name of the column
                detect_method[(intiger)] (default = 0): which method should be used to detect outliers,
                                                            0 => Extreme Value Analysis
                                                            1 => Z-score method
                less_probable[(boolean)] (default = False): should less probable outliers be removed?
                level[(intiger)] (default = 3): level of std in Z-score method.
                log[(boolean)] (default = False): Apply log transforamation before outlier detection?
                
            Returns:
                pandas.Dataframe: Updated Dataframe
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
                
            #? Invalid Input
            else:
                status = 3

            logging.info("data preprocessing : OutliersTreatmentClass : remove_outliers : execution stop")
            return status
        except:
            return 1
        
    def apply_log_transformation(self,DBObject,connection,table_name,col_name):
        '''
            Apply log transformation on the given column.
            
            Args:
                series[(pandas.Series)]: column data.
                
            Returns:
                pandas.Series: transformed series.
        '''
        try:
            logging.info("data preprocessing : OutliersTreatmentClass : apply_log_transformation : execution start")
            
            sql_command = f'Update {table_name} set "{col_name}"= log("{col_name}")' # Get update query
            logging.info("Sql_command : Update query : apply_log_transformation : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            logging.info("data preprocessing : OutliersTreatmentClass : apply_log_transformation : execution stop")
            return status
        except:
            return 1