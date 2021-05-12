
import uuid
import os
import sys
import shutil

#? Adding current folder to the system path
sys.path.insert(0,'/mlaas')

from common.utils.dynamic_dag.dag_utils import DagUtilsClass
from common.utils.database.db import DBClass
from database import *

DAG_OBJ = DagUtilsClass()
DB_OBJ = DBClass()

def create_dags(dag_type = 1, dag_count = 100):
    '''
        This function is used to mass create dags.
    '''

    try:
        #? Creating Directories

        print("Creating Directories")
        try:
            os.mkdir("project_dags/cleanup_dags/")
        except:
            #? Folder is Already there, so No need to create new dags
            print("Folder is already there, Deleting It & Creating a new one.")
            shutil.rmtree("project_dags/cleanup_dags/")
            os.mkdir("project_dags/cleanup_dags/")
        try:
            os.mkdir("project_dags/manual_modeling_dags/")
        except:
            print("Folder is already there, Deleting It & Creating a new one.")
            shutil.rmtree("project_dags/manual_modeling_dags/")
            os.mkdir("project_dags/manual_modeling_dags/")
        
        #? Creating Cleanup Dags
        print("Creating Cleanup Dags")
        
        with open("common/utils/dynamic_dag/templates/cleanup_dag.template","r") as ro:
            content = ro.read()
        
        content = content.replace("#MASTER_DICT","{}")
            
        for _ in range(dag_count):
            id = uuid.uuid1().time
            dag_id='Cleanup_dag_'+str(id)

            #? Filling the information in the dag
            file_content = content.replace("#DAG_ID",'"'+dag_id+'"')
            
            with open(f"project_dags/cleanup_dags/{dag_id}.py",'w') as wo:
                wo.write(file_content)

        #? Creating Modelling Dags
        print("Creating Modelling Dags")
        
        with open("common/utils/dynamic_dag/templates/manual_model_dag.template","r") as ro:
            content = ro.read()
        
        content = content.replace("#MASTER_DICT","{}")
            
        for _ in range(dag_count):
            id = uuid.uuid1().time
            dag_id='manual_model_dag_'+str(id)

            #? Filling the information in the dag
            file_content = content.replace("#DAG_ID",'"'+dag_id+'"')
            
            with open(f"project_dags/manual_modeling_dags/{dag_id}.py",'w') as wo:
                wo.write(file_content)

        print("Creating Entry into the Table")

        connection,_ = DB_OBJ.database_connection(database,user,password,host,port)
        DAG_OBJ.add_dag_to_table(connection)

        print("Complete")
    except Exception as e:
        print(str(e))
    finally:
        connection.close()

if __name__ == '__main__':
    create_dags(dag_count=5)
