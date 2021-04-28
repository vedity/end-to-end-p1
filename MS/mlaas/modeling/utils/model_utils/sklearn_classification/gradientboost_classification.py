'''
/*CHANGE HISTORY

----CREATED BY----------CREATION DATE--------VERSION--------PURPOSE----------------------
 Brijrajsinh Gohil      1-April-2021           1.0           Initial Version 
 
*/
'''

import numpy as np
import pandas as pd
import json
import mlflow
import mlflow.sklearn
import shap


from modeling.utils.model_common_utils.evaluation_metrics import EvaluationMetrics as EM
from modeling.utils.model_common_utils.mlflow_artifacts import MLFlowLogs 
from common.utils.exception_handler.python_exception.modeling.modeling_exception import *

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import *

from sklearn.model_selection import ( train_test_split, 
                                     GridSearchCV, 
                                     cross_val_score, 
                                     cross_val_predict,
                                     KFold )


class GradientBoostingClassificationClass:
    
    def __init__(self,input_features_list,target_features_list,# labels,
                X_train, X_valid, X_test, y_train, y_valid, y_test, scaled_split_dict,
                hyperparameters):
        
        self.input_features_list = input_features_list[1:] 
        # list of target features (features to be predicted)
        self.target_features_list = target_features_list[1:]
        self.dataset_split_dict = scaled_split_dict # This object stores the variables used to split the data. 
       
        self.X_train = X_train 
        self.X_test = X_test
        self.X_valid = X_valid
        self.y_train = y_train
        self.y_test = y_test
        self.y_valid = y_valid


        self.loss = hyperparameters['loss']
        self.learning_rate = float(hyperparameters['learning_rate'])
        self.subsample = float(hyperparameters['subsample'])
        self.n_estimators = int(hyperparameters['n_estimators'])
        self.criterion = hyperparameters['criterion']
        self.max_features = hyperparameters['max_features']
        self.min_impurity_decrease = float(hyperparameters['min_impurity_decrease'])
        self.min_samples_leaf = int(hyperparameters['min_samples_leaf'])
        
        if hyperparameters['max_depth'] != 'None':
            self.max_depth = int(hyperparameters['max_depth'])
        else:
            self.max_depth = None


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
        
        # get Input Training Features
        X_train = self.X_train[:,1:] 
        # get Target Training Features
        y_train = self.y_train[:,-1].reshape(-1 ,1)

        #Avaiable Kernel = {'linear','poly','rbf','sigmoid'} , default = rbf
        #Value of C = [0,infinity] , default = 1
        #Value of gamma = [0,infinity] , default = 'scale'
        model = GradientBoostingClassifier(loss=self.loss, learning_rate=self.learning_rate, subsample=self.subsample,
                                      n_estimators=self.n_estimators, criterion=self.criterion, max_depth=self.max_depth, 
                                      min_samples_leaf=self.min_samples_leaf, min_impurity_decrease=self.min_impurity_decrease, 
                                      max_features=self.max_features)

        # fit the model
        model.fit(X_train, y_train) 

        return model
    
    def get_learning_curve(self,model):
        
        """This function is get learning curve.

        Args:
            model ([object]): [train model object]
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]
        """
        X_train = self.X_train[:,1:] 
        y_train = self.y_train[:,-1].reshape(-1, 1)
        # Dividing train data size into bins.
        train_sizes=np.linspace(0.10, 1.0, 10)
        train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='accuracy',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        
        train_sizes_2, train_loss, test_loss, fit_times_2, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='neg_log_loss',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        

        # Average of train score(accuracy).
        train_mean = train_scores.mean(axis=1)
        # Average of train score(accuracy).
        test_mean = test_scores.mean(axis=1)
        # Create the learning curve dictionary.
        # learning_curve_dict = {"train_size":train_sizes.tolist(),"train_score":train_mean.tolist(),"test_score":test_mean.tolist(),
        #                         "train_loss": abs(train_loss.mean(axis=1)).tolist(), "test_loss": abs(test_loss.mean(axis=1)).tolist()}
        
        learning_curve_dict = {"train_size":train_sizes.tolist(),"train_score":np.nan_to_num(train_mean).tolist(),"test_score":np.nan_to_num(test_mean).tolist(),
                                "train_loss": abs(np.nan_to_num(train_loss).mean(axis=1)).tolist(), "test_loss": abs(np.nan_to_num(test_loss).mean(axis=1)).tolist()}
        
        return learning_curve_dict
        
        
    def features_importance(self,model):
        
        """This function is used to get features impact.

        Returns:
            [dict]: [it will return features impact dictionary.]
        """
        
        shap_data = self.X_train[:min(10, self.X_train.shape[0]), 1:]
        treeexplainer = shap.TreeExplainer(model)
        shap_values = treeexplainer.shap_values(shap_data[:5])
        if isinstance(shap_values, list):
            shap_values = np.array(shap_values).mean(axis=0)
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

        Returns:
            [list]: [it will return actual and prediction list.]
        """
        X_train = self.X_train[:,1:]
        X_test = self.X_test[:, 1:]
  
        prediction_arr = model.predict(X_test)
        prediction_lst = prediction_arr.tolist()
        
        print("pred shape=",prediction_arr.shape)
        print("pred lst")
        print(prediction_lst)

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

        train_size = self.X_train.shape[0]
        test_size = self.X_test.shape[0]
        
        model_summary = {"Model Name":"DecisionTree_Regression",
                         "Loss": self.loss,
                         "Learning Rate":self.learning_rate,
                         "Subsample": self.subsample,
                         "N_Estimator": self.n_estimators,
                         "Criterion": self.criterion,
                         "Max Depth": self.max_depth,
                         "Max Features": self.max_features,
                         "Minimum Impurity Decrease": self.min_impurity_decrease,
                         "Minimum Samples Leaf": self.min_samples_leaf,
                         "Input Features":self.input_features_list,
                         "Target Features":self.target_features_list,
                         "Train Size":float(train_size),"Test Size":int(test_size),
                         "Train Split":1-(self.dataset_split_dict['test_ratio'] + self.dataset_split_dict['valid_ratio']),
                         "Test Split":float(self.dataset_split_dict['test_ratio']),
                         "Random State":int(self.dataset_split_dict['random_state']),
                         "Valid Split":self.dataset_split_dict['valid_ratio'],
                         "CV (K-Fold )":self.dataset_split_dict['cv']}
        
        
        return model_summary
        
       
    def cv_score(self, model):
        
        """This function is used to get cv score.

        Returns:
            [float]: [it will return cv score.]
        """
        
        X_train = self.X_train[:,1:] 
        y_train = self.y_train[:,-1].reshape(-1, 1)
        
        shuffle = KFold(n_splits=self.dataset_split_dict['cv'],
                    shuffle=True,
                    random_state=self.dataset_split_dict['random_state'])
        
        cv_scores = cross_val_score(estimator=model,
                                X=X_train,
                                y=y_train,
                                cv=shuffle,
                                scoring='accuracy')
        cv_score_mean = cv_scores.mean()

        return cv_score_mean


    def run_pipeline(self):
        
        """This function is used as a pipeline which will execute function in a sequence.
        """
        try :
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
            
            func_code = "M10"
            # log mlflow matrix
            self.MLFlowLogObj.store_model_metrics(accuracy=accuracy, recall=recall, precision=precision, f1_score=f1_score,
                                                holdout_score=holdout_score, cv_score=cv_score)

            # log artifacts (output files)
            self.MLFlowLogObj.store_model_dict(learning_curve=learning_curve_dict, features_importance=features_impact_dict,
                                                model_summary=model_summary, predictions=final_result_dict,confusion_matrix=confusion_matrix_dict)

            # log mlflow parameter
            self.MLFlowLogObj.store_model_params(self.dataset_split_dict)

            # Store the Machine Learning Model.
            self.MLFlowLogObj.store_model(model, model_name="GBM_Classification", model_type='sklearn')

        except:
            
            raise ModelFailed(func_code)