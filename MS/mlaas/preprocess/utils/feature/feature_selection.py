
#* Library Imports
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import LabelEncoder
import logging
import warnings
import ast 
import requests
import json
import pandas as pd
#* Relative Imports
from .fs_utility import FSUtilityClass
from .mutual_info import MutualInfoClass
from .chisq import ChiSquareClass
from .RFE import RFEClass
from .anova import AnovaClass
from .coorelation import CoorelationClass
warnings.filterwarnings("ignore")
from preprocess.utils import common  
from requests.auth import HTTPBasicAuth


commonObj = common.CommonClass()
DBObject,connection,connection_string = commonObj.get_conn()



class FeatureSelectionClass(FSUtilityClass,MutualInfoClass,ChiSquareClass,RFEClass,AnovaClass,CoorelationClass):

    def feature_schema(self):
        # schema table name
        table_name = 'mlaas.feature_info_tbl'
        # Columns for schema table
        cols = 'schema_id,feature_value,feature_selection_type'

        return table_name,cols


    def algo_call(self,schema_id,target_col):
        
            #fetch all column
            column,change_col = self.fetch_column(DBObject,connection,schema_id)
            change_col.remove(target_col)

            
            # feature_dict = {"target_col":target_col,"column_list":column,"option_list":[chisq_dict,rfe_dict,mutual_dict,anova_dict,co_dict]}
            # status = self.insert_feature_record(DBObject,connection,schema_id,feature_dict)

            return change_col

    def get_extra_column(self,DBObject,connection,schema_id,col_lst):

        col,change_col = self.fetch_column(DBObject,connection,schema_id)
        extra_col = {}
        for i in change_col:
            if i not in col_lst:
                extra_col[i] = "True"
            else:
                continue
        return extra_col,col

    def insert_feature_record(self,DBObject,connection,schema_id,feature_dict):

        table_nm,cols = self.feature_schema()
        row = schema_id,str(feature_dict),None
        tpl = row_tuples = [tuple(row)] 
        status = DBObject.insert_records(connection,table_nm,tpl,cols)
        logging.info("  +status"+str(status))
        return status

    def fs_dag_executor(self,feature_params_dict):
        # ti1 = kwargs['ti1']
        # feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        # dataset_id = feature_params_dict["dataset_id"]
        # schema_id = feature_params_dict["schema_id"]
        # target_col = feature_params_dict["target_col"]

        
        fs_lst = self.get_possible_fs_algo(feature_params_dict['schema_id'],feature_params_dict['target_col'],'reg')
        feature_params_dict['algo_list'] = fs_lst
        json_data = {'conf':'{"feature_params_dict":"'+str(feature_params_dict)+'"}'}
        result = requests.post("http://airflow:8080/api/experimental/dags/feature_selection_dag/dag_runs",data=json.dumps(json_data),verify=False)#owner
        return 0

    def chisq_fs(self,run_id,**kwargs):
        logging.info("--->"+str(run_id))
        # ti = kwargs['ti']
        # algo_list = ti.xcom_pull(key='possible_algo', task_ids='get_possible_algo')
        algo_id = 2

        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        #Chisq
        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]
        algo_list = feature_params_dict["algo_list"]
        
        if algo_id not in algo_list: return 1

        col_lst,value_lst = self.chisq_result(DBObject,connection,dataset_id,schema_id,target_col)
        extra_col,col = self.get_extra_column(DBObject,connection,schema_id,col_lst)
        chisq_col = {**value_lst ,**extra_col } #! merge 2 dict 
        chisq_col.pop(target_col, 'No Key found')
        chisq_dict = {"name" : "Chi Square","column" : chisq_col}

        
        kwargs['ti'].xcom_push(key='chisq', value=chisq_dict)

    def mutual_fs(self,**kwargs):
        # ti = kwargs['ti']
        # algo_list = ti.xcom_pull(key='possible_algo', task_ids='get_possible_algo')
        algo_id = 4
        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        #mutual
        
        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]
        algo_list = feature_params_dict["algo_list"]
        
        if algo_id not in algo_list: return 1
        
        mutual_col = self.get_mutual_info(DBObject,connection,dataset_id,schema_id,target_col)
        mutual_col.pop(target_col, 'No Key found')
        mutual_dict = {"name" : "Mutual Information","column" : mutual_col}

        kwargs['ti'].xcom_push(key='mutual', value=mutual_dict)

    def anova_fs(self,**kwargs):
        # ti = kwargs['ti']
        # algo_list = ti.xcom_pull(key='possible_algo', task_ids='get_possible_algo')
        algo_id = 1
        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        #anova

        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]
        algo_list = feature_params_dict["algo_list"]
        
        if algo_id not in algo_list: return 1
        
        anova_col = self.get_anova_info(DBObject,connection,dataset_id,schema_id,target_col)   
        anova_col.pop(target_col, 'No Key found')
        anova_dict = {"name" : "Anova F-test","column" : anova_col}
        logging.info(" +anova"+str(anova_dict))   
        kwargs['ti'].xcom_push(key='anova', value=anova_dict)

    def rfe_fs(self,**kwargs):
        # ti = kwargs['ti']
        # algo_list = ti.xcom_pull(key='possible_algo', task_ids='get_possible_algo')
        algo_id = 5
        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        #RFE

        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]
        algo_list = feature_params_dict["algo_list"]
        
        if algo_id not in algo_list: return 1
        
        rfe_col = self.get_RFE(DBObject,connection,dataset_id,schema_id,target_col)
        rfe_col.pop(target_col, 'No Key found')
        rfe_dict = {"name" : "Recursive Feature Elimination","column" : rfe_col}
        logging.info(" +rfe"+str(rfe_dict))
        kwargs['ti'].xcom_push(key='rfe', value=rfe_dict)

    def coorelation_fs(self,**kwargs):
        # ti = kwargs['ti']
        # algo_list = ti.xcom_pull(key='possible_algo', task_ids='get_possible_algo')
        algo_id = 3 
        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        #coorelation

        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]
        algo_list = feature_params_dict["algo_list"]
        
        if algo_id not in algo_list: return 1
        
        co_col = self.get_coorelation(DBObject,connection,dataset_id,schema_id,target_col)
        co_col.pop(target_col, 'No Key found')
        co_dict = {"name" : "Coorelation","column" : co_col}
        logging.info(" +co"+str(co_dict))
        kwargs['ti'].xcom_push(key='co', value=co_dict)

    
    def end_fs(self,**kwargs):
        ti = kwargs['ti']
        feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        dataset_id = feature_params_dict["dataset_id"]
        schema_id = feature_params_dict["schema_id"]
        target_col = feature_params_dict["target_col"]

        chisq_return_dict = ti.xcom_pull(key='chisq', task_ids='chisq_fs')
        mutual_return_dict = ti.xcom_pull(key='mutual', task_ids='mutual_fs')
        anova_return_dict = ti.xcom_pull(key='anova', task_ids='anova_fs')
        rfe_return_dict = ti.xcom_pull(key='rfe', task_ids='rfe_fs')
        co_return_dict = ti.xcom_pull(key='co', task_ids='coorelation_fs')
        logging.info(" +dict return"+str(co_return_dict))
        
        data_store = {"target_col":target_col,"option_list":[i for i in [chisq_return_dict,mutual_return_dict,anova_return_dict,rfe_return_dict,co_return_dict] if i != None]}
        
        logging.info(" +data_stroe"+str(data_store))
        status = self.insert_feature_record(DBObject,connection,schema_id,data_store)
        return status


    def data_availablity_fs(self,schema_id,targetcol):

        try:
            sql_command = f"select feature_value from mlaas.feature_info_tbl where schema_id='{schema_id}';"
            data_dict = DBObject.select_records(connection,sql_command)
            if len(data_dict) == 0:
                return False

            val = str(data_dict['feature_value'].values[0])
            val = ast.literal_eval(val)
            name = val['target_col'] 
            

            if name != targetcol:
                try:
                    logging.info("+val"+str(val['target_col']))
                    sql_command = f"delete from mlaas.feature_info_tbl where schema_id='{schema_id}';"
                    status = DBObject.delete_records(connection,sql_command)
                    return False
                except Exception as e:
                    return False
            else:
                
                column = self.algo_call(schema_id,targetcol)
                data = {"column_list":column,"data":val}

                return data

        except Exception as e:
            return e

    def get_possible_fs_algo(self,schema_id,target_name,project_type):
        # feature_params_dict = ast.literal_eval(kwargs['dag_run'].conf['feature_params_dict'])
        # dataset_id = feature_params_dict["dataset_id"]
        # schema_id = feature_params_dict["schema_id"]
        # target_name = feature_params_dict["target_col"]

        # Getting Target_Column type
        sql_command = f"select data_type from mlaas.schema_tbl st where st.schema_id = {schema_id} and (st.column_name='{target_name}' or st.changed_column_name='{target_name}')"
        datatype_df = DBObject.select_records(connection,sql_command)

        if not isinstance(datatype_df,pd.DataFrame):
            return #Raise an exception here, failed to fatch data

        if len(datatype_df) == 0:
            return #No datafound

        target_datatype = datatype_df['data_type'][0]
        
        sql_command = f"select id from mlaas.feature_master_tbl where algo_target_type = '{target_datatype}' or algo_target_type is null ;"     
        
        algo_dtype = DBObject.select_records(connection,sql_command)  

        fs_lst = list(algo_dtype['id'])

        # kwargs['ti'].xcom_push(key='possible_algo', value=fs_lst)
        return fs_lst


    def get_fs_activity_desc(self,project_name,activity_id):
        """This function will replace * into project name and get activity description of scale and split.

        Args:
        project_name[String]: get project name
        activity_id[Integer]: get activity id

        Returns:
            [String]: activity_description
        """
        #project_name = '"'+project_name+'"'
        sql_command = f"select replace (amt.activity_description, '*', '{project_name}') as description from mlaas.activity_master_tbl amt where amt.activity_id = '{activity_id}'"
        desc_df = DBObject.select_records(connection,sql_command)
        activity_description = desc_df['description'][0]

        return activity_description

        
