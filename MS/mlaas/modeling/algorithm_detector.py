class AlgorithmDetector:

    def __init__(self, target_df, DBObject, connection):
        # self.target_df = target_df
        self.DBObject = DBObject
        self.connection = connection
        self.algorithm_type, self.model_type = self.set_model_type(target_df)
        self.models_list = self.show_models_list()
        


    def set_model_type(self, target_df):
        """Returns the list of all algorithm using the model_type and algorithm_type.

        Args:
            target_df ([DataFrame]): [Target values of the target features.]

        Returns:
            [string, string]: [algorithm type, model type]
        """
        algorithm_type = None
        model_type = None
        if len(target_df) == 0:
            algorithm_type = 'unsupervised'
            self.algorithm_type, self.model_type = algorithm_type, model_type
            return algorithm_type, model_type
        else:
            target_shape = target_df.shape
            if target_shape[1] == 2:
                algorithm_type = 'Single_target'
            elif target_shape[1] > 2:
                algorithm_type = 'Multi_target'
            total_length = target_shape[0]
            # print(target_shape)
            print('Algorithm Detector:- ', target_shape)
            unq_length = len(target_df.iloc[:,1].unique())

            threshold = int((total_length * 20) / 100)

            if threshold < unq_length :
                model_type = 'Regression'
            else:
                if unq_length == 2:
                    model_type = 'Binary_Classification'
                elif unq_length > 2:
                    model_type = 'MultiClass_Classification'
            self.algorithm_type, self.model_type = algorithm_type, model_type
            return algorithm_type, model_type


    def get_model_types(self):
        return self.algorithm_type, self.model_type
    
    def show_models_list(self):
        sql_command = 'select * from mlaas.model_master where model_type='+self.model_type+' and algorithm_type='+self.algorithm_type
        self.models_list = self.DBObject.select_records(self.connection, sql_command)
        return self.models_list


    def get_hyperparameters_list(self, model_name):
        sql_command = 'select model_parameter from mlaas.model_master_tbl where model_name='+model_name
        hyperparameters_list = self.DBObject.select_records(self.connection, sql_command).to_json()
        return hyperparameters_list


        

# How to get the DBObject, and connection in the class AlgorithmDetector?

#Update my code in model_identifier.
