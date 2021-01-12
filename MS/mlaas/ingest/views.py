'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 INFOSENSE          07-DEC-2020           1.0           Intial Version 

 ****************************************************************************************/

*/
'''

import json
import logging
import traceback
import pandas as pd
from database import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import schema_creation 
from .utils.schema_creation import *
from .utils import ingestion
from .utils.ingestion import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception import *
from common.utils.json_format.json_formater import *

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
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Args  : 
                User_name[(String)]   :[Name of user]
                ProjectName[(String)] :[Name of project]
                Description[(String)] :[Discreption of project]
                dataset_visibility[(String)] :[Name of Visibility public or private]
                dataset_id[(Integer)] :[ID of dataset selected by user from dropdown]
                inputfile(CSV File)   :[Input CSV file]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for retrival & insertions failed or successfull),
                Response(return false if failed otherwise json data)
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
                                        exists_project_status = IngestionObj.does_project_exists(project_name,user_name) 
                                        if exists_project_status == False:
                                                file=request.FILES['inputfile'] #get inputfile Name
                                                file_data = pd.read_csv(request.FILES['inputfile']) # read the csv file and store into dataframe variable
                                                file_check_status = IngestionObj.check_file(file,file_data) # call check_file function to verify csv file data
                                                if file_check_status !=True: #if file_check_status not equal to true then file must  be inappropriate
                                                        status_code,error_msg=get_Status_code(file_check_status) # extract the status_code and error_msg from file_check_status
                                                        logging.info("data ingestion : CreateProjectClass : POST Method : execution stop : status_code :"+status_code)
                                                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                                                file_path="static/server/" 
                                                file_name = IngestionObj.save_file(user_name,dataset_visibility,file,file_path) 
                                                 
                                        else:
                                                return Response({"status_code":"500","error_msg":"Project already exist","response":"false"})
                                else:
                                        dataset_id = int(dataset_id)
                                                
                                datasetexist_status=IngestionObj.does_dataset_exists(dataset_name,user_name) #get the status if dataset exist or not 
                                if datasetexist_status != False:
                                        status_code,error_msg=get_Status_code(datasetexist_status) # extract the status_code and error_msg from datasetexist_status
                                        logging.info("data ingestion : DatasetExistClass : GET Method : execution stop : status_code :"+status_code)
                                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                                else:
                                        logging.info("data ingestion : DatasetExistClass : GET Method : execution stop : status_code :200")
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
        And if Method is "POST" then it will return Status or if Method is "GET" then it will return Data in Json Format else it will return Method is not allowed.

        Args   :
                user_name[(String)]   :[Name of user]
                dataset_Name[(String)] :[Name of dataset]
                dataset_visibility[(String)] :[Name of Visibility public or private]
                inputfile(CSV File)   :[Input CSV file]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for retrival & insertions failed or successfull),
                Response(return false if failed otherwise json data) 
        """
        # permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
                try:
                        logging.info("data ingestion : CreateDatasetClass : GET Method : execution start")
                        user_name=request.query_params.get('user_name')  #get Username
                        dataset_df=IngestionObj.show_dataset_details(user_name) #Call show_dataset_details method it will return dataset detail for specific user_name
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
                        logging.info("data ingestion : CreateDatasetClass : POST Method : execution start")
                        # user_name=request.user.get_username()
                        user_name=str(request.POST.get('user_name'))  #get Username
                        dataset_name=request.POST.get('dataset_name') #get dataset name
                        dataset_visibility= request.POST.get('visibility')
                        exists_dataset_status=IngestionObj.does_dataset_exists(dataset_name,user_name) #call does_dataset_exists, check if dataset name exist for that perticular user name return false if not,otherwise true
                        if exists_dataset_status == False:
                                file=request.FILES['inputfile'] #get inputfile Name
                                file_data = pd.read_csv(request.FILES['inputfile'])   # read the csv file and store into dataframe variable                             
                                file_check_status = IngestionObj.check_file(file,file_data)  # call check_file function to verify csv file data
                                if file_check_status !=True:
                                        status_code,error_msg=get_Status_code(file_check_status) # extract the status_code and error_msg from file_check_status
                                        logging.info("data ingestion : CreateProjectClass : POST Method : execution stop : status_code :"+status_code)
                                        return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                                file_path="static/server/"
                                file_name =IngestionObj.save_file(user_name,dataset_visibility,file,file_path)
                        else:
                                return Response({"status_code":"500","error_msg":"Dataset name exists","response":"false"})

                        dataset_Status=IngestionObj.create_dataset(dataset_name,file_name,dataset_visibility,user_name) #call create_dataset method to create dataset and insert csv data into table
                        if dataset_Status != 0:
                                status_code,error_msg=get_Status_code(dataset_Status) # extract the status_code and error_msg from dataset_status
                                logging.info("data ingestion : CreateDatasetClass : POST Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"}) 
                        else:
                                logging.info("data ingestion : CreateDatasetClass : POST Method : execution stop : status_code : 200")
                                return Response({"status_code":"200","error_msg":"Successfully Inserted","response":"true"})
                        
                except Exception as e:
                        logging.error("data ingestion : CreateDatasetClass : POST Method : Exception : " + str(e))
			# logging.error("data ingestion : CreateDatasetClass : POST Method : "+traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 
                  
class DatasetSchemaClass(APIView):
        def get(self,request,format=None):
                dataset_id=request.query_params.get('dataset_id')
                schema_obj=SchemaClass(database,user,password,host,port)
                schema_data=schema_obj.get_dataset_schema(str(dataset_id))
                return Response({"Schema":schema_data})    
   

        def put(self,request,format=None):
                update_schema_data=json.loads(request.body)
                user_name=request.POST.get('user_name')
                dataset_id=request.POST.get('dataset_id')

                # column_list 
                # col_attribute_list
                # col_datatype_list
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
                    

                # col_datatype_list.append(request.POST.get('col_id'))
                # col_datatype_list.append(request.POST.get('col_name'))
                # col_datatype_list.append(request.POST.get('col_sal'))

                schema_obj=SchemaClass(database,user,password,host,port)
                schema_status=schema_obj.update_dataset_schema(column_list,col_datatype_list,col_attribute_list,dataset_id,user_name)

                return Response({"Status":update_schema_data})           
                

class DataDetailClass(APIView):
        """
        this class used to get the fixed length of records with option to search and sorting 
        It will take url string as mlaas/ingest/data_detail/.

        Args : 
                start_index[(Integer)] : [value of the starting index]
                length[(Integer)] :[value of length of records to be shown]
                sort_type[(String)] : [value of sort_type ascending or descending]
                sort_index[(Integer)] : [index value of the column to perform sorting]
                global_value[(String)] : [value that need be search in table]
                dataset_id[(Integer)] : [Id of the dataset table]
        Return : 
                [json] : [It will return json formatted data of table ]
        """   

        def post(self, request, format=None ):
                try:
                        logging.info("data ingestion : DataDetailClass : POST Method : execution start")
                        # logging.info("json data"+ str(type(request.data)) )
                        data = json.dumps(request.data)
                        request_body = json.loads(data) #get all the request body parameter and convert into dictonery
                        draw=request_body["draw"]
                        start_index=request_body["start"] #get the start index
                        length=request_body["length"] #get the length
                        order_values=request_body['order'] 
                        sort_type=order_values[0]['dir'] # get the sort type value(asc or desc)
                        sort_index=order_values[0]['column'] # get the sort_index column value
                        global_value=request_body['search']['value']  #get String value for global search
                        dataset_id = request.query_params.get('dataset_id') #get dataset_id
                        row_count=DBObject.get_row_count(connection,dataset_id) #get the row count
                        dataset_df=IngestionObj.show_data_details(dataset_id,start_index,length,sort_type,sort_index,global_value) #call show_data_details and it will return dataset detail data in dataframe
                        if isinstance(dataset_df,str): #check the instance of dataset_df
                                status_code,error_msg=get_Status_code(dataset_df) # extract the status_code and error_msg  from dataset_df
                                logging.info("data ingestion : DataDetailClass : POST Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : DataDetailClass : POST Method : execution stop : status_code :200")
                                # return Response({​​​​​"draw":draw,"recordsTotal":RowCount,"recordsFiltered":RowCount,"data":data}​​​​​)
                                return Response({"draw":draw,"recordsTotal":row_count,"recordsFiltered":row_count,"data":dataset_df})  #return Data             
                except Exception as e:
                        logging.error("data ingestion : DataDetailClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : DataDetailClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class DataDetailColumnListClass(APIView):
         def get(self, request, format=None):
                try:
                        logging.info("data ingestion : DataDetailClass : GET Method : execution start")
                        dataset_id = request.query_params.get('dataset_id') #get dataset_id
                        DBObject=db.DBClass()
                        dataset_df=DBObject.get_column_list(connection,dataset_id) #call show_data_details and it will return dataset detail data in dataframe
                        if isinstance(dataset_df,str): #check the instance of dataset_df
                                status_code,error_msg=get_Status_code(dataset_df) # extract the status_code and error_msg  from dataset_df
                                logging.info("data ingestion : DataDetailClass : GET Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : DataDetailClass : GET Method : execution stop : status_code :200")
                                getcolumn = get_column_name(dataset_df)
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":getcolumn})  #return Data             
                except Exception as e:
                        logging.error("data ingestion : DataDetailClass : GET Method : Exception :" + str(e))
                        logging.error("data ingestion : DataDetailClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 
class DeleteProjectDetailClass(APIView):
        """
        This class is used to delete project detail.
        It will take url string as mlaas/ingest/delete/project_detail/.

        Args   : 
                User_name[(String)]   :[Name of user]
                project_id[(Integer)] :[ID of project]
                
        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
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
                                return Response({"status_code":"200","error_msg":"Successfully delete","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : DeleteProjectDetailClass : DELETE Method :  Exception : " + str(e))
                        logging.error("data ingestion : DeleteProjectDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class DeleteDatasetDetailClass(APIView):
        """
        This class is used to delete Dataset detail.
        It will take url string as mlaas/ingest/delete/dataset_detail/.

        Args   : 
                User_name[(String)]   :[Name of user]
                dataset_id[(Integer)] :[ID of dataset]

        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
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
                                return Response({"status_code":"200","error_msg":"Successfully deleted","response":"true"})

                except Exception as e:
                        logging.error("data ingestion : DeleteDatasetDetailClass : DELETE Method : Exception : " + str(e))
                        logging.error("data ingestion : DeleteDatasetDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class DeleteDataDetailClass(APIView):
        """
        This class is used to delete data(CSV) detail.
        It will take url string as mlaas/ingest/delete/data_detail/.

        Args  : 
                user_name[(String)]  :  [Name of the user]
                table_name[(String)] :  [Name of the table]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
                Response(false or true)
        """
        def delete(self, request, format=None):

                try:
                        logging.info("data ingestion : DeleteDataDetailClass : DELETE Method : execution start")
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
                                return Response({"status_code":"200","error_msg":"Successfully deleted","response":"true"})
                except Exception as e:
                        logging.error("data ingestion : DeleteDataDetailClass : DELETE Method : Exception :" + str(e))
                        logging.error("data ingestion : DeleteDataDetailClass : DELETE Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"}) 

class ProjectExistClass(APIView):
        """
        This class is used to Check ProjectName already exist or not.
        It will take url string as mlaas/ingest/project_exist/.

        Args  : 
                user_name[(String)] : [Name of the user]
                project_name[(String)] : [Name of the project]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
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


        Args  : 
                user_name[(String)] : [Name of the user]
                dataset_name[(String)] : [Name of the dataset]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
                Response(false or true)
        """
        def get(self,request,format=None):
                logging.info("data ingestion : DatasetExistClass : GET Method : execution start")
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
        This class is used to get All Dataset name which are uploaded.
        It will take url string as mlaas/ingest/datasetname_exist/.


        Args  : 
                user_name[(String)] : [Name of the user]
        Return : 
                status_code(500 or 200),
                error_msg(Error message for deletion failed or successfull),
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
        