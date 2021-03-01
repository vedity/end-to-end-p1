
import json
import pandas as pd

from pandas import DataFrame
import logging
import traceback
from common.utils.logger_handler import custom_logger as cl
# from MS.mlaas.modeling.views import SelectAlgorithmClass

user_name = 'admin'
log_enable = True
 
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
 
logger = logging.getLogger('view')



class ModelStatisticsClass:

    def __init__(self, DBObject, connection):
        self.DBObject = DBObject
        self.connection = connection

    
    def learning_curve(self, experiment_id):
        """This function is used to get learning curve of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for learning curve.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution start")
            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end"+str(experiment_id))
            
            artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end"+str(artifact_uri))
            learning_curve_uri = artifact_uri + '/learning_curve.json'
            # json_data = open(learning_curve_uri, 'r')
            # learning_curve = json_data.read()
            with open(learning_curve_uri, "r") as rf:
                learning_curve_df = json.load(rf)

            #learning_curve = pd.DataFrame.from_dict(decoded_data)
            learning_curve_rounded_df = DataFrame(learning_curve_df, columns = ['train_size','train_score','test_score']).round(decimals = 2)
            # learning_curve = dict()
            # for key in decoded_data:
            #     learning_curve[key] = round(decoded_data[key], 2)            
            # return learning_curve
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : learning_curve : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : learning_curve : " +traceback.format_exc())
            return str(exc)
        return learning_curve_rounded_df


    def actual_vs_prediction(self, experiment_id):
        """This function is used to get actuval_vs_prediction of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for actual_vs_prediction.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution start")

            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
            actual_vs_prediction_uri = artifact_uri + '/predictions.json'
            # json_data = open(actual_vs_prediction_uri, 'r')
            # actual_vs_prediction = json_data.read()
            with open(actual_vs_prediction_uri, "r") as rf:
                actual_vs_prediction_df = json.load(rf)

            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : actual_vs_prediction : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : actual_vs_prediction : " +traceback.format_exc())
            return str(exc)
        return actual_vs_prediction_df


    
    def features_importance(self, experiment_id):
        """This function is used to get features_importance of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for features_importance.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : features_importance : execution end")
            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
            features_importance_uri = artifact_uri + '/features_importance.json'
            #json_data = open(features_importance_uri, 'r')
            #features_importance = json_data.read()
            with open(features_importance_uri, "r") as rf:
                features_importance_df = json.load(rf)

            features_importance_rounded_df = pd.DataFrame(features_importance_df).round(decimals = 2)
            #features_importance_rounded_df = features_importance_rounded_df.sort_values('norm_importance',ascending = False)
            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : features_importance : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : features_importance : " +traceback.format_exc())
            return str(exc)

        return features_importance_rounded_df

    
    def model_summary(self, experiment_id):
        """This function is used to get model_summary of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for model_summary.]
            
        """
        try:

            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
            model_summary_uri = artifact_uri + '/model_summary.json'
            json_data = open(model_summary_uri, 'r')
            model_summary = json_data.read()

        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : model_summary : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : model_summary : " +traceback.format_exc())
            return str(exc)
        return model_summary
    
    def performance_metrics(self, experiment_id): # Remaining
        """This function is used to get features_importance of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for performance_metrics.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : performance_metrics : execution start")            
            sql_command = 'select run_uuid from mlaas.runs where experiment_id='+str(experiment_id)
            run_uuid = self.DBObject.select_records(self.connection, sql_command).iloc[0, 0]
            
            sql_command = "select key, value from mlaas.metrics where run_uuid='"+str(run_uuid) +"'"
            metrics_df = self.DBObject.select_records(self.connection, sql_command).set_index('key')
            metrics_rounded_df = DataFrame(metrics_df, columns = ['value']).round(decimals = 2)

            sql_command = 'select model_id, exp_created_on from mlaas.model_experiment_tbl where experiment_id='+str(experiment_id)
            model_experiment_tbl_data = self.DBObject.select_records(self.connection, sql_command).iloc[0, :]
            sql_command = 'select model_name from mlaas.model_master_tbl where model_id='+str(model_experiment_tbl_data['model_id'])
            model_name = self.DBObject.select_records(self.connection, sql_command).iloc[0, 0]
            
            # final_df = pd.merge(metrics_df, model_name_df, left_index=True, right_index=True)
            # metrics_dict = metrics_df.to_dict()
            # metrics_dict['model_name'] = str(model_name)
            # metrics_json = pd.DataFrame(metrics_dict).to_json()
            
            metrics_json = json.loads(metrics_rounded_df.to_json())
            model_desc = {'model_name': model_name, 'exp_created_on': model_experiment_tbl_data['exp_created_on']}
            metrics_json.update(model_desc)
            logging.info("modeling : ModelStatisticsClass : performance_metrics : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return str(exc)
        return metrics_json


    def accuracy_metrics(self, project_id):
        """This function is used to get accuracy_metrics of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for accuracy_metrics.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : accuracy_metrics : execution start")
            sql_command = 'select experiment_id from mlaas.model_experiment_tbl where project_id='+str(project_id)
            experiment_ids = tuple(self.DBObject.select_records(self.connection, sql_command)['experiment_id'])
            if len(experiment_ids) > 1:
                logging.info(' greater')
                sql_command = "select key, value from mlaas.metrics where run_uuid in (select run_uuid from mlaas.runs where experiment_id in (select experiment_id from mlaas.model_experiment_tbl where project_id = " + str(project_id ) + ")) and (key='cv_score' or key='holdout_score')"
            else:
                logging.info(' SMALLER' + str(experiment_ids[0]))
                
                sql_command = "select key, value from mlaas.metrics where run_uuid= (select run_uuid from mlaas.runs where experiment_id={}) and (key='cv_score' or key='holdout_score')".format(str(experiment_ids[0]))
            df = self.DBObject.select_records(self.connection, sql_command)
            logging.info('DF:- ' + str(df))
            cv_score_df = df[df['key'] == 'cv_score'].reset_index(drop=True).rename(columns={'value': 'cv_score'})['cv_score']
            holdout_score_df = df[df['key'] == 'holdout_score'].reset_index(drop=True).rename(columns={'value': 'holdout_score'})['holdout_score']
            cv_score_rounded_df = DataFrame(cv_score_df, columns = ['cv_score']).round(decimals = 2)
            holdout_score_rounded_df = DataFrame(holdout_score_df, columns = ['holdout_score']).round(decimals = 2)
            accuracy_df = pd.merge(cv_score_rounded_df, holdout_score_rounded_df, left_index=True, right_index=True)
            logging.info("modeling : ModelStatisticsClass : accuracy_metrics : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : accuracy_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : accuracy_metrics : " +traceback.format_exc())
            return str(exc)
        return accuracy_df



    def show_model_details(self, project_id):
        """This function is used to get show_model_details of particular experiment.

        Args:
            experiment_id ([object]): [Experiment id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe for show_model_details.]
            
        """
        try:
            logging.info("modeling : ModelStatisticsClass : show_model_details : execution start")
            sql_command = 'select ms.model_id,ms.model_name,ms.model_desc,exp.experiment_id from mlaas.model_experiment_tbl exp,mlaas.model_master_tbl ms where exp.model_id = ms.model_id and exp.project_id ='+str(project_id)
            model_details_df = self.DBObject.select_records(self.connection, sql_command)
            
            accuracy_df = self.accuracy_metrics(project_id)

            final_df = pd.merge(accuracy_df, model_details_df, right_index=True, left_index=True)
            json_data = final_df.to_json(orient='records',date_format='iso')
            final_model_data = json.loads(json_data)

            logging.info("modeling : ModelStatisticsClass : show_model_details : execution end")
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : show_model_details : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_model_details : " +traceback.format_exc())
            return str(exc)
        return final_model_data


    def show_experiments_list(self, project_id):
        """This function is used to get experiments_list of particular project.

        Args:
            project_id ([object]): [Project id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe of experiments_list.]
            
        """
        try:
            # Get the necessary values from the mlaas.model_experiment_tbl
            sql_command = "select experiment_id, model_mode, exp_created_on, 'completed' status from mlaas.model_experiment_tbl where project_id="+str(project_id)
            logging.info("Model Exp Table:- " + str(project_id))
            model_experiment_tbl_data = self.DBObject.select_records(self.connection, sql_command)
            logging.info("Model Exp Table:- " + str(model_experiment_tbl_data))
            # Get the name of the experiments
            experiment_ids = tuple(model_experiment_tbl_data['experiment_id'])
            logging.info('aaa'+str(experiment_ids))
            if len(experiment_ids) > 1:
                sql_command = 'select name as experiment_name from mlaas.experiments where experiment_id in'+str(experiment_ids)
                exp_names = self.DBObject.select_records(self.connection, sql_command)['experiment_name']
                logging.info("aaaaaaaaaa"+str(exp_names))
            else:
                sql_command = 'select name as experiment_name from mlaas.experiments where experiment_id='+str(experiment_ids[0])
                exp_names = self.DBObject.select_records(self.connection, sql_command)['experiment_name']
            
            # Get the name of the models, associated with their respective model_id
            sql_command = 'select mmt.model_id,mmt.model_name from mlaas.model_master_tbl mmt inner join mlaas.model_experiment_tbl met on mmt.model_id = met.model_id'
            model_df = self.DBObject.select_records(self.connection, sql_command)
            model_names=model_df['model_name']
            
            model_ids =model_df['model_id'] 
            
            # Get the name of the datasets associated with their respective dataset_id
            sql_command = 'select dbt.dataset_name from mlaas.dataset_tbl dbt inner join mlaas.model_experiment_tbl met on dbt.dataset_id = met.dataset_id'
            dataset_names = self.DBObject.select_records(self.connection, sql_command)['dataset_name']

            # Get the cv_score and holdout_score associated with the project_id
            accuracy_df = self.accuracy_metrics(project_id)

            # Get the experiment creation dates
            exp_creation_dates = model_experiment_tbl_data['exp_created_on']

            # Get the model mode
            model_modes = model_experiment_tbl_data['model_mode']

            status_df = model_experiment_tbl_data['status']


            experiment_series = model_experiment_tbl_data['experiment_id']
            # Merging all the Dataframes and Series to get the final Df.
            final_df = pd.DataFrame([experiment_series, status_df, exp_names, model_names,model_ids, dataset_names, exp_creation_dates, model_modes, accuracy_df['cv_score'], accuracy_df['holdout_score']]).T

            ### 
            sql_command ="select mmt.model_id,mmt.model_name,ti.task_id,ti.dag_id,ti.execution_date,ti.state from task_instance ti,mlaas.model_master_tbl mmt where ti.task_id = mmt.model_name and ti.execution_date in (select execution_date from dag_run where run_id in (select run_id from mlaas.model_dags_tbl where project_id ="+str(project_id)+" order by execution_date desc limit 1))"
            dag_df = self.DBObject.select_records(self.connection, sql_command)[['model_id','model_name','state']]
            
            final_df=pd.merge(final_df,dag_df,how='inner',on='model_id')
            # Converting final_df to json
            json_data = final_df.to_json(orient='records',date_format='iso')
            final_data = json.loads(json_data)
        except Exception as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return str(exc)
        return final_data

    