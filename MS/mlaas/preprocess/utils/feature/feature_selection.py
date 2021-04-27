from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import LabelEncoder
from .fs_utility import FSUtilityClass
from .mutual_info import MutualInfoClass
from .chisq import ChiSquareClass
from .RFE import RFEClass
from .anova import AnovaClass
from .coorelation import CoorelationClass
import logging
import warnings
warnings.filterwarnings("ignore")


# fu = FSUtilityClass()
# mi = MutualInfoClass()
# cs = ChiSquareClass()
# rfe = RFEClass()
# an = AnovaClass()
# cf = CoorelationClass()
class FeatureSelectionClass(FSUtilityClass,MutualInfoClass,ChiSquareClass,RFEClass,AnovaClass,CoorelationClass):

    def algo_call(self,DBObject,connection,dataset_id,schema_id,target_col,choice):
        if choice ==1:
            #Chisq
            col_lst,value_lst = self.chisq_result(DBObject,connection,dataset_id,schema_id,target_col)
            extra_col,col = self.get_extra_column(DBObject,connection,schema_id,col_lst)
            chisq_col = {**value_lst ,**extra_col } #! merge 2 dict 
            
            #RFE
            rfe_col = self.get_RFE(DBObject,connection,dataset_id,schema_id,target_col)

            #mutual
            mutual_col = self.get_mutual_info(DBObject,connection,dataset_id,schema_id,target_col)

            #anova
            anova_col = self.get_anova_info(DBObject,connection,dataset_id,schema_id,target_col)   

            #coorelation
            co_col = self.get_coorelation(DBObject,connection,dataset_id,schema_id,target_col)

        return chisq_col,rfe_col,mutual_col,anova_col,co_col

    def get_extra_column(self,DBObject,connection,schema_id,col_lst):

        col = self.fetch_column(DBObject,connection,schema_id)
        extra_col = {}
        for i in col:
            if i not in col_lst:
                # val = i+":False"
                # extra_col.append(val)
                extra_col[i] = "True"
            else:
                continue
        return extra_col,col

    


    

   
