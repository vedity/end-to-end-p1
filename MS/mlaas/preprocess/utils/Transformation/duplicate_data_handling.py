import pandas as pd
import logging
from common.utils.logger_handler import custom_logger as cl
from ..schema import schema_creation as sc

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('duplicate_data_handling')
schemaObj = sc.SchemaClass()
class RemoveDuplicateRecordClass:
    
    def getDuplicateColumns(self,df):
        """
        Function will get the duplicate column name from the dataframe

        Args:
                df[dataframe] : [dataframe]
        Return :
                [List] : [ return list of duplicate column name else empty list if not found ]
        """
        try:
            logging.info("Preprocess : RemoveDuplicateRecordClass : getDuplicateColumns : execution start")
            # Create an empty set
            duplicateColumnNames = []
            
            # Iterate through all the columns 
            # of dataframe
            for x in range(df.shape[1]):
                
                # Take column at xth index.
                col = df.iloc[:, x]
                
                # Iterate through all the columns in
                # DataFrame from (x + 1)th index to
                # last index
                for y in range(x + 1, df.shape[1]):
                    
                    # Take column at yth index.
                    other_col = df.iloc[:, y]
                    
                    # Check if two columns at x & y
                    # index are equal or not,
                    # if equal then adding to list
                    if col.equals(other_col):
                        duplicateColumnNames.append(df.columns.values[y])
            logging.info("Preprocess : RemoveDuplicateRecordClass : getDuplicateColumns : execution ends")
            return duplicateColumnNames
        except Exception as exc:
            logging.info("Preprocess : RemoveDuplicateRecordClass : getDuplicateColumns : Exception : "+str(exc))
            return None

    def delete_duplicate_records(self,DBObject,connection,schema_id,table_name,column_string):
        """
        Function will remove the duplicate rows from the given table name
        Args  :
                table_name[(String)] : [Name of the table]
                column_string[(String)] : [the query string of column name use to identify duplicate rows ]
        Return :
                [Integer ] : [Return the status 0 if success else 1 ]
        
        """
        logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_records : execution start")
        try:
            sql_command = f'delete from {table_name} where index not in (select min(index) from {table_name} group by {column_string})'

            logging.info("Sql_command : delete_duplicate_records : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)
            
        except Exception as exc:
            logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_records : Exception : "+str(exc))
            status = 1
        
        logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_records : execution stop")
        return status

    def delete_duplicate_column(self,DBObject,connection,schema_id,table_name):
        """
        Function will detect the duplicate columns in the dataframe and delete those columns from the table
        Args  :
                table_name[(String)] : [Name of the table]
        Return :
                [Integer | list] : [Return the status 0 if success else 1 ,list of the duplicate column names]
        """

        try:
            logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_column : execution start  ")

            #Get all table data
            sql_command = f'select * from {table_name}'

            #Execute sql query and get dataframe
            dataframe = DBObject.select_records(connection,sql_command)

            
            #Get the duplicate column name from the dataframe if present
            #?if not return empty list
            col_list = self.getDuplicateColumns(dataframe)

            #?check the list is empty or not
            if len(col_list) != 0:
                for index in range(len(col_list)):

                    #?Iterate all the names from the col_list and delete that column 
                    status = self.delete_column(DBObject,connection,schema_id,table_name,col_list[index])
            else:
                if col_list is None:
                    status = 1
                else:
                    status = 0

            logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_column : execution ends  ")
            return status,col_list

        except Exception as exc:
            logging.info("Preprocess : RemoveDuplicateRecordClass : delete_duplicate_column : Exception : "+str(exc))
            return 1,None
        
    
    def delete_column(self,DBObject,connection,schema_id,table_name,column_name):
        """
        function will delete the the column from the table
        Args:
            table_name[(String)]  :  [Name of the table]
            column_name[(String)] :  [Name the column]
        Return:
            [Integer|String] : [return 0 if successfully performed the operation else return 1,
                                return String if any exception occurred ]
        """
        logging.info("Preprocess : RemoveDuplicateRecordClass : delete_column : execution start")
        try:
            sql_command = f'ALTER TABLE {table_name} DROP "{column_name}" '

            logging.info("Sql_command : delete_column  : "+str(sql_command))

            status = DBObject.update_records(connection,sql_command)

            if status == 0:
                
                status = schemaObj.delete_schema_record(DBObject,connection,schema_id,col_name = column_name)
        except Exception as exc:
            logging.info("Preprocess : RemoveDuplicateRecordClass : delete_column : Exception : "+str(exc))
            status = 1
        
        logging.info("Preprocess : RemoveDuplicateRecordClass : delete_column : execution stop")
        return status

