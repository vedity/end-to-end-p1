
import json
import pandas as pd
import ast

from pandas import DataFrame
import logging
import traceback
from common.utils.logger_handler import custom_logger as cl
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *
from common.utils.exception_handler.python_exception.common.common_exception import *
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *
# from MS.mlaas.modeling.views import SelectAlgorithmClass

user_name = 'admin'
log_enable = True
 
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
 
logger = logging.getLogger('view')



class ModelStatisticsClass:

    def __init__(self, db_param_dict):
        
        self.DBObject = db_param_dict['DBObject']
        self.connection = db_param_dict['connection']

    
    def learning_curve(self, experiment_id):
        """This function is used to get learning curve of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for learning curve.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution start")
            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the learning curve's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command) 
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500) 
                
            artifact_uri = artifact_uri.iloc[0,0]
            learning_curve_uri = artifact_uri + '/learning_curve.json'
            
            with open(learning_curve_uri, "r") as rf: # Read the learning curve's data from mlruns.
                learning_curve_json = json.load(rf)
           

            learning_curve_rounded_df = pd.DataFrame(learning_curve_json).round(3)
            learning_curve_json = learning_curve_rounded_df.to_dict(orient='list')
           
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end")
            return learning_curve_json

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : learning_curve : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : learning_curve : " +traceback.format_exc())
            return exc.msg
        


    def actual_vs_prediction(self, experiment_id):
        """This function is used to get actuval_vs_prediction of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for actual_vs_prediction.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution start")

            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the actual_vs_predction's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500) 

            artifact_uri = artifact_uri.iloc[0,0]
            actual_vs_prediction_uri = artifact_uri + '/predictions.json'

            with open(actual_vs_prediction_uri, "r") as rf: # Read the actual vs prediction data from mlaas.runs
                actual_vs_prediction_json = json.load(rf)
                
            actual_vs_prediction_df = DataFrame(actual_vs_prediction_json).round(decimals = 3) #Round to the nearest 3 decimals.
            actual_vs_prediction_json = actual_vs_prediction_df.to_dict(orient='list')

            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
            return actual_vs_prediction_json

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : actual_vs_prediction : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : actual_vs_prediction : " +traceback.format_exc())
            return exc.msg

    def features_importance(self, experiment_id):
        """This function is used to get features_importance of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for features_importance.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : features_importance : execution end")
            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the features importance's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
    
            if artifact_uri is None:
                  raise DatabaseConnectionFailed(500)
            
            if len(artifact_uri) == 0:# If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)
            
            artifact_uri = artifact_uri.iloc[0,0]
            features_importance_uri = artifact_uri + '/features_importance.json'
            
            with open(features_importance_uri, "r") as rf:# Read the features importance data from mlruns.
                features_importance_json = json.load(rf)

            # features_importance_rounded_df = pd.DataFrame(features_importance_json).round(decimals = 2)
            # features_importance_json = features_importance_rounded_df.to_dict(orient='list')
            
            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
            return features_importance_json
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : features_importance : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : features_importance : " +traceback.format_exc())
            return exc.msg

        

    
    def model_summary(self, experiment_id):
        """This function is used to get model_summary of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for model_summary.]
            
        """
        try:

            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the model summary's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)

            artifact_uri=artifact_uri.iloc[0,0]
            model_summary_uri = artifact_uri + '/model_summary.json'
            
            with open(model_summary_uri, "r") as rf: # Read the model_summary's data from mlaas.runs
                model_summary = json.load(rf)

            sql_command = 'select model_desc from mlaas.model_master_tbl mmt, mlaas.model_experiment_tbl met where mmt.model_id=met.model_id and met.experiment_id='+str(experiment_id)

            model_desc = self.DBObject.select_records(self.connection, sql_command)
            if model_desc is None:
                raise DatabaseConnectionFailed(500)

            elif len(model_desc) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)
            
            model_desc = model_desc.iloc[0, 0]

            model_summary.update({'Model_Description': model_desc})

            return model_summary

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : model_summary : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : model_summary : " +traceback.format_exc())
            return exc.msg
        

    def confusion_matrix(self, experiment_id): #TODO perform
        """This function is used to get model_summary of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for model_summary.]
            
        """
        try:

            sql_command = 'select artifact_uri from mlflow.runs where experiment_id='+str(experiment_id)
            # Get the confusion matrix's data path from mlaas.runs with the associated experiment id
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)

            artifact_uri = artifact_uri.iloc[0,0]
            confusion_matrix_uri = artifact_uri + '/confusion_matrix.json'

            with open(confusion_matrix_uri, "r") as rf: # Read the model_summary's data from mlaas.runs
                confusion_matrix = json.load(rf)
            return confusion_matrix

        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : confusion_matrix : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : confusion_matrix : " +traceback.format_exc())
            return str(exc)
        

    
    
    def performance_metrics(self, experiment_id): # Remaining
        """This function is used to get features_importance of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for performance_metrics.]
            
        """
        try:
            sql_command = 'select mtr.key, mtr.value, met.experiment_id from mlflow.metrics mtr, mlaas.model_experiment_tbl met where mtr.run_uuid=met.run_uuid and met.experiment_id='+str(experiment_id)
            perform_metrics_df = self.DBObject.select_records(self.connection, sql_command)
            if perform_metrics_df is None:
                raise DatabaseConnectionFailed(500)

            if len(perform_metrics_df) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)

            perform_pivot_df = perform_metrics_df.pivot(columns='key', values='value', index='experiment_id').round(2)
            sql_command = 'select met.experiment_id, met.exp_created_on, mmt.model_name from mlaas.model_experiment_tbl met, mlaas.model_master_tbl mmt where mmt.model_id=met.model_id and met.experiment_id='+str(experiment_id)
            experiment_df = self.DBObject.select_records(self.connection, sql_command)
            if experiment_df is None:
                raise DatabaseConnectionFailed(500)

            if len(experiment_df) == 0: # If the experiment_id is not present in the mlaas.runs.
                raise DataNotFound(500)
            experiment_df = experiment_df.set_index('experiment_id')
            merged_df = pd.merge(experiment_df, perform_pivot_df, left_index=True, right_index=True)
            final_dict = merged_df.to_dict(orient='records')[0]
            return {'key': final_dict.keys(), 'value': final_dict.values()}

        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        

    def show_running_experiments(self, project_id):
        """This function is used to get experiments_list of particular project.

        Args:
            project_id ([object]): [Project id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe of experiments_list.]
            
        """
        try:
            # Get the necessary values from the mlaas.model_experiment_tbl where the state of the experiment is 'running'.
            sql_command = "select met.*,e.name as experiment_name,mmt.model_name, mmt.model_type,dt.dataset_name, 0.0 as cv_score, 0.0 as holdout_score"\
                          " from mlaas.model_experiment_tbl met,mlaas.model_master_tbl mmt,mlaas.dataset_tbl dt,mlflow.experiments e"\
                          " where met.model_id = mmt.model_id and met.dataset_id=dt.dataset_id and met.experiment_id=e.experiment_id "\
                          " and met.project_id="+str(project_id)+" and status='running'"
                          
            model_experiment_data_df = self.DBObject.select_records(self.connection, sql_command)
            if model_experiment_data_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_experiment_data_df) == 0:# If there are no experiments for a particular project_id.
                sql_command = ''
                return []
            # Converting final_df to json
            json_data = model_experiment_data_df.to_json(orient='records',date_format='iso')
            final_data = json.loads(json_data)
            return final_data
        except (DatabaseConnectionFailed,ModelIsStillInQueue) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg

    def check_running_experiments(self, project_id):
        
        sql_command = "select exp_name from mlaas.model_dags_tbl mdt,dag_run dr where mdt.run_id=dr.run_id"\
                      " and dr.state in ('running') and mdt.project_id={}".format(project_id)
        exp_name = self.DBObject.select_records(self.connection, sql_command)

        if exp_name is None:
            raise DatabaseConnectionFailed(500)

        if len(exp_name) == 0:# If there are no experiments for a particular project_id.
            return {'exp_name': ''}
        
        exp_name = exp_name['exp_name'][0]
        
        return {'exp_name': exp_name}


    def show_all_experiments(self, project_id):
        """This function is used to get experiments_list of particular project.

        Args:
            project_id ([object]): [Project id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe of experiments_list.]
            
        """
        try:
            # Get everything from model_experiment_tbl and, experiment name, model_name and dataset_name associated with a particular project_id.
            sql_command = "select met.*,e.name as experiment_name,mmt.model_name, mmt.model_type,dt.dataset_name,"\
                          "round(cast(sv.cv_score as numeric),3) as cv_score,round(cast(sv.holdout_score as numeric),3) as holdout_score "\
                          " from mlaas.model_experiment_tbl met,mlaas.model_master_tbl mmt,mlaas.score_view sv,mlaas.dataset_tbl dt,mlflow.experiments e"\
                          " where met.model_id = mmt.model_id and met.experiment_id=sv.experiment_id and met.dataset_id=dt.dataset_id and met.experiment_id=e.experiment_id "\
                          " and met.project_id="+str(project_id)+" order by met.exp_created_on desc"
                          
            model_experiment_data_df = self.DBObject.select_records(self.connection, sql_command)

            if model_experiment_data_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_experiment_data_df) == 0:# If there are no experiments for a particular project_id.
                return []
            # Converting final_df to json
            json_data = model_experiment_data_df.to_json(orient='records',date_format='iso')
            final_data = json.loads(json_data)
            return final_data
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg
        
        
    def check_model_status(self,project_id,experiment_name):
        """This function is used to check the 'state' of the given experiment.

        Args:
            project_id (int): project_id
            experiment_name (string): experiment's name

        Raises:
            DatabaseConnectionFailed: If the connection is not established with the Database.
            DataNotFound: If there is no data in the database for a particular query.

        Returns:
            [string]: state of the experiment
        """
        
        try:
            # Get dag_id and run_id from the model_dags_tbl with associated experiment_name.
            sql_command ="select dag_id,run_id from mlaas.model_dags_tbl where project_id="+str(project_id)+" and exp_name='"+experiment_name+"'"
            
            dag_df = self.DBObject.select_records(self.connection, sql_command)

            if dag_df is None:
                raise DatabaseConnectionFailed(500)

            if len(dag_df) == 0 :
                return 0
            
            dag_id,run_id = dag_df['dag_id'][0],dag_df['run_id'][0]
            
            # Get the state of the experiment associated with run_id.
            sql_command = "select state from dag_run where dag_id='"+dag_id+"' and run_id='"+run_id +"'"
            state_df = self.DBObject.select_records(self.connection, sql_command)
            
            if state_df is None:
                raise DatabaseConnectionFailed(500)

            if len(state_df) == 0 :
                raise DataNotFound(500)

            # Update Project Status 
            status = state_df['state'][0]
            if status == 'running':
                st=0
            elif status == 'success':
                st=1
            else:
                st=2
            
            # Update the model_status in the project table.
            sql_command = "update mlaas.project_tbl set model_status="+str(st)+" where project_id="+str(project_id)
            project_upd_status = self.DBObject.update_records(self.connection,sql_command)
            #status=state_df['state'][0]
            return st
        
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg
    

    def check_existing_experiment(self,project_id, experiment_name):
        """Checks if the experiment_name entered by the user already exists in a particular project id or not.

        Args:
            experiment_name ([string]): User entered experiment name.

        Raises:
            ExperimentAlreadyExist: [This experiment already exist, so enter a new,unique experiment name.]

        Returns:
            integer: status code of the experiment_name exists.
        """
        try:
            # Get the experiment's name from the model_dag_tbl
            sql_command="select * from mlaas.model_dags_tbl where exp_name='"+experiment_name+"' and project_id="+str(project_id)
            experiment_data_df = self.DBObject.select_records(self.connection, sql_command)

            if experiment_data_df is None: # If the database connection fails.
                return 0
            elif len(experiment_data_df) > 0: # If the experiment name already exists.
                raise ExperimentAlreadyExist(500)
            else:
                return 0
    
        except (ExperimentAlreadyExist) as exc:
            logging.error("modeling : ModelStatisticsClass : check_existing_experiment : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : check_existing_experiment : " +traceback.format_exc())
            return exc.msg

        
    def compare_experiments(self, experiment_ids):
        """This function is called when user wants to compare multiple experiments.

        Args:
            experiment_ids ([tuple]): It contains all the experiment ids.

        Raises:
            DatabaseConnectionFailed: If the database connection is not established.
            DataNotFound: If the entry for the query is not found in the database.

        Returns:
            Dictionary: It contains the accuracy_metrics, model_name, model_params, and the associated experiment_id.
        """
            # Get the model parameters for the associated experiment_ids.
        try:
            exp_ids = tuple(experiment_ids)
            sql_command = 'select prms.key, prms.value, met.experiment_id from mlflow.params prms,mlaas.model_experiment_tbl met where prms.run_uuid=met.run_uuid and met.experiment_id in'+str(exp_ids)
            params_df = self.DBObject.select_records(self.connection, sql_command)
            if params_df is None:
                raise DatabaseConnectionFailed(500)

            if len(params_df) == 0 :
                raise DataNotFound(500)
            # Rearraging Dataframe according to our requirement.
            params_pivot_df = params_df.pivot(index='experiment_id', columns='key', values='value')
            
            # Get the accuracy metrics for the associated experiment_ids.
            sql_command = 'select mtr.key, mtr.value, met.experiment_id from mlflow.metrics mtr,mlaas.model_experiment_tbl met where mtr.run_uuid=met.run_uuid and met.experiment_id in'+str(exp_ids)
            metrics_df = self.DBObject.select_records(self.connection, sql_command)
            if metrics_df is None:
                raise DatabaseConnectionFailed(500)

            if len(metrics_df) == 0 :
                raise DataNotFound(500)
            # Rearraging Dataframe according to our requirement.
            metrics_pivot_df = metrics_df.pivot(index='experiment_id', columns='key', values='value')
            
            
            # Get the model_name for the associated experiment_ids.
            sql_command = 'select mmt.model_name, met.experiment_id from mlaas.model_master_tbl mmt, mlaas.model_experiment_tbl met where mmt.model_id=met.model_id and met.experiment_id in '+str(exp_ids)
            model_names_df = self.DBObject.select_records(self.connection, sql_command)
            if model_names_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_names_df) == 0 :
                raise DataNotFound(500)
            
            model_names_df = model_names_df.set_index('experiment_id') # Set index to experiment_id

            metrics_params_df = metrics_pivot_df.merge(params_pivot_df, left_index=True, right_index=True)

            final_df = model_names_df.merge(metrics_params_df, left_index=True, right_index=True)
            
            sql_command = "select exp_name from mlaas.model_dags_tbl mdt, mlaas.model_experiment_tbl met where mdt.run_id=met.dag_run_id"\
                          " and met.experiment_id in "+str(exp_ids)

            exp_names = tuple(self.DBObject.select_records(self.connection, sql_command)['exp_name'])

            final_df['experiment_name'] = exp_names
            columns = final_df.columns.values

            return {'column_names': columns, 'responsedata': final_df.to_dict(orient='records')}

        except (ExperimentAlreadyExist) as exc:
            logging.error("modeling : ModelStatisticsClass : check_existing_experiment : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : check_existing_experiment : " +traceback.format_exc())
        return exc.msg


