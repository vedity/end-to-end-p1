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
from .utils.schema_creation import *
from database import *

from .utils import ingestion
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils.dataset import dataset_creation
from .utils.ingestion import *
from .utils.project import project_creation
from ingest.testing import get_json_format
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import InputSerializer
from .testing import *
import logging
logger = logging.getLogger('django')
DBObject=db.DBClass()     #Get DBClass object
#user=None
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)
IngestionObj=ingestion.IngestClass(database,user,password,host,port)

class CreateProjectClass(APIView):
        """
        This class is used to Create Project and Insert Uploaded CSV File data into Table.
        It will take url string as mlaas/ingest/create_project/.
        It will take input parameters as Username,ProjectName,Description,inputfile(CSV File).
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Input  : Username,ProjectName,Description,inputfile(CSV File)
        Output : json
        """
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        logger.info(" Call GET method in CreateProjectClass")
                        # user_name=request.user.get_username()
                        user_name=request.POST.get('user_name')  #get Username
                        project_df=IngestionObj.show_project_details(user_name) # call show_project_details to retrive project detail data and it will return dataframe
                        project_df = json.loads(project_df)
                        logger.info("project detail retrival successfull")
                        return Response({"Data":project_df})  #return Data

                except Exception as e:
                        logger.error("Error in CreateProjectClass GET method "+str(e))
                        return Response({"Exception":str(e)}) 
        
        def post(self, request, format=None):
                        try:
                        # user_name=request.user.get_username()  #get Username
                                logger.info("Entered In CreateProjectClass")
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
                                        project_obj=project_creation.ProjectClass()
                                        table_name,_,_=project_obj.make_project_schema()
                                        exists_project_status=project_obj.project_exists(DBObject,connection,table_name,project_name,user_name)
                                        if exists_project_status == False:
                                                my_file=request.FILES['inputfile'] #get inputfile Name
                                                path='static/server/'
                                                try:
                                                        if dataset_visibility == 'public':
                                                                public_path = path + "public"
                                                                fs = FileSystemStorage(location=public_path)
                                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                                filename = fs.save(file_name, my_file)
                                                                file_url = public_path + fs.url(filename)
                                                        elif dataset_visibility == 'private':
                                                                private_path = path + user_name
                                                                fs = FileSystemStorage(location=private_path)
                                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                                filename = fs.save(file_name, my_file)
                                                                file_url = private_path + fs.url(filename)
                                                        else:
                                                                return Response({"visibility":"Not appropriate Value"})

                                                except Exception as e:
                                                        return Response({"Exception":str(e)}) 
                                        else:
                                                return Response({"message":"Project Name already Exists"})
                                else:
                                        dataset_id = int(dataset_id)
                                                
                                
                                Status=IngestionObj.create_project(project_name,project_desc,dataset_name,dataset_visibility,file_name,dataset_id,user_name)    #call create_project method to create project and insert csv data into table
                                status_code,error_msg=get_Status_code(Status)
                                logger.info("Exit From Createprojectclass")
                                return Response({"status_code":status_code,"error_msg":error_msg}) 
                        except Exception as e:
                                        logging.error("Exception occurred In Creatprojectclas", exc_info=True)
                                        return Response({"Exception":str(e)})      

        
class CreateDatasetClass(APIView):
        """
        This Class is used to Create Dataset and Insert Uploaded CSV File data into Table.
        It will take url string as mlaas/ingest/create_dataset/.
        It will take input parameters as Username,ProjectName,Description,inputfile(CSV File).
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Input  : Username,ProjectName,Description,inputfile(CSV File)
        Output : json
        """
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        user_name=request.POST.get('user_name')  #get Username
                       
                        dataset_df=IngestionObj.show_dataset_details(user_name) #Call show_dataset_details method it will return dataset detail for sepecific user_name
                        dataset_df = json.loads(dataset_df)
                        return Response({"Data":dataset_df}) #return Data                
                except Exception as e:
                        return Response({"Exception":str(e)}) 
        
        def post(self, request, format=None):
                try: 

                        # user_name=request.user.get_username()
                        user_name=str(request.POST.get('user_name'))  #get Username
                        dataset_name=request.POST.get('dataset_name') #get dataset name
                        my_file=request.FILES['inputfile'] #get inputfile Name
                        dataset_visibility= request.POST.get('visibility')
                        
                        dataset_obj=dataset_creation.DatasetClass()
                        table_name,_,_=dataset_obj.make_dataset_schema()
                        exists_dataset_status=dataset_obj.dataset_exists(DBObject,connection,table_name,dataset_name,user_name,dataset_visibility)
                        if exists_dataset_status == False:
                                path='static/server/'
                                try:
                                        if dataset_visibility == 'public':
                                                public_path = path + "public"
                                                fs = FileSystemStorage(location=public_path)
                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                filename = fs.save(file_name, my_file)
                                                file_url = public_path + fs.url(filename)
                                        elif dataset_visibility == 'private':
                                                private_path = path + user_name
                                                fs = FileSystemStorage(location=private_path)
                                                file_name = my_file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
                                                filename = fs.save(file_name, my_file)
                                                file_url = private_path + fs.url(filename)
                                        else:
                                                return Response({"visibility":"Not appropriate Value"})

                                except Exception as e:
                                        return Response({"Exception":str(e)})
                        else:
                                return Response({"message":"Dataset Name already Exists"})


                        
                        Status=IngestionObj.create_dataset(dataset_name,file_name,dataset_visibility,user_name) #call create_dataset method to create dataset and insert csv data into table
                        return Response({"Status":Status})   #return Status 
                except Exception as e:
                        return Response({"Exception":str(e)})   

import json

class DatasetSchemaClass(APIView):
        def get(self,request,format=None):
                dataset_id=request.POST.get('dataset_id')
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
        Output : json
        """   
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        user_name = request.POST.get('user_name')
                        table_name=request.POST.get('table_name')  #get tablename
                        dataset_visibility = request.POST.get('dataset_visibility')
                        dataset_df=IngestionObj.show_data_details(table_name,user_name,dataset_visibility) #call show_data_details and it will return dataset detail data in dataframe
                        dataset_json=json.loads(dataset_df)  # convert datafreame into json
                        json_data=get_json_format(dataset_json,['dataset_id','index']) #calling function to get pre-define json format
                        return Response({"Dataset":json_data})  #return Data 
                except Exception as e:
                        return Response({"Exception":str(e)}) 


class DeleteProjectDetailClass(APIView):
        """
        This class is used to delete project detail.
        It will take url string as mlaas/ingest/delete/project_detail/.
        It will take input parameters as project id.
        And it will return status.

        Input  : project id
        Output : status(0 or 1)
        """  
        def delete(self, request, format=None):
                try:
                        # user_name=request.user.get_username()
                        user_name=request.POST.get('user_name')
                        project_id=request.POST.get('project_id')  #get tablename
                        #project_obj=project_creation.ProjectClass()  
                        project_status= IngestionObj.delete_project_details(project_id,user_name) 
                        return Response({"Status":project_status})  #return status 
                except Exception as e:
                        return Response({"Exception":str(e)}) 

class DeleteDatasetDetailClass(APIView):
        """
        This class is used to delete Dataset detail.
        It will take url string as mlaas/ingest/delete/dataset_detail/.
        It will take input parameters as project id.
        And it will return status.

        Input  : dataset id
        Output : status(0 or 1)
        """
        def delete(self, request, format=None):
                try:
                        # user_name=request.user.get_username()
                        user_name=request.POST.get('user_name')
                        dataset_id=request.POST.get('dataset_id')  #get dataset name
                        #dataset_obj=dataset_creation.DatasetClass()
                        dataset_status=IngestionObj.delete_dataset_details(dataset_id,user_name) 
                        return Response({"Status":dataset_status})  #return status 
                except Exception as e:
                        return Response({"Exception":str(e)}) 

class DeleteDataDetailClass(APIView):
        """
        This class is used to delete data(CSV) detail.
        It will take url string as mlaas/ingest/delete/data_detail/.
        It will take input parameters as table name.
        And it will return status.

        Input  : dataset id
        Output : status(0 or 1)
        """
        def delete(self, request, format=None):

                try:
                        # user_name=request.user.get_username()
                        user_name=request.POST.get('user_name')
                        table_name=request.POST.get('table_name')  #get tablename
                        #dataset_obj=dataset_creation.DatasetClass()
                        status=IngestionObj.delete_data_details(table_name,user_name) 
                        return Response({"Status":status})  #return status 
                except Exception as e:
                        return Response({"Exception":str(e)}) 


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

