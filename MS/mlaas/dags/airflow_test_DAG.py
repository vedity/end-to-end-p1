import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator

from src.models.airflow_demo import start_pipeline
from src.models.airflow_demo import linear_regression_sklearn
from src.models.airflow_demo import linear_regression_keras

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2019, 12, 9),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      # this in combination with catchup=False ensures the DAG being triggered from the current date onwards along the set interval
    'provide_context': True,                            # this is set to True as we want to pass variables on from one task to another
}

dag = DAG(
    dag_id='airflow_test_DAG',
    default_args=args,
    schedule_interval= '@daily',             # set interval
	catchup=False,                          # indicate whether or not Airflow should do any runs for intervals between the start_date and the current date that haven't been run thus far
)

# with DAG('store_dag',default_args=default_args,schedule_interval='@daily',catchup=True) as dag:


t1 = DummyOperator(
    task_id='print_rest',
    bash_command='date',
    dag=dag,
)
    
t2 = PythonOperator(
    task_id='linear_regression_with_sklearn', 
    python_callable=linear_regression_sklearn,
    dag=dag,
)
t3 = PythonOperator(
    task_id='linear_regression_with_keras', 
    python_callable=linear_regression_keras,
    dag=dag,
)
    
t1 >> [t2,t3] 

# def get_hello():
#     return "hello"

# def get_world():
#     return "world"
# import datetime
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime.datetime.now(),
#     'email_on_failure': False,
#     'retries': 1,
#     'max_active_runs': 1
# }

# dag = airflow.DAG('first', default_args=default_args, description='First ever airflow DAG run')

# hello = PythonOperator(task_id='hello', python_callable=get_hello, dag=dag)

# world = PythonOperator(task_id='world', python_callable=get_world, dag=dag)

# bash_op = BashOperator(
#     task_id='sleep',
#     depends_on_past=False,
#     bash_command='sleep 10',
#     retries=0,
#     dag=dag,
# )

# hello >> bash_op >> world
