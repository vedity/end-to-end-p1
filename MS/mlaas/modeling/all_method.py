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
from sklearn.preprocessing import StandardScaler

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
        """This function is used to get actual_vs_prediction of particular experiment based on model type.

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
            actual_vs_prediction_df=actual_vs_prediction_df.drop('residuals',axis=1)
            # Get Original Data
            original_data_df = self.get_original_data(experiment_id)
            # Get Target Features
            _,target_features = self.get_unscaled_data(experiment_id) 
            original_data_df = original_data_df.drop(target_features[1],axis=1)
            
            original_data_df.rename(columns = {target_features[0]:'index'},inplace = True)
    
            actual_vs_prediction_df.rename(columns = {target_features[0]:'index',target_features[1]:'actual',target_features[1]+'_prediction':'prediction'}, inplace = True)
            
            # Final df
            final_df = pd.merge(original_data_df, actual_vs_prediction_df, on="index")
            
            final_df = final_df.sort_values(by='index', ascending=False)
            
            final_json=final_df.to_dict(orient='list')
            
            popup_keys=[]
            popup_values =[]
            actual_vs_prediction_json={}
            for key,value in final_json.items():
                if key not in ('index','actual','prediction'):
                    popup_keys.append(key)
                    popup_values.append(value)
                else:
                    actual_vs_prediction_json[key] = value
                    
            
            new_data_json={'popup_keys':popup_keys,'popup_values':popup_values}
            
            for key,value in new_data_json.items():
                actual_vs_prediction_json[key] = value
                
              
            logging.info("final output  =="+str(actual_vs_prediction_json.keys()))  
            # actual_vs_prediction_df = actual_vs_prediction_df.sort_values(by='index', ascending=False)
            # actual_vs_prediction_json = actual_vs_prediction_df.to_dict(orient='list')
            
        elif model_type == 'Classification':
            
            unscaled_df,target_features = self.get_unscaled_data(experiment_id)

            actual_vs_prediction_df = DataFrame(actual_vs_prediction_json) 
            
            actual_vs_prediction_df.rename(columns = {target_features[0]:'seq_id'}, inplace = True)
            
            final_df=pd.merge(unscaled_df, actual_vs_prediction_df, on='seq_id', how='inner')
            
            logging.info("final df =="+str(final_df))
            
            actual_vs_prediction_df = actual_vs_prediction_df.drop(['seq_id','prediction_prob'],axis=1)
            
            
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
                
                
    def get_original_data(self,experiment_id):
        
        #TODO : Need to add exception
        sql_command = "select dataset_id,schema_id from mlaas.project_tbl "\
                      " where project_id in ("\
                      " select project_id from mlaas.model_experiment_tbl "\
                      " where experiment_id ="+str(experiment_id) + ")"   
                      
        ids_df = self.DBObject.select_records(self.connection, sql_command)
        
        dataset_id,schema_id = ids_df['dataset_id'][0],ids_df['schema_id'][0] 
        
        original_data_df = self.DBObject.get_dataset_df(self.connection, dataset_id, schema_id)
         
        return original_data_df
    
    
    def get_test_data(self,experiment_id):
        
        sql_command="select input_features,target_features,scaled_split_parameters from mlaas.project_tbl "\
                    "where project_id in "\
                                        "( select project_id from mlaas.model_experiment_tbl "\
                                            "where experiment_id="+str(experiment_id) +")"

        param_df = self.DBObject.select_records(self.connection, sql_command)
        
        input_features_list=eval(param_df['input_features'][0])
        target_features_list=eval(param_df['target_features'][0])
        scaled_split_parameters=eval(param_df['scaled_split_parameters'][0])
        
        train_path='./'+scaled_split_parameters['train_X_filename']
        test_path='./'+scaled_split_parameters['test_X_filename']
        
        x_train_arr = np.load(train_path,allow_pickle=True)
        x_test_arr = np.load(test_path,allow_pickle=True)
        
        return x_train_arr,x_test_arr,input_features_list,target_features_list
        
        
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
              
            logging.info("modeling : CommonMethodClass : get_unscaled_data : execution end")
            return unscaled_df,target_features

        except (DataNotFound) as exc:
            logging.error("modeling : CommonMethodClass : get_unscaled_data : Exception " + str(exc))
            logging.error("modeling : CommonMethodClass : get_unscaled_data : " +traceback.format_exc())
            return exc.msg



    def get_residuals(self,experiment_id):
        """[summary]

        Args:
            experiment_id ([type]): [description]

        Returns:
            [type]: [description]
        """
    
        path = '/predictions.json'
        artifact_uri = self.get_artifact_uri(experiment_id,path)#will get artifact_uri for particular experiment
        actual_prediction_json = self.get_json(artifact_uri)# will get json data from particular artifact_uri location
        residuals_df= pd.DataFrame(actual_prediction_json)
        # Get Selected Columns
        residuals = residuals_df['residuals'].values.reshape(-1, 1)
        # Convert dataframe into json

        # residual_hist = np.histogram(residuals, 10)
        # fbins = residual_hist[1]

        convert_dict = self.unit_conversion(residuals)
        f_residuals = convert_dict['Output_arr']
        unit = convert_dict['Unit']
        
        residuals_hist_dict = {'Residuals': f_residuals, 'Unit': unit}
 
        return residuals_hist_dict

    def unit_conversion(self, org_arr, roundto=2):
        """Determines the unit to show on screen for the org_arr

        Args:
            org_arr (array): array to convert
        """
        org_arr = np.array(org_arr)
        flat_arr = org_arr.flatten()
        amin = abs(min(flat_arr))
        amax = abs(max(flat_arr))

        if (amin > 10**11) and (amax > 10**11):
            converted_arr = (flat_arr/(10**9)).round(1)
            unit = 'Billions'
        
        elif (amin > 10**8) and (amax > 10**8):
            converted_arr = (flat_arr/(10**6)).round(1)
            unit = 'Millions'

        elif (amin > 10**6) and (amax > 10**6):
            converted_arr = (flat_arr/(10**5)).round(1)
            unit = 'Lacs'

        elif (amin > 10**5) and (amax > 10**5):
            converted_arr = (flat_arr/(10**3)).round(1)
            unit = 'Thousands'

        elif (amin <= 10) and (amax <= 10):
            converted_arr = flat_arr.round(3)
            unit = 'Ones'

        else:
            converted_arr = flat_arr
            unit = 'Ones'
        
        output_arr = converted_arr.reshape(org_arr.shape)

        return {'Output_arr': output_arr, 'Unit': unit}
