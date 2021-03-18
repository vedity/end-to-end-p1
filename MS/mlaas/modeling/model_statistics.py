
import json
import pandas as pd

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
            
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0 :
                raise DataNotFound(500) 
                
            artifact_uri = artifact_uri.iloc[0,0]
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end"+str(artifact_uri))
            learning_curve_uri = artifact_uri + '/learning_curve.json'
            
            with open(learning_curve_uri, "r") as rf:
                learning_curve_df = json.load(rf)

           
            learning_curve_rounded_df = DataFrame(learning_curve_df).round(decimals = 2)
           
            logging.info("modeling : ModelStatisticsClass : learning_curve : execution end")
            return learning_curve_rounded_df
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

            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0 :
                raise DataNotFound(500) 
            artifact_uri = artifact_uri.iloc[0,0]
            actual_vs_prediction_uri = artifact_uri + '/predictions.json'
            # json_data = open(actual_vs_prediction_uri, 'r')
            # actual_vs_prediction = json_data.read()
            with open(actual_vs_prediction_uri, "r") as rf:
                actual_vs_prediction_df = json.load(rf)
                
            actual_vs_prediction_df = DataFrame(actual_vs_prediction_df).round(decimals = 0)

            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
            return actual_vs_prediction_df
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
            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            ##logging.info("aaaaaaaaaaa111---"+str(artifact_uri))
            if artifact_uri is None:
                  raise DatabaseConnectionFailed(500)
            
            if len(artifact_uri) == 0:
                raise DataNotFound(500)
            
            artifact_uri = artifact_uri.iloc[0,0]
            features_importance_uri = artifact_uri + '/features_importance.json'
            
            with open(features_importance_uri, "r") as rf:
                features_importance_df = json.load(rf)

            features_importance_rounded_df = pd.DataFrame(features_importance_df).round(decimals = 2)
            #features_importance_rounded_df = features_importance_rounded_df.sort_values('norm_importance',ascending = False)
            logging.info("modeling : ModelStatisticsClass : actual_vs_prediction : execution end")
            return features_importance_rounded_df
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

            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            
            if artifact_uri is None:
                raise DatabaseConnectionFailed(500)

            if len(artifact_uri) == 0 :
                raise DataNotFound(500)

            artifact_uri=artifact_uri.iloc[0,0]
            model_summary_uri = artifact_uri + '/model_summary.json'
            # json_data = open(model_summary_uri, 'r')
            # model_summary = json_data.read()
            with open(model_summary_uri, "r") as rf:
                model_summary = json.load(rf)
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

            sql_command = 'select artifact_uri from mlaas.runs where experiment_id='+str(experiment_id)
            artifact_uri = self.DBObject.select_records(self.connection, sql_command)
            # if artifact_uri is None:
            #     raise DatabaseConnectionFailed(500)

            # if len(artifact_uri) == 0 :
            #     raise DataNotFound(500)

            artifact_uri = artifact_uri.iloc[0,0]
            confusion_matrix_uri = artifact_uri + '/confusion_matrix.json'
            json_data = open(confusion_matrix_uri, 'r')
            confusion_matrix = json_data.read()
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
            logging.info("modeling : ModelStatisticsClass : performance_metrics : execution start")            
            sql_command = 'select run_uuid from mlaas.runs where experiment_id='+str(experiment_id)
            run_uuid = self.DBObject.select_records(self.connection, sql_command)
            if run_uuid is None:
                raise DatabaseConnectionFailed(500)

            if len(run_uuid) == 0 :
                raise DataNotFound(500)
            
            run_uuid=run_uuid.iloc[0,0]

            sql_command = "select key, value from mlaas.metrics where run_uuid='"+str(run_uuid) +"'"
            metrics_df = self.DBObject.select_records(self.connection, sql_command).set_index('key')
            if metrics_df is None:
                raise DatabaseConnectionFailed(500)

            if len(metrics_df) == 0 :
                raise DataNotFound(500)
            
            metrics_rounded_df = DataFrame(metrics_df, columns = ['value']).round(decimals = 2)

            sql_command = 'select model_id, exp_created_on from mlaas.model_experiment_tbl where experiment_id='+str(experiment_id)
            model_experiment_tbl_data = self.DBObject.select_records(self.connection, sql_command)

            if model_experiment_tbl_data is None:
                raise DatabaseConnectionFailed(500)

            if len(model_experiment_tbl_data) == 0 :
                raise DataNotFound(500)

            model_experiment_tbl_data=model_experiment_tbl_data.iloc[0, :]
            sql_command = 'select model_name from mlaas.model_master_tbl where model_id='+str(model_experiment_tbl_data['model_id'])
            model_name = self.DBObject.select_records(self.connection, sql_command)

            if model_name is None:
                raise DatabaseConnectionFailed(500)

            if len(model_name) == 0 :
                raise DataNotFound(500)
            
            model_name=model_name.iloc[0,0]
            
            metrics_json = json.loads(metrics_rounded_df.to_json())
            model_desc = {'model_name': model_name, 'exp_created_on': model_experiment_tbl_data['exp_created_on']}
            metrics_json.update(model_desc)
            logging.info("modeling : ModelStatisticsClass : performance_metrics : execution end")
            return metrics_json
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : performance_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : performance_metrics : " +traceback.format_exc())
            return exc.msg
        


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
            if df is None:
                raise DatabaseConnectionFailed(500)

            if len(df) == 0 :
                raise DataNotFound(500)
                
            #logging.info('DF:- ' + str(df))
            cv_score_df = df[df['key'] == 'cv_score'].reset_index(drop=True).rename(columns={'value': 'cv_score'})['cv_score']
            holdout_score_df = df[df['key'] == 'holdout_score'].reset_index(drop=True).rename(columns={'value': 'holdout_score'})['holdout_score']
            cv_score_rounded_df = DataFrame(cv_score_df, columns = ['cv_score']).round(decimals = 2)
            holdout_score_rounded_df = DataFrame(holdout_score_df, columns = ['holdout_score']).round(decimals = 2)
            accuracy_df = pd.merge(cv_score_rounded_df, holdout_score_rounded_df, left_index=True, right_index=True)
            logging.info("modeling : ModelStatisticsClass : accuracy_metrics : execution end")
            return accuracy_df
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : accuracy_metrics : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : accuracy_metrics : " +traceback.format_exc())
            return exc.msg



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
            if model_details_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_details_df) == 0 :
                raise DataNotFound(500)
            
            accuracy_df = self.accuracy_metrics(project_id)

            final_df = pd.merge(accuracy_df, model_details_df, right_index=True, left_index=True)
            json_data = final_df.to_json(orient='records',date_format='iso')
            final_model_data = json.loads(json_data)
            return final_model_data

            logging.info("modeling : ModelStatisticsClass : show_model_details : execution end")
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : show_model_details : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_model_details : " +traceback.format_exc())
            return exc.msg


    def show_running_experiments(self, project_id):
        """This function is used to get experiments_list of particular project.

        Args:
            project_id ([object]): [Project id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe of experiments_list.]
            
        """
        try:
            # Get the necessary values from the mlaas.model_experiment_tbl
            sql_command = "select met.*,e.name as experiment_name,mmt.model_name,dt.dataset_name,round(cast(sv.cv_score as numeric),3) as cv_score,round(cast(sv.holdout_score as numeric),3) as holdout_score "\
                          "from mlaas.model_experiment_tbl met,mlaas.model_master_tbl mmt,mlaas.score_view sv,mlaas.dataset_tbl dt,mlaas.experiments e "\
                          "where met.model_id = mmt.model_id and met.experiment_id=sv.experiment_id and met.dataset_id=dt.dataset_id and met.experiment_id=e.experiment_id "\
                          "and met.project_id="+str(project_id) +" and met.status='running'"
                          
            model_experiment_data_df = self.DBObject.select_records(self.connection, sql_command)
            logging.info("-------------"+str(model_experiment_data_df))
            if model_experiment_data_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_experiment_data_df) == 0:
                return []
            # Converting final_df to json
            json_data = model_experiment_data_df.to_json(orient='records',date_format='iso')
            final_data = json.loads(json_data)
            return final_data
        except (DatabaseConnectionFailed,ModelIsStillInQueue) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg
        
    
    def show_all_experiments(self, project_id):
        """This function is used to get experiments_list of particular project.

        Args:
            project_id ([object]): [Project id of particular experiment.]

        Returns:
            [data_frame]: [it will return the dataframe of experiments_list.]
            
        """
        try:
            sql_command = "select met.*,e.name as experiment_name,mmt.model_name,mmt.model_type,dt.dataset_name,"\
                          "round(cast(sv.cv_score as numeric),3) as cv_score,round(cast(sv.holdout_score as numeric),3) as holdout_score "\
                          " from mlaas.model_experiment_tbl met,mlaas.model_master_tbl mmt,mlaas.score_view sv,mlaas.dataset_tbl dt,mlaas.experiments e"\
                          " where met.model_id = mmt.model_id and met.experiment_id=sv.experiment_id and met.dataset_id=dt.dataset_id and met.experiment_id=e.experiment_id "\
                          " and met.project_id="+str(project_id)
                          
            model_experiment_data_df = self.DBObject.select_records(self.connection, sql_command)

            if model_experiment_data_df is None:
                raise DatabaseConnectionFailed(500)

            if len(model_experiment_data_df) == 0 :
                return []
            # Converting final_df to json
            json_data = model_experiment_data_df.to_json(orient='records',date_format='iso')
            final_data = json.loads(json_data)
            return final_data
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg
    
    
    def check_existing_experiment(self,experiment_name):
        
        sql_command="select * from mlaas.model_dags_tbl where exp_name='"+experiment_name+"'"
        experiment_data_df = self.DBObject.select_records(self.connection, sql_command)
        
        if experiment_data_df is None :
            return 0
        elif len(experiment_data_df) > 0:
            return 1
        else:
            return 0
        
        
    def check_model_status(self,project_id,experiment_name):
        
        try:
        
            sql_command ="select dag_id,run_id from mlaas.model_dags_tbl where project_id="+str(project_id)+" and exp_name='"+experiment_name+"'"
            
            dag_df = self.DBObject.select_records(self.connection, sql_command)

            if dag_df is None:
                raise DatabaseConnectionFailed(500)

            if len(dag_df) == 0 :
                raise DataNotFound(500)
            
            dag_id,run_id = dag_df['dag_id'][0],dag_df['run_id'][0]
            
            sql_command = "select state from dag_run where dag_id='"+dag_id+"' and run_id='"+run_id +"'"
            state_df = self.DBObject.select_records(self.connection, sql_command)
            
            if state_df is None:
                raise DatabaseConnectionFailed(500)

            if len(state_df) == 0 :
                raise DataNotFound(500)
            logging.info("========="+str(type(state_df['state'][0])))
            #status=state_df['state'][0]
            return state_df
        
        except (DatabaseConnectionFailed,DataNotFound) as exc:
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : Exception " + str(exc))
            logging.error("modeling : ModelStatisticsClass : show_experiments_list : " +traceback.format_exc())
            return exc.msg
        
def compare_experiments(self, experiment_ids):
 
        exp_ids = tuple(experiment_ids)
    
        sql_command = 'select prms.key, prms.value, met.experiment_id from mlaas.params prms,mlaas.model_experiment_tbl met where prms.run_uuid=met.run_uuid and met.experiment_id in'+str(exp_ids)
        params_df = self.DBObject.select_records(self.connection, sql_command)
        params_pivot_df = params_df.pivot(index='experiment_id', columns='key', values='value')
        
        sql_command = 'select mtr.key, mtr.value, met.experiment_id from mlaas.metrics mtr,mlaas.model_experiment_tbl met where mtr.run_uuid=met.run_uuid and met.experiment_id in'+str(exp_ids)
        metrics_df = self.DBObject.select_records(self.connection, sql_command)
        metrics_pivot_df = metrics_df.pivot(index='experiment_id', columns='key', values='value')
 
        sql_command = 'select model_name from mlaas.model_master_tbl mmt, mlaas.model_experiment_tbl met where mmt.model_id=met.model_id and met.experiment_id in '+str(exp_ids)
        model_names = list(self.DBObject.select_records(self.connection, sql_command)['model_name'])
        exp_list = {}
        for index, id in enumerate(exp_ids):
            exp_list[str(id)] = {'metrics': metrics_pivot_df.loc[id, :].to_dict(), 
                                'params': params_pivot_df.loc[id, :].to_dict(),
                                'model_name': model_names[index]}
 
        return exp_list     
        

    