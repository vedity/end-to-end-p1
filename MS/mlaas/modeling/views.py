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
from modeling.split_data import *
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

db_param_dict = {'DBObject':DBObject,'connection':connection,'connection_string':connection_string}

AlgorithmDetectorObj = AlgorithmDetector(db_param_dict)

ModelStatObject = ModelStatisticsClass(db_param_dict)

json_obj = JsonFormatClass()

SplitObject = SplitData()

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
                        
                       
                        project_id = request.query_params.get('project_id')#get project id
                        dataset_id = request.query_params.get('dataset_id')#get dataset id
                        user_id=request.query_params.get('user_id')#get user id

                        
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
                        project_id[(String)] :[Id of project]
                        dataset_id[(String)] :[Id of dataset]
                        user_name[(String)] :[name of user]
                        model_type[(String)] : [Type of Model (Regression/Classification)]
                        experiment_name[(String)] :[name of experiment]
                                
 
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                        
                """
                try:
                        logging.info("modeling : StartModelClass : POST Method : execution start")
                        # We will get it from the front-end
                        model_mode = request.query_params.get('model_mode')#get model_mode
                        model_name = request.query_params.get('model_name')#get model_mode
                        user_name = request.query_params.get('user_name')#get user name
                        user_id = 1 # get user id from user auth table
                        project_id = int(request.query_params.get('project_id'))#get project id
                        dataset_id = int(request.query_params.get('dataset_id'))#get dataset id
                        model_type = request.query_params.get('model_type')#model_type
                        experiment_name = request.query_params.get('experiment_name')#experiment_name
                        experiment_desc ='this is for testing'

                        #will store created experiment activity in activity_detail_tbl
                        activity_id = 'md_41'
                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)
                        

                        #will store started experiment activity in activity_detail_tbl
                        activity_id = 'md_45'
                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)
                        
                        ModelObject = ModelClass(db_param_dict)# Initializing the ModelClass

                        basic_params_dict = {'model_mode':model_mode,'model_type':model_type,
                                             'experiment_name':experiment_name,'experiment_desc':experiment_desc,
                                             'user_id':user_id,'project_id':project_id,'dataset_id':dataset_id}
                        
                        # Check Model Requirement
                        model_req_status = AlgorithmDetectorObj.check_model_requirements(project_id)
                        
                        if model_req_status == True:

                                if model_mode == 'Auto':
                                        #will add 'Selected Auto modeling' activity in activity_detail_tbl 
                                        activity_id = 'md_42'
                                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)

                                        result = ModelObject.algorithm_identifier(basic_params_dict)
                                        
                                        if result.status_code != 200:
                                                # status_code,error_msg=json_obj.get_Status_code(learning_curve_json) # extract the status_code and error_msg from project_df
                                                logging.info("modeling : StartModelClass : GET Method : execution : status_code :"+ result)
                                                return Response({"status_code":result.status_code,"error_msg":str(result.content, 'UTF-8'),"response":"false"})

                                        logging.info("modeling : StartModelClass : GET Method : execution stop : status_code :200")
                                        return Response({"status_code":"200","error_msg":"Successfully updated","response":"pipeline started"})
                                
                                else:
                                        #will add 'selected manual modeling' activity in activity_detail_tbl
                                        model_id = int(request.query_params.get('model_id'))
                                        model_name = request.query_params.get('model_name') #ASK
                                        activity_id = 'md_43'
                                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)

                                        activity_id = 'md_44'
                                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name,model_name)

                                        data = json.dumps(request.data)
                                        request_body = json.loads(data) #get all the request body parameter
                                        
                                        model_hyperparams = request_body["hyperparameters"]
                                        
                                        
                                        result = ModelObject.run_model(basic_params_dict,model_id,model_name,model_hyperparams)

                                        if result.status_code != 200:
                                                # status_code,error_msg=json_obj.get_Status_code(learning_curve_json) # extract the status_code and error_msg from project_df
                                                logging.info("modeling : StartModelClass : GET Method : execution : status_code :"+ result)
                                                return Response({"status_code":result.status_code,"error_msg":str(result.content, 'UTF-8'),"response":"false"})
                                        
                                        logging.info("modeling : StartModelClass : GET Method : execution stop : status_code :200")
                                        return Response({"status_code":"200","error_msg":"Successfully updated","response":"True"})
                                
                        else:
                                logging.info("modeling : StartModelClass : GET Method : execution : error_msg :"+ model_req_status)
                                return Response({"status_code":"500","error_msg":model_req_status,"response":"false"})
                                
                                
                except Exception as e:
                        logging.error("modeling : StartModelClass : GET Method : Exception :" + str(e))
                        logging.error("modeling : StartModelClass : GET Method : " +traceback.format_exc())
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
                        
                        experiment_id  = request.query_params.get('experiment_id') #get experiment id
                        
                        learning_curve_json =ModelStatObject.learning_curve(experiment_id)#call learning curve method which will return train size,test size and test score
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
                        experiment_id  = request.query_params.get('experiment_id') #get experiment id
                        feature_importance_json =ModelStatObject.features_importance(experiment_id)# will call feature_importance method which will return features names and norm importance
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
                        experiment_id  = request.query_params.get('experiment_id') #get experiment id
                        performance_metrics_json =ModelStatObject.performance_metrics(experiment_id)#will call performance metrics meethod
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
                        experiment_id = request.query_params.get('experiment_id') #get experiment_id
                        model_summary_json =ModelStatObject.model_summary(experiment_id)#will call model_summary method which will return summary of model
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
                        experiment_id = request.query_params.get('experiment_id') #get experiment_id
                        model_type = request.query_params.get('model_type') #get model_type
                        actual_vs_prediction_json =ModelStatObject.actual_vs_prediction(experiment_id,model_type)#will call actual_vs_prediction method
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
                This function is used to get Confusion Matrix of particular experiement
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get experiment_id
                        confusion_matrix_json = ModelStatObject.show_confusion_matrix(experiment_id)# will call confusion matrix method
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        if isinstance(confusion_matrix_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(confusion_matrix_json) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":confusion_matrix_json})
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":json.loads(confusion_matrix_json)})
                        

                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  


class ROCCurveClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Confusion Matrix of particular experiement
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get experiment_id
                        roc_curve_json = ModelStatObject.show_roc_curve(experiment_id)# will call confusion matrix method
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        if isinstance(roc_curve_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(roc_curve_json) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":roc_curve_json})
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":json.loads(roc_curve_json)})
                        

                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  



#class to get actual vs prediction 
#It will take url string as mlaas/modeling/actualvsprediction/.
class ShowRunningExperimentsListClass(APIView):
        def get(self, request, format=None):
                """
                This function is used to get running experiment of particular project.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id'))#get project id
                        experiment_data =ModelStatObject.show_running_experiments(project_id)# will call show_running_experiments
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


                
#class to get all experiment list 
#It will take url string as mlaas/modeling/showallexperimentslist/.              
class ShowAllExperimentsListClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get all Experiment.
        
                Args  : 
                        project_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id'))# get project id
                
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
                
#class to get all experiment list 
#It will take url string as mlaas/modeling/checkmodelstatus/.                          
class CheckModelStatusClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to check status of particular model.
        
                Args  : 
                        experiment_name[(String)]   :[Name of Experiment]
                        project_id[(Integer)]   :[Id of project]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id')) #get Username
                        dataset_id = int(request.query_params.get('dataset_id')) #get Username
                        experiment_name = request.query_params.get('experiment_name')
                        user_name = request.query_params.get('user_name')
        
                        experiment_status = ModelStatObject.check_model_status(project_id,experiment_name)
                        # if len(experiment_data) != 0:
                        # if isinstance(experiment_data, pd.DataFrame):
                        #         status = experiment_data['state'][0]
                        if isinstance(experiment_status,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(experiment_status) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                if experiment_status == 0:
                                        status = 'running'
                                elif experiment_status == 1:
                                        status = 'success'
                                else:
                                        status = 'failed'

                                if(status == 'success'):
                                        #will add 'Completed modeling' activity in activity_detail_tbl
                                        activity_id = 'md_47'
                                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)
                                elif(status == 'failed'):
                                        logging.info('LOG FOR Failed status----------------------------------')
                                        activity_id = 'md_48'
                                        timeline_Obj.user_activity(activity_id,experiment_name,project_id,dataset_id,user_name)
                                        
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":status})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})



class RefreshModelingPageClass(APIView):
        def get(self, request, format=None):
                """
                This function is used to check whether an experiment is running for a given project_id.
        
                Args  : 
                        project_id[(Integer)]   :[Id of Project]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = int(request.query_params.get('project_id'))#get project id
                        dataset_id = int(request.query_params.get('dataset_id'))#get dataset id
                        exp_name = ModelStatObject.refresh_modeling(project_id, dataset_id)# will call show_running_experiments
                        if isinstance(exp_name, str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(exp_name) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":exp_name})
                       
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":exp_name})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})



#class to get all experiment list 
#It will take url string as mlaas/modeling/selectalgorithm/.                          
class SelectAlgorithmClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get algorithm list.
        
                Args  : 
                        model_type[(String)]   :[Type of model]
                        project_id[(Integer)]   :[Id of project]
                        dataset_id[(Integer)]   :[Id of dataset]
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
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  


#class to show hyperparameters
#It will take url string as mlaas/modeling/hyperparameters/.                                 
class ShowHyperParametersClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get HyperParameters 
        
                Args  : 
                        model_id[(Integer)]   :[Id of Model]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        model_id  = request.query_params.get('model_id')
                        hyperparams_dict = AlgorithmDetectorObj.get_hyperparameters(model_id)

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

#class to show experiments list for comparision
#It will take url string as mlaas/modeling/compareexperiments/.                                 
class CompareExperimentsGridClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get all Experiment to compare
        
                Args  : 
                        experiment_ids[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_ids = tuple(json.loads(request.query_params.get('experiment_ids')))
 
                        experiment_data = ModelStatObject.compare_experiments_grid(experiment_ids)
                        
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

#class to check experiment name already exist or not
class CheckExperimentNameClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to check name of particular experiment exist or not
        
                Args  : 
                        experiment_name[(Integer)]   :[Id of Experiment]
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
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})                        


class CheckRunningExperimentsClass(APIView):
        
        def get(self, request, format=None):
                """
                This function is used to check name of particular experiment exist or not
        
                Args  : 
                        experiment_name[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = request.query_params.get('project_id')
 
                        experiment_data = ModelStatObject.check_running_experiments(project_id)

                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200"+str(experiment_data))
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



#class to show experiments list for comparision
#It will take url string as mlaas/modeling/compareexperiments/.                                 
class CompareExperimentsGraphClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get all Experiment to compare
        
                Args  : 
                        experiment_ids[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_ids = tuple(json.loads(request.query_params.get('experiment_ids')))
 
                        experiment_data = ModelStatObject.compare_experiments_graph(experiment_ids)
                        
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":experiment_data})
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

class ModelTypeClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get regression or classification type'
        
                Args  : 
                        project_id[(Integer)]   :[Id of Project]
                        dataset_ids[(Integer)]   :[Id of Dataset]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = request.query_params.get('project_id')

                        dataset_id = request.query_params.get('dataset_id')
 

                        model_type = AlgorithmDetectorObj.get_model_type(project_id,dataset_id)
                        if isinstance(model_type,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(model_type) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":model_type})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})


class GetSplitDataClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to get regression or classification type'
        
                Args  : 
                        project_id[(Integer)]   :[Id of Project]
                        dataset_ids[(Integer)]   :[Id of Dataset]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        project_id = request.query_params.get('project_id')

                        dataset_id = request.query_params.get('dataset_id')

                        scaled_data = SplitObject.get_scaled_split_dict(DBObject,connection,project_id,dataset_id)

                        train_X,valid_X,test_X,train_y,valid_y,test_y,actual_y = SplitObject.get_scaled_data(scaled_data)

                        data = {"train_X":train_X,"valid_X":valid_X,"test_X":test_X,"train_y":train_y,"valid_y":valid_y,"test_y":test_y,"actual_y":actual_y}
                        if isinstance(data,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(data) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":data})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

class ModelFailedClass(APIView):
 
        def get(self, request, format=None):
                """
                This function is used to check model is failed or not'
        
                Args  : 
                        experiment_ids[(Integer)]   :[Id of Experiment]
                
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        
                        experiment_id = request.query_params.get('experiment_id')

                        model_type = ModelStatObject.model_failed(experiment_id)
                        if isinstance(model_type,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(model_type) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":model_type})
                        
                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})


class PDPCurveClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Confusion Matrix of particular experiement
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution start")
                        experiment_id = int(request.query_params.get('experiment_id')) #get experiment_id
                        project_id = int(request.query_params.get('project_id')) #get project_id
                        feature = request.query_params.get('feature') #get feature selected by the user
                        sclass = request.query_params.get('sclass') #get the class selected by the user.
                        roc_curve_json = ModelStatObject.show_partial_dependence_plot(project_id, experiment_id, feature, sclass)# will call confusion matrix method
                        logging.info(" modeling : ModelStatisticsClass : GET Method : execution stop : status_code :200")
                        if isinstance(roc_curve_json,str): #check the instance of dataset_df
                                status_code,error_msg=json_obj.get_Status_code(roc_curve_json) # extract the status_code and error_msg from project_df
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code :"+ status_code)
                                return Response({"status_code":status_code,"error_msg":error_msg,"response":"false"})
                        else:
                                logging.info("modeling : ModelStatisticsClass : GET Method : execution : status_code : 200")
                                return Response({"status_code":"200","error_msg":"successfull retrival","response":roc_curve_json})
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":json.loads(roc_curve_json)})
                        

                except Exception as e:
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " + str(e))
                        logging.error(" modeling : ModelStatisticsClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
