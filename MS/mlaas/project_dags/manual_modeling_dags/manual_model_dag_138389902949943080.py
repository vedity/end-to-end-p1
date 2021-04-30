
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
from modeling.all_supervised_models import *



args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}

<<<<<<< HEAD:MS/mlaas/project_dags/manual_modeling_dags/manual_model_dag_138389902949943080.py
main_dag_id = "manual_model_dag_138389902949943080"
=======
main_dag_id = "manual_model_dag_138389775277004670"
>>>>>>> fcda16aca3b3bdc2d9d7a34a768b2c39b96cd678:MS/mlaas/project_dags/manual_modeling_dags/manual_model_dag_138389775277004670.py

dag = DAG(dag_id=main_dag_id,default_args=args,catchup=False,schedule_interval = '@once',)



start_task = PythonOperator(task_id='start_pipeline',python_callable=start_pipeline,dag=dag,)


# Get model dict 

<<<<<<< HEAD:MS/mlaas/project_dags/manual_modeling_dags/manual_model_dag_138389902949943080.py
master_dict = {}
=======
master_dict = {'model_id': [13], 'model_name': ['KNeighbors_Classification'], 'model_hyperparams': [{'n_neighbors': '11', 'metric': 'euclidean', 'algorithm': 'auto'}], 'model_class_name': ['KNeighborsClassificationClass'], 'algorithm_type': ['Multi']}
>>>>>>> fcda16aca3b3bdc2d9d7a34a768b2c39b96cd678:MS/mlaas/project_dags/manual_modeling_dags/manual_model_dag_138389775277004670.py

if len(master_dict) != 0:

    model_id = master_dict['model_id']
    model_name = master_dict['model_name']
    model_class_name = master_dict['model_class_name']
    model_hyperparams = master_dict['model_hyperparams']
    algorithm_type = master_dict['algorithm_type']

    for model_id,model_name, model_class_name, model_hyperparams,algorithm_type in zip(model_id,model_name, model_class_name, model_hyperparams,algorithm_type):
        dynamic_task = PythonOperator(task_id=model_name,
                                    python_callable=eval('supervised_models'),
                                    op_kwargs={'model_id':model_id,'model_name':model_name,
                                               'model_class_name':model_class_name,'algorithm_type': algorithm_type,
                                               'model_hyperparams':model_hyperparams},
                                    dag=dag)
        
        start_task >> dynamic_task
