'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Shivani Bhalodiya      05-APRIL-2021           1.0           Initial Version 
 
*/
'''

import json
import pandas as pd
import numpy as np
import ast

from pandas import DataFrame
import logging
import traceback
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *

user_name = 'admin'
log_enable = True
 
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
 
logger = logging.getLogger('view')

class CommonMethodClass:
    def __init__(self, db_param_dict):
        
        self.DBObject = db_param_dict['DBObject']
        self.connection = db_param_dict['connection']

    def get_artifact_uri(self, experiment_id,str1):
        """
        This function is used to get artifact_uri of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]
            str1 ([string]): [prefix for artifact]

        Returns:
            [artifact_uri]: [it will return the artifact_uri.]
            
        """
        try:
            logging.info("modeling : CommonMethodClass : get_artifact_uri : execution start")
            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the learning curve's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command) 
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500) 
                
            artifact_uri = artifact_uri.iloc[0,0]
            final_artifact_uri = artifact_uri + str1

            return final_artifact_uri #Will return artifact_uri

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : CommonMethodClass : get_artifact_uri : Exception " + str(exc))
            logging.error("modeling : CommonMethodClass : get_artifact_uri : " +traceback.format_exc())
            return exc.msg

    def get_json(self,artifact_uri):
        """This function is used to get json data for particular uri.

        Args:
            artifact_uri ([object]): [artifact_uri of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for learning curve.]
            
        """
        logging.info("modeling : CommonMethodClass : get_json : Execution Start")
        with open(artifact_uri, "r") as rf: 
                json_data = json.load(rf)
        logging.info("modeling : CommonMethodClass : get_json : Execution End")
        return json_data
           
    def set_json(self,json_data,round_digit):
        """This function is used to round json data.

        Args:
            json_data ([object]): [artifact_uri of particular experiment.]

        Returns:
            [json_data]: [it will return rounded json_data.]
            
        """
        logging.info("modeling : CommonMethodClass : set_json : Execution Start")
        json_data_df = pd.DataFrame(json_data).round(round_digit)
        final_json_data = json_data_df.to_dict(orient='list')
        logging.info("modeling : CommonMethodClass : set_json : Execution End")
        return final_json_data

    def actual_vs_prediction_fun(self,experiment_id,model_type,actual_vs_prediction_json):
        """This function is used to get actuval_vs_prediction of particular experiment based on model type.

        Args:
            experiment_id ([Integer]): [Experiment id of particular experiment.]
            model_type ([String]): [Type of model.]
            actual_vs_prediction_json ([Integer]): [actual_vs_prediction_json of particular experiment.]

        Returns:
            [actual_vs_prediction_json]: [it will return the actual_vs_prediction_json.]
            
        """
        logging.info("modeling : CommonMethodClass : actual_vs_prediction_fun : execution start")
        if model_type == 'Regression':
            actual_vs_prediction_df = DataFrame(actual_vs_prediction_json).round(decimals = 3) #Round to the nearest 3 decimals.
            _,target_features = self.get_unscaled_data(experiment_id) 
            actual_vs_prediction_df.rename(columns = {target_features[0]:'index',target_features[1]:'price',target_features[1]+'_prediction':'price_prediction'}, inplace = True)
            actual_vs_prediction_json = actual_vs_prediction_df.to_dict(orient='list')
            
        elif model_type == 'Classification':
            
            unscaled_df,target_features = self.get_unscaled_data(experiment_id)

            actual_vs_prediction_df = DataFrame(actual_vs_prediction_json) 
            
            actual_vs_prediction_df.rename(columns = {target_features[0]:'seq_id'}, inplace = True)
            
            final_df=pd.merge(unscaled_df, actual_vs_prediction_df, on='seq_id', how='inner')
            
            logging.info("final df =="+str(final_df))
            
            actual_vs_prediction_df = actual_vs_prediction_df.drop(['seq_id'],axis=1)
            
            
            cols=actual_vs_prediction_df.columns.values.tolist()
            actual_col=''
            predict_col=''
            for i in cols:
                if i.endswith('_prediction') :
                    predict_col=i
                else:
                    actual_col = i
            
            
            classes_df = final_df[[actual_col,actual_col+'_str']]
            logging.info("classes_df df =="+str(classes_df))
            
            actual_dict = classes_df.groupby(actual_col+'_str').count().to_dict()

            prediction_dict = actual_vs_prediction_df.groupby(predict_col).count().to_dict()
            
            act_dict = {}
            prd_dict = {}
            for i,j in zip(actual_dict.items(),prediction_dict.items()):
                act_dict.update(i[1])
                prd_dict.update(j[1])
            
            key = list(act_dict.keys())
            actual_lst = list(act_dict.values())
            prediction_lst = list(prd_dict.values())
            
            actual_vs_prediction_json = {"keys":key,"actual":actual_lst,"prediction":prediction_lst}
            

        logging.info("modeling : CommonMethodClass : actual_vs_prediction_fun : execution end")
        return actual_vs_prediction_json
                
        
    def get_unscaled_data(self,experiment_id):
        """This function is used to get unscaled_data of particular experiment.

        Args:
            experiment_id ([Integer]): [Experiment id of particular experiment.]
        Returns:
            [unscaled_df]: [it will return the unscaled_df.]
            [target_features]: [it will return the target_features.]
            
        """   
        try:
            logging.info("modeling : CommonMethodClass : get_unscaled_data : execution start")
            sql_command = "select scaled_split_parameters,target_features from mlaas.project_tbl"\
                        " Where project_id in ( select project_id from mlaas.model_experiment_tbl where experiment_id="+str(experiment_id) +")"
            
            unscaled_info_df = self.DBObject.select_records(self.connection, sql_command)
            
            if unscaled_info_df is None or len(unscaled_info_df) == 0 :
                raise DataNotFound(500)
            
            scaled_split_parameters= ast.literal_eval(unscaled_info_df['scaled_split_parameters'][0])
            
            target_features = ast.literal_eval(unscaled_info_df['target_features'][0])
            
            unscaled_path = scaled_split_parameters['actual_Y_filename']
            
            unscaled_arr= np.load('./'+unscaled_path,allow_pickle=True)
            
            unscaled_df=pd.DataFrame(unscaled_arr,columns=target_features)
        
            unscaled_df.rename(columns = {target_features[0]:'seq_id',target_features[1]:target_features[1]+'_str'}, inplace = True)
            
            
            logging.info("arr =="+str(unscaled_df))
            logging.info("arr =="+str(target_features))
            
            logging.info("modeling : CommonMethodClass : get_unscaled_data : execution end")
            return unscaled_df,target_features

        except (DataNotFound) as exc:
            logging.error("modeling : CommonMethodClass : get_unscaled_data : Exception " + str(exc))
            logging.error("modeling : CommonMethodClass : get_unscaled_data : " +traceback.format_exc())
            return exc.msg
