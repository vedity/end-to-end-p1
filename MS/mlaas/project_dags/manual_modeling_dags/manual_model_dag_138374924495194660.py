
#* Library Imports
import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator

#* Relative Imports
from modeling.utils.modeling_dag_utils.dag_common_utils import start_pipeline
from modeling.all_regressor import get_regression_models
from modeling.all_classifier import get_classification_models
from modeling.all_regressor import linear_regression_sklearn
from modeling.all_classifier import logistic_regression_sklearn



args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}

main_dag_id = "manual_model_dag_138374924495194660"

dag = DAG(dag_id=main_dag_id,default_args=args,catchup=False,schedule_interval = '@once',)



start_task = PythonOperator(task_id='start_pipeline',python_callable=start_pipeline,dag=dag,)


# Get model dict 

master_dict = {}

if len(master_dict) != 0:

    model_id = master_dict['model_id']
    model_name = master_dict['model_name']
    model_param = master_dict['model_param']

    for model_id,model_name in zip(model_id,model_name):
        dynamic_task = PythonOperator(task_id=model_name,
                                    python_callable=eval(model_name.lower()),
                                    op_kwargs={'model_id':int(model_id),
                                                'model_param':model_param},
                                    dag=dag)
        
        start_task >> dynamic_task


    

 

