import pandas as pd
import numpy as np
import logging
from common.utils.logger_handler import custom_logger as cl

user_name = 'admin'
log_enable = True
LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()
logger = logging.getLogger('missing_value_handling')


class MissingValueClass:

    def mean_imputation(self,dataframe,column_id):
        """
        Function will replace column NaN value with its column mean value
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]  

        """
        logging.info("Preprocess : MissingValueClass : mean_imputation : execution start")
        for index in column_id:
            logging.info(str(dataframe))
            logging.info(str(index))
            logging.info(str(dataframe.columns[np.int(index)]))

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #Replace the NaN value with mean of the column 
            dataframe[column_name] = dataframe[column_name].fillna(round(dataframe[column_name].mean(),2),inplace = True)

            return dataframe[column_name]
        logging.info("Preprocess : MissingValueClass : mean_imputation : execution stop")
        return dataframe
    
    def median_imputation(self,dataframe,column_id):
        """
        Function will replace column NaN value with its column median value
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : median_imputation : execution start")

        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #Replace the NaN value with median of the column 
            dataframe[column_name].fillna(round(dataframe[column_name].median()),inplace = True)

        logging.info("Preprocess : MissingValueClass : median_imputation : execution stop")
        return dataframe
    
    def mode_imputation(self,dataframe,column_id):
        """
        function will replace column NaN value with its column mode value
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : mode_imputation : execution start")

        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #Replace the NaN value with Mode of the column
            dataframe = dataframe[column_name].fillna(round(dataframe[column_name].mode()),inplace = True)

        logging.info("Preprocess : MissingValueClass : mode_imputation : execution stop")
        return dataframe
    
    def end_of_distribution(self,dataframe,column_id):
        """
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : end_of_distribution : execution start")

        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #get the extreme distribution value based on the formula
            extreme = dataframe[column_name].mean()+3*dataframe[column_name].std()

            #replace the NaN value extreme distribution value
            dataframe[column_name].fillna(round(extreme,2),inplace = True)

        logging.info("Preprocess : MissingValueClass : end_of_distribution : execution stop")
        return dataframe
    
    def random_sample_imputation(self,dataframe,column_id):
        """
        Function will replace column NaN value with random values
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution start")
        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            ## it will have the random sample to fill NaN value
            random_sample = dataframe[column_name].dropna().sample(dataframe[column_name].isnull().sum(),random_state=1)

            ## pandas need to have same index in order to merge the dataset
            random_sample.index = dataframe[dataframe[column_name].isnull()].index

            #insert the random number into its specific index location
            dataframe.loc[dataframe[column_name].isnull(),column_name] = random_sample
        
        logging.info("Preprocess : MissingValueClass : random_sample_imputation : execution stop")

        return dataframe
    

    def add_missing_category(self,dataframe,column_id):
        """
        Function will replace column NaN value with "Missing"  category name
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : add_missing_category : execution start")
        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #add the "Missing" category where it find the NaN value
            dataframe[column_name] = np.where(dataframe[column_name].isnull(),"Missing",dataframe[column_name])

        logging.info("Preprocess : MissingValueClass : add_missing_category : execution stop")
        return dataframe
    
    def frequent_category_imputation(self,dataframe,column_id):
        """
        Function will replace column NaN value with most frequent used category name
        Args:
                dataframe[(pandas.Series)] : [the Series containing the column data]
                column_id[(Integer)] : [index of the columns]
        Return:
                dataframe[(pandas.Series)] : [return the updated dataframe]
        """
        logging.info("Preprocess : MissingValueClass : frequent_category_imputation : execution start")

        for index in column_id:

            #get the dataframe column name based on index
            column_name = dataframe.columns[np.int(index)]

            #get the most occuring category
            frequent_category = dataframe[column_name].value_counts().index[0]

            #Replace the NaN value with most occuring category
            dataframe[column_name].fillna(frequent_category,inplace = True)
        
        logging.info("Preprocess : MissingValueClass : frequent_category_imputation : execution stop")
        return dataframe