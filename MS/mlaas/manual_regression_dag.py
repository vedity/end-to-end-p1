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

from modeling.all_regressor import start_pipeline
from modeling.all_regressor import linear_regression_sklearn
from modeling.all_regressor import manual_algorithm_identifier



args = {
'owner': 'airflow',
'start_date': airflow.utils.dates.days_ago(1),      
'provide_context': True,}



dag = DAG(
    dag_id='manual_regression_dag',
    default_args=args,         
    catchup=False,          
)

# model_dict = {'linear_regression_sklearn': linear_regression_sklearn}


t1 = PythonOperator(
    task_id='start_pipeline',
    python_callable=start_pipeline,
    dag=dag,
)


t2 = PythonOperator(task_id='regression_manual',
                    python_callable=manual_algorithm_identifier,
                    op_kwargs={'model_mode': 'Manual'},
                    dag=dag)

t1 >> t2