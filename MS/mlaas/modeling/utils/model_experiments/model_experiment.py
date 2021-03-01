'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


import json
from pandas import DataFrame

class ExperimentClass:
    
    def __init__(self,experiment_id,experiment_name,run_uuid,project_id,dataset_id,
                user_id,model_id,model_mode):
        
        self.run_uuid = run_uuid
        self.experiment_id = experiment_id
        self.experiment_name = experiment_name
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.user_id = user_id
        self.model_id = model_id
        self.model_mode = model_mode
        
       
          
    def add_experiments(self, DBObject, connection, connection_string):
        
        table_name='mlaas.model_experiment_tbl'
        cols = 'experiment_id,run_uuid,project_id,dataset_id,user_id,model_id,model_mode' 
        
        row = self.experiment_id,self.run_uuid,self.project_id ,self.dataset_id,self.user_id,self.model_id,self.model_mode    
        row_tuples = [tuple(row)]
        
        experiment_status = DBObject.insert_records(connection,table_name,row_tuples,cols)
        return experiment_status
           
            
   
