'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0         Initial Version 

*/
'''

from common.utils.exception_handler.python_exception.modeling.modeling_exception import *

def regression_func_call(self):
    """This function is used to call all regression model function in a sequence.
       And each function is associated with specific function code. 
    """
    try:
        func_code = "M01"
        # train the model
        model = self.train_model()
        
        func_code = "M02"
        # get features importance
        features_impact_dict = self.features_importance(model) 
        
        func_code = "M03"
        # get actual and predicted values 
        actual_lst,prediction_lst = self.get_actual_prediction(model)
        
        func_code = "M04"
        # save prediction
        final_result_dict = self.EvalMetricsObj.save_prediction(self.y_test, prediction_lst, self.target_features_list)
        
        func_code = "M05"
        # all evaluation matrix
        r2score,mse,mae,mape = self.EvalMetricsObj.get_evaluation_matrix(actual_lst,prediction_lst, model_type='Regression')  
        
        func_code = "M06"
        # get cv score
        if self.dataset_split_dict['split_method'] == 'cross_validation':
            cv_score = self.cv_score(model) # default k-fold with 5 (r2-score)
        else:
            cv_score = 0
            
        func_code = "M07"  
        # get holdout score
        holdout_score = self.EvalMetricsObj.holdout_score(self.y_test, prediction_lst, model_type='Regression') # default 80:20 splits (r2-score)
        
        func_code = "M08"
        # get model summary
        model_summary = self.model_summary() # high level model summary
        
        func_code = "M09"
        # get model learning curve
        learning_curve_dict = self.get_learning_curve(model)
        
        func_code = "M15"
        # Get PDP Scores for every feature
        pdp_scores = self.EvalMetricsObj.get_partial_dependence_scores(model, self.X_train, self.input_features_list, self.target_features_list, self.dataset_split_dict)

        # Mlflow log artificats
        
        func_code = "M10"
        
        # Mlflow Matrix
        self.MLFlowLogObj.store_model_metrics(r2_score=r2score, mae=mae, mse=mse, mape=mape, 
                                            holdout_score=holdout_score, cv_score=cv_score)
        func_code = "M15"
        # Get PDP Scores for every feature
        pdp_scores = self.EvalMetricsObj.get_partial_dependence_scores(model, self.X_train, self.input_features_list, self.target_features_list, self.dataset_split_dict)
        
        # Mlflow Parameter
        self.MLFlowLogObj.store_model_params(self.dataset_split_dict)

        # Mlflow Artifacts 
        self.MLFlowLogObj.store_model_dict(learning_curve=learning_curve_dict, features_importance=features_impact_dict,
                                            model_summary=model_summary, predictions=final_result_dict,pdp_scores=pdp_scores)
        

        # Save Model.
        self.MLFlowLogObj.store_model(model, model_name=self.hyperparameters['model_name'], model_type='sklearn')
        
    except:
        raise ModelFailed(func_code)
        
            
            
def classification_func_call(self):
    """This function is used to call all classification model function in a sequence.
       And each function is associated with specific function code. 
    """
    try:
        
        func_code = "M01"
        # train the model
        model = self.train_model()
        
        func_code = "M02"
        # get features importance
        features_impact_dict = self.features_importance(model) 
        
        func_code = "M03"
        # get actual and predicted values 
        actual_lst,prediction_lst = self.get_actual_prediction(model)
    
        func_code = "M05"
        # all evaluation matrix
        accuracy,recall,precision,f1_score = self.EvalMetricsObj.get_evaluation_matrix(actual_lst,prediction_lst, model_type='Classification')   
        
        func_code = "M06"
        # get cv score
        if self.dataset_split_dict['split_method'] == 'cross_validation':
            cv_score = self.cv_score(model) # default k-fold with 5 (r2-score)
        else:
            cv_score = 0
            
        func_code = "M07"  
        # get holdout score
        holdout_score = self.EvalMetricsObj.holdout_score(self.y_test, prediction_lst, model_type='Classification') # default 80:20 splits (r2-score)
        
        func_code = "M08"
        # get model summary
        model_summary = self.model_summary() # high level model summary
        
        func_code = "M09"
        # get model learning curve
        learning_curve_dict = self.get_learning_curve(model)
        
        func_code = "M11"
        # get confusion matrix
        confusion_matrix_dict = self.EvalMetricsObj.get_confusion_matrix(actual_lst,prediction_lst)
        
        func_code = "M12"
        # Get probaility for each class
        y_pred_prob = self.EvalMetricsObj.get_predict_proba(model, self.X_test, self.y_train, model_type='sklearn')
        
        func_code = "M04"
        # save prediction
        final_result_dict = self.EvalMetricsObj.save_prediction(self.y_test, prediction_lst, self.target_features_list)

        func_code = "M13"
        # Get ROC Curve values for each class
        roc_scores = self.EvalMetricsObj.get_performance_curve('roc_curve', model, y_pred_prob, self.y_test, self.dataset_split_dict)

        func_code = "M14"
        # Get Precision Recall Values for each class
        precision_recall_scores = self.EvalMetricsObj.get_performance_curve('precision_recall_curve', model, y_pred_prob, self.y_test, self.dataset_split_dict)
        
        func_code = "M15"
        # Get PDP Scores for every feature
        pdp_scores = self.EvalMetricsObj.get_partial_dependence_scores(model, self.X_train, self.input_features_list, self.target_features_list, self.dataset_split_dict)
        
        # Mlflow log artificats

        func_code = "M10"
        # Mlflow Matrix
        self.MLFlowLogObj.store_model_metrics(accuracy=accuracy, recall=recall, precision=precision, f1_score=f1_score,
                                            holdout_score=holdout_score, cv_score=cv_score)
        
        # Mlflow Parameter
        self.MLFlowLogObj.store_model_params(self.dataset_split_dict)

        # Mlflow Artifacts 
        self.MLFlowLogObj.store_model_dict(learning_curve=learning_curve_dict, features_importance=features_impact_dict,
                                            model_summary=model_summary, predictions=final_result_dict,confusion_matrix=confusion_matrix_dict,
                                            roc_scores=roc_scores, precision_recall_scores=precision_recall_scores,pdp_scores=pdp_scores)

        # Save  Model.
        self.MLFlowLogObj.store_model(model, model_name=self.hyperparameters['model_name'], model_type='sklearn')
        
    except:
        raise ModelFailed(func_code)
        

