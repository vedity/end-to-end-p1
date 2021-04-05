
# Python library imports
import logging
import json
import traceback
import datetime 

# common utils file imports
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl
from common.utils.json_format.json_formater import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *


user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('activity_timeline')



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
        table_name = 'mlaas.activity_detail_tbl'
        # Columns for activity table
        cols = 'activity_id,user_name,project_id,dataset_id,activity_description,end_time,column_id,parameter' 
        # Schema for activity table.
        schema ="index bigserial,"\
                "activity_id bigint,"\
                "user_name text,"\
                "project_id bigint,"\
                "dataset_id bigint,"\
                "activity_description  text,"\
                "start_time  timestamp NOT NULL DEFAULT NOW(),"\
                "end_time  timestamp DEFAULT NULL,"\
                "column_id  text DEFAULT NULL,"\
                "parameter text DEFAULT NULL"\

        return table_name,cols,schema
    
    def insert_user_activity(self,activity_id,user_name,project_id,dataset_id,activity_description,end_time=None,column_id =None,parameter = None):
        """
        this function used to insert the record into activity table

        Args:
            user_name[(string)] :[Name of user]
            project_id[(Integer)] :[Id of the project]
            dataset_id[(Integer)] :[Id of the dataset]
            activity_description[(String)] :[description of the activity perform]
            timestamp[(timestamp)] :[timestamp of user activity perform]
            
        Return : 
            [Boolean]:[return True if successfully inserted else return False]

        """
        try:
            logging.info("Common : ActivityTimelineClass : insert_user_activity : execution start")
            DBObject = db.DBClass() # create object for database class
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
            
            if connection == None :
                raise DatabaseConnectionFailed(500)

            #function get the table name ,columns and schema
            table_name,cols,schema = self.get_schema() 

            #check if the table is created or not
            create_status = self.is_existing_schema(DBObject,connection,table_name,schema) 

            if create_status ==True:
                rows = activity_id,user_name,project_id,dataset_id,activity_description,end_time,column_id,parameter

                #form the tuple of sql values to be inserted
                row_tuples = [tuple(rows)]
                
                #insert the record and return 1 if inserted else return 1
                status,index = DBObject.insert_records(connection,table_name,row_tuples,cols,column_name='index') 

                if status == 1:
                    raise ActivityInsertionFailed(500)

            else:
                raise ActivityTableNotFound(500)

            logging.info("Common : ActivityTimelineClass : insert_user_activity : execution stop")
            return status,index

        except (ActivityInsertionFailed,DatabaseConnectionFailed,ActivityTableNotFound) as exc:
            logging.error("Common : ActivityTimelineClass : get_user_activity : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : get_user_activity : " +traceback.format_exc())
            return exc.msg,None
    
    def get_user_activity(self,user_name):
        """
        this function used to get the records from activity table  for the specific users
        Args:
            user_id[(String)] : [Id of the user]
        Return:
            [List]: [List of activity data]
        """
        try:
            logging.info("Common : ActivityTimelineClass : get_user_activity : execution start")
            DBObject = db.DBClass() # create object for database class
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)

            table_name,_,_ = self.get_schema()

            if connection == None :
                raise DatabaseConnectionFailed(500)

            #command to get the all activity based on the user_name 
            sql_command = ("SELECT at.user_name,amt.activity_name,at.activity_description,date(at.start_time),at.start_time,amt.operation from "+str(table_name)+" at, mlaas.activity_master_tbl amt where at.user_name='"+str(user_name)+"' and at.activity_id=amt.activity_id and amt.code in (-1,0) order by at.start_time desc")
            logging.info(str(sql_command)+ " sql command")

            #excute the sql query
            activity_df = DBObject.select_records(connection,sql_command)  
            if activity_df is None:
                raise DataNotFound(500)
            length_df = activity_df['user_name']            
            if len(length_df)==0:
                raise DataNotFound(500)

            # convert into json string
            activity_df = activity_df.to_json(orient='records',date_format='iso',force_ascii=True)  

            #convert into dict format
            activity_df = json.loads(activity_df) 

            logging.info("Common : ActivityTimelineClass : get_user_activity : execution stop")
            return activity_df

        except (DataNotFound,DatabaseConnectionFailed) as exc:
            logging.error("Common : ActivityTimelineClass : get_user_activity : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : get_user_activity : " +traceback.format_exc())
            return exc.msg

    def is_existing_schema(self,DBObject,connection,table_name,schema):
        """
        this function checks activity table created or not,If not then it will create the table

        Args : 
                table_name[(String)] : [Name of the table]
                Schema[(String)] : [structure of activity table]
        Return :
                [Boolean] : [return True if exists or created else False if any error occurred]
        """ 
        try :
            logging.info("Common : ActivityTimelineClass : is_existing_schema : execution start")
            Flag = False

            #check if the table is exist or not
            status = DBObject.is_existing_table(connection,table_name,'mlaas') 
            
            # check if status false then create table 
            if status == 'False':
                create_status = DBObject.create_table(connection,table_name,schema)                
                Flag =  True

            #if status is True then table is already exist
            elif status == 'True':
                Flag =  True

            logging.info("Common : ActivityTimelineClass : is_existing_schema : execution stop")
            return Flag

        except (TableCreationFailed) as exc:
            logging.error("Common : ActivityTimelineClass : is_existing_schema : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : is_existing_schema : " +traceback.format_exc())
            return exc.msg


    def get_activity(self,id,language,code=0):
        '''This function is used to fetch the activity from master activity table.

            Args : 
                id[(Integer)] : [id of the activity]
                language[(String)] : [Language of activity shown]
            Return :
                [Dataframe] : [return activity_name,activity_description,operation]

        '''
        try:
            logging.info("Common : ActivityTimelineClass : get_activity : execution start")
            DBObject = db.DBClass() 

            #get the connection stablish to postgressql  
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
            
            if connection == None :
                raise DatabaseConnectionFailed(500)

            #command to get the activity master table details based on activity id and language and code
            sql_command = ("SELECT activity_name,activity_description,operation from mlaas.activity_master_tbl where activity_id='"+str(id)+"' and language='"+str(language)+"' and code ='"+str(code)+"'")
            
            #excute the sql query
            activity_df = DBObject.select_records(connection,sql_command)  

            if activity_df is None:
                raise DataNotFound(500)

            # convert into json string 
            activity_df = activity_df.to_json(orient='records',date_format='iso',force_ascii=True) 

            #convert into dict format
            activity_df = json.loads(activity_df) 

            logging.info("Common : ActivityTimelineClass : get_activity : execution stop")
            return activity_df

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("Common : ActivityTimelineClass : get_activity : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : get_activity : " +traceback.format_exc())
            return exc.msg
    
    def update_activity(self,index,description):
        """
        function used to update the "end_time" and "activity description" of the  activity details table
        Args : 
                index[(Integer)] : [Id of the Activity detail table] 
                description[(string)] : [activity description value] 
        Return:
                [Integer] : [return 0 if successfully updated else return 1 if failed]
        """
        try:
            logging.info("Common : ActivityTimelineClass : update_activity : execution start")

            DBObject = db.DBClass() 
            #get the connection stablish to postgressql  
            connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
            
            if connection == None :
                raise DatabaseConnectionFailed(500)

            table_name,_,_ = self.get_schema()

            end_time  = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            #command will update the end_time based on the index id
            sql_command = "update "+str(table_name)+" set end_time='"+end_time+"',activity_description='"+description+"' where index='"+str(index)+"'"
            
            logging.info("--------->" + sql_command)

            #execute sql query command
            status = DBObject.update_records(connection,sql_command)

            if status == 1:
                raise ActivityUpdateFailed(500)

            logging.info("Common : ActivityTimelineClass : update_activity : execution stop")
            return status

        except (DatabaseConnectionFailed,ActivityUpdateFailed) as exc:
            logging.error("Common : ActivityTimelineClass : update_activity : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : update_activity : " +traceback.format_exc())
            return exc.msg


    def user_activity(self,activity_id,experiment_name,project_id,dataset_id,user_name,model_name=None):
        """
         this function is used to add activity description 
        Args : 
                activity_id[(Integer)] : [Id of the activity] 
                project_id[(Integer)] : [Id of the project] 
                dataset_id[(Integer)] : [Id of the dataset] 
                experiment_name[(string)] : [Name of experiment] 
                user_name[(string)] : [name of user]
                model_name[(string)] : [name of model]
        Return:
                [Integer] : [return 0 if successfully updated else return 1 if failed]
        """
        try:
            logging.info("Common : ActivityTimelineClass : update_activity : execution start")
            activity_df = self.get_activity(activity_id,"US")
            if activity_df is None:
                raise DatabaseConnectionFailed(500)
 
            if len(activity_df) == 0 :
                raise DataNotFound(500)
 
            if activity_id == 47 or activity_id == 48:
                activity_str= activity_df[0]["activity_description"]
                activity_description = activity_str.replace('*',experiment_name)
            elif activity_id == 44:
                activity_str= activity_df[0]["activity_description"]
                activity_description = activity_str.replace('#',experiment_name)
                activity_description = activity_description.replace('*',model_name)
                # activity_description = activity_str.replace('#',experiment_name)
            else:
                activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
 
            end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            self.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 
                    
 
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("Common : ActivityTimelineClass : update_activity : Exception " + str(exc.msg))
            logging.error("Common : ActivityTimelineClass : update_activity : " +traceback.format_exc())
            return exc.msg