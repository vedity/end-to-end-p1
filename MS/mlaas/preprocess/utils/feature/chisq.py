import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency
from .fs_utility import FSUtilityClass
import logging
FU= FSUtilityClass()
class ChiSquareClass():
    df =None
    p = None #P-Value
    chi2 = None #Chi Test Statistic
    dof = None
        
    dfObserved = None
    dfExpected = None

    def chisq_result(self,DBObject,connection,dataset_id,schema_id,target_col):
        col_lst = []
        value_lst = []
        dict_col_value = dict()
        col = FU.get_schema_dtype(DBObject,connection,schema_id)
        df = DBObject.get_feature_df(connection,dataset_id,col)
        
        for var in col:
           if var != target_col:
                column_name,value= self.TestIndependence(df,colX=var,colY=target_col)  
                col_lst.append(column_name)
                #value_lst.append(column_name+value)
                logging.info("&&&&"+str(column_name))
                d = {column_name:value}
                dict_col_value.update(d)
           else:
                continue
        logging.info("!!!!!!"+str(dict_col_value))
        return col_lst,dict_col_value
    
    def _print_chisquare_result(self,p, colX, alpha):
        result = ""
        #dict_col_value = {}
        if p<alpha:
            column_name = colX
            value = ":True"
           # dict_col_value[colX] = "True"
        else:
            column_name = colX
            value = ":False"
            #dict_col_value[colX] = "False"

        return column_name,value
        
        
    def TestIndependence(self,df,colX,colY,alpha=0.05):
        X = df[colX].astype(str)
        Y = df[colY].astype(str)
        
        dfObserved = pd.crosstab(Y,X) 
        chi2, p, dof, expected = stats.chi2_contingency(dfObserved.values)
        p = p
        chi2 = chi2
        dof = dof      
        dfExpected = pd.DataFrame(expected, columns=dfObserved.columns, index = dfObserved.index) 
        column_name,value = self._print_chisquare_result(p,colX,alpha)

        return column_name,value

    