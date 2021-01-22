'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
Abhishek Negi           11-JAN-2020           1.0       Initial Version

 ****************************************************************************************/

*/
'''
import json
import logging
import traceback
from database import *
from rest_framework.views import APIView
from rest_framework.response import Response
from ingest.utils import ingestion
from ingest.utils.ingestion import *
from .utils.exception_handler.python_exception.common.common_exception import *
from .utils.exception_handler.python_exception.ingest.ingest_exception import *
from .utils.logger_handler import custom_logger as cl
from .utils.exception_handler.python_exception import *
from .utils.json_format.json_formater import *
from .utils.activity_timeline import *
from .utils.activity_timeline import activity_timeline
from database import *

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('view')
DBObject=db.DBClass()     #Get DBClass object
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)
IngestionObj=ingestion.IngestClass(database,user,password,host,port)
timeline_Obj=activity_timeline.ActivityTimelineClass(database,user,password,host,port)
class UserLoginClass(APIView):
        
        def get(self,request,format=None):
                """ this class used to check the authorized user login data.

                Args   :
                        user_name[(String)] : [Name of user]
                        password [(String)] : [password value]
                Return :
                        status_code(500 or 200),
                        error_msg(Error message for login successfull & unsuccessfull),
                        Response(return false if failed otherwise true)
                """
                try:
                        logging.info("data ingestion : UserLoginClass : GET Method : execution start")
                        user_name = request.query_params.get('user_name')
                        password = request.query_params.get('password')
                        check_user_auth_tbl=DBObject.is_existing_table(connection,'user_auth_tbl','mlaas')
                        if check_user_auth_tbl == "False":
                                user_df=DBObject.read_data('common/user_registration_tbl.csv')
                                status=DBObject.load_csv_into_db(connection_string,'user_auth_tbl',user_df,'mlaas')        
                        check_menu_tbl=DBObject.is_existing_table(connection,'menu_tbl','mlaas')
                        if check_menu_tbl == "False":
                                menu_df=DBObject.read_data('common/Menu.csv')
                                status=DBObject.load_csv_into_db(connection_string,'menu_tbl',menu_df,'mlaas')           
                        user_status = IngestionObj.user_authentication(DBObject,connection,user_name,password)
                        if user_status != True:
                                status_code,error_msg=get_Status_code(user_status)
                                logging.info("data ingestion : UserLoginClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else: 
                                logging.info("data ingestion : UserLoginClass : POST Method : execution stop : status_code : 200")
                                return Response({"status_code":"200","error_msg":"Login Successfull","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : UserLoginClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : UserLoginClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
        
        def post(self,request):
                """ this function used to insert user data into table.

                Args   :
                        csv_file[(CSV)] : [CSV data of authorized user]
                Return :

                        Response(return 1 if failed otherwise 0)
                """
                try:
                        logging.info("data ingestion : UserLoginClass : POST Method : execution start")
                        user_df=DBObject.read_data('ingest/user_registration_tbl.csv') #read the data from csv file store into dataframe variable
                        status=DBObject.load_csv_into_db(connection_string,'user_auth_tbl',user_df,'mlaas') # this function will insert the csv data into  user_auth table
                        return Response({"Status":status})
                except Exception as e:
                        logging.error("data ingestion : UserLoginClass : POST Method : Exception :" + str(e))
                        logging.error("data ingestion : UserLoginClass : POST Method : " +traceback.format_exc())
                        return Response({"Exception":str(e)}) 

class MenuClass(APIView):
        def post(self, request, format=None):
                """
                this function used to insert  nevigation Menu detail into database. 
                Args:
                       [This function does not take any argument] 
                Return:
                        status_code(500 or 200),
                        error_msg(Error message for Insertion successfull or unsuccessfull),
                        Response(return false if failed otherwise true )  
                """
                try:
                        logging.info("data ingestion : MenuClass : POST Method : execution start")
                        menu_df=DBObject.read_data('common/Menu.csv')
                        status=DBObject.load_csv_into_db(connection_string,'menu_tbl',menu_df,'mlaas')
                        if status != 0:
                                logging.info("data ingestion : MenuClass : POST Method : execution stop : status_code :500")
                                return Response({"status_code":"500","error_msg":"Insertion Failed","response":"false"})
                        else:
                                logging.info("data ingestion : MenuClass : POST Method : execution stop : status_code : 200")
                                return Response({"status_code":"200","error_msg":"Insertion successfull","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : MenuClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : MenuClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":"Failed","response":str(e)}) 
        
        def get(self, request, format=None):
                """
                this function used to get Navigation menu data from the database and convert into appropriate json format.
                Args:
                       [This function does not take any argument] 
                Return:
                        status_code(500 or 200),
                        error_msg(Error message for retrive successfull or unsuccessfull),
                        Response(return error_msg if failed otherwise Json data )  
                """
                try:
                        logging.info("data ingestion : MenuClass : POST Method : execution start")
                        sql_command1='select id,modulename,menuname as "label",url as "link",parent_id as "parentId",icon from mlaas.menu_tbl where parent_id ='+"'null'"
                        dataset_df1=DBObject.select_records(connection,sql_command1) #call show_data_details and it will return dataset detail data in dataframe
                        dataset_json1=json.loads(dataset_df1.to_json(orient='records'))  # convert datafreame into json
                        sql_command2='select id,modulename,menuname as "label",url as "link",parent_id as "parentId",icon from mlaas.menu_tbl where parent_id !='+"'null'"
                        dataset_df2=DBObject.select_records(connection,sql_command2) #call show_data_details and it will return dataset detail data in dataframe
                        dataset_json2=json.loads(dataset_df2.to_json(orient='records'))  # convert datafreame into json
                        
                        json_data=menu_nested_format(dataset_json1,dataset_json2)   
                        return Response({"status_code":"200","error_msg":"Menu Data","response":json_data})
                except Exception as e:
                        logging.error("data ingestion : MenuClass : POST Method : Exception :" + str(e))
			logging.error("data ingestion : MenuClass : POST Method : "+ traceback.format_exc())
                        return Response({"status_code":"500","error_msg":"Failed","response":str(e)})

class ScheamDatatypeListClass(APIView):
        
        def get(self, request, format=None):
                """
                This class is used to get  Datatype list.
                It will take url string as mlaas/dataset_schema/datatype/.

                Args  : 
                        
                        
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                def get(self, request, format=None):
                        try :
                                logging.info("data ingestion : ScheamAttributeListClass : POST Method : execution start")
                                schema_df=DBObject.read_data('common/attribute_list.csv')
                                return Response({"status_code":"200","error_msg":"Successfull retrival","response":schema_df})
                        except Exception as e:
                                logging.error("data ingestion : ScheamAttributeListClass : POST Method : Exception :" + str(e))
		        	logging.error("data ingestion : ScheamAttributeListClass : POST Method : "+ traceback.format_exc())
                                return Response({"status_code":"500","error_msg":"Failed","response":str(e)})

        def post(self, request, format=None):
                """
                This class is used to post  Datatype list.
                It will take url string as mlaas/dataset_schema/datatype/.

                Args  : 
                        
                        
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival failed or successfull),
                        Response(return false if failed otherwise json data)
                this function used to get datatype list for schema page 
                Args:
                       [This function does not take any argument] 
                Return:
                        status_code(500 or 200),
                        error_msg(Error message for retrive successfull or unsuccessfull),
                        Response(return error_msg if failed otherwise true )  
                """
                try :
                        logging.info("data ingestion : ScheamAttributeListClass : POST Method : execution start")
                        schema_df=DBObject.read_data('common/attribute_list.csv') #read the data from csv file store into dataframe variable
                        status=DBObject.load_csv_into_db(connection_string,'attribute_types',schema_df,'mlaas') # this function will insert the csv data into  attribute_types table
                        return Response({"status_code":"200","error_msg":"Successfull insertion","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : ScheamAttributeListClass : POST Method : Exception :" + str(e))
			logging.error("data ingestion : ScheamAttributeListClass : POST Method : "+ traceback.format_exc())
                        return Response({"status_code":"500","error_msg":"Failed","response":str(e)})

class ScheamColumnListClass(APIView):

        def get(self, request, format=None):
                """
                This class is used to get  schema column list.
                It will take url string as mlaas/dataset_schema/column_attribute_list/.

                Args  : 
                        
                        
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival failed or successfull),
                        Response(return false if failed otherwise json data)
       
                this function used to get Attribute list for schema page and

                Return:
                        status_code(500 or 200),
                        error_msg(Error message for retrive successfull or unsuccessfull),
                        Response(return false if failed otherwise List of column attribute)  
                """
                def get(self, request, format=None):
                        try :
                                logging.info("data ingestion : ScheamAttributeListClass : POST Method : execution start")
                                column_attribute = {"column_attribute":["ignore","target"] }
                                return Response({"status_code":"200","error_msg":"Successfull retrival","response":column_attribute})
                        except Exception as e:
                                logging.error("data ingestion : ScheamAttributeListClass : POST Method : Exception :" + str(e))
		        	logging.error("data ingestion : ScheamAttributeListClass : POST Method : "+ traceback.format_exc())
                                return Response({"status_code":"500","error_msg":"Failed","response":str(e)})

        def post(self, request, format=None):
                """
                This class is used to post  schema column list.
                It will take url string as mlaas/dataset_schema/column_attribute_list/.

                Args  : 
                        
                        
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival failed or successfull),
                        Response(return false if failed otherwise json data)
                this function used to insert Schema datatype values into a database.
                Args:
                        [This function does not take any argument]
                Return:
                        status_code(500 or 200),
                        error_msg(Error message for retrive successfull or unsuccessfull),
                        Response(return error if failed otherwise true)  
                """
                try :
                        logging.info("data ingestion : ScheamAttributeListClass : POST Method : execution start")
                        schema_df=DBObject.read_data('common/attribute_list.csv') #read the data from csv file store into dataframe variable
                        status=DBObject.load_csv_into_db(connection_string,'attribute_types',schema_df,'mlaas') # this function will insert the csv data into  attribute_types table
                        return Response({"status_code":"200","error_msg":"Successfull insertion","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : ScheamAttributeListClass : POST Method : Exception :" + str(e))
			logging.error("data ingestion : ScheamAttributeListClass : POST Method : "+ traceback.format_exc())
                        return Response({"status_code":"500","error_msg":"Failed","response":str(e)})


class ActivityTimelineClass(APIView):
        

        def get(self,request,format=None):
                """
                This class is used to show the user activity for each of single user.
                It will take url string as mlaas/activity_timeline/.

                Args  : 
                        user_name[(String)]   :[User Name]
                        
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival failed or successfull),
                        Response(return false if failed otherwise json data)
                """
             
                try:
                        logging.info("data ingestion : ActivityTimelineClass : GET Method : execution start")
                        user_name = request.query_params.get('user_name')
                        activity_df = timeline_Obj.get_user_activity(user_name)
                        if isinstance(activity_df,str): #check the instance of activity_df
                                status_code,error_msg=get_Status_code(activity_df) # extract the status_code and error_msg from activity_df
                                logging.info("data ingestion : ActivityTimelineClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                        
                              return Response({"status_code":"200","error_msg":"Successfull retrival","response":activity_df})  
                except Exception as e:
                        logging.error("data ingestion : ActivityTimelineClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : ActivityTimelineClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
 
        