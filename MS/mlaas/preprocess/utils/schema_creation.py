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
import pandas as pd
import datetime 
import traceback
from database import *
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils.activity_timeline import activity_timeline
from ingest.utils.dataset.dataset_creation import *
from dateutil.parser import parse
from ingest.utils.dataset import dataset_creation as dt

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')
timeline_Obj=activity_timeline.ActivityTimelineClass(database,user,password,host,port)
json_obj = JsonFormatClass()

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
            schema_data = json_obj.get_schema_format(column_name,predicted_datatype) #call get_schema_format to get json format data

            logging.info("data ingestion : SchemaClass :get_dataset_schema : execution stop")
            return schema_data

        except (DatasetDataNotFound,DataNotFound,DatabaseConnectionFailed) as exc:
            logging.error("data ingestion : SchemaClass : get_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : get_dataset_schema : " +traceback.format_exc())
            return exc.msg

    
    def update_dataset_schema(self,DBObject,connection,project_id,dataset_id,table_name,column_name_list,change_column_name,column_datatype_list,column_attribute_list): ###
        """
        this function used to insert the records into a table if not exist otherwise it will update the record.
        Args:
                project_id [(Integer)]  : [Id of the project table]
                dataset_id [(Integer)]  : [Id of the dataset table]
                table_name[(String)] : [updated table name]
                column_name_list[(List)]  : [Existing table column name value]
                change_column_name[(List)] : [change column values]
                data_type_lst [(List)]  : [Existing table column datatype value]
                column_datatype_list[(List)]  : [column datatype list(numeric,test,categorical)]
                column_attribute_list [(List)]  : [names of type attribute(ignore,target,select)]
                
        Return:
            [(integer)] : [return 0 if successfully inserted other wise return 1]
        """
        try :
            schema_table_name,cols,schema = self.get_schema()
            create_status = DBObject.create_table(connection,schema_table_name,schema)
            if create_status in [1,0]:
                
                prev_cols_lst = column_name_list
                new_cols_lst = change_column_name
                prev_dtype_lst = column_datatype_list
                cols_attribute_lst = column_attribute_list

                
                #check if values in schema table,data is exist or not. If exist then update the values else insert new record
                status = self.is_existing_schema(DBObject,connection,table_name)
                logging.info(str(status)+"schema status")
                if status == False  :
                    raise SchemaUpdateFailed(500)
                else:
                    for prev_col,new_col,new_dtype,col_attr in zip(prev_cols_lst,new_cols_lst,prev_dtype_lst,cols_attribute_lst):
                        if str(col_attr) !='ignore': 
                                row = project_id,str(dataset_id),table_name,prev_col,new_col,new_dtype,col_attr
                                row_tuples = [tuple(row)] # Make record for project table
                                logger.info(str(row_tuples) + "row tuple")
                                status = DBObject.insert_records(connection,schema_table_name,row_tuples,cols) #insert the records into schema table
                                
                                if status == 1:
                                    raise SchemaInsertionFailed(500)
                
            else :
                raise TableCreationFailed(500)
            
            return status
        except(DatabaseConnectionFailed,SchemaUpdateFailed,SchemaCreationFailed,IgnoreAttributeClass) as exc:
            logging.error("data ingestion : SchemaClass : update_dataset_schema : Exception " + str(exc.msg))
            logging.error("data ingestion : SchemaClass : update_dataset_schema : " +traceback.format_exc())
            return exc.msg

    
    def is_existing_schema(self,DBObject,connection,dataset_table_name):
        """
        this function checks Data for the perticular dataset Id in schema table already exist or not

        Args : 
                dataset_id[(Integer)] : [Id of the dataset table]
        Return :
                [Boolean] : [return True if record exists else False]
        """ 
        logging.info("data ingestion : SchemaClass : is_existing_schema : execution start")
        table_name,*_ = self.get_schema()  #get the table name from schema

        sql_command = "select project_id from "+ table_name +" where table_name='"+dataset_table_name+"'"
        logging.info(str(sql_command)+" is_existing_schema")
        data=DBObject.select_records(connection,sql_command) #execute the query string,if record exist return dataframe else None 

        if data is None: 
            return True
        if len(data) > 0 :

                #command will delete the records of the given table name from schema table
                sql_command = "delete from mlaas.schema_tbl where table_name='"+dataset_table_name+"'"
                logging.info(str(sql_command)+" is_existing_schema")
                status = DBObject.delete_records(connection,sql_command)

                if status==0:
                    return True
                else:
                    return False
        else:
            return True
        
    
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
    
    def save_schema(self,DBObject,connection,connection_string,schema_data,project_id,dataset_id):
        """
       
        Args :
                schema_data[(List)]   : [list of dictonery with details of schema]
                project_id[(Integer)] : [Id of the project table]
        Return :
                [Integer|string] : [return 0 if successfully updated else return error string]
        """
        try:
            logging.info("data ingestion : SchemaClass : save_schema : execution start")
            logging.info(str(dataset_id)+" dataset")
            column_name_list=[] #get column name list
            column_attribute_list = [] # get column attribute list
            column_datatype_list = [] #get column datatype list
            change_column_name = [] # get change column name

            for index in range(len(schema_data)):
                logging.info("call_for_loop_extract")
                change_column_name.append(schema_data[index]["change_column_name"])
                column_datatype_list.append(schema_data[index]["data_type"])
                column_name_list.append(schema_data[index]["column_name"])
                column_attribute_list.append(schema_data[index]["column_attribute"])
            
            logging.info(str(column_name_list)+"  column_name_list")
            logging.info(str(column_attribute_list)+"  column_attribute_list")
            logging.info(str(column_datatype_list)+"  column_datatype_list")
            logging.info(str(change_column_name)+"  change_column_name")

            #check For all column if attribute type are ignore then return True and raise error else False
            check_attribute_type = True if len(column_attribute_list) == column_attribute_list.count("ignore") else False
            if check_attribute_type == True :
                raise IgnoreAttributeClass(500)
            
            dataframe = DBObject.get_project_detail(DBObject,connection,project_id)
            dataset_id = dataframe['dataset_id'][0]

            sql_command = "SELECT dataset_table_name,user_name,dataset_visibility from mlaas.dataset_tbl where dataset_id='"+str(dataset_id)+"' "
            logging.info(str(sql_command) +" dataset details")

            dataframe = DBObject.select_records(connection,sql_command)
            dataframe = dataframe.to_records(index=False) # convert dataframe to a NumPy record
            
            dataset_table_name,user_name,dataset_visibility = dataframe[0] #Get all dataset table details into respective variables
            dataset_table_name,user_name,dataset_visibility =str(dataset_table_name),str(user_name),str(dataset_visibility)

            if dataset_visibility =="private":
                table_name = user_name+"."+'"'+dataset_table_name+'"'
            else:
                table_name = dataset_table_name

            
            status = self.alter_table_data(DBObject,connection,table_name,change_column_name,column_name_list,column_attribute_list)

            
            if status == 0:

                schema_status = self.update_dataset_schema(DBObject,connection,project_id,dataset_id,dataset_table_name,column_name_list,change_column_name,column_datatype_list,column_attribute_list)
                if schema_status == 0:
                    
                    sql_command = "UPDATE mlaas.project_tbl set dataset_id="+str(dataset_id)+" where project_id="+str(project_id)
                    update_status = DBObject.update_records(connection,sql_command)
                else:
                    raise SchemaUpdateFailed(500)
            else:
                raise UpdatingTableStructureFailed(500)

            logging.info("data ingestion : SchemaClass : save_schema : execution stop")
            return update_status

        except (DatasetCreationFailed,SchemaUpdateFailed,IgnoreAttributeClass,TableCreationFailed,UpdatingTableStructureFailed) as exc:
            logging.error("data ingestion : ingestclass : create_dataset : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : create_dataset : " +traceback.format_exc())
            return exc.msg
        

    def alter_table_data(self,DBObject,connection,table_name,change_column_name,column_name_list,column_attribute_list):
            logging.info("alter_table_data")
            status = 0
            for index in range(len(column_name_list)):
                if column_attribute_list[index]=='ignore':
                    logging.info("call_ignore")
                    sql_command = 'ALTER TABLE '+table_name+' DROP COLUMN "'+str(column_name_list[index])+'";'
                    logging.info(str(sql_command)+"  Ignore ")
                    status = DBObject.update_records(connection,sql_command)
                    logging.info(str(status)+"  status for Ignore ")
                        
                elif (change_column_name[index] != column_name_list[index]) and (change_column_name[index] != ''):
                        sql_command = 'ALTER TABLE '+table_name+' RENAME COLUMN "'+str(column_name_list[index])+'" TO "'+str(change_column_name[index])+'";'
                        logging.info(str(sql_command)+"  Rename")
                        status = DBObject.update_records(connection,sql_command)
                        logging.info(str(status)+"  status for Rename")
                            
                if status==1:
                    return status
            return status
    

    # def update_timeline(self,project_id,dataset_id,column_name_list,column_attribute_list,change_column_name,method_type,dataset_name):
    #     """
    #     function used to insert record all the changes done in schema mapping into activity timeline table that performed by user.
    #     1)For the column been selected and target , 
    #     2)For the column been ignore
    #     3)For the column name updated
    #     4)For "Save as" option Updated dataset name inserted by user

    #     Args:
    #             project_id[(Integer)]:[Id of the project]
    #             dataset_id[(Integer)]:[Id of the dataset]
    #             method_type[(String)]:[Name of the method(Save,Save as)]
    #             dataset_name[(String)]:[Updated dataset name uploaded  by user]
    #             column_name_list[(List)]  : [Existing table column name value]
    #             change_column_name[(List)] : [Change column name values]
    #             column_attribute_list [(List)]  : [name of type attribute(select,ignore,target)]
    #     Return :
    #             [(Boolean)] : [return True if successfully updated record else return False]
    #     """
    #     logging.info("data ingestion : SchemaClass : update_timeline : execution start")
    #     column_name,column_change,target_column_lst,selected_column_lst,ignore_column_list= self.get_schema_column_values(column_name_list,column_attribute_list,change_column_name)
    #     activity_id =[5,6,7,8]
    #     activity_description=""

    #     for id in activity_id:
    #         activity_df = timeline_Obj.get_activity(id,"US")
    #         activity_name = activity_df[0]["activity_name"]
    #         activity_description = "{x}".format(x=activity_df[0]["activity_description"])
    #         activity=""
    #         if id==5:
    #             for index in range(len(column_name)):
    #                 activity += activity_description.replace('*',column_name[index]).replace('?',column_change[index])+"," 

    #         elif id==6:
    #             column_target='"'+",".join(target_column_lst)+'"'
    #             column_selected='"'+",".join(selected_column_lst)+'"'
    #             activity += activity_description.replace('*',column_selected).replace('?',column_target)+","

    #         elif id==7:
    #             column_ignore='"'+",".join(ignore_column_list)+'"'
    #             activity += activity_description.replace('*',column_ignore)+","

    #         elif id==8:
    #             if method_type=='Save as':
    #                 activity = activity_description.replace('*',dataset_name)+","
    #             else:
    #                 break
                
    #         activity_description = activity[0:len(activity)-1]
    #         timestamp = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    #         operation = activity_df[0]["operation"]
    #         status = timeline_Obj.insert_user_activity(user_name,project_id,dataset_id,activity_name,activity_description,timestamp,operation)
    #         if status==False:
    #             logger.info("Insert failed at "+str(activity_name))
    #             break
    #     logging.info("data ingestion : SchemaClass : update_timeline : execution stop")
    #     return status
    
