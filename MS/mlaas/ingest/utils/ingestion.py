'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/

*/
'''
import pandas as pd 
from common.utils.database import db
from .project.project_creation import *
from .dataset import dataset_creation as dt
from .project import project_creation as pj
from common.utils.exception_handler.python_exception import *
import logging
import json
logger = logging.getLogger('django')


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
        DBObject = db.DBClass() # Get database object from database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port) # Initialize connection with database and get connection string , connection object.
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
        logger.info(" Create Project Execution Start")
        try:
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            
            project_status,project_id = super(IngestClass,self).make_project(DBObject,connection,project_name,project_desc,dataset_name,dataset_visibility,file_name ,dataset_id,user_name)
            
            if project_status == 2:
                raise ProjectAlreadyExist(500)
                
            elif project_status == 1:
                raise ProjectCreationFailed(500) # If Failed.
                
            elif project_status == 0 and dataset_id == None:
                load_data_status = super(IngestClass,self).load_dataset(DBObject,connection,connection_string,file_name,dataset_visibility,user_name)
                if load_data_status == 1:
                    raise LoadCSVDataFailed(500)
                
                status = super(IngestClass,self).update_dataset_status(DBObject,connection,project_id,load_data_status)
                     
            elif project_status == 0:
                status = super(IngestClass,self).update_dataset_status(DBObject,connection,project_id)
                
                
        except (DatabaseConnectionFailed,ProjectAlreadyExist,LoadCSVDataFailed,ProjectCreationFailed) as exc:
            logger.error("Exception Occurred : "+ exc.msg)
            return exc.msg
        logger.info(" Create Project Execution End")
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
        logger.info(" Create Dataset Execution Start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            dataset_status,_ = super(IngestClass,self).make_dataset(DBObject,connection,dataset_name,file_name,dataset_visibility,user_name) # Get Status about dataset creation,if successfully then 0 else 1.
            
            if dataset_status == 2:
                raise DatasetAlreadyExist(500)
            
            elif dataset_status == 1 :
                raise DatasetCreationFailed(500)
            # Condition will check dataset successfully created or not. if successfully then 0 else 1.
            elif dataset_status == 0 :
                load_data_status = super(IngestClass,self).load_dataset(DBObject,connection,connection_string,file_name,dataset_visibility,user_name)
                if load_data_status == 1:
                    raise LoadCSVDataFailed(500)

        except (DatabaseConnectionFailed,DatasetAlreadyExist,DatasetCreationFailed,LoadCSVDataFailed) as exc:
            logger.error("Exception Occurred : "+ exc.msg)
            return exc.msg
        
        logger.info(" Create Dataset Execution End")
        return dataset_status
        
    def show_dataset_details(self,user_name):
        """This function is used to show dataset details.

        Args:
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the dataset details.]
        """
        logger.info(" Show Dataset Details Execution Start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None :
                raise DatabaseConnectionFailed(500)
            
            dataset_df = super(IngestClass,self).show_dataset_details(DBObject,connection,user_name) # Get dataframe of dataset created.
            if dataset_df is None:
                raise DatasetDataNotFound(500)
            dataset_df = dataset_df.to_json(orient='records')
            dataset_df = json.loads(dataset_df)
            if len(dataset_df) == 0:
                raise DatasetDataNotFound(500)

        except (DatabaseConnectionFailed,DatasetDataNotFound) as exc:
            logger.error("Exception Occurred : "+ exc.msg)
            return exc.msg
         
        logger.info(" Show Dataset Details Execution End")
        return dataset_df

    def show_data_details(self,table_name,user_name,dataset_visibility):
        """This function is used to show data details.
           It will show all the columns and rows from uploaded csv files.

        Args:
            table_name ([string]): [name of the  table.]

        Returns:
            [dataframe]: [it will return dataframe of the loaded csv's data.]
        """
        logger.info(" Show Data Details Execution Start")
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            
            if dataset_visibility.lower() == 'public':
                user_name = 'public'
            
            if connection == None :
                raise DatabaseConnectionFailed(500) 
            
            data_details_df = super(IngestClass,self).show_data_details(DBObject,connection,table_name,user_name) # Get dataframe of loaded csv.
            if data_details_df is None :
                raise DataNotFound(500)
            data_details_df=data_details_df.to_json(orient='records')
            if len(data_details_df) <= 2 :
                raise DataNotFound(500)
            
            data_details_df=json.loads(data_details_df)  # convert datafreame into json
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logger.error("Exception Occurred : "+ exc.msg)
            return exc.msg
        
        logger.info(" Show Data Details Execution End")
        return data_details_df

    def show_project_details(self,user_name):
        """This function is used to show project details.
        
        Args:
            user_name ([string]): [name of the user]

        Returns:
            [dataframe]: [dataframe of project details data]
        """
        logger.info(" Show Project Details Execution Start")
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
            logger.error("Exception Occurred : "+ exc.msg)
            return exc.msg
        logger.info(" Show Project Details Execution End")
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
        
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            deletion_status = super(IngestClass, self).delete_project_details(DBObject,connection,project_id,user_name)
            if deletion_status == 1:
                raise ProjectDeletionFailed(500)
            elif deletion_status == 2:
                raise UserAuthenticationFailed(500)
            
            return deletion_status
        
        except (DatabaseConnectionFailed,ProjectDeletionFailed,UserAuthenticationFailed) as exc:
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
                raise DatasetEntryNotFound(500)
            
            return deletion_status
        
        except (DatabaseConnectionFailed,DatasetDeletionFailed,DataDeletionFailed,UserAuthenticationFailed,DatasetInUse,DatasetEntryNotFound) as exc:
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
        
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            deletion_status = super(IngestClass, self).delete_data_details(DBObject,connection,table_name,user_name)
            if deletion_status == 1:
                raise DataDeletionFailed(500)
            
            return deletion_status
        
        except (DatabaseConnectionFailed,DataDeletionFailed) as exc:
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
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            dataset_df=super(IngestClass, self).show_dataset_names(DBObject,connection,user_name) 
            
            if dataset_df is None:
                raise DatasetDataNotFound(500)
            
            dataset_df = dataset_df.to_json(orient='records')
            if len(dataset_df) <=2:
                raise DatasetDataNotFound(500)

            dataset_df=json.loads(dataset_df)
            
        except (DatabaseConnectionFailed,DatasetDataNotFound) as exc:
            return exc.msg
            
        return dataset_df
        

    #? Check if project with same name 
    def does_project_exists(self,project_name,user_name):
        """This function is used to check if same name project exist or not .

        Args:
            project_name ([string]): [name of the project.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean]: [it will return true or false. if exists true else false.]
        """
        
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            table_name,schema,cols = super(IngestClass, self).make_project_schema() 
        
            exist_status = super(IngestClass, self).project_exists(DBObject,connection,table_name,project_name,user_name)
            
            if exist_status:
                raise ProjectAlreadyExist(500)
            
            return exist_status
        
        except (DatabaseConnectionFailed,ProjectAlreadyExist) as exc:
            return exc.msg
        
    #? Check if project with same name 
    def does_dataset_exists(self,dataset_name,user_name):
        """This function is used to check existing dataset name.

        Args:
            dataset_name ([string]): [name of the dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean | integer]: [it will return False if no dataset with same name does not exists,
                                    or else it will return the id of the existing dataset]
        """
        
        try:
            DBObject,connection,connection_string = self.get_db_connection() # Get database object,connection object and connecting string.
            if connection == None:
                raise DatabaseConnectionFailed(500)
            
            table_name,schema,cols = super(IngestClass, self).make_dataset_schema()
        
            sql_command = f"SELECT DATASET_VISIBILITY FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND USER_NAME = '{user_name}'"
            visibility_df = DBObject.select_records(connection,sql_command) 
            
            if len(visibility_df) == 0:
                return False
            
            dataset_visibility = str(visibility_df['dataset_visibility'][0])
            
            exist_status = super(IngestClass, self).dataset_exists(DBObject,connection,table_name,dataset_visibility,dataset_name,user_name)
        
            if exist_status != False:
                raise DatasetAlreadyExist(500)
            
            return exist_status
        
        except (DatabaseConnectionFailed,DatasetAlreadyExist) as exc:
            return exc.msg
        
        
