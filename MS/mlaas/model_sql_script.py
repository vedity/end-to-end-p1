
import pandas as pd 
from database import *
from common.utils.database import db

class ModelSqlClass:
    
    def __init__(self,database,user,password,host,port):
        self.DBObject = db.DBClass()
        self.connection,self.connection_string = self.DBObject.database_connection(database,user,password,host,port)
        
    def add_model_records(self):
        
        table_name = 'mlaas.model_master_tbl'
        cols = 'model_id,model_name,model_desc,model_parameter,model_type,algorithm_type'
        
        # First Model
        model_id = 1
        model_name = "Linear_Regression_Sklearn"
        model_desc = "This is simple linear model"
        model_parameter = None
        model_type = "Regression"
        algorithm_type = "Single_Target"
        
        
        row=model_id,model_name,model_desc,model_parameter,model_type,algorithm_type 
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        
        # Second Model
        
        model_id = 2
        model_name = "Linear_Regression_Keras"
        model_desc = "This is simple linear model with keras"
        model_parameter = "['lr','batch_size','epoch','optimizer','loss','activation']"
        model_type = "Regression"
        algorithm_type = "Single_Target"
        
        row=model_id,model_name,model_desc,model_parameter,model_type,algorithm_type 
        row_tuples = [tuple(row)] 
        
        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        
        # Third Model
         # Second Model
        
        model_id = 3
        model_name = "XGBoost_Regressor"
        model_desc = "This is simple linear ensemble model"
        model_parameter = None
        model_type = "Regression"
        algorithm_type = "Single_Target"
        
        row=model_id,model_name,model_desc,model_parameter,model_type,algorithm_type 
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        
        # Logistic Regression Model
        model_id = 4
        model_name = "Logistic_Regression_SKlearn"
        model_desc = "This is a logistic regressor"
        model_parameter = None
        model_type = "Classification"
        algorithm_type = "Single_Target"
        
        row=model_id,model_name,model_desc,model_parameter,model_type,algorithm_type 
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        
        return ref_status
    
    def add_data_model_hyperparams_tbl(self):

        table_name = 'mlaas.model_hyperparams_tbl'
        cols = 'model_id, hyperparameter, param_value, display_type'

        model_id = 1
        hyperparameter = ""
        param_value = "[]"
        display_type = ""
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)


        model_id = 2
        hyperparameter = 'epochs'
        param_value = "[]"
        display_type = ""
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)


        model_id = 2
        hyperparameter = 'learning_rate'
        param_value = '[0.001, 1]'
        display_type = 'validation'
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)

        
        model_id = 2
        hyperparameter = 'batch_size'
        param_value = '[8, 16, 32, 64, 128, 256]'
        display_type = 'dropdown'
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)

        
        model_id = 2
        hyperparameter = 'loss'
        param_value =  '["Mean_Absolute_Error", "Mean_Squared_Error", "Mean_Absolute_Percentage_Error"]'
        display_type = 'dropdown'
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)

        
        model_id = 2
        hyperparameter = 'optimizer'
        param_value = '["SGD", "RMSProp", "Adam"]'
        display_type = 'dropdown'
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)

        
        model_id = 2
        hyperparameter = 'activation'
        param_value = '["Relu", "Sigmoid", "Tanh"]'
        display_type = 'dropdown'
        row=model_id,hyperparameter, param_value, display_type
        row_tuples = [tuple(row)] 

        ref_status = self.DBObject.insert_records(self.connection,table_name,row_tuples,cols)
        
        return ref_status
        
  
 
# DataBase Credintials  
ModelSqlObject = ModelSqlClass(database,user,password,host,port)
# ref_status = ModelSqlObject.add_model_records()
# print("ref_status for model_master_tbl== ",ref_status)

# ref_status = ModelSqlObject.add_data_model_hyperparams_tbl()
# print("ref_status for model_hyperparams_tbl== ",ref_status)





        
        
        
   

        
        
        
    
    
