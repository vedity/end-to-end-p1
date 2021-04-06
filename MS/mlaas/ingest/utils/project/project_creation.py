'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule
 Jay Shukla               14-DEC-2020           1.3           Added Atomicity in the case where dataset_tbl creation fails.
 Abishek Negi             18-Dec-2020           1.4           need to Check the code not working fine
 Abishek Negi             18-Dec-2020           1.4           Added original_dataset_id into the arguments 

*/
'''
# Python library import
import pandas as pd
import logging
import traceback
import time 

#Ingest util/dataset file import
from ..dataset import dataset_creation 

#Database variable import
from database import *

# Common file imports
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.logger_handler import custom_logger as cl
from common.utils.database import db

# Preprocess file imports
from preprocess.utils import preprocessing
from preprocess.utils.schema.schema_creation import *
from preprocess.utils.Transformation.split_data import Split_Data

#Manual modeling file imports
from modeling.utils.modeling_dag_utils.dag_common_utils import get_modeling_dag_name

# Object Initialization
preprocessObj =  preprocessing.PreprocessingClass(database,user,password,host,port) #initialize Preprocess class object
schema_obj=SchemaClass() #initialize Schema object from schema class
PREPROCESS_OBJ = Split_Data()
user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('project_creation')
DatasetObject = dataset_creation.DatasetClass()

class ProjectClass:

    def make_project_schema(self):
        """This function is used to make schema for creating project table.
           E.g. column_name  data_type.

        Returns:
            [string]: [it will return name of the table, structure of the table and columns of the table.]
        """
        logging.info("data ingestion : ProjectClass : make_project_schema : execution start")
        # Project table name
        table_name = 'mlaas.project_tbl'
        # Columns for project table
        cols = 'project_name,project_desc,user_name,original_dataset_id,dataset_id,cleanup_dag_id,model_dag_id' 
        # Schema for project table.
        schema ="project_id bigserial,"\
                "project_name  text,"\
                "project_desc  text,"\
                "dataset_status integer NOT NULL DEFAULT -1,"\
                "model_status integer NOT NULL DEFAULT -1,"\
                "deployment_status integer NOT NULL DEFAULT -1,"\
                "scale_split_flag integer NOT NULL DEFAULT 1,"\
                "user_name  text,"\
                "original_dataset_id  bigint,"\
                "dataset_id bigint,"\
                "schema_id bigserial,"\
                "cleanup_dag_id text,"\
                "model_dag_id text,"\
                "input_features text,"\
                "target_features text,"\
                "scaled_split_parameters text ,"\
                "problem_type text,"\
                "created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()" 
                
        logging.info("data ingestion : ProjectClass : make_project_schema : execution end")
        return table_name,schema,cols

    def make_project_records(self,project_name,project_desc,user_name,original_dataset_id,dataset_id):
        """This function is used to make records for inserting data into project table.
           E.g. column_name_1,column_name_2 .......,column_name_n.

        Args:
            project_name ([string]): [name of the project.],
            project_desc ([string]): [descriptions of the project.],
            user_name ([string]): [name of the user.],
            original_dataset_id ([integer]): [dataset id of the created dataset.]

        Returns:
            [tuple]: [it will return records in the form of tuple.]
        """
        logging.info("data ingestion : ProjectClass : make_project_records : execution start")
        
        #TODO : both dag are not run together
        cleanup_dag_id = preprocessObj.get_cleanup_dag_name()
        time.sleep(3)
        model_dag_id = get_modeling_dag_name()
        
        row = project_name,project_desc,user_name,original_dataset_id,dataset_id,cleanup_dag_id,model_dag_id
        row_tuples = [tuple(row)] # Make record for project table.
        logging.info("data ingestion : ProjectClass : make_project_records : execution end")
        return row_tuples
        

    def make_project(self,DBObject,connection,connection_string,project_name,project_desc,page_name,dataset_desc,dataset_name,user_visibility,file_name ,original_dataset_id,user_name):
        """This function is used to make project and it will create main project table and also
           load project details into database main project table.
           E.g. project name : sales forecast, travel time prediction etc.
           E.g. project details : project_name,project_desc,file_name,user_name,dataset_table_name.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_name ([string]): [name of the project.],
            project_desc ([string]): [descriptions of the project.],
            dataset_name ([string]): [name of the dataset.],
            user_visibility ([string]): [visibility of the dataset.],
            file_name ([string]): [name of the file.],
            original_dataset_id ([integer]): [dataset id of the selected dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [string,integer]: [it will return status of the project creation and 
            also return project id of the created project.]
        """
        try:
            logging.info("data ingestion : ProjectClass : make_project : execution start")

            # Get table name,schema and columns from dataset class.
            table_name,schema,cols = self.make_project_schema() 
            dataset_table_name,dataset_schema,datset_cols = DatasetObject.make_dataset_schema()

            if self.project_exists(DBObject,connection,table_name,project_name,user_name) : 
                raise ProjectAlreadyExist(500)
            
            

            if original_dataset_id == None:
                status,original_dataset_id  = DatasetObject.make_dataset(DBObject,connection,connection_string,dataset_name,file_name,user_visibility,user_name,dataset_desc,page_name)   
                
                if status != 0:
                    return status,None,None

            #Get the dataset details based on the original dataset id   
            data_df = DBObject.get_dataset_detail(DBObject,connection,original_dataset_id)
            
            #Extract the data from the dataframe variable " data_df "
            dataset_name,file_name,file_size,old_table_name,dataset_desc,dataset_visibility = str(data_df['dataset_name'][0]),str(data_df['file_name'][0]),str(data_df['file_size'][0]),str(data_df['dataset_table_name'][0]),str(data_df['dataset_desc'][0]),str(data_df['dataset_visibility'][0])
                
            # Get the updated table name for the variable dataset
            new_table_name = DBObject.get_table_name(connection,old_table_name)

            page_name = 'schema mapping'

            
            row=dataset_name,file_name,file_size,new_table_name,user_visibility,user_name,dataset_desc,page_name 
            row_tuples = [tuple(row)]

            #Insert the dataset record into table
            dataset_insert_status,dataset_id = DBObject.insert_records(connection,dataset_table_name,row_tuples,datset_cols,column_name='dataset_id')
                
            if dataset_insert_status == 0:
    
                #Create the variable table based on the  Raw dataset table.
                create_status = DatasetObject.create_variable_dataset(DBObject,connection,dataset_id,user_name,old_table_name,new_table_name,user_visibility,dataset_visibility)
                    
                if create_status != 0:
                    return create_status,None,None

            else:
                raise ProjectCreationFailed(500)
                    
            
            # Get row for project table.
            row_tuples = self.make_project_records(project_name,project_desc,user_name,original_dataset_id,dataset_id) 
            
                
                # Get status about inserting records into project table. if successful then 0 else 1. 
            insert_status,_ = DBObject.insert_records(connection,table_name,row_tuples,cols) 

                # This condition is used to check project table and data is successfully stored into project table or not.if successful then 0 else 1. 
            if insert_status == 0 :

                status = 0 # Successfully Created

                    #function will get the schema_id and project_id from the project table
                project_id,schema_id = self.get_project_id(DBObject,connection,row_tuples,user_name) 
                    
                    #get the schema mapping details with column name and datatype
                column_name_list,column_datatype_list = schema_obj.get_dataset_schema(DBObject,connection,dataset_id) 
                    
                missing_value_lst,noise_status_lst = preprocessObj.get_preprocess_cache(dataset_id)
                    
                missing_value_lst,noise_status_lst = list(missing_value_lst),list(noise_status_lst)
                    # column name and datatype will be inserted into schema table with schema id
                    
                status=schema_obj.update_dataset_schema(DBObject,connection,schema_id,column_name_list,column_datatype_list,missing_flag=missing_value_lst,noise_flag=noise_status_lst)
                    
            else:
                raise ProjectCreationFailed(500)
                
            
            return status,project_id,original_dataset_id
        except (ProjectCreationFailed,ProjectAlreadyExist) as exc:
            return exc.msg,None,None


    def get_project_id(self,DBObject,connection,row_tuples,user_name):
        """This function is used to get project id of created project.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            row_tuples ([list]): [list of tuple of record.],
            user_name ([string]): [name of the user.]

        Returns:
            [integer]: [it will return the project id of the created project.]
            [integer]: [it will return the schema id of the created project.]
        """
        
        logging.info("data ingestion : ProjectClass : get_project_id : execution start")
        table_name,*_ = self.make_project_schema()
        project_name,*_ = row_tuples[0]
        
        logging.debug("data ingestion : ProjectClass : get_project_id : this will excute select query on table name : "+table_name + " based on project name :"+project_name + " and user name :"+user_name)
        project_name=str(project_name).replace("'","''")
        sql_command = "SELECT project_id,schema_id from "+ table_name + " Where project_name ='"+ project_name + "' and user_name = '"+ user_name + "'"
        project_df = DBObject.select_records(connection,sql_command)
        project_id = int(project_df['project_id'][0])
        schema_id = int(project_df['schema_id'][0])
        logging.info("data ingestion : ProjectClass : get_project_id : execution end")
        return project_id,schema_id
    
    def update_dataset_status(self,DBObject,connection,project_id,load_data_status = 0):
        """This function is used to update dataset status field in project table.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_id ([integer]): [project id for update dataset status field in project.],
            load_data_status ([integer]): [description]

        Returns:
            [integer]: [it will return stauts of update dataset. if successfully then 1 else 0.]
        """
        
        try:
            logging.info("data ingestion : ProjectClass : update_dataset_status : execution start")
            table_name,*_ = self.make_project_schema()
            
            logging.debug("data ingestion : ProjectClass : update_dataset_status : this will excute update query on table name : "+table_name + " and set value of dataset_status : "+str(load_data_status) +" based on project id : "+str(project_id))
            try:
                sql_command = "UPDATE "+ table_name + " SET dataset_status=" + str(load_data_status) + " WHERE project_id="+ str(project_id)        
                status = DBObject.update_records(connection,sql_command)
                logging.info("data ingestion : ProjectClass : update_dataset_status : execution end")
                if status !=0:
                    raise ProjectColumnUpdateFailed

            except (ProjectColumnUpdateFailed) as  exc:
                return exc.msg

            return status
        except Exception as exc:
            return str(exc)
        
    
    def show_project_details(self,DBObject,connection,user_name):
        """This function is used to show details about all created projects.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the project details.]
        """
        try:

            logging.info("data ingestion : ProjectClass : show_project_details : execution start")
            table_name,*_ = self.make_project_schema() # Get table name,schema and columns from dataset class
            # This command is used to get project details from project table of database.
            
            logging.debug("data ingestion : ProjectClass : show_project_details : this will excute select query on table name : "+table_name +" based on user name : "+user_name)
            try:
                sql_command = "SELECT p.*,d.dataset_name FROM "+ table_name + " p,mlaas.dataset_tbl d WHERE p.USER_NAME ='"+ user_name +"' and p.dataset_id = d.dataset_id"
                
                project_df=DBObject.select_records(connection,sql_command) # Get project details in the form of dataframe.
                if len(project_df) == 0 or project_df is None:
                    raise ProjectDataNotFound(500)
                
                #? To check scale and split in all project 
                split_flags = []
                try:
                    for i in project_df['project_id']:
                        flag,desc = PREPROCESS_OBJ.check_split_exist(i)
                        split_flags.append(flag)
                    
                except Exception as e:
                    return e

                project_df['split_status'] = split_flags
            
            except (ProjectDataNotFound) as exc:
                return exc.msg
            logging.info("data ingestion : ProjectClass : show_project_details : execution end")
    
            return project_df

        except Exception as exc:
            return str(exc)

    #* Version 1.3
    def delete_project_details(self,DBObject,connection,project_id,user_name):
        """
        This function is used to delete the project entry from the project table.
        It also deletes the dataset if no other project is using it.
        
        Args: 
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_id ([number]): [id of the project_tbl entry that you want to delete.],
            user_name ([string]): [name of the user.]

        Returns:
            status ([boolean]): [status of the project deletion. if successfully then 0 else 1.]
        """
        logging.info("data ingestion : ProjectClass : delete_project_details : execution start")
        try:
            try:
                table_name,_,_ = self.make_project_schema()

                #? Fetching original user from the table
                sql_command = f"SELECT USER_NAME,PROJECT_NAME,original_dataset_id FROM {table_name} WHERE PROJECT_ID = '{project_id}'"
                user_name_df = DBObject.select_records(connection,sql_command) 
                if len(user_name_df) == 0:
                    logging.debug(f"data ingestion  :  ProjectClass  :  delete_project_details  :  Entry not found for the project_id = {project_id}")
                    raise EntryNotFound(500)
                
                user_name_from_table = user_name_df['user_name'][0]
                project_name = user_name_df['project_name'][0]
                original_dataset_id = user_name_df['original_dataset_id'][0]
                #? Authenticating the user    
                if user_name == user_name_from_table:

                    #? Deleting Project Table Entry
                    sql_command = "DELETE FROM "+ table_name + " WHERE PROJECT_ID ='"+ project_id +"'"
                    project_status = DBObject.delete_records(connection,sql_command)

                    if project_status == 0:
                        schema_id = project_id
                        project_status = schema_obj.delete_schema_record(DBObject,connection,schema_id)
                        if project_status !=0:
                            raise SchemaDeletionFailed(500)
                        
                else:
                    logging.debug(f"data ingestion  :  ProjectClass  :  delete_project_details  :  Function failed because the Given user = {user_name} is not authorized to delete the project.")
                    raise UserAuthenticationFailed(500)
                
                logging.info("data ingestion : ProjectClass : delete_project_details : execution end")
                return project_status,original_dataset_id,project_name
            except (EntryNotFound,SchemaDeletionFailed,UserAuthenticationFailed) as exc:
                return exc.msg,None,None
        except:
            return 1,None,None
        
    

    #? Check if project with same name 
    def project_exists(self,DBObject,connection,table_name,project_name,user_name):
        """This function is used to check if same name project exist or not .

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            table_name ([string]): [name of the table.],
            project_name ([string]): [name of the project.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean]: [it will return true or false. if exists true else false.]
        """
        
        logging.info("data ingestion : ProjectClass : project_exists : execution start")
        
        try:
            project_name=str(project_name).replace("'","''")
            #? Checking if Same project_name exists for the same user
            project_name=str(project_name).replace("'","''")
            sql_command = f"SELECT PROJECT_ID FROM {table_name} WHERE PROJECT_NAME = '{project_name}' AND USER_NAME = '{user_name}'"
           

            data=DBObject.select_records(connection,sql_command)
            data=len(data)

           
            logging.info("data ingestion : ProjectClass : project_exists : execution end")
            
            #! Same project_name exists for the same user, then return status True
            if data == 0: return False
            else: 
                logging.debug(f"data ingestion  :  ProjectClass  :  project_exists  :  Project with the same name({project_name}) exists for the user = {user_name}")
                return True
        except:
            return False

    
    
 
