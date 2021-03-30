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
import time

from .regression.regression_model import RegressionClass as RC
from .classification.classification_model import ProbabilisticClass as PC
from common.utils.logger_handler import custom_logger as cl
from modeling.algorithm_detector import AlgorithmDetector
from modeling.split_data import SplitData

from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
from common.utils import dynamic_dag


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
        file_name = dag_id + '.py'
        master_dict = {"model_id": model_id,"model_name": model_name,"model_param": model_param}
        

        status = self.dag_updater(master_dict, file_name, namespace)
        if not isinstance(status,int):
            logging.error(f"Dag Updation Failed : Error : {str(status)}")
            raise DagUpdateFailed(500)


        # json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
        # result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

        
        # time.sleep(10)

        # sql_command = "select run_id from dag_run where dag_id='dag_creator' and state='running' order by start_date desc limit 1"
        # DBObject = db_param_dict['DBObject']
        # connection = db_param_dict['connection']
        # run_id = DBObject.select_records(connection, sql_command)
        # if run_id is None:
        #     # raise DatabaseConnectionFailed(500)
        #     logging.info('DB CONNECTION FAILED ')

        # if len(run_id) == 0:# If there are no experiments for a particular project_id.
        #     logging.info('DB LENGTH ZERO')

        # else:
        #     run_id = run_id['run_id'][0]
        #     logging.info('RUN ID_------------------------------------------'+str(run_id))
        #     state = 'running'
        #     while state == 'running':
        #         sql_command = "select state from dag_run where run_id='{}'".format(run_id)
        #         state = DBObject.select_records(connection, sql_command)

        #         if state is None:
        #         # raise DatabaseConnectionFailed(500)
        #             logging.info('STATE DB CONNECTION FAILED')
        #             break

        #         if len(state) == 0:# If there are no experiments for a particular project_id.
        #             logging.info('STATE LENGTH ZERO')
        #             break

        #         state = state['state'][0]
        #         time.sleep(4)
        #     logging.info('STATUSSS------------------------------------------'+str(state))
        json_data = {'conf':'{"model_param_dict":"'+str(model_param_dict)+'","master_dict":"'+str(master_dict)+'"}'}
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


    def dag_updater(self, dic, file, namespace = '.'):
        '''
            Updates the dag.

            Args:
            -----
            dic (`dictionary`): Python dictionary that you want to place in the file.
            file (`string`): Name of the file.
            namespace (`string`): Name of the folder inside of the dynamic_dags directory.

            Returns:
            --------
            status (`integer | Exception`): `0` if updation was successful else error.
        '''
        try:
            logging.info("data preprocessing : PreprocessingClass : dag_updater : execution start")
            
            #? Reading the file
            with open(f"dynamic_dags/{namespace}/{file}","r") as ro:
                content = ro.read()
        
            new_dic = str(dic)

            point = content.find("master")
            bracket_start = content.find("{",point) 
            
            def bracket_end_finder(string, length = 0):
                '''
                    A Subfunction to find the ending bracket.
                '''
                
                opening_count = 0
                length -= 1
                flag = False
                
                for i in string:
                    if i == '{':
                        opening_count += 1
                        flag = True
                    elif i == '}':
                        opening_count -= 1
                    length += 1
                        
                    if flag:
                        if opening_count == 0:
                            return length
                else:
                    #? Closing bracket not found
                    return -1    
            
            bracket_end = bracket_end_finder(content[bracket_start:],bracket_start)

            new_str = content[:bracket_start] + new_dic + content[bracket_end + 1:]
        
            #? Writing into the file
            with open(f"dynamic_dags/{namespace}/{file}", 'w') as wo:
                wo.write(new_str)

            logging.info("data preprocessing : PreprocessingClass : dag_updater : execution stop")
            
            return 0

        except Exception as e:
            return e



         
        
        
        
   
    