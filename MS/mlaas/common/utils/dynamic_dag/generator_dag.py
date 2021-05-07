### DAG Creator
'''
This workflow listens for Triggers. Based on config parameters passed., It creates DAG.
'''

from datetime import timedelta, datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from common.utils.dynamic_dag.operators.request_formatter import RestToTemplateWrapperOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'schedule_interval': None, # exclusively “externally triggered” DAG
    'start_date': days_ago(2),
    'catchup': False,
    'owner': 'admin',
}

dag = DAG(
    'dag_creator',
    default_args=default_args,
    description='For Creating Dynamic Dags',
)

t1 = RestToTemplateWrapperOperator(task_id="generate-dag", dag=dag)

dag.doc_md = __doc__

t1.doc_md = """\
#### Generate dag
This action generates a DAG workflow.
"""