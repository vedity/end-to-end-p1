'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
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
from modeling.all_regressor import get_dataset_ids
from modeling.all_regressor import get_dataset_info

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      
    'provide_context': True,                            
}

dag = DAG(
    dag_id='model_pipeline_test_DAG',
    default_args=args,         
	catchup=False,                         
)



t1 = PythonOperator(
    task_id='get_dataset_ids',
    python_callable=get_dataset_ids,
    dag=dag,
)
    
t2 = PythonOperator(
    task_id='get_dataset_info', 
    python_callable=get_dataset_info,
    dag=dag,
)

    
t1 >> t2 

