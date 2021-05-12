'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0         Initial Version 
 Mann Purohit         02-FEB-2021           1.1         Initial Version   

*/
'''

# Airflow Related Imports.
import ast 
import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator

# Import All Supervised Models Function.
from modeling.all_supervised_models import *


# Define Airflow Arguments.
args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}

# Declare Airflow Dag Object.
dag = DAG(dag_id='auto_classification_pipeline',default_args=args,catchup=False,schedule_interval = None,)

# Define First Task.
start_task = PythonOperator(task_id='start_pipeline',python_callable=start_pipeline,dag=dag,)


# Get model dict. 
model_type = 'Classification'
model_dict = get_supervised_models(model_type)

model_id = model_dict['model_id'][:3]
model_name = model_dict['model_name'][:3]
model_class_name = model_dict['model_class_name'][:3]
model_hyperparams =  model_dict['model_hyperparams'][:3]
algorithm_type = model_dict['algorithm_type'][:3]

# Create Dynamic Task.
for model_id,model_name,model_class_name,model_hyperparams,algorithm_type in zip(model_id,model_name,model_class_name, model_hyperparams, algorithm_type):
    dynamic_task = PythonOperator(task_id=model_name,
                                  python_callable=eval('supervised_models'),
                                  op_kwargs={'model_id':model_id,'model_name':model_name,'model_type':model_type,
                                             'algorithm_type': algorithm_type,'model_class_name':model_class_name,
                                             'model_hyperparams':ast.literal_eval(model_hyperparams)},
                                  dag=dag)
    
    start_task >> dynamic_task
