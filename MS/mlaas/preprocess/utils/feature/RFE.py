from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from .fs_utility import FSUtilityClass
from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from .fs_utility import FSUtilityClass
from pandas import read_csv
import warnings
warnings.filterwarnings("ignore")

FU = FSUtilityClass()

class RFEClass():
    def get_RFE(self,DBObject,connection,dataset_id,schema_id,target_col,**kwargs):
        value_lst = []

        # define dataset
        col = FU.fetch_column(DBObject,connection,schema_id)
        df = DBObject.get_feature_df(connection,dataset_id,col)
        X, y = FU.load_dataset(df,target_col)
        # define RFE
        rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=None)
        # fit RFE
        rfe.fit(X, y)
        # summarize all features
        dict_col_lst = dict()
        for i in range(X.shape[1]):
            #print('%s : %s' % (X.columns[i], rfe.support_[i]))
            value_lst.append('%s : %s' % (X.columns[i], rfe.support_[i]))
            dict_col_lst.update({X.columns[i]:str(rfe.support_[i])})
        return dict_col_lst