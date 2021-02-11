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

from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import learning_curve

from sklearn.metrics import *

from sklearn.model_selection import ( train_test_split, 
                                     GridSearchCV, 
                                     cross_val_score, 
                                     cross_val_predict,
                                     KFold )


class LogisticClassifierClass:
    
    def __init__(self,input_df,target_df,test_size,random_state,cv):
        
        """This is used to initialise the model input parameter when model class is called.
        """
        
        self.input_df = input_df
        self.target_df = target_df
        self.test_size = test_size
        self.random_state = random_state
        self.cv = cv
        self.input = input_df.columns.values.tolist()
        self.input.remove('seq_id')
        self.target = target_df.columns.values.tolist()
        self.target.remove('seq_id')
        
        self.input_features = self.input
        self.target_features = self.target
           
     
    
    
    def split_dataset(self):
        
        """This function is used to splits the dataset.

        Returns:
            [dataframe]: [it will return train and test data dataframe.]
        """
        
        X_train, X_test, y_train, y_test = train_test_split(self.input_df,
                                                            self.target_df, 
                                                            test_size=self.test_size, 
                                                            random_state=self.random_state
                                                            )
        
        
        return X_train, X_test, y_train, y_test
    
        
    def train_model(self,X_train,y_train):
        
        """This function is used to train the model.

        Args:
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]

        Returns:
            [object]: [it will return train model object.]
        """
        # get Input Training Features
        X_train = X_train[self.input_features] 
        # get Target Tarining Features
        y_train = y_train[self.target_features] 
        
        # Note, solvers available: {‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’}, default=’lbfgs’
        # define the model
        model = LogisticRegression(solver='sag')
        # fit the model
        model.fit(X_train, y_train) 

        return model
    
    def get_learning_curve(self,model,X_train,y_train):
        
        """This function is get learning curve.

        Args:
            model ([object]): [train model object]
            X_train ([dataframe]): [input train data]
            y_train ([dataframe]): [target train data]
        """
        
        X_train = X_train[self.input_features]
        y_train = y_train[self.target_features]
        
        train_sizes=np.linspace(0.10, 1.0, 5)
        train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator = model, X=X_train, y=y_train,cv=2,
                       train_sizes=train_sizes,
                       return_times=True)
        
        train_mean = train_scores.mean(axis=1)
        test_mean = test_scores.mean(axis=1)
        
    def features_importance(self,model,X_train):
        
        """This function is used to get features impact.

        Returns:
            [dict]: [it will return features impact dictionary.]
        """
        
        
        X_train = X_train[self.input_features]
        stddev = []
        importance = model.coef_.tolist()[0]
        
        features = pd.DataFrame(importance, self.input_features ,columns = ['coefficient'])
        features.coefficient = features.coefficient.abs()
        
        for i in self.input_features:
            stdev = X_train[i].std()
            stddev.append(stdev)
         
        features['stddev'] = np.array(stddev).reshape(-1,1)
        features['importance'] = features['coefficient'] * features['stddev']
        features['norm_importance'] = 100 * features['importance'] / features['importance'].max()
        
        features['features_name'] = features.index
        sorted_df = features.sort_values(by='norm_importance')
        
        features_impact_dict = sorted_df[['features_name','norm_importance']].to_dict(orient='list')
        
        return features_impact_dict
       
    def save_model(self,model):
        
        """This function is used to save model file.
        """
        
        filename = 'logistic_classifier_finalized_model.sav'
        # pickle.dump(model, open(filename, 'wb'))

    def get_actual_prediction(self,model,X_test,y_test):
        
        """This function is used to get actuals and predictions.

        Returns:
            [list]: [it will return actual and prediction list.]
        """
        
        X_test = X_test[self.input_features]
  
        prediction_arr = model.predict(X_test)
        prediction_flat_lst = prediction_arr.tolist()

        actual_df= y_test[self.target_features]
        actual_lst = actual_df.values.tolist()
        actual_flat_lst = [int(item) for elem in actual_lst for item in elem]
        
        return actual_flat_lst,prediction_flat_lst
        
        
    
    def get_evaluation_matrix(self,actual_lst,prediction_lst):
        
        """This function is used to find model performance matrices.
        
        Returns:
            [dict]: [it will return model matrices.]
        """
        
        score = accuracy_score(actual_lst,prediction_lst)
        ## Accuray e AUC
        accuracy = accuracy_score(actual_lst, prediction_lst)
#         auc = roc_auc_score(actual_lst, prediction_lst,average='micro',multi_class='raise')
        ## Precision e Recall
        recall = recall_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
        precision = precision_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
        
        classes = np.unique(actual_lst)
        
        CM = confusion_matrix(actual_lst,prediction_lst,labels=classes)
        
        return CM,round(accuracy,2),round(recall,2),round(precision,2)
        
    def model_summary(self,X_train, X_test,y_train):
        
        """This function is used to get model summary.

        Returns:
            [dict]: [it will return model summary.]
        """

        X_train = X_train[self.input_features]
        X_test = X_test[self.input_features]
        y_train = y_train[self.target_features]
        train_size = X_train.shape[0]
        test_size = X_test.shape[0]
        model_summary = {"Model Name":"Logistic Classifier",
                         "Input Features":self.input_features,
                         "Target Features":self.target_features,
                         "Train Size":train_size,"Test Size":test_size,
                         "Train Split":1-self.test_size,"Test Split":self.test_size,
                         "Random State":self.random_state,
                         "CV (K-Fold )":self.cv}
            
        return model_summary
        
       
    def cv_score(self,X_train,y_train):
        
        """This function is used to get cv score.

        Returns:
            [float]: [it will return cv score.]
        """
        
        X_train = X_train[self.input_features]
        y_train = y_train[self.target_features]
        
        shuffle = KFold(n_splits=self.cv,
                    shuffle=True,
                    random_state=self.random_state)
        
        cv_scores = cross_val_score(estimator=LogisticRegression(),
                                X=X_train,
                                y=y_train,
                                cv=shuffle)
        
        return  cv_scores.mean()
        
    def holdout_score(self,model,X_test,y_test):
        
        """This function is used to get holdout score.

        Args:
            model ([object]): [train model object.]
            X_test ([dataframe]): [input test data dataframe.]
            y_test ([dataframe]): [target test data dataframe.]

        Returns:
            [float]: [it will return holdout score.]
        """
        
        X_test = X_test[self.input_features]
        actual = y_test[self.target_features]
        
        prediction = model.predict(X_test)
        ho_score = accuracy_score(actual,prediction)

        return ho_score
      

    def save_prediction(self,y_test,prediction_lst):
        
        """This function is used to save test results or predictions.
        """
         
        y_test.reset_index(inplace = True, drop = True)
        append_str = '_prediction'
        target_features_suf_res = [sub + append_str for sub in self.target_features]
        test_results_df = pd.DataFrame(prediction_lst, columns = target_features_suf_res) 
        
        final_result_df = pd.concat([y_test,test_results_df],axis=1)
              
    def run_pipeline(self):
        
        """This function is used as a pipeline which will execute function in a sequence.
        """
        X_train, X_test, y_train, y_test = self.split_dataset()
        # train the model
        model = self.train_model(X_train,y_train)
        # get features importance
        features_impact_dict = self.features_importance(model,X_train) 
        # get actual and predicted values 
        actual_lst,prediction_lst = self.get_actual_prediction(model,X_test,y_test)
        # save prediction
        self.save_prediction(y_test,prediction_lst)
        # all evaluation matrix
        CM,accuracy,recall,precision = self.get_evaluation_matrix(actual_lst,prediction_lst)  
        # get cv score
        cv_scores = self.cv_score(X_train,y_train) # default k-fold with 5 (r2-score)
        # get holdout score
        ho_score = self.holdout_score(model,X_test,y_test) # default 80:20 splits (r2-score)
        # get model summary
        model_summary = self.model_summary(X_train, X_test,y_train) # high level model summary
        # get model learning curve
        self.get_learning_curve(model,X_train,y_train)
        # finally save the model
        # self.save_model(model) # it will save in pickle format
        
        # log mlflow parameter
        mlflow.log_param("random state", self.random_state)
        mlflow.log_param("train size", 1-self.test_size)
        mlflow.log_param("test size", self.test_size)
        mlflow.log_param("k-fold", self.cv)
        
        # log mlflow matrix
        # mlflow.log_metric("confusion matrix", CM)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("precision", precision)
       
        # log artifacts (output files)
        mlflow.sklearn.log_model(model,"Logistic_Classifier_Model")
        mlflow.log_dict(features_impact_dict,"features_importance.json")
        mlflow.log_dict(model_summary,"model_summary.json")
        
        
