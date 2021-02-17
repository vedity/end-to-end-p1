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
from modeling.model_statistics import *

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')


  

DBObject=db.DBClass()     #Get DBClass object
connection,connection_string=DBObject.database_connection(database,user,password,host,port)      #Create Connection with postgres Database which will return connection object,conection_string(For Data Retrival)

ModelStatObject = ModelStatisticsClass(DBObject,connection)

#################### DO NOT CHANGE THIS AT THIS POINT ################

Model_Mode ="auto"
project_id,dataset_id,user_id = 2,2,2
input_features_list = ['index','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']  
target_features_list = ['index','price'] 

###############




class ShowDatasetInfoClass(APIView):
        
        def get(self,request,format=None):
                """
                This function is used to show Project Name, Dataset name and List of Target Columns which are uploaded user.

                Args  : 
                        project_id[(String)] :[Id of project]
                        dataset_id[(String)] :[Id of dataset]
                                

                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for deletion failed or successfull),
                        Response(false or true)
                """
                try:

                        logging.info(": : POST Method : execution start")
                        
                        
                        project_id = request.query_params.get('project_id')
                        dataset_id = request.query_params.get('dataset_id')
                        user_id=request.query_params.get('user_id')
                        
                        ModelObject = ModelClass(Model_Mode,
                                        input_features_list,
                                        target_features_list,
                                        project_id,
                                        dataset_id, 
                                        user_id,
                                        DBObject,
                                        connection, 
                                        connection_string)
                        
                        project_name, dataset_name, target_columns = ModelObject.get_dataset_info()
                        
                        show_dataset_info_dictionary = {"project_name":project_name,
                                                        "dataset_name":dataset_name,
                                                        "target_columns":target_columns
                                                        }
                        
                        
                        if show_dataset_info_dictionary:
                                
                                logging.info("modeling : ModelClass : GET Method : execution stop : status_code :200")
                                return Response({"status_code":"200","error_msg":"Successfully updated","response":show_dataset_info_dictionary})
                        else:
                                logging.info("modeling : ModelClass : GET Method : execution stop : status_code :"+500)
                                return Response({"status_code":"500","error_msg":"Error","response":"false"})   
                                
                except Exception as e:
                        logging.error("modeling : ModelClass : GET Method : Exception :" + str(e))
                        logging.error("modeling : ModelClass : GET Method : " +traceback.format_exc())
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
                try:

                        ModelObject = ModelClass(Model_Mode,input_features_list,
                                                target_features_list,project_id,dataset_id,user_id,
                                                DBObject,connection,connection_string)
                        
                        logging.info("modeling : ExperimentClass : GET Method : execution start")
                        # model_mode =request.query_params.get('model_mode')
                        
                        
                        if Model_Mode == 'auto':
                                
                                basic_split_parameters = {'model_mode': 'auto'}
                                # SplitDataObject = ModelObject.split_dataset(basic_split_parameters)
                                ModelObject.algorithm_identifier(basic_split_parameters)
                                logging.info("modeling : ModelClass : GET Method : execution stop : status_code :200")
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
                        logging.error("mdeling : ModelClass : GET Method : Exception :" + str(e))
                        logging.error(": : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})

#class to get learning curve
#It will take url string as mlaas/modeling/learning_curve/.
class LearningCurveClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Learning Curve of project uploaded uploaded by te user.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" modeling : ExperimentClass : GET Method : execution start")
                        
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        
                        learning_curve_json =ModelStatObject.learning_curve(experiment_id)
                        logging.info("modeling : ExperimentClass : GET Method : execution stop : status_code :200")
                      
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":learning_curve_json})

                except Exception as e:
                        logging.error(" modeling : ExperimentClass : GET Method : " + str(e))
                        logging.error(" modeling : ExperimentClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
                
#class to get feature importance
#It will take url string as mlaas/modeling/featureimportance/.                
class FeatureImportanceClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get FeatuImportance of particular experiment.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                
                        logging.info(" modeling : ExperimentClass : GET Method : execution start")
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        feature_importance_json =ModelStatObject.features_importance(experiment_id)
                        logging.info(" modeling : ExperimentClass : GET Method : execution stop : status_code :200")
                       
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":feature_importance_json})
                        
                except Exception as e:
                        logging.error(" modeling : ExperimentClass : GET Method : " + str(e))
                        logging.error("data ingestion : ExperimentClass : GET Method : " +traceback.format_exc())
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
                        logging.info(" modeling : ExperimentClass : GET Method : execution start")
                        experiment_id  = request.query_params.get('experiment_id') #get Username
                        performance_metrics_json =ModelStatObject.performance_metrics(experiment_id)
                        logging.info("modeling : ExperimentClass : GET Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":performance_metrics_json})
                        
                except Exception as e:
                        logging.error(" modeling : ExperimentClass : GET Method : " + str(e))
                        logging.error(" modeling : ExperimentClass : GET Method : " +traceback.format_exc())
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
                       
                        logging.info(" modeling : ExperimentClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        model_summary_json =ModelStatObject.model_summary(experiment_id)
                        logging.info("modeling : ExperimentClass : GET Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":model_summary_json})
                        
                except Exception as e:
                        logging.error(" modeling : ExperimentClass : GET Method : " + str(e))
                        logging.error(" modeling : ExperimentClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

#class to get actual vs prediction 
#It will take url string as mlaas/modeling/actualvsprediction/. 
class ActualVsPredictionClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Actual VS Predicated value of particular experience
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                       
                        logging.info(" modeling : ExperimentClass : GET Method : execution start")
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        actual_vs_prediction_json =ModelStatObject.actual_vs_prediction(experiment_id)
                        logging.info(" modeling : ExperimentClass : GET Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":actual_vs_prediction_json})
                        

                except Exception as e:
                        logging.error(" modeling : ExperimentClass : GET Method : " + str(e))
                        logging.error(" modeling : ExperimentClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  

class FinalModelDescriptionClass(APIView):

        def post(self, request, format=None):
                """
                This function is used to get PerformanceMetrics of project uploaded uploaded by te user.
        
                Args  : 
                        experiment_id[(Integer)]   :[Id of Experiment]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        logging.info(" : ModelClass : GET Method : execution start")
                        
                        experiment_id = request.query_params.get('experiment_id') #get Username
                        
                        model_details_json,accuracy_json =ModelStatObject.show_model_details(experiment_id)
                        
                        logging.info(": : POST Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":(model_details_json,accuracy_json)})
                        
                except Exception as e:
                        logging.error(" modeling : ModelingClass : GET Method : " + str(e))
                        logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  


class SelectAlgorithmClass(APIView):

        def get(self, request, format=None):
                """
                This function is used to get Learning Curve of project uploaded uploaded by te user.
        
                Args  : 
                        algorithm_name[(String)]   :[Name of Algorithm]
                Return : 
                        status_code(500 or 200),
                        error_msg(Error message for retrival & insertions failed or successfull),
                        Response(return false if failed otherwise json data)
                """
                try:
                        
                        
                        ModelObject = ModelClass(Model_Mode,input_features_list,
                                                target_features_list,project_id,dataset_id,user_id,
                                                DBObject,connection,connection_string)
                        
                        logging.info(" : ModelClass : GET Method : execution start")
                        # experiment_id = request.query_params.get('experiment_id') #get Username
                        models_list = ModelObject.show_model_list()
                        logging.info(": : POST Method : execution stop : status_code :200")
                        # print(learning_curve_json)
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":models_list})
                        
                except Exception as e:
                        logging.error(" modeling : ModelingClass : GET Method : " + str(e))
                        logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  


#class to start and stop model
#It will take url string as mlaas/modeling/featureimportance/.                                 
class HyperParametersClass(APIView):

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
                        ModelObject = ModelClass(Model_Mode,input_features_list,
                                                target_features_list,project_id,dataset_id,user_id,
                                                DBObject,connection,connection_string)
                        
                        logging.info(" : ModelClass : GET Method : execution start")
                        model_name  = request.query_params.get('model_name') #get Username 
                        hyperparameters_json = ModelObject.get_hyperparameters_list(model_name)
                        logging.info(": : POST Method : execution stop : status_code :200")
                        return Response({"status_code":"200","error_msg":"Successfully updated","response":hyperparameters_json})
                        

                except Exception as e:
                        logging.error(" modeling : ModelingClass : GET Method : " + str(e))
                        logging.error("data ingestion : ModelingClass : GET Method : " +traceback.format_exc())
                        return Response({"status_code":"500","error_msg":str(e),"response":"false"})  
