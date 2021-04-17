# Keras specific
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
import shap

from modeling.utils.model_common_utils.evaluation_metrics import EvaluationMetrics as EM
from modeling.utils.model_common_utils.mlflow_artifacts import MLFlowLogs 
from tensorflow import keras 


from sklearn.model_selection import ( train_test_split, 
                                     GridSearchCV, 
                                     cross_val_score, 
                                     cross_val_predict,
                                     KFold )

from sklearn.metrics import *


class KerasLogisticRegressionClass:
    
    def __init__(self,input_features_list,target_features_list,# labels,
                X_train, X_valid, X_test, y_train, y_valid, y_test, scaled_split_dict,
                hyperparameters):
        
        self.input_features_list = input_features_list[1:] 
        # list of target features (features to be predicted)
        self.target_features_list = target_features_list[1:]
        self.dataset_split_dict = scaled_split_dict # This object stores the variables used to split the data. 
    
        ## Tarin Test Split Data
        self.X_train = X_train
        self.y_train = y_train
        
        self.X_valid = X_valid
        self.y_valid = y_valid
        
        self.X_test = X_test
        self.y_test = y_test
        
        #### INPUT AND TARGET ######
        self.input_dim = len(self.input_features_list)
        self.output_dim = len(self.target_features_list)
        
        # Hyper Parameter list
        self.learning_rate = float(hyperparameters['learning_rate'])
        self.epoch = int(hyperparameters['epochs'])
        self.batch_size = int(hyperparameters['batch_size'])
        self.loss = hyperparameters['loss'].lower()
        self.optimizer = hyperparameters['optimizer'].lower()


        self.EvalMetricsObj = EM()
        self.MLFlowLogObj = MLFlowLogs()


    def create_model(self):
        # Define model
        layers = 3
        neurons = [64, 16, 1]
        activation = ['relu', 'relu', 'sigmoid']
        model = tf.keras.Sequential()
        layer_info = tf.keras.layers.Dense(units=int(neurons[0]), input_shape=(len(self.input_features_list), ), activation=activation[0].lower())
        model.add(layer_info)

        for layer in range(layers-1):
            layer_info = tf.keras.layers.Dense(units=int(neurons[layer+1]), activation=activation[layer+1].lower())
            model.add(layer_info)


        if self.optimizer.lower() == "adam":
            opt = keras.optimizers.Adam(learning_rate=self.learning_rate)
            
        elif self.optimizer.lower() == "sgd":
            opt = keras.optimizers.SGD(learning_rate=self.learning_rate)
        
        elif self.optimizer.lower() == 'rmsprop':
            opt = keras.optimizers.RMSprop(learning_rate=self.learning_rate)
        
        model.compile(loss= self.loss , optimizer=opt, metrics=["accuracy"])

        return model


    def train_model(self):
        
        X_train = self.X_train[:,1:]
        y_train = self.y_train[:,-1].reshape(-1, 1)
        X_test = self.X_test[:, 1:]
        y_test = self.y_test[:, -1].reshape(-1, 1)

        model = self.create_model()
        H = model.fit(X_train, y_train, epochs=self.epoch,batch_size=self.batch_size,
                    validation_data=(X_test, y_test))
     
        return model,H
        

    def get_learning_curve(self, H):

        train_loss = np.array(H.history['loss']).astype(np.float64).tolist()
        train_accuracy = np.array(H.history['accuracy']).astype(np.float64).tolist()
        
        valid_loss = np.array(H.history['val_loss']).astype(np.float64).tolist()
        valid_accuracy = np.array(H.history['val_accuracy']).astype(np.float64).tolist()
        
        epochs = H.epoch
        
        learning_curve_dict = {'train_score': train_accuracy, 'test_score': valid_accuracy, 'train_loss': train_loss, 
                'test_loss': valid_loss, 'train_size': epochs}
        return learning_curve_dict


    def features_importance(self,model):

        shap_data = self.X_train[:min(100, self.X_train.shape[0]), 1:]
        deepexplainer = shap.DeepExplainer(model, shap_data)
        shap_values = deepexplainer.shap_values(shap_data[:20])
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
  
        prediction_arr = (model.predict(X_test) > 0.5).astype("int8").reshape(-1, )
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
        
        model_summary = {"Model Name":"Logistic_Regression_Keras",
                         "Input Features":self.input_features_list,
                         "Target Features":self.target_features_list,
                         "Learning Rate": self.learning_rate,
                         "Optimizer": self.optimizer,
                         "Loss": self.loss,
                         "Epochs": self.epoch,
                         "Batch Size": self.batch_size,
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

        model = tf.keras.wrappers.scikit_learn.KerasClassifier(self.create_model, batch_size=self.batch_size)
        
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
        # train the model
        model, History = self.train_model()
        print("train model")

        # get model learning curve
        learning_curve_dict = self.get_learning_curve(History)
        print(" learning_curve_dict ")

        # get features importance
        features_impact_dict = self.features_importance(model) 
        print("features importanace")

        # get actual and predicted values 
        actual_lst,prediction_lst = self.get_actual_prediction(model)
        print("actual ",actual_lst)
        print("prediction_lst ")

        # save prediction
        final_result_dict = self.EvalMetricsObj.save_prediction(self.y_test, prediction_lst, self.target_features_list)
        print("final_result_dict ")

        # all evaluation matrix
        accuracy,recall,precision,f1_score = self.EvalMetricsObj.get_evaluation_matrix(actual_lst,prediction_lst, model_type='Classification')   
        print(" accuracy recall precision ")

        # get cv score
        if self.dataset_split_dict['split_method'].lower() == 'cross_validation':
            cv_score = self.cv_score(model) # default k-fold with 5 (r2-score)
        else:
            cv_score = 0
        print(" cv_score ")
        
        # get model summary
        model_summary = self.model_summary() # high level model summary
        print(" model_summary ")
        
        # get holdout score
        holdout_score = self.EvalMetricsObj.holdout_score(self.y_test, prediction_lst, model_type='Classification') # default 80:20 splits (r2-score)
        print(" holdout_score ")

        precision_recall_dict = self.EvalMetricsObj.get_precision_recall(model, self.X_test, self.y_test, lib='keras')

        # log mlflow matrix
        self.MLFlowLogObj.store_model_metrics(accuracy=accuracy, recall=recall, precision=precision, f1_score=f1_score,
                                            holdout_score=holdout_score, cv_score=cv_score)

        # log artifacts (output files)
        self.MLFlowLogObj.store_model_dict(learning_curve=learning_curve_dict, features_importance=features_impact_dict,
                                            model_summary=model_summary, predictions=final_result_dict, precision_recall=precision_recall_dict)

        # log mlflow parameter
        self.MLFlowLogObj.store_model_params(self.dataset_split_dict)

        # Store the Machine Learning Model.
        self.MLFlowLogObj.store_model(model, model_name="Logistic_Regression_Keras", model_type='keras')

        print("ENDING\n\n\n\n\n DONE--------------------------------------------")
