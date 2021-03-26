import pandas as pd
import uuid
import requests
import json
import ast
from database import *
from common.utils.database import db

DBObject=db.DBClass()    
connection,connection_string=DBObject.database_connection(database,user,password,host,port)  


def get_modeling_dag_name():
    id = uuid.uuid1().time
    dag_id='manual_model_dag_'+str(id)

    template = "manual_model_dag.template"
    namespace = "manual_modeling_dags"
    
    master_dict = {}
    
    json_data = {'conf':'{"master_dict":"'+ str(master_dict)+'","dag_id":"'+ str(dag_id)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
    
    result = requests.post("http://airflow:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

    return dag_id

def start_pipeline(dag,run_id,execution_date,ds,**kwargs):
    print("pipeline start")
    dag_id = dag.dag_id
    
    model_param_dict = ast.literal_eval(kwargs['dag_run'].conf['model_param_dict'])
    
    model_mode = model_param_dict['model_mode']
    
    project_id = int(model_param_dict['project_id'])
    dataset_id = int(model_param_dict['dataset_id'])
    user_id = int(model_param_dict['user_id'])
    exp_name  = model_param_dict['experiment_name']
    
    
    
    table_name='mlaas.model_dags_tbl'
    cols = 'dag_id,exp_name,run_id,execution_date,project_id,dataset_id,user_id,model_mode' 
        
    row = dag_id,exp_name ,run_id,execution_date,project_id,dataset_id,user_id,model_mode    
    row_tuples = [tuple(row)]
    
    dag_status = DBObject.insert_records(connection,table_name,row_tuples,cols)
    
    ### New Code Added #####
    table_name = 'mlaas.model_experiment_tbl'
    cols = 'project_id,dataset_id,user_id,model_id,model_mode,dag_run_id'
    
    if model_mode == 'Auto' :
        
        if model_param_dict['model_type'] == 'Regression':
            
            sql_command = "select model_id from mlaas.model_master_tbl where model_type='Regression'"
        else:
            sql_command = "select model_id from mlaas.model_master_tbl where model_type='Classification'"
            
        model_df = DBObject.select_records(connection,sql_command)
        model_ids = model_df['model_id'].to_list()
            
    else:
        master_dict = ast.literal_eval(kwargs['dag_run'].conf['master_dict'])
        model_ids = master_dict['model_id']
        
    for model_id in model_ids:
        
        row = project_id,dataset_id ,user_id,model_id,model_mode,run_id
        row_tuples = [tuple(row)]
        exp_status = DBObject.insert_records(connection,table_name,row_tuples,cols)
        
         
    ### End Changes ######
        
