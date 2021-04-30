

#* Library Imports
import logging
import traceback

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

    def get_dag(self, connection, dag_type = 1, project_id = None):
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
            index, dag_id = dag_df['index'],dag_df['dag_id']

            logging.info("common : DagUtilsClass : get_dag : execution stop")
            return index, dag_id
        
        except Exception as e:
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {str(e)}")
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {traceback.format_exc()}")
            return None

    def release_dag(self, connection, index = None, dag_id = None):
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
            logging.info("common : DagUtilsClass : get_dag : execution start")
            
            logging.info("common : DagUtilsClass : get_dag : execution stop")

        except Exception as e:
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {str(e)}")
            logging.error(f"common : DagUtilsClass : get_dag : execution failed : {traceback.format_exc()}")
            return 1

