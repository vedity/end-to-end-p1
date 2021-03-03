'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


import json
from pandas import DataFrame

class ExperimentClass:
    
    def __init__(self,DBObject, connection, connection_string):
        
        self.DBObject = DBObject
        self.connection = connection
        self.connection_string = connection_string
        self.table_name='mlaas.model_experiment_tbl'
        self.cols = 'experiment_id,run_uuid,project_id,dataset_id,user_id,model_id,model_mode,dag_run_id' 
        
       
         
    def add_experiments(self,experiment_id,experiment_name,run_uuid,
                        project_id,dataset_id,user_id,model_id,model_mode,dag_run_id):
        
        row = experiment_id,run_uuid,project_id ,dataset_id,user_id,model_id,model_mode,dag_run_id
        row_tuples = [tuple(row)]
        
        experiment_status = self.DBObject.insert_records(self.connection,self.table_name,row_tuples,self.cols)
        return experiment_status
    
    def update_experiment(self,experiment_id,status):
        
        sql_command = "UPDATE "+self.table_name+" SET status='"+status+"' WHERE experiment_id="+str(experiment_id)
        upd_exp_status = self.DBObject.update_records(self.connection,sql_command)
        
        return upd_exp_status
        
           
            
   
