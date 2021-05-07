

#* Library Imports
import logging
import traceback
import os

#* Common Utilities
from common.utils.database import db
from common.utils.logger_handler import custom_logger as cl

#* Defining Objects
DBObject = db.DBClass()

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('dag_utils')

class DagUtilsClass():
    '''
        This class provides dag related utilities.
    '''

    def get_dag(self, connection, dag_type = 1, project_id = None, **kwargs):
        '''
            This function is used to get a dag from dag_pool.

            Args:
            -----
            connection (`object`): pycopg2.connection object
            dag_type (`int`): type of dag you want from dag_pool
                - `0` (default) : Cleanup Dag
                - `1` : Manual Modelling Dag
            
            Returns:
            --------
            dag_id (`String`): id of the dag that is allocated to you

            Note:
            ----
            Don't Forget to use release_dag once you are done using the dag.
        '''
        try:
            logging.info("common : DagUtilsClass : get_dag : execution start")

            #? Getting a dag from dag_management_tbl
            sql_command = f'''
            update mlaas.dag_management_tbl 
                set allocated = true 
                where "index" in (
                    select "index" from mlaas.dag_management_tbl 
                        where allocated = false 
                        and dag_type_id = {dag_type}
                        limit 1
                )
                returning "index",dag_id 
            '''
            dag_df = DBObject.select_records(connection, sql_command)
            if dag_df is None: raise RuntimeError #! Failed to get the dataframe, connection issue
            
            index, dag_id = dag_df['index'][0],dag_df['dag_id'][0]

            #? Making Entry in thr Project table
            if project_id:
                if dag_type == 1: #? Making entry for cleanup dag
                    sql_command = f"update mlaas.project_tbl set cleanup_dag_id = '{dag_id}' where project_id={project_id}"
                elif dag_type == 2:#? Making entry for modelling dag
                    sql_command = f"update mlaas.project_tbl set model_dag_id = '{dag_id}' where project_id={project_id}"
                #? Updating the table
                try:
                    status = DBObject.update_records(connection, sql_command)
                    if status == 1:
                        raise RuntimeError
                except Exception as e:
                    logging.error(f"common : DagUtilsClass : get_dag : failed to update project table : {str(e)}")
                    return None,None

            logging.info("common : DagUtilsClass : get_dag : execution stop")
            return index, dag_id
        
        except Exception as e:
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {str(e)}")
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {traceback.format_exc()}")
            return None,None

    def release_dag(self, connection, index = None, dag_id = None, **kwargs):
        '''
            This function is used to submit the dag back to the dag pool.
            
            Args:
            ----
            connection (`object`): pycopg2.connection object
            index (`int | string`) (default : `None`): index of the dag in the dag_management_tbl
            dag_id (`String`) (default : `None`): id of the dag

            Returns:
            -------
            status (`int`): Status of dag release 
        '''
        try:
            logging.info("common : DagUtilsClass : release_dag : execution start")
            
            if not index and not dag_id:
                #? We require at least one of these two things
                logging.error("common : DagUtilsClass : release_dag : dag_index or dag_id needed, None given.")
                raise RuntimeError

            if index:
                #? Index is given
                sql_command = f'''
                update mlaas.dag_management_tbl 
                    set allocated=false 
                    where "index"={index}
                '''
            else:
                #? dag_id is given
                sql_command = f'''
                update mlaas.dag_management_tbl 
                    set allocated=false 
                    where dag_id={dag_id}
                '''
            status = DBObject.update_records(connection, sql_command)

            logging.info("common : DagUtilsClass : release_dag : execution stop")
            return status

        except Exception as e:
            logging.error(f"common : DagUtilsClass : release_dag : execution failed : {str(e)}")
            logging.error(f"common : DagUtilsClass : release_dag : execution failed : {traceback.format_exc()}")
            return 1

    def add_dag_to_table(self, connection, namespace = 'project_dags'):
        '''
            This function is used to add newly created dags to the dag_managemet_tbl.

            Args:
            -----
            connection (`object`): pycopg2.conn object
            namespace (`String`) (Default : `project_dags`): Folder where dags are stored. 

            Returns:
            -------
            status (`Int`): Status of insertion.
        '''
        try:
            logging.info("common : DagUtilsClass : add_dag_to_table : execution start")
            
            #? Folders where we dags are stored
            directory = f'{namespace}/cleanup_dags'
            sql_command = "DELETE FROM mlaas.dag_management_tbl;"

            #? Inserting cleanup dag
            for filename in os.listdir(directory):
                if filename.endswith(".py"):
                    #                               Table Name                   index     dag_id   allocated  dag_type_id
                    sql_command += f"INSERT INTO mlaas.dag_management_tbl VALUES(DEFAULT,'{filename[:-3]}',false,1);"
                else:
                    continue
        
            #? Folders where we dags are stored
            directory = f'{namespace}/manual_modeling_dags'
            
            #? Inserting manual modelling dags
            for filename in os.listdir(directory):
                if filename.endswith(".py"):
                    sql_command += f"INSERT INTO mlaas.dag_management_tbl VALUES(DEFAULT,'{filename[:-3]}',false,2);"
                else:
                    continue

            status = DBObject.update_records(connection, sql_command)

            logging.info("common : DagUtilsClass : add_dag_to_table : execution stop")
            return status
        except Exception as e:
            logging.error(f"common : DagUtilsClass : add_dag_to_table : execution failed : {str(e)}")
            logging.error(f"common : DagUtilsClass : add_dag_to_table : execution failed : {traceback.format_exc()}")
            return 1
    