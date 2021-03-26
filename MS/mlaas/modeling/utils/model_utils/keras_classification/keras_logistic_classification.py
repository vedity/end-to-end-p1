# # Keras specific
# import pandas as pd
# import numpy as np
# import pickle
# import tensorflow as tf
# from tensorflow import keras 

# import shap
# import matplotlib.pyplot as plt

# from sklearn.model_selection import ( train_test_split, 
#                                      GridSearchCV, 
#                                      cross_val_score, 
#                                      cross_val_predict,
#                                      KFold )

# from sklearn.metrics import *


# class KerasLogisticRegressionClass:
    
#     def __init__(self,input_features_lst,target_features_lst, labels,
#                  X_train,y_train,X_valid,y_valid,X_test,y_test,
#                 learning_rate,epoch,batch_size,loss,optimizer,activation,cv,random_state):
        
#         self.input_features_list = input_features_lst[1:] 
#         # list of target features (features to be predicted)
#         self.target_features_list = target_features_lst[1:] 
#         self.labels = labels
        
#         self.cv = cv
#         self.random_state = random_state
    
#         ## Tarin Test Split Data
#         self.X_train = X_train
#         self.y_train = y_train
        
#         self.X_valid = X_valid
#         self.y_valid = y_valid
        
#         self.X_test = X_test
#         self.y_test = y_test
        
#         #### INPUT AND TARGET ######
#         self.input_dim = len(self.input_features_list)
#         self.output_dim = len(self.target_features_list)
        
#         # Hyper Parameter list
#         self.learning_rate = learning_rate
#         self.epoch = epoch
#         self.batch_size = batch_size
#         self.loss = loss
#         self.optimizer = optimizer
#         self.activation = activation


#     def train_model(self):
        
#         X_train = self.X_train[:,1:]
#         y_train = self.y_train[:,-1]
        
#         # Define model
#         model = keras.Sequential([
#             keras.layers.Dense(units=64, input_shape=(len(self.input_features_list),), activation='relu'),
#             keras.layers.Dense(units=16, activation='relu'),
#             keras.layers.Dense(units=1, activation='sigmoid'),
#         ])
        

#         #model.summary() #Print model Summary
        
#         if self.optimizer == "adam":
#             opt = keras.optimizers.Adam(learning_rate=self.learning_rate)
            
#         elif self.optimizer == "sgd":
#             opt = keras.optimizers.SGD(learning_rate=self.learning_rate)
            
#         model.compile(loss= self.loss , optimizer=opt, metrics=["accuracy"])
#         H = model.fit(X_train, y_train, epochs=self.epoch,batch_size=self.batch_size,validation_data=(X_test[:, 1:], y_test[:, 1]))#Need To change this
     
#         return model,H
        
#     def get_learning_curve(self, H):

#         train_loss = H.history['loss']
#         train_accuracy = H.history['accuracy']
        
#         valid_loss = H.history['val_loss']
#         valid_accuracy = H.history['val_accuracy']
        
#         epochs = H.epoch
        
#         learning_curve_dict = {'train_score': train_accuracy, 'valid_score': valid_accuracy, 'train_loss': train_loss, 
#                 'valid_loss': valid_loss, 'epochs': epoch}
#         return learning_curve_dict


#     def get_actual_prediction(self,model):
        
#         """This function is used to get actuals and predictions.

#         Returns:
#             [list]: [it will return actual and prediction list.]
#         """
#         X_test = self.X_test[:, 1:]
        
#         prediction_arr = (model.predict(X_test) > 0.5).astype("int8")
#         prediction_lst = prediction_arr.tolist()

#         actual_values = self.y_test[:,1].reshape(-1, 1)
#         actual_lst = actual_values.tolist()
    
#         if len(self.target_features_list) == 1 :
#             actual_flat_lst = actual_lst 
    
#             return actual_lst,prediction_lst
        
#         else:
            
#             prediction_flat_lst =  [ list(map(sub_lst)) for sub_lst in prediction_lst ]
#             actual_flat_lst =  [ list(map(sub_lst)) for sub_lst in actual_lst ]
#             return actual_flat_lst,prediction_flat_lst

    
#     def save_prediction(self,prediction_lst):
        
#         """This function is used to save test results or predictions.
#         """
         
#         y_df = pd.DataFrame(self.y_test[:,1],columns=self.target_features_list)
        
#         y_df.reset_index(inplace = True, drop = True)
        
#         y_df['index']=self.y_test[:,0]
        
#         append_str = '_prediction'
        
#         target_features_suf_res = [sub + append_str for sub in self.target_features_list]
#         test_results_df = pd.DataFrame(prediction_lst, columns = target_features_suf_res) 
        
#         final_result_df = pd.concat([y_df,test_results_df],axis=1)
#         print("final results ==",final_result_df)
#         final_result_dict = final_result_df.to_dict(orient='list') 
# #         print("final results dict ==",final_result_dict)
        
#         return final_result_dict

    
#     def get_evaluation_matrix(self,actual_lst,prediction_lst):
        
#         """This function is used to find model performance matrices.
        
#         Returns:
#             [dict]: [it will return model matrices.]
#         """
#         print("actual_lst", actual_lst[:10])
#         print("prediction_lst", prediction_lst[:10])
#         score = accuracy_score(actual_lst,prediction_lst)
#         ## Accuray e AUC
#         accuracy = accuracy_score(actual_lst, prediction_lst)
# #         auc = roc_auc_score(actual_lst, prediction_lst,average='micro',multi_class='raise')
#         ## Precision e Recall
#         recall = recall_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
#         precision = precision_score(actual_lst, prediction_lst, pos_label='positive',average='micro')
#         # print('ACTUAL LSTTT:-         ', actual_lst.shape)
#         classes = self.labels
#         CM = confusion_matrix(actual_lst,prediction_lst)
#         CM_df = pd.DataFrame(CM, columns=self.labels+'_true', index=self.labels+'_predicted')
#         CM_dict = CM_df.to_dict()

#         return CM_dict,round(accuracy,2),round(recall,2),round(precision,2)

    
#     def model_summary(self,X_train, X_test,y_train):
        
#         """This function is used to get model summary.

#         Returns:
#             [dict]: [it will return model summary.]
#         """

#         train_size = X_train.shape[0]
#         test_size = X_test.shape[0]
        
#         model_summary = {"Model Name":"Linear_Regression_Sklearn",
#                          "Input Features":self.input_features_list,
#                          "Target Features":self.target_features_list,
#                          "Train Size":float(train_size),"Test Size":int(test_size),
#                          "Train Split":1-(self.dataset_split_dict['test_ratio'] + self.dataset_split_dict['valid_ratio']),
#                          "Test Split":float(self.dataset_split_dict['test_ratio']),
#                          "Random State":int(self.dataset_split_dict['random_state']),
#                          "Valid Split":self.dataset_split_dict['valid_ratio'],
#                          "CV (K-Fold )":self.dataset_split_dict['cv']}
        
        
#         return model_summary

    
#     def holdout_score(self,model,X_test,y_test):
        
#         """This function is used to get holdout score.

#         Args:
#             model ([object]): [train model object.]
#             X_test ([dataframe]): [input test data dataframe.]
#             y_test ([dataframe]): [target test data dataframe.]

#         Returns:
#             [float]: [it will return holdout score.]
#         """
#         X_test = X_test[:, 1:]
#         actual = y_test[:, 1]
        
#         prediction = (model.predict(X_test) > 0.5).astype("int8")
#         holdout_score = accuracy_score(actual,prediction)

#         return holdout_score