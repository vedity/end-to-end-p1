'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version. 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule. 
 Jay Shukla               01-Jay-2021           1.2           Added Deletion Functionality
 Vipul Prajapati          04-JAN-2021           1.3           File Check Mechanism Added.
 Vipul Prajapati          05-JAN-2021           1.4           no_of_rows field added into dataset tbl.
 Abhishek Negi            11-JAN-2021           1.5           Added Save file mechanism
*/
'''
import pandas as pd 
import json
import re
import logging
import traceback
import datetime
from common.utils.database import db
from .project.project_creation import *
from .dataset import dataset_creation as dt
from .project import project_creation as pj
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.logger_handler import custom_logger as cl
from django.core.files.storage import FileSystemStorage

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('ingestion')



class IngestClass(pj.ProjectClass,dt.DatasetClass):

    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.],
            user ([string]): [user of the database.],
            password ([string]): [password of the database.],
            host ([string]): [host ip or name where database is running.],
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number

    def get_db_connection(self):
        """This function is used to initialize database connection.
        
        Returns:
            [object,string]: [it will return database object as well as connection string.]
        """
        logging.info("data ingestion : ingestclass : get_db_connection : execution start")
        DBObject = db.DBClass() # Get database object from database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port) # Initialize connection with database and get connection string , connection object.
        
        logging.info("data ingestion : ingestclass : get_db_connection : execution end")
        return DBObject,connection,connection_string
    
    def create_project(self,project_name,project_desc,dataset_name = None,dataset_visibility = None,file_name = None,dataset_id = None,user_name = None):
        """This function is used to create project.
           E.g. sales forecast , travel time predictions etc.
           
        Args:
            project_name ([string]): [name of the project],
            project_desc ([string]): [descriptions of the project],
            dataset_name ([string], optional): [name of the dataset]. Defaults to None.
            dataset_visibility ([string], optional): [visibility of the dataset]. Defaults to None.
            file_name ([string], optional): [name of the csv file]. Defaults to None.
            dataset_id ([integer], optional): [dataset id of the selected dataset name]. Defaults to None.
            user_name ([string], optional): [name of the user]. Defaults to None.

        Returns:
            [integer]: [status of the project creation. if successfully then 0 else 1.]
        """
        logging.info("data ingestion : ingestclass : create_project : execution start")
        try:
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            
            project_status,project_id,load_dataset_id = super(IngestClass,self).make_project(DBObject,connection,project_name,project_desc,dataset_name,dataset_visibility,file_name ,dataset_id,user_name)
            logging.debug("data ingestion : ingestclass : create_project : we get status of project : "+str(project_status)+ " and Project id : "+str(project_id)+" and dataset_id : "+str(dataset_id))
            if project_status == 2:
                raise ProjectAlreadyExist(500)
                
            elif project_status == 1:
                raise ProjectCreationFailed(500) # If Failed.
                
            elif project_status == 0 and dataset_id == None:
                load_data_status,no_of_rows = super(IngestClass,self).load_dataset(DBObject,connection,connection_string,file_name,dataset_visibility,user_name)
                logging.debug("data ingestion : ingestclass : create_project : we get status of load_dataset : "+str(load_data_status)+ " and no of records in dataset : "+str(no_of_rows)+" and dataset_id : "+str(load_dataset_id))
                if load_data_status == 1:
                    raise LoadCSVDataFailed(500)
                else:
                    #v1.3
                    # update number of rows into dataset.
                    sql_command = "UPDATE mlaas.dataset_tbl SET no_of_rows="+str(no_of_rows)+" where dataset_id="+str(load_dataset_id)
                    update_status = DBObject.update_records(connection,sql_command)
                
                status = super(IngestClass,self).update_dataset_status(DBObject,connection,project_id,load_data_status)
                     
            elif project_status == 0:
                status = super(IngestClass,self).update_dataset_status(DBObject,connection,project_id)
                
                
        except (DatabaseConnectionFailed,ProjectAlreadyExist,LoadCSVDataFailed,ProjectCreationFailed,Exception) as exc:
            logging.error("data ingestion : ingestclass : create_project : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : create_project : " +traceback.format_exc())
            return exc.msg
        logging.info("data ingestion : ingestclass : create_project : execution end")
        return project_status

        
    def create_dataset(self,dataset_name,file_name,dataset_visibility,user_name):
        """This function is used to create dataset.
           E.g. sales , traveltime etc.
           
        Args:
            dataset_name ([string]): [name of the dataset.],
            file_name ([string]): [name of the name.],
            dataset_visibility ([string]): [visibility of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [status]: [status of the dataset creation. if successfully then 0 else 1.]
        """
        logging.info("data ingestion : ingestclass : create_dataset : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            dataset_status,dataset_id = super(IngestClass,self).make_dataset(DBObject,connection,dataset_name,file_name,dataset_visibility,user_name) # Get Status about dataset creation,if successfully then 0 else 1.
            
            if dataset_status == 2:
                raise DatasetAlreadyExist(500)
            
            elif dataset_status == 1 :
                raise DatasetCreationFailed(500)
            # Condition will check dataset successfully created or not. if successfully then 0 else 1.
            elif dataset_status == 0 :
                load_data_status,no_of_rows = super(IngestClass,self).load_dataset(DBObject,connection,connection_string,file_name,dataset_visibility,user_name)
                if load_data_status == 1:
                    raise LoadCSVDataFailed(500)
                else:
                    # update number of rows into dataset.
                    sql_command = "UPDATE mlaas.dataset_tbl set no_of_rows="+str(no_of_rows)+" where dataset_id="+str(dataset_id)
                    update_status = DBObject.update_records(connection,sql_command)

        except (DatabaseConnectionFailed,DatasetAlreadyExist,DatasetCreationFailed,LoadCSVDataFailed) as exc:
            logging.error("data ingestion : ingestclass : create_dataset : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : create_dataset : " +traceback.format_exc())
            return exc.msg
        
        logging.info("data ingestion : ingestclass : create_dataset : execution end")
        return dataset_status
        
    def show_dataset_details(self,user_name):
        """This function is used to show dataset details.

        Args:
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the dataset details.]
        """
        logging.info("data ingestion : ingestclass : show_dataset_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None :
                raise DatabaseConnectionFailed(500)
            
            dataset_df = super(IngestClass,self).show_dataset_details(DBObject,connection,user_name) # Get dataframe of dataset created.
            if dataset_df is None:
                raise DatasetDataNotFound(500)
            dataset_df = dataset_df.to_json(orient='records')
            dataset_df = json.loads(dataset_df)
            if len(dataset_df) == 0 :
                raise DatasetDataNotFound(500) 
                 
        except (DatabaseConnectionFailed,DatasetDataNotFound) as exc:
            logging.error("data ingestion : ingestclass : show_dataset_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : show_dataset_details : " +traceback.format_exc())
            return exc.msg
         
        logging.info("data ingestion : ingestclass : show_dataset_details : execution end")
        return dataset_df

    def show_data_details(self,dataset_id,start_index,length,sort_type,sort_index,global_value):
        """This function is used to show data details.
           It will show all the columns and rows from uploaded csv files.

        Args:
            table_name ([string]): [name of the  table.]

        Returns:
            [dataframe]: [it will return dataframe of the loaded csv's data.]
        """
        logging.info("data ingestion : ingestclass : show_data_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            
            if connection == None :
                raise DatabaseConnectionFailed(500) 
            
            data_details_df = super(IngestClass,self).show_data_details(DBObject,connection,dataset_id,start_index,length,sort_type,sort_index,global_value) # Get dataframe of loaded csv.
            if data_details_df is None :
                raise DataNotFound(500)
            data_details_df=data_details_df.to_json(orient='records')
            data_details_df = json.loads(data_details_df)
            if len(data_details_df) == 0 :
                raise DataNotFound(500)
            
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("data ingestion : ingestclass : show_data_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : show_data_details : " +traceback.format_exc())
            return exc.msg
        
        logging.info("data ingestion : ingestclass : show_data_details : execution end")
        return data_details_df

    def show_project_details(self,user_name):
        """This function is used to show project details.
        
        Args:
            user_name ([string]): [name of the user]

        Returns:
            [dataframe]: [dataframe of project details data]
        """
        logging.info("data ingestion : ingestclass : show_project_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            project_df = super(IngestClass,self).show_project_details(DBObject,connection,user_name) # Get dataframe of project created.
            if project_df is None:
                raise ProjectDataNotFound(500)
            project_df = project_df.to_json(orient='records')
            project_df = json.loads(project_df)
            
            if len(project_df) == 0:
                raise ProjectDataNotFound(500)
            
        except (DatabaseConnectionFailed,ProjectDataNotFound) as exc:
            logging.error("data ingestion : ingestclass : show_data_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : show_data_details : " +traceback.format_exc())
            return exc.msg
        
        logging.info("data ingestion : ingestclass : show_project_details : execution end")
        return project_df
    
    def delete_project_details(self, project_id, user_name):
        '''
        This function is used to delete an entry in the project_tbl
        
        Args:
            project_id ([integer]): [id of the entry which you want to delete.],
            user_name ([string]): [Name of the user.]
            
        Returns:
            status ([boolean]): [status of the project deletion. if successfully then 0 else 1.]
        '''
        logging.info("data ingestion : ingestclass : delete_project_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            deletion_status = super(IngestClass, self).delete_project_details(DBObject,connection,project_id,user_name)
            if deletion_status == 1:
                raise ProjectDeletionFailed(500)
            elif deletion_status == 2:
                raise UserAuthenticationFailed(500)
            elif deletion_status == 3:
                raise EntryNotFound(500)
            
            logging.info("data ingestion : ingestclass : delete_project_details : execution end")
            return deletion_status
        
        except (DatabaseConnectionFailed,ProjectDeletionFailed,UserAuthenticationFailed,EntryNotFound) as exc:
            logging.error("data ingestion : ingestclass : delete_project_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : delete_project_details : " +traceback.format_exc())
            return exc.msg
        
    def delete_dataset_detail(self, dataset_id, user_name):
        '''
        This function is used to delete an entry in the project_tbl
        
        Args:
            dataset_id ([integer]): [id of the dataset entry which you want to delete.],
            user_name ([string]): [Name of the user.]
            
        Returns:
            status ([boolean]): [status of the project deletion. if successfully then 0 else 1.]
        '''
        logging.info("data ingestion : ingestclass : delete_dataset_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            deletion_status = super(IngestClass, self).delete_dataset_details(DBObject,connection,dataset_id,user_name)
            if deletion_status == 1:
                raise DatasetDeletionFailed(500)
            elif deletion_status == 2:
                raise DataDeletionFailed(500)
            elif deletion_status == 3:
                raise DatasetInUse(500)
            elif deletion_status == 4:
                raise UserAuthenticationFailed(500)
            elif deletion_status == 5:
                raise EntryNotFound(500)
            logging.info("data ingestion : ingestclass : delete_dataset_details : execution end")
            return deletion_status
        
        except (DatabaseConnectionFailed,DatasetDeletionFailed,DataDeletionFailed,UserAuthenticationFailed,DatasetInUse,EntryNotFound) as exc:
            logging.error("data ingestion : ingestclass : delete_dataset_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : delete_dataset_details : " +traceback.format_exc())
            return exc.msg
        
    def delete_data_detail(self,table_name,user_name):
        """
        This function is used to delete the whole table which was created from 
        user input file.
        
        Args:
            table_name ([string]): [Name of the table that you want to delete.],
            user_name ([string]): [Name of the user.]

        Returns:
            [integer]: [it will return status of the dataset deletion. if successfully then 0 else 1.]
        """
        logging.info("data ingestion : ingestclass : delete_data_details : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            deletion_status = super(IngestClass, self).delete_data_details(DBObject,connection,table_name,user_name)
            if deletion_status == 1:
                raise DataDeletionFailed(500)
            
            logging.info("data ingestion : ingestclass : delete_data_details : execution end")
            return deletion_status
        
        except (DatabaseConnectionFailed,DataDeletionFailed) as exc:
            logging.error("data ingestion : ingestclass : delete_data_details : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : delete_data_details : " +traceback.format_exc())
            return exc.msg
        
    def show_dataset_names(self,user_name):
        """Show all the existing datasets created by user.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the selected columns from dataset details.]
        """
        logging.info("data ingestion : ingestclass : show_dataset_names : execution start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            dataset_df=super(IngestClass, self).show_dataset_names(DBObject,connection,user_name) 
            
            if dataset_df is None:
                raise DatasetDataNotFound(500)
            
            dataset_df = dataset_df.to_json(orient='records')
            dataset_df = json.loads(dataset_df)
            
            if len(dataset_df) == 0:
                raise DatasetDataNotFound(500)

            dataset_df=json.loads(dataset_df)
            
        except (DatabaseConnectionFailed,DatasetDataNotFound) as exc:
            logging.error("data ingestion : ingestclass : show_dataset_names : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : show_dataset_names : " +traceback.format_exc())
            return exc.msg
        logging.info("data ingestion : ingestclass : show_dataset_names : execution end")    
        return dataset_df
        

     
    def does_project_exists(self,project_name,user_name):
        """This function is used to check if same name project exist or not .

        Args:
            project_name ([string]): [name of the project.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean]: [it will return true or false. if exists true else false.]
        """
        logging.info("data ingestion : ingestclass : does_project_exists : execution start")    
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            table_name,schema,cols = super(IngestClass, self).make_project_schema() 
        
            exist_status = super(IngestClass, self).project_exists(DBObject,connection,table_name,project_name,user_name)
            
            if exist_status:
                raise ProjectAlreadyExist(500)
            
            logging.info("data ingestion : ingestclass : does_project_exists : execution end")    
            return exist_status
        
        except (DatabaseConnectionFailed,ProjectAlreadyExist) as exc:
            logging.error("data ingestion : ingestclass : does_project_exists : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : does_project_exists : " +traceback.format_exc())
            return exc.msg
        
    
    def does_dataset_exists(self,dataset_name,user_name):
        """This function is used to check existing dataset name.

        Args:
            dataset_name ([string]): [name of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean | integer]: [it will return False if no dataset with same name does not exists,
                                    or else it will return the id of the existing dataset]
        """
        logging.info("data ingestion : ingestclass : does_dataset_exists : execution start")    
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            table_name,schema,cols = super(IngestClass, self).make_dataset_schema()
        
            sql_command = f"SELECT DATASET_VISIBILITY FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND USER_NAME = '{user_name}'"
            visibility_df = DBObject.select_records(connection,sql_command) 
            if visibility_df is None:
                return False
            if len(visibility_df) == 0:
                return False
            
            dataset_visibility = str(visibility_df['dataset_visibility'][0])
            
            exist_status = super(IngestClass, self).dataset_exists(DBObject,connection,table_name,dataset_visibility,dataset_name,user_name)
        
            if exist_status != False:
                raise DatasetAlreadyExist(500)
            
            logging.info("data ingestion : ingestclass : does_dataset_exists : execution end")    
            return exist_status
        
        except (DatabaseConnectionFailed,DatasetAlreadyExist) as exc:
            logging.error("data ingestion : ingestclass : does_dataset_exists : Exception " + str(exc.msg))
            logging.error("data ingestion : ingestclass : does_dataset_exists : " +traceback.format_exc())
            return exc.msg
    #v1.2   
    def check_file(self,my_file,file_data = None):
        """This function is used to check file extension and file format.

        Args:
            my_file ([string]): [name of the file.]
            file_data ([blob]): [data of the file.]

        Returns:
            [bool]: [status of the file. if file is perfect then it will return True else False.]
        """
        try:
            logging.info("data ingestion : ingestclass : check_file : execution start")
            
            file_data_df = file_data
            original_file_name = str(my_file)
            ALL_SET = False
            
            if file_data_df is None:
                # it will check file extension.
                if str(my_file).lower().endswith(('.csv')):
                    check_file_name = original_file_name[:-4]
                    # it will check file name 
                    if(bool(re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$',check_file_name))==True):
                        ALL_SET = True
            else:       
                #* Below code is updated by Jay
                #? Solved a bug where the Function is only checking the file_name if the 
                #? - dataframe is None.
                
                #Todo: Below condition will need to be updated when we will be supporting more file formates
                if str(my_file).lower().endswith(('.csv')):
                    check_file_name = original_file_name[:-4]
                    # it will check file name 
                    if(bool(re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$',check_file_name))==True):
                        
                        #? File Name is valid so checking for column names.
                        # get column names.
                        logging.debug("data ingestion : ingestclass : check_file : rows =="+str(file_data_df.shape[0]) + " columns =="+ str(file_data_df.shape[1]))
                        if file_data_df.shape[0] > 0 and file_data_df.shape[1] >= 2:
                            All_SET_Count = 0
                            logging.debug("data ingestion : ingestclass : check_file : column list value =="+str(file_data_df.columns.to_list()))   
                            col_names = file_data_df.columns.to_list()
                            for col in col_names:
                                # it will check column names into the files.
                                if(bool(re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$',col))==True):
                                    
                                    All_SET_Count = All_SET_Count + 1
                                else:
                                    #All_SET_Count = All_SET_Count - 1  #Vipul
                                    #* Below 4 lines are added by Jay
                                    #? Once this loop executes, ALL_SET_Count will never match len(col_names)
                                    #? No need to run the loop forward if the All_SET_Count is never going to match
                                    #? - the len(col_names), breaking the loop right here will save time
                                    break
                                    
                            logging.debug("data ingestion : ingestclass : check_file : count value =="+str(All_SET_Count))        
                            if All_SET_Count == len(col_names):
                                ALL_SET = True
                            else: pass
                        else: pass
                    else: pass
                else: pass
                
                # logging.debug("data ingestion : ingestclass : check_file : rows =="+str(file_data_df.shape[0]) + " columns =="+ str(file_data_df.shape[1]))
                # if file_data_df.shape[0] > 0 and file_data_df.shape[1] >= 2:
                #     All_SET_Count = 0
                #     logging.debug("data ingestion : ingestclass : check_file : column list value =="+str(file_data_df.columns.to_list()))   
                #     col_names = file_data_df.columns.to_list()
                #     for col in col_names:
                #         # it will check column names into the files.
                #         if(bool(re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$',col))==True):
                            
                #             All_SET_Count = All_SET_Count + 1
                #         else:
                #             #All_SET_Count = All_SET_Count - 1
                #     logging.debug("data ingestion : ingestclass : check_file : count value =="+str(All_SET_Count))        
                #     if All_SET_Count == len(col_names):
                #         ALL_SET = True
                
            if ALL_SET == False:
                raise InvalidCsvFormat(500)             
            logging.debug("data ingestion : ingestclass : check_file : return value =="+str(ALL_SET))        
            logging.info("data ingestion : ingestclass : check_file : execution end")          
            return ALL_SET
        except InvalidCsvFormat as exc:
            return exc.msg
    
    def user_authentication(self,DBObject,connection,user_name,password):
        try:
            sql_command = "SELECT user_name from mlaas.user_auth_tbl where user_name='"+ str(user_name) +"' and password='"+ str(password) +"'"
            user_df = DBObject.select_records(connection,sql_command)
            if user_df is None:
                raise UserAuthenticationFailed(500)
            
            if len(user_df) > 0 :
                return True
            else:
                raise UserAuthenticationFailed(500)

        except UserAuthenticationFailed as exc:
            return exc.msg

   
    def save_file(self,user_name,dataset_visibility,file,file_path):
        """this function used to save the file uploaded by the user.file name will be append by the timestamp and 
        if the dataset_visibility is private save into user specific folder,else save into public folder. 

        Args:
                user_name[(String)]:[Name of the user]
                dataset_visibility[(String)]:[Name of Visibility public or private ]
                file_path[(string)] : [path string where we need to save file]
        return:
                [String]:[return name of the file]
        """
        logging.info("data ingestion : ingestclass : save_file : execution start")
        if dataset_visibility.lower()=='private':
            file_path += user_name
        else:
            file_path += dataset_visibility
        fs = FileSystemStorage(location=file_path)
        file_name = file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
        fs.save(file_name, file)
        logging.info("data ingestion : ingestclass : save_file : execution ")
        return file_name
            

