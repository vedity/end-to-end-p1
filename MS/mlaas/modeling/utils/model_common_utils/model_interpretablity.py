'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      06-MAY-2021           1.0           Initial Version 
 
*/
'''

# All Necessary Imports
import logging
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import lime
from lime import lime_tabular
import logging
import traceback
import pickle
# Imports Common Class Files.
from common.utils.logger_handler import custom_logger as cl
# Declare Global Object And Varibles.
user_name = 'admin'
log_enable = True
 
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
 
logger = logging.getLogger('model_interpretability')

class ModelExplanation:
    
    def __init__(self,DBObject,connection):
        
        self.DBObject = DBObject
        self.connection = connection
    
    def get_model_explanation(self,actual_prediction_json,exp_type):
        
        # Get Residuals Dataframe
        residuals_df= pd.DataFrame(actual_prediction_json)
        
        if exp_type.lower() == 'regression':
            # Get Selected Columns
            residuals = residuals_df[['index','residuals']]
            # Convert Whole Dataframe into integer
            residuals = residuals.astype(int)
            # Convert Residuals into absolute values
            residuals['residuals'] = abs(residuals['residuals'])
            # Sort Residuals Values
            residuals = residuals.sort_values(by='residuals',ascending=True)
            # Convert dataframe into json
            residuals_json = residuals.to_dict(orient='list')
            
        else:
            # Get Selected Columns
            residuals = residuals_df[['index','prediction_prob']]
            # Sort Residuals Values
            residuals = residuals.sort_values(by='prediction_prob',ascending=True)
            
            residuals=residuals.round(decimals = 2) #Round to the nearest 3 decimals.
            # Convert dataframe into json
            residuals_json = residuals.to_dict(orient='list')
        
        return residuals_json
    
    
    def get_local_explanation(self,experiment_id,exp_type,artifact_uri,seq_ids,
                              original_data_df,test_df,x_train_arr,
                              input_features_lst,target_features_list):
        
        model_name = self.get_model_name(experiment_id)
        loaded_model = self.load_model(artifact_uri,model_name)
        # Get Input Array
        input_arr=x_train_arr[:,1:]
        
        input_features_list = input_features_lst[1:]
        
          
        model_interpreter = lime_tabular.LimeTabularExplainer(training_data=input_arr,
                                                                feature_names=input_features_list,
                                                                mode=exp_type.lower())
        
        index_lst =[]
        features_lst=[]
        importance_lst = []
        prediction_lst = []
        
        for id in seq_ids:
            
            df=test_df[test_df['index'] == id]
            
            df_arr = np.array(df)
            
            row = df_arr[:,1:]
            
            if exp_type.lower() == 'regression':
                
                explaination = model_interpreter.explain_instance(data_row=row.flatten(),predict_fn = loaded_model.predict)
                pred = loaded_model.predict(row.reshape(1,-1)).tolist()[0][0]
                pred = round(pred,2)
                
            else:
                
                explaination = model_interpreter.explain_instance(data_row=row.flatten(),predict_fn = loaded_model.predict_proba)
                pred = loaded_model.predict_proba(row.reshape(1,-1)).tolist()[0][0]
                pred = round(pred,2)
                
            features=[]
            importance=[]
            exp_lst=explaination.as_list()
            
            for i in exp_lst:
                string = list(i)[0]
                importance.append(list(i)[1])
                only_alpha = ""
                ## looping through the string to find out alphabets
                for char in string:
                    ## checking whether the char is an alphabet or not using chr.isalpha() method
                    if char.isalpha():
                        only_alpha += char

                ## printing the string which contains only alphabets
                features.append(only_alpha)
              
            features_lst.append(features)
            importance_lst.append(importance)
            index_lst.append(id)
            prediction_lst.append(pred)
            
        
        local_explanation_json = {'index':index_lst,'prediction':prediction_lst,
                                  'features_list':features_lst,'importance_list':importance_lst}
        
        return model_name,local_explanation_json
    
    
    def load_model(self,artifact_uri,model_name):
        
        logged_model_path = artifact_uri + model_name
        # Load model as a PyFuncModel.
        # loaded_model = mlflow.pyfunc.load_model(logged_model_path)
    
        with open(logged_model_path+'/model.pkl', 'rb') as pickle_file:
            loaded_model = pickle.load(pickle_file)
                
        return loaded_model
    
    def get_model_name(self,experiment_id):
        
        sql_command= "select mmt.model_id,mmt.model_name from mlaas.model_master_tbl mmt,mlaas.model_experiment_tbl met "\
                     "where mmt.model_id=met.model_id and met.experiment_id="+str(experiment_id)
                     
        model_df = self.DBObject.select_records(self.connection, sql_command)
        model_name = model_df['model_name'][0]
        
        return model_name
    
        
        
        
        
