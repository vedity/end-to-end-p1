class AlgorithmDetector:
    """Maintains the track and data for algorithms and their respective hyperparameters.
    """
    def __init__(self, target_df, DBObject, connection):
        # self.target_df = target_df
        self.DBObject = DBObject
        self.connection = connection
        self.algorithm_type, self.model_type = self.set_model_type(target_df)
        # self.models_list = self.show_models_list()
        


    def set_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        algorithm_type = None
        model_type = None
        
        target_shape = target_df.shape
        total_length = target_shape[0]
        unq_length = len(target_df.iloc[:,1].unique())
        threshold = int((total_length * 10) / 100)

        if threshold < unq_length :
            model_type = 'Regression'
            
            if target_shape[1] == 2:
                algorithm_type = 'Single_Target'
            elif target_shape[1] > 2:
                algorithm_type = 'Multi_Target'
            
        else:
            model_type = 'Classification'
            if unq_length == 2:
                algorithm_type = 'Binary_Classification'
            elif unq_length > 2:
                algorithm_type = 'MultiClass_Classification'
                
        self.algorithm_type, self.model_type = algorithm_type, model_type
        
        return algorithm_type, model_type


    def get_model_types(self):
        """This function returns the algorithm and model type on the basis of target_df.

        Returns:
            tuple: algorithm_type (single_target, multi_target, unseupervised, and more), model_type (Regression, Classification, and more)
        """
        return self.algorithm_type, self.model_type
    
    def show_models_list(self):
        """Returns the compatible list of model on the basis of algorithm_type and model_type.

        Returns:
            list: models_list, contains list of all the ML/DL models derived from the algorithm and model type.
        """
        print('In show models_list')
        sql_command = "select model_name from mlaas.model_master_tbl where model_type='"+self.model_type+"'"+" and algorithm_type='"+self.algorithm_type+"'"
        self.models_list = self.DBObject.select_records(self.connection, sql_command)
        return self.models_list


    def get_hyperparameters_list(self, model_name):
        """Returns the appropriate list of hyperparameters associated with the model_name argument.

        Args:
            model_name (string): name of the ML/DL model.

        Returns:
            list: list of hyperparameters of the model 'model_name'.
        """
        print('Model_name:- ', model_name)
        sql_command = "select model_parameter from mlaas.model_master_tbl where model_name='"+model_name+"'"
        print('SQL Command:- ', sql_command)
        hyperparameters_list = self.DBObject.select_records(self.connection, sql_command)
        print(hyperparameters_list)
        return hyperparameters_list


        

# How to get the DBObject, and connection in the class AlgorithmDetector?

#Update my code in model_identifier.
