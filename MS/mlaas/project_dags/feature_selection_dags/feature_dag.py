#* Library Imports
import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

#* Relative Import
from preprocess.utils.feature import feature_selection
FS_OBJ = feature_selection.FeatureSelectionClass()

args = {'owner': 'airflow','start_date': airflow.utils.dates.days_ago(1),'provide_context': True,}

main_dag_id = "feature_selection_dag"

dag = DAG(dag_id=main_dag_id,default_args=args,catchup=False,schedule_interval = '@once',)

# start_task = PythonOperator(task_id='algo_call',python_callable=algo_call,dag=dag)
# start_feature_selection =  PythonOperator(
#     task_id = 'get_possible_algo',
#     python_callable = FS_OBJ.get_possible_fs_algo,
#     dag = dag
# )

chi_sq = PythonOperator(
    task_id = 'chisq_fs',
    python_callable = FS_OBJ.chisq_fs,
    dag = dag
)

mutual_info = PythonOperator(
    task_id = 'mutual_fs',
    python_callable = FS_OBJ.mutual_fs,
    dag = dag
)

anova = PythonOperator(
    task_id = 'anova_fs',
    python_callable = FS_OBJ.anova_fs,
    dag = dag
)

rfe = PythonOperator(
    task_id = 'rfe_fs',
    python_callable = FS_OBJ.rfe_fs,
    dag = dag
)

coorelation = PythonOperator(
    task_id = 'coorelation_fs',
    python_callable = FS_OBJ.coorelation_fs,
    dag = dag
)

end_feature_selection = PythonOperator(
    task_id = 'end_fs',
    python_callable = FS_OBJ.end_fs,
    dag = dag
)


[chi_sq,mutual_info,anova,rfe,coorelation] >> end_feature_selection
