from sklearn.model_selection import train_test_split
import json
import ast 
class SplitData:
    
    def __init__(self,basic_split_parameters,DBObject, connection):
        
        self.model_mode = basic_split_parameters['model_mode']
        
        if self.model_mode == 'manual':
            
            self.split_method, self.random_state, self.test_size, self.train_size, self.cv, self.valid_size = self.get_split_dataset(basic_split_parameters)
            
        else :
            sql_command = "select * from mlaas.auto_model_split_param_tbl"
            split_data_df=DBObject.select_records(connection,sql_command)
            split_param = split_data_df['split_param'][0]
            
            dataset_split_param_dict = ast.literal_eval(split_param)
            #TODO Need to change
            # config_path ="./modeling/basic_dataset_split_config.json"
            # json_data=open(config_path,'r') 
            # dataset_split = json_data.read()
            # dataset_split_param_dict = ast.literal_eval(dataset_split) 
                
                
            # dataset_split_param_dict = json.load(config_path)
            self.split_method = dataset_split_param_dict['split_method']
            self.random_state = dataset_split_param_dict['random_state']
            self.test_size = dataset_split_param_dict['test_size'] 
            self.train_size = dataset_split_param_dict['train_size']
            self.cv =  dataset_split_param_dict['cv']
            self.valid_size = dataset_split_param_dict['valid_size']
           
            
        # if self.model_mode == 'auto':
                #     self.split_method, self.random_state, self.test_size, self.train_size, self.cv, self.valid_size = self.get_auto_split_dataset(model_id, DBObject, connection)


    def get_split_dataset(self, dataset_split_parameters):
        """ Returns the splitting dataset parameters.
        Args:
        dataset_split_parameters (dictionary): [Contains the model_mode, and if required, other necessary parameters.]

        Returns:
            [tuple]: [dataset splitting method, and parameters required to split it.]
        """

        split_method = dataset_split_parameters['split_method']
        random_state = dataset_split_parameters['random_state']
        test_size = dataset_split_parameters['test_size']
        train_size = 1 - test_size
        
        if split_method == 'cross_validation':    
            cv = dataset_split_parameters['cv']
            valid_size = None
        else:
            valid_size = dataset_split_parameters['valid_size']
            cv = None
        # print(split_method, random_state, test_size, train_size, cv, valid_size)
        return split_method, random_state, test_size, train_size, cv, valid_size


    

    def get_split_data(self, X, y):
        """Returns train-test or train-valid-test split on the basis of split_method.

        Args:
            X (array/DataFrame): Input values.
            y (array/DataFrame): Target values.

        Returns:
            X_train, X_test, Y_train, Y_test or also returns X_valid, Y_valid: Splitted data for train and test.
        """
        if self.split_method == 'cross_validation':
            X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=self.test_size,
                                                                random_state=self.random_state)

            return X_train, None, X_test, Y_train, None, Y_test
        else:
            X_train_valid, X_test, Y_train_valid, Y_test = train_test_split(X, y, test_size=self.test_size,
                                                                        random_state=self.random_state)

            X_train, X_valid, Y_train, Y_valid = train_test_split(X_train_valid, Y_train_valid, test_size=self.valid_size,
                                                            random_state=self.random_state)

            return X_train, X_valid, X_test, Y_train, Y_valid, Y_test 

