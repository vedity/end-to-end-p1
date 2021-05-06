
import uuid
import os
import sys

def create_dags(dag_type = 1, dag_count = 100):
    '''
        This function is used to mass create dags.
    '''

    # try:
    #? Creating Directories

    print("Creating Directories")
    try:
        os.mkdir("MS/mlaas/project_dags/cleanup_dags/")
    except:
        #? Folder is Already there, so No need to create new dags
        print("Folder is already there, Exiting.")
        sys.exit()
    try:
        os.mkdir("MS/mlaas/project_dags/manual_modelling_dags/")
    except:
        print("Folder is already there, Exiting.")
        sys.exit()
    
    #? Creating Cleanup Dags
    print("Creating Cleanup Dags")
    
    with open("MS/mlaas/common/utils/dynamic_dag/templates/cleanup_dag.template","r") as ro:
        content = ro.read()
        
    for _ in range(dag_count):
        id = uuid.uuid1().time
        dag_id='Cleanup_dag_'+str(id)

        #? Filling the information in the dag
        file_content = content.replace("#DAG_ID",'"'+dag_id+'"')
        file_content = file_content.replace("#MASTER_DICT","{}")

        with open(f"MS/mlaas/project_dags/cleanup_dags/{dag_id}.py",'w') as wo:
            wo.write(file_content)

    #? Creating Modelling Dags
    print("Creating Modelling Dags")
    
    with open("MS/mlaas/common/utils/dynamic_dag/templates/manual_model_dag.template","r") as ro:
        content = ro.read()
        
    for _ in range(dag_count):
        id = uuid.uuid1().time
        dag_id='manual_model_dag_'+str(id)

        #? Filling the information in the dag
        file_content = content.replace("#DAG_ID",'"'+dag_id+'"')
        file_content = file_content.replace("#MASTER_DICT","{}")

        with open(f"MS/mlaas/project_dags/manual_modelling_dags/{dag_id}.py",'w') as wo:
            wo.write(file_content)

    print("Complete")
    # except Exception as e:
    #     return str(e)

if __name__ == '__main__':
    create_dags()
