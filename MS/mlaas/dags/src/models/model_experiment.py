import pandas as pd
from .db import DBClass

class ExperimentClass:
    
    def __init__(self,experiment_id,experiment_name,run_uuid,project_id,dataset_id,user_id,model_id,model_mode):
        
        self.run_uuid = run_uuid
        self.experiment_id = experiment_id
        self.experiment_name = experiment_name
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.user_id = user_id
        self.model_id = model_id
        self.model_mode = model_mode
        
        self.database="postgres"
        self.user = "postgres" 
        self.password = "admin"
        self.host = "postgresql"
        self.port = "5432"

    def get_db_connection(self):
        
        DbObject = DBClass()
        connection,connection_string = DbObject.database_connection(self.database,
                                                                    self.user,
                                                                    self.password,
                                                                    self.host,
                                                                    self.port)
        
        return DbObject,connection,connection_string
        
        
    def add_experiments(self):
        
        DbObject,connection,connection_string = self.get_db_connection()
        
        table_name='mlaas.model_experiment_tbl'
        cols = 'experiment_id,experiment_name,run_uuid,project_id ,dataset_id,user_id,model_id,model_mode' 
        
        row = self.experiment_id,self.experiment_name,self.run_uuid,self.project_id ,self.dataset_id,self.user_id,self.model_id,self.model_mode    
        row_tuples = [tuple(row)]
        
        experiment_status = DbObject.insert_records(connection,table_name,row_tuples,cols)
        
        return experiment_status   
        
    def show_experiments(self):
        
        
        
        return None
    
    