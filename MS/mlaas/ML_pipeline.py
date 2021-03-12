import mlflow



class MLPipelineClass:

    def store_model_params(self, dataset_split_dict):
        
        # log mlflow parameter TODO change it to a for loop in future.
        mlflow.log_param("split method", self.dataset_split_dict['split_method'])
        mlflow.log_param("train ratio", 1-(self.dataset_split_dict['test_ratio'] + self.dataset_split_dict['valid_ratio']))
        mlflow.log_param("test ratio", self.dataset_split_dict['test_ratio'])
        mlflow.log_param("valid ratio", self.dataset_split_dict['valid_ratio'])
        mlflow.log_param("random state", self.dataset_split_dict['random_state'])
        mlflow.log_param("k-fold", self.dataset_split_dict['cv'])
        mlflow.log_param("train size", self.dataset_split_dict['train_size'])
        mlflow.log_param("test size", self.dataset_split_dict['test_size'])
        mlflow.log_param("valid size", self.dataset_split_dict['valid_size'])

    def store_model_metrics(self, **kwargs):
        for key in kwargs.keys():
            mlflow.log_param(key, kwargs[key])
        
        