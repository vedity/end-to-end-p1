'''
/*CHANGE HISTORY
--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 
*/
'''


import logging
import traceback
import datetime
from database import *
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils.activity_timeline import activity_timeline

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('Schema_creation')
json_obj = JsonFormatClass()  # Initialize the JsonFormat Class
timeline_Obj=activity_timeline.ActivityTimelineClass(database,user,password,host,port) #initialize the ActivityTimeline Class

class SchemaClass:
            
    def get_schema(self):
        # schema table name
        table_name = 'mlaas.schema_tbl'
        # Columns for schema table
        cols = 'schema_id,column_name,changed_column_name,data_type,column_attribute,missing_flag,noise_flag' 
        # Schema of schema_table
        schema ="index bigserial,"\
                "schema_id bigint,"\
                "column_name  text,"\
                "changed_column_name  text,"\
                "data_type  text,"\
                "column_attribute  text,"\
                "missing_flag text,"\
                "noise_flag text"
                
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
                table_name=user_name+'."'+dataset_table_name+'"'
                
            else:
                
                table_name = 'public."'+dataset_table_name+'"'
            
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
            logging.info(str(sql_command)+ "command")
            csv_data = DBObject.select_records(connection,sql_command) #execute sql commnad if data exist then return data else return None
            
            if csv_data is None or len(csv_data) == 0:
                raise TableDataNotFound(500)

            column_name_list = csv_data.columns.values.tolist() # covert the dataframe into list

            no_of_rows = csv_data.shape[0]

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


    def save_schema(self,DBObject,connection,schema_data,project_id,dataset_id,schema_id):
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
 
            target_count = 0
            for count in range(len(schema_data)):


                #check if change column and  prev column are same or not
                if schema_data[count]["change_column_name"] == schema_data[count]["column_name"]: 
                    raise SameColumnNameFound(500)

                change_col_name = str(schema_data[count]["change_column_name"])

                if change_col_name.find('(') !=-1 or  change_col_name.find(')') !=-1 or change_col_name.find('%')!=-1:
                    raise InvalidColumnNames(500)
                            
                if len(schema_data[count]["change_column_name"]) == 0:

                    change_column_name.append(schema_data[count]["column_name"]) #append change column name
                else:
                    change_column_name.append(schema_data[count]["change_column_name"])

                index_list.append(schema_data[count]["index"]) #append  index 

                column_name_list.append(schema_data[count]["column_name"]) #append column_name
                
                #Check if  Target attribute incoming
                if schema_data[count]["column_attribute"] == 'Target':

                    #Increment variable by 1 if Target attribute is present
                    target_count+=1

                    #Check if "target_count" variable having value greater then 1 then raise exception
                    if target_count > 1:
                        raise TargetAttributeException(500)

                column_attribute_list.append(schema_data[count]["column_attribute"]) #append attribute type

            logging.info(str(change_column_name)+" change_column_name")
            logging.info(str(column_name_list)+" column_name_list")
            logging.info(str(column_attribute_list)+" column_attribute_list")

            for value in change_column_name:
                if value != '':
                    #check the changed column name having same name
                    #?if name count in canged column list is greater then one means its duplicate then raise exception 
                    if str(change_column_name).strip().count(str(value).strip()) > 1 :
                        raise ChangeColumnNameSame(500)



            index_value = self.get_target_attribute_index(DBObject,connection,schema_id)
            logging.info(str(index_value) + " index ")
            #if index value is not Zero 
            #? Then in schema table having a column with target Attribute 
            if index_value !=0 and column_attribute_list.count('Target')>=1:
                #if the index value is not present in index_list raise
                if index_value not in index_list:
                    raise TargetAttributeExistException(500)


            column_count_value,ignore_count_value = self.get_count_value(DBObject,connection,schema_id)

            if (column_count_value-ignore_count_value)== column_attribute_list.count('Ignore') and column_attribute_list.count('Select')>=1 and column_attribute_list.count('Target')==0 :
                raise IgnoreColumns(500)


            #set the datatype list none
            column_datatype_list=None
            
            #updated the schema details 
            schema_status = self.update_dataset_schema(DBObject,connection,schema_id,column_name_list,column_datatype_list,change_column_name,column_attribute_list,index_list)
            
            if schema_status ==0:

                #get the different column list
                column_lst,change_column_lst,target_column_lst,ignore_column_lst = self.get_column_list(column_name_list,change_column_name,column_attribute_list)
                

                #get the dataset table details
                dataset_df = DBObject.get_dataset_detail(DBObject,connection,dataset_id)

                #get the 0 index  key as 'user_name' from the dataframe
                user_name,dataset_name = str(dataset_df['user_name'][0]),str(dataset_df['dataset_name'][0])
                

                #get te timeline status if successfully inserted return 0 else return 1
                timeline_status = self.update_timeline(project_id,dataset_id,user_name,dataset_name,column_lst,change_column_lst,target_column_lst,ignore_column_lst)

                
            logging.info("data preprocess : SchemaClass : save_schema : execution stop")
            return schema_status

        except (SchemaUpdateFailed,TableCreationFailed,SameColumnNameFound,InvalidColumnNames,ChangeColumnNameSame,IgnoreColumns,TargetAttributeException,TargetAttributeExistException) as exc:
            logging.error("data preprocess : ingestclass : save_schema : Exception " + str(exc.msg))
            logging.error("data preprocess : ingestclass : save_schema : " +traceback.format_exc())
            return exc.msg

    def update_timeline(self,project_id,dataset_id,user_name,dataset_name,column_lst,change_column_lst,target_column_lst,ignore_column_lst):
        """
        function used to insert record all the changes done in schema mapping into activity timeline table that performed by user.
        1)For the column been selected and target , 
        2)For the column been ignore
        3)For the column name updated

        Args:
                project_id[(Integer)]:[Id of the project]
                dataset_id[(Integer)]:[Id of the dataset]
                user_name[(String)]:[Name of the user]
                dataset_name[(String)]:[Updated dataset name uploaded  by user]
                column_lst[(List)]  : [Existing table column name value]
                change_column_lst[(List)] : [Change column name values]
                target_column_lst [(List)]  : [name of type attribute(select,ignore,target)]
        Return :
                [(Boolean)] : [return True if successfully updated record else return False]
        """
        try:
            logging.info("data preprocess : SchemaClass : update_timeline : execution start")
            activity_id = [] #empty list
            
            #check length of  change_column_lst if true append 5 as ID
            if len(change_column_lst)!=0:
                activity_id.append(5)

            #check length of  target_column_lst if true append 6 as ID
            if len(target_column_lst)!=0:
                activity_id.append(6)

            #check length of  target_column_lst if true append 7 as ID
            if len(ignore_column_lst)!=0:
                activity_id.append(7)
            
            status = 0 
            for id in activity_id:
                
                #get the activity dataframe based on id
                activity_df = timeline_Obj.get_activity(id,"US")

                #extract the activity description from dataframe
                activity_description = "{x}".format(x=activity_df[0]["activity_description"])

                activity=""

                if id==5:
                    column_string = " "
                    column_string = activity_description+" <br/>"
                    for count in range(len(change_column_lst)):
                        column_string += str(column_lst[count])+" <-> "+str(change_column_lst[count])+"<br/> "
                    activity = column_string

                elif id==6:
                    column_target=",".join(target_column_lst)
                    activity = activity_description.replace('*',column_target).replace('$',dataset_name)+","

                elif id==7:
                    column_ignore=",".join(ignore_column_lst)
                    activity = activity_description.replace('*',column_ignore)+","
                
                # length will minus from the string to avoid comma(,)
                activity_description = activity[0:len(activity)-1]

                #insert data into activity table
                status = timeline_Obj.insert_user_activity(id,user_name,project_id,dataset_id,activity_description)
                
                #return 1 if insertion failed 
                if status==False:
                    return 1
            logging.info("data preprocess : SchemaClass : update_timeline : execution stop")
            return status
        except Exception as exc:
            logging.error("data preprocess : SchemaClass : update_timeline : Exception " + str(exc))
            logging.error("data preprocess : SchemaClass : update_timeline : " +traceback.format_exc())
            return str(exc)
    
    def get_column_list(self,column_name_list,change_column_name,column_attribute_list):
        """
        function used to find the below column values :
        1)actual column name
        1)changed column name
        2)target attribute  column name
        3)ignore attribute  column name

        Args :
                column_name_list[(List)]  : [Existing table column name value]
                change_column_name[(List)] : [Change column name values]
                column_attribute_list [(List)]  : [name of type attribute(select,ignore,target)]
        Return :
                column_lst[(List)] :[return the column name ]
                change_column_lst[(List)]  : [return column change value ]
                target_column_lst[(List)] : [return the target attribute column name]
                ignore_column_lst[(List)] : [return the ignore attribute column name]
        """
        try:
            logging.info("data preprocess : SchemaClass : get_column_list : execution start")
            column_lst =[] #get the actual column name
            change_column_lst = [] #get the change column name
            target_column_lst = [] #get the target column value
            ignore_column_lst = [] #get the ignore column value
            #get the change column list and column list
            for count in range(len(column_name_list)):

                target_flag=0

                if (column_name_list[count] != change_column_name[count]) and (change_column_name[count] != ''): 
                    column_lst.append(column_name_list[count])
                    change_column_lst.append(change_column_name[count])
                    if column_attribute_list[count] =='Target':
                        target_column_lst.append(change_column_name[count])
                        target_flag=1

                elif column_attribute_list[count] =='Target' and target_flag==0:
                    target_column_lst.append(column_name_list[count])

                elif column_attribute_list[count] =='Ignore':
                    ignore_column_lst.append(column_name_list[count])
            
            logging.info("data preprocess : SchemaClass : get_column_list : execution stop")
            return column_lst,change_column_lst,target_column_lst,ignore_column_lst
        except Exception as exc:
            logging.error("data preprocess : SchemaClass : get_column_list : Exception " + str(exc))
            logging.error("data preprocess : SchemaClass : get_column_list : " +traceback.format_exc())
            return str(exc)

    def update_dataset_schema(self,DBObject,connection,schema_id,column_name_list,column_datatype_list,change_column_name=None,column_attribute_list=None,index_list=None,missing_flag=None,noise_flag=None,flag = False): ###
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
                if status == True and flag == False :
                    new_cols_lst = change_column_name
                    cols_attribute_lst = column_attribute_list
                   
                    for index,new_col,col_attr in zip(index_list,new_cols_lst,cols_attribute_lst): 

                        #sql command for updating change_column_name and column_attribute column  based on index column value
                        sql_command = "update "+ schema_table_name + " SET changed_column_name = '" + str(new_col) + "',"\
                                                                    "column_attribute = '" +str(col_attr) +"'"\
                                    " Where index ='"+str(index)+"' "
                        
                        logging.info(str(sql_command) + " sql")
                        #execute sql query command
                        status = DBObject.update_records(connection,sql_command) 

                        if status ==1:
                            raise SchemaUpdateFailed(500)
                else:
                    prev_dtype_lst = column_datatype_list
                    prev_cols_lst = column_name_list
                    new_cols_lst = ''
                    cols_attribute_lst = 'Select'
                    for prev_col,new_dtype,missing_value,noise_value in zip(prev_cols_lst,prev_dtype_lst,missing_flag,noise_flag): 

                        row = schema_id,prev_col,new_cols_lst,new_dtype,cols_attribute_lst,str(missing_value),str(noise_value)

                        # Make record for project table
                        row_tuples = [tuple(row)] 
                        
                        #insert the records into schema table
                        status,_ = DBObject.insert_records(connection,schema_table_name,row_tuples,cols) 
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
            logging.info(str(sql_command) + " check error" )
            #execute the query string,if record exist return dataframe else None
            data=DBObject.select_records(connection,sql_command) 

            logging.info(str(len(data)) + " check error" )
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
            sql_command = "select case when changed_column_name ='' then column_name else changed_column_name end column_list,index,data_type,column_attribute  from "+str(table_name)+" where schema_id="+str(schema_id)+" order by index"           
        
            #execute sql commnad if data exist then return dataframe else return None
            schema_df = DBObject.select_records(connection,sql_command) 
            
            if schema_df is None or len(schema_df) == 0:
                raise SchemaDataNotFound(500)

            #store all the schema table data into 
            index,column_name,data_type,column_attribute = schema_df['index'],schema_df['column_list'],schema_df['data_type'],schema_df['column_attribute']
            
            #get the appropriate structure format  
            schema_data=json_obj.get_schema_format(index,column_name,data_type,column_attribute)
            
            logging.info("data preprocess : SchemaClass : get_schema_data : execution stop")
            return schema_data

        except (SchemaDataNotFound) as exc:
            logging.error("data preprocess : SchemaClass : get_schema_data : Exception " + str(exc.msg))
            logging.error("data preprocess : SchemaClass : get_schema_data : " +traceback.format_exc())
            return exc.msg
    
    def get_count_value(self,DBObject,connection,schema_id):
        """
        function used to get the count values from the schema table of column name and "Ignore" attribute type

        Args:
            schema_id[(Integer)] : [Id of the schema table]

        Return:
            [Integer,Integer] : [return the count value of column name,return the count value of Ignore type in column attribute ]
        """
        try:
            #get the table name and columns,and schema of the table
            schema_table_name,_,_ = self.get_schema()

            #get the total column count and Ignore count for the perticular schema id
            sql_command = f'''select count(schema_id) as column_count,(select count(column_attribute) from {schema_table_name} where schema_id ={schema_id} and column_attribute ='Ignore') as ignore_count from {schema_table_name} where schema_id ={str(schema_id)}'''
            logging.info(str(sql_command) + "  select command")
            #Execute the sql command
            dataframe = DBObject.select_records(connection,sql_command)

            #get the total count value where index column will not be considered
            column_count_value,ignore_count_value = int(dataframe['column_count'][0])-1,int(dataframe['ignore_count'][0])

            return column_count_value,ignore_count_value
        except Exception as exc:
            return str(exc),None
    
    def get_target_attribute_index(self,DBObject,connection,schema_id):
        try:
            #get the table name and columns,and schema of the table
            schema_table_name,_,_ = self.get_schema()

            #get the total column count and Ignore count for the perticular schema id
            sql_command = f'''select index from {schema_table_name} where  schema_id ={schema_id} and column_attribute='Target' '''
            
            #Execute the sql command
            dataframe = DBObject.select_records(connection,sql_command)
            if len(dataframe['index'])==0:
                index_value = 0
            else:
                #get the total  index  value where column having target attribute
                index_value = int(dataframe['index'][0])

            return index_value
        except Exception as exc:
            return str(exc)
    
    def delete_schema_record(self,DBObject,connection,schema_id,col_name = None):
        """
        Function used to delete the record from  the schema table
        Args : 
                schema_id[(integer)] : [Id of the schema table]
                col_name[(String)] : [Name of the column]
        Return:
                [Integer] : [return 0 if successfully deleted else 1]
        """
        try:
            schema_table_name,_,_ = self.get_schema()
            if col_name is None:
                #this command will delete all records based on the schema_id
                sql_command = f'delete from {schema_table_name} where schema_id={str(schema_id)}'
            else:
                #this command will delete the record based on the schema_id and column_name if found
                sql_command = f"delete from {schema_table_name} where schema_id={str(schema_id)} and column_name ='{col_name}'"
            
            #Execute the sql command
            status = DBObject.update_records(connection,sql_command)
            return status
        except Exception as exc:
            return str(exc)
    





    
        