import pandas as pd 
import logging
import json
from datetime import * 
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
# DBObject = db.DBClass() # create object for database class
# connection,connection_string = DBObject.database_connection(database,user,password,host,port)


class ActivityTimelineClass:

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
        # table name
        table_name = 'mlaas.activity_tbl'
        # Columns for activity table
        cols = 'user_name,project_id,dataset_id,activity_name,activity_description,timestamp,operation' 
        # Schema for activity table.
        schema ="user_name text,"\
                "project_id bigint,"\
                "dataset_id bigint,"\
                "activity_name  text,"\
                "activity_description  text,"\
                "timestamp  timestamp,"\
                "operation  text"
                
        return table_name,cols,schema
    
    def insert_user_activity(self,user_name,project_id,dataset_id,activity_name,activity_description,timestamp,operation):
        """
        this function used to insert the record into activity table

        Args:
            user_name[(string)] :[Name of user]
            project_id[(Integer)] :[Id of the project]
            dataset_id[(Integer)] :[Id of the dataset]
            activity_name[(String)] :[Name of activity(create,delete)]
            activity_description[(String)] :[description of the activity perform]
            timestamp[(timestamp)] :[timestamp of user activity perform]
            operation[(String)] : [Name of the operation(create,delete)]
        Return : 
            [Boolean]:[return True if successfully inserted else return False]

        """
        DBObject = db.DBClass() # create object for database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        table_name,cols,schema = self.get_schema()
        create_status = self.is_existing_schema(DBObject,connection,table_name,schema) #check if the table is created or not
        if create_status ==True:
            rows = user_name,project_id,dataset_id,activity_name,activity_description,timestamp,operation
            row_tuples = [tuple(rows)] # form the tuple of sql values to be inserted
            status = DBObject.insert_records(connection,table_name,row_tuples,cols) #insert the record and return 1 if inserted else return 1
            if status ==1:
                return False
        return True
    
    def get_user_activity(self,user_name):
        """
        this function used to get the records from activity table  for the specific users
        Args:
            user_id[(String)] : [Id of the user]
        Return:
            [List]: [List of activity data]
        """
        try:
            DBObject = db.DBClass() # create object for database class
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)

            sql_command = ("SELECT user_name,activity_name,activity_description,date(timestamp),timestamp,operation from mlaas.activity_tbl where user_name='"+str(user_name)+"' order by timestamp desc")
            activity_df = DBObject.select_records(connection,sql_command) #excute the sql query 

            if activity_df is None:
                raise DataNotFound(500)

            length_df = activity_df['user_name']            
            if len(length_df)==0:
                raise DataNotFound(500)

            activity_df = activity_df.to_json(orient='records',date_format='iso',force_ascii=True) # convert into json string 
            activity_df = json.loads(activity_df) #convert into dict format
            
            return activity_df
        except (DataNotFound) as exc:
            return exc.msg

    def is_existing_schema(self,DBObject,connection,table_name,schema):
        """
        this function checks activity table created or not,If not then it will create the table

        Args : 
                table_name[(String)] : [Name of the table]
                Schema[(String)] : [structure of activity table]
        Return :
                [Boolean] : [return True if exists or created else False]
        """ 
        status = DBObject.is_existing_table(connection,table_name,'mlaas') #check if the table is exist or not
        if status == 'False': #if status false then create table 
            create_status = DBObject.create_table(connection,table_name,schema)
            return True
        elif status == 'True':
            return True
        return False

    def get_activity(self,id,language):
        '''This function is used to fetch the activity from master activity table.
            Args : 
                id[(Integer)] : [id of the activity]
                language[(String)] : [Language of activity shown]
            Return :
                [Dataframe] : [return activity_name,activity_description,operation]

        '''
        try:
            DBObject = db.DBClass() 
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)

            sql_command = ("SELECT activity_name,activity_description,operation from mlaas.activity_master_tbl where id='"+str(id)+"' and language='"+str(language)+"'")
            activity_df = DBObject.select_records(connection,sql_command) #excute the sql query 

            if activity_df is None:
                raise DataNotFound(500)

            activity_df = activity_df.to_json(orient='records',date_format='iso',force_ascii=True) # convert into json string 

            activity_df = json.loads(activity_df) #convert into dict format
            
            return activity_df
        except (DataNotFound) as exc:
            return exc.msg


