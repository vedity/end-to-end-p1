'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         17-Jan-2021           1.0           Created Class
 
*/
'''

from common.utils.exception_handler.python_exception.common.common_exception import EntryNotFound
from preprocess.utils.Exploration.dataset_exploration import ExploreClass
from .Exploration import dataset_exploration as de
from .schema import schema_creation as sc
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl


import logging
import traceback

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('preprocessing')


class PreprocessingClass(sc.SchemaClass,de.ExploreClass):
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
        logging.info("data preprocessing : PreprocessingClass : get_db_connection : execution start")
        DBObject = db.DBClass() # Get database object from database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port) # Initialize connection with database and get connection string , connection object.
        
        logging.info("data preprocessing : PreprocessingClass : get_db_connection : execution end")
        return DBObject,connection,connection_string
    
    def get_exploration_data(self,dataset_id,schema_id):
        """
            This class returns all the statistics for the given dataset.
            
            Args:
                dataset_id ([intiger]): [id of the dataset.]
            
            Returns:
                stats_df ([pandas.Dataframe]): [Dataframe containing all the statistics.]
        """
        try:
            logging.info("data preprocessing : PreprocessingClass : get_exploration_data : execution start")
            
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            stats_df = super(PreprocessingClass,self).get_dataset_statistics(DBObject,connection,dataset_id,schema_id)
            if isinstance(stats_df, int):
                if stats_df == 1:
                    return EntryNotFound(500)
                elif stats_df == 2:
                    return StatisticsError(500)
            
        except (Exception,EntryNotFound,StatisticsError) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_exploration_data : Exception " + str(exc))
            logging.error("data preprocessing : PreprocessingClass : get_exploration_data : " +traceback.format_exc())
            return str(exc)
            
        logging.info("data preprocessing : PreprocessingClass : get_exploration_data : execution end")
        return stats_df
    
    def save_schema_data(self,schema_data,project_id,dataset_id,schema_id):
        try:
            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")

            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            status = super(PreprocessingClass,self).save_schema(DBObject,connection,schema_data,project_id,dataset_id,schema_id)

            logging.info("data preprocessing : PreprocessingClass : save_schema_data : execution start")
            return status
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : save_schema_data : " +traceback.format_exc())
            return exc.msg

    def get_schema_details(self,schema_id):
        try:
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution start")
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)

            status = super(PreprocessingClass,self).get_schema_data(DBObject,connection,schema_id)
            
            logging.info("data preprocessing : PreprocessingClass : get_schema_details : execution stop")
            return status
        except (DatabaseConnectionFailed) as exc:
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : Exception " + str(exc.msg))
            logging.error("data preprocessing : PreprocessingClass : get_schema_details : " +traceback.format_exc())
            return exc.msg
    
    





