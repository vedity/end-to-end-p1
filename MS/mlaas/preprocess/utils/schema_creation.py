'''
/*CHANGE HISTORY
--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 
*/
'''


import logging
import traceback
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('Schema_creation')
json_obj = JsonFormatClass()  # Initialize the JsonFormat Class

class SchemaClass:
            
    def get_schema(self):
        # schema table name
        table_name = 'mlaas.schema_tbl'
        # Columns for schema table
        cols = 'schema_id,column_name,changed_column_name,data_type,column_attribute' 
        # Schema of schema_table
        schema ="index bigserial,"\
                "schema_id bigint,"\
                "column_name  text,"\
                "changed_column_name  text,"\
                "data_type  text,"\
                "column_attribute  text"
                
        return table_name,cols,schema
    
    def get_dataset_schema(self,DBObject,connection,dataset_id):
        """
        this function used to get the column name and datatype of the given dataset id.

        Args :
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
                
                column_name_list[List] : [return the list column name]
                predicted_datatype[List] : [return the list of datatype of the columns]
        """
        try:
            logging.info("data preprocess : SchemaClass :get_dataset_schema : execution start")
            
            #get the dataset table details based on the dataset id
            dataset_df = DBObject.get_dataset_detail(DBObject,connection,dataset_id)

            #check the dataset_df is empty or not if yes raise exception
            if dataset_df is None or len(dataset_df) == 0:
                        raise DatasetDataNotFound(500)

            dataset_records = dataset_df.to_records(index=False) # convert dataframe to a NumPy record  

            dataset_name,dataset_table_name,user_name,dataset_visibility,no_of_rows,_ = dataset_records[0] # first record of dataset

            dataset_name,dataset_table_name,user_name,dataset_visibility = str(dataset_name),str(dataset_table_name),str(user_name),str(dataset_visibility)

            #check the dataset visibility if private append the user name with  dataset table name 
            #dataset visibility if public assign table name as  dataset table name we get
            if dataset_visibility =="private":
                table_name=user_name+"."+dataset_table_name
            else:
                
                table_name = dataset_table_name
            
            #get the column list and datatype  based on given table name
            column_name_list,predicted_datatype = self.get_attribute_datatype(connection,DBObject,table_name)

            logging.info("data preprocess : SchemaClass :get_dataset_schema : execution stop")
            return column_name_list,predicted_datatype

        except (DatasetDataNotFound,DataNotFound,DatabaseConnectionFailed) as exc:
            logging.error("data preprocess : SchemaClass : get_dataset_schema : Exception " + str(exc.msg))
            logging.error("data preprocess : SchemaClass : get_dataset_schema : " +traceback.format_exc())
            return exc.msg

    

    
    def get_attribute_datatype(self,connection,DBObject,table_name):
        """
        this function used to get proper attribute type for the column in csv file.

        Args : 
            [(table_name)] : [ Name of te table]
            [(column_name_list)] : [List of the column name]
            [(no_of_rows)] : [No of rows in csv data]

        Return :
            [List] : [List of the predicted type attribute for columns]

        """
        try:
            logging.info("data preprocess : SchemaClass : get_attribute_datatype : execution start")

            sql_command = "SELECT * FROM "+table_name #sql query

            csv_data = DBObject.select_records(connection,sql_command) #execute sql commnad if data exist then return data else return None
            if csv_data is None or len(csv_data) == 0:
                raise TableDataNotFound(500)

            column_name_list = csv_data.columns.values.tolist() # covert the dataframe into list

            no_of_rows = csv_data.shape[1]

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

            logging.info("data preprocess : SchemaClass : get_attribute_datatype : execution stop")    
            return column_name_list,attribute_type

        except (TableDataNotFound) as exc:
            logging.error("data preprocess : ingestclass : save_schema : Exception " + str(exc.msg))
            logging.error("data preprocess : ingestclass : save_schema : " +traceback.format_exc())
            return exc.msg




    def save_schema(self,DBObject,connection,schema_data,schema_id):
        """
        function used to update the changed columns values in schema table  

        Args :
                schema_data[(List)]   : [list of dictonery with details of schema]
                schema_id[(Integer)] : [Id of the schema table]
        Return:
                [Integer|string] : [return 0 if successfully updated else return error string]
        """
        try:
            logging.info("data preprocess : SchemaClass : save_schema : execution start")
            column_name_list=[] #get column name list

            column_attribute_list = [] # get column attribute list

            change_column_name = [] # get change column 
            
            index_list = [] #get the index id
 

            for count in range(len(schema_data)):

                    #check if change column and  prev column are same or not
                    if schema_data[count]["change_column_name"] == schema_data[count]["column_name"]: 
                        raise SameColumnNameFound(500)
                    change_col_name = str(schema_data[count]["change_column_name"])
                    if change_col_name.find('(') !=-1 or  change_col_name.find(')') !=-1 or change_col_name.find('%')!=-1:
                        raise InvalidColumnName(500)

                    index_list.append(schema_data[count]["index"]) #append  index 

                    change_column_name.append(schema_data[count]["change_column_name"]) #append change column name

                    column_name_list.append(schema_data[count]["column_name"]) #append column_name

                    column_attribute_list.append(schema_data[count]["column_attribute"]) #append attribute type
            
            column_datatype_list=None
            schema_status = self.update_dataset_schema(DBObject,connection,schema_id,column_name_list,column_datatype_list,change_column_name,column_attribute_list,index_list)
            

            logging.info("data preprocess : SchemaClass : save_schema : execution stop")
            return schema_status

        except (SchemaUpdateFailed,TableCreationFailed,SameColumnNameFound,InvalidColumnName) as exc:
            logging.error("data preprocess : ingestclass : save_schema : Exception " + str(exc.msg))
            logging.error("data preprocess : ingestclass : save_schema : " +traceback.format_exc())
            return exc.msg
        
    def update_dataset_schema(self,DBObject,connection,schema_id,column_name_list,column_datatype_list,change_column_name=None,column_attribute_list=None,index_list=None): ###
        """
        this function used to insert the records into a table if not exist otherwise it will update the existing schema data record from the table.
        Args:
                schema_id [(Integer)]  : [Id of the schema table]
                column_name_list[(List)]  : [Existing table column name value]
                change_column_name[(List)] : [change column values]
                data_type_lst [(List)]  : [Existing table column datatype value]
                column_datatype_list[(List)]  : [column datatype list(numeric,test,categorical)]
                column_attribute_list [(List)]  : [names of type attribute(Ignore,target,select)]
                index_list[(List)] : [Id of index column ]
        Return:
            [(integer)] : [return 0 if successfully inserted other wise return 1]
        """
        try :
            logging.info("data preprocess : SchemaClass : update_dataset_schema : execution start")

            #get the table name and columns,and schema of the table
            schema_table_name,cols,schema = self.get_schema()

            #create the schema table if already created return 1,if not return 0
            create_status = DBObject.create_table(connection,schema_table_name,schema)

            if create_status in [1,0]:

                #check if values in schema table,data is exist or not. If exist then update the values else insert new record
                status = self.is_existing_schema(DBObject,connection,schema_id)

                if status == True  :
                    new_cols_lst = change_column_name
                    cols_attribute_lst = column_attribute_list

                    for index,new_col,col_attr in zip(index_list,new_cols_lst,cols_attribute_lst): 

                        #sql command for updating change_column_name and column_attribute column  based on index column value
                        sql_command = "update "+ schema_table_name + " SET changed_column_name = '" + str(new_col) + "',"\
                                                                    "column_attribute = '" +str(col_attr) +"'"\
                                    " Where index ='"+str(index)+"' "

                        #execute sql query command
                        status = DBObject.update_records(connection,sql_command) 

                        if status ==1:
                            raise SchemaUpdateFailed(500)
                else:
                    prev_dtype_lst = column_datatype_list
                    prev_cols_lst = column_name_list
                    new_cols_lst = ''
                    cols_attribute_lst = 'Select'
                    for prev_col,new_dtype in zip(prev_cols_lst,prev_dtype_lst): 

                        row = schema_id,prev_col,new_cols_lst,new_dtype,cols_attribute_lst

                        # Make record for project table
                        row_tuples = [tuple(row)] 
                        
                        #insert the records into schema table
                        status = DBObject.insert_records(connection,schema_table_name,row_tuples,cols) 
                        if status ==1:
                            raise SchemaInsertionFailed(500)

                
            else :
                raise TableCreationFailed(500)
            
            logging.info("data preprocess : SchemaClass : update_dataset_schema : execution stop ")
            return status
        except(SchemaUpdateFailed,TableCreationFailed,SchemaInsertionFailed) as exc:
            logging.error("data preprocess : SchemaClass : update_dataset_schema : Exception " + str(exc.msg))
            logging.error("data preprocess : SchemaClass : update_dataset_schema : " +traceback.format_exc())
            return exc.msg

    
    def is_existing_schema(self,DBObject,connection,schema_id):
        """
        this function used to  check the  Data for the given schema Id in schema table where data is already exist or not.

        Args : 
                schema_id[(Integer)] : [Id of the schema table]
        Return :
                [Boolean] : [return True if record exists else False]
        """ 
        try:
            logging.info("data preprocess : SchemaClass : is_existing_schema : execution start")

            #get the table name from schema
            table_name,*_ = self.get_schema() 

            #this sql command will get schema_id if found.
            sql_command = "select schema_id from "+ table_name +" where schema_id='"+str(schema_id)+"'"

            #execute the query string,if record exist return dataframe else None
            data=DBObject.select_records(connection,sql_command) 

            
            if len(data) > 0: 
                Flag = True
            else:
                Flag = False

            logging.info("data preprocess : SchemaClass : is_existing_schema : execution stop")
            return Flag
        except Exception as exc:
            logging.error("data preprocess : SchemaClass : is_existing_schema : Exception " + str(exc))
            logging.error("data preprocess : SchemaClass : is_existing_schema : " +traceback.format_exc())
            return str(exc)
        
    
    def get_schema_data(self,DBObject,connection,schema_id):
        """
        function used to get the schema table details based on the schema id.
        Args : 
                schema_id[(Integer)] : [Id of the schema table]
        Return :
                [List] : [schema details in form of list of dictonery]
        """
        try :
            logging.info("data preprocess : SchemaClass : get_schema_data : execution start")

            # get the table name
            table_name,_,_ = self.get_schema()
            
            # sql command to get details from schema table  based on  schema id 
            sql_command = " SELECT * FROM "+table_name+" WHERE schema_id ='"+str(schema_id)+"' order by index"
        
            #execute sql commnad if data exist then return dataframe else return None
            schema_df = DBObject.select_records(connection,sql_command) 
            
            if schema_df is None or len(schema_df) == 0:
                raise SchemaDataNotFound(500)

            #store all the schema table data into 
            index,column_name,changed_column_name,data_type,column_attribute = schema_df['index'],schema_df['column_name'],schema_df['changed_column_name'],schema_df['data_type'],schema_df['column_attribute']
            
            #get the appropriate structure format  
            schema_data=json_obj.get_schema_format(index,column_name,changed_column_name,data_type,column_attribute)
            
            logging.info("data preprocess : SchemaClass : get_schema_data : execution stop")
            return schema_data
        except (SchemaDataNotFound) as exc:
            logging.error("data preprocess : SchemaClass : get_schema_data : Exception " + str(exc.msg))
            logging.error("data preprocess : SchemaClass : get_schema_data : " +traceback.format_exc())
            return exc.msg
    
    def get_query_string(self,DBObject,connection,schema_id):
        try:
            logging.info("data preprocess : SchemaClass : get_query_string : execution start")
            # sql command to get details from schema table  based on  schema id 
            sql_command = "select column_name,case when changed_column_name = '' then column_name else changed_column_name end column_list  from mlaas.schema_tbl where schema_id ="+str(schema_id)+"order by index"
            
            #execute sql commnad if data exist then return dataframe else return None
            schema_df = DBObject.select_records(connection,sql_command) 

            #extract the column name and column_list
            column_name,column_list = schema_df['column_name'],schema_df['column_list']

            string_query = ""
            for count in range(1,len(column_name)):
                #append string column name as alias  column list name
                string_query +='"'+column_name[count]+'" as '+column_list[count]+','
            
            logging.info("data preprocess : SchemaClass : get_query_string : execution stop")
            return string_query[:len(string_query)-1]
        except  Exception as exc:
            logging.error("data preprocess : SchemaClass : get_query_string : Exception " + str(exc))
            logging.error("data preprocess : SchemaClass : get_query_string : " +traceback.format_exc())
            return exc
        




    

   
