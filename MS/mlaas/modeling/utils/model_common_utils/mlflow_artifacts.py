'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Mann Purohit       25-JAN-2021           1.0           Initial Version 
 
*/
'''

import mlflow

class MLFlowLogs:

    def store_model(self, model, model_name, model_type):
        if model_type.lower() == 'sklearn':
            mlflow.sklearn.log_model(model,model_name)
        elif model_type.lower() == 'keras':
            mlflow.keras.log_model(model, model_name)

    def store_model_metrics(self, **kwargs):
        for key in kwargs.keys():
            mlflow.log_metric(key, kwargs[key])


    def store_model_dict(self, **kwargs):
        for key in kwargs.keys():
            mlflow.log_dict(kwargs[key], str(key)+'.json')
            

    def store_model_params(self, dataset_split_dict):
        for key in dataset_split_dict.keys():
            if ('file' or 'classes') not in key:
                mlflow.log_param(key, dataset_split_dict[key])
        mlflow.log_param("train ratio", 1-(dataset_split_dict['test_ratio'] + dataset_split_dict['valid_ratio']))