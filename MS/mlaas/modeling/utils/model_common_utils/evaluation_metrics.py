import logging
import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.preprocessing import label_binarize
from common.utils.exception_handler.python_exception.common.common_exception import *

# user_name = 'admin'
# log_enable = True

# LogObject = cl.LogClass(user_name,log_enable)
# LogObject.log_setting()

# logger = logging.getLogger('evaluation_metrics')


class EvaluationMetrics:

    def save_prediction(self,y_test,prediction_lst, target_features_list):
        
        """This function is used to save test results or predictions.
        """
         
        y_df = pd.DataFrame(y_test[:,1],columns=target_features_list)
        y_df.reset_index(inplace = True, drop = True)
        y_df['index']=y_test[:,0]
        append_str = '_prediction'
        target_features_suf_res = [sub + append_str for sub in target_features_list]
        test_results_df = pd.DataFrame(prediction_lst, columns = target_features_suf_res) 
        
        final_result_df = pd.concat([y_df,test_results_df],axis=1)
        
        final_result_dict = final_result_df.to_dict(orient='list') 
        
        
        return final_result_dict


    def get_evaluation_matrix(self,actual_lst,prediction_lst, model_type, lib='sklearn'):
        """This function is used to find model performance matrices.
        
        Returns:
            [dict]: [it will return model matrices.]
        """
        
        if model_type == 'Classification':
        
            ## Accuray e AUC
            accuracy = metrics.accuracy_score(actual_lst, prediction_lst)
    #         auc = roc_auc_score(actual_lst, prediction_lst,average='micro',multi_class='raise')
            ## Precision e Recall
            recall = metrics.recall_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
            precision = metrics.precision_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
            print("PRED LIST_---------------------", prediction_lst[:10])
            print("ACTUALLL LIST_---------------------", actual_lst[:10])
            f1_score = metrics.f1_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
            print("F1SCORE-------------------------------------------------------", f1_score) 
            # print('ACTUAL LSTTT:-         ', actual_lst.shape)
            # classes = np.unique(actual_lst).astype(object)
            # CM = confusion_matrix(actual_lst,prediction_lst,labels=classes)
            # CM_df = pd.DataFrame(CM, columns=classes+'_true', index=classes+'_predicted')
            # CM_dict = CM_df.to_dict()
            
            return round(accuracy,2),round(recall,2),round(precision,2), f1_score
        
        elif model_type == 'Regression':
            
            r2score = metrics.r2_score(actual_lst,prediction_lst)
            mse = metrics.mean_squared_error(actual_lst,prediction_lst)
            mae = metrics.mean_absolute_error(actual_lst,prediction_lst)
            
            actual_lst = np.array(actual_lst).reshape(-1, )
            prediction_lst = np.array(prediction_lst).reshape(-1, )
            
            actual, pred = np.array(actual_lst), np.array(prediction_lst)
        
            temp_arr=np.isfinite(np.abs((actual - pred) / actual))
            abs_arr=np.abs((actual - pred) / actual)

            print("temp_arr==",temp_arr)
            print("abs_arr==",abs_arr)
            for i,j in zip(temp_arr,abs_arr):
                if i == False:
                    np.put(abs_arr,np.where(temp_arr == i),0)
        
            print("updated abs_arr==",abs_arr)
            mape = np.mean(abs_arr) * 100
            print("mape ==",mape)
            
            return r2score,mse,mae,mape
        
    def holdout_score(self,y_actual, y_pred, model_type):
        
        """This function is used to get holdout score.

        Args:
            model ([object]): [train model object.]
            X_test ([dataframe]): [input test data dataframe.]
            y_test ([dataframe]): [target test data dataframe.]

        Returns:
            [float]: [it will return holdout score.]
        """
        y_actual = y_actual[:, -1].reshape(-1, 1)
        
        if model_type == 'Classification':
            holdout_score = metrics.accuracy_score(y_actual,y_pred)
            return holdout_score

        elif model_type == 'Regression':
            holdout_score = metrics.r2_score(y_actual, y_pred)
            return holdout_score

    def get_precision_recall(self, model, X_test, y_test, lib='sklearn'):

        y_test = y_test[:, -1]
        X_test = X_test[:, 1:]
        
        n_classes = len(np.unique(y_test))
        if n_classes > 2:
            y_pred_prob = model.predict_proba(X_test)
            y_test_encoded = label_binarize(y_test, classes=[*range(n_classes)])

            precision = dict()
            recall = dict()
            threshold = dict()
            recall_sum = 0
            precision_sum = 0
            for i in range(n_classes):
                precision[i], recall[i], threshold[i] = metrics.precision_recall_curve(y_test_encoded[:, i],
                                                                    y_pred_prob[:, i])
                recall_sum += recall[i]
                precision_sum += precision[i]
                threshold_sum += threshold[i]
            
            recall_arr = recall_sum / n_classes
            precision_arr = precision_sum / n_classes
            threshold_arr = threshold_sum / n_classes
        
        elif n_classes == 2:
            if lib == 'sklearn':
                y_true_prob = model.predict_proba(X_test)[:, 1]
            elif lib == 'keras':
                y_true_prob = model.predict_proba(X_test)
            precision_arr, recall_arr, threshold_arr = metrics.precision_recall_curve(y_test, y_true_prob)
            precision_arr = precision_arr.tolist()
            recall_arr = recall_arr.tolist()
            threshold_arr = threshold_arr.tolist()
        
        precision_recall_dict = {'Precision': precision_arr, 'Recall': recall_arr, 'Threshold': threshold_arr}

        return precision_recall_dict