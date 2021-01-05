'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 INFOSENSE          07-DEC-2020           1.0           Intial Version 

 ****************************************************************************************/

*/
'''


import os
import datetime
import json
import pandas as pd
import logging
import traceback
from .utils.schema_creation import *
from database import *
from common.utils.logger_handler import custom_logger as cl
from .utils import ingestion
from django.core.files.storage import FileSystemStorage
from .utils.dataset import dataset_creation
from .utils.ingestion import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from .utils.project import project_creation
from common.utils.json_format.json_formater import *
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')

DBObject=db.DBClass()     #Get DBClass object
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)
IngestionObj=ingestion.IngestClass(database,user,password,host,port)

class CreateProjectClass(APIView):
        """
        This class is used to Create Project and Insert Uploaded CSV File data into Table.
        It will take url string as mlaas/ingest/create_project/.
        It will take input parameters as Username,ProjectName,Description,inputfile(CSV File).
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Input  : User_name,ProjectName,Description,inputfile(CSV File)
        Output : status_code(500 or 200),
                 error_msg(Error message for retrival & insertions faild or successfull),
                 Response(return false if faild otherwise json data)
        """
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        logging.info("data ingestion : CreateProjectClass : GET Method : execution start")
                        #user_name = request.user.get_username()
                        user_name  = request.query_params.get('user_name') #get Username
                        project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
                        if isinstance(project_df,str): #check the instance of dataset_df
                                status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

                except Exception as e:
                        logging.error("data ingestion : CreateProjectClass : GET Method : " + str(e))
                        logging.error("data ingestion : CreateProjectClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
        
        def post(self, request, format=None):
                        try:
                                
                                logging.info("data ingestion : CreateProjectClass : POST Method : execution start")
                                # user_name=request.user.get_username()  #get Username
                                user_name=request.POST.get('user_name')  #get Username
                                project_name=request.POST.get('project_name') #get project_name
                                project_desc=request.POST.get('description') #get description
                                dataset_name = request.POST.get('dataset_name')#get dataset name
                                dataset_visibility = request.POST.get('visibility') #get Visibility
                                dataset_id = request.POST.get('dataset_id') # get dataset_id, if selected the dataset from dropdown menu otherwise None 
                                file_name = None
                                if dataset_id == "":
                                        dataset_id = None
                                else:
                                        dataset_id = dataset_id               
                                if dataset_id == None :
                                        # project_obj=project_creation.ProjectClass()
                                        # table_name,_,_=project_obj.make_project_schema()
                                        exists_project_status = IngestionObj.does_project_exists(project_name,user_name) 
                                        #logger.info("Calling project_exist function to check project Name")
                                        # exists_project_status=project_obj.project_exists(DBObject,connection,table_name,project_name,user_name)
                                        if exists_project_status == False:
                                                my_file=request.FILES['inputfile'] #get inputfile Name
                                                file_check_status = IngestionObj.check_file(my_file)
                                                if file_check_status == False:
                                                        raise FileNotFound(500)
                                                
                                                file_data = pd.read_csv(request.FILES['inputfile'])  
                                                file_check_status = IngestionObj.check_file(my_file,file_data)
                                                if file_check_status == False:
                                                        raise FileNotFound(500)
                                                        
                                                path='static/server/'
                                                try:
                                                        if dataset_visibility == 'public': #checking visibility if public then file uploaded into public folder
                                                                public_path = path + "public"
                                                                fs = FileSystemStorage(location=public_path)
                                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                                filename = fs.save(file_name, my_file)
                                                                file_url = public_path + fs.url(filename)
                                                        elif dataset_visibility == 'private': #checking visibility if private then file uploaded into public folder
                                                                private_path = path + user_name
                                                                fs = FileSystemStorage(location=private_path)
                                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                                filename = fs.save(file_name, my_file)
                                                                file_url = private_path + fs.url(filename)
                                                        else:
                                                                return Response({"visibility":"Not appropriate Value"})

                                                except Exception as e:
                                                        logger.error(" call POST method in CreateProjectClass while uploading file to server"+str(e))
                                                        return Response({"status_code":"500","error_msg":"InvalidFileInput","response":"false"}) 
                                        else:
                                                return Response({"status_code":"500","error_msg":"ProjectALreadyExist","response":"false"})
                                else:
                                        dataset_id = int(dataset_id)
                                                
                                
                                project_Status=IngestionObj.create_project(project_name,project_desc,dataset_name,dataset_visibility,file_name,dataset_id,user_name)    #call create_project method to create project and insert csv data into table
                                if project_Status != 0:
                                        status_code,error_msg=get_Status_code(project_Status) # extract the status_code and error_msg from project_Status
                                        logging.info("data ingestion : CreateProjectClass : POST Method : execution stop : status_code :"+status_code)
                                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                                else:
                                        logging.info("data ingestion : CreateProjectClass : POST Method : execution stop : status_code : 200")
                                        return Response({"status_code":"200","status_msg":"Successfully Inserted","response":"true"}) 

                        except Exception as e:
                                logging.error("data ingestion : CreateProjectClass : POST Method : " + str(e))
                                logging.error("data ingestion : CreateProjectClass : POST Method : " +traceback.format_exc())
                                return Response({"status_code":"500","error_msg":str(e),"response":"false"})      

        
class CreateDatasetClass(APIView):
        """
        This Class is used to Create Dataset and Insert Uploaded CSV File data into Table.
        It will take url string as mlaas/ingest/create_dataset/.
        It will take input parameters as Username,ProjectName,Description,inputfile(CSV File).
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Input  : Username,ProjectName,Description,inputfile(CSV File)
        Output : status_code(500 or 200),
                 error_msg(Error message for retrival & insertions faild or successfull),
                 Response(return false if faild otherwise json data) 
        """
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        # logging.info("data ingestion : CreateDatasetClass : GET Method : execution start")
                        user_name=request.query_params.get('user_name')  #get Username
                        dataset_df=IngestionObj.show_dataset_details(user_name) #Call show_dataset_details method it will return dataset detail for sepecific user_name
                        if isinstance(dataset_df,str): #check the instance of dataset_df
                                status_code,error_msg=get_Status_code(dataset_df) # extract the status_code and error_msg from dataset_df
                                logging.info("data ingestion : CreateDatasetClass : GET Method : execution stop : status_code : "+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateDatasetClass : GET Method : execution stop : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":dataset_df})  #return Data             
                except Exception as e:
                        logging.error("data ingestion : CreateDatasetClass : GET Method : " + str(e))
                        logging.error("data ingestion : CreateDatasetClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
        
        def post(self, request, format=None):
                try: 
                        # logging.info("data ingestion : CreateDatasetClass : POST Method : execution start")
                        # user_name=request.user.get_username()
                        user_name=str(request.POST.get('user_name'))  #get Username
                        dataset_name=request.POST.get('dataset_name') #get dataset name
                        my_file=request.FILES['inputfile'] #get inputfile Name
                        dataset_visibility= request.POST.get('visibility')
                        
                        exists_dataset_status=IngestionObj.does_dataset_exists(dataset_name,user_name) 
                        # exists_dataset_status=dataset_obj.dataset_exists(DBObject,connection,table_name,dataset_name,user_name,dataset_visibility)
                        
                        if exists_dataset_status == False:
                                
                                try:
                                        file_check_status = IngestionObj.check_file(my_file)
                                        if file_check_status == False:
                                                raise FileNotFound(500)
                                        
                                        file_data = pd.read_csv(request.FILES['inputfile']) 
                                        file_check_status = IngestionObj.check_file(my_file,file_data)
                                        
                                        if file_check_status == False:
                                                raise FileNotFound(500)
                                        
                                        path='static/server/'
                                
                                        if dataset_visibility == 'public':
                                                public_path = path + "public"
                                                fs = FileSystemStorage(location=public_path)
                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                filename = fs.save(file_name, my_file)
                                                file_url = public_path + fs.url(filename)
                                        elif dataset_visibility == 'private': #checking visibility if private then file uploaded into user specific folder 
                                                private_path = path + user_name
                                                fs = FileSystemStorage(location=private_path)
                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                filename = fs.save(file_name, my_file)
                                                file_url = private_path + fs.url(filename)
                                        else:
                                                
                                                return Response({"status_code":"500","error_msg":"Not appropriate Value","response":"false"}) 
                                                

                                except Exception as e:
                                        # logging.error("data ingestion : CreateDatasetClass : POST Method :  Exception : " + str(e))
                                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
                                        # return Response({"status_code":"500","error_msg":"InputProperFile":str(e),"response":"false"})
                        else:
                                return Response({"status_code":"200","error_msg":"Dataset Name already Exists","response":"true"})
                                # return Response({"status_code":"500","Dataset Name already Exists","response":"false"})

                        dataset_Status=IngestionObj.create_dataset(dataset_name,file_name,dataset_visibility,user_name) #call create_dataset method to create dataset and insert csv data into table
                        if dataset_Status != 0:
                                status_code,error_msg=get_Status_code(dataset_Status) # extract the status_code and error_msg from dataset_status
                                logging.info("data ingestion : CreateDatasetClass : POST Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                        else:
                                logging.info("data ingestion : CreateDatasetClass : POST Method : execution stop : status_code : 200")
                                return Response({"status_code":"200","error_msg":"Successfully Inserted","response":"true"})
                        
                except Exception as e:
                        # logging.error("data ingestion : CreateDatasetClass : POST Method : Exception : " + str(e))
			# logging.error("data ingestion : CreateDatasetClass : POST Method : "+ traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 
                  
class DatasetSchemaClass(APIView):
        def get(self,request,format=None):
                dataset_id=request.query_params.get('dataset_id')
                schema_obj=SchemaClass(database,user,password,host,port)
                schema_data=schema_obj.get_dataset_schema(str(dataset_id))
                return Response({"Schema":str(schema_data)})    

        def put(self,request,format=None):
                update_schema_data=json.loads(request.body)

                # user_name=request.POST.get('user_name')
                # dataset_id=request.POST.get('dataset_id')

                # column_list=[]
                # col_attribute_list=[]
                # col_datatype_list=[]
                # column_list.append(request.POST.get('id'))
                # column_list.append(request.POST.get('name'))
                # column_list.append(request.POST.get('sal'))

                # col_attribute_list.append(request.POST.get('datatype_id'))
                # col_attribute_list.append(request.POST.get('datatype_name'))
                # col_attribute_list.append(request.POST.get('datatype_sal'))

                # col_datatype_list.append(request.POST.get('col_id'))
                # col_datatype_list.append(request.POST.get('col_name'))
                # col_datatype_list.append(request.POST.get('col_sal'))

                # schema_obj=SchemaClass(database,user,password,host,port)
                # schema_status=schema_obj.update_dataset_schema(column_list,col_datatype_list,col_attribute_list,dataset_id,user_name)

                return Response({"Status":update_schema_data})           
                

class DataDetailClass(APIView):
        """
        This class is used to Retrive dataset detail Data(CSV Data).
        It will take url string as mlaas/ingest/data_detail/.
        It will take input parameters as tablename.
        And it will return dataset detail Data in Json Format.

        Input  : tablename
        Output : status_code(500 or 200),
                 error_msg(Error message for retrival faild or successfull),
                 Response(return false if faild otherwise json data)
        """   
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        # logging.info("data ingestion : DataDetailClass : GET Method : execution start")
                        dataset_id = request.query_params.get('dataset_id') #get dataset_id
                        dataset_df=IngestionObj.show_data_details(dataset_id) #call show_data_details and it will return dataset detail data in dataframe
                        if isinstance(dataset_df,str): #check the instance of dataset_df
                                status_code,error_msg=get_Status_code(dataset_df) # extract the status_code and error_msg  from dataset_df
                                logging.info("data ingestion : DataDetailClass : GET Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : DataDetailClass : GET Method : execution stop : status_code :200")
                                json_data=get_json_format(dataset_df,['dataset_id','index']) 
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":json_data})  #return Data             
                except Exception as e:
                        logging.error("data ingestion : DataDetailClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : DataDetailClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 


class DeleteProjectDetailClass(APIView):
        """
        This class is used to delete project detail.
        It will take url string as mlaas/ingest/delete/project_detail/.
        It will take input parameters as project id.
        And it will return status.

        Input  : project id
        Output : status_code(500 or 200),
                 error_msg(Error message for deletion faild or successfull),
                 Response(false or true)
        """  
        def delete(self, request, format=None):
                try:
                        logging.info("data ingestion : DeleteProjectDetailClass : DELETE Method : execution start")
                        # user_name=request.user.get_username()
                        user_name=request.query_params.get('user_name') # get username
                        project_id=request.query_params.get('project_id')  #get tablename 
                        project_status= IngestionObj.delete_project_details(project_id,user_name)  #get the project_status if project Deletion failed or successfull
                        if project_status != 0:
                                status_code,error_msg=get_Status_code(project_status) # extract the status_code and error_msg from  project_status
                                logging.info("data ingestion : DeleteProjectDetailClass : DELETE Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                        else:
                                logging.info("data ingestion : DeleteProjectDetailClass : DELETE Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully Delete","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : DeleteProjectDetailClass : DELETE Method :  Exception : " + str(e))
                        logging.error("data ingestion : DeleteProjectDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class DeleteDatasetDetailClass(APIView):
        """
        This class is used to delete Dataset detail.
        It will take url string as mlaas/ingest/delete/dataset_detail/.
        It will take input parameters as project id.
        And it will return status.

        Input  : dataset id
        Output : status_code(500 or 200),
                 error_msg(Error message for deletion faild or successfull),
                 Response(false or true)
        """
        def delete(self, request, format=None):
                try:
                        logging.info("data ingestion : DeleteDatasetDetailClass : DELETE Method : execution start")
                        # user_name=request.user.get_username()
                        user_name=request.query_params.get('user_name') #get user_name
                        dataset_id=request.query_params.get('dataset_id')  #get dataset_name
                        dataset_status=IngestionObj.delete_dataset_detail(dataset_id,user_name) #get the dataset_status if dataset Deletion failed or successfull 
                        if dataset_status != 0:
                                status_code,error_msg=get_Status_code(dataset_status) # extract the status_code and error_msg from dataset_status
                                logging.info("data ingestion : DeleteDatasetDetailClass : DELETE Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                        else:
                                logging.info("data ingestion : DeleteDatasetDetailClass : DELETE Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully Deleted","response":"true"})

                except Exception as e:
                        logging.error("data ingestion : DeleteDatasetDetailClass : DELETE Method : Exception : " + str(e))
                        logging.error("data ingestion : DeleteDatasetDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class DeleteDataDetailClass(APIView):
        """
        This class is used to delete data(CSV) detail.
        It will take url string as mlaas/ingest/delete/data_detail/.
        It will take input parameters as table name.
        And it will return status.

        Input  : dataset id
        Output : status_code(500 or 200),
                error_msg(Error message for deletion faild or successfull),
                Response(false or true)
        """
        def delete(self, request, format=None):

                try:
                        # logging.info("data ingestion : DeleteDataDetailClass : DELETE Method : execution start")
                        # user_name=request.user.get_username()
                        user_name=request.query_params.get('user_name')
                        table_name=request.query_params.get('table_name')  #get tablename
                        data_detail_status=IngestionObj.delete_data_detail(table_name,user_name) 
                        if data_detail_status != 0 :
                                status_code,error_msg=get_Status_code(data_detail_status) # extract the status_code and error_msg from data_detail_status
                                logging.info("data ingestion : DeleteDataDetailClass : DELETE Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                        else:
                                logging.info("data ingestion : DeleteDataDetailClass : DELETE Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully Deleted","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : DeleteDataDetailClass : DELETE Method : Exception :" + str(e))
                        logging.error("data ingestion : DeleteDataDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 


class ToggleLogs(APIView):
        def get(self,request,format=None):
                reader_obj = open(r'Mlaas/settings.py','r')
                settings_string = reader_obj.read()
                logging_line_index = settings_string.find("LOGGING")
                bracket_index = settings_string.find("(",logging_line_index)
                bracket_index+=1
                
                if settings_string[bracket_index] == 'T':
                        settings_string = settings_string[:bracket_index] + "False" + settings_string[bracket_index+4:]
                        logging_status = "False"
                else:
                        settings_string = settings_string[:bracket_index] + "True" + settings_string[bracket_index+5:]
                        logging_status = "True"
                
                reader_obj.close()
                
                writer_obj = open(r'Mlaas/settings.py','w')
                writer_obj.write(settings_string)
                
                writer_obj.close()
                
                return Response({"msg":f"Logging Status changed to {logging_status}"})

class ProjectExistClass(APIView):
        """
        This class is used to Check ProjectName already exist or not.
        It will take url string as mlaas/ingest/project_exist/.
        It will take input parameters as user_name,project_name.
        And it will return status,error_msg and response.

        Input  : user_name,project_name
        Output : status_code(500 or 200),
                 error_msg(Error message for deletion faild or successfull),
                 Response(false or true)
        """
        def get(self,request,format=None):
                logging.info("data ingestion : ProjectExistClass : GET Method : execution start")
                user_name = request.query_params.get('user_name') #get user_name
                project_name =request.query_params.get('project_name') #get project_name
                projectexist_status=IngestionObj.does_project_exists(project_name,user_name) # get status
                if projectexist_status != False:
                        status_code,error_msg=get_Status_code(projectexist_status) # extract the status_code and error_msg from projectexist_status
                        logging.info("data ingestion : ProjectExistClass : GET Method : execution stop : status_code :"+status_code)
                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                else:
                        logging.info("data ingestion : ProjectExistClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"you can proceed","response":"true"})  
class DatasetExistClass(APIView):
        """
        This class is used to Check Dataset already exist or not.
        It will take url string as mlaas/ingest/dataset_exist/.
        It will take input parameters as user_name,dataset_name.
        And it will return status,error_msg and response.

        Input  : user_name,dataset_name
        Output : status_code(500 or 200),
                 error_msg(Error message for deletion faild or successfull),
                 Response(false or true)
        """
        def get(self,request,format=None):
                # logging.info("data ingestion : DatasetExistClass : GET Method : execution start")
                user_name = request.query_params.get('user_name') #get user_name
                dataset_name = request.query_params.get('dataset_name') #get dataset_name
                datasetexist_status=IngestionObj.does_dataset_exists(dataset_name,user_name) #get the status if dataset exist or not 
                if datasetexist_status != False:
                        status_code,error_msg=get_Status_code(datasetexist_status) # extract the status_code and error_msg from datasetexist_status
                        logging.info("data ingestion : DatasetExistClass : GET Method : execution stop : status_code :"+status_code)
                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                else:
                        logging.info("data ingestion : DatasetExistClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"you can proceed","response":"true"})  
class DatasetNameClass(APIView):
        """
        This class is used to get All Dataset name which are unploaded.
        It will take url string as mlaas/ingest/datasetname_exist/.
        It will take input parameters as user_name.
        And it will return status,error_msg and response.

        Input  : user_name
        Output : status_code(500 or 200),
                 error_msg(Error message for deletion faild or successfull),
                 Response(false or true)
        """
        def get(self,request,format=None):
                logging.info("data ingestion : DatasetNameClass : GET Method : execution start")
                user_name =request.query_params.get('user_name') #get user_name
                dataset_df=IngestionObj.show_dataset_names(user_name) #retrive all dataset name for that perticular user_name
                if isinstance(dataset_df,str): #check the instance of dataset_df
                        status_code,error_msg=get_Status_code(dataset_df) # extract the status_code and error_msg from dataset_df
                        logging.info("data ingestion : DatasetNameClass : GET Method : execution stop : status_code :"+status_code)
                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                else:
                        logging.info("data ingestion : DatasetNameClass : GET Method : execution stop : status_code : 200")
                        return Response({"status_code":"200","error_msg":"you can proceed","response":dataset_df})
        

class MenuClass(APIView):
        def post(self, request, format=None):
                try:
                        logging.info("data ingestion : MenuClass : POST Method : execution start")
                        menu_df=DBObject.read_data('ingest/Menu.csv')
                        status=DBObject.load_csv_into_db(connection_string,'menu_tbl',menu_df,'mlaas')
                        return Response({"Status":status})
                except Exception as e:
                        logging.error("data ingestion : MenuClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : MenuClass : GET Method : " +traceback.format_exc())
                        return Response({"Exception":str(e)}) 
        
        def get(self, request, format=None):
                try:
                        # logging.info("data ingestion : MenuClass : POST Method : execution start")
                        sql_command1='select id,modulename,menuname as "label",parent_id as "parentId",url,icon from mlaas.menu_tbl where parent_id is null'
                        dataset_df1=DBObject.select_records(connection,sql_command1) #call show_data_details and it will return dataset detail data in dataframe
                        dataset_json1=json.loads(dataset_df1.to_json(orient='records'))  # convert datafreame into json
                        sql_command2='select id,modulename,menuname as "label",parent_id as "parentId",url,icon from mlaas.menu_tbl where parent_id is not null'
                        dataset_df2=DBObject.select_records(connection,sql_command2) #call show_data_details and it will return dataset detail data in dataframe
                        dataset_json2=json.loads(dataset_df2.to_json(orient='records'))  # convert datafreame into json
                        json_data=menu_nested_format(dataset_json1,dataset_json2)   
                        return Response({"status_code":"200","error_msg":"Menu Data","response":json_data})
                except Exception as e:
                        # logging.error("data ingestion : MenuClass : POST Method : Exception :" + str(e))
			# logging.error("data ingestion : MenuClass : POST Method : "+ traceback.format_exc())
                        return Response({"status_code":"500","error_msg":"Failed","response":str(e)})
