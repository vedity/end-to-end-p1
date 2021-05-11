#coorelation feature selection
import pandas as pd
from sklearn.model_selection import train_test_split
from .fs_utility import FSUtilityClass
import logging

FU = FSUtilityClass()
class CoorelationClass():
    def get_coorelation(self,DBObject,connection,dataset_id,schema_id,target_col,**kwargs):
        col,change_col = FU.get_numeric_schema_dtype(DBObject,connection,schema_id)
        df = DBObject.get_feature_df(connection,dataset_id,col,change_col)

        #target column Y
        targetcol,change_col = FU.fetch_column(DBObject,connection,schema_id)
        targetdf = DBObject.get_feature_df(connection,dataset_id,targetcol,change_col)
        X, y = FU.load_dataset(df,target_col,targetdf)
        algo_column = list(X.columns)

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=1)
        cor=X_train.corr() #find coorelation matrix for X_train data
        corr_features=self.correlation_feature(X_train,0.7) #remove column having more then threshold value
        cf = list(corr_features)

        final_col =X_train.drop(corr_features,axis=1) # final column after droping coorelated column
        
        final_col = list(final_col.columns) #column list name
        
        co_col = FU.selectkbest_extra_column(DBObject,connection,schema_id,final_col,algo_column) # Column dict with selected or not boolean key value pair

        return co_col
    


    def correlation_feature(self,dataset, threshold):
        col_corr = set()  # Set of all the names of correlated columns\n",
        corr_matrix = dataset.corr()
        for i in range(len(corr_matrix.columns)):        
            for j in range(i):
                if abs(corr_matrix.iloc[i, j]) > threshold:
                        colname = corr_matrix.columns[i]  
                        col_corr.add(colname)
        return col_corr


