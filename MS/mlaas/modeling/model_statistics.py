
import json
import pandas as pd


import logging
import traceback
from common.utils.logger_handler import custom_logger as cl

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
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
        learning_curve_uri = artifact_uri + '/learning_curve.json'
        json_data = open(learning_curve_uri, 'r')
        learning_curve = json_data.read()
        return learning_curve


    def actual_vs_prediction(self, experiment_id):
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
        actual_vs_prediction_uri = artifact_uri + '/predictions.json'
        json_data = open(actual_vs_prediction_uri, 'r')
        actual_vs_prediction = json_data.read()
        return actual_vs_prediction

    
    def features_importance(self, experiment_id):
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
        features_importance_uri = artifact_uri + '/features_importance.json'
        json_data = open(features_importance_uri, 'r')
        features_importance = json_data.read()
        return features_importance

    
    def model_summary(self, experiment_id):
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = self.DBObject.select_records(self.connection, sql_command).iloc[0,0]
        model_summary_uri = artifact_uri + '/model_summary.json'
        json_data = open(model_summary_uri, 'r')
        model_summary = json_data.read()
        return model_summary
    
    def performance_metrics(self, experiment_id): # Remaining
        sql_command = 'select run_uuid from runs where experiment_id='+str(experiment_id)
        run_uuid = self.DBObject.select_records(self.connection, sql_command).iloc[0, 0]
        
        sql_command = "select key, value from metrics where run_uuid='"+str(run_uuid) +"'"
        metrics_df = self.DBObject.select_records(self.connection, sql_command).set_index('key') 
        metrics_df.index.name = None
        metrics_json = metrics_df.iloc[:, 0].to_json()
        print(metrics_json)
        return metrics_json

    # def accuracy_metrics(self, experiment_ids):
        

    #     sql_command = 'select run_uuid from runs where experiment_id in'+str(experiment_ids)
    #     run_uuids = tuple(self.DBObject.select_records(self.connection, sql_command)['run_uuid'])
        
    #     sql_command = "select key,value from metrics where run_uuid in"+str(run_uuids)+" and (key='cv_score' or key='holdout_score')"
    #     accuracy_df = self.DBObject.select_records(self.connection, sql_command).set_index('key') 
        
    #     return accuracy_df
    
    # def show_model_details(self, project_id):
    #     sql_command = 'select ms.model_id,ms.model_name,ms.model_desc,exp.experiment_id from mlaas.model_experiment_tbl exp,mlaas.model_master_tbl ms where exp.model_id = ms.model_id and exp.project_id ='+str(project_id)
    #     model_details_df = self.DBObject.select_records(self.connection, sql_command)
        
    #     experiment_ids = tuple(model_details_df['experiment_id'])
    #     accuracy_df = self.accuracy_metrics(experiment_ids)
        
    #     model_details_json = model_details_df.to_json()
    #     accuracy_json = accuracy_df.to_json()
       
    #     return model_details_json,accuracy_json


    # def accuracy_metrics2(self, project_id):
        
    #     sql_command = "select value as cv_score from metrics where run_uuid in (select run_uuid from runs where experiment_id in (select experiment_id from mlaas.model_experiment_tbl where project_id = " + str(project_id ) + ")) and (key='cv_score')"
    #     sql_command2 = "select value as holdout_score from metrics where run_uuid in (select run_uuid from runs where experiment_id in (select experiment_id from mlaas.model_experiment_tbl where project_id = " + str(project_id ) + ")) and (key='holdout_score')"
    #     cv_df = self.DBObject.select_records(self.connection, sql_command)
    #     holdout_df = self.DBObject.select_records(self.connection, sql_command2)
    #     accuracy_df = pd.merge(cv_df, holdout_df, left_index=True, right_index=True)
        
    #     return accuracy_df

    def accuracy_metrics(self, project_id):
        
        sql_command = "select key, value from metrics where run_uuid in (select run_uuid from runs where experiment_id in (select experiment_id from mlaas.model_experiment_tbl where project_id = " + str(project_id ) + ")) and (key='cv_score' or key='holdout_score')"
        df = self.DBObject.select_records(self.connection, sql_command)
        cv_score_df = df[df['key'] == 'cv_score'].reset_index(drop=True).rename(columns={'value': 'cv_score'})['cv_score']
        holdout_score_df = df[df['key'] == 'holdout_score'].reset_index(drop=True).rename(columns={'value': 'holdout_score'})['holdout_score']
        accuracy_df = pd.merge(cv_score_df, holdout_score_df, left_index=True, right_index=True)

        return accuracy_df



    def show_model_details(self, project_id):
        sql_command = 'select ms.model_id,ms.model_name,ms.model_desc,exp.experiment_id from mlaas.model_experiment_tbl exp,mlaas.model_master_tbl ms where exp.model_id = ms.model_id and exp.project_id ='+str(project_id)
        model_details_df = self.DBObject.select_records(self.connection, sql_command)
        
        accuracy_df = self.accuracy_metrics(project_id)

        final_df = pd.merge(accuracy_df, model_details_df, right_index=True, left_index=True)
        json_data = final_df.to_json(orient='records',date_format='iso')
        final_model_data = json.loads(json_data)

        return final_model_data


    def show_experiments_list(self, project_id):
        # Get the necessary values from the mlaas.model_experiment_tbl
        sql_command = 'select experiment_id, model_mode, exp_created_on from mlaas.model_experiment_tbl where project_id='+str(project_id)
        model_experiment_tbl_data = self.DBObject.select_records(self.connection, sql_command)

        # Get the name of the experiments
        experiment_ids = tuple(model_experiment_tbl_data['experiment_id'])
        sql_command = 'select name as experiment_name from experiments where experiment_id in'+str(experiment_ids)
        exp_names = self.DBObject.select_records(self.connection, sql_command)['experiment_name']
        
        # Get the name of the models, associated with their respective model_id
        sql_command = 'select mmt.model_name from mlaas.model_master_tbl mmt inner join mlaas.model_experiment_tbl met on mmt.model_id = met.model_id'
        model_names = self.DBObject.select_records(self.connection, sql_command)['model_name']
        
        # Get the name of the datasets associated with their respective dataset_id
        sql_command = 'select dbt.dataset_name from mlaas.dataset_tbl dbt inner join mlaas.model_experiment_tbl met on dbt.dataset_id = met.dataset_id'
        dataset_names = self.DBObject.select_records(self.connection, sql_command)['dataset_name']

        # Get the cv_score and holdout_score associated with the project_id
        accuracy_df = self.accuracy_metrics(project_id)

        # Get the experiment creation dates
        exp_creation_dates = model_experiment_tbl_data['exp_created_on']

        # Get the model mode
        model_modes = model_experiment_tbl_data['model_mode']

        # Merging all the Dataframes and Series to get the final Df.
        final_df = pd.DataFrame([exp_names, model_names, dataset_names, exp_creation_dates, model_modes, accuracy_df['cv_score'], accuracy_df['holdout_score']]).T

        # Converting final_df to json
        json_data = final_df.to_json(orient='records',date_format='iso')
        final_data = json.loads(json_data)

        return final_data

    # def get_hyperparameters_values(self, experiment_id):
    #     # DbObject,connection,connection_string = self.get_db_connection()
    #     sql_command = 'select run_uuid from runs where experiment_id='+experiment_id
    #     run_uuid = self.DBObject.select_records(self.connection, sql_command).iloc[0, 0]

    #     sql_command = 'select key, value from params where run_uuid='+run_uuid
    #     hyperparameters = self.DBObject.select_records(self.connection, sql_command)
    #     hyperparameters_json = hyperparameters.set_index('key')['value'].to_json()
    #     return hyperparameters_json
    