'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Mann Purohit       25-JAN-2021           1.0           Initial Version 
 
*/
'''

# All Necessary Imports
import logging
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve
from sklearn.preprocessing import label_binarize
from sklearn.inspection import partial_dependence

# Common Class File Imports
from common.utils.exception_handler.python_exception.common.common_exception import *


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


    
    def get_predict_proba(self, model, X_test, y_train, model_type):
        """Returns the probability values for each class.

        Args:
            model (ML model Object): ML model
            algorithm_type (string): binary or multiclass
            model_type (string): sklearn or keras
        """

        X_test = X_test[:, 1:]
        y_train = y_train[:, -1]

        n_classes = len(np.unique(y_train))
        
        if n_classes == 2:
            if model_type.lower() == 'sklearn':
                y_pred_proba = model.predict_proba(X_test)[:, 1]
            elif model_type.lower() == 'keras':
                y_pred_proba = model.predict_proba(X_test)
        
        elif n_classes > 2:
            y_pred_proba = model.predict_proba(X_test)

        return y_pred_proba


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
            
            
            f1_score = metrics.f1_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
            
            
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

            for i,j in zip(temp_arr,abs_arr):
                if i == False:
                    np.put(abs_arr,np.where(temp_arr == i),0)
                    
            mape = np.mean(abs_arr) * 100
            
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

    def get_performance_curve(self, curve_name, model, y_pred_prob, y_test, dataset_split_dict):

        y_test = y_test[:, -1]
        classes = dataset_split_dict['classes']
        
        dict1, dict2, dict3 = dict(), dict(), dict()
        n_classes = len(classes)

        if n_classes > 2:
            
            y_test_encoded = label_binarize(y_test, classes=[*range(n_classes)])
            
            for i, c in enumerate(classes):
                
                dict1[c], dict2[c], dict3[c] = eval(curve_name)(y_test_encoded[:, i], y_pred_prob[:, i])
                dict1[c] = dict1[c].round(3).tolist()
                dict2[c] = dict2[c].round(3).tolist()
                dict3[c] = dict3[c].round(3).tolist()
            
            final_classes = classes

        
        elif n_classes == 2:
            
            arr1, arr2, arr3 = eval(curve_name)(y_test, y_pred_prob)
            c = classes[1]
            dict1 = {c: arr1.round(3).tolist()}
            dict2 = {c: arr2.round(3).tolist()}
            dict3 = {c: arr3.round(3).tolist()}
            final_classes = [c]

        if curve_name.lower() == 'roc_curve':
            return {'FPR': dict1, 'TPR': dict2, 'classes':final_classes}# FPR is False Positive Rate, TPR is True Positive Rate

        elif curve_name.lower() == 'precision_recall_curve':
            return {'Precision' : dict1, 'Recall': dict2}
    
    def get_confusion_matrix(self,actual_lst,prediction_lst):
        '''
        This function retuns confusion matrix dictionary for classification models

        Args : actual_lst [list] : A list containing actual values
               prediction_lst [list] : A list containing predicted values

        Returns : [Dictionary] Confusion Matrix dictionary 
        '''
        cm = confusion_matrix(actual_lst,prediction_lst)
        confusion_matrix_df = pd.DataFrame(cm)                                                            
        confusion_matrix_dict = confusion_matrix_df.to_dict()

        return confusion_matrix_dict

    
    def get_partial_dependence_scores(self, model, X_train, input_features_list, target_features_list, dataset_split_dict):
        """Returns the values needed to plot partial dependence plot.

        Args:
            model (object): ML estimator
            X_train (array): input training data
            y_train (array): target training data
        """
        data_ratio = 0.2
        data_size = int(X_train.shape[0]*data_ratio)
        data_index = X_train[:data_size, 0].tolist()
        # X_train = X_train[:, 1:]
        
        
        # np.random.seed(dataset_split_dict['random_state'])
        # data_size = all_index.shape[0]
        # index = all_index[np.random.choice(data_size, int(data_size*0.2))].astype(np.int16)
        # print("INDEX----", index)
        # print("INDEX TYPE------", type(index))
        pdp_data = X_train[:data_size, 1:]
        classes = dataset_split_dict['classes']

        pdp_values = dict()
        for index, feature in enumerate(input_features_list):
            grid_resolution=min(100, len(np.unique(pdp_data[:, index])))
            feature_average = partial_dependence(model, pdp_data, [index], kind='average', percentiles=[0, 1], grid_resolution=grid_resolution)
            pdp_values[feature] = feature_average['average'][0].round(3).tolist()

        if len(classes) == 2:
            classes = [classes[1]]
        if classes == []:
            classes = []

        return {'PDP_Scores': pdp_values, 'classes':classes, 'input_features':input_features_list, 'target_features': target_features_list, 'index':data_index}
        
    
    
    def model_summary(self,dataset_split_dict):
        
        model_summary = {
                            "Model Name":dataset_split_dict['model_name'],
                            
                            "Input Features":dataset_split_dict['input_features_list'],
                            "Target Features":dataset_split_dict['target_features_list'],
                            
                            "Scaling Type":dataset_split_dict['scaling_type'],
                            "Split Method":dataset_split_dict['split_method'],
                            
                            "Train Size":float(dataset_split_dict['train_size']),
                            "Valid Size":float(dataset_split_dict['valid_size']),
                            "Test Size":float(dataset_split_dict['test_size']),
                            
                            "Train Split":float( 1 - (dataset_split_dict['test_ratio'] + dataset_split_dict['valid_ratio']) ),
                            "Valid Split":float(dataset_split_dict['valid_ratio']),
                            "Test Split":float(dataset_split_dict['test_ratio']),
                            
                            "Random State":int(dataset_split_dict['random_state']),
                            "CV (K-Fold )":dataset_split_dict['cv']
                         }
        
        return model_summary
