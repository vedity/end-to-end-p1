# # Keras specific
# import pandas as pd
# import numpy as np
# import pickle
# import keras
# import tensorflow as tf

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
#         model = Sequential()
#         model.add(Dense(128, activation= self.activation))
#         model.add(Dense(32, activation= self.activation))
#         model.add(Dense(1, activation='sigmoid'))
        
#         #model.summary() #Print model Summary
        
#         if self.optimizer == "adam":
#             opt = keras.optimizers.Adam(learning_rate=self.learning_rate)
            
#         elif self.optimizer == "sgd":
#             opt = keras.optimizers.SGD(learning_rate=self.learning_rate)
            
#         model.compile(loss= self.loss , optimizer=opt, metrics=["accuracy"])
#         H = model.fit(X_train, y_train, epochs=self.epoch,batch_size=self.batch_size,validation_split=0.2)#Need To change this
     
#         return model,H
        
#     def get_learning_curve(self, H):

#         learning_curve_dict = H.history
#         learning_curve_dict['epoch'] = H.epoch