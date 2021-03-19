'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Mann Purohit         15-FEB-2021           1.0         Initial Version           

*/
'''
import numpy as np
import logging
import traceback
import ast
import json

from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception import *

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('project_creation')

class AlgorithmDetector:

    def __init__(self, DBObject, connection):
        self.DBObject = DBObject
        self.connection = connection
    
    
    def get_dataset_info(self,project_id,dataset_id,user_id):
        """This function returns the project_name, dataset_name and the target columns for the associated dataset.
 
        Returns:
            Tuple: project_name, dataset_name, target_columns:- name of target feature/s associated to the dataset.
        """
        try:

            logging.info("modeling : ModelClass : get_dataset_info : execution start")
        
            # SQL query to get the project_name
            sql_command = 'select target_features,project_name from mlaas.project_tbl where project_id='+str(project_id)
            project_df = self.DBObject.select_records(self.connection, sql_command)
            if project_df is None:
                raise DatabaseConnectionFailed(500)

            if len(project_df) == 0 :
                raise DataNotFound(500)
            
            project_name = project_df['project_name'][0]
            target_features = project_df['target_features'][0]
            target_columns= ast.literal_eval(target_features)[1:]
            
            # SQL query to get the dataset_name
            sql_command = 'select dataset_name from mlaas.dataset_tbl where dataset_id='+str(dataset_id)
            dataset_df = self.DBObject.select_records(self.connection, sql_command)
            dataset_name = dataset_df['dataset_name'][0]
    
            logging.info("modeling : ModelClass : get_dataset_info : execution end"+str(type(target_columns)))
            return project_name, dataset_name, target_columns
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
    
        
        
    def get_model_type(self, project_id, dataset_id):
        try:

            sql_command = 'select problem_type from mlaas.project_tbl where project_id={} and dataset_id={}'.format(project_id, dataset_id)
            model_type_literal = self.DBObject.select_records(self.connection, sql_command)
            if model_type_literal is None:
                raise DatabaseConnectionFailed(500)

            if len(model_type_literal) == 0 :
                raise DataNotFound(500)
    
            model_type_dict = ast.literal_eval(model_type_literal.iloc[0, 0])

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        return model_type_dict
    
    
    def show_models_list(self, project_id, dataset_id, model_type):
        """Returns the compatible list of model on the basis of algorithm_type and model_type.
 
        Returns:
            list: models_list, contains list of all the ML/DL models derived from the algorithm and model type.
        """
        try:
            sql_command = 'select target_features from mlaas.project_tbl where project_id={} and dataset_id={}'.format(project_id, dataset_id)
            target_features = ast.literal_eval(self.DBObject.select_records(self.connection, sql_command).iloc[0, 0])
            if model_type != 'Unsupervised':
                if len(target_features) > 2:
                    algorithm_type = 'Multi_Target'
                elif len(target_features) == 2:
                    algorithm_type = 'Single_Target'
    
                sql_command = "select * from mlaas.model_master_tbl where model_type='"+model_type+"'"+" and algorithm_type='"+algorithm_type+"'"
            elif model_type == 'Unsupervised':
    
                sql_command = "select * from mlaas.model_master_tbl where model_type='"+model_type+"'"
            models_list = self.DBObject.select_records(self.connection, sql_command)# Add exception
            models_list_json = json.loads(models_list.to_json(orient='records', date_format='iso'))
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        return models_list_json
 
    def get_hyperparameters(self, model_id):
        """Returns the appropriate list of hyperparameters associated with the model_name argument, 
            along with how to display and validate them.
 
        Args:
            model_id (int): Unique identity of the ML/DL model.
 
        Returns:
            list: list of hyperparameters associated with the model 'model_id'.
        """
        try:

            sql_command = 'select hyperparameter, value, type from mlaas.model_hyperparams_tbl where model_id='+str(model_id)
            model_hyperparams_df = self.DBObject.select_records(self.connection, sql_command)
            if model_hyperparams_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_hyperparams_df) == 0 :
                raise DataNotFound(500)
            model_hyperparams_df['value'] = model_hyperparams_df['value'].apply(lambda x: ast.literal_eval(x))
            logging.info("Model_hyperparams_df dtypes = " + str(model_hyperparams_df))
            # if model_hyperparams_df == None or (len(model_hyperparams_df) == 0):
            #     # Raise Error of model_id not found
            #     pass
            json_data = json.loads(model_hyperparams_df.to_json(orient='records', date_format='iso'))

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        return json_data