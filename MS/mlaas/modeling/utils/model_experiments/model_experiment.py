'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


# import pandas as pd
from .db import DBClass
import json

class ExperimentClass:
    
    def __init__(self,experiment_id,experiment_name,run_uuid,project_id,dataset_id,
                user_id,model_id,model_mode,DBObject, connection,connection_string):
        
        self.run_uuid = run_uuid
        self.experiment_id = experiment_id
        self.experiment_name = experiment_name
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.user_id = user_id
        self.model_id = model_id
        self.model_mode = model_mode
        
        # self.database="postgres"
        # self.user = "postgres" 
        # self.password = "admin"
        # self.host = "postgresql"
        # self.port = "5432"

    # def get_db_connection(self):
        
    #     DbObject = DBClass()
    #     connection,connection_string = DbObject.database_connection(self.database,
    #                                                                 self.user,
    #                                                                 self.password,
    #                                                                 self.host,
    #                                                                 self.port)
        
    #     return DbObject,connection,connection_string
        
        
    def add_experiments(self, DBObject, connection, connection_string):
        
        # DbObject,connection,connection_string = self.get_db_connection()
        
        table_name='mlaas.model_experiment_tbl'
        cols = 'experiment_id,experiment_name,run_uuid,project_id ,dataset_id,user_id,model_id,model_mode' 
        
        row = self.experiment_id,self.experiment_name,self.run_uuid,self.project_id ,self.dataset_id,self.user_id,self.model_id,self.model_mode    
        row_tuples = [tuple(row)]
        
        experiment_status = DBObject.insert_records(connection,table_name,row_tuples,cols)
        
        return experiment_status
           
            
    def learning_curve(self, experiment_id, DBObject, connection):
        # DbObject,connection,connection_string = self.get_db_connection()
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = DBObject.select_records(connection, sql_command).iloc[0,0]
        learning_curve_uri = artifact_uri + '/learning_curve.json'
        json_data = open(learning_curve_uri, 'r')
        learning_curve = json_data.read()
        return learning_curve



    def actual_vs_prediction(self, experiment_id, DBObject, connection):
        # DbObject,connection,connection_string = self.get_db_connection()
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = DBObject.select_records(connection, sql_command).iloc[0,0]
        actual_vs_prediction_uri = artifact_uri + '/predictions.json'
        json_data = open(actual_vs_prediction_uri, 'r')
        actual_vs_prediction = json_data.read()
        return actual_vs_prediction

    
    def features_importance(self, experiment_id, DBObject, connection):
        # DbObject,connection,connection_string = self.get_db_connection()
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = DBObject.select_records(connection, sql_command).iloc[0,0]
        features_importance_uri = artifact_uri + '/features_importance.json'
        json_data = open(features_importance_uri, 'r')
        features_importance = json_data.read()
        return features_importance

    
    def model_summary(self, experiment_id, DBObject, connection):
        # DbObject,connection,connection_string = self.get_db_connection()
        sql_command = 'select artifact_uri from runs where experiment_id='+str(experiment_id)
        artifact_uri = DBObject.select_records(connection, sql_command).iloc[0,0]
        model_summary_uri = artifact_uri + '/model_summary.json'
        json_data = open(model_summary_uri, 'r')
        model_summary = json_data.read()
        return model_summary
    
    def performance_metrics(self, experiment_id, DBObject, connection): # Remaining
        # DbObject,connection,connection_string = self.get_db_connection()
        sql_command = 'select run_uuid from runs where experiment_id='+str(experiment_id)
        run_uuid = DBObject.select_records(connection, sql_command).iloc[0, 0]
        
        sql_command = "select key, value from metrics where run_uuid='"+str(run_uuid) +"'"
        metrics_df = DBObject.select_records(connection, sql_command).set_index('key') 
        metrics_df.index.name = None
        metrics_json = metrics_df.iloc[:, 0].to_json()
        print(metrics_json)
        return metrics_json

    def accuracy_metrics(self, experiment_id, DBObject, connection):
        from pandas import DataFrame

        sql_command = 'select run_uuid from runs where experiment_id='+str(experiment_id)
        run_uuid = DBObject.select_records(connection, sql_command).iloc[0, 0]
        
        sql_command = "select key,value from metrics where run_uuid='"+str(run_uuid)+"' and (key='cv_score' or key='holdout_score')"
        accuracy_df = DBObject.select_records(connection, sql_command).set_index('key') 
        # accuracy_dict = {}
        # if 'cross_validation' in accuracy_df.index:
        #     accuracy_dict['cross_validation'] = [accuracy_df.loc['cross_validation', 'value']]
        # else:
        #     accuracy_dict['cross_validation'] = [None]
        
        # if 'holdout' in accuracy_df.index:
        #     accuracy_dict['holdout'] = [accuracy_df.loc['holdout', 'value']]
        # else:
        #     accuracy_dict['holdout'] = [None]
        
        accuracy_json = accuracy_df.to_json()
        # metrics_json = metrics_df.loc[['c']]
        return accuracy_json

    def model_name_desc(self, experiment_id, DBObject, connection):
        sql_command = 'select model_id from mlaas.model_experiment_tbl where experiment_id='+str(experiment_id)
        model_id = DBObject.select_records(connection, sql_command)['model_id'][0]
        # print('Model_ID', model_id)
        sql_command = 'select model_name,model_desc from mlaas.model_master_tbl where model_id='+str(model_id)
        df = DBObject.select_records(connection, sql_command)
        # print(df)
        model_name = df['model_name'][0]
        model_desc = df['model_desc'][0]

        return model_name, model_desc


    def final_model_desc(self, experiment_id, DBObject, connection):
        sql_command = 'select model_id from mlaas.model_experiment_tbl where experiment_id='+str(experiment_id)
        model_id = DBObject.select_records(connection, sql_command)['model_id'][0]
        # print('Model_ID', model_id)
        sql_command = 'select model_name,model_desc from mlaas.model_master_tbl where model_id='+str(model_id)
        df = DBObject.select_records(connection, sql_command)
        # print(df)
        model_name = df['model_name'][0]
        model_desc = df['model_desc'][0]

        # from pandas import DataFrame
        sql_command = 'select run_uuid from runs where experiment_id='+str(experiment_id)
        run_uuid = DBObject.select_records(connection, sql_command).iloc[0, 0]
        
        sql_command = "select key,value from metrics where run_uuid='"+str(run_uuid)+"' and (key='cv_score' or key='holdout_score')"
        accuracy_df = DBObject.select_records(connection, sql_command).set_index('key') 
        # accuracy_dict = {}
        # if 'cross_validation' in accuracy_df.index:
        #     accuracy_dict['cross_validation'] = [accuracy_df.loc['cross_validation', 'value']]
        # else:
        #     accuracy_dict['cross_validation'] = [None]
        
        # if 'holdout' in accuracy_df.index:
        #     accuracy_dict['holdout'] = [accuracy_df.loc['holdout', 'value']]
        # else:
        #     accuracy_dict['holdout'] = [None]
        
        accuracy_json = accuracy_df.to_json()

        return model_id, experiment_id, model_name, model_desc, accuracy_json






    # def get_hyperparameters_values(self, experiment_id, DBObject, connection):
    #     # DbObject,connection,connection_string = self.get_db_connection()
    #     sql_command = 'select run_uuid from runs where experiment_id='+experiment_id
    #     run_uuid = DBObject.select_records(connection, sql_command).iloc[0, 0]

    #     sql_command = 'select key, value from params where run_uuid='+run_uuid
    #     hyperparameters = DBObject.select_records(connection, sql_command)
    #     hyperparameters_json = hyperparameters.set_index('key')['value'].to_json()
    #     return hyperparameters_json
    