'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0         Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''
import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator

### Import function from main file
from modeling.utils.modeling_dag_utils.dag_common_utils import start_pipeline
from modeling.all_supervised_models import *


args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}


dag = DAG(dag_id='auto_classification_pipeline',default_args=args,catchup=False,)


start_task = PythonOperator(task_id='start_pipeline',python_callable=start_pipeline,dag=dag,)


# Get model dict 
model_type = 'Classification'
model_dict = get_supervised_models(model_type)

model_id = model_dict['model_id']
model_name = model_dict['model_name']
model_class_name = model_dict['model_class_name']
model_hyperparams =  model_dict['hyperparam']
algorithm_type = model_dict['algorithm_type']

for model_id,model_name,model_class_name,model_hyperparams,algorithm_type in zip(model_id,model_name,model_class_name, model_hyperparams, algorithm_type):
    dynamic_task = PythonOperator(task_id=model_name,
                                  python_callable=eval('supervised_models'),
                                  op_kwargs={'model_id':model_id,'model_name':model_name, 'model_mode': 'Auto',
                                             'model_class_name':model_class_name,'model_hyperparams':model_hyperparams,
                                             'algorithm_type': algorithm_type, 'model_type':model_type},
                                  dag=dag)
    
    start_task >> dynamic_task