'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''

# All Necessary Imports
import json
from pandas import DataFrame
import mlflow
import re


class ExperimentClass:
    
    def __init__(self,DBObject, connection, connection_string):
        
        self.DBObject = DBObject
        self.connection = connection
        self.connection_string = connection_string
        self.table_name='mlaas.model_experiment_tbl'
        self.cols = 'experiment_id,run_uuid,project_id,dataset_id,user_id,model_id,model_mode,dag_run_id' 
        
       
    def add_experiments(self,experiment_id,experiment_name,run_uuid,
                        project_id,dataset_id,user_id,model_id,model_mode,dag_run_id):
        
        sql_command = "UPDATE "+self.table_name+" SET experiment_id="+str(experiment_id)+",run_uuid='"+ run_uuid +"' "\
                      "WHERE project_id="+str(project_id) + " and model_id="+str(model_id)+" and dag_run_id='"+str(dag_run_id)+"'"
                      
        upd_exp_status = self.DBObject.update_records(self.connection,sql_command)
        
        return upd_exp_status
    
    def update_experiment(self,experiment_id,status):
        
        sql_command = "UPDATE "+self.table_name+" SET status='"+status+"' WHERE experiment_id="+str(experiment_id)
        upd_exp_status = self.DBObject.update_records(self.connection,sql_command)
        
        return upd_exp_status


    def get_mlflow_experiment(self, experiment_name):
        sql_command = "select nextval('unq_num_seq') as ids"
        counter = self.DBObject.select_records(self.connection, sql_command)
        
        counter = counter['ids'][0]

        experiment_name = experiment_name.lower() + "_" + str(counter)
        
        # create experiment 
        experiment_id = mlflow.create_experiment(experiment_name)
        experiment = mlflow.get_experiment(experiment_id)
        
        return experiment, experiment_id
        
           
            
   
