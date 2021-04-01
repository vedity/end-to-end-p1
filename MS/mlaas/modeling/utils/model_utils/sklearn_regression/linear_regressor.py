'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


import numpy as np
import pandas as pd
import json
import mlflow
import mlflow.sklearn
import shap

from common.utils.logger_handler import custom_logger as cl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve

from sklearn.model_selection import ( train_test_split, 
                                     GridSearchCV, 
                                     cross_val_score, 
                                     cross_val_predict,
                                     KFold )

from sklearn.metrics import ( mean_squared_error,
                             mean_absolute_error,
                             r2_score )

import logging
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('view')


 
class LinearRegressionClass:
    
    def __init__(self, input_features_list, target_features_list, X_train, X_valid, X_test, 
                y_train, y_valid, y_test, scaled_split_dict):
        
        """This is used to initialise the model input parameter when model class is called.
        """
        self.dataset_split_dict = scaled_split_dict # This object stores the variables used to split the data.
        # List of input features(which are used to train the model)
        self.input_features_list = input_features_list[1:] 
        # list of target features (features to be predicted)
        self.target_features_list = target_features_list[1:] 
       
        self.X_train = X_train 
        self.X_test = X_test
        self.X_valid = X_valid
        self.y_train = y_train
        self.y_test = y_test
        self.y_valid = y_valid
        
        
    def train_model(self,X_train,y_train):
        
        """This function is used to train the model.

        Args:
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]

        Returns:
            [object]: [it will return train model object.]
        """
        # get Input Training Features
        X_train = X_train[:,1:] 
        # get Target Training Features
        y_train = y_train[:,-1].reshape(len(y_train[:,-1]),1)
        # define the model
        model = LinearRegression() 
        # fit the model
        model.fit(X_train, y_train) 
        return model
    
    def get_learning_curve(self,model,X_train,y_train):
        
        """This function gets learning curve generated while training the data.

        Args:
            model ([object]): [train model object]
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]
        """
        X_train = X_train[:,1:] 
        y_train = y_train[:,-1].reshape(-1,1)
        # Dividing train data size into bins.
        train_sizes = np.linspace(0.10, 1.0, 10)
        train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='r2',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        
        train_sizes_2, train_loss, test_loss, fit_times_2, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='neg_mean_squared_error',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        

        # Average of train score(accuracy).
        train_mean = train_scores.mean(axis=1)
        # Average of train score(accuracy).
        test_mean = test_scores.mean(axis=1)
        # Create the learning curve dictionary.
        learning_curve_dict = {"train_size":train_sizes.tolist(),"train_score":train_mean.tolist(),"test_score":test_mean.tolist(),
                                "train_loss": abs(train_loss.mean(axis=1)).tolist(), "test_loss": abs(test_loss.mean(axis=1)).tolist()}
        
        return learning_curve_dict
        
    
    def features_importance(self,model,X_train):
        
        """This function is used to get features impact.

        Returns:
            [dict]: [it will return features impact dictionary.]
        """
        
        shap_data = X_train[:min(1000, X_train.shape[0]), 1:]
        LinearExplainer = shap.LinearExplainer(model, shap_data)
        shap_values = abs(LinearExplainer.shap_values(shap_data)).mean(axis=0)

        features_importance_values = shap_values / shap_values.sum()

        features_df = pd.DataFrame(data=features_importance_values, index=self.input_features_list, columns=['features_importance'])

        features_df = features_df.sort_values(by='features_importance', ascending=False)*100

        features_dict = features_df.T.to_dict(orient='records')[0]

        features_names = list(features_dict.keys())
        norm_importance = np.array(list(features_dict.values())).round(2).tolist()

        features_importance_dict = {'features_name': features_names, 'norm_importance': norm_importance}

        return features_importance_dict

        
    def get_actual_prediction(self,model,X_test,y_test):
        
        """This function is used to get actuals and predictions.

        Returns:
            [list]: [it will return actual and prediction list.]
        """
        X_train = self.X_train[:,1:]
        X_test = X_test[:, 1:]
  
        prediction_arr = model.predict(X_test)
        prediction_lst = prediction_arr.tolist()

        actual_values = y_test[:,1]
        actual_lst = actual_values.tolist()
        
        if len(self.target_features_list) == 1 :
            
            prediction_flat_lst = [item for elem in prediction_lst for item in elem]
            actual_flat_lst = actual_lst 
            return actual_flat_lst,prediction_flat_lst
        
        else:
            prediction_flat_lst =  [ list(map(sub_lst)) for sub_lst in prediction_lst ]
            actual_flat_lst =  [ list(map(sub_lst)) for sub_lst in actual_lst ]
            return actual_flat_lst,prediction_flat_lst
        
        
    def save_prediction(self,y_test,prediction_lst):
        
        """This function is used to save test results or predictions.
        """
         
        y_df = pd.DataFrame(y_test[:,1],columns=self.target_features_list)
        
        y_df.reset_index(inplace = True, drop = True)
        y_df['index']=y_test[:,0]
        append_str = '_prediction'
        target_features_suf_res = [sub + append_str for sub in self.target_features_list]
        test_results_df = pd.DataFrame(prediction_lst, columns = target_features_suf_res) 
        
        final_result_df = pd.concat([y_df,test_results_df],axis=1)
        print("final results ==",final_result_df)
        final_result_dict = final_result_df.to_dict(orient='list') 
        print("final results dict ==",final_result_dict)
        return final_result_dict
        
        
    def get_evaluation_matrix(self,actual_lst,prediction_lst):
        
        """This function is used to find model performance matrices.
        
        Returns:
            [dict]: [it will return model matrices.]
        """
        
        
        r2score = r2_score(actual_lst,prediction_lst)
        mse = mean_squared_error(actual_lst,prediction_lst)
        #rmse = math.sqrt(mse)
        
        mae = mean_absolute_error(actual_lst,prediction_lst)
        
        
        actual, pred = np.array(actual_lst), np.array(prediction_lst)
        mape = np.mean(np.abs((actual - pred) / actual)) * 100
        
        return r2score,mse,mae,mape
        
        
        
    def model_summary(self,X_train, X_test,y_train):
        
        """This function is used to get model summary.

        Returns:
            [dict]: [it will return model summary.]
        """
            
        train_size = X_train.shape[0]
        test_size = X_test.shape[0]
        
        model_summary = {"Model Name":"Linear_Regression_Sklearn",
                         "Input Features":self.input_features_list,
                         "Target Features":self.target_features_list,
                         "Train Size":float(train_size),"Test Size":int(test_size),
                         "Train Split":1-(self.dataset_split_dict['test_ratio'] + self.dataset_split_dict['valid_ratio']),
                         "Test Split":float(self.dataset_split_dict['test_ratio']),
                         "Random State":int(self.dataset_split_dict['random_state']),
                         "Valid Split":self.dataset_split_dict['valid_ratio'],
                         "CV (K-Fold )":self.dataset_split_dict['cv']}
        
        
        return model_summary
      
      
       
    def cv_score(self,X_train,y_train):
        
        """This function is used to get cv score.

        Returns:
            [float]: [it will return cv score.]
        """

        if X_train.shape[1] == 2:
            X_train = X_train[:,1:].reshape(-1, 1)
        else:
            X_train = X_train[:,1:]
        y_train = y_train[:,-1].reshape(len(y_train[:,-1]),1)
        
        shuffle = KFold(n_splits=self.dataset_split_dict['cv'],
                    shuffle=True,
                    random_state=self.dataset_split_dict['random_state'])
        
        cv_scores = cross_val_score(estimator=LinearRegression(),
                                X=X_train,
                                y=y_train,
                                cv=shuffle,
                                scoring='r2')
        cv_score_mean = cv_scores.mean()

        return cv_score_mean
        
        
    def holdout_score(self,model,X_test,y_test):
        
        """This function is used to get holdout score.

        Args:
            model ([object]): [train model object.]
            X_test ([dataframe]): [input test data dataframe.]
            y_test ([dataframe]): [target test data dataframe.]

        Returns:
            [float]: [it will return holdout score.]
        """
        X_test = X_test[:, 1:]
        actual = y_test[:, 1]
        
        prediction = model.predict(X_test)
        holdout_score = r2_score(actual,prediction)

        return holdout_score

        
    def run_pipeline(self):
        
        """This function is used as a pipeline which will execute function in a sequence.
        """
        # train the model
        model = self.train_model(self.X_train,self.y_train)
        # get features importance
        features_impact_dict = self.features_importance(model,self.X_train) 
        # get actual and predicted values 
        actual_lst,prediction_lst = self.get_actual_prediction(model,self.X_test,self.y_test)
        # save prediction
        final_result_dict = self.save_prediction(self.y_test,prediction_lst)
        # all evaluation matrix
        r2score,mse,mae,mape = self.get_evaluation_matrix(actual_lst,prediction_lst)  
        # get cv score
        if self.dataset_split_dict['split_method'] == 'cross_validation':
            cv_score = self.cv_score(self.X_train,self.y_train) # default k-fold with 5 (r2-score)
        else:
            cv_score = 0
        # get holdout score
        holdout_score = self.holdout_score(model,self.X_test,self.y_test) # default 80:20 splits (r2-score)
        # get model summary
        model_summary = self.model_summary(self.X_train,self.X_test,self.y_train) # high level model summary
        # get model learning curve
        learning_curve_dict = self.get_learning_curve(model,self.X_train,self.y_train)
        
        
        
        # log mlflow parameter
        mlflow.log_param("split method", self.dataset_split_dict['split_method'])
        mlflow.log_param("train ratio", 1-(self.dataset_split_dict['test_ratio'] + self.dataset_split_dict['valid_ratio']))
        mlflow.log_param("test ratio", self.dataset_split_dict['test_ratio'])
        mlflow.log_param("valid ratio", self.dataset_split_dict['valid_ratio'])
        mlflow.log_param("random state", self.dataset_split_dict['random_state'])
        mlflow.log_param("k-fold", self.dataset_split_dict['cv'])
        mlflow.log_param("train size", self.dataset_split_dict['train_size'])
        mlflow.log_param("test size", self.dataset_split_dict['test_size'])
        mlflow.log_param("valid size", self.dataset_split_dict['valid_size'])
        
        # log mlflow matrix
        mlflow.log_metric("r2 score", r2score)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("mape", mape)
        mlflow.log_metric("holdout_score", holdout_score)
        mlflow.log_metric("cv_score", cv_score)
       
        # log artifacts (output files)
        mlflow.sklearn.log_model(model,"Linear_Regressor_Model")
        mlflow.log_dict(learning_curve_dict,"learning_curve.json")
        mlflow.log_dict(features_impact_dict,"features_importance.json")
        mlflow.log_dict(model_summary,"model_summary.json")
        mlflow.log_dict(final_result_dict,"predictions.json")
        print("ENDING\n\n\n\n\n DONE--------------------------------------------")
        
        
        
        
        
        
        
               
        
        
