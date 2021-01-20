'''
/*CHANGE HISTORY
--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 
*/
'''
import pandas as pd 
import logging
import json
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from dateutil.parser import parse
import pandas as pd
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')

class SchemaClass:
    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.]
            user ([string]): [user of the database.]
            password ([string]): [password of the database.]
            host ([string]): [host ip or name where database is running.]
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number
        
    def get_schema(self):
        # schema table name
        table_name = 'mlaas.schema_tbl'
        # Columns for schema table
        cols = 'project_id,column_name,changed_column_name,data_type,column_attribute' 
        # Schema of schema_table
        schema ="project_id bigint,"\
                "column_name  text,"\
                "changed_column_name  text,"\
                "data_type  text,"\
                "column_attribute  text"
                
        return table_name,cols,schema
    
    def get_dataset_schema(self,dataset_id):
        """
        this function used to get the column name and datatype of the table

        Args :
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
                [List] : [return the list of dictonery]
        """
        try:
            logging.info("data ingestion : SchemaClass :get_dataset_schema : execution start")
            DBObject = db.DBClass() # create object for database class
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
            if connection == None:
                raise DatabaseConnectionFailed(500)
            sql_command = "SELECT dataset_name,dataset_table_name,user_name,dataset_visibility,no_of_rows from mlaas.dataset_tbl Where dataset_id =" +dataset_id
            dataset_df = DBObject.select_records(connection,sql_command)  # execute the sql query and return data if found else return None
            if dataset_df is None or len(dataset_df) == 0:
                raise DatasetDataNotFound(500)
            dataset_records = dataset_df.to_records(index=False) # convert dataframe to a NumPy record  
            dataset_name,dataset_table_name,user_name,dataset_visibility,no_of_rows = dataset_records[0]
            dataset_name,dataset_table_name,user_name,dataset_visibility = str(dataset_name),str(dataset_table_name),str(user_name),str(dataset_visibility)

            if dataset_visibility =="private":
                table_name=user_name+"."+dataset_table_name
            else:
                table_name = dataset_table_name

            #sql query string
            sql_command = "SELECT * from "+table_name
            data_details_df = DBObject.select_records(connection,sql_command) #execute the sql query
            if data_details_df is None:
                raise DataNotFound(500)
            column_name = data_details_df.columns.values.tolist() # covert the dataframe into list
            predicted_datatype = self.get_attribute_datatype(connection,DBObject,table_name,column_name ,no_of_rows)
            schema_data = get_schema_format(column_name,predicted_datatype) #call get_schema_format to get json format data
            logging.info("data ingestion : SchemaClass :get_dataset_schema : execution stop")
            return schema_data
        except (DatasetDataNotFound,DataNotFound,DatabaseConnectionFailed) as exc:
            logging.error("data ingestion : SchemaClass : get_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : get_dataset_schema : " +traceback.format_exc())
            return exc.msg

    def map_dataset_schema(self,DBObject,connection,project_id,column_name_list,column_lst,data_type_lst,column_attribute_lst):
        """

        """
        try:
            logging.info("data ingestion : SchemaClass : map_dataset_schema : execution start")
            prev_cols_lst = []
            prev_dtype_lst = []
            
            new_cols_lst = column_lst
            cols_attribute_lst = column_attribute_lst

            table_name,cols,schema =self.get_schema()
            prev_cols_lst = column_name_list
            prev_dtype_lst = data_type_lst
            
            #check if values in schema table,data is exist or not. If exist then update the values else insert new record
            if self.is_existing_schema(DBObject,connection,project_id):
                #Iterate all column,data type,previous column name one by one to update schema table values
                for prev_col,new_col,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,cols_attribute_lst): 
                    sql_command = "update "+table_name + " SET changed_column_name = '" + new_col + "',"\
                                                                "column_attribute = '" + col_attr +"'"\
                                " Where project_id ='"+ project_id+"' and column_name ='"+prev_col+"' "
                    status = DBObject.update_records(connection,sql_command) # execute sql query command

                    if status ==1:
                        raise SchemaUpdateFailed(500)
                    
            else:
                for prev_col,new_col,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,cols_attribute_lst): 
                    row = project_id,prev_col,new_col,new_dtype,col_attr
                    row_tuples = [tuple(row)] # Make record for project table
                    logger.info(str(row_tuples) + "row tuple")
                    status = DBObject.insert_records(connection,table_name,row_tuples,cols) #insert the records into schema table
                    
                    if status ==1:
                        raise SchemaInsertionFailed(500)
            logging.info("data ingestion : SchemaClass : map_dataset_schema : execution stop")
            return status
        except (SchemaUpdateFailed,SchemaInsertionFailed) as exc:
            logging.error("data ingestion : SchemaClass : map_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : map_dataset_schema : " +traceback.format_exc())
            return exc.msg
    
    def update_dataset_schema(self,schema_data,dataset_id): ###
        """
        this function use to update the Schema table values with the new upcoming values.

        Args : 
                  column_name_list[(List)]  : [Existing table column name value]
                  column_lst [(List)]  : [Updated column name value]
                  data_type_lst [(List)]  : [Existing table column datatype value]
                  column_attribute_lst [(List)]  : []
                  column_change_datatype[(List)]  : [Updated column datatype value]
                  dataset_id [(Integer)]  : [Id of the project table]

        Return :
                [String] : [Status value if succeed return 0 else 1]

        """
        try :
            logging.info("data ingestion : SchemaClass : update_dataset_schema : execution start")
            DBObject = db.DBClass()
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
            if connection == None:
                raise DatabaseConnectionFailed(500)
            column_name_list=[] #get column name list
            column_datatype_list = [] #get column datatype list
            column_attribute_list = [] # get column attribute list
            column_change_name = [] # get column change name
            for index in range(len(schema_data)):
                if schema_data[index]["column_name"] == schema_data[index]["change_column_name"] :
                    raise SameColumnName(500)
                column_name_list.append(schema_data[index]["column_name"])
                column_datatype_list.append(schema_data[index]["data_type"])
                column_change_name.append(schema_data[index]["change_column_name"])
                column_attribute_list.append(schema_data[index]["column_attribute"])
            table_name,col,schema = self.get_schema()
            create_status = DBObject.create_table(connection,table_name,schema)
            mapping_status =self.map_dataset_schema(DBObject,connection,str(project_id),column_name_list,column_change_name,column_datatype_list,column_attribute_list) 
            logging.info("data ingestion : SchemaClass : update_dataset_schema : execution stop")
            if mapping_status == 0:
                return True
            else:
                raise SchemaUpdateFailed(500 )
        except(SameColumnName,DatabaseConnectionFailed,SchemaUpdateFailed,SchemaCreationFailed) as exc:
            logging.error("data ingestion : SchemaClass : update_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : update_dataset_schema : " +traceback.format_exc())
            return exc.msg

    
    def is_existing_schema(self,DBObject,connection,project_id):
        """
        this function checks Data for the perticular dataset Id in schema table already exist or not

        Args : 
                dataset_id[(Integer)] : [Id of the dataset table]
        Return :
                [Boolean] : [return True if record exists else False]
        """ 
        logging.info("data ingestion : SchemaClass : is_existing_schema : execution start")
        table_name,*_ = self.get_schema()  #get the table name from schema
        sql_command = "select project_id from "+ table_name +" where project_id="+project_id
        data=DBObject.select_records(connection,sql_command) #execute the query string,if record exist return dataframe else None 
        if data is None: 
            return False
        logging.info("data ingestion : SchemaClass : is_existing_schema : execution stop")
        if len(data) > 0 : #check if record found return True else False
            return True
        else:
            return False
    
    def get_attribute_datatype(self,connection,DBObject,table_name,column_name_list,no_of_rows):
        """
        this function used to get proper attribute type for the column in csv file.

        Args : 
            [(table_name)] : [ Name of te table]
            [(column_name_list)] : [List of the column name]
            [(no_of_rows)] : [No of rows in csv data]

        Return :
            [List] : [List of the predicted type attribute for columns]

        """
        logging.info("data ingestion : SchemaClass : get_attribute_datatype : execution start")
        sql_command = "SELECT * FROM "+table_name #sql query
        csv_data = DBObject.select_records(connection,sql_command) #execute sql commnad if data exist then return data else return None
        attribute_type = [] #empty list to append attribute type
        for column_name in column_name_list: #iterate column name list 
            column_data = csv_data[column_name].tolist() #get the specified column data convert into list
            unique_values = list(set(column_data)) #get the set of unique values convert into list
            if (len(unique_values)/no_of_rows) < 0.2 :
                if "," in str(column_data[1]): #check if the comma value present
                    value = "categorical list"
                else :
                    value = "categorical"
            else:
                value =  "false" #check condition if condition true then set as categorical else false
            if value =="false": 
                datatype_value = csv_data.dtypes.to_dict()[column_name] #get datatype specified for perticular column name
                if datatype_value in ['float64','float32','int32','int64']: #check if int,float,double present then set it "numerical"
                    value = "numerical"
                elif datatype_value in ['datetime64[ns]']: #check if datetime value present then set it "timestamp"
                    value = "timestamp"
                elif datatype_value in ['object']:  #check if object type value present then set it "text"
                        value = "text"
            attribute_type.append(value) #append type attribute value into list 
        logging.info("data ingestion : SchemaClass : get_attribute_datatype : execution stop")    
        return attribute_type

