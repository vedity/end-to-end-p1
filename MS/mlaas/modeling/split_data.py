from sklearn.model_selection import train_test_split



class SplitData:
    '''
        A Class which maintains the attributes of train, test, validation ratios.

    '''
    def __init__(self, split_dataset):
        # self.split_dataset = split_dataset
        self.model_mode = split_dataset['model_mode']
        if self.model_mode == 'manual':
            self.split_method = split_dataset['method']
            self.random_state = split_dataset['random_state']
            
            if split_dataset == 'cross_validation':
                self.test_size = split_dataset['test_size']
                self.train_size = 1 - self.test_size
                self.cv = split_dataset['cv']
            else:
                self.test_size = split_dataset['test_size']
                self.train_size = 1 - split_dataset['test_size']
                self.valid_size = split_dataset['valid_size']
        else:
            self.split_method = 'cross_validation'
            self.train_size = 0.8
            self.test_size = 0.2
            self.cv = 5
            self.random_state = 0
        

    # def get_auto_split_data_object(self, model_name, DBObject, connection):
    #     sql_command = 'select split_method,cv,valid_size,test_size,random_state from mlaas.split_data_tbl where model_name='+model_name
    #     split_dataset = 

    # def get_split_params(self):
    #     if self.split_method == 'cross_validation':
    #         return self.split_method, 1 - self.split_dataset['test_size'], self.split_dataset['test_size'],
    #                 self.split_dataset['cv']
    #     else:
    #         return self.split_method, split_dataset['train_size'], split_dataset['valid_size'],
    #                 split_dataset['test_size']

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

