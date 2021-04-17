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
from modeling.all_classifier import logistic_regression_sklearn
from modeling.all_classifier import get_classification_models


args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}


dag = DAG(dag_id='auto_classification_pipeline',default_args=args,catchup=False,)



start_task = PythonOperator(task_id='start_pipeline',python_callable=start_pipeline,dag=dag,)

# Get model dict 

model_dict = get_classification_models()

model_id = model_dict['model_id']
model_name = model_dict['model_name']
function_name = 'Logistic_Regression_SKlearn' #TODO we will get dynamic when we are developing more models.

for model_id,model_name in zip(model_id,model_name):
    dynamic_task = PythonOperator(task_id=model_name,
                                  python_callable=eval(function_name.lower()),
                                  op_kwargs={'model_id':model_id},
                                  dag=dag)
    
    start_task >> dynamic_task
