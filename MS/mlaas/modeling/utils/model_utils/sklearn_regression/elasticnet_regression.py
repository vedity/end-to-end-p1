'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''

# Necessary Imports.
import json
import shap
import logging
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

# Common Utils Imports.
from common.utils.logger_handler import custom_logger as cl
from modeling.utils.model_common_utils.evaluation_metrics import EvaluationMetrics as EM
from modeling.utils.model_common_utils.mlflow_artifacts import MLFlowLogs
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *
from modeling.utils.model_utils.function_calls import regression_func_call
# Sklearn Library  Imports.
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import learning_curve

from sklearn.model_selection import ( train_test_split, 
                                     GridSearchCV, 
                                     cross_val_score, 
                                     cross_val_predict,
                                     KFold )

from sklearn.metrics import ( mean_squared_error,
                             mean_absolute_error,
                             r2_score )


# Global Variable.
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')


 
class ElasticNetClass:
    
    def __init__(self,input_features_list,target_features_list,
                X_train, X_valid, X_test, y_train, y_valid, y_test, scaled_split_dict,
                hyperparameters):
        
        # Get Input Features And Target Features  List.
        self.input_features_list = input_features_list[1:]  
        self.target_features_list = target_features_list[1:] 
        
        # This object stores the variables used to split the data. 
        self.dataset_split_dict = scaled_split_dict 
       
        # Splits Datasets Array Initialization.
        self.X_train = X_train 
        self.X_test = X_test
        self.X_valid = X_valid
        self.y_train = y_train
        self.y_test = y_test
        self.y_valid = y_valid
        
        # Model Hyperparameters Initialization.
        self.alpha = float(hyperparameters['alpha'])
        self.l1_ratio = float(hyperparameters['l1_ratio'])
        self.selection = hyperparameters['selection']

        # Common Utility Object Declaration. 
        self.EvalMetricsObj = EM()
        self.MLFlowLogObj = MLFlowLogs()
        
        
    def train_model(self):
        
        """This function is used to train the model.

        Args:
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]

        Returns:
            [object]: [it will return train model object.]
        """
        # Get Input Training Features.
        X_train = self.X_train[:,1:] 
        # Get Target Training Features.
        y_train = self.y_train[:,-1].reshape(-1, 1)
        # Define The Model.
        model = ElasticNet(alpha=self.alpha, l1_ratio=self.l1_ratio, selection=self.selection) 
        # Fit The Model.
        model.fit(X_train, y_train) 
        
        return model
    
    def get_learning_curve(self,model):
        
        """This function gets learning curve generated while training the data.

        Args:
            model ([object]): [train model object]
            
         Returns:
            [dict]: [it will return learning curve dictionary.]
            
        """
        # Get Input Training Features.
        X_train = self.X_train[:,1:] 
        # Get Target Training Features.
        y_train = self.y_train[:,-1].reshape(-1,1)
        # Dividing Train Data Size Into Bins.
        train_sizes = np.linspace(0.10, 1.0, 10)
        # Learning Curve Function Return The Train Scores And Test Scores.
        train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='r2',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        
        # Learning Curve Function Return The Train Loss And Test Loss.
        train_sizes_2, train_loss, test_loss, fit_times_2, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='neg_mean_squared_error',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        

        # Average Of Train Score.
        train_mean = train_scores.mean(axis=1)
        # Average Of Test Score.
        test_mean = test_scores.mean(axis=1)
       
        # Get Learning Curve Dictionary.
        learning_curve_dict = {"train_size":train_sizes.tolist(),"train_score":np.nan_to_num(train_mean).tolist(),"test_score":np.nan_to_num(test_mean).tolist(),
                                "train_loss": abs(np.nan_to_num(train_loss).mean(axis=1)).tolist(), "test_loss": abs(np.nan_to_num(test_loss).mean(axis=1)).tolist()}
        
        return learning_curve_dict
        
    
    def features_importance(self,model):
        
        """This function is used to get features impact.

        Args:
            model ([object]): [train model object]
            
         Returns:
            [dict]: [it will return features impact dictionary.]
            
        """
        
        shap_data = self.X_train[:min(100, self.X_train.shape[0]), 1:]
        LinearExplainer = shap.LinearExplainer(model, shap_data)
        shap_values = LinearExplainer.shap_values(shap_data)
        shap_values = abs(np.array(shap_values)).mean(axis=0)

        features_importance_values = shap_values / shap_values.sum()

        features_df = pd.DataFrame(data=features_importance_values, index=self.input_features_list, columns=['features_importance'])

        features_df = features_df.sort_values(by='features_importance', ascending=False)*100

        features_dict = features_df.T.to_dict(orient='records')[0]

        features_names = list(features_dict.keys())
        norm_importance = np.array(list(features_dict.values())).round(2).tolist()

        features_importance_dict = {'features_name': features_names, 'norm_importance': norm_importance}

        return features_importance_dict

        
    def get_actual_prediction(self,model):
        
        """This function is used to get actuals and predictions.
        
        Args:
            model ([object]): [train model object]

        Returns:
            [list,list]: [it will return actual list and prediction list.]
        """
        X_train = self.X_train[:,1:]
        X_test = self.X_test[:, 1:]
  
        prediction_arr = model.predict(X_test)
        prediction_lst = prediction_arr.tolist()
        
        actual_values = self.y_test[:,1]
        actual_lst = actual_values.tolist()
        
        try:
            prediction_flat_lst = [item for elem in prediction_lst for item in elem]
            actual_flat_lst = actual_lst
        except:
            prediction_flat_lst = prediction_lst
            actual_flat_lst = actual_lst
            
        return actual_flat_lst,prediction_flat_lst

        
    
    def model_summary(self):
        
        """This function is used to get model summary.

        Returns:
            [dict]: [it will return model summary.]
        """
        model_summary = {}
        
        for key,value in self.dataset_split_dict.items():
            if 'file' not in key:
                model_summary[key] = value
            
        
        for key,value in self.hyperparameters.items():
            model_summary[key] = value
        
        return model_summary
      
      
       
    def cv_score(self,model):
        
        """This function is used to get cv score.
        
        Args:
            model ([object]): [model object]

        Returns:
            [float]: [it will return cv score.]
        """

        if self.X_train.shape[1] == 2:
            X_train = self.X_train[:,1:].reshape(-1, 1)
        else:
            X_train = self.X_train[:,1:]
            
        y_train = self.y_train[:,-1].reshape(-1, 1)
        
        shuffle = KFold(n_splits=self.dataset_split_dict['cv'],shuffle=True,
                        random_state=self.dataset_split_dict['random_state'])
        
        cv_scores = cross_val_score(estimator=model,X=X_train,y=y_train,
                                    cv=shuffle,scoring='r2')
        cv_score_mean = cv_scores.mean()

        return cv_score_mean
        
        
    def run_pipeline(self):
        
        """This function is used as a pipeline which will execute function in a sequence.
        """
        regression_func_call(self)
            