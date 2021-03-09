
#* Importing Libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class EncodeClass:
    '''
        Encoding Related Functions.
    '''
    
    def label_encoding(self, series):

        labelencoder = LabelEncoder()

        series = labelencoder.fit_transform(series)
        
        return series
    
    def one_hot_encoding(self, series):
        
        df = pd.DataFrame(series)
        col_name = series.name
    
        enc = OneHotEncoder(handle_unknown='ignore')

        ohe_df = enc.fit_transform(df).toarray()
        enc_df = pd.DataFrame(ohe_df, columns = [f"{col_name}_{i}" for i in range(ohe_df.shape[1])])

        return enc_df

