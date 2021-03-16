import requests
import uuid
import json
import time

def make_dynamic_file(dic):
    file_str = '''
#This File is Dynamically generated through a Script. 

import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

main_dag_id = 'testAirflow_dag'

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      
    'provide_context': True,                            
}

dag = DAG(
    main_dag_id,
    default_args=args,         
    catchup=False,                         
)


def get_params(run_id,**kwargs):


    get_dict = kwargs['dag_run'].conf['operation']

    my_var = Variable.set(run_id,get_dict)



def end_pipeline(dag,run_id,execution_date,ds,**kwargs):

    print("key (run_id): ",kwargs['key'])


def dummy(**kwargs):

    print("Ended")




t1 = PythonOperator(task_id='get_params',provide_context=True,python_callable=get_params,dag=dag,)


key = "{{ run_id }}"

t2 = PythonOperator(task_id='get_key_operation',provide_context=True,python_callable=end_pipeline,dag=dag,
                        op_kwargs={"key":key})
        
t3 = BashOperator(task_id='End', dag=dag, bash_command='echo task has ended')

        

t1 >> t2

operation= *@* # this will work statically (we give this dict static this is working properly but we want to get it dynamically by line no 65)
op_dict = {1:dummy,4:dummy,5:dummy,7:dummy}

t1.set_downstream(t2)

previous_task = t2
i = 0
daglist = []    

for index in operation.keys():
    dynamicTaskOne = BashOperator(
    task_id='Function_start_' +str(index),
    bash_command='echo "hello"',
    dag=dag,)

    for task in daglist:
        task.set_downstream(dynamicTaskOne)

    previous_task.set_downstream(dynamicTaskOne)
    daglist = []    

    for col in operation[index]: 
        dynamicTask = PythonOperator(
            task_id='Operation_' + str(index) + "_col_" + str(col),
            dag=dag,
            provide_context=True,
            python_callable=op_dict[index],)

        dynamicTaskOne.set_downstream(dynamicTask)
        daglist.append(dynamicTask)
        previous_task = dynamicTaskOne

    i+=1
    if i == len(operation.keys()):
        previous_task.set_downstream(t3)
        for task in daglist:
            task.set_downstream(t3)

    '''
    file_str = file_str.replace("*@*", str(dic))
    return file_str
  
if __name__ == '__main__':
    dic = {
    1: [1,2,3,4,5,6,7,8,9,10],
    4: [3,4,5,6,7]
    }
    
    # wo = open(r"C:\Users\jshukla\Desktop\My Folders\My Stuff\Gitlab Repos\end-to-end-p1\MS\mlaas\temp_dag.py",'w')
    # wo.write(make_dynamic_file(dic))
    # wo.close()
    
    # operation=dic
    # id = uuid.uuid1().time
    # key="op_"+str(id)
    # json_data = {'conf':'{"operation":"'+ str(operation)+'","key":"'+ str(key)+'"}'}
    # result = requests.post("http://localhost:8080/api/experimental/dags/testAirflow_dag/dag_runs",data=json.dumps(json_data),verify=False)#owner

    # print(result)
    
    operation=dic
    id = uuid.uuid1().time
    key='Cleanup_dag_'+str(id)
    template = "cleanup_dag.template"
    namespace = "Cleanup_Dags"
    
    json_data = {'conf':'{"operation_dict":"'+ str(operation)+'","dag_id":"'+ str(key)+'","template":"'+ template+'","namespace":"'+ namespace+'"}'}
    print(json_data)
    result = requests.post("http://localhost:8080/api/experimental/dags/dag_creator/dag_runs",data=json.dumps(json_data),verify=False)#owner

    print(result)
    
    