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
        # Project table name
        table_name = 'mlaas.activity_tbl'
        # Columns for project table
        cols = 'user_id,project_id,dataset_id,activity_name,activity_description,date,timestamp,operation' 
        # Schema for project table.
        schema ="user_id bigint,"\
                "project_id bigint,"\
                "dataset_id bigint,"\
                "activity_name  text,"\
                "activity_description  text,"\
                "date  date,"\
                "timestamp  timestamp,"\
                "operation  text"
                
        return table_name,cols,schema
    
    def insert_user_activity(self,user_id,project_id,dataset_id,activity_name,activity_description,date,timestamp,operation):
        DBObject = db.DBClass() # create object for database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        table_name,cols,schema = self.get_schema()
        user_id =1
        project_id = 0
        dataset_id = 1
        activity_name = "Created Dataset"
        activity_description = "You have created dataset ABC"
        current_date = str(date.today())
        timestamp = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        operation = "Create"
        create_status = self.is_existing_schema(DBObject,connection,table_name,schema)
        if create_status ==True:
            rows = user_id,project_id,dataset_id,activity_name,activity_description,current_date,timestamp,operation
            row_tuples = [tuple(rows)]
            status = DBObject.insert_records(connection,table_name,row_tuples,cols)
            if status ==1:
                return "Not inserted"
        return "inserted"
    
    def get_user_activity(self):
        user_id=1
        DBObject = db.DBClass() # create object for database class
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)

        sql_command = ("SELECT user_id,activity_description,date,timestamp,operation from mlaas.activity_tbl where user_id='"+str(user_id)+"' order by timestamp")
        logger.info(sql_command)
        activity_df = DBObject.select_records(connection,sql_command)
        activity_df = activity_df.to_json(orient='records',date_format='iso')
        activity_df = json.loads(activity_df)
        return activity_df

    def is_existing_schema(self,DBObject,connection,table_name,schema):
            status = DBObject.is_existing_table(connection,table_name,'mlaas')
            if status == 'False': 
                create_status = DBObject.create_table(connection,table_name,schema)
                return True
            elif status == 'True':
                return True
            return False