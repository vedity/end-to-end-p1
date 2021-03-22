'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''
import numpy as np
import pandas as pd
import json
import mlflow
import mlflow.sklearn
import uuid
import logging
import requests

from .regression.regression_model import RegressionClass as RC
from .classification.classification_model import ProbabilisticClass as PC
from common.utils.logger_handler import custom_logger as cl
from modeling.algorithm_detector import AlgorithmDetector
from modeling.split_data import SplitData

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('model_identifier')

class SupervisedClass(RC,PC):
   
    def supervised_algorithm(self,model_param_dict,db_param_dict):
        
        """This function is used to call supervised algorithm.
        """
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution start")
        
       
        AlgorithmDetectorObject = AlgorithmDetector(db_param_dict)
        
        project_id=model_param_dict['project_id']
        dataset_id = model_param_dict['dataset_id']
        
        model_type_dict = AlgorithmDetectorObject.get_model_type(project_id,dataset_id)
        
        model_param_dict['algorithm_type'] = model_type_dict['algorithm_type']
        model_param_dict['target_type'] = model_type_dict['target_type']
        
        if model_param_dict['model_type'] == "Regression" :
            # Call Regression Class's method
            super(SupervisedClass,self).regression_model(model_param_dict,db_param_dict)                                  
        else:
            # Call Probabilistic Class's method
            super(SupervisedClass,self).classification_model(model_param_dict,db_param_dict)
            
        logging.info("modeling : SupervisedClass : supervised_algorithm : execution end")
        
        
    def run_supervised_model(self,model_param_dict,db_param_dict,model_id,model_name,model_param):
        
        logging.info("modeling : SupervisedClass : run_regression_model : execution start") 
        # Call the super class method.
        
        dag_id = self.get_dag_id(model_param_dict,db_param_dict)
        
        #TODO this will get from front end
        model_id = [model_id]
        model_name = [model_name]
        model_param = [model_param]
    
        template = "manual_model_dag.template"
        namespace = "manual_modeling_dags"
        
        master_dict = {"model_id": model_id,"model_name": model_name,"model_param": model_param}
        
        json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
        result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner
        
        json_data = {'conf':'{"model_param_dict":"'+str(model_param_dict)+'"}'}
        result = requests.post(f"http://airflow:8080/api/experimental/dags/{dag_id}/dag_runs",data=json.dumps(json_data),verify=False)#owner
        
        logging.info("dag run result: "+str(result))
        logging.info("modeling : SupervisedClass : run_supervised_model : execution end")
        
    
    def get_dag_id(self,model_param_dict,db_param_dict):
        
        project_id = model_param_dict['project_id']     
        DBObject = db_param_dict['DBObject']
        connection = db_param_dict['connection']
        
        sql_command = "select model_dag_id from mlaas.project_tbl where project_id="+str(project_id)
        dag_id_df = DBObject.select_records(connection,sql_command) 
        dag_id = dag_id_df['model_dag_id'][0]
        
        return dag_id


         
        
        
        
   
    