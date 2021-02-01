from common.utils.exception_handler.python_exception.common.common_exception import EntryNotFound
from preprocess.utils.Visualization.data_visualization import VisualizationClass
from .Visualization import data_visualization as dv
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

logger = logging.getLogger('visualization')


class VisualClass(dv.VisualizationClass):
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

    def get_visualization(self):
            DBObject,connection,connection_string = self.get_db_connection()
            if connection == None :
                raise DatabaseConnectionFailed(500)  
            
            stats_df = super(VisualClass,self).get_data_visualization(DBObject,connection)
            return stats_df