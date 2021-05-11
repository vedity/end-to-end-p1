# example of anova f-test feature selection for numerical data
#Needed Encoding (Only numeric columns is allowed)
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif,f_regression
from .fs_utility import FSUtilityClass
import warnings
warnings.filterwarnings("ignore")

FU = FSUtilityClass()

class AnovaClass():
    # feature selection
    def select_anovaK_features(self,X_train, y_train, X_test):
        # configure to select all features
        comp = int(round((len(X_train.columns)/2)))
        fs = SelectKBest(score_func=f_classif, k=comp)

        # learn relationship from training data
        fs.fit(X_train, y_train)

        # transform train input data
        X_train_fs = fs.transform(X_train)

        # transform test input data
        X_test_fs = fs.transform(X_test)

        return X_train_fs, X_test_fs, fs

    def get_anova_info(self,DBObject,connection,dataset_id,schema_id,target_col,**kwargs):
        # load the dataset
        value_lst = []
        col,change_col = FU.get_numeric_schema_dtype(DBObject,connection,schema_id)
        df = DBObject.get_feature_df(connection,dataset_id,col,change_col)
        #target column Y
        targetcol,changecol = FU.fetch_column(DBObject,connection,schema_id)
        targetdf = DBObject.get_feature_df(connection,dataset_id,targetcol,changecol)
        X, y = FU.load_dataset(df,target_col,targetdf)
        algo_col = list(X.columns)
        # split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

        # feature selection
        X_train_fs, X_test_fs, fs = self.select_anovaK_features(X_train, y_train, X_test)

        # what are scores for the features
        #GET column name by get_support
        vector_names = list(X.columns[fs.get_support(indices=True)])
        col = FU.selectkbest_extra_column(DBObject,connection,schema_id,vector_names,algo_col)
        
        return col