
#* Relative Imports
from preprocess.utils.preprocessing import PreprocessingClass
from database import *

#* Library Imports
from datetime import datetime, timedelta
import sys

#* Airflow Imports
from airflow import DAG
import airflow
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

#* Defining Objects
PC_OBJ = PreprocessingClass(database,user,password,host,port)

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

main_dag_id = "Cleanup_dag_138375250467332160"

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      
    'provide_context': True, 
}

dag = DAG(
    main_dag_id,
    default_args=args,    
    description='A Dynamically Generated DAG.',
    catchup=False,
    schedule_interval = '@once',                         
)

#? Getting Required Parameters

master_dict = {'active': 1, 'operation_dict': {29: [1]}, 'values_dict': {29: ['100']}, 'schema_id': '5', 'dataset_id': '9', 'project_id': '5', 'save_as': 'False', 'visibility': None, 'dataset_name': None, 'dataset_desc': None, 'user_name': 'abhishek'} 

if int(master_dict['active']) == 0:
    sys.exit()

else:
    operation = master_dict['operation_dict']
    value_dict = master_dict['values_dict']
    schema_id = int(master_dict['schema_id'])
    dataset_id = int(master_dict['dataset_id'])
    project_id = int(master_dict['project_id'])
    save_as = master_dict['save_as']
    visibility = master_dict['visibility']
    dataset_name = master_dict['dataset_name']
    dataset_desc = master_dict['dataset_desc']
    new_user_name = master_dict['user_name']

#Note: This thing might be causing the connection issues
DBObject,connection,connection_string = PC_OBJ.get_db_connection()
if connection == None :
    raise DatabaseConnectionFailed(500)

#Get the dataframe of dataset detail based on the dataset id
dataframe = DBObject.get_dataset_detail(DBObject,connection,dataset_id)

#Extract the dataframe based on its column name as key
table_name,dataset_visibility,user_name = str(dataframe['dataset_table_name'][0]),str(dataframe['dataset_visibility'][0]),str(dataframe['user_name'][0])

if dataset_visibility == 'private':
    dataset_table_name = user_name+'."'+table_name+'"'
else:
    dataset_table_name = 'public'+'."'+table_name+'"'

#get the Column list
column_list = PC_OBJ.get_col_names(DBObject, connection ,schema_id)
old_column_list = PC_OBJ.get_col_names(DBObject, connection ,schema_id,json = False,original = True)

schema_column_list = DBObject.get_schema_column(connection,schema_id)

op_dict = {
    1 : PC_OBJ.discard_missing_values,
    2 : PC_OBJ.discard_noise,
    3 : PC_OBJ.delete_above,
    4 : PC_OBJ.delete_below,
    5 : PC_OBJ.remove_noise,
    6 : PC_OBJ.mean_imputation,
    7 : PC_OBJ.median_imputation,
    8 : PC_OBJ.mode_imputation,
    9 : PC_OBJ.missing_category_imputation,
    10 : PC_OBJ.end_of_distribution,
    11 : PC_OBJ.frequent_category_imputation,
    12 : PC_OBJ.missing_category_imputation,
    13 : PC_OBJ.random_sample_imputation,
    14 : PC_OBJ.repl_noise_mean,
    15 : PC_OBJ.repl_noise_median,
    16 : PC_OBJ.repl_noise_mode,
    17 : PC_OBJ.repl_noise_eod,
    18 : PC_OBJ.repl_noise_random_sample,
    19 : PC_OBJ.repl_noise_arbitrary_val,
    20 : PC_OBJ.rem_outliers_ext_val_analysis,
    21 : PC_OBJ.rem_outliers_z_score,
    22 : PC_OBJ.repl_outliers_mean_ext_val_analysis,
    23 : PC_OBJ.repl_outliers_mean_z_score,
    24 : PC_OBJ.repl_outliers_med_ext_val_analysis,
    25 : PC_OBJ.repl_outliers_med_z_score,
    26 : PC_OBJ.apply_log_transformation,
    27 : PC_OBJ.label_encoding,
    28 : PC_OBJ.one_hot_encoding,
    29 : PC_OBJ.add_to_column,
    30 : PC_OBJ.subtract_from_column,
    31 : PC_OBJ.divide_column,
    32 : PC_OBJ.multiply_column
}

def dag_end(DBObject,connection,dataset_id,project_id,dag_id,new_user_name,dataset_name,**kwargs):
    '''
        To reset the dag status
    '''
    activity_id = 52
    status = PC_OBJ.get_cleanup_startend_desc(DBObject,connection,dataset_id,project_id,activity_id,new_user_name,dataset_name)
    return status

#? Making Dynamic Tasks
t1= DummyOperator(task_id='start',dag=dag)
t2= PythonOperator(
            task_id='Finishing_Up',
            dag=dag,
            provide_context=True,
            python_callable=PC_OBJ.update_schema_flag_status,
            op_args=[DBObject,connection,schema_id,dataset_id,schema_column_list],
            trigger_rule="all_done")
t4= PythonOperator(
            task_id='Enable_Cleanup_Page',
            dag=dag,
            provide_context=True,
            python_callable=dag_end,
            op_args=[DBObject,connection,dataset_id,project_id,main_dag_id,new_user_name,dataset_name],
            trigger_rule="all_done")

if save_as == 'True':
    t3 = PythonOperator(
                task_id='Save-As',
                dag=dag,
                provide_context=True,
                python_callable=PC_OBJ.SaveAs,
                op_args=[DBObject,connection,project_id,table_name,user_name,dataset_visibility,dataset_name,visibility,dataset_desc],
                trigger_rule="all_done")
    t2.set_downstream(t3)
    t3.set_downstream(t4)
else:
    t2.set_downstream(t4)


previous_task = t1
i = 0
daglist = []    

for index in operation.keys():
    dynamicTaskOne = DummyOperator(
    task_id='Function_' +str(index) + '_Start',
    dag=dag,)

    for task in daglist:
        task.set_downstream(dynamicTaskOne)

    previous_task.set_downstream(dynamicTaskOne)
    daglist = []    

    value = value_dict[index]
    for j,col in enumerate(operation[index]): 
        
        #? Which parameters should be given to which function
        param_dict = {
            1 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            2 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            3 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            4 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            5 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            6 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            7 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            8 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            9 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j], True],
            10 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            11 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            12 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            13 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            14 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            15 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            16 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            17 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            18 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            19 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            20 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            21 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            22 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            23 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            24 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            25 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            26 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            27 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col]],
            28 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], schema_id],
            29 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            30 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            31 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]],
            32 : [DBObject,connection,project_id,column_list,old_column_list, dataset_table_name, [col], value[j]]
        }
        
        dynamicTask = PythonOperator(
            task_id='Operation_' + str(index) + "_col_" + str(col),
            dag=dag,
            provide_context=True,
            python_callable=op_dict[index],
            op_args=param_dict[index])

        dynamicTaskOne.set_downstream(dynamicTask)
        daglist.append(dynamicTask)
        previous_task = dynamicTaskOne

    i+=1
    if i == len(operation.keys()):
        previous_task.set_downstream(t2)
        for task in daglist:
            task.set_downstream(t2)
