from django.shortcuts import render
import json
import requests
import logging
import traceback
import pandas as pd
import ast
import datetime
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
from modeling.model_statistics import *
from common.utils.activity_timeline import *
from common.utils.activity_timeline import activity_timeline
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')

timeline_Obj=activity_timeline.ActivityTimelineClass(database,user,password,host,port) #initialize the ActivityTimeline Class
json_obj = JsonFormatClass() #initialize the JsonFormat Class 

DBObject=db.DBClass()     #Get DBClass object
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)

AlgorithmDetectorObj = AlgorithmDetector(DBObject, connection)

ModelStatObject = ModelStatisticsClass(DBObject,connection)

json_obj = JsonFormatClass()

class ShowDatasetInfoClass(APIView):
        
        def get(self,request,format=None):
                """
                This function is used to show Project Name, Dataset name and List of Target Columns which are uploaded user.

                Args  : 
                        project_id[(String)] :[Id of project]
                        dataset_id[(String)] :[Id of dataset]
                        user_id[(String)] :[Id of user] 
                                

                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                """
                try:

                        logging.info("modeling : ModelStatisticsClass : GET Method : execution start")
                        
                       
                        project_id = request.query_params.get('project_id')
                        dataset_id = request.query_params.get('dataset_id')
                        user_id=request.query_params.get('user_id')

                        
                        project_name, dataset_name, target_columns = AlgorithmDetectorObj.get_dataset_info(project_id, dataset_id, user_id)
                        
                        show_dataset_info_dictionary = {"project_name":project_name,
                                                        "dataset_name":dataset_name,
                                                        "target_columns":target_columns
                                                        }
                        
                        
                        if isinstance(show_dataset_info_dictionary,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(show_dataset_info_dictionary) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":show_dataset_info_dictionary})
                                
                except Exception as e:
                        logging.error("modeling : ModelStatisticsClass : GET Method : Exception :" + str(e))
                        logging.error("modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

                
class StartModelClass(APIView):
        def post(self,request,format=None):
                """
                This function is used to get  model mode selected by user and will start running model according to model mode.
 
                Args  : 
                        mode[(String)] :[mode of model]
                                
 
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                        
                """
                try:
                        logging.info("modeling : ExperimentClass : GET Method : execution start")
                        # We will get it from the front-end
                        Model_Mode = request.query_params.get('model_mode')
                        # NEED TO GET USER ID
                        user_name = request.query_params.get('user_name')
                        user_id = 1 # get user id from user auth table
                        project_id = int(request.query_params.get('project_id'))
                        dataset_id = int(request.query_params.get('dataset_id'))
                        model_type = request.query_params.get('model_type')
                        
                        experiment_name = request.query_params.get('experiment_name')
                        experiment_desc ='this is for testing'

                        # activity_id = 46
                        # activity_df = timeline_Obj.get_activity(activity_id,"US")
                        # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                        # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                        # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 
                
                        # activity_id = 42
                        # activity_df = timeline_Obj.get_activity(activity_id,"US")
                        # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                        # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                        # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 
                        
                        ModelObject = ModelClass(Model_Mode,user_id, project_id,dataset_id,
                                                DBObject,connection,connection_string)# Initializing the ModelClass

                        if Model_Mode == 'Auto': 
                                # activity_id = 43
                                # activity_df = timeline_Obj.get_activity(activity_id,"US")
                                # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                                # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                                # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 
                                # # SplitDataObject = ModelObject.split_dataset(basic_split_parameters)
                                ModelObject.algorithm_identifier(model_type,experiment_name,experiment_desc)
                                

                                # activity_id = 48
                                # activity_df = timeline_Obj.get_activity(activity_id,"US")
                                # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                                # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                                # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 

                                logging.info("modeling : ModelClass : GET Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":"pipeline started"})
                        else:
                                # activity_id = 44
                                # activity_df = timeline_Obj.get_activity(activity_id,"US")
                                # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                                # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                                # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time)
                                model_id = int(request.query_params.get('model_id'))
                                # hyperparameters = request.query_params.get('hyperparameters')
                                if model_id == 2:
                                        hyperparameters = {"epochs": 10, "learning_rate": 0.01, "batch_size": 32, "loss": "mean_absolute_error", "optimizer": "Adam", 
                                                "activation": "relu"}
                                else:
                                        hyperparameters = ""
                                
                                ModelObject = ModelClass(Model_Mode,user_id, project_id,dataset_id,
                                                DBObject,connection,connection_string)
                                
                                manual_model_params_dict = {'model_id':model_id, 'hyperparameters': hyperparameters,
                                                        'experiment_name': experiment_name}

                                ModelObject.store_manual_model_params(manual_model_params_dict)
                                # model_type = 'Regression'
                                ModelObject.run_model(model_type, model_id, experiment_name, experiment_desc)

                                # activity_id = 48
                                # activity_df = timeline_Obj.get_activity(activity_id,"US")
                                # activity_description = "{x} '{y}'".format(x=activity_df[0]["activity_description"],y= experiment_name)
                                # end_time = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                                # activity_status,index = timeline_Obj.insert_user_activity(activity_id,user_name,project_id,str(dataset_id),activity_description,end_time) 

                                logging.info("modeling : ModelClass : GET Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":"True"})
                                
                                
                except Exception as e:
                        logging.error("mdeling : ModelClass : GET Method : Exception :" + str(e))
                        logging.error("modeling : ModelClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

#class to get learning curve
#It will take url string as mlaas/modeling/learning_curve/.
class LearningCurveClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Learning Curve of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        
                        learning_curve_json =ModelStatObject.learning_curve(experiment_id)
                        logging.info("modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        if isinstance(learning_curve_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(learning_curve_json) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":learning_curve_json})                   

                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                
#class to get feature importance
#It will take url string as mlaas/modeling/featureimportance/.                
class FeatureImportanceClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get FeatureImportance of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        feature_importance_json =ModelStatObject.features_importance(experiment_id)
                        if isinstance(feature_importance_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(feature_importance_json) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution stop: status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution stop: status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":feature_importance_json})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

#class to get performance metrics
#It will take url string as mlaas/modeling/performancemetrics/. 
class PerformanceMetricsClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        performance_metrics_json =ModelStatObject.performance_metrics(experiment_id)
                        logging.info("modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        if isinstance(performance_metrics_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(performance_metrics_json) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":performance_metrics_json})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

#class to get model summary
#It will take url string as mlaas/modeling/modelsummary/.                 
class ModelSummaryClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get model summary of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data).
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        model_summary_json =ModelStatObject.model_summary(experiment_id)
                        logging.info("modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        if isinstance(model_summary_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(model_summary_json) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":model_summary_json})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

#class to get actual vs prediction 
#It will take url string as mlaas/modeling/actualvsprediction/. 
class ActualVsPredictionClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Actual VS Predicated value of particular experiement
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        actual_vs_prediction_json =ModelStatObject.actual_vs_prediction(experiment_id)
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        if isinstance(actual_vs_prediction_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(actual_vs_prediction_json) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":actual_vs_prediction_json})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  



#It will take url string as mlaas/modeling/actualvsprediction/. 
class ConfusionMatrixClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Actual VS Predicated value of particular experiement
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        confusion_matrix_json = ModelStatObject.confusion_matrix(experiment_id)
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        # if isinstance(confusion_matrix_json,str): #check the instance of dataset_df
                        #         status_code,error_msg=json_obj.get_Status_code(confusion_matrix_json) # extract the status_code and error_msg from project_df
                        #         logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                        #         return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        # else:
                        #         logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                        #         return Response({"status_code":"200","error_msg":"successfull retrival","response":confusion_matrix_json})
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":json.loads(confusion_matrix_json)})
                        

                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  



class ShowRunningExperimentsListClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiement.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id')) 
                        experiment_data =ModelStatObject.show_running_experiments(project_id)
                        if isinstance(experiment_data,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(experiment_data) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":experiment_data})
                       
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":experiment_data})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
                
                
class ShowAllExperimentsListClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id')) 
                
                        experiment_data =ModelStatObject.show_all_experiments(project_id)
                        if isinstance(experiment_data,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(experiment_data) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":experiment_data}) 
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})
                
                
class CheckModelStatusClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to check status of particular model.
        
                Args  : 
                        experiment_name[(String)]   :[Name of Experiment]
                        project_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id')) #get Username
                        
                        experiment_name = request.query_params.get('experiment_name')
        
                        model_status = ModelStatObject.check_model_status(project_id,experiment_name)
                        if model_status == 0:
                                status = 'running'
                        elif model_status == 1:
                                status = 'success'
                        else:
                                status = 'failed'
                        # status = experiment_data['state'][0]
                        if isinstance(model_status,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(model_status) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                # status = experiment_data['state'][0]
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":status})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})



class SelectAlgorithmClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to show list of models.
        
                Args  : 
                        algorithm_name[(String)]   :[Name of Algorithm]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        
                        project_id = int(request.query_params.get('project_id'))
                        dataset_id = int(request.query_params.get('dataset_id'))
                        model_type = request.query_params.get('model_type')
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        # experiment_id = request.query_params.get('experiment_id') #get Username
                        models_list = AlgorithmDetectorObj.show_models_list(project_id,dataset_id,model_type)

                        # print(learning_curve_json)
                        if isinstance(models_list,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(models_list) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":models_list})
                        #return Response({"status_code":"200","error_msg":"Successfully updated","response":models_list})
                        
                except Exception as e:
                        logging.error(" modelinggggggg : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  


#class to start and stop model
#It will take url string as mlaas/modeling/featureimportance/.                                 
class ShowHyperParametersClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Actual and Predicated value of project uploaded uploaded by te user.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        model_id  = request.query_params.get('model_id')
                        hyperparams_dict = AlgorithmDetectorObj.get_hyperparameters(model_id)
                        # h1 = hyperparameters_json.to_json(orient='records',date_format='iso')
                        # logging.info("aaaaaaaaa"+str(h1))
                        # x = '[ "A","B","C" , " D"]'
                        # if hyperparams != 'none':
                        #         hyperparams = ast.literal_eval(hyperparams)

                        # hyperparams_dict = {'model_parameters': hyperparams}
                        if isinstance(hyperparams_dict,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(hyperparams_dict) # extract the status_code and error_msg from project_df
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("data ingestion : CreateProjectClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":hyperparams_dict})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

                        
class CompareExperimentsClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_ids = tuple(json.loads(request.query_params.get('experiment_ids')))
 
                        experiment_data = ModelStatObject.compare_experiments(experiment_ids)
                        
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

class CheckExperimentNameClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_name = request.query_params.get('experiment_name')

                        project_id = request.query_params.get('project_id')
 
                        experiment_data = ModelStatObject.check_existing_experiment(project_id, experiment_name)
                        
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200"+str(experiment_data))
                        if isinstance(experiment_data,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(experiment_data) # extract the status_code and error_msg from project_df
                                logging.info(" -------"+str(status_code))
                                logging.info(" -------"+str(error_msg))
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})                        




class RoughAPI(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_id = request.query_params.get('experiment_id')

                        # project_id = request.query_params.get('project_id')
 
                        experiment_data = ModelStatObject.per_met(experiment_id)
                        
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200"+str(experiment_data))
                        if isinstance(experiment_data,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(experiment_data) # extract the status_code and error_msg from project_df
                                logging.info(" -------"+str(status_code))
                                logging.info(" -------"+str(error_msg))
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})                        