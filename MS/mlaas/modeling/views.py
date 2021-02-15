from django.shortcuts import render
import json
import logging
import traceback
import pandas as pd
from database import *
from rest_framework.views import APIView
from rest_framework.response import Response
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.ingest.ingest_exception import *
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception import *
from common.utils.json_format.json_formater import *
from common.utils.database import db
from modeling.model_identifier import *


user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')



DBObject=db.DBClass()     #Get DBClass object
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)

# input_features_list = ['index','house_size','bedrooms','bathrooms']
# target_features_list = ['index','price'] 

input_features_list = ['index','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']  
target_features_list = ['index','price'] 


project_id = 2
dataset_id = 2
user_id = 2

Model_Mode ="auto"

#ModelObject = ModelClass(Model_Mode,input_features_list,target_features_list,project_id,dataset_id, user_id)
# Create your views here.
#class to get project name,dataset name,target column list
#It will take url string as mlaas/modeling/showdatasetinfo/.

class ShowDatasetInfoClass(APIView):
        
        def get(self,request,format=None):
                """
                This function is used to get Project Name, Dataset name and List of Target Columns which are uploaded user.

                Args  : 
                        project_id[(String)] :[Id of project]
                        dataset_id[(String)] :[Id of dataset]
                                

                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                """
                try:
                        ############### New Changes #########################
                        Model_Mode = "Auto"

                        

                        # Call The Model Class
                        ModelObject = ModelClass(Model_Mode,
                                                input_features_list,
                                                target_features_list,
                                                project_id,
                                                dataset_id, 
                                                user_id,
                                                DBObject,
                                                connection, 
                                                connection_string)


                        # If Manual Mode Then Give Below Details #########

                        # split_dataset = {'model_mode': 'manual', 'split_method': 'cross_validation',
                        #     'cv': 5, 'train_size': None, 'valid_size': None, 'test_size': 0.2, 'random_state': 0}

                      
                        
                        ####################################################
                        logging.info(": : POST Method : execution start")
                        # project_id =request.query_params.get('project_id')

                        # dataset_id =request.query_params.get('dataset_id')
                        # user_id=request.query_params.get('user_id')
                        
                        
                        

                        
                        project_name, dataset_name, target_columns =ModelObject.get_dataset_info()
                        
                        show_dataset_info_dictionary = {}
                        show_dataset_info_dictionary['project_name']=project_name
                        show_dataset_info_dictionary['dataset_name']=dataset_name
                        show_dataset_info_dictionary['target_columns']=target_columns
                        
                        if show_dataset_info_dictionary:
                                logging.info(": : POST Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":show_dataset_info_dictionary})
                        else:
                                #status_code,error_msg=get_Status_code(schema_status) # extract the status_code and error_msg from schema_status
                                logging.info("data ingestion : DatasetSchemaClass : POST Method : execution stop : status_code :"+500)
                                #return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})           
                                return Response({"status_code":"500","error_msg":"Error","response":"false"})           
                except Exception as e:
                        logging.error(": : POST Method : Exception :" + str(e))
                        logging.error(": : POST Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})


# Start And End
class SplitDataClass(APIView):
        def post(self,request,format=None):
                """
                This function is used to get Project Name, Dataset name and List of Target Columns which are uploaded user.

                Args  : 
                        project_id[(Integer)] :[ID of project]
                        dataset_id[(Integer)] :[ID of dataset]
                        user_id[(Integer)] :[ID of user]
                        split_data_dictionary[(Dictionary)] : [Dictionary of Split Data]

                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                """
                try:
                        logging.info(": : POST Method : execution start")
                        
                        Model_Mode = "Auto"

                        ModelObject = ModelClass(Model_Mode,input_features_list,target_features_list,project_id,
                                                 dataset_id, user_id, DBObject, connection, connection_string)
                        
                        
                        model_mode = request.POST.get('model_mode')
                        if model_mode == 'manual': 
                                split_method = request.POST.get('split_method')
                                cv = request.POST.get('cv')
                                valid_size = request.POST.get('valid_size')
                                test_size = request.POST.get('test_size')
                                random_state = request.POST.get('random_state')
                                model_id = request.POST.get('model_id')
                                model_name = request.POST.get('model_name')
                                model_type = request.POST.get('model_type')
                                basic_split_parameters = {}
                                basic_split_parameters['model_mode']=model_mode
                                basic_split_parameters['split_method']=split_method
                                basic_split_parameters['cv']=cv
                                basic_split_parameters['valid_size']= valid_size
                                basic_split_parameters['test_size']= test_size
                                basic_split_parameters['random_state']= random_state
                                split_data_object = ModelObject.split_dataset(basic_split_parameters)

                        elif model_mode == 'auto':
                                
                                basic_split_parameters = {'model_mode': model_mode}
                                split_data_object = ModelObject.split_dataset(basic_split_parameters)
                                
                                
                        

                        
                        #split_data_dictionary=json.loads(request.body) #convert the data into dictonery
                        # split_data_object = ModelObject.get_split_data_object(split_data_dictionary)
                        #run_model_status=
                        ModelObject.run_model(model_id,model_name,model_type,split_data_object)
                        if run_model_status !=True:
                                status_code,error_msg=get_Status_code(run_model_status) # extract the status_code and error_msg from schema_status
                                logging.info(" :  : POST Method : execution stop : status_code :"+status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info(": : POST Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":"true"})           
                except Exception as e:
                        logging.error(": : POST Method : Exception :" + str(e))
                        logging.error(": : POST Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
                
                
                
class StartModelClass(APIView):
        def get(self,request,format=None):
                """
                This function is used to get  model mode selected by user
 
                Args  : 
                        mode[(String)] :[mode of model]
                                
 
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                        
                """
                ModelObject = ModelClass(Model_Mode,input_features_list,target_features_list,
                                         project_id,dataset_id,user_id,
                                         DBObject,connection,connection_string)

                try:
                        logging.info(": : POST Method : execution start")
                        # model_mode =request.query_params.get('model_mode')
                        model_mode = 'auto'
                        if model_mode == 'auto':
                                
                                basic_split_parameters = {'model_mode': 'auto'}
                                split_data_object = ModelObject.split_dataset((basic_split_parameters))
                                ModelObject.algorithm_identifier(split_data_object)
                                logging.info(": : POST Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":"True"})
                        else:
                                
                                
                                split_method = request.POST.get('split_method')
                                cv = request.POST.get('cv')
                                valid_size = request.POST.get('valid_size')
                                test_size = request.POST.get('test_size')
                                random_state = request.POST.get('random_state')
                                
                                model_id = request.POST.get('model_id')
                                model_name = request.POST.get('model_name')
                                model_type = request.POST.get('model_type')
                                
                                
                                basic_split_parameters = {'model_mode': model_mode, 'split_method': split_method ,
                                                           'cv': cv, 'valid_size': valid_size, 'test_size': test_size,
                                                           'random_state': random_state}
                                
                                split_dataset = ModelObject.split_dataset((basic_split_parameters))
                                
                                
                                
                except Exception as e:
                        logging.error(": : POST Method : Exception :" + str(e))
                        logging.error(": : POST Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

        
# class SelectAlgorithmClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get Learning Curve of project uploaded uploaded by te user.
        
#                 Args  : 
#                         algorithm_name[(String)]   :[Name of Algorithm]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         algorithm_name  = request.query_params.get('algorithm_name') #get Username
#                         project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                
                
               

# class LearningCurveClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get Learning Curve of project uploaded uploaded by te user.
        
#                 Args  : 
#                         experiment_id[(Integer)]   :[Id of Experiment]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         experiment_id  = request.query_params.get('experiment_id') #get Username
#                         project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                
                
# class FeatureImportanceClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get FeatuImportance of project uploaded uploaded by te user.
        
#                 Args  : 
#                         experiment_id[(Integer)]   :[Id of Experiment]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         experiment_id  = request.query_params.get('experiment_id') #get Username
#                         project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

# class PerformanceMetricsClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get PerformanceMetrics of project uploaded uploaded by te user.
        
#                 Args  : 
#                         experiment_id[(Integer)]   :[Id of Experiment]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         experiment_id  = request.query_params.get('experiment_id') #get Username
#                         project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                
# class ModelSummaryClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get model summary of project uploaded uploaded by te user.
        
#                 Args  : 
#                         experiment_id[(Integer)]   :[Id of Experiment]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         experiment_id  = request.query_params.get('experiment_id') #get Username
#                         project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

# class ActualVsPredictionClass(APIView):

#         def get(self, request, format=None):
#                 """
#                 This function is used to get Actual and Predicated value of project uploaded uploaded by te user.
        
#                 Args  : 
#                         experiment_id[(Integer)]   :[Id of Experiment]
#                 Return : 
#                         status_code(500 or 200),
#                         error_msg(Error message for retrival & insertions failed or successfull),
#                         Response(return false if failed otherwise json data)
#                 """
#                 try:
#                         logging.info(" : ModelClass : GET Method : execution start")
#                         experiment_id  = request.query_params.get('experiment_id') #get Username
#                         #project_df = IngestionObj.show_project_details(user_name) #call show_project_details to retrive project detail data and it will return dataframe
#                         if isinstance(project_df,str): #check the instance of dataset_df
#                                 status_code,error_msg=get_Status_code(project_df) # extract the status_code and error_msg from project_df
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
#                                 return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
#                         else:
#                                 logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
#                                 return Response({"status_code":"200","error_msg":"successfull retrival","response":project_df})  

#                 except Exception as e:
#                         logging.error(" modeling : ModelingClass : GET Method : " + str(e))
#                         logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
#                         return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                                
                                
