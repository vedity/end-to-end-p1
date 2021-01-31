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
from .dataset.dataset_creation import *
from .dataset import dataset_creation
from dateutil.parser import parse
import pandas as pd
import traceback
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')
from .dataset import dataset_creation as dt
class SchemaClass(dt.DatasetClass):
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
        cols = 'project_id,dataset_id,table_name,column_name,changed_column_name,data_type,column_attribute' 
        # Schema of schema_table
        schema ="project_id bigint,"\
                "dataset_id bigint,"\
                "table_name text,"\
                "column_name  text,"\
                "changed_column_name  text,"\
                "data_type  text,"\
                "column_attribute  text"
                
        return table_name,cols,schema
    
    def get_dataset_schema(self,project_id,dataset_id):
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
            
            sql_command = "SELECT project_id,dataset_id from mlaas.schema_tbl where project_id='"+str(project_id)+"' and dataset_id='"+str(dataset_id)+"'" 
            logging.info("sql_command"+sql_command )
            dataset_df = DBObject.select_records(connection,sql_command)
            if dataset_df is None or len(dataset_df)==0 :
                    # project_df = DBObject.get_project_detail(DBObject,connection,project_id)
                    # dataset_id = project_df['dataset_id'][0]

                    dataset_df = DBObject.get_dataset_detail(DBObject,connection,dataset_id)
                    if dataset_df is None or len(dataset_df) == 0:
                        raise DatasetDataNotFound(500)
                    dataset_records = dataset_df.to_records(index=False) # convert dataframe to a NumPy record  
                    dataset_name,dataset_table_name,user_name,dataset_visibility,no_of_rows,_ = dataset_records[0]
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
                    
            else:
                    sql_command = "SELECT column_name,changed_column_name,data_type,column_attribute from mlaas.schema_tbl where project_id='"+str(project_id)+"' and dataset_id='"+str(dataset_id)+"'"
                    logging.info("sql_command"+sql_command )
                    dataset_df = DBObject.select_records(connection,sql_command)
                    if dataset_df is None or len(dataset_df)==0:
                        raise DataNotFound(500)
                    column_name,changed_column_name,data_type,column_attribute = dataset_df['column_name'],dataset_df['changed_column_name'],dataset_df['data_type'],dataset_df['column_attribute']
                    schema_data= get_updated_schema_format(column_name,changed_column_name,data_type,column_attribute)

            logging.info("data ingestion : SchemaClass :get_dataset_schema : execution stop")
            return schema_data

        except (DatasetDataNotFound,DataNotFound,DatabaseConnectionFailed) as exc:
            logging.error("data ingestion : SchemaClass : get_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : get_dataset_schema : " +traceback.format_exc())
            return exc.msg

    def map_dataset_schema(self,DBObject,connection,project_id,dataset_id,table_name,column_name_list,column_lst,data_type_lst,column_attribute_lst):
        """
        this function used to insert the records into a table if not exist otherwise it will update the record.
        Args:
                column_name_list[(List)]  : [Existing table column name value]
                column_lst [(List)]  : [Updated column name value]
                data_type_lst [(List)]  : [Existing table column datatype value]
                column_attribute_lst [(List)]  : [name of type attribute(ignore,target)]
                column_change_datatype[(List)]  : [Updated column datatype value]
                project_id [(Integer)]  : [Id of the project table]
                dataset_id [(Integer)]  : [Id of the dataset table]
                table_name[(String)] : [updated table name]
        Return:
            [(integer)] : [return 0 if successfully inserted or updated other wise return 1]
        """
        try:
            logging.info("data ingestion : SchemaClass : map_dataset_schema : execution start")
            prev_cols_lst = []
            prev_dtype_lst = []
            
            new_cols_lst = column_lst
            cols_attribute_lst = column_attribute_lst

            schema_table_name,cols,schema =self.get_schema()
            prev_cols_lst = column_name_list
            prev_dtype_lst = data_type_lst
            
            #check if values in schema table,data is exist or not. If exist then update the values else insert new record
            if self.is_existing_schema(DBObject,connection,project_id,dataset_id):
                #Iterate all column,data type,previous column name one by one to update schema table values
                for prev_col,new_col,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,cols_attribute_lst): 
                    sql_command = "update "+ schema_table_name + " SET changed_column_name = '" + new_col + "',"\
                                                                "column_attribute = '" + col_attr +"'"\
                                " Where project_id ='"+ project_id+"' and dataset_id ='"+ dataset_id +"' "
                    status = DBObject.update_records(connection,sql_command) # execute sql query command

                    if status ==1:
                        raise SchemaUpdateFailed(500)
                    
            else:
                for prev_col,new_col,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,cols_attribute_lst): 
                    row = project_id,dataset_id,table_name,prev_col,new_col,new_dtype,col_attr
                    row_tuples = [tuple(row)] # Make record for project table
                    logger.info(str(row_tuples) + "row tuple")
                    status = DBObject.insert_records(connection,schema_table_name,row_tuples,cols) #insert the records into schema table
                    
                    if status ==1:
                        raise SchemaInsertionFailed(500)
            logging.info("data ingestion : SchemaClass : map_dataset_schema : execution stop")
            return status
        except (SchemaUpdateFailed,SchemaInsertionFailed) as exc:
            logging.error("data ingestion : SchemaClass : map_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : map_dataset_schema : " +traceback.format_exc())
            return exc.msg
    
    def update_dataset_schema(self,DBObject,connection,project_id,dataset_id,table_name,column_name_list,column_change_name,column_datatype_list,column_attribute_list): ###
        """
        this function use to update the Schema table values with the new upcoming values.

        Args : 
                project_id [(Integer)]  : [Id of the project table]

        Return :
                [String] : [Status value if succeed return 0 else 1]

        """
        try :
            logging.info("data ingestion : SchemaClass : update_dataset_schema : execution start")
            schema_table_name,col,schema = self.get_schema()
            create_status = DBObject.create_table(connection,schema_table_name,schema)
            if create_status in [1,0]:
                mapping_status =self.map_dataset_schema(DBObject,connection,str(project_id),str(dataset_id),table_name,column_name_list,column_change_name,column_datatype_list,column_attribute_list) 
                logging.info("data ingestion : SchemaClass : update_dataset_schema : execution stop")
                if mapping_status == 0:
                    return True
                else:
                    raise SchemaUpdateFailed(500)
            else :
                raise TableCreationFailed(500)
            
            
        except(SameColumnName,DatabaseConnectionFailed,SchemaUpdateFailed,SchemaCreationFailed,IgnoreAttributeClass) as exc:
            logging.error("data ingestion : SchemaClass : update_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : update_dataset_schema : " +traceback.format_exc())
            return exc.msg

    
    def is_existing_schema(self,DBObject,connection,project_id,dataset_id):
        """
        this function checks Data for the perticular dataset Id in schema table already exist or not

        Args : 
                dataset_id[(Integer)] : [Id of the dataset table]
        Return :
                [Boolean] : [return True if record exists else False]
        """ 
        logging.info("data ingestion : SchemaClass : is_existing_schema : execution start")
        table_name,*_ = self.get_schema()  #get the table name from schema
        sql_command = "select project_id from "+ table_name +" where project_id='"+project_id+"' and dataset_id ='"+dataset_id+"'"
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
                    vaslue = "timestamp"
                elif datatype_value in ['object']:  #check if object type value present then set it "text"
                        value = "text"
            attribute_type.append(value) #append type attribute value into list 
        logging.info("data ingestion : SchemaClass : get_attribute_datatype : execution stop")    
        return attribute_type
    
    def save_schema(self,DBObject,connection,connection_string,schema_data,project_id,method_name,dataset_name=None,dataset_desc=None,visibility=None):
        """
        function used to call create dataset function to insert a record into dataset table with(if click in save) always private visibility,
        (if click on Save as) then visibility can be private or public,
        call update_dataset_schema function which update the schema of the selected dataset and
        update the column[link_dataset_id] in project table with dataset_id which newly created in dataset table.
        
        Args :
                schema_data[(List)]   : [list of dictonery with details of schema]
                project_id[(Integer)] : [Id of the project table]
        Return :
                [Integer|string] : [return 0 if successfully updated else return error string]
        """
        try:
            logging.info("data ingestion : SchemaClass : save_schema : execution start")
            column_name_list=[] #get column name list
            column_attribute_list = [] # get column attribute list
            column_datatype_list = [] #get column datatype list
            column_change_name = [] # get change column name
            for index in range(len(schema_data)):
                if schema_data[index]["change_column_name"] == "":
                    column_change_name.append(schema_data[index]["column_name"])
                else:
                    column_change_name.append(schema_data[index]["change_column_name"])
                column_datatype_list.append(schema_data[index]["data_type"])
                column_name_list.append(schema_data[index]["column_name"])
                column_attribute_list.append(schema_data[index]["column_attribute"])
            
            # check For all column if attribute type are ignore then return True and raise error else False
            check_attribute_type = True if len(column_attribute_list) == column_attribute_list.count("ignore") else False
            if check_attribute_type == True :
                raise IgnoreAttributeClass(500)
            select_query = self.get_query_string(column_name_list,column_change_name,column_attribute_list)
            dataframe = DBObject.get_project_detail(DBObject,connection,project_id)
            dataset_id = dataframe['dataset_id'][0]
            dataset_status,dataset_id,table_name = self.create_dataset(DBObject,connection,connection_string,select_query,dataset_id,method_name,dataset_name,dataset_desc,visibility)
            if dataset_status ==0:
                schema_status = self.update_dataset_schema(DBObject,connection,project_id,dataset_id,table_name,column_name_list,column_change_name,column_datatype_list,column_attribute_list)
                if schema_status ==True:
                    sql_command = "UPDATE mlaas.project_tbl set link_dataset_id="+str(dataset_id)+" where project_id="+str(project_id)
                    update_status = DBObject.update_records(connection,sql_command)
                else:
                    raise SchemaUpdateFailed(500)
            else:
                raise DatasetCreationFailed(500)
            logging.info("data ingestion : SchemaClass : save_schema : execution stop")
            return update_status
        except (DatasetCreationFailed,SchemaUpdateFailed,IgnoreAttributeClass) as exc:
            logging.error("data ingestion : ingestclass : create_dataset : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : create_dataset : " +traceback.format_exc())
            return exc.msg
        
    
    def get_query_string(self,column_name_list,column_change_name,column_attribute_list):
        """
        function used to generate query string which will be used in select query to fetch the details.

        Args :
                column_name_list[(List)]       : [Existing table column name value]
                column_change_name [(List)]    : [change column name value]
                column_attribute_lst [(List)]  : [name of type attribute list]
        Return :
                [String] : [return the query string]
        """
        logging.info("data ingestion : SchemaClass : get_query_string : execution start")
        query = ""
        for index in range(len(column_attribute_list)):
            if column_attribute_list[index] !='ignore':
                query +='"'+column_name_list[index]+'" as '+column_change_name[index]+',' # append the string
        logging.info("data ingestion : SchemaClass : get_query_string : execution stop")       
        return query[0:len(query)-1]

    def create_dataset(self,DBObject,connection,connection_string,select_query,dataset_id,method_name,dataset_name,dataset_desc,visibility):
        """
        function will insert new record in dataset table and update the schema table with selected 
        column name and attribute and load the csv data into table.
        Args :
                select_query[(String)] : [String query which used in "sql query"]
                dataset_id[(Integer)]  : [Id of the dataset]
        Return :
                [integer,integer,string] : [dataset status(0) if success else status(1),ID of the dataset,name of table]
        """
        try:
            logging.info("data ingestion : SchemaClass : create_dataset : execution start")
            dataframe = DBObject.get_dataset_detail(DBObject,connection,dataset_id)
            dataframe = dataframe.to_records(index=False) # convert dataframe to a NumPy record
            dataset_name,dataset_table_name,user_name,dataset_visibility,_,dataset_desc = dataframe[0]
            dataset_name,dataset_table_name,user_name,dataset_visibility,dataset_desc = str(dataset_name),str(dataset_table_name),str(user_name),str(dataset_visibility),str(dataset_desc)
            if dataset_visibility =="private":
                table_name = user_name+"."+dataset_table_name
            else:
                table_name = dataset_table_name
            sql_command = "SELECT "+select_query+" from "+table_name # sql_query
            file_data_df = DBObject.select_records(connection,sql_command) # execute the sql command and get the dataframe
            table_name = self.get_table_name(DBObject,connection,dataset_table_name) # get the updated table name
            page_name = "Schema mapping" 
            parent_dataset_id=int(dataset_id) 
              
            if method_name =='Save as':
                dataset_name = dataset_name 
                dataset_visibility = visibility
                dataset_desc = dataset_desc
            else:
                dataset_visibility ="private"

            dataset_status,dataset_id = super(SchemaClass,self).make_dataset(DBObject,connection,dataset_name,table_name,dataset_visibility,user_name,dataset_desc,page_name,parent_dataset_id,method_name,flag=1)
            if dataset_status == 2:
                raise DatasetAlreadyExist(500)
            
            elif dataset_status == 1 :
                raise DatasetCreationFailed(500)
            # Condition will check dataset successfully created or not. if successfully then 0 else 1.
            elif dataset_status == 0 :
                load_dataset_status = DBObject.load_csv_into_db(connection_string,table_name,file_data_df,user_name)
                if load_dataset_status == 1:
                    raise LoadCSVDataFailed(500)
            logging.info("data ingestion : SchemaClass : create_dataset : execution stop")
            return load_dataset_status,dataset_id,table_name
        except (DatasetAlreadyExist,DatasetCreationFailed,LoadCSVDataFailed) as exc:
            logging.error("data ingestion : ingestclass : create_dataset : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : create_dataset : " +traceback.format_exc())
            return exc.msg,None,None
    
    def get_table_name(self,DBObject,connection,table_name):
        """
        function used to create table name by adding unique sequence number init.
        Args :
                table_name[(String)] : [Name of old table]
        Return :
                [String] : [return the table name]
        """
        logging.info("data ingestion : SchemaClass : get_table_name : execution start")
        split_value = table_name.split('_tbl')[0].split('_')[-1] # Extract the sequence number
        table_name = table_name.split(split_value) # split with the sequence number
        seq = DBObject.get_sequence(connection) #get the sequence number
        table_name = table_name[0]+str(seq['nextval'][0])+table_name[1] #create table name by joining sequence
        logging.info("data ingestion : SchemaClass : get_table_name : execution stop")
        return table_name
    



