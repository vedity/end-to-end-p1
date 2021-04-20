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


        
