import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelType():
    def get_model_type(self, target_df):
         """Returns the list of all algorithm using the model_type and algorithm_type.

         Args:
             target_df ([DataFrame]): [Target values of the target features.]

         Returns:
             [string, string]: [algorithm type, model type]
         """
         # This logic is used to distinguish different types of algorithms and models.
         target_df=np.array(target_df)
         target_shape = target_df.shape
         total_length = target_shape[0]
         unq_length = len(np.unique(target_df))
         threshold = int((total_length * 0.01) / 100) # Subject to change, further research.
         target_type = ""
         if threshold < unq_length:
             model_type = 'Regression'
         else:
             model_type = 'Classification'
           
         if unq_length == 2:
             algorithm_type = 'Binary'
         elif unq_length > 2:
             algorithm_type = 'MultiClass'   
               
         if target_shape[1] == 2:
             target_type = 'Single_Target'
         elif target_shape[1] > 2:
             target_type = 'Multi_Target'
       
         return model_type,algorithm_type,target_type


    def get_split_data(self, input_df, target_df, random_state, test_size, valid_size, split_method):
        """Returns train-test or train-valid-test split on the basis of split_method.

        Args:
            X (array/DataFrame): Input values.
            y (array/DataFrame): Target values.

        Returns:
            X_train, X_test, Y_train, Y_test or also returns X_valid, Y_valid: Splitted data for train and test.
        """
        if split_method == 'cross_validation':
            X_train, X_test, Y_train, Y_test = train_test_split(input_df, target_df, test_size=test_size,
                                                                random_state=random_state)

            return X_train, None, X_test, Y_train, None, Y_test
        else:
            X_train_valid, X_test, Y_train_valid, Y_test = train_test_split(input_df, target_df, test_size=test_size,
                                                                        random_state=random_state)

            X_train, X_valid, Y_train, Y_valid = train_test_split(X_train_valid, Y_train_valid, test_size=valid_size,
                                                            random_state=random_state)

            return X_train, X_valid, X_test, Y_train, Y_valid, Y_test
