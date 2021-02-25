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
from modeling.all_regressor import start_pipeline
from modeling.all_regressor import linear_regression_sklearn
from modeling.all_regressor import get_auto_model_param

from modeling.split_data import SplitData

############## Dag Code Start From Here ################################## 

input_features_list,target_features_list,project_id,dataset_id,user_id,X_train,X_test, y_train, y_test,DBObject,connection,connection_string = get_auto_model_param()
basic_split_parameters = {'model_mode': 'Auto'}

SplitDataObject = SplitData(basic_split_parameters,DBObject,connection)
####################### Get Parameter #######################


yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      
    'provide_context': True,                            
}

dag = DAG(
    dag_id='model_pipeline_test_demo',
    default_args=args,         
	catchup=False,                         
)



t1 = PythonOperator(
    task_id='start_pipeline',
    python_callable=start_pipeline,
    dag=dag,
)
    
t2 = PythonOperator(
    task_id='get_dataset_ids', 
    python_callable=get_dataset_ids,
    dag=dag,
)

t3 = PythonOperator(
    task_id='Linear_Regression_Sklearn', 
    python_callable=linear_regression_sklearn,
    dag=dag,
    op_kwargs={'model_id':1,'model_mode': 'Auto', 
               'input_features_list': input_features_list, 'target_features_list': target_features_list,
               'project_id':project_id,'dataset_id':dataset_id,'user_id':user_id,
               'X_train':X_train,'X_valid':None,'X_test':X_test,
               'y_train': y_train,'y_valid':None,'y_test':y_test,
               'SplitDataObject':SplitDataObject,
               'DBObject':DBObject,'connection':connection,'connection_string':connection_string
               }
)

t4 = PythonOperator(
    task_id='Linear_Regression_Keras', 
    python_callable=linear_regression_sklearn,
    dag=dag,
    op_kwargs={'model_id':2,'model_mode': 'Auto', 
               'input_features_list': input_features_list, 'target_features_list': target_features_list,
               'project_id':project_id,'dataset_id':dataset_id,'user_id':user_id,
               'X_train':X_train,'X_valid':None,'X_test':X_test,
               'y_train': y_train,'y_valid':None,'y_test':y_test,
               'SplitDataObject':SplitDataObject,
               'DBObject':DBObject,'connection':connection,'connection_string':connection_string
               }
)

t5 = PythonOperator(
    task_id='XGBoost_Regressor', 
    python_callable=linear_regression_sklearn,
    dag=dag,
    op_kwargs={'model_id':3,'model_mode': 'Auto', 
               'input_features_list': input_features_list, 'target_features_list': target_features_list,
               'project_id':project_id,'dataset_id':dataset_id,'user_id':user_id,
               'X_train':X_train,'X_valid':None,'X_test':X_test,
               'y_train': y_train,'y_valid':None,'y_test':y_test,
               'SplitDataObject':SplitDataObject,
               'DBObject':DBObject,'connection':connection,'connection_string':connection_string
               }
)

    
t1 >> t2 >> [t3,t4,t5]


