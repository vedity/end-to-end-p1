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
# from MS.mlaas.modeling.views import SplitDataClass



 
class LinearRegressionClass:
    
    def __init__(self, input_features_list, target_features_list, X_train, X_valid, X_test, 
                y_train, y_valid, y_test, SplitDataObject):
        
        """This is used to initialise the model input parameter when model class is called.
        """

        # self.input_features_list = input_features_list # List of input features(which are used to train the model)
        # self.target_features_list = target_features_list # list of target features (features to be predicted)
        self.SplitDataObject = SplitDataObject # This object stores the variables used to split the data.
        # self.input_features_list.remove('index')
        self.input_features_list = input_features_list[1:] # List of input features(which are used to train the model)
        self.target_features_list = target_features_list[1:] # list of target features (features to be predicted)
        # self.input_features_list.remove('index')
        self.X_train = X_train 
        self.X_test = X_test
        self.X_valid = X_valid
        self.y_train = y_train
        self.y_test = y_test
        self.y_valid = y_valid
        
     
    
    
    # def get_split_dataset(self):
        
    #     """This function is used to splits the dataset.

    #     Returns:
    #         [dataframe]: [it will return train-test or train-valid-test data dataframe.]
    #     """
        
    #     return self.split_data_object.get_split_data(self.input_df, self.target_df)                                                                            
    
    #     # split_data_object
        
    def train_model(self,X_train,y_train):
        
        """This function is used to train the model.

        Args:
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]

        Returns:
            [object]: [it will return train model object.]
        """
        
        # get Input Training Features
        X_train = X_train[self.input_features_list] 
        # get Target Tarining Features
        y_train = y_train[self.target_features_list] 
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
        
        X_train = X_train[self.input_features_list]
        y_train = y_train[self.target_features_list]
        
        # Dividing train data size into bins.
        train_sizes=np.linspace(0.10, 1.0, 5)
        train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train, cv=None, scoring='r2',n_jobs=None,
                       train_sizes=train_sizes,
                       return_times=True)
        
        # Average of train score(accuracy).
        train_mean = train_scores.mean(axis=1)
        # Average of train score(accuracy).
        test_mean = test_scores.mean(axis=1)
        # Create the learning curve dictionary.
        learning_curve_dict = {"train_size":train_sizes.tolist(),"train_score":train_mean.tolist(),"test_score":test_mean.tolist()}
        
        return learning_curve_dict
        
    
    def features_importance(self,model,X_train):
        
        """This function is used to get features impact.

        Returns:
            [dict]: [it will return features impact dictionary.]
        """
        
        
        X_train = X_train[self.input_features_list]
        stddev = []
        importance = model.coef_.tolist()[0]
        
        features = pd.DataFrame(importance, self.input_features_list,columns = ['coefficient'])
        features.coefficient = features.coefficient.abs()
        
        for i in self.input_features_list:
            stdev = X_train[i].std()
            stddev.append(stdev)
         
        features['stddev'] = np.array(stddev).reshape(-1,1)
        features['importance'] = features['coefficient'] * features['stddev']
        features['norm_importance'] = 100 * features['importance'] / features['importance'].max()
        
        features['features_name'] = features.index
        sorted_df = features.sort_values(by='norm_importance')
        
        features_impact_dict = sorted_df[['features_name','norm_importance']].to_dict(orient='list')
        
        return features_impact_dict
 
    # def save_model(self,model):
        
        
    #     """This function is used to save model file.
    #     """
        
    #     # save the model to disk
    #     filename = 'linear_regressor_finalized_model.sav'
    #     pickle.dump(model, open(filename, 'wb'))

    def get_actual_prediction(self,model,X_test,y_test):
        
        """This function is used to get actuals and predictions.

        Returns:
            [list]: [it will return actual and prediction list.]
        """
        
        X_test = X_test[self.input_features_list]
  
        prediction_arr = model.predict(X_test)
        prediction_lst = prediction_arr.tolist()

        actual_df= y_test[self.target_features_list]
        actual_lst = actual_df.values.tolist()
        
        if len(self.target_features_list) == 1 :
            
            prediction_flat_lst = [int(item) for elem in prediction_lst for item in elem]
            actual_flat_lst = [int(item) for elem in actual_lst for item in elem]
            return actual_flat_lst,prediction_flat_lst
        
        else:
            prediction_flat_lst =  [ list(map(int,sub_lst)) for sub_lst in prediction_lst ]
            actual_flat_lst =  [ list(map(int,sub_lst)) for sub_lst in actual_lst ]
            return actual_flat_lst,prediction_flat_lst
        
        
    def save_prediction(self,y_test,prediction_lst):
        
        """This function is used to save test results or predictions.
        """
         
        y_test.reset_index(inplace = True, drop = True)
        append_str = '_prediction'
        target_features_suf_res = [sub + append_str for sub in self.target_features_list]
        test_results_df = pd.DataFrame(prediction_lst, columns = target_features_suf_res) 
        
        final_result_df = pd.concat([y_test,test_results_df],axis=1)
        final_result_dict = final_result_df.to_dict(orient='list') 
        
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
        
        X_train = X_train[self.input_features_list]
        X_test = X_test[self.input_features_list]
        y_train = y_train[self.target_features_list]
            
        train_size = X_train.shape[0]
        test_size = X_test.shape[0]
        print('SplitDataObject:- ', self.SplitDataObject)
        # print(self.valid
        
        # print('Type of cv:- ', type(self.split_data_object.cv))

        # json does not recognize NumPy data types. 
        # Convert the number to a Python int before serializing the object:
        model_summary = {"Model Name":"linear Regression",
                         "Input Features":self.input_features_list,
                         "Target Features":self.target_features_list,
                         "Train Size":int(train_size),"Test Size":int(test_size),
                         "Train Split":1-float(self.SplitDataObject.test_size),"Test Split":float(self.SplitDataObject.test_size),
                         "Random State":int(self.SplitDataObject.random_state),
                         "CV (K-Fold )":int(self.SplitDataObject.cv)}
        print(model_summary)
        return model_summary
      
      
       
    def cv_score(self,X_train,y_train):
        
        """This function is used to get cv score.

        Returns:
            [float]: [it will return cv score.]
        """
        
        
        
        X_train = X_train[self.input_features_list]
        y_train = y_train[self.target_features_list]
        
        shuffle = KFold(n_splits=self.SplitDataObject.cv,
                    shuffle=True,
                    random_state=self.SplitDataObject.cv)
        
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
        
        
        X_test = X_test[self.input_features_list]
        actual = y_test[self.target_features_list]
        
        prediction = model.predict(X_test)
        holdout_score = r2_score(actual,prediction)

        return holdout_score

        
        
        
    def run_pipeline(self):
        
        """This function is used as a pipeline which will execute function in a sequence.
        """
        
        # X_train, X_test, y_train, y_test = self.split_dataset()
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
        cv_score = self.cv_score(self.X_train,self.y_train) # default k-fold with 5 (r2-score)
        # get holdout score
        holdout_score = self.holdout_score(model,self.X_test,self.y_test) # default 80:20 splits (r2-score)
        # get model summary
        model_summary = self.model_summary(self.X_train,self.X_test,self.y_train) # high level model summary
        # get model learning curve
        learning_curve_dict = self.get_learning_curve(model,self.X_train,self.y_train)
        # finally save the model
        # self.save_model(model) # it will save in pickle format
        
        
        # log mlflow parameter
        mlflow.log_param("random state", self.SplitDataObject.random_state)
        mlflow.log_param("train size", 1-self.SplitDataObject.test_size)
        mlflow.log_param("test size", self.SplitDataObject.test_size)
        mlflow.log_param("k-fold", self.SplitDataObject.cv)
        
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
        print('This is done')
        
        
        
        
               
        
        
